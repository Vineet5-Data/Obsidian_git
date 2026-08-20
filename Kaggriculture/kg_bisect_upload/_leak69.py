"""Measure end-of-day shed overflow loss.

Engine `_drop_inventories_to_shed` (kaggriculture.py:830) force-drains every
worker inventory into the shed at day end and DISCARDS whatever does not fit
(`del inv[item]` runs even when `take == 0`).  An agent that deliberately keeps
stock on a worker because the shed is full is not carrying it over -- it is
throwing it away.  Wrap the engine function and count what vanishes.

Usage:  python _leak69.py v46_a.py
"""
import importlib.util
import sys

from kaggle_environments import make
from kaggle_environments.envs.kaggriculture import kaggriculture as K

lost = {}
peak = [0]
_orig = K._drop_inventories_to_shed


def counting_drop(private, capacity):
    before = {}
    for inv in private["inventories"]:
        for item, n in inv.items():
            if n > 0:
                before[item] = before.get(item, 0) + n
    shed_before = sum(private["shed"].values())
    _orig(private, capacity)
    shed_after = sum(private["shed"].values())
    peak[0] = max(peak[0], shed_after)
    banked = shed_after - shed_before
    dropped = sum(before.values()) - banked
    if dropped > 0:
        # attribute the loss coarsely: the shed was full, so everything the
        # workers held past `room` died regardless of which item it was
        for item, n in before.items():
            lost[item] = lost.get(item, 0) + n
        lost["__units__"] = lost.get("__units__", 0) + dropped


K._drop_inventories_to_shed = counting_drop


def load(path):
    spec = importlib.util.spec_from_file_location(path.replace(".", "_"), path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "v46_a.py"
    m = load(path)

    def raw(obs, config=None):
        return m._plan(obs)

    env = make("kaggriculture",
               configuration={"episodeSteps": 720, "seed": 101})
    env.run([raw, raw])
    print(f"{path}: score {int(env.steps[-1][0].reward):,}  "
          f"peak shed {peak[0]}/100  "
          f"units discarded at day end {lost.get('__units__', 0)}")
    if lost:
        detail = {k: v for k, v in lost.items() if k != "__units__"}
        print("  worker-held items on overflow days:", detail)
