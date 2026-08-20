"""Broad-seed panel: one agent against every threat archetype we know of.

Selection so far happened on 3-6 hand-picked seeds.  The real ladder draws
seeds like 654920739, and the 24-seed measurement showed a 83% win rate where
3 seeds had shown 8-0.  Everything gets judged on 24 seeds x 2 seats from here.

Usage:  python _panel.py <agent.py> [n_seeds]
"""
import multiprocessing as mp
import os
import statistics
import sys

import _duel

PANEL = [
    (".loss/o_90711580.py", "family B (Nat Bel, ladder)"),
    (".loss/o_90729118.py", "mirror (Leon Christians)"),
    (".field/f_90639963_p1.py", "Seb 4-quadrant milk flood"),
    (".field/f_90635979_p1.py", "Khanh"),
    (".field/f_90635229_p1.py", "Youssef EL MSIYAH"),
    ("wufang_agent.py", "Wufang Hong (current top)"),
]


def main():
    agent = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 24
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, n + 1)]
    jobs = []
    for path, _ in PANEL:
        if not os.path.exists(path):
            continue
        jobs += [(agent, path, s, seat) for s in seeds for seat in (0, 1)]
    workers = max(1, (os.cpu_count() or 4) - 2)
    with mp.Pool(workers) as pool:
        results = pool.map(_duel.one, jobs)

    print(f"{os.path.basename(agent)}  --  {n} seeds x 2 seats per opponent\n")
    index = 0
    grand = []
    print(f"{'opponent':30s} {'W-L-T':>10} {'win%':>6} {'mean':>9} "
          f"{'worst':>9} {'best':>9}")
    for path, label in PANEL:
        if not os.path.exists(path):
            continue
        chunk = results[index:index + 2 * n]
        index += 2 * n
        margins = [r[2] for r in chunk]
        grand += margins
        w = sum(1 for m in margins if m > 0)
        l = sum(1 for m in margins if m < 0)
        t = len(margins) - w - l
        print(f"{label:30s} {f'{w}-{l}-{t}':>10} "
              f"{100 * w / len(margins):>5.1f}% "
              f"{statistics.mean(margins):>+9,.0f} {min(margins):>+9,.0f} "
              f"{max(margins):>+9,.0f}")
    w = sum(1 for m in grand if m > 0)
    l = sum(1 for m in grand if m < 0)
    print(f"\nOVERALL {w}-{l}-{len(grand) - w - l}  "
          f"({100 * w / len(grand):.1f}%)  mean {statistics.mean(grand):+,.0f}  "
          f"worst {min(grand):+,.0f}")


if __name__ == "__main__":
    mp.freeze_support()
    main()
