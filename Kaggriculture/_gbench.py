"""Multi-seed ABSOLUTE-score bench for the pure-policy g* line.

_duel.py answers "does A beat B" (margin).  The g* line is nowhere near the
ladder yet, so the number that matters is how much money the policy actually
makes, over many seeds, not the margin against one opponent.  Handoff rule:
never trust a single seed -- a fixed-volume-cap variant once looked great on
one opponent (+726) and scored 6.6% on the full panel.

Usage:
    python _gbench.py g4.py                # mirror, 12 seeds
    python _gbench.py g4.py g3.py 12       # g4 vs g3, both scores reported
"""
import importlib.util
import multiprocessing as mp
import os
import statistics
import sys

_CACHE = {}


def load(path):
    if path not in _CACHE:
        name = "b_" + os.path.basename(path).replace(".", "_")
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        _CACHE[path] = module.agent
    return _CACHE[path]


def one(job):
    """-> (seed, seat, my_money, opp_money, status)."""
    a_path, b_path, seed, seat = job
    from kaggle_environments import make
    a, b = load(a_path), load(b_path)
    pair = [a, b] if seat == 0 else [b, a]
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run(pair)
    final = env.steps[-1]
    return (seed, seat, final[seat].reward, final[1 - seat].reward,
            str(final[seat].status))


def seeds_for(n):
    # spread over the 32-bit range the way the ladder does (same as _duel.py)
    return [(i * 2654435761) % 2147483647 for i in range(1, n + 1)]


def bench(a_path, b_path, seeds, workers=None):
    jobs = [(a_path, b_path, s, seat) for s in seeds for seat in (0, 1)]
    workers = workers or min(len(jobs), max(1, (os.cpu_count() or 4) - 2))
    with mp.Pool(workers) as pool:
        return pool.map(one, jobs)


def report(label, rows):
    mine = [r[2] for r in rows]
    theirs = [r[3] for r in rows]
    bad = [r for r in rows if r[4] != "DONE"]
    wins = sum(1 for r in rows if r[2] > r[3])
    losses = sum(1 for r in rows if r[2] < r[3])
    print(f"{label}  n={len(rows)}")
    print(f"  mine   mean {statistics.mean(mine):>10,.0f} "
          f" median {statistics.median(mine):>10,.0f} "
          f" min {min(mine):>10,.0f}  max {max(mine):>10,.0f}")
    print(f"  opp    mean {statistics.mean(theirs):>10,.0f} "
          f" median {statistics.median(theirs):>10,.0f}")
    print(f"  record {wins}-{losses}-{len(rows) - wins - losses} "
          f"({100 * wins / max(1, len(rows)):.1f}%)")
    if bad:
        print(f"  !! {len(bad)} non-DONE episodes: "
              f"{sorted({r[4] for r in bad})} seeds {sorted({r[0] for r in bad})}")
    worst = sorted(rows, key=lambda r: r[2])[:3]
    print("  worst seeds: " + ", ".join(f"{r[0]}/seat{r[1]}={r[2]:,.0f}" for r in worst))
    return statistics.mean(mine)


if __name__ == "__main__":
    mp.freeze_support()
    a_path = sys.argv[1]
    b_path = sys.argv[2] if len(sys.argv) > 2 and sys.argv[2].endswith(".py") else a_path
    n = int(sys.argv[-1]) if sys.argv[-1].isdigit() else 12
    rows = bench(a_path, b_path, seeds_for(n))
    report(f"{os.path.basename(a_path)} vs {os.path.basename(b_path)}", rows)
