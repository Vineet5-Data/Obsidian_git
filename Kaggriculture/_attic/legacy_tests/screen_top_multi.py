"""screen_top.py for N candidates at once, sharing one baseline run.

Same paired test, same tapes, same seeds.  The baseline is the expensive half
and it is identical for every candidate, so running it once instead of N times
roughly halves the cost of a grid.

    python screen_top_multi.py --baseline a_v140_market_dominance.py \
        --seeds 2 cand_a.py cand_b.py cand_c.py
"""
import argparse
import multiprocessing as mp
import statistics
from pathlib import Path

import _duel
import top_tournament as T

ROOT = Path(__file__).resolve().parent


def run(agent, mode, seeds, pool):
    work = T.jobs(str(Path(agent).resolve()), mode, seeds)
    return work, [float(r[2]) for r in pool.map(_duel.one, work)]


def report(name, cand, base):
    n = len(cand)
    cw = sum(m > 0 for m in cand)
    bw = sum(m > 0 for m in base)
    gained = sum(1 for c, b in zip(cand, base) if c > 0 >= b)
    lost = sum(1 for c, b in zip(cand, base) if b > 0 >= c)
    disc = gained + lost
    chi = ((abs(gained - lost) - 1) ** 2 / disc) if disc else 0.0
    deltas = [c - b for c, b in zip(cand, base)]
    sem = statistics.stdev(deltas) / (n ** 0.5) if n > 1 else 0.0
    t = statistics.mean(deltas) / sem if sem else 0.0
    flag = "SIG" if chi > 3.84 else "   "
    print(f"  {name:<26}{100.0 * cw / n:>7.1f}%{100.0 * (cw - bw) / n:>+9.2f}"
          f"{gained:>7}{lost:>7}{chi:>9.2f} {flag}"
          f"{statistics.mean(deltas):>+11,.0f}{t:>+8.2f}")
    return 100.0 * (cw - bw) / n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("candidates", nargs="+")
    ap.add_argument("--baseline", default=str(ROOT / "a_v140_market_dominance.py"))
    ap.add_argument("--mode", choices=("recorded", "random"), default="random")
    ap.add_argument("--seeds", type=int, default=2)
    ap.add_argument("--workers", type=int, default=14)
    args = ap.parse_args()

    with mp.Pool(args.workers) as pool:
        work_b, base = run(args.baseline, args.mode, args.seeds, pool)
        print(f"  baseline {Path(args.baseline).name}: "
              f"{sum(m > 0 for m in base)}-{sum(m <= 0 for m in base)} "
              f"over {len(base)} games", flush=True)
        results = []
        for c in args.candidates:
            work_c, cand = run(c, args.mode, args.seeds, pool)
            assert [j[1:] for j in work_c] == [j[1:] for j in work_b], "jobs diverged"
            results.append((Path(c).name, cand))

    print(f"\n  {len(base)} paired games vs {Path(args.baseline).name}"
          f" ({args.mode}, {args.seeds} seeds)\n")
    print(f"  {'candidate':<26}{'win%':>8}{'delta':>9}{'+W':>7}{'+L':>7}"
          f"{'chi2':>9}    {'margin':>11}{'t':>8}")
    for name, cand in results:
        report(name, cand, base)


if __name__ == "__main__":
    mp.freeze_support()
    main()
