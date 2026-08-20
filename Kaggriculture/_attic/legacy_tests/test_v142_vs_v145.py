import os
from kaggle_environments import make

agent_142 = "a_v142_surgical_dominance.py"
agent_145 = "a_v145_mastery.py"

print("=======================================================")
print("HEAD-TO-HEAD BATTLE: v142 vs v145 Mastery (6 Games)")
print("=======================================================")

v142_wins = 0
v145_wins = 0
v142_total_score = 0
v145_total_score = 0

for i in range(6):
    env = make("kaggriculture", configuration={"episodeSteps": 720})
    if i % 2 == 0:
        # v145 is P0, v142 is P1
        env.run([agent_145, agent_142])
        s145, s142 = env.steps[-1][0].reward, env.steps[-1][1].reward
        print(f"Game {i+1}: v145 (P0) = {s145:.0f} vs v142 (P1) = {s142:.0f} -> {'v145 WON!' if s145 > s142 else 'v142 WON!'}")
    else:
        # v142 is P0, v145 is P1
        env.run([agent_142, agent_145])
        s142, s145 = env.steps[-1][0].reward, env.steps[-1][1].reward
        print(f"Game {i+1}: v142 (P0) = {s142:.0f} vs v145 (P1) = {s145:.0f} -> {'v145 WON!' if s145 > s142 else 'v142 WON!'}")
    
    v142_total_score += s142
    v145_total_score += s145
    if s145 > s142:
        v145_wins += 1
    elif s142 > s145:
        v142_wins += 1

print("\n=======================================================")
print(f"FINAL HEAD-TO-HEAD SCORE: v145: {v145_wins} wins | v142: {v142_wins} wins")
print(f"Total Aggregate Coins: v145 = ${v145_total_score:,.0f} | v142 = ${v142_total_score:,.0f} (Margin: {v145_total_score - v142_total_score:+,.0f})")
print("=======================================================")
