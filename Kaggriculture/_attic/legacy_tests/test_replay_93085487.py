import json
from kaggle_environments import make

REPLAY_PATH = r"C:\Users\Vinee\Downloads\93085487.json"
AGENT_PATH = "a_v142_surgical_dominance.py"

with open(REPLAY_PATH, "r", encoding="utf-8") as f:
    replay_data = json.load(f)

steps = replay_data["steps"]
print("Original match scores: Seat 0 = 97,174 vs Seat 1 = 76,686 (Loss by -20,488)")

def make_tape(seat):
    def tape_agent(obs, config=None):
        step = obs["step"]
        if step + 1 < len(steps):
            raw = steps[step + 1][seat].get("action")
            if isinstance(raw, dict):
                return raw
        return {"farmer": ["PASS"], "hands": [], "market": []}
    return tape_agent

# Match 1: Opponent Tape (Seat 0 - winner with 97k) vs v142 (Seat 1)
env1 = make("kaggriculture", configuration={"episodeSteps": 720})
env1.run([make_tape(0), AGENT_PATH])
s0, s1 = env1.steps[-1][0].reward, env1.steps[-1][1].reward
print("\n--- Match 1: Opponent Seat 0 Tape vs v142 Seat 1 ---")
print(f"  Opponent Tape: {s0}")
print(f"  v142: {s1}")
res1 = "v142 WON!" if s1 > s0 else "Opponent Tape WON"
print(f"  Result: {res1} (Margin: {s1 - s0:+.0f})")

# Match 2: v142 (Seat 0) vs Opponent Seat 1 Tape
env2 = make("kaggriculture", configuration={"episodeSteps": 720})
env2.run([AGENT_PATH, make_tape(1)])
s0, s1 = env2.steps[-1][0].reward, env2.steps[-1][1].reward
print("\n--- Match 2: v142 Seat 0 vs Opponent Seat 1 Tape ---")
print(f"  v142: {s0}")
print(f"  Opponent Tape: {s1}")
res2 = "v142 WON!" if s0 > s1 else "Opponent Tape WON"
print(f"  Result: {res2} (Margin: {s0 - s1:+.0f})")
