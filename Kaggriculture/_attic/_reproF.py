"""Reproduce the six real losses at their TRUE seeds, then re-fight with v30/v33.

Testing a replayed tape on an arbitrary seed is meaningless -- its scripted
actions only fit the state they were recorded in.  info.seed carries the real
one.  First check each loss reproduces; only then is a re-fight informative.
"""
import collections, glob, importlib.util, json, multiprocessing as mp, os

OURS = {"STRAWBERRY": 292, "WHEAT": 273, "MILK": 213, "FERTILIZER": 210}

def load(p, n):
    s = importlib.util.spec_from_file_location(n, p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def meta():
    out = []
    for path in sorted(glob.glob("v27_losses/*.json")):
        ep = os.path.basename(path).split(".")[0]
        rep = json.load(open(path, encoding="utf-8"))
        steps = rep["steps"]
        sold = [collections.Counter(), collections.Counter()]
        for i in range(len(steps) - 1):
            for seat in (0, 1):
                for o in ((steps[i+1][seat].get("action") or {}).get("market") or []):
                    if o and o[0] == "SELL" and len(o) >= 3:
                        sold[seat][o[1]] += int(o[2])
        us = 0 if all(sold[0].get(k) == v for k, v in OURS.items()) else 1
        out.append((ep, rep["info"]["seed"], us,
                    steps[-1][us].get("reward", 0), steps[-1][1-us].get("reward", 0)))
    return out

def one(job):
    agent_path, ep, seed, us = job
    from kaggle_environments import make
    tag = f"{os.path.basename(agent_path)}_{ep}_{os.getpid()}"
    a = load(agent_path, "a_" + tag).agent
    b = load(f".pure/p_{ep}.py", "b_" + tag).agent
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run([a, b] if us == 0 else [b, a])
    f = env.steps[-1]
    return agent_path, ep, f[us].reward, f[1-us].reward

def main():
    info = meta()
    agents = ["v27.py", "v30.py", "v33.py"]
    jobs = [(a, ep, seed, us) for a in agents for ep, seed, us, _, _ in info]
    with mp.Pool(max(1, (os.cpu_count() or 4) - 2)) as pool:
        res = pool.map(one, jobs)
    got = {(a, ep): (mine, theirs) for a, ep, mine, theirs in res}

    print(f"{'episode':11s}{'seed':>11s}{'REAL v27':>22s}{'sim v27':>22s}"
          f"{'sim v30':>22s}{'sim v33':>22s}")
    wins = collections.Counter()
    for ep, seed, us, real_us, real_them in info:
        cells = []
        for a in agents:
            m, t = got[(a, ep)]
            cells.append(f"{m:,.0f}/{t:,.0f} ({m-t:+,.0f})")
            if m > t: wins[a] += 1
        print(f"{ep:11s}{seed:>11d}"
              f"{f'{real_us:,.0f}/{real_them:,.0f} ({real_us-real_them:+,.0f})':>22s}"
              + "".join(c.rjust(22) for c in cells))
    print()
    for a in agents:
        print(f"{a:9s} wins {wins[a]}/{len(info)} at the real seeds")

if __name__ == "__main__":
    mp.freeze_support(); main()
