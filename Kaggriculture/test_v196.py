import os
import glob
import multiprocessing as mp
import time
from kaggle_environments import make

def load(path):
    import importlib.util
    spec = importlib.util.spec_from_file_location("m_" + os.path.basename(path).replace(".", "_"), path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.agent

def one(job):
    agent_path, opp_path, seed, seat = job
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    pair = [load(agent_path), load(opp_path)] if seat == 0 else [load(opp_path), load(agent_path)]
    env.run(pair)
    margin = env.steps[-1][seat].reward - env.steps[-1][1-seat].reward
    return {"win": margin > 0, "margin": margin}

if __name__ == "__main__":
    mp.freeze_support()
    agent = "a_v200.py"
    # Find .top opponents in the C:\Users\Vinee\Desktop\Kaggriculture directory or its subdirs
    opps = glob.glob(".top/t_*.py")
    if not opps:
        opps = glob.glob("t_*.py")
    if not opps:
        print("No .top/t_*.py opponents found.")
        import sys; sys.exit(1)
        
    opps = sorted(opps)[:5] # use first 5 for a quick 10-game test
    seeds = [12345]
    jobs = []
    for o in opps:
        for s in seeds:
            jobs.append((agent, o, s, 0))
            jobs.append((agent, o, s, 1))
            
    print(f"Queueing {len(jobs)} games for {agent} vs {len(opps)} top opponents...", flush=True)
    t0 = time.time()
    results = []
    with mp.Pool(max(1, os.cpu_count() - 2)) as pool:
        for n, r in enumerate(pool.imap(one, jobs), 1):
            results.append(r)
            job_idx = n - 1
            o = jobs[job_idx][1]
            s = jobs[job_idx][2]
            seat = jobs[job_idx][3]
            print(f"[{n}/10] {o} (seed {s}, seat {seat}): {r['margin']:.0f}")
                
    wins = sum(1 for r in results if r["win"])
    mean_margin = sum(r["margin"] for r in results) / len(results)
    print(f"\n{agent} vs top: {wins}-{len(results)-wins} ({100.0*wins/len(results):.1f}%)")
    print(f"Mean margin: {mean_margin:+.1f}")
