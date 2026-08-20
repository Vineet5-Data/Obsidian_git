"""Route search on the CORRECT engine (1.32.6) against the REAL ladder opponents.

Everything before this was computed on 1.32.4, where verbatim replay of the six
real games does not reproduce.  Under 1.32.6 all six reproduce exactly, so this
is the first valid route comparison.

Candidates include the six current ladder routes themselves -- the two
wheat-heavy builds (1,280 and 1,902 wheat sold) are the only ones still beating
v33, and wheat is the good whose price the town drain lifts.
"""
import glob, importlib.util, multiprocessing as mp, os, statistics

def load(p, n):
    s = importlib.util.spec_from_file_location(n, p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

OPPS = sorted(glob.glob(".pure/p_*.py"))
CANDS = ["v33.py", ".loss/o_90729118.py", ".field/f_90635979_p1.py"] + \
        [f"v27_tape_{os.path.basename(p)[2:-3]}" for p in []]
CANDS += sorted(glob.glob("v27_losses/*.json"))   # marker: use extracted tapes

def tape_of(path, tag):
    """Return an _ACTIONS list for a candidate given as agent file or replay."""
    if path.endswith(".json"):
        ep = os.path.basename(path).split(".")[0]
        return load(f".pure/p_{ep}.py", "t_" + tag)._ACTIONS
    return load(path, "t_" + tag)._ACTIONS

def one(job):
    cand, opp, seed, seat = job
    from kaggle_environments import make
    tag = f"{abs(hash(cand))%99999}_{abs(hash(opp))%9999}_{seed}_{seat}_{os.getpid()}"
    try:
        m = load("v33.py", "a_" + tag)
        if cand != "v33.py":
            t = tape_of(cand, tag)
            m._ROUTE_A = t
            m._ACTIONS = t
        b = load(opp, "o_" + tag).agent
    except Exception:
        return (cand, opp), None
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run([m.agent, b] if seat == 0 else [b, m.agent])
    f = env.steps[-1]
    return (cand, opp), f[seat].reward - f[1 - seat].reward

def main():
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, 5)]
    jobs = [(c, o, s, seat) for c in CANDS for o in OPPS
            for s in seeds for seat in (0, 1)]
    print(f"{len(CANDS)} candidate routes x {len(OPPS)} real opponents x "
          f"{len(seeds)} seeds x 2 seats = {len(jobs)} games", flush=True)
    with mp.Pool(max(1, (os.cpu_count() or 4) - 2)) as pool:
        res = pool.map(one, jobs)
    t = {}
    for k, v in res:
        if v is not None: t.setdefault(k, []).append(v)
    rows = []
    for c in CANDS:
        cells, tot, grand = [], 0, []
        ok = True
        for o in OPPS:
            v = t.get((c, o), [])
            if not v: ok = False; break
            grand += v
            n = sum(1 for x in v if x <= 0); tot += n
            cells.append(f"{len(v)-n}/{len(v)}")
        if ok:
            rows.append((tot, -statistics.mean(grand), c, cells, min(grand),
                         statistics.mean(grand)))
    rows.sort(key=lambda r: (r[0], r[1]))
    print(f"\n{'candidate route':26s}" + "".join(f"{os.path.basename(o)[2:10]:>10s}" for o in OPPS)
          + f"{'LOSS':>6s}{'worst':>10s}{'mean':>11s}")
    for tot, _, c, cells, worst, mean in rows:
        name = os.path.basename(c).replace(".json", "*").replace(".py", "")
        print(f"{name:26s}" + "".join(x.rjust(10) for x in cells)
              + f"{tot:>6d}{worst:>+10,.0f}{mean:>+11,.0f}")

if __name__ == "__main__":
    mp.freeze_support(); main()
