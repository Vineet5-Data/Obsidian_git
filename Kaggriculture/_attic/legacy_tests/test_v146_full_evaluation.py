import json
from kaggle_environments import make

AGENT_PATH = "a_v146_apex_dominance.py"
REPLAYS = [
    ("Episode 93087343", r"C:\Users\Vinee\Downloads\93087343.json", 0),
    ("Episode 93088274", r"C:\Users\Vinee\Downloads\93088274.json", 0),
    ("Episode 93089211", r"C:\Users\Vinee\Downloads\93089211.json", 1),
    ("Episode 93084013", r"C:\Users\Vinee\Downloads\93084013.json", 0),
    ("Episode 93084812", r"C:\Users\Vinee\Downloads\93084812.json", 0),
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

print("=======================================================")
print("BENCHMARKING a_v146_apex_dominance AGAINST 5 TOP REPLAYS")
print("=======================================================")

v146_wins = 0
for name, path, seat in REPLAYS:
    with open(path, "r", encoding="utf-8") as f:
        replay_data = json.load(f)
    steps = replay_data["steps"]
    orig_scores = [s.get("reward") for s in steps[-1]]
    opp_seat = 1 - seat
    
    agents = [None, None]
    agents[opp_seat] = make_tape_agent(steps, opp_seat)
    agents[seat] = AGENT_PATH
    
    env = make("kaggriculture", configuration={"episodeSteps": 720})
    env.run(agents)
    s_v146 = env.steps[-1][seat].reward
    s_opp = env.steps[-1][opp_seat].reward
    res = "v146 WON!" if s_v146 > s_opp else "Opponent WON"
    if s_v146 > s_opp: v146_wins += 1
    print(f"{name} (Seat {seat}): v146 = {s_v146:.0f} vs Opponent = {s_opp:.0f} -> {res} (Margin: {s_v146 - s_opp:+.0f})")

print(f"\nTotal Replay Wins: {v146_wins} / {len(REPLAYS)}")

print("\n=======================================================")
print("HEAD-TO-HEAD: v146 Apex Dominance vs v142 (4 Games)")
print("=======================================================")
h2h_146 = 0
h2h_142 = 0
for i in range(4):
    env = make("kaggriculture", configuration={"episodeSteps": 720})
    if i % 2 == 0:
        env.run([AGENT_PATH, "a_v142_surgical_dominance.py"])
        s146, s142 = env.steps[-1][0].reward, env.steps[-1][1].reward
        print(f"H2H Game {i+1}: v146 (P0) = {s146:.0f} vs v142 (P1) = {s142:.0f} -> {'v146 WON!' if s146 > s142 else 'v142 WON!'}")
    else:
        env.run(["a_v142_surgical_dominance.py", AGENT_PATH])
        s142, s146 = env.steps[-1][0].reward, env.steps[-1][1].reward
        print(f"H2H Game {i+1}: v142 (P0) = {s142:.0f} vs v146 (P1) = {s146:.0f} -> {'v146 WON!' if s146 > s142 else 'v142 WON!'}")
    if s146 > s142: h2h_146 += 1
    else: h2h_142 += 1

print(f"H2H Result: v146: {h2h_146} wins vs v142: {h2h_142} wins")
