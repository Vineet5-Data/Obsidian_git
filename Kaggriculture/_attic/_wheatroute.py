"""Do the wheat-heavy ladder routes beat v33's route on the correct engine?

v33 loses only 6 of 96 against the real field, all to the two builds selling
1,280 and 1,902 wheat.  Wheat is the good the town drain lifts, so their route
may simply be better.  Graft each onto our functional stack and compare.
"""
import glob, importlib.util, multiprocessing as mp, os, statistics

def load(p, n):
    s = importlib.util.spec_from_file_location(n, p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

OPPS = sorted(glob.glob(".pure/p_*.py"))
CANDS = ["v33.py", ".pure/p_90874645.py", ".pure/p_90879807.py", ".pure/p_90880659.py"]

def one(job):
    cand, opp, seed, seat = job
    from kaggle_environments import make
    tag = f"{abs(hash(cand))%9999}_{abs(hash(opp))%999}_{seed}_{seat}_{os.getpid()}"
    m = load("v33.py", "a_" + tag)
    if cand != "v33.py":
        t = load(cand, "t_" + tag)._ACTIONS
        m._ROUTE_A = t; m._ACTIONS = t
    b = load(opp, "o_" + tag).agent
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run([m.agent, b] if seat == 0 else [b, m.agent])
    f = env.steps[-1]
    return (cand, opp), f[seat].reward - f[1 - seat].reward

def main():
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, 4)]
    jobs = [(c, o, s, seat) for c in CANDS for o in OPPS for s in seeds for seat in (0, 1)]
    print(f"{len(jobs)} games", flush=True)
    with mp.Pool(8) as pool:
        res = pool.map(one, jobs)
    t = {}
    for k, v in res: t.setdefault(k, []).append(v)
    print(f"\n{'route':22s}" + "".join(f"{os.path.basename(o)[2:10]:>10s}" for o in OPPS)
          + f"{'W-L':>9s}{'mean':>11s}")
    for c in CANDS:
        cells, grand = [], []
        for o in OPPS:
            v = t.get((c, o), []); grand += v
            cells.append(f"{sum(1 for x in v if x>0)}/{len(v)}".rjust(10))
        w = sum(1 for x in grand if x > 0)
        print(f"{os.path.basename(c):22s}" + "".join(cells)
              + f"{f'{w}-{len(grand)-w}':>9s}{statistics.mean(grand):>+11,.0f}")

if __name__ == "__main__":
    mp.freeze_support(); main()
