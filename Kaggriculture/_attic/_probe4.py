"""Do route A or route B already beat the four rivals that beat v33?

If one does, this is a CLASSIFIER miss (cheap: extend the decision rule).
If neither does, a third route is needed.
"""
import importlib.util, multiprocessing as mp, os, statistics

def load(p, n):
    s = importlib.util.spec_from_file_location(n, p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

HARD = [".field/f_90629703_p0.py", ".field/f_90631991_p1.py",
        ".field/f_90630506_p0.py", ".field/f_90634316_p1.py"]
MINE = ["v30.py", "v31.py", "v33.py"]

def one(job):
    me, path, seed, seat = job
    from kaggle_environments import make
    tag = f"{os.path.basename(me)}_{abs(hash(path))%9999}_{seed}_{seat}_{os.getpid()}"
    a = load(me, "a_" + tag).agent
    b = load(path, "b_" + tag).agent
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run([a, b] if seat == 0 else [b, a])
    f = env.steps[-1]
    return (me, path), f[seat].reward - f[1 - seat].reward

def main():
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, 5)]
    jobs = [(m, p, s, seat) for m in MINE for p in HARD
            for s in seeds for seat in (0, 1)]
    with mp.Pool(max(1, (os.cpu_count() or 4) - 2)) as pool:
        res = pool.map(one, jobs)
    t = {}
    for k, v in res: t.setdefault(k, []).append(v)
    print(f"{'agent':9s}" + "".join(f"{os.path.basename(p)[2:12]:>14s}" for p in HARD))
    for m in MINE:
        cells = []
        for p in HARD:
            v = t[(m, p)]
            cells.append(f"{sum(1 for x in v if x<=0)}/{len(v)} ({min(v):+,.0f})".rjust(14))
        print(f"{m:9s}" + "".join(cells))

if __name__ == "__main__":
    mp.freeze_support(); main()
