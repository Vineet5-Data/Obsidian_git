import json
import glob
from kaggle_environments import make

AGENTS = [
    "a_v140_market_dominance.py",
    "a_v142_surgical_dominance.py",
    "a_v152_sweet_spot_v2.py",
    "a_v163_sweet_spot_v3.py"
]

files = [
    r"C:\Users\Vinee\Downloads\93084812.json",
    r"C:\Users\Vinee\Downloads\93084013.json",
    r"C:\Users\Vinee\Downloads\93088274.json",
    r"C:\Users\Vinee\Downloads\93085487.json",
    r"C:\Users\Vinee\Downloads\93081881.json",
    r"C:\Users\Vinee\Downloads\93089211.json",
    r"C:\Users\Vinee\Downloads\93087343.json",
    r"C:\Users\Vinee\Downloads\92255956.json"
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

results = {a: {"wins": 0, "total_margin": 0, "scores": []} for a in AGENTS}

print("=======================================================")
print(f"BENCHMARKING {len(AGENTS)} AGENTS ON {len(files)} TOP REPLAYS")
print("=======================================================")

for path in files:
    name = path.split('\\')[-1]
    with open(path, "r", encoding="utf-8") as f:
        replay_data = json.load(f)
    steps = replay_data["steps"]
    
    rewards = [s['reward'] for s in steps[-1]]
    opp_seat = 0 if rewards[0] > rewards[1] else 1
    test_seat = 1 - opp_seat
    
    print(f"\n--- Replay: {name} (Opponent played seat {opp_seat}, their score: {rewards[opp_seat]:.0f}) ---")
    
    for agent in AGENTS:
        agents = [None, None]
        agents[opp_seat] = make_tape_agent(steps, opp_seat)
        agents[test_seat] = agent
        
        env = make("kaggriculture", configuration={"episodeSteps": 720})
        env.run(agents)
        s_test = env.steps[-1][test_seat].reward
        s_opp = env.steps[-1][opp_seat].reward
        
        margin = s_test - s_opp
        if s_test > s_opp:
            res = "WON!"
            results[agent]["wins"] += 1
        else:
            res = "LOST"
            
        results[agent]["total_margin"] += margin
        results[agent]["scores"].append(s_test)
        
        print(f"{agent:30} : {s_test:7.0f} vs {s_opp:7.0f} -> {res} (Margin: {margin:+7.0f})")

print("\n=======================================================")
print("FINAL SUMMARY")
print("=======================================================")
for agent in AGENTS:
    wins = results[agent]["wins"]
    avg_score = sum(results[agent]["scores"]) / len(files)
    avg_margin = results[agent]["total_margin"] / len(files)
    print(f"{agent:30} : {wins}/{len(files)} Wins | Avg Score: {avg_score:.0f} | Avg Margin: {avg_margin:+.0f}")
