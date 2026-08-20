import json
from kaggle_environments import make

AGENTS = [
    ("v24 (Rating 2947.4)", r"C:\Users\Vinee\Desktop\Kaggriculture\_attic\v24.py"),
    ("v26 (Rating 2867.8)", r"C:\Users\Vinee\Desktop\Kaggriculture\_attic\v26.py"),
    ("v142 Surgical Dominance", "a_v142_surgical_dominance.py")
]

REPLAYS = [
    ("Episode 93087343", r"C:\Users\Vinee\Downloads\93087343.json", 0),
    ("Episode 93088274", r"C:\Users\Vinee\Downloads\93088274.json", 0),
    ("Episode 93089211", r"C:\Users\Vinee\Downloads\93089211.json", 1),
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

for agent_name, agent_path in AGENTS:
    print(f"\n=======================================================")
    print(f"EVALUATING {agent_name} ON 3 LIVE KAGGLE LOSS REPLAYS")
    print(f"=======================================================")
    total_wins = 0
    for name, path, seat in REPLAYS:
        with open(path, "r", encoding="utf-8") as f:
            replay_data = json.load(f)
        steps = replay_data["steps"]
        opp_seat = 1 - seat
        
        agents = [None, None]
        agents[opp_seat] = make_tape_agent(steps, opp_seat)
        agents[seat] = agent_path
        
        env = make("kaggriculture", configuration={"episodeSteps": 720})
        env.run(agents)
        s_agent = env.steps[-1][seat].reward
        s_opp = env.steps[-1][opp_seat].reward
        res = "WON!" if s_agent > s_opp else "LOST"
        if s_agent > s_opp: total_wins += 1
        print(f"  {name}: {agent_name} = {s_agent:.0f} vs Opponent = {s_opp:.0f} -> {res} (Margin: {s_agent - s_opp:+.0f})")
    print(f"Total Wins: {total_wins} / {len(REPLAYS)}")
