import os
from kaggle_environments import make

our_agent = "a_v144_pure_unleashed.py"
opponents = [
    ("v142 Surgical Dominance", "a_v142_surgical_dominance.py"),
    ("v140 Market Dominance", "a_v140_market_dominance.py"),
    ("v138 Competitive Counter", r"C:\Users\Vinee\Downloads\a_v138_competitive_counter.py"),
    ("v138 Hidden Wave", r"C:\Users\Vinee\Downloads\a_v138_hidden_wave_denial.py"),
    ("v128 Terminal Value", r"C:\Users\Vinee\Downloads\a_v128_terminal_value.py"),
    ("v126 Fertilizer Denial", r"C:\Users\Vinee\Downloads\a_v126_fertilizer_denial.py")
]

results = {"v144 Pure Unleashed": 0}
for opp in opponents:
    if os.path.exists(opp[1]):
        results[opp[0]] = 0

for opp_name, opp_path in opponents:
    if not os.path.exists(opp_path):
        print(f"Skipping {opp_name}, file not found.")
        continue
    
    print(f"\n--- Match: v144 Pure Unleashed (P1) vs {opp_name} (P2) ---")
    env = make("kaggriculture", configuration={"episodeSteps": 720})
    try:
        env.run([our_agent, opp_path])
        final = env.steps[-1]
        r1, r2 = final[0].reward, final[1].reward
        print(f"Result: v144: {r1}, {opp_name}: {r2}")
        if r1 > r2:
            results["v144 Pure Unleashed"] += 1
        elif r2 > r1:
            results[opp_name] += 1
    except Exception as e:
        print(f"Error running match: {e}")

    print(f"\n--- Match: {opp_name} (P1) vs v144 Pure Unleashed (P2) ---")
    env = make("kaggriculture", configuration={"episodeSteps": 720})
    try:
        env.run([opp_path, our_agent])
        final = env.steps[-1]
        r1, r2 = final[0].reward, final[1].reward
        print(f"Result: {opp_name}: {r1}, v144: {r2}")
        if r2 > r1:
            results["v144 Pure Unleashed"] += 1
        elif r1 > r2:
            results[opp_name] += 1
    except Exception as e:
        print(f"Error running match: {e}")

print("\n=== FINAL TOURNAMENT RESULTS ===")
for name, wins in sorted(results.items(), key=lambda x: -x[1]):
    print(f"{name}: {wins} wins")
