"""Barbell anchor: mean-reversion market-making in WHEAT.

Where this comes from.  The robust-portfolio reading (Ben-Tal & Nemirovski
minimax under an adversary-controlled parameter) says: hold a low-glut staple
anchor sized to survive a premium shock, and size premium exposure inversely to
observed rival pressure.  Our measured failure is exactly the missing anchor --
premium goods are ~87% of revenue, and when all premium bases drop 40% we go
0-16.

WHEAT is the only anchor available:
  * glut 1.00 -- the sole market where seasonal drain equals total supply
  * the heaviest drain in the game (5 shops + town centre, ~1.5 units/turn)
  * the ONLY product besides FERTILIZER that BUY_PRODUCT will sell back to us

Why this is not free-money nonsense: the engine deliberately quotes BUY_PRODUCT
at post-buy inventory "so a buy/sell round-trip against an unchanged market nets
zero."  The edge is not the spread, it is the DRAIN -- between our buy and our
sell the town removes wheat, inventory falls, price rises.  We are being paid to
warehouse the one good the town actually wants.  Positive expectation is funded
by scripted demand, not by the opponent.

Everything is computed live (EWMA of the wheat price, current inventory, shed
headroom), so it re-prices itself if the meta moves.  Tape-safe: only market
orders, no unit ops, no positional state.

Usage:  python _wheat.py [opponent.py] [n_seeds] [regime]
"""
import importlib.util
import multiprocessing as mp
import os
import statistics
import sys

BASE = "v26.py"

PRESETS = {
    "off":     None,
    "tight":   {"alpha": 0.05, "buy_band": 0.97, "sell_band": 1.03,
                "lot": 6, "max_pos": 24, "cash_floor": 1500,
                "start": 48, "stop": 690, "shed_headroom": 45},
    "wide":    {"alpha": 0.05, "buy_band": 0.92, "sell_band": 1.08,
                "lot": 10, "max_pos": 40, "cash_floor": 1500,
                "start": 48, "stop": 690, "shed_headroom": 45},
    "big":     {"alpha": 0.03, "buy_band": 0.95, "sell_band": 1.05,
                "lot": 14, "max_pos": 60, "cash_floor": 800,
                "start": 48, "stop": 690, "shed_headroom": 60},
    "greedy":  {"alpha": 0.08, "buy_band": 1.00, "sell_band": 1.00,
                "lot": 10, "max_pos": 40, "cash_floor": 1500,
                "start": 48, "stop": 690, "shed_headroom": 45},
}

REGIMES = {
    "baseline": {},
    "premium_bear": {"STRAWBERRY": {"base": 72}, "MILK": {"base": 96},
                     "WOOL": {"base": 120}, "MELON": {"base": 150}},
}


def fresh(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def wheat_agent(preset, tag):
    module = fresh(BASE, "w_" + tag)
    inner = module.agent
    P = PRESETS[preset]
    state = {}

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
            inventory = int(module._get(
                module._get(market, "inventory", {}) or {}, "WHEAT", 10000) or 0)
            price = float(module._market_price("WHEAT", inventory))
            st["ewma"] = price if st["ewma"] is None else (
                P["alpha"] * price + (1 - P["alpha"]) * st["ewma"])
            reference = st["ewma"]

            if not (P["start"] <= step < P["stop"]):
                return action
            farm = module._farm(obs)
            money = float(module._get(farm, "money", 0) or 0)
            private = module._get(obs, "private", {}) or {}
            shed = {k: max(0, int(v or 0)) for k, v in
                    dict(module._get(private, "shed", {}) or {}).items()}
            shed_used = sum(shed.values())
            orders = list(action.get("market") or [])
            if len(orders) >= 10:
                return action
            # never fight our own scripted wheat orders
            if any(o and len(o) >= 2 and o[1] == "WHEAT"
                   and o[0] in ("SELL", "BUY_PRODUCT") for o in orders):
                return action

            if price <= P["buy_band"] * reference:
                room = min(P["lot"], P["max_pos"] - st["pos"],
                           P["shed_headroom"] - shed_used,
                           int((money - P["cash_floor"]) // max(1.0, price)))
                if room > 0:
                    orders.append(["BUY_PRODUCT", "WHEAT", room])
                    st["pos"] += room
            elif price >= P["sell_band"] * reference and st["pos"] > 0:
                quantity = min(P["lot"], st["pos"], shed.get("WHEAT", 0))
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
    agent = wheat_agent(preset, f"{preset}_{seed}_{seat}")
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
    print(f"wheat anchor vs {os.path.basename(opponent)}  "
          f"({n} seeds x 2 seats)\n")
    for regime in REGIMES:
        print(f"-- regime: {regime} --")
        print(f"{'preset':9s} {'W-L':>8} {'win%':>6} {'mean':>9} {'worst':>9}")
        for preset in PRESETS:
            margins = table.get((preset, regime), [])
            if not margins:
                continue
            w = sum(1 for m in margins if m > 0)
            tag = "  <= control" if preset == "off" else ""
            print(f"{preset:9s} {f'{w}-{len(margins) - w}':>8} "
                  f"{100 * w / len(margins):>5.1f}% "
                  f"{statistics.mean(margins):>+9,.0f} {min(margins):>+9,.0f}{tag}")
        print()


if __name__ == "__main__":
    mp.freeze_support()
    main()
