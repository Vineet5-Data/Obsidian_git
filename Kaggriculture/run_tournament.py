import os
import sys
from kaggle_environments import make

agents = [
    ("v139 Subagent Optimized", "a_v139_subagent_optimized.py"),
    ("v140 Market Dominance", "a_v140_market_dominance.py")
]

results = {agent[0]: 0 for agent in agents}
matchups = [
    (agents[0], agents[1]),
    (agents[1], agents[0])
]

print(f"Running {len(matchups)} matches...")

for a1, a2 in matchups:
    print(f"\nMatch: {a1[0]} (P1) vs {a2[0]} (P2)")
    env = make("kaggriculture", configuration={"episodeSteps": 720}, debug=True)
    env.run([a1[1], a2[1]])
    
    final_state = env.steps[-1]
    r1 = final_state[0].reward
    r2 = final_state[1].reward
    
    print(f"Result: {a1[0]}: {r1}, {a2[0]}: {r2}")
    
    if r1 > r2:
        print(f"Winner: {a1[0]}")
        results[a1[0]] += 1
    elif r2 > r1:
        print(f"Winner: {a2[0]}")
        results[a2[0]] += 1
    else:
        print("Draw!")

print("\n--- Match Results ---")
for name, wins in sorted(results.items(), key=lambda x: -x[1]):
    print(f"{name}: {wins} wins")
