import os
import json
from multiprocessing import Pool
import importlib.util

# Load seeds and demands
with open('seed_demands.json') as f:
    seed_demands = json.load(f)

seeds = [int(k) for k in seed_demands.keys()]

# Load archetypes
with open('archetypes.json') as f:
    archetypes = json.load(f)

def get_focus(spec):
    crops = spec.get('crops', {})
    animals = spec.get('animals', {})
    c_val = sum(crops.values())
    a_val = sum(animals.values())
    if a_val > c_val:
        if animals.get('COW', 0) > animals.get('SHEEP', 0):
            return "MILK"
        return "WOOL"
    else:
        if crops.get('MELON', 0) > 0.2:
            return "MELON"
        return "STRAWBERRY"

opp_foci = [get_focus(arch) for arch in archetypes]

_cache = {}
def load(path):
    if path not in _cache:
        name = "m_" + os.path.splitext(os.path.basename(path))[0]
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        _cache[path] = mod.agent
    return _cache[path]

def play(job):
    idx_i, idx_j, seed, seat = job
    path_i = f"arch_agent_{idx_i}.py"
    path_j = f"arch_agent_{idx_j}.py"
    
    from kaggle_environments import make
    ours = load(path_i)
    theirs = load(path_j)
    
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    pair = [ours, theirs] if seat == 0 else [theirs, ours]
    env.run(pair)
    last = env.steps[-1]
    
    # We want margin of i over j
    r_ours = last[0].reward if seat == 0 else last[1].reward
    r_theirs = last[1].reward if seat == 0 else last[0].reward
    margin = (r_ours or 0) - (r_theirs or 0)
    
    return idx_i, idx_j, seed, seat, margin

def main():
    jobs = []
    for i in range(10):
        for j in range(10):
            for seed in seeds:
                for seat in (0, 1):
                    jobs.append((i, j, seed, seat))
                    
    print(f"Starting {len(jobs)} jobs...")
    
    # Use max workers
    workers = max(1, (os.cpu_count() or 4) - 1)
    with Pool(workers) as pool:
        out = pool.map(play, jobs, chunksize=4)
        
    print("Games finished, computing payoff matrix...")
    
    # Bucket by top_demand, opp_focus
    # For each, what is the best arch_i?
    
    # dict: (top_demand, opp_focus, arch_i) -> list of margins
    margins = {}
    
    for i, j, seed, seat, margin in out:
        td = seed_demands[str(seed)]
        of = opp_foci[j]
        
        key = (td, of, i)
        if key not in margins:
            margins[key] = []
        margins[key].append(margin)
        
    payoff_matrix = {}
    
    # Get all distinct (td, of) pairs
    td_of_pairs = set((td, of) for (td, of, i) in margins.keys())
    
    for td, of in td_of_pairs:
        best_i = 0
        best_avg = -float('inf')
        
        for i in range(10):
            key = (td, of, i)
            if key in margins:
                avg_margin = sum(margins[key]) / len(margins[key])
                if avg_margin > best_avg:
                    best_avg = avg_margin
                    best_i = i
                    
        payoff_matrix[f"{td}_{of}"] = best_i
        
    with open('payoff.json', 'w') as f:
        json.dump(payoff_matrix, f, indent=2)
        
    print(f"Generated payoff matrix: {len(payoff_matrix)} keys")
    unique_routes = len(set(payoff_matrix.values()))
    print(f"Unique optimal routes chosen: {unique_routes}")

if __name__ == '__main__':
    main()
