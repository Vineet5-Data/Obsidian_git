"""Paired local screen: candidate vs baseline on identical (opponent, seed, seat).

Same methodology as the v140 header (paired margin delta + t), held to the
20-game local cap. Rejects a loser cheaply; it cannot confirm a winner -- that
still needs the full Kaggle set.

Usage: python screen_pair.py <candidate.py> <baseline.py>
"""
import glob
import importlib.util
import multiprocessing as mp
import statistics
import sys
from pathlib import Path

REPO = Path(r"C:\Users\Vinee\Desktop\Kaggriculture")
TOP = Path(r"C:\Users\Vinee\Downloads\grid_search")
CAP = 20  # hard local cap on total games


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.agent


def one(job):
    agent_path, opp_path, seed, seat = job
    from kaggle_environments import make
    a = _load(agent_path, "a_" + Path(agent_path).stem)
    b = _load(opp_path, "o_" + Path(opp_path).stem)
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run([a, b] if seat == 0 else [b, a])
    return env.steps[-1][seat].reward - env.steps[-1][1 - seat].reward


def main():
    cand, base = sys.argv[1], sys.argv[2]
    opps = sorted(glob.glob(str(TOP / "t_*_0.py")))
    opps = [opps[i] for i in range(0, len(opps), max(1, len(opps) // 5))][:5]
    seed = (11 * 2654435761) % 2147483647
    cells = [(o, seed, seat) for o in opps for seat in (0, 1)]
    assert 2 * len(cells) <= CAP, f"{2*len(cells)} games exceeds cap {CAP}"

    jobs = [(cand, o, s, st) for o, s, st in cells] + \
           [(base, o, s, st) for o, s, st in cells]
    print(f"{len(jobs)} games ({len(cells)} paired cells), seed {seed}", flush=True)
    with mp.Pool(min(8, max(1, (mp.cpu_count() or 4) - 2))) as pool:
        res = pool.map(one, jobs)
    n = len(cells)
    deltas = [res[i] - res[i + n] for i in range(n)]

    print(f"\n{'opponent':<18}{'seat':>5}{'cand':>11}{'base':>11}{'delta':>11}")
    for (o, _s, st), c, b, d in zip(cells, res[:n], res[n:], deltas):
        print(f"{Path(o).stem:<18}{st:>5}{c:>+11,.0f}{b:>+11,.0f}{d:>+11,.0f}")

    mean = statistics.mean(deltas)
    sd = statistics.stdev(deltas) if n > 1 else 0.0
    t = mean / (sd / (n ** 0.5)) if sd else float("inf") if mean else 0.0
    wins = sum(1 for d in deltas if d > 0)
    print(f"\nmean delta {mean:>+10,.0f}   sd {sd:>9,.0f}   t {t:>+6.2f}   "
          f"cells won {wins}/{n}")
    if t <= -2.0:
        print("VERDICT: reject -- clear loser, do not spend a Kaggle run")
    elif t >= 2.0:
        print("VERDICT: promising -- not proof; confirm on the full set")
    else:
        print("VERDICT: inconclusive at this n. A near-zero paired screen is "
              "NOT evidence of no effect (shared-market gains cancel).")


if __name__ == "__main__":
    mp.freeze_support()
    main()
