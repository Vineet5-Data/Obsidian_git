"""Rival-supply identification + net-recovery selling.

The two matchups that beat us (Seb's milk flood 6-42, the Leon mirror 0-48) are
both supply-flooding problems.  A tape cannot see flooding.  An estimator can.

IDENTIFICATION
--------------
Market inventory is observable, and the town's drain is exactly computable from
the engine's own schedule (shops every 4 steps, centre every 12, multipliers
known).  Our own submitted sells are known.  So the rival's sales fall out of an
accounting identity, with no assumption about their farm:

    inv[t] - inv[t-1] = ours[t-1] + rival[t-1] - drain[t-1]
    =>  rival[t-1] = inv[t] - inv[t-1] - ours[t-1] + drain[t-1]

Smooth that with an EWMA and you have a live estimate of how fast the opponent
is dumping each product.

DECISION
--------
Holding stock only pays if the price rebuilds before we sell.  The price
rebuilds at rate (drain - rival_supply).  So:

    net(item) = drain(item) - rival_rate(item)
    hold  <=>  net > 0  AND  price is currently depressed

Against a flooder net goes negative and the rule dumps immediately; against a
quiet market net is positive and it waits.  Uniform patience measured -1,768 to
-2,629 precisely because it ignored this term.

Run:  python _adapt.py [mode ...]
"""
import glob
import importlib.util
import json
import os
import sys

LOSSES = r"C:\Users\Vinee\Desktop\Kaggriculture\recent _loss"
LOSSDIR = r"C:\Users\Vinee\Desktop\Kaggriculture\.loss"
SLOTS = 10

SHOPS = {
    "BAKERY":         ["EGG", "WHEAT"],
    "PIZZA_SHOP":     ["MILK", "TOMATO", "WHEAT"],
    "BRUNCH_SPOT":    ["EGG", "WHEAT", "STRAWBERRY"],
    "YARN_STORE":     ["WOOL"],
    "ICE_CREAM_SHOP": ["STRAWBERRY", "MILK", "WHEAT"],
    "PET_CAFE":       ["CARROT"],
    "SMOOTHIE_SHOP":  ["STRAWBERRY", "MILK"],
    "FARMERS_MARKET": ["WHEAT", "CARROT", "TOMATO", "STRAWBERRY"],
}


def fresh(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def drain_at(module, obs, step, item):
    """Exact units removed by the town at `step` (engine schedule)."""
    total = 0
    if step % 4 == 0:
        town = module._get(obs, "town", {}) or {}
        for name in list(module._get(town, "unlocked_shops", []) or []):
            products = SHOPS.get(name)
            if products and item in products:
                total += 2 if len(products) == 1 else 1
    if step % 12 == 0 and item != "FERTILIZER":
        day = int(module._get(obs, "day", 0) or 0)
        total += 4 if day >= 20 else 2 if day >= 10 else 1
    return total


def drain_rate(module, obs, item):
    """Forward-looking per-turn drain at the current unlock state."""
    town = module._get(obs, "town", {}) or {}
    per_interval = 0
    for name in list(module._get(town, "unlocked_shops", []) or []):
        products = SHOPS.get(name)
        if products and item in products:
            per_interval += 2 if len(products) == 1 else 1
    rate = per_interval / 4.0
    if item != "FERTILIZER":
        day = int(module._get(obs, "day", 0) or 0)
        rate += (4 if day >= 20 else 2 if day >= 10 else 1) / 12.0
    return rate


def make_policy(module, params):
    state = {}

    def policy(obs, action):
        seat = module._seat(obs)
        step = int(module._get(obs, "step", 0) or 0)
        st = state.get(seat)
        if st is None or step <= 0 or step < st.get("last", 0):
            st = {"last": step, "pending": {}, "prev_inv": None,
                  "ours": {}, "rival": {}}
            state[seat] = st
        st["last"] = step

        market_obs = module._get(obs, "market", {}) or {}
        inventory = {k: int(v or 0) for k, v in
                     dict(module._get(market_obs, "inventory", {}) or {}).items()}

        # ---- identify rival supply from the accounting identity ----
        if st["prev_inv"] is not None:
            alpha = params["ewma"]
            for item, now in inventory.items():
                before = st["prev_inv"].get(item, now)
                drained = drain_at(module, obs, max(0, step - 1), item)
                added = now - before + drained
                rival = max(0.0, added - st["ours"].get(item, 0))
                prior = st["rival"].get(item, 0.0)
                st["rival"][item] = alpha * rival + (1 - alpha) * prior
        st["prev_inv"] = dict(inventory)

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

        endgame = step >= params["hard_sell_step"]
        decided, st["pending"] = {}, {}

        for item, want in wanted.items():
            if want <= 0:
                continue
            if item not in module._MARKET_PARAMS or endgame:
                decided[item] = want
                continue
            net = drain_rate(module, obs, item) - st["rival"].get(item, 0.0)
            inv = inventory.get(item, 10000)
            price = float(module._market_price(item, inv))
            base = float(module._MARKET_PARAMS[item][0])
            if (params["hold"] and net > params["net_min"]
                    and price < params["hold_ratio"] * base):
                keep_back = min(int(want * params["hold_frac"]), params["max_hold"])
                if keep_back > 0:
                    st["pending"][item] = keep_back
                    want -= keep_back
            decided[item] = want

        sells = [["SELL", item, q] for item, q in decided.items() if q > 0]
        st["ours"] = {item: q for item, q in decided.items()}

        sells.sort(key=lambda o: -module._impact_score(obs, o))
        room = max(0, SLOTS - len(keep))
        action["market"] = (sells[:room] + keep)[:SLOTS]
        return action

    return policy


PRESETS = {
    "baseline": None,
    "net":      {"hold": 1, "ewma": 0.25, "net_min": 0.0, "hold_ratio": 1.6,
                 "hold_frac": 0.5, "max_hold": 25, "hard_sell_step": 660},
    "net_str":  {"hold": 1, "ewma": 0.25, "net_min": 0.3, "hold_ratio": 2.0,
                 "hold_frac": 0.6, "max_hold": 35, "hard_sell_step": 660},
    "net_slow": {"hold": 1, "ewma": 0.10, "net_min": 0.0, "hold_ratio": 1.6,
                 "hold_frac": 0.5, "max_hold": 25, "hard_sell_step": 660},
    "net_wide": {"hold": 1, "ewma": 0.25, "net_min": -0.5, "hold_ratio": 1.6,
                 "hold_frac": 0.5, "max_hold": 25, "hard_sell_step": 660},
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


def build(mode, tag, base="v26.py"):
    module = fresh(base, "a_" + tag)
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
    print(f"{'mode':11s} " + " ".join(f"{e['episode'][-5:]:>8}" for e in eps)
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
        print(f"{mode:11s} " + " ".join(f"{m:>+8,.0f}" for m in margins)
              + f" {sum(margins):>+9,.0f} {sum(1 for m in margins if m > 0):>2}",
              flush=True)


if __name__ == "__main__":
    main()
