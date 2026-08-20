import itertools
import subprocess
import json
import time
import os

def kaggriculture_fib(n):
    a, b = 1, 1
    for _ in range(int(max(0, n))):
        a, b = b, a + b
    return float(a)

base_file = "v97_cap70.py"
with open(base_file, "r") as f:
    base_code = f.read()

hire_caps = [9, 10, 11]
cash_ratios = [0.10, 0.16, 0.22]
pressures = [0.60, 0.66, 0.70]

best_win_rate = -1
best_margin = -99999
best_params = None

grid = list(itertools.product(hire_caps, cash_ratios, pressures))
print(f"Starting Grid Search with {len(grid)} permutations...")
for idx, (hc, cr, pr) in enumerate(grid):
    code = base_code
    
    # Replace Hire Cap
    fib_cost = kaggriculture_fib(hc - 1)
    target_hire = 'if n_hired >= 10 and c > max(55.0, cash * 0.16):'
    new_hire = f'if n_hired >= {hc} and c > max({fib_cost}, cash * {cr}):'
    code = code.replace(target_hire, new_hire)
    
    # Replace Land Rush
    target_land = 'if (day >= unlock_day and pressure >= 0.66 and cash - c >= reserve'
    new_land = f'if (day >= unlock_day and pressure >= {pr} and cash - c >= reserve'
    code = code.replace(target_land, new_land)
    
    temp_agent = "grid_temp_agent.py"
    with open(temp_agent, "w") as f:
        f.write(code)
    
    out_json = "grid_temp_out.json"
    subprocess.run(["python", "top_tournament.py", temp_agent, "--json-out", out_json], capture_output=True)
    
    with open(out_json, "r") as f:
        res = json.load(f)
    
    wr = res["win_rate"]
    margin = res["mean_margin"]
    print(f"[{idx+1}/{len(grid)}] HC={hc}, CR={cr}, PR={pr} => WR: {wr:.3f}, Margin: {margin:.1f}")
    
    if wr > best_win_rate or (wr == best_win_rate and margin > best_margin):
        best_win_rate = wr
        best_margin = margin
        best_params = (hc, cr, pr)
        
    os.remove(temp_agent)
    os.remove(out_json)

print("\n=== GRID SEARCH COMPLETE ===")
print(f"Best Win Rate: {best_win_rate:.3f}")
print(f"Best Margin: {best_margin:.1f}")
print(f"Best Params: HIRE_CAP={best_params[0]}, CASH_RATIO={best_params[1]}, PRESSURE={best_params[2]}")
