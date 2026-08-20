"""Functional market strategies derived from the engine's demand model.

Not a clone: every number below is computed from live observation state
(unlocked shops, day, market inventory, prices), so if the meta shifts -- more
melon farmers, a wool rush, a different shop draw -- the rule re-prioritises
itself instead of replaying a tape.

Econometric basis, read straight out of the engine:

  SHOPS consume `multiplier` of each listed product every townShopSellInterval
  (4) steps, multiplier = 2 for single-product shops.  The town centre consumes
  center_mult of every non-FERTILIZER product every townCenterSellInterval (12)
  steps, center_mult stepping 1 -> 2 -> 4 at days 10 and 20.

  => per-turn drain d(item) = shop_rate + centre_rate, both known live.

Two regimes follow:

  d(item) ~ 0   (FERTILIZER: no shop, excluded from town centre; MELON: no shop)
      The price never recovers.  Total revenue available to BOTH players is a
      fixed integral of the price curve.  It is a race: sell first, sell now.

  d(item) large (WHEAT: 5 shops, drain == total supply)
      Price rebuilds between turns.  Holding is genuinely profitable here, and
      only here.  A uniform reserve across all products loses money because it
      also holds the zero-drain goods -- measured: -1,768 to -2,629.

Run:  python _strat.py [mode ...]
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
SHOP_INTERVAL = 4.0
CENTER_INTERVAL = 12.0


def fresh(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def drain_rate(module, obs, item):
    """Units of `item` the town removes per turn, at the CURRENT unlock state."""
    town = module._get(obs, "town", {}) or {}
    unlocked = list(module._get(town, "unlocked_shops", []) or [])
    per_interval = 0
    for name in unlocked:
        products = SHOPS.get(name)
        if products and item in products:
            per_interval += 2 if len(products) == 1 else 1
    rate = per_interval / SHOP_INTERVAL
    if item != "FERTILIZER":
        day = int(module._get(obs, "day", 0) or 0)
        center_mult = 4 if day >= 20 else 2 if day >= 10 else 1
        rate += center_mult / CENTER_INTERVAL
    return rate


def make_strategy(module, params):
    state = {}

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
            d = drain_rate(module, obs, item)
            # Patience only where the market actually rebuilds.
            if params["hold"] and d >= params["hold_drain_min"]:
                inv = int(inventory.get(item, 10000) or 0)
                price = float(module._market_price(item, inv))
                base = float(module._MARKET_PARAMS[item][0])
                if price < params["hold_ratio"] * base:
                    keep_back = min(int(want * params["hold_frac"]),
                                    params["max_hold"])
                    if keep_back > 0:
                        st["pending"][item] = keep_back
                        want -= keep_back
            decided[item] = want

        sells = [["SELL", item, q] for item, q in decided.items() if q > 0]

        def priority(order):
            item, quantity = order[1], int(order[2])
            inv = int(inventory.get(item, 10000) or 0)
            price = float(module._market_price(item, inv))
            later = float(module._market_price(item, inv + quantity))
            impact = quantity * max(0.0, price - later)
            if params["race"]:
                # zero-drain goods are a bounded pot: being second is permanent
                urgency = 1.0 / (1.0 + params["race_k"] * drain_rate(module, obs, item))
                return impact * urgency + quantity * price * params["rev_w"]
            return impact

        sells.sort(key=priority, reverse=True)
        room = max(0, SLOTS - len(keep))
        action["market"] = (sells[:room] + keep)[:SLOTS]
        return action

    return policy


PRESETS = {
    "baseline":   None,
    "race":       {"race": 1, "race_k": 2.0, "rev_w": 0.0, "hold": 0,
                   "hold_drain_min": 1.0, "hold_ratio": 1.0, "hold_frac": 0.0,
                   "max_hold": 0, "hard_sell_step": 700},
    "race_hi":    {"race": 1, "race_k": 6.0, "rev_w": 0.0, "hold": 0,
                   "hold_drain_min": 1.0, "hold_ratio": 1.0, "hold_frac": 0.0,
                   "max_hold": 0, "hard_sell_step": 700},
    "wheathold":  {"race": 0, "race_k": 0.0, "rev_w": 0.0, "hold": 1,
                   "hold_drain_min": 1.0, "hold_ratio": 1.6, "hold_frac": 0.5,
                   "max_hold": 25, "hard_sell_step": 660},
    "both":       {"race": 1, "race_k": 2.0, "rev_w": 0.0, "hold": 1,
                   "hold_drain_min": 1.0, "hold_ratio": 1.6, "hold_frac": 0.5,
                   "max_hold": 25, "hard_sell_step": 660},
    "both_rev":   {"race": 1, "race_k": 2.0, "rev_w": 0.01, "hold": 1,
                   "hold_drain_min": 1.0, "hold_ratio": 1.6, "hold_frac": 0.5,
                   "max_hold": 25, "hard_sell_step": 660},
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
    module = fresh(base, "s_" + tag)
    params = PRESETS[mode]
    if params is not None:
        module._impact_slots = make_strategy(module, params)
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
