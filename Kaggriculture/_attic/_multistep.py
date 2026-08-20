"""Where do the near-identical family-A variants separate into route groups?

29703_p0 / 31991_p1 / Wufang / mirror want route A; Khanh / Youssef want route B.
All are the same underlying route with different market cells, so they are
identical at step 200.  Sample the money delta on a grid of steps to find one
where the two groups split.
"""
import importlib.util, multiprocessing as mp, os

def load(p, n):
    s = importlib.util.spec_from_file_location(n, p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

STEPS = [200, 220, 240, 260, 300, 340, 400, 480]
OPP = [(".field/f_90629703_p0.py", "29703_p0", "A"),
       (".field/f_90631991_p1.py", "31991_p1", "A"),
       ("wufang_agent.py", "Wufang", "A"),
       (".loss/o_90729118.py", "mirror", "A"),
       (".field/f_90635979_p1.py", "Khanh", "B"),
       (".field/f_90635229_p1.py", "Youssef", "B")]

def probe(job):
    path, label, seed, seat = job
    from kaggle_environments import make
    tag = f"{label}_{seed}_{seat}_{os.getpid()}"
    me = load("v30.py", "m_" + tag).agent
    b = load(path, "o_" + tag).agent
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run([me, b] if seat == 0 else [b, me])
    out = {}
    for st in STEPS:
        f = env.steps[st][0]["observation"]["farms"]
        out[st] = int(f[1-seat]["money"]) - int(f[seat]["money"])
    return label, out

def main():
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, 5)]
    jobs = [(p, l, s, seat) for p, l, _ in OPP if os.path.exists(p)
            for s in seeds for seat in (0, 1)]
    with mp.Pool(max(1, (os.cpu_count() or 4) - 2)) as pool:
        rows = pool.map(probe, jobs)
    want = {l: g for _, l, g in OPP}
    by = {}
    for lab, out in rows:
        for st, d in out.items(): by.setdefault((lab, st), []).append(d)
    print(f"{'step':>6s}  {'A-group range':>22s}  {'B-group range':>22s}  {'gap':>8s}")
    for st in STEPS:
        a = [d for l in want if want[l]=='A' for d in by.get((l,st),[])]
        b = [d for l in want if want[l]=='B' for d in by.get((l,st),[])]
        if not a or not b: continue
        gap = min(b) - max(a) if min(b) > max(a) else (min(a) - max(b) if min(a) > max(b) else 0)
        flag = "SEPARABLE" if gap > 0 else ""
        print(f"{st:>6d}  {f'{min(a)} .. {max(a)}':>22s}  {f'{min(b)} .. {max(b)}':>22s}  {gap:>8d}  {flag}")

if __name__ == "__main__":
    mp.freeze_support(); main()
