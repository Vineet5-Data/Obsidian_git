import json

REPLAYS = [
    r"C:\Users\Vinee\Downloads\93087343.json",
    r"C:\Users\Vinee\Downloads\93088274.json",
    r"C:\Users\Vinee\Downloads\93089211.json"
]

for path in REPLAYS:
    print("\n" + "="*70)
    print(f"ANALYSIS OF REPLAY: {path}")
    print("="*70)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    final_step = data["steps"][-1]
    scores = [s.get("reward") for s in final_step]
    print(f"Final Scores: Seat 0 = {scores[0]:.0f} | Seat 1 = {scores[1]:.0f}")
    
    # Identify which player our agent was by checking submission/agent name or behavior
    obs0 = final_step[0]["observation"]
    shops = obs0["town"]["unlocked_shops"]
    print(f"Unlocked Shops ({len(shops)}): {shops}")
    
    # Track sales, purchases, and production for both seats
    for seat in [0, 1]:
        sells = {}
        buys = {}
        plants = {}
        animals = {}
        hires = 0
        land = 0
        
        for step in data["steps"]:
            act = step[seat].get("action")
            if not isinstance(act, dict): continue
            for m in act.get("market", []):
                if not m: continue
                verb = m[0]
                if verb == "SELL":
                    sells[m[1]] = sells.get(m[1], 0) + int(m[2] or 0)
                elif verb in ("BUY_SEED", "BUY_PRODUCT"):
                    buys[m[1]] = buys.get(m[1], 0) + int(m[2] or 0)
                elif verb == "BUY_ANIMAL":
                    animals[m[1]] = animals.get(m[1], 0) + int(m[2] or 0)
                elif verb == "BUY_LAND":
                    land += 1
                elif verb == "HIRE":
                    hires += 1
            
            f = act.get("farmer", [])
            if f and f[0] == "PLANT" and len(f) > 1:
                plants[f[1]] = plants.get(f[1], 0) + 1
            for h in act.get("hands", []):
                if h and h[0] == "PLANT" and len(h) > 1:
                    plants[h[1]] = plants.get(h[1], 0) + 1
        
        print(f"\n--- Seat {seat} Stats (Score: {scores[seat]:.0f}) ---")
        print(f"  Land buys: {land} | Hires: {hires}")
        print(f"  Animals bought: {animals}")
        print(f"  Crops planted: {plants}")
        print(f"  Products bought: {buys}")
        print(f"  Products SOLD: {sells}")

    # Money curves at Days 5, 10, 15, 20, 25, 30
    print("\n--- Day-by-Day Cash Progression ---")
    for day in [0, 5, 10, 15, 20, 25, 30]:
        step_idx = min(day * 24, 719)
        s = data["steps"][step_idx]
        m0 = s[0]["observation"]["farms"][0]["money"]
        m1 = s[1]["observation"]["farms"][1]["money"]
        print(f"  Day {day:2d} (Step {step_idx:3d}): Seat 0 = ${m0:<8.0f} | Seat 1 = ${m1:<8.0f} | Diff (0 - 1): {m0 - m1:+8.0f}")
