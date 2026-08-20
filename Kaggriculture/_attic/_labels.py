"""Which route wins each real matchup, on engine 1.32.6?

v33's classifier was calibrated on 1.32.4 where the six real games do not even
reproduce.  Its target labels (which rival needs route A vs route B) must be
re-derived before any threshold is re-fitted.
"""
import glob, importlib.util, multiprocessing as mp, os, statistics

ROUTES = {"A": ".loss/o_90729118.py", "B": ".field/f_90635979_p1.py"}
OPPS = sorted(glob.glob(".pure/p_*.py"))

def load(p, n):
    s = importlib.util.spec_from_file_location(n, p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def one(job):
    tag_r, opp, seed, seat = job
    from kaggle_environments import make
    tag = f"{tag_r}_{abs(hash(opp))%999}_{seed}_{seat}_{os.getpid()}"
    m = load("v30.py", "a_" + tag)          # v30 = stack without route switching
    m._ACTIONS = load(ROUTES[tag_r], "t_" + tag)._ACTIONS
    b = load(opp, "o_" + tag).agent
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run([m.agent, b] if seat == 0 else [b, m.agent])
    f = env.steps[-1]
    return (tag_r, opp), f[seat].reward - f[1 - seat].reward

def main():
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, 9)]
    jobs = [(r, o, s, seat) for r in ROUTES for o in OPPS
            for s in seeds for seat in (0, 1)]
    with mp.Pool(10) as pool:
        res = pool.map(one, jobs)
    t = {}
    for k, v in res: t.setdefault(k, []).append(v)
    print(f"{'opponent':12s}{'routeA W-L':>14s}{'A mean':>10s}"
          f"{'routeB W-L':>14s}{'B mean':>10s}{'  WANT':>8s}")
    labels = {}
    for o in OPPS:
        cells = {}
        for r in ROUTES:
            v = t[(r, o)]
            cells[r] = (sum(1 for x in v if x > 0), len(v), statistics.mean(v))
        want = "A" if cells["A"][0] > cells["B"][0] else \
               "B" if cells["B"][0] > cells["A"][0] else \
               ("A" if cells["A"][2] >= cells["B"][2] else "B")
        labels[os.path.basename(o)] = want
        print(f"{os.path.basename(o)[2:10]:12s}"
              f"{f'{cells[chr(65)][0]}-{cells[chr(65)][1]-cells[chr(65)][0]}':>14s}"
              f"{cells['A'][2]:>+10,.0f}"
              f"{f'{cells[chr(66)][0]}-{cells[chr(66)][1]-cells[chr(66)][0]}':>14s}"
              f"{cells['B'][2]:>+10,.0f}{want:>8s}")
    print("\nlabels:", labels)

if __name__ == "__main__":
    mp.freeze_support(); main()
