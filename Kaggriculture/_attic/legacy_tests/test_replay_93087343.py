import json
from kaggle_environments import make

REPLAY_PATH = r"C:\Users\Vinee\Downloads\93087343.json"
AGENT_PATH = "a_v142_surgical_dominance.py"

with open(REPLAY_PATH, "r", encoding="utf-8") as f:
    replay_data = json.load(f)

steps = replay_data["steps"]
orig_scores = [s.get("reward") for s in steps[-1]]
print(f"=== Replay 93087343 ===")
print(f"Original match scores: Seat 0 = {orig_scores[0]:.0f}, Seat 1 = {orig_scores[1]:.0f}")

shops = steps[-1][0]["observation"]["town"]["unlocked_shops"]
print("Unlocked Shops:", shops)

def make_tape(seat):
    def tape_agent(obs, config=None):
        step = obs["step"]
        if step + 1 < len(steps):
            raw = steps[step + 1][seat].get("action")
            if isinstance(raw, dict):
                return raw
        return {"farmer": ["PASS"], "hands": [], "market": []}
    return tape_agent

# Match 1: Opponent Tape (Seat 0) vs v142 (Seat 1)
env1 = make("kaggriculture", configuration={"episodeSteps": 720})
env1.run([make_tape(0), AGENT_PATH])
s0, s1 = env1.steps[-1][0].reward, env1.steps[-1][1].reward
res1 = "v142 WON!" if s1 > s0 else "Opponent Tape WON"
print("\n--- Match 1: Opponent Seat 0 Tape vs v142 Seat 1 ---")
print(f"  Opponent: {s0:.0f} | v142: {s1:.0f} -> {res1} (Margin: {s1 - s0:+.0f})")

# Match 2: v142 (Seat 0) vs Opponent Seat 1 Tape
env2 = make("kaggriculture", configuration={"episodeSteps": 720})
env2.run([AGENT_PATH, make_tape(1)])
s0, s1 = env2.steps[-1][0].reward, env2.steps[-1][1].reward
res2 = "v142 WON!" if s0 > s1 else "Opponent Tape WON"
print("\n--- Match 2: v142 Seat 0 vs Opponent Seat 1 Tape ---")
print(f"  v142: {s0:.0f} | Opponent: {s1:.0f} -> {res2} (Margin: {s0 - s1:+.0f})")
