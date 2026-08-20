"""Same features, but with us at SEAT 1 -- the case _delta.py never measured."""
import importlib.util, multiprocessing as mp, os

def load(p, n):
    s = importlib.util.spec_from_file_location(n, p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

OPP = [(".field/f_90635229_p1.py", "Youssef"), (".field/f_90635979_p1.py", "Khanh"),
       ("wufang_agent.py", "Wufang"), (".loss/o_90729118.py", "mirror")]

def probe(job):
    path, label, seed, seat = job
    from kaggle_environments import make
    tag = f"{label}_{seed}_{seat}_{os.getpid()}"
    me = load("v30.py", "me_" + tag).agent
    riv = load(path, "op_" + tag).agent
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run([me, riv] if seat == 0 else [riv, me])
    f = env.steps[200][0]["observation"]["farms"]
    return label, seat, seed, int(f[1 - seat]["money"]) - int(f[seat]["money"])

def main():
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, 25)]
    jobs = [(p, l, s, seat) for p, l in OPP if os.path.exists(p)
            for s in seeds for seat in (0, 1)]
    with mp.Pool(max(1, (os.cpu_count() or 4) - 2)) as pool:
        rows = pool.map(probe, jobs)
    by = {}
    for label, seat, seed, d in rows:
        by.setdefault((label, seat), []).append(d)
    print(f"{'opp':9s}{'seat':>6s}{'delta min':>12s}{'delta max':>12s}")
    for (label, seat), v in sorted(by.items()):
        print(f"{label:9s}{seat:>6d}{min(v):>12d}{max(v):>12d}")
    b = [d for (l, s), v in by.items() if l in ("Khanh", "Youssef") for d in v]
    a = [d for (l, s), v in by.items() if l == "Wufang" for d in v]
    print(f"\nBOTH SEATS  B min {min(b)}  A max {max(a)}  gap {min(b)-max(a)}")

if __name__ == "__main__":
    mp.freeze_support(); main()
