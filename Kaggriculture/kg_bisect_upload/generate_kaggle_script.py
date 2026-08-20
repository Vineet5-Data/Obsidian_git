import json

with open('archetypes.json') as f:
    archetypes = f.read()

with open('seed_demands.json') as f:
    seed_demands = f.read()

with open('v97_cap70.py') as f:
    v97_code = f.read()

script = f'''
import os
import json
from multiprocessing import Pool
import importlib.util

# 1. Create the base files locally
archetypes = json.loads({repr(archetypes)})
seed_demands = json.loads({repr(seed_demands)})
v97_code = {repr(v97_code)}

lines = v97_code.split("\\n")
start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if line.startswith('    elif day < 3:') and 'animal_target = 4' in lines[i+1]:
        start_idx = i
    if line.startswith('    remaining_crop_slots = crop_slots - sum(want_crop.values())'):
        end_idx = i
        break

for arch_idx in range(10):
    loader_code = f"""
    import json
    if not hasattr(obs, 'archetypes'):
        obs.archetypes = {{archetypes}}
        
    ACTIVE_SPEC = obs.archetypes[{{arch_idx}}]
    
    spec_animals = ACTIVE_SPEC.get('animals', {{{{}}}})
    animal_target = sum(spec_animals.values())
    animal_need = max(0, animal_target - len(beasts) - pending_animals)
    structure_need = min(slots, max(0, animal_target - current_animal_assets))
    
    want_animal = {{{{}}}}
    for name, target in spec_animals.items():
        owned = (own_animal_counts.get(name, 0)
                 + int(shed.get(name, 0) or 0)
                 + int(carried_all.get(name, 0) or 0))
        if target > owned:
            want_animal[name] = target - owned
            
    crop_slots = max(0, min(60, slots - structure_need))
    want_crop = {{{{}}}}
    spec_crops = ACTIVE_SPEC.get('crops', {{{{}}}})
    for crop, ratio in spec_crops.items():
        target = int(round(crop_slots * ratio))
        already = own_crop_counts.get(crop, 0)
        if target > already:
            want_crop[crop] = target - already
"""
    new_lines = lines[:start_idx] + [loader_code] + lines[end_idx:]
    with open(f'arch_agent_{{arch_idx}}.py', 'w') as f:
        f.write("\\n".join(new_lines))


# 2. Run the tournament
seeds = [int(k) for k in seed_demands.keys()]

def get_focus(spec):
    crops = spec.get('crops', {{}})
    animals = spec.get('animals', {{}})
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

_cache = {{}}
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
    path_i = f"arch_agent_{{idx_i}}.py"
    path_j = f"arch_agent_{{idx_j}}.py"
    
    from kaggle_environments import make
    ours = load(path_i)
    theirs = load(path_j)
    
    env = make("kaggriculture", configuration={{"episodeSteps": 720, "seed": seed}})
    pair = [ours, theirs] if seat == 0 else [theirs, ours]
    env.run(pair)
    last = env.steps[-1]
    
    r_ours = last[0].reward if seat == 0 else last[1].reward
    r_theirs = last[1].reward if seat == 0 else last[0].reward
    margin = (r_ours or 0) - (r_theirs or 0)
    return idx_i, idx_j, seed, seat, margin

jobs = []
for i in range(10):
    for j in range(10):
        for seed in seeds:
            for seat in (0, 1):
                jobs.append((i, j, seed, seat))
                
print(f"Starting {{len(jobs)}} jobs...")
workers = max(1, (os.cpu_count() or 4) - 1)
with Pool(workers) as pool:
    out = pool.map(play, jobs, chunksize=4)
    
print("Games finished, computing payoff matrix...")
margins = {{}}
for i, j, seed, seat, margin in out:
    td = seed_demands[str(seed)]
    of = opp_foci[j]
    key = (td, of, i)
    if key not in margins: margins[key] = []
    margins[key].append(margin)
    
payoff_matrix = {{}}
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
    payoff_matrix[f"{{td}}_{{of}}"] = best_i
    
print("\\n\\n========= FINAL PAYOFF.JSON =========")
print(json.dumps(payoff_matrix, indent=2))
print("=====================================")
'''

with open('kaggle_tpu_runner.py', 'w') as f:
    f.write(script)
