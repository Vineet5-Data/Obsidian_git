"""Unbeatable against the KNOWN 6 is not unbeatable.  Test all 41 routes as rivals.

v33 is 576-0-0 across the 6-opponent panel on calibration and held-out seeds.
But the classifier only ever had to separate six archetypes, and unknown rivals
fall through to route A (93.8% alone).  Every route in .field/ and .loss/ is a
real ladder agent, so run them all.
"""
import glob, importlib.util, multiprocessing as mp, os, statistics, sys

def load(p, n):
    s = importlib.util.spec_from_file_location(n, p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def one(job):
    me, path, seed, seat = job
    from kaggle_environments import make
    tag = f"{abs(hash(path))%99999}_{seed}_{seat}_{os.getpid()}"
    try:
        a = load(me, "a_" + tag).agent
        b = load(path, "b_" + tag).agent
    except Exception:
        return path, None
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run([a, b] if seat == 0 else [b, a])
    f = env.steps[-1]
    return path, f[seat].reward - f[1 - seat].reward

def main():
    me = sys.argv[1] if len(sys.argv) > 1 else "v33.py"
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, n + 1)]
    opps = sorted(glob.glob(".field/f_*.py")) + sorted(glob.glob(".loss/o_*.py"))
    opps += ["wufang_agent.py"] if os.path.exists("wufang_agent.py") else []
    jobs = [(me, p, s, seat) for p in opps for s in seeds for seat in (0, 1)]
    print(f"{me} vs {len(opps)} rival routes x {n} seeds x 2 seats = {len(jobs)} games", flush=True)
    with mp.Pool(max(1, (os.cpu_count() or 4) - 2)) as pool:
        res = pool.map(one, jobs)
    t = {}
    for p, m in res:
        if m is not None: t.setdefault(p, []).append(m)
    losers, grand = [], []
    for p, v in t.items():
        grand += v
        l = sum(1 for m in v if m <= 0)
        if l: losers.append((l, min(v), p))
    w = sum(1 for m in grand if m > 0)
    print(f"\nOVERALL {w}-{len(grand)-w}  ({100*w/len(grand):.1f}%)  "
          f"mean {statistics.mean(grand):+,.0f}  worst {min(grand):+,.0f}")
    print(f"rival routes that beat us at least once: {len(losers)}/{len(t)}")
    for l, worst, p in sorted(losers, reverse=True):
        print(f"   {os.path.basename(p):28s} {l}/{2*n} losses  worst {worst:+,.0f}")

if __name__ == "__main__":
    mp.freeze_support(); main()
