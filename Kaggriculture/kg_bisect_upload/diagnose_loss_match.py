import json
from kaggle_environments import make

REPLAY_PATH = r"C:\Users\Vinee\Downloads\93081881.json"
AGENT_PATH = "a_v142_surgical_dominance.py"

with open(REPLAY_PATH, "r", encoding="utf-8") as f:
    replay_data = json.load(f)

steps_ref = replay_data["steps"]

def make_tape_agent(steps_ref, seat):
    def tape_agent(obs, config=None):
        step = obs["step"]
        if step + 1 < len(steps_ref):
            raw = steps_ref[step + 1][seat].get("action")
            if isinstance(raw, dict):
                return raw
        return {"farmer": ["PASS"], "hands": [], "market": []}
    return tape_agent

opp_p0_tape = make_tape_agent(steps_ref, 0)

env = make("kaggriculture", configuration={"episodeSteps": 720})
env.run([opp_p0_tape, AGENT_PATH])

# Analyze match progression
print("=== Turn-by-turn Diagnostic for Episode 93081881 (Seat 0 Opponent vs Seat 1 v142) ===")
print("Final Scores: Opponent =", env.steps[-1][0].reward, "v142 =", env.steps[-1][1].reward)

# Sample every 5 days (120 steps)
for day in range(0, 31, 5):
    step_idx = min(day * 24, 719)
    s = env.steps[step_idx]
    f0 = s[0]["observation"]["farms"][0]
    f1 = s[1]["observation"]["farms"][1]
    
    # Count plants and animals
    p0_plants = sum(1 for row in f0["tiles"] for cell in row if isinstance(cell, dict) and cell.get("kind") == "PLANT")
    p1_plants = sum(1 for row in f1["tiles"] for cell in row if isinstance(cell, dict) and cell.get("kind") == "PLANT")
    p0_animals = sum(1 for row in f0["tiles"] for cell in row if isinstance(cell, dict) and cell.get("kind") in ("COOP", "PASTURE") and cell.get("animal"))
    p1_animals = sum(1 for row in f1["tiles"] for cell in row if isinstance(cell, dict) and cell.get("kind") in ("COOP", "PASTURE") and cell.get("animal"))
    
    p1_priv = s[1]["observation"]["private"]
    p1_shed = p1_priv.get("shed", {})
    p1_inv = p1_priv.get("inventories", [])
    p1_held_items = sum(p1_shed.values()) + sum(sum(inv.values()) for inv in p1_inv if isinstance(inv, dict))
    
    print(f"Day {day:2d} (Step {step_idx:3d}):")
    print(f"  Money: Opp = ${f0['money']:<8.1f} | v142 = ${f1['money']:<8.1f} (Diff: {f1['money'] - f0['money']:+8.1f})")
    print(f"  Tiles: Opp = {p0_plants} plants, {p0_animals} animals | v142 = {p1_plants} plants, {p1_animals} animals")
    print(f"  v142 Shed/Inventory items held: {p1_held_items} {p1_shed}")

# Check final unsold inventory at step 719
final_obs_p1 = env.steps[-1][1]["observation"]
final_shed = final_obs_p1["private"]["shed"]
final_invs = final_obs_p1["private"]["inventories"]
print("\n=== End of Game Liquidation Check (Step 719) ===")
print("v142 Final Shed:", final_shed)
print("v142 Final Field Worker Inventories:", final_invs)
market_prices = final_obs_p1["market"]["prices"]
print("Final Market Prices:", market_prices)

unsold_value = sum(count * market_prices.get(item, 0) for item, count in final_shed.items())
for inv in final_invs:
    if isinstance(inv, dict):
        unsold_value += sum(count * market_prices.get(item, 0) for item, count in inv.items())
print(f"Total Unsold / Unliquidated Assets in v142 possession at game end: ${unsold_value:.1f}")
