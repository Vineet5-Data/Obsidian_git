from kaggle_environments import make

print("=======================================================")
print("HEAD-TO-HEAD: v26 (Rating 2867.8) vs v142 (8 Games)")
print("=======================================================")

v26_wins = 0
v142_wins = 0

v26_path = r"C:\Users\Vinee\Desktop\Kaggriculture\_attic\v26.py"
v142_path = "a_v142_surgical_dominance.py"

for i in range(8):
    env = make("kaggriculture", configuration={"episodeSteps": 720})
    if i % 2 == 0:
        env.run([v26_path, v142_path])
        s_v26, s_v142 = env.steps[-1][0].reward, env.steps[-1][1].reward
        res = "v26 WON!" if s_v26 > s_v142 else "v142 WON!"
        print(f"Game {i+1}: v26 (P0) = {s_v26:.0f} vs v142 (P1) = {s_v142:.0f} -> {res} (Margin: {s_v26 - s_v142:+.0f})")
    else:
        env.run([v142_path, v26_path])
        s_v142, s_v26 = env.steps[-1][0].reward, env.steps[-1][1].reward
        res = "v26 WON!" if s_v26 > s_v142 else "v142 WON!"
        print(f"Game {i+1}: v142 (P0) = {s_v142:.0f} vs v26 (P1) = {s_v26:.0f} -> {res} (Margin: {s_v26 - s_v142:+.0f})")
    if s_v26 > s_v142: v26_wins += 1
    else: v142_wins += 1

print(f"\nFinal Result: v26 = {v26_wins} Wins vs v142 = {v142_wins} Wins")
