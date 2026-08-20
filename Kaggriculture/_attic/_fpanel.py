"""Panel built from the SIX CURRENT ladder opponents (v27's actual losses).

The old panel came from a single earlier snapshot and none of its opponents
sells 1,900 wheat.  Selection against it is selection against a dead meta.
"""
import glob, importlib.util, multiprocessing as mp, os, statistics, sys
import _duel

PANEL = sorted(glob.glob(".pure/p_*.py"))

def main():
    agents = sys.argv[1:-1] or ["v27.py", "v30.py", "v33.py"]
    n = int(sys.argv[-1]) if sys.argv[-1].isdigit() else 8
    if not sys.argv[-1].isdigit():
        agents = sys.argv[1:] or agents
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, n + 1)]
    jobs = [(a, p, s, seat) for a in agents for p in PANEL
            for s in seeds for seat in (0, 1)]
    with mp.Pool(max(1, (os.cpu_count() or 4) - 2)) as pool:
        res = pool.map(_duel.one, jobs)
    idx, table = 0, {}
    for a in agents:
        for p in PANEL:
            for _ in seeds:
                for _ in (0, 1):
                    table.setdefault((a, p), []).append(res[idx][2]); idx += 1
    print(f"FRESH panel ({len(PANEL)} current opponents x {n} seeds x 2 seats)\n")
    print(f"{'agent':10s}" + "".join(f"{os.path.basename(p)[2:10]:>10s}" for p in PANEL)
          + f"{'W-L':>10s}{'win%':>8s}{'mean':>10s}")
    for a in agents:
        cells, grand = [], []
        for p in PANEL:
            v = table[(a, p)]; grand += v
            cells.append(f"{sum(1 for m in v if m>0)}/{len(v)}".rjust(10))
        w = sum(1 for m in grand if m > 0)
        print(f"{a:10s}" + "".join(cells)
              + f"{f'{w}-{len(grand)-w}':>10s}{100*w/len(grand):>7.1f}%"
              + f"{statistics.mean(grand):>+10,.0f}")

if __name__ == "__main__":
    mp.freeze_support(); main()
