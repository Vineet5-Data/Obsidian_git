"""Adaptive market layer: decide SELL quantities from live prices, not the tape.

v24 replays fixed sell quantities at fixed turns.  That is the part of the agent
most exposed to a shifting meta: when a rival floods milk (Seb) or the field
converges on our own route (mirrors), the tape keeps dumping into a crushed
market because it cannot see the price.

This replaces _impact_slots with a real policy.  The tape's SELL orders are
treated as *intent*, not instruction:

  * anything the tape wanted to sell but we held back accrues in a pending pool
  * each turn we sell greedily unit-by-unit while the marginal price clears a
    reserve, using the engine's own price curve
  * the reserve decays with the season so everything liquidates by the end
  * shed pressure force-sells before end-of-day overflow discards stock

Non-SELL orders (HIRE / BUY_LAND / BUY_SEED / BUY_ANIMAL / BUY_PRODUCT) pass
through untouched -- they drive the build and must stay on script.

Run:  python _mkt.py [mode ...]
"""
import glob
import importlib.util
import json
import os
import sys

LOSSES = r"C:\Users\Vinee\Desktop\Kaggriculture\recent _loss"
LOSSDIR = r"C:\Users\Vinee\Desktop\Kaggriculture\.loss"
SLOTS = 10


def fresh(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# --------------------------------------------------------------------------
# policy
# --------------------------------------------------------------------------
def make_policy(module, params):
    """Return a drop-in replacement for _impact_slots."""
    state = {}

    def reserve(step, item):
        """Price floor we insist on, as a fraction of the item's base price."""
        base = float(module._MARKET_PARAMS[item][0])  # tuple: base is index 0
        progress = step / 719.0
        alpha = params["alpha0"] * max(0.0, 1.0 - progress / params["decay"])
        return alpha * base

    def policy(obs, action):
        seat = module._seat(obs)
        step = int(module._get(obs, "step", 0) or 0)
        st = state.get(seat)
        if st is None or step <= 0 or step < st["last"]:
            st = {"last": step, "pending": {}}
            state[seat] = st
        st["last"] = step

        market_obs = module._get(obs, "market", {}) or {}
        inventory = dict(module._get(market_obs, "inventory", {}) or {})
        private = module._get(obs, "private", {}) or {}
        shed = {k: max(0, int(v or 0))
                for k, v in dict(module._get(private, "shed", {}) or {}).items()}

        orders = list(action.get("market") or [])
        keep = [o for o in orders if not module._is_sell(o)]
        wanted = {}
        for order in orders:
            if module._is_sell(order):
                try:
                    wanted[order[1]] = wanted.get(order[1], 0) + max(0, int(order[2]))
                except (TypeError, ValueError):
                    pass
        for item, quantity in st["pending"].items():
            wanted[item] = wanted.get(item, 0) + quantity

        # Do NOT clamp to the observed shed.  The observation predates this
        # turn's DROP and this route harvests-drops-sells in one turn, so the
        # reading is ~0 exactly when the tape is about to sell.  The engine
        # skips units we do not hold, so over-asking costs nothing.
        intent = {item: q for item, q in wanted.items() if q > 0}

        shed_used = sum(shed.values())
        pressure = shed_used >= params["pressure"]
        endgame = step >= params["hard_sell_step"]

        decided = {}
        for item, want in intent.items():
            if item not in module._MARKET_PARAMS:
                decided[item] = want
                continue
            floor = 0.0 if (endgame or pressure) else reserve(step, item)
            inv = int(inventory.get(item, 10000) or 0)
            sold = 0
            for _ in range(want):
                if module._market_price(item, inv + sold) < floor:
                    break
                sold += 1
            if params["min_frac"]:
                sold = max(sold, int(want * params["min_frac"]))
            decided[item] = min(want, sold)

        # carry the remainder forward, bounded so intent cannot run away
        st["pending"] = {}
        if not endgame:
            for item, want in intent.items():
                held = min(want - decided.get(item, 0), params["max_hold"])
                if held > 0:
                    st["pending"][item] = held

        sells = [["SELL", item, q] for item, q in decided.items() if q > 0]
        # the engine matches orders by slot index: protect the biggest first
        sells.sort(key=lambda o: -module._impact_score(obs, o))
        room = max(0, SLOTS - len(keep))
        action["market"] = (sells[:room] + keep)[:SLOTS]
        return action

    return policy


PRESETS = {
    "baseline":  None,
    "patient":   {"alpha0": 0.90, "decay": 0.85, "pressure": 70,
                  "hard_sell_step": 660, "min_frac": 0.0, "max_hold": 40},
    "mild":      {"alpha0": 0.55, "decay": 0.85, "pressure": 70,
                  "hard_sell_step": 660, "min_frac": 0.0, "max_hold": 40},
    "gentle":    {"alpha0": 0.35, "decay": 0.90, "pressure": 80,
                  "hard_sell_step": 640, "min_frac": 0.0, "max_hold": 30},
    "tiny":      {"alpha0": 0.15, "decay": 0.95, "pressure": 85,
                  "hard_sell_step": 620, "min_frac": 0.0, "max_hold": 20},
    "halfhold":  {"alpha0": 0.55, "decay": 0.85, "pressure": 70,
                  "hard_sell_step": 660, "min_frac": 0.5, "max_hold": 40},
    "passthru":  {"alpha0": 0.0, "decay": 1.0, "pressure": 999,
                  "hard_sell_step": 720, "min_frac": 0.0, "max_hold": 0},
}


def episodes():
    out = []
    for path in sorted(glob.glob(os.path.join(LOSSES, "*.json"))):
        episode = os.path.splitext(os.path.basename(path))[0]
        with open(path, encoding="utf-8") as handle:
            replay = json.load(handle)
        info = replay.get("info") or {}
        names = info.get("TeamNames") or ["p0", "p1"]
        seat = 0 if "vineet" in names[0].lower() else 1
        out.append({"episode": episode, "seat": seat, "seed": info.get("seed"),
                    "opp": os.path.join(LOSSDIR, f"o_{episode}.py")})
    return out


def build(mode, tag):
    module = fresh("v24.py", "p_" + tag)
    params = PRESETS[mode]
    if params is not None:
        module._impact_slots = make_policy(module, params)
    return module.agent


def main():
    from kaggle_environments import make
    modes = sys.argv[1:] or list(PRESETS)
    eps = episodes()
    opponents = {e["episode"]: fresh(e["opp"], "o_" + e["episode"]).agent
                 for e in eps}
    print(f"{'mode':10s} " + " ".join(f"{e['episode'][-5:]:>8}" for e in eps)
          + f" {'total':>9} {'W':>2}")
    for mode in modes:
        margins = []
        for e in eps:
            agent = build(mode, f"{mode}_{e['episode']}")
            config = {"episodeSteps": 720}
            if e["seed"] is not None:
                config["seed"] = e["seed"]
            pair = [agent, opponents[e["episode"]]]
            if e["seat"] == 1:
                pair = pair[::-1]
            env = make("kaggriculture", configuration=config)
            env.run(pair)
            final = env.steps[-1]
            margins.append(final[e["seat"]].reward - final[1 - e["seat"]].reward)
        print(f"{mode:10s} " + " ".join(f"{m:>+8,.0f}" for m in margins)
              + f" {sum(margins):>+9,.0f} {sum(1 for m in margins if m > 0):>2}",
              flush=True)


if __name__ == "__main__":
    main()
