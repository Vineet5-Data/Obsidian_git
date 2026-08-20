"""Parallel head-to-head over many seeds, across all cores.

The field benchmark and the 8-0 family A/B result both used a handful of
hand-picked seeds (9701-9703, 9901-9903).  The real ladder uses seeds like
654920739.  This measures the true win rate over a wide seed sample so
selection stops happening on three lucky draws.

Usage:  python _duel.py <agent.py> <opponent.py> [n_seeds]
"""
import importlib.util
import multiprocessing as mp
import os
import statistics
import sys

_CACHE = {}


def load(path):
    if path not in _CACHE:
        name = "m_" + os.path.basename(path).replace(".", "_")
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        _CACHE[path] = module.agent
    return _CACHE[path]


def one(job):
    a_path, b_path, seed, seat = job
    from kaggle_environments import make
    a, b = load(a_path), load(b_path)
    pair = [a, b] if seat == 0 else [b, a]
    env = make("kaggriculture",
               configuration={"episodeSteps": 720, "seed": seed})
    env.run(pair)
    final = env.steps[-1]
    return seed, seat, final[seat].reward - final[1 - seat].reward


def duel(a_path, b_path, seeds, workers=None):
    jobs = [(a_path, b_path, s, seat) for s in seeds for seat in (0, 1)]
    workers = workers or min(len(jobs), max(1, (os.cpu_count() or 4) - 2))
    with mp.Pool(workers) as pool:
        return pool.map(one, jobs)


def report(label, rows):
    margins = [r[2] for r in rows]
    wins = sum(1 for m in margins if m > 0)
    losses = sum(1 for m in margins if m < 0)
    ties = len(margins) - wins - losses
    by_seat = {0: [r[2] for r in rows if r[1] == 0],
               1: [r[2] for r in rows if r[1] == 1]}
    print(f"{label}: {wins}-{losses}-{ties} "
          f"({100 * wins / max(1, len(margins)):.1f}%)  "
          f"mean {statistics.mean(margins):+,.0f}  "
          f"median {statistics.median(margins):+,.0f}  "
          f"min {min(margins):+,.0f}  max {max(margins):+,.0f}")
    for seat in (0, 1):
        m = by_seat[seat]
        if m:
            w = sum(1 for x in m if x > 0)
            print(f"    seat{seat}: {w}/{len(m)} wins, mean {statistics.mean(m):+,.0f}")
    return wins, losses, ties, statistics.mean(margins)


if __name__ == "__main__":
    mp.freeze_support()
    a_path, b_path = sys.argv[1], sys.argv[2]
    n = int(sys.argv[3]) if len(sys.argv) > 3 else 24
    # spread over the whole 32-bit range like the real ladder does
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, n + 1)]
    rows = duel(a_path, b_path, seeds)
    report(f"{os.path.basename(a_path)} vs {os.path.basename(b_path)}", rows)
