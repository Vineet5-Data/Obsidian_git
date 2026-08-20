"""Paired candidate-vs-baseline screen on the REAL instrument (.top/ tapes).

Why this exists: the mirror-match screen (`screen_v140.py`, candidate vs its own
baseline) is systematically blind to a whole class of real gain.  In a mirror
both sides share one market, so extra production crashes the price and the gain
cancels out; against 80 structurally different opponents it does not.  The
no-op-suppression change measured +82 (parity) in the mirror and +1.8 points
(77.6% -> 79.4%) on the full benchmark.

Use the mirror screen only to REJECT large losers cheaply.  Use this to decide
anything that lands near zero there.

Both agents run the identical job list -- same opponents, same seeds, same
seats -- so margins pair up game for game and the comparison is a paired test,
which needs far fewer games than comparing two independent win rates.

    python screen_top.py <candidate.py> [--baseline X] [--seeds N] [--workers N]
"""
import argparse
import multiprocessing as mp
import statistics
from pathlib import Path

import _duel
import top_tournament as T

ROOT = Path(__file__).resolve().parent
DEFAULT_BASE = ROOT / "a_v140_market_dominance.baseline.py"


def run(agent, mode, seeds, pool):
    work = T.jobs(str(Path(agent).resolve()), mode, seeds)
    return work, pool.map(_duel.one, work)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("candidate")
    ap.add_argument("--baseline", default=str(DEFAULT_BASE))
    ap.add_argument("--mode", choices=("recorded", "random"), default="random")
    ap.add_argument("--seeds", type=int, default=2)
    ap.add_argument("--workers", type=int, default=14)
    args = ap.parse_args()

    with mp.Pool(args.workers) as pool:
        work_c, rows_c = run(args.candidate, args.mode, args.seeds, pool)
        work_b, rows_b = run(args.baseline, args.mode, args.seeds, pool)

    assert [j[1:] for j in work_c] == [j[1:] for j in work_b], "job lists diverged"

    cand = [float(r[2]) for r in rows_c]
    base = [float(r[2]) for r in rows_b]
    n = len(cand)
    cw, bw = sum(m > 0 for m in cand), sum(m > 0 for m in base)

    # McNemar on the discordant pairs: only games whose result actually flipped
    # carry information about the change.
    gained = sum(1 for c, b in zip(cand, base) if c > 0 >= b)
    lost = sum(1 for c, b in zip(cand, base) if b > 0 >= c)
    disc = gained + lost
    chi = ((abs(gained - lost) - 1) ** 2 / disc) if disc else 0.0

    deltas = [c - b for c, b in zip(cand, base)]
    sem = statistics.stdev(deltas) / (n ** 0.5) if n > 1 else 0.0

    print(f"\n  {Path(args.candidate).name}  vs  {Path(args.baseline).name}")
    print(f"  {n} paired games ({T.__name__} {args.mode}, {args.seeds} seeds)\n")
    print(f"  candidate   {cw}-{n - cw}   {100.0 * cw / n:.1f}%")
    print(f"  baseline    {bw}-{n - bw}   {100.0 * bw / n:.1f}%")
    print(f"  win-rate delta          {100.0 * (cw - bw) / n:+.2f} pts")
    print(f"\n  games flipped to win    {gained}")
    print(f"  games flipped to loss   {lost}")
    print(f"  McNemar chi2            {chi:.2f}"
          f"   {'SIGNIFICANT' if chi > 3.84 else 'not significant'} (p<0.05 at 3.84)")
    print(f"\n  mean paired margin      {statistics.mean(deltas):+,.0f}"
          f"   sem {sem:,.0f}"
          f"   t {statistics.mean(deltas) / sem if sem else 0.0:+.2f}")
    print(f"  median paired margin    {statistics.median(deltas):+,.0f}")


if __name__ == "__main__":
    mp.freeze_support()
    main()
