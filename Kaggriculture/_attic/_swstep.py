"""Which switch step is free for the Youssef matchup?

v32 is 286-2.  Route B beats Youssef 48-0 on its own, and the money-delta
classifier separates cleanly at BOTH seats on all 24 seeds (gap 5), so the two
losses are the COST of switching at step 240 on those seeds, not a
misidentification.  Forcing route B (oracle) isolates that cost per step.

Step 169 is excluded on purpose: it straddles the step-168 BUY_LAND turn and
measured a -73,382 tail.
"""
import importlib.util, multiprocessing as mp, os, statistics

def load(p, n):
    s = importlib.util.spec_from_file_location(n, p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

STEPS = [1, 100, 200, 240, 280, 360]
OPP = [(".field/f_90635229_p1.py", "Youssef"), (".field/f_90635979_p1.py", "Khanh"),
       (".loss/o_90711580.py", "familyB")]

def one(job):
    step, path, label, seed, seat = job
    from kaggle_environments import make
    tag = f"{step}_{label}_{seed}_{seat}_{os.getpid()}"
    m = load("v30.py", "a_" + tag)
    tb = load("v31.py", "b_" + tag)._ACTIONS
    ta = m._ACTIONS
    inner = m.agent
    def agent(obs):
        s = int(m._get(obs, "step", 0) or 0)
        if s <= 0:
            m._ACTIONS = ta
        if s >= step:
            m._ACTIONS = tb
        return inner(obs)
    riv = load(path, "o_" + tag).agent
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run([agent, riv] if seat == 0 else [riv, agent])
    f = env.steps[-1]
    return (step, label), f[seat].reward - f[1 - seat].reward

def main():
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, 25)]
    jobs = [(st, p, l, s, seat) for st in STEPS for p, l in OPP
            if os.path.exists(p) for s in seeds for seat in (0, 1)]
    with mp.Pool(max(1, (os.cpu_count() or 4) - 2)) as pool:
        res = pool.map(one, jobs)
    t = {}
    for k, v in res: t.setdefault(k, []).append(v)
    print(f"{'switch':>8s}" + "".join(f"{l:>14s}" for _, l in OPP) + f"{'LOSSES':>9s}")
    for st in STEPS:
        cells, tot = [], 0
        for _, l in OPP:
            v = t.get((st, l), [])
            n = sum(1 for x in v if x <= 0); tot += n
            cells.append(f"{n}/{len(v)} ({min(v):+,.0f})".rjust(14))
        print(f"{st:>8d}" + "".join(cells) + f"{tot:>9d}")

if __name__ == "__main__":
    mp.freeze_support(); main()
