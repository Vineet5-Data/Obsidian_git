import json
import os
from kaggle_environments import make

AGENT_PATH = "a_v142_surgical_dominance.py"
REPLAYS = [
    ("Episode 93081881", r"C:\Users\Vinee\Downloads\93081881.json"),
    ("Episode 93084812", r"C:\Users\Vinee\Downloads\93084812.json")
]

for name, path in REPLAYS:
    print(f"\n=======================================================")
    print(f"Testing against {name} ({path})")
    print(f"=======================================================")
    with open(path, "r", encoding="utf-8") as f:
        replay_data = json.load(f)
    
    steps = replay_data["steps"]
    orig_scores = [s.get("reward") for s in steps[-1]]
    print(f"Original match scores: Seat 0 = {orig_scores[0]}, Seat 1 = {orig_scores[1]}")
    
    def make_tape_agent(steps_ref, seat):
        def tape_agent(obs, config=None):
            step = obs["step"]
            if step + 1 < len(steps_ref):
                raw = steps_ref[step + 1][seat].get("action")
                if isinstance(raw, dict):
                    return raw
            return {"farmer": ["PASS"], "hands": [], "market": []}
        return tape_agent

    # Test 1: v142 playing as Seat 1 vs Seat 0 tape (the winner of the original replay)
    opp_p0_tape = make_tape_agent(steps, 0)
    env1 = make("kaggriculture", configuration={"episodeSteps": 720})
    env1.run([opp_p0_tape, AGENT_PATH])
    s0, s1 = env1.steps[-1][0].reward, env1.steps[-1][1].reward
    print(f"\n--- Match 1: Opponent Tape (Seat 0) vs v142 (Seat 1) ---")
    print(f"  Opponent Tape: {s0}")
    print(f"  v142: {s1}")
    print(f"  Result: {'v142 WON (Beat Opponent!)' if s1 > s0 else 'Opponent Tape WON'} (Margin: {s1 - s0:+.0f})")

    # Test 2: v142 playing as Seat 0 vs Seat 1 tape
    opp_p1_tape = make_tape_agent(steps, 1)
    env2 = make("kaggriculture", configuration={"episodeSteps": 720})
    env2.run([AGENT_PATH, opp_p1_tape])
    s0, s1 = env2.steps[-1][0].reward, env2.steps[-1][1].reward
    print(f"\n--- Match 2: v142 (Seat 0) vs Opponent Tape (Seat 1) ---")
    print(f"  v142: {s0}")
    print(f"  Opponent Tape: {s1}")
    print(f"  Result: {'v142 WON (Beat Opponent!)' if s0 > s1 else 'Opponent Tape WON'} (Margin: {s0 - s1:+.0f})")
