import os
from kaggle_environments import make

agent_142 = "a_v142_surgical_dominance.py"
agent_143 = "a_v143_omnipotent.py"

print("=======================================================")
print("HEAD-TO-HEAD BATTLE: v142 vs Refined v143 (6 Games)")
print("=======================================================")

v142_wins = 0
v143_wins = 0
v142_total_score = 0
v143_total_score = 0

for i in range(6):
    env = make("kaggriculture", configuration={"episodeSteps": 720})
    if i % 2 == 0:
        # v143 is P0, v142 is P1
        env.run([agent_143, agent_142])
        s143, s142 = env.steps[-1][0].reward, env.steps[-1][1].reward
        print(f"Game {i+1}: v143 (P0) = {s143:.0f} vs v142 (P1) = {s142:.0f} -> {'v143 WON!' if s143 > s142 else 'v142 WON!'}")
    else:
        # v142 is P0, v143 is P1
        env.run([agent_142, agent_143])
        s142, s143 = env.steps[-1][0].reward, env.steps[-1][1].reward
        print(f"Game {i+1}: v142 (P0) = {s142:.0f} vs v143 (P1) = {s143:.0f} -> {'v143 WON!' if s143 > s142 else 'v142 WON!'}")
    
    v142_total_score += s142
    v143_total_score += s143
    if s143 > s142:
        v143_wins += 1
    elif s142 > s143:
        v142_wins += 1

print("\n=======================================================")
print(f"FINAL HEAD-TO-HEAD SCORE: v143: {v143_wins} wins | v142: {v142_wins} wins")
print(f"Total Aggregate Coins: v143 = ${v143_total_score:,.0f} | v142 = ${v142_total_score:,.0f} (Margin: {v143_total_score - v142_total_score:+,.0f})")
print("=======================================================")
