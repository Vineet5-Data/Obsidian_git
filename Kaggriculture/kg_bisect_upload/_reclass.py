"""Re-fit the route classifier on engine 1.32.6 against the real field.

Both halves must be redone: the LABELS (which route actually wins each matchup)
and the FEATURES (the rival's public state at the switch step).  Both were
derived on 1.32.4, where none of the recorded games even reproduce.
"""
import glob, importlib.util, multiprocessing as mp, os, statistics

ROUTES = {"A": ".loss/o_90729118.py", "B": ".field/f_90635979_p1.py"}
PANEL = sorted(glob.glob(".pure/p_*.py")) + [
    ".top/t_90914286_0.py", ".top/t_90913514_1.py", ".top/t_90916037_1.py",
    ".top/t_90920155_1.py", ".top/t_90904143_0.py", ".top/t_90916074_1.py"]
STEP = 200

def load(p, n):
    s = importlib.util.spec_from_file_location(n, p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def one(job):
    r, opp, seed, seat = job
    from kaggle_environments import make
    tag = f"{r}_{abs(hash(opp))%999}_{seed}_{seat}_{os.getpid()}"
    m = load("v30.py", "a_" + tag)
    m._ACTIONS = load(ROUTES[r], "t_" + tag)._ACTIONS
    b = load(opp, "o_" + tag).agent
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run([m.agent, b] if seat == 0 else [b, m.agent])
    f = env.steps[-1]
    fa = env.steps[STEP][0]["observation"]["farms"]
    an = sum(1 for row in (fa[1-seat].get("tiles") or []) for t in (row or [])
             if isinstance(t, dict) and t.get("animal"))
    delta = int(fa[1-seat]["money"]) - int(fa[seat]["money"])
    return (r, opp), (f[seat].reward - f[1-seat].reward, delta, an)

def main():
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, 5)]
    jobs = [(r, o, s, seat) for r in ROUTES for o in PANEL if os.path.exists(o)
            for s in seeds for seat in (0, 1)]
    with mp.Pool(10) as pool:
        res = pool.map(one, jobs)
    t = {}
    for k, v in res: t.setdefault(k, []).append(v)
    print(f"{'opponent':12s}{'A W-L':>8s}{'A mean':>10s}{'B W-L':>8s}{'B mean':>10s}"
          f"{'WANT':>6s}{'delta@200':>18s}{'animals':>9s}")
    lab = {}
    for o in PANEL:
        if (("A", o) not in t): continue
        stats = {}
        for r in ROUTES:
            v = t[(r, o)]
            stats[r] = (sum(1 for x in v if x[0] > 0), len(v),
                        statistics.mean(x[0] for x in v))
        want = "A" if stats["A"][0] > stats["B"][0] else \
               "B" if stats["B"][0] > stats["A"][0] else \
               ("A" if stats["A"][2] >= stats["B"][2] else "B")
        d = [x[1] for x in t[("A", o)]]
        an = sorted({x[2] for x in t[("A", o)]})
        lab[o] = want
        print(f"{os.path.basename(o)[2:10]:12s}"
              f"{f'{stats[chr(65)][0]}-{stats[chr(65)][1]-stats[chr(65)][0]}':>8s}{stats['A'][2]:>+10,.0f}"
              f"{f'{stats[chr(66)][0]}-{stats[chr(66)][1]-stats[chr(66)][0]}':>8s}{stats['B'][2]:>+10,.0f}"
              f"{want:>6s}{f'{min(d)} .. {max(d)}':>18s}{str(an):>9s}")
    A = [x[1] for o in PANEL if lab.get(o) == "A" for x in t.get(("A", o), [])]
    B = [x[1] for o in PANEL if lab.get(o) == "B" for x in t.get(("A", o), [])]
    print(f"\nwant-A count {sum(1 for o in lab if lab[o]=='A')}, "
          f"want-B count {sum(1 for o in lab if lab[o]=='B')}")
    if A and B:
        print(f"delta ranges -> A: {min(A)} .. {max(A)}   B: {min(B)} .. {max(B)}")
        print(f"separable: {min(A) > max(B) or min(B) > max(A)}")

if __name__ == "__main__":
    mp.freeze_support(); main()
