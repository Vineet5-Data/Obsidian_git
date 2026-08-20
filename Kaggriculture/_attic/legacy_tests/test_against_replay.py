import json
import sys
from kaggle_environments import make

REPLAY_PATH = r"C:\Users\Vinee\Downloads\93084013.json"
AGENT_PATH = "a_v142_surgical_dominance.py"

with open(REPLAY_PATH, "r", encoding="utf-8") as f:
    replay_data = json.load(f)

steps = replay_data["steps"]

def create_tape_agent(seat):
    def tape_agent(obs, config=None):
        step = obs["step"]
        if step + 1 < len(steps):
            raw = steps[step + 1][seat].get("action")
            if isinstance(raw, dict):
                return raw
        return {"farmer": ["PASS"], "hands": [], "market": []}
    return tape_agent

p0_tape = create_tape_agent(0)
p1_tape = create_tape_agent(1)

print("--- Testing a_v142_surgical_dominance against 93084013 Replay Players ---")

# Match 1: v142 (Seat 0) vs Replay P1 (Seat 1 - Winner of 93084013)
env1 = make("kaggriculture", configuration={"episodeSteps": 720})
env1.run([AGENT_PATH, p1_tape])
r1_0, r1_1 = env1.steps[-1][0].reward, env1.steps[-1][1].reward
print(f"Match 1 [v142 (Seat 0) vs Top Player Tape (Seat 1)]:")
print(f"  v142: {r1_0}")
print(f"  Top Player Tape: {r1_1}")
print(f"  Winner: {'v142' if r1_0 > r1_1 else 'Top Player Tape'}")

# Match 2: Top Player Tape (Seat 0) vs v142 (Seat 1)
# For this, we use P0's tape if played as Seat 0 or P1's tape adjusted for Seat 0
env2 = make("kaggriculture", configuration={"episodeSteps": 720})
env2.run([p0_tape, AGENT_PATH])
r2_0, r2_1 = env2.steps[-1][0].reward, env2.steps[-1][1].reward
print(f"\nMatch 2 [Player 0 Tape (Seat 0) vs v142 (Seat 1)]:")
print(f"  Player 0 Tape: {r2_0}")
print(f"  v142: {r2_1}")
print(f"  Winner: {'v142' if r2_1 > r2_0 else 'Player 0 Tape'}")

print("\n--- Summary ---")
print(f"v142 Scores: {r1_0} (as Seat 0), {r2_1} (as Seat 1)")
print(f"Replay Original Scores were: 110,824 (Seat 0) vs 118,144 (Seat 1)")
