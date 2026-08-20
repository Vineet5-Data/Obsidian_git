"""Are the opponents actually playing, or erroring out and forfeiting?

A 34-0 sweep is more likely a harness artifact than a real result.  If an
opponent raises, kaggle_environments marks that seat ERROR/INVALID and stops
stepping it, so it banks nothing and the margin looks enormous.  Print the
per-seat status and reward for one episode against each opponent, and run each
opponent twice in the SAME process to expose module-level state that survives
between episodes (these bots keep globals; a cached module is not a fresh bot).
"""
import importlib.util
import os
import sys

from kaggle_environments import make

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DIRS = [os.path.join(ROOT, "Top_fresh-21"), os.path.join(ROOT, "v27_losses")]


def load(path, tag=""):
    spec = importlib.util.spec_from_file_location(
        "x_" + os.path.basename(path)[:-3] + tag, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


cand = load(sys.argv[1] if len(sys.argv) > 1 else "v75.py").agent
opps = sorted(os.path.join(d, f) for d in DIRS
              for f in os.listdir(d) if f.endswith(".py"))

print(f"{'opponent':14s} {'run':>3s} {'our status':>12s} {'their status':>13s} "
      f"{'ours':>10s} {'theirs':>10s}")
for p in opps:
    for run in (1, 2):
        # fresh import each run -> if run 2 differs, the bot carries state
        opp = load(p, tag=f"_r{run}").agent
        env = make("kaggriculture",
                   configuration={"episodeSteps": 720, "seed": 2654435761 % 2147483647})
        env.run([cand, opp])
        a, b = env.steps[-1][0], env.steps[-1][1]
        print(f"{os.path.basename(p)[:-3]:14s} {run:>3d} {a.status:>12s} "
              f"{b.status:>13s} {int(a.reward or 0):>10,} "
              f"{int(b.reward or 0):>10,}")
