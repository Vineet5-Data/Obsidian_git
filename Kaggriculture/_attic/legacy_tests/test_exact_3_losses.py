import json
from kaggle_environments import make

AGENT_PATH = "a_v143_omnipotent.py"
REPLAYS = [
    ("Episode 93087343", r"C:\Users\Vinee\Downloads\93087343.json", 0),  # v142 was Seat 0
    ("Episode 93088274", r"C:\Users\Vinee\Downloads\93088274.json", 0),  # v142 was Seat 0
    ("Episode 93089211", r"C:\Users\Vinee\Downloads\93089211.json", 1),  # v142 was Seat 1
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

for name, path, v142_seat in REPLAYS:
    print(f"\n=======================================================")
    print(f"Testing a_v143_omnipotent on {name} (where v142 was Seat {v142_seat})")
    print(f"=======================================================")
    with open(path, "r", encoding="utf-8") as f:
        replay_data = json.load(f)
    
    steps = replay_data["steps"]
    orig_scores = [s.get("reward") for s in steps[-1]]
    opp_seat = 1 - v142_seat
    print(f"Original match: v142 = {orig_scores[v142_seat]:.0f} vs Opponent = {orig_scores[opp_seat]:.0f} (Lost by {orig_scores[opp_seat] - orig_scores[v142_seat]:.0f})")
    
    # Run v143 in the exact seat where v142 played against the opponent tape
    agents = [None, None]
    agents[opp_seat] = make_tape_agent(steps, opp_seat)
    agents[v142_seat] = AGENT_PATH
    
    env = make("kaggriculture", configuration={"episodeSteps": 720})
    env.run(agents)
    s_v143 = env.steps[-1][v142_seat].reward
    s_opp = env.steps[-1][opp_seat].reward
    res = "v143 WON!" if s_v143 > s_opp else "Opponent WON"
    print(f"Replay Match (v143 in Seat {v142_seat}):")
    print(f"  v143 Score: {s_v143:.0f} | Opponent Score: {s_opp:.0f}")
    print(f"  Result: {res} (Margin: {s_v143 - s_opp:+.0f})")
