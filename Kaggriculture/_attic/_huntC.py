"""Find one route beating the whole delta≈-25 cluster.

At step 200 these five rivals are observationally IDENTICAL (money delta -26..-25,
7 animals, 38 plants, same crop mix, same sales) yet route A beats two of them
and route B beats the other two -- no classifier can split them, at any step
tested up to 480.

But they form a clean CLUSTER, distinct from mirror (delta 0), Wufang (-187..-78),
familyB (10 animals) and Seb (<=4 animals).  So identification is unnecessary if
a single route C beats every member.  That sidesteps the information limit
entirely.
"""
import glob, importlib.util, multiprocessing as mp, os

def load(p, n):
    s = importlib.util.spec_from_file_location(n, p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

CLUSTER = [".field/f_90629703_p0.py", ".field/f_90631991_p1.py",
           ".field/f_90630506_p0.py", ".field/f_90635979_p1.py",
           ".field/f_90635229_p1.py"]

def one(job):
    route, path, seed, seat = job
    from kaggle_environments import make
    tag = f"{abs(hash(route))%99999}_{abs(hash(path))%9999}_{seed}_{seat}_{os.getpid()}"
    try:
        m = load("v30.py", "a_" + tag)
        if route != "v30.py":
            m._ACTIONS = load(route, "t_" + tag)._ACTIONS
        b = load(path, "o_" + tag).agent
    except Exception:
        return (route, path), None
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run([m.agent, b] if seat == 0 else [b, m.agent])
    f = env.steps[-1]
    return (route, path), f[seat].reward - f[1 - seat].reward

def main():
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, 3)]
    routes = ["v30.py"] + sorted(glob.glob(".field/f_*.py")) + sorted(glob.glob(".loss/o_*.py"))
    jobs = [(r, p, s, seat) for r in routes for p in CLUSTER
            for s in seeds for seat in (0, 1)]
    print(f"{len(routes)} routes x {len(CLUSTER)} cluster rivals x {len(seeds)} seeds "
          f"x 2 seats = {len(jobs)} games", flush=True)
    with mp.Pool(max(1, (os.cpu_count() or 4) - 2)) as pool:
        res = pool.map(one, jobs)
    t = {}
    for k, v in res:
        if v is not None: t.setdefault(k, []).append(v)
    rows = []
    for r in routes:
        cells, tot, worst = [], 0, None
        ok = True
        for p in CLUSTER:
            v = t.get((r, p), [])
            if not v: ok = False; break
            n = sum(1 for x in v if x <= 0); tot += n
            worst = min(v) if worst is None else min(worst, min(v))
            cells.append(f"{n}/{len(v)}")
        if ok: rows.append((tot, -(worst or 0), r, cells, worst))
    rows.sort(key=lambda x: (x[0], x[1]))
    print(f"\n{'route':28s}" + "".join(f"{os.path.basename(p)[2:11]:>11s}" for p in CLUSTER)
          + f"{'LOSS':>6s}{'worst':>10s}")
    for tot, _, r, cells, worst in rows[:12]:
        print(f"{os.path.basename(r):28s}" + "".join(c.rjust(11) for c in cells)
              + f"{tot:>6d}{worst:>+10,.0f}")
    clean = [r for r in rows if r[0] == 0]
    print(f"\nroutes sweeping the whole cluster: {len(clean)}")
    for r in clean: print("   ", os.path.basename(r[2]), f"worst {r[4]:+,.0f}")

if __name__ == "__main__":
    mp.freeze_support(); main()
