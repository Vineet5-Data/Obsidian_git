"""Compare our action mix against the actual top players', per 1000 unit-turns.

Raw counts are not comparable across replays: a farm with more hands simply
does more of everything.  Normalising by total unit-turns turns the question
into "how does a top player SPEND a turn?", which is the thing we can copy.

Usage:  python _topops.py v40.py
"""
import glob
import json
import os
import sys
from collections import Counter

MOVES = {"NORTH", "SOUTH", "EAST", "WEST"}


def count_actions(steps, seat):
    """-> Counter of unit ops for one seat across an episode."""
    ops = Counter()
    for st in steps[1:]:
        a = (st[seat].get("action") or {}) if seat < len(st) else {}
        if not isinstance(a, dict):
            continue
        for u in [a.get("farmer")] + list(a.get("hands") or []):
            if isinstance(u, list) and u:
                ops[u[0]] += 1
        for o in (a.get("market") or []):
            if o:
                ops["mkt:" + o[0]] += 1
    return ops


def profile(ops):
    """Normalise to per-1000 unit-turns so farms of different size compare."""
    unit = sum(v for k, v in ops.items() if not k.startswith("mkt:"))
    if not unit:
        return {}, 0
    return {k: 1000.0 * v / unit for k, v in ops.items()}, unit


def top_profiles(pattern="Top_fresh-21/*.json"):
    """Average the WINNER's profile across every top replay."""
    acc, n = Counter(), 0
    for path in sorted(glob.glob(pattern)):
        try:
            with open(path, encoding="utf-8") as fh:
                rep = json.load(fh)
        except Exception as exc:
            print(f"  skip {os.path.basename(path)}: {exc}")
            continue
        steps = rep.get("steps") or []
        if not steps:
            continue
        final = steps[-1]
        rewards = [(final[s].get("reward") or 0) for s in range(len(final))]
        seat = rewards.index(max(rewards))          # learn from the winner only
        prof, unit = profile(count_actions(steps, seat))
        if not prof:
            continue
        for k, v in prof.items():
            acc[k] += v
        n += 1
        print(f"  {os.path.basename(path):16} winner=seat{seat} "
              f"score={rewards[seat]:>9,.0f} unit_turns={unit:,}")
    return {k: v / n for k, v in acc.items()}, n


def ours(agent_path, seed=7):
    from kaggle_environments import make
    import importlib.util
    spec = importlib.util.spec_from_file_location("me", agent_path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run([m.agent, m.agent])
    prof, unit = profile(count_actions(env.steps, 0))
    return prof, unit, int(env.steps[-1][0].reward)


if __name__ == "__main__":
    agent = sys.argv[1] if len(sys.argv) > 1 else "v40.py"
    print("top replays (winner seat only):")
    top, n = top_profiles()
    print(f"\naveraged over {n} top winners\n")
    mine, unit, score = ours(agent)
    print(f"{agent}: score {score:,}, {unit:,} unit-turns\n")

    keys = sorted(set(top) | set(mine), key=lambda k: -(top.get(k, 0)))
    print(f"{'op':<22}{'TOP/1k':>9}{'OURS/1k':>9}{'diff':>9}")
    for k in keys:
        t, o = top.get(k, 0.0), mine.get(k, 0.0)
        if max(t, o) < 1.0:
            continue
        print(f"{k:<22}{t:>9.1f}{o:>9.1f}{o - t:>+9.1f}")

    tmove = sum(v for k, v in top.items() if k in MOVES)
    omove = sum(v for k, v in mine.items() if k in MOVES)
    print(f"\n{'MOVE total':<22}{tmove:>9.1f}{omove:>9.1f}{omove - tmove:>+9.1f}")
