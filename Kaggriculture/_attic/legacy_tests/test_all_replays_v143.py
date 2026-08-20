import json
from kaggle_environments import make

AGENT_PATH = "a_v143_omnipotent.py"
REPLAYS = [
    ("Episode 93081881", r"C:\Users\Vinee\Downloads\93081881.json"),
    ("Episode 93084812", r"C:\Users\Vinee\Downloads\93084812.json"),
    ("Episode 93085487", r"C:\Users\Vinee\Downloads\93085487.json"),
    ("Episode 93084013", r"C:\Users\Vinee\Downloads\93084013.json")
]

def make_tape_agent(steps_ref, seat):
    def tape_agent(obs, config=None):
        step = obs["step"]
        if step + 1 < len(steps_ref):
            raw = steps_ref[step + 1][seat].get("action")
            if isinstance(raw, dict):
                return raw
        return {"farmer": ["PASS"], "hands": [], "market": []}
    return tape_agent

total_v143_wins = 0
total_matches = 0

for name, path in REPLAYS:
    print(f"\n=======================================================")
    print(f"Testing a_v143_omnipotent against {name}")
    print(f"=======================================================")
    with open(path, "r", encoding="utf-8") as f:
        replay_data = json.load(f)
    
    steps = replay_data["steps"]
    orig_scores = [s.get("reward") for s in steps[-1]]
    print(f"Original match scores: Seat 0 = {orig_scores[0]:.0f}, Seat 1 = {orig_scores[1]:.0f}")
    
    # Match 1: Opponent Tape (Seat 0) vs v143 (Seat 1)
    opp_p0 = make_tape_agent(steps, 0)
    env1 = make("kaggriculture", configuration={"episodeSteps": 720})
    env1.run([opp_p0, AGENT_PATH])
    s0, s1 = env1.steps[-1][0].reward, env1.steps[-1][1].reward
    w1 = "v143 WON!" if s1 > s0 else "Opponent Tape WON"
    print(f"--- Match 1: Opponent (Seat 0) vs v143 (Seat 1) ---")
    print(f"  Opponent: {s0:.0f} | v143: {s1:.0f} -> {w1} (Margin: {s1 - s0:+.0f})")
    if s1 > s0: total_v143_wins += 1
    total_matches += 1

    # Match 2: v143 (Seat 0) vs Opponent Tape (Seat 1)
    opp_p1 = make_tape_agent(steps, 1)
    env2 = make("kaggriculture", configuration={"episodeSteps": 720})
    env2.run([AGENT_PATH, opp_p1])
    s0, s1 = env2.steps[-1][0].reward, env2.steps[-1][1].reward
    w2 = "v143 WON!" if s0 > s1 else "Opponent Tape WON"
    print(f"--- Match 2: v143 (Seat 0) vs Opponent (Seat 1) ---")
    print(f"  v143: {s0:.0f} | Opponent: {s1:.0f} -> {w2} (Margin: {s0 - s1:+.0f})")
    if s0 > s1: total_v143_wins += 1
    total_matches += 1

print("\n=======================================================")
print(f"FINAL REPLAY TOURNAMENT TALLY: v143 Won {total_v143_wins} / {total_matches} matches ({total_v143_wins/total_matches*100:.1f}%)")
print("=======================================================")
