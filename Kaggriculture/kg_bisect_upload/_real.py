"""The honest benchmark: every build vs the ACTUAL current field, engine 1.32.6.

Panel = the six agents that really beat us + six distinct top-leaderboard
builds (Seb, Mohit Rao, mrgrishninsb, CemBas, kakuteki, Ueddy).  All are pure
verbatim replays, and every recorded game reproduces to the dollar on 1.32.6.

Question this answers: does ROUTE SHOPPING (v30/v31/v33 graft another player's
tape) beat running our own route with functional layers only (v27)?  If not,
the cloned routes are pure fragility with no upside.
"""
import glob, importlib.util, multiprocessing as mp, os, statistics, sys
import _duel

PANEL = sorted(glob.glob(".pure/p_*.py")) + [
    ".top/t_90914286_0.py", ".top/t_90913514_1.py", ".top/t_90916037_1.py",
    ".top/t_90920155_1.py", ".top/t_90904143_0.py", ".top/t_90916074_1.py"]
LABEL = {".top/t_90914286_0.py": "Seb", ".top/t_90913514_1.py": "MohitRao",
         ".top/t_90916037_1.py": "mrgrish", ".top/t_90920155_1.py": "CemBas",
         ".top/t_90904143_0.py": "kakuteki", ".top/t_90916074_1.py": "Ueddy"}

def main():
    agents = sys.argv[1:-1]
    n = int(sys.argv[-1])
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, n + 1)]
    jobs = [(a, p, s, seat) for a in agents for p in PANEL if os.path.exists(p)
            for s in seeds for seat in (0, 1)]
    with mp.Pool(10) as pool:
        res = pool.map(_duel.one, jobs)
    idx, t = 0, {}
    for a in agents:
        for p in PANEL:
            if not os.path.exists(p): continue
            for _ in seeds:
                for _ in (0, 1):
                    t.setdefault((a, p), []).append(res[idx][2]); idx += 1
    print(f"REAL field: {len(PANEL)} current opponents x {n} seeds x 2 seats\n")
    print(f"{'agent':9s}{'W-L':>10s}{'win%':>8s}{'mean':>11s}{'worst':>10s}   losing matchups")
    for a in agents:
        grand, bad = [], []
        for p in PANEL:
            v = t.get((a, p), [])
            if not v: continue
            grand += v
            k = sum(1 for x in v if x <= 0)
            if k: bad.append(f"{LABEL.get(p, os.path.basename(p)[2:10])}:{k}")
        w = sum(1 for x in grand if x > 0)
        print(f"{a:9s}{f'{w}-{len(grand)-w}':>10s}{100*w/len(grand):>7.1f}%"
              f"{statistics.mean(grand):>+11,.0f}{min(grand):>+10,.0f}   {' '.join(bad)}")

if __name__ == "__main__":
    mp.freeze_support(); main()
