import json
from kaggle_environments import make

AGENT_PATH = "a_v151_sweet_spot.py"

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
print("BENCHMARKING a_v151_sweet_spot.py ON REPLAYS")
print("=======================================================")
v151_wins = 0
for name, path, seat in REPLAYS:
    with open(path, "r", encoding="utf-8") as f:
        replay_data = json.load(f)
    steps = replay_data["steps"]
    opp_seat = 1 - seat
    
    agents = [None, None]
    agents[opp_seat] = make_tape_agent(steps, opp_seat)
    agents[seat] = AGENT_PATH
    
    env = make("kaggriculture", configuration={"episodeSteps": 720})
    env.run(agents)
    s_v151 = env.steps[-1][seat].reward
    s_opp = env.steps[-1][opp_seat].reward
    res = "WON!" if s_v151 > s_opp else "LOST"
    if s_v151 > s_opp: v151_wins += 1
    print(f"{name}: v151 = {s_v151:.0f} vs Opponent = {s_opp:.0f} -> {res} (Margin: {s_v151 - s_opp:+.0f})")

print(f"\nTotal Replay Wins: {v151_wins} / {len(REPLAYS)}")

print("\n=======================================================")
print("HEAD-TO-HEAD: v151 vs v140 (4 Games)")
print("=======================================================")
h2h_151 = 0
h2h_140 = 0
for i in range(4):
    env = make("kaggriculture", configuration={"episodeSteps": 720})
    if i % 2 == 0:
        env.run([AGENT_PATH, "a_v140_market_dominance.py"])
        s151, s140 = env.steps[-1][0].reward, env.steps[-1][1].reward
        print(f"H2H Game {i+1}: v151 (P0) = {s151:.0f} vs v140 (P1) = {s140:.0f} -> {'v151 WON!' if s151 > s140 else 'v140 WON!'}")
    else:
        env.run(["a_v140_market_dominance.py", AGENT_PATH])
        s140, s151 = env.steps[-1][0].reward, env.steps[-1][1].reward
        print(f"H2H Game {i+1}: v140 (P0) = {s140:.0f} vs v151 (P1) = {s151:.0f} -> {'v151 WON!' if s151 > s140 else 'v140 WON!'}")
    if s151 > s140: h2h_151 += 1
    else: h2h_140 += 1
print(f"H2H Result vs v140: v151 = {h2h_151} Wins vs v140 = {h2h_140} Wins")

print("\n=======================================================")
print("HEAD-TO-HEAD: v151 vs v142 (4 Games)")
print("=======================================================")
h2h_151_2 = 0
h2h_142 = 0
for i in range(4):
    env = make("kaggriculture", configuration={"episodeSteps": 720})
    if i % 2 == 0:
        env.run([AGENT_PATH, "a_v142_surgical_dominance.py"])
        s151, s142 = env.steps[-1][0].reward, env.steps[-1][1].reward
        print(f"H2H Game {i+1}: v151 (P0) = {s151:.0f} vs v142 (P1) = {s142:.0f} -> {'v151 WON!' if s151 > s142 else 'v142 WON!'}")
    else:
        env.run(["a_v142_surgical_dominance.py", AGENT_PATH])
        s142, s151 = env.steps[-1][0].reward, env.steps[-1][1].reward
        print(f"H2H Game {i+1}: v142 (P0) = {s142:.0f} vs v151 (P1) = {s151:.0f} -> {'v151 WON!' if s151 > s142 else 'v142 WON!'}")
    if s151 > s142: h2h_151_2 += 1
    else: h2h_142 += 1
print(f"H2H Result vs v142: v151 = {h2h_151_2} Wins vs v142 = {h2h_142} Wins")
