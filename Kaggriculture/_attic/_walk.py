"""How much does our own bulk selling cost us in price walk-down?

For every SELL we post in a loss episode, price the order two ways:
  * realised  - unit by unit against rising inventory (what the engine does)
  * frozen    - every unit at the first unit's price (perfect smoothing bound)

The gap is the theoretical prize for spreading sells over more turns.  It is an
upper bound: real smoothing only recovers the part the town shops drain back
out between turns.
"""
import collections
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kaggle_environments.envs.kaggriculture.kaggriculture as E

LOSSES = r"C:\Users\Vinee\Desktop\Kaggriculture\recent _loss"


def main():
    for path in sorted(glob.glob(os.path.join(LOSSES, "*.json"))):
        with open(path, encoding="utf-8") as handle:
            replay = json.load(handle)
        steps = replay["steps"]
        names = (replay.get("info") or {}).get("TeamNames") or ["p0", "p1"]
        seat = 0 if "vineet" in names[0].lower() else 1

        loss = collections.Counter()
        realised = collections.Counter()
        biggest = []
        drain = collections.Counter()
        prev_inv = None

        for index, state in enumerate(steps[1:], start=0):
            obs = steps[index][0].get("observation", {})
            inv = dict((obs.get("market") or {}).get("inventory") or {})
            if prev_inv is not None:
                for item, value in inv.items():
                    delta = value - prev_inv.get(item, value)
                    if delta < 0:
                        drain[item] += -delta
            action = state[seat].get("action") or {}
            # price each of our orders against a local copy of inventory
            local = dict(inv)
            for order in (action.get("market") or []):
                if not order or order[0] != "SELL" or len(order) < 3:
                    continue
                item, n = order[1], int(order[2])
                if item not in E.MARKET_PARAMS:
                    continue
                first = E.market_price(item, local.get(item, 0))
                got = 0
                for _ in range(n):
                    got += E.market_price(item, local.get(item, 0))
                    local[item] = local.get(item, 0) + 1
                frozen = first * n
                realised[item] += got
                loss[item] += frozen - got
                if frozen - got > 0:
                    biggest.append((frozen - got, index, item, n, first,
                                    got // max(1, n)))
            prev_inv = inv

        print("=" * 76)
        print(f"{os.path.basename(path)}  seat{seat} vs {names[1 - seat]}")
        print(f"  {'item':12s} {'realised':>10} {'walkdown':>10} {'%':>6}  "
              f"{'shop drain/ep':>13}")
        for item in sorted(loss, key=lambda k: -loss[k]):
            pct = 100 * loss[item] / max(1, realised[item] + loss[item])
            print(f"  {item:12s} {realised[item]:>10,} {loss[item]:>10,} "
                  f"{pct:>5.1f}%  {drain[item]:>13,}")
        print(f"  {'TOTAL':12s} {sum(realised.values()):>10,} "
              f"{sum(loss.values()):>10,}")
        print("  worst single orders (walkdown, step, item, qty, p_first->p_avg):")
        for row in sorted(biggest, reverse=True)[:6]:
            print(f"    -{row[0]:>6,}  step {row[1]:>3}  {row[2]:12s} "
                  f"n={row[3]:>3}  {row[4]:>4} -> {row[5]:>4}")


if __name__ == "__main__":
    main()
