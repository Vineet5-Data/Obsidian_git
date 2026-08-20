"""How much value does our agent destroy by overflowing the 100-unit shed?

kaggriculture.py:831 `_drop_inventories_to_shed` silently DISCARDS anything
that will not fit at end of day, and :654 makes a full shed reject BUY_PRODUCT.
Both are invisible in the observation, so a leak here never shows up as a bug --
only as a lower final score.

This wraps the engine's own functions and counts what the engine threw away,
valued at the market price prevailing at that moment.

Usage:  python _shedleak.py v46_a.py [seed ...]
"""
import importlib.util
import sys
from collections import Counter

import kaggle_environments.envs.kaggriculture.kaggriculture as K

DISCARD = Counter()      # item -> units deleted at end of day
FULLDAYS = Counter()     # seat -> nights the shed was already at capacity
_orig_drop = K._drop_inventories_to_shed


def _counting_drop(private, capacity):
    """Same call the engine makes, but diff the books before and after."""
    before_shed = sum(private["shed"].values())
    before_inv = Counter()
    for inv in private["inventories"]:
        for item, n in inv.items():
            if n > 0:
                before_inv[item] += n
    _orig_drop(private, capacity)
    after_shed = sum(private["shed"].values())
    banked = after_shed - before_shed
    carried = sum(before_inv.values())
    lost = carried - banked
    if lost > 0:
        # attribute proportionally; exact per-item split needs engine order,
        # and the total is what matters for sizing the leak
        for item, n in before_inv.items():
            DISCARD[item] += lost * n / carried
    if after_shed >= capacity:
        FULLDAYS["nights_at_cap"] += 1


K._drop_inventories_to_shed = _counting_drop


def load(path):
    spec = importlib.util.spec_from_file_location("cand", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.agent


if __name__ == "__main__":
    from kaggle_environments import make

    path = sys.argv[1] if len(sys.argv) > 1 else "v46_a.py"
    seeds = [int(s) for s in sys.argv[2:]] or [101, 202, 303]
    ag = load(path)

    for seed in seeds:
        DISCARD.clear()
        FULLDAYS.clear()
        env = make("kaggriculture",
                   configuration={"episodeSteps": 720, "seed": seed})
        env.run([ag, ag])
        score = int(env.steps[-1][0].reward)
        prices = env.steps[-1][0]["observation"]["market"]["prices"]
        # both seats share the counter; halve to get per-farm figures
        units = sum(DISCARD.values()) / 2.0
        value = sum(n * prices.get(i, 0) for i, n in DISCARD.items()) / 2.0
        print(f"seed {seed:>4}  score {score:>8,}  "
              f"discarded {units:>7.1f} units  ~{value:>9,.0f} money  "
              f"({100.0 * value / max(score, 1):>5.1f}% of score)  "
              f"nights_at_cap {FULLDAYS['nights_at_cap'] / 2.0:>4.1f}/30")
        if units > 0:
            top = sorted(DISCARD.items(), key=lambda kv: -kv[1])[:4]
            print("        top losses:",
                  {k: round(v / 2.0, 1) for k, v in top})
