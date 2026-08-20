"""Richer fingerprint: rival crop composition + per-item sales, both public.

Five rivals are identical at step 200 on (money delta, animals, plants) yet need
different routes.  Crop mix is directly visible on their tiles; per-item sales
are exactly identified from shared-market inventory deltas minus our own.
"""
import importlib.util, multiprocessing as mp, os, collections

def load(p, n):
    s = importlib.util.spec_from_file_location(n, p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

OPP = [(".field/f_90629703_p0.py", "29703_p0", "A"),
       (".field/f_90631991_p1.py", "31991_p1", "A"),
       ("wufang_agent.py", "Wufang", "A"),
       (".loss/o_90729118.py", "mirror", "A"),
       (".field/f_90635979_p1.py", "Khanh", "B"),
       (".field/f_90635229_p1.py", "Youssef", "B"),
       (".loss/o_90711580.py", "familyB", "B")]
STEP = 200
CROPS = ("WHEAT", "MELON", "STRAWBERRY", "TOMATO", "CARROT")

def probe(job):
    path, label, seed = job
    from kaggle_environments import make
    tag = f"{label}_{seed}_{os.getpid()}"
    me = load("v30.py", "m_" + tag).agent
    b = load(path, "o_" + tag).agent
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run([me, b])
    obs = env.steps[STEP][0]["observation"]
    crop = collections.Counter()
    for row in (obs["farms"][1].get("tiles") or []):
        for t in (row or []):
            if isinstance(t, dict) and t.get("crop"):
                crop[t["crop"]] += 1
    inv0 = env.steps[0][0]["observation"]["market"]["inventory"]
    inv = obs["market"]["inventory"]
    mine = collections.Counter()
    for i in range(STEP):
        for o in ((env.steps[i+1][0].get("action") or {}).get("market") or []):
            if o and o[0] == "SELL" and len(o) >= 3:
                mine[o[1]] += int(o[2])
    sales = {k: inv[k] - inv0[k] + mine[k] for k in inv}
    return label, tuple(crop[c] for c in CROPS), sales.get("WHEAT", 0), sales.get("MILK", 0)

def main():
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, 4)]
    jobs = [(p, l, s) for p, l, _ in OPP if os.path.exists(p) for s in seeds]
    with mp.Pool(max(1, (os.cpu_count() or 4) - 2)) as pool:
        rows = pool.map(probe, jobs)
    by = {}
    for lab, crop, w, mk in rows: by.setdefault(lab, []).append((crop, w, mk))
    want = {l: g for _, l, g in OPP}
    print(f"{'rival':10s}{'want':>5s}  {'crops (WH,ME,ST,TO,CA)':28s}{'wheatSales':>12s}{'milkSales':>11s}")
    for _, lab, _g in OPP:
        v = by.get(lab)
        if not v: continue
        crops = sorted({x[0] for x in v})
        print(f"{lab:10s}{want[lab]:>5s}  {str(crops[0]):28s}"
              f"{str(sorted({x[1] for x in v})):>12s}{str(sorted({x[2] for x in v})):>11s}")
    ca = {x[0] for l in by for x in by[l] if want[l]=='A'}
    cb = {x[0] for l in by for x in by[l] if want[l]=='B'}
    print(f"\ncrop-mix separates A from B: {not (ca & cb)}")
    if ca & cb: print("   shared crop signatures:", ca & cb)

if __name__ == "__main__":
    mp.freeze_support(); main()
