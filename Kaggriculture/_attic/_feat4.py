"""Classifier features at step 200 for the four rivals v33 gets wrong."""
import importlib.util, multiprocessing as mp, os

def load(p, n):
    s = importlib.util.spec_from_file_location(n, p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

OPP = [(".field/f_90629703_p0.py", "29703_p0", "A"),
       (".field/f_90631991_p1.py", "31991_p1", "A"),
       (".field/f_90630506_p0.py", "30506_p0", "?"),
       (".field/f_90634316_p1.py", "34316_p1", "?"),
       (".field/f_90635979_p1.py", "Khanh", "B"),
       (".field/f_90635229_p1.py", "Youssef", "B"),
       ("wufang_agent.py", "Wufang", "A"),
       (".loss/o_90711580.py", "familyB", "B"),
       (".loss/o_90729118.py", "mirror", "A")]

def probe(job):
    path, label, seed, seat = job
    from kaggle_environments import make
    tag = f"{label}_{seed}_{seat}_{os.getpid()}"
    me = load("v30.py", "m_" + tag).agent
    b = load(path, "o_" + tag).agent
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run([me, b] if seat == 0 else [b, me])
    f = env.steps[200][0]["observation"]["farms"]
    an = pl = 0
    for row in (f[1 - seat].get("tiles") or []):
        for t in (row or []):
            if isinstance(t, dict):
                if t.get("animal"): an += 1
                elif t.get("kind") == "PLANT": pl += 1
    return label, int(f[1-seat]["money"]) - int(f[seat]["money"]), an, pl

def main():
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, 5)]
    jobs = [(p, l, s, seat) for p, l, _ in OPP if os.path.exists(p)
            for s in seeds for seat in (0, 1)]
    with mp.Pool(max(1, (os.cpu_count() or 4) - 2)) as pool:
        rows = pool.map(probe, jobs)
    by = {}
    for lab, d, an, pl in rows: by.setdefault(lab, []).append((d, an, pl))
    print(f"{'rival':10s}{'want':>6s}{'delta range':>18s}{'animals':>10s}{'plants':>10s}{'v33 picks':>11s}")
    for _, lab, want in OPP:
        v = by.get(lab)
        if not v: continue
        ds = sorted(x[0] for x in v)
        ans = sorted({x[1] for x in v}); pls = sorted({x[2] for x in v})
        # replicate v33's rule
        picks = set()
        for d, an, pl in v:
            picks.add("A" if an <= 4 else "B" if an >= 10 else
                      "A" if d == 0 else "B" if d > -34 else "A")
        print(f"{lab:10s}{want:>6s}{f'{ds[0]} .. {ds[-1]}':>18s}"
              f"{str(ans):>10s}{str(pls):>10s}{'/'.join(sorted(picks)):>11s}")

if __name__ == "__main__":
    mp.freeze_support(); main()
