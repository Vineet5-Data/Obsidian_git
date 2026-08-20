"""Idle-hand job priority sweep on the four reproduced ladder losses.

v24 ships USE_IDLE=0 because an earlier idle layer measured -519 -- but that was
on arbitrary seeds, and the job order it used (fertilizer first, harvest before
care) is backwards for value and creates orphan field inventory.

Ranked by what a unit-turn is actually worth:
  CARE   -> +1 product on next production (milk 193 / wool 241)
  WATER  -> +1 yield unit on a one-time crop in its bonus window
  FEED   -> keeps production alive, but eats wheat the script may need
  HARVEST/COLLECT_FERTILIZER -> fill a unit inventory the tape may never DROP
"""
import glob
import importlib.util
import json
import os
import sys

from kaggle_environments import make

LOSSES = r"C:\Users\Vinee\Desktop\Kaggriculture\recent _loss"
LOSSDIR = r"C:\Users\Vinee\Desktop\Kaggriculture\.loss"


def fresh(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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


def make_job(mode):
    """Return an _idle_job replacement for the given priority policy."""
    def job(tile, inventory):
        animal = bool(tile.get("animal"))
        fed = bool(tile.get("fed_today"))
        cared = bool(tile.get("cared_today"))
        have_wheat = int((inventory or {}).get("WHEAT", 0) or 0) > 0
        if animal:
            if mode in ("care", "care_water", "care_feed", "care_fert"):
                if fed and not cared:
                    return ["CARE"]
                if mode in ("care_feed", "care_fert") and not fed and have_wheat:
                    return ["FEED"]
                if mode == "care_fert" and tile.get("fertilizer_available"):
                    return ["COLLECT_FERTILIZER"]
                return None
            if mode == "all":  # v24's original ordering
                if tile.get("fertilizer_available"):
                    return ["COLLECT_FERTILIZER"]
                if not fed and have_wheat:
                    return ["FEED"]
                if int(tile.get("yield_units", 0) or 0) > 0:
                    return ["HARVEST"]
                if fed and not cared:
                    return ["CARE"]
            return None
        if mode == "care":
            return None
        if (tile.get("kind") == "PLANT" and tile.get("crop")
                and not tile.get("watered_today")):
            return ["WATER"]
        return None
    return job


def build(mode, tag):
    module = fresh("v24.py", "c_" + tag)
    if mode == "off":
        module.USE_IDLE = 0
    else:
        module.USE_IDLE = 1
        module._idle_job = make_job(mode)
    return module.agent


def main():
    modes = sys.argv[1:] or ["off", "all", "care", "care_water", "care_feed",
                             "care_fert"]
    eps = episodes()
    opponents = {e["episode"]: fresh(e["opp"], "o_" + e["episode"]).agent
                 for e in eps}
    print(f"{'mode':12s} " + " ".join(f"{e['episode'][-5:]:>8}" for e in eps)
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
        print(f"{mode:12s} " + " ".join(f"{m:>+8,.0f}" for m in margins)
              + f" {sum(margins):>+9,.0f} {sum(1 for m in margins if m > 0):>2}",
              flush=True)


if __name__ == "__main__":
    main()
