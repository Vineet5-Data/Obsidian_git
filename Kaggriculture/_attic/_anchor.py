"""Adaptive barbell: wheat anchor sized by live premium-market health.

The fixed-size sweep found a clean minimax frontier -- a small anchor is free at
baseline but barely helps in a shock, a large anchor halves the shock loss but
costs 1,697 at baseline.  Robust-portfolio theory says the size should not be
fixed: hold premium exposure inversely to observed pressure in those markets.

Health index, computed live every turn from the shared market:

    H = mean over {STRAWBERRY, MILK, WOOL, MELON} of  price(item) / base(item)

H >= HI  -> premium markets healthy, run a minimal anchor (keep baseline EV)
H <= LO  -> premium markets depressed, run the full anchor (buy protection)
between -> linear interpolation

Nothing here is copied from a replay: H is a function of market state, so the
agent re-sizes itself as the meta moves.  That is the property a tape cannot
have.
"""
import importlib.util
import multiprocessing as mp
import os
import statistics
import sys

BASE = "v26.py"
PREMIUM = ("STRAWBERRY", "MILK", "WOOL", "MELON")

PRESETS = {
    "off": None,
    "fixed_big": {"adaptive": 0, "alpha": 0.03, "buy_band": 0.95,
                  "sell_band": 1.05, "lot": 14, "max_pos": 60,
                  "cash_floor": 800, "shed_headroom": 60},
    "adaptive": {"adaptive": 1, "alpha": 0.03, "buy_band": 0.95,
                 "sell_band": 1.05, "lot_lo": 4, "lot_hi": 14,
                 "pos_lo": 12, "pos_hi": 60, "cash_floor": 800,
                 "shed_headroom": 60, "hi": 1.00, "lo": 0.70},
    "adaptive_kn": {"adaptive": 1, "alpha": 0.03, "buy_band": 0.95,
                    "sell_band": 1.05, "lot_lo": 6, "lot_hi": 18,
                    "pos_lo": 16, "pos_hi": 80, "cash_floor": 800,
                    "shed_headroom": 70, "hi": 1.05, "lo": 0.75},
}

REGIMES = {
    "baseline": {},
    "premium_bear": {"STRAWBERRY": {"base": 72}, "MILK": {"base": 96},
                     "WOOL": {"base": 120}, "MELON": {"base": 150}},
    "steep_glut": {"STRAWBERRY": {"above_target": 3.2},
                   "MILK": {"above_target": 3.2},
                   "WOOL": {"above_target": 6.4},
                   "MELON": {"above_target": 7.2}},
}
START, STOP = 48, 690


def fresh(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def anchor_agent(preset, tag):
    module = fresh(BASE, "k_" + tag)
    inner = module.agent
    P = PRESETS[preset]
    state = {}

    def health(obs):
        market = module._get(obs, "market", {}) or {}
        inventory = module._get(market, "inventory", {}) or {}
        ratios = []
        for item in PREMIUM:
            params = module._MARKET_PARAMS.get(item)
            if not params:
                continue
            inv = int(module._get(inventory, item, 10000) or 0)
            ratios.append(module._market_price(item, inv) / float(params[0]))
        return sum(ratios) / len(ratios) if ratios else 1.0

    def agent(obs):
        action = inner(obs)
        if P is None:
            return action
        try:
            seat = module._seat(obs)
            step = int(module._get(obs, "step", 0) or 0)
            st = state.get(seat)
            if st is None or step <= 0 or step < st["last"]:
                st = {"last": step, "ewma": None, "pos": 0}
                state[seat] = st
            st["last"] = step

            market = module._get(obs, "market", {}) or {}
            inv = int(module._get(module._get(market, "inventory", {}) or {},
                                  "WHEAT", 10000) or 0)
            price = float(module._market_price("WHEAT", inv))
            st["ewma"] = price if st["ewma"] is None else (
                P["alpha"] * price + (1 - P["alpha"]) * st["ewma"])
            if not (START <= step < STOP):
                return action

            if P["adaptive"]:
                H = health(obs)
                span = max(1e-6, P["hi"] - P["lo"])
                weight = min(1.0, max(0.0, (P["hi"] - H) / span))
                lot = int(round(P["lot_lo"] + weight * (P["lot_hi"] - P["lot_lo"])))
                max_pos = int(round(P["pos_lo"] + weight * (P["pos_hi"] - P["pos_lo"])))
            else:
                lot, max_pos = P["lot"], P["max_pos"]

            farm = module._farm(obs)
            money = float(module._get(farm, "money", 0) or 0)
            private = module._get(obs, "private", {}) or {}
            shed = {k: max(0, int(v or 0)) for k, v in
                    dict(module._get(private, "shed", {}) or {}).items()}
            shed_used = sum(shed.values())
            orders = list(action.get("market") or [])
            if len(orders) >= 10:
                return action
            if any(o and len(o) >= 2 and o[1] == "WHEAT"
                   and o[0] in ("SELL", "BUY_PRODUCT") for o in orders):
                return action

            if price <= P["buy_band"] * st["ewma"]:
                room = min(lot, max_pos - st["pos"],
                           P["shed_headroom"] - shed_used,
                           int((money - P["cash_floor"]) // max(1.0, price)))
                if room > 0:
                    orders.append(["BUY_PRODUCT", "WHEAT", room])
                    st["pos"] += room
            elif price >= P["sell_band"] * st["ewma"] and st["pos"] > 0:
                quantity = min(lot, st["pos"], shed.get("WHEAT", 0))
                if quantity > 0:
                    orders.append(["SELL", "WHEAT", quantity])
                    st["pos"] -= quantity
            action["market"] = orders[:10]
        except Exception:
            pass
        return action

    return agent


def one(job):
    preset, regime, opponent_path, seed, seat = job
    from kaggle_environments import make
    agent = anchor_agent(preset, f"{preset}_{seed}_{seat}")
    opponent = fresh(opponent_path, f"o_{seed}_{seat}").agent
    pair = [agent, opponent] if seat == 0 else [opponent, agent]
    env = make("kaggriculture",
               configuration={"episodeSteps": 720, "seed": seed,
                              "marketParams": REGIMES[regime]})
    env.run(pair)
    final = env.steps[-1]
    return (preset, regime), final[seat].reward - final[1 - seat].reward


def main():
    opponent = sys.argv[1] if len(sys.argv) > 1 else ".loss/o_90711580.py"
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, n + 1)]
    jobs = [(p, r, opponent, s, seat)
            for r in REGIMES for p in PRESETS for s in seeds for seat in (0, 1)]
    with mp.Pool(max(1, (os.cpu_count() or 4) - 2)) as pool:
        results = pool.map(one, jobs)
    table = {}
    for key, margin in results:
        table.setdefault(key, []).append(margin)
    print(f"adaptive anchor vs {os.path.basename(opponent)} "
          f"({n} seeds x 2 seats)\n")
    for regime in REGIMES:
        print(f"-- {regime} --")
        for preset in PRESETS:
            margins = table.get((preset, regime), [])
            if not margins:
                continue
            w = sum(1 for m in margins if m > 0)
            tag = "  <= control" if preset == "off" else ""
            print(f"  {preset:13s} {f'{w}-{len(margins) - w}':>7} "
                  f"{100 * w / len(margins):>5.1f}% "
                  f"{statistics.mean(margins):>+9,.0f} "
                  f"{min(margins):>+9,.0f}{tag}")
        print()


if __name__ == "__main__":
    mp.freeze_support()
    main()
