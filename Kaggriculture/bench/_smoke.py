"""Run one self-play season per candidate with the safety net removed.

`agent()` wraps `_plan` in a bare try/except that returns an all-PASS action on
any exception, so a candidate whose planner throws every turn still produces a
complete, legal episode and a plausible-looking score.  Benchmarking through
`agent()` would then measure the fallback.  Call `_plan` directly so anything
broken surfaces as a traceback here, before the panel spends an hour on it.

Usage:  python bench/_smoke.py v75.py v67_lin.py
"""
import importlib.util
import sys

from kaggle_environments import make


def load(path):
    spec = importlib.util.spec_from_file_location(
        "s_" + path.replace(".", "_").replace("\\", "_").replace("/", "_"),
        path)
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
        farm = env.steps[-1][0]["observation"]["farms"][0]
        live = sum(1 for row in farm["tiles"] for t in row
                   if isinstance(t, dict) and "animal" in t)
        empty = sum(1 for row in farm["tiles"] for t in row
                    if isinstance(t, dict)
                    and t.get("kind") in ("COOP", "PASTURE")
                    and "animal" not in t)
        print(f"{path:16s} score {int(env.steps[-1][0].reward):>8,}  "
              f"_plan calls {calls[0]:>4}  animals {live:>3}  "
              f"empty structures {empty:>3}  status {env.steps[-1][0].status}")
