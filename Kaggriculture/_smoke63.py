"""Smoke a candidate WITHOUT the agent() try/except safety net.

agent() catches every exception and returns a degenerate fallback, so a broken
_plan still produces a legal episode and a plausible-looking score.  That would
make a panel run measure the fallback instead of the change.  Call _plan raw so
any exception surfaces as a traceback here.

Usage:  python _smoke63.py v63_a.py v63_b.py v62_unbeatable.py
"""
import importlib.util
import sys

from kaggle_environments import make


def load(path):
    spec = importlib.util.spec_from_file_location(path.replace(".", "_"), path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


if __name__ == "__main__":
    for path in sys.argv[1:]:
        m = load(path)
        calls = [0]

        def raw(obs, config=None, _m=m, _c=calls):
            _c[0] += 1
            return _m._plan(obs)          # no try/except: let it blow up

        env = make("kaggriculture",
                   configuration={"episodeSteps": 720, "seed": 101})
        env.run([raw, raw])
        # Animals that starve escape silently (engine `_daily_refresh_animals`
        # swaps the tile back to a bare structure), so a feeding change can look
        # fine on score alone while quietly losing the herd.  Count both.
        farm = env.steps[-1][0]["observation"]["farms"][0]
        live = sum(1 for row in farm["tiles"] for t in row
                   if isinstance(t, dict) and "animal" in t)
        empty = sum(1 for row in farm["tiles"] for t in row
                    if isinstance(t, dict) and t.get("kind") in ("COOP", "PASTURE")
                    and "animal" not in t)
        print(f"{path:22s} score {int(env.steps[-1][0].reward):>8,}  "
              f"_plan calls {calls[0]:>4}  animals {live:>3}  "
              f"empty structures {empty:>3}  status {env.steps[-1][0].status}")
