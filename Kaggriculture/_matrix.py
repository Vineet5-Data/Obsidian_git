"""Per-opponent breakdown, not just an aggregate win%.

_real.py collapses the panel to one number, which hides the shape of the
result: 36.8% overall can mean "slightly behind everyone" or "even with most
and annihilated by three". Those need opposite fixes, so print the matrix.

Usage:  python _matrix.py v46_a.py 6
"""
import glob
import multiprocessing as mp
import os
import statistics
import sys

import _duel
from _real import LABEL, PANEL


def main():
    agent = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, n + 1)]
    panel = [p for p in PANEL if os.path.exists(p)]
    jobs = [(agent, p, s, seat) for p in panel for s in seeds for seat in (0, 1)]
    with mp.Pool(10) as pool:
        res = pool.map(_duel.one, jobs)

    per = {}
    for (a, p, s, seat), r in zip(jobs, res):
        per.setdefault(p, []).append(r[2])

    print(f"{agent} vs each panel opponent, {n} seeds x 2 seats\n")
    print(f"{'opponent':<14}{'W-L':>8}{'win%':>8}{'mean margin':>14}"
          f"{'median':>12}{'best':>11}")
    rows = sorted(per.items(), key=lambda kv: statistics.mean(kv[1]))
    for p, v in rows:
        w = sum(1 for x in v if x > 0)
        name = LABEL.get(p, os.path.basename(p)[2:10])
        print(f"{name:<14}{f'{w}-{len(v)-w}':>8}{100.0*w/len(v):>7.1f}%"
              f"{statistics.mean(v):>+14,.0f}{statistics.median(v):>+12,.0f}"
              f"{max(v):>+11,.0f}")
    allv = [x for v in per.values() for x in v]
    w = sum(1 for x in allv if x > 0)
    print(f"\n{'TOTAL':<14}{f'{w}-{len(allv)-w}':>8}{100.0*w/len(allv):>7.1f}%"
          f"{statistics.mean(allv):>+14,.0f}")


if __name__ == "__main__":
    mp.freeze_support()
    main()
