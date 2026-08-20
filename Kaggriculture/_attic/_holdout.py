"""Held-out validation: the classifier threshold was calibrated on seeds i=1..24.

If -34 at step 200 only works because it was fitted to those seeds, it will fail
on fresh ones.  These seeds (i = 101..124) were never used for anything.
"""
import multiprocessing as mp, os, statistics, sys
import _duel, _panel

def main():
    agent = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 24
    off = int(sys.argv[3]) if len(sys.argv) > 3 else 100
    seeds = [((i + off) * 2654435761) % 2147483647 for i in range(1, n + 1)]
    jobs = []
    for path, _ in _panel.PANEL:
        if os.path.exists(path):
            jobs += [(agent, path, s, seat) for s in seeds for seat in (0, 1)]
    with mp.Pool(max(1, (os.cpu_count() or 4) - 2)) as pool:
        res = pool.map(_duel.one, jobs)
    print(f"{agent} -- HELD-OUT seeds i={off+1}..{off+n} x 2 seats\n")
    print(f"{'opponent':30s} {'W-L-T':>10} {'win%':>6} {'mean':>10} {'worst':>10}")
    i, grand = 0, []
    for path, label in _panel.PANEL:
        if not os.path.exists(path):
            continue
        chunk = [r[2] for r in res[i:i + 2 * n]]; i += 2 * n
        grand += chunk
        w = sum(1 for m in chunk if m > 0); l = sum(1 for m in chunk if m < 0)
        print(f"{label:30s} {f'{w}-{l}-{len(chunk)-w-l}':>10} "
              f"{100*w/len(chunk):>5.1f}% {statistics.mean(chunk):>+10,.0f} "
              f"{min(chunk):>+10,.0f}")
    w = sum(1 for m in grand if m > 0); l = sum(1 for m in grand if m < 0)
    print(f"\nOVERALL {w}-{l}-{len(grand)-w-l}  ({100*w/len(grand):.1f}%)  "
          f"mean {statistics.mean(grand):+,.0f}  worst {min(grand):+,.0f}")

if __name__ == "__main__":
    mp.freeze_support(); main()
