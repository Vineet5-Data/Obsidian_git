import shutil
import os

def main():
    with open('v97_cap70.py', 'r') as f:
        content = f.read()

    # Injection 1: Archetype & Mode
    target1 = """                    if t.get("fertilizer_available"):
                        opp_wave["FERTILIZER"] += 0.8

    # Hidden carried/shed stock cannot be observed after a harvest.  Retain a"""

    replacement1 = """                    if t.get("fertilizer_available"):
                        opp_wave["FERTILIZER"] += 0.8

    opp_archetype = "UNKNOWN"
    if day > 4:
        if opp_animal_counts.get("COW", 0) + opp_animal_counts.get("SHEEP", 0) >= 3 and opp_animal_counts.get("GOOSE", 0) == 0:
            opp_archetype = "HEAVY_GRAZER"
            
    agent_mode = "NORMAL"
    if len(farms) > 1 and day >= 20:
        our_assets = money + sum(price(it, I0) * (shed.get(it, 0) + carried_all.get(it, 0)) for it in PRODUCTS)
        opp_money = float(_get(farms[1 - seat], "money", 0) or 0)
        score_delta = our_assets - opp_money
        if score_delta > 5000:
            agent_mode = "FRONT_RUNNER"
        elif score_delta < -5000:
            agent_mode = "UNDERDOG"

    # Hidden carried/shed stock cannot be observed after a harvest.  Retain a"""

    content = content.replace(target1, replacement1)

    # Injection 2: Preemptive crash & Marginal multipliers
    target2 = """    for item in PRODUCTS:
        opp_wave[item] = min(100.0, max(opp_wave[item],
                                       0.50 * fallback_wave.get(item, 0.0)))

    def marginal(item, extra=0.0):
        over = max(0.0, supply.get(item, 0.0) + extra - absorb.get(item, 0.0))
        return price(item, int(minv.get(item, I0) + over))"""

    replacement2 = """    for item in PRODUCTS:
        opp_wave[item] = min(100.0, max(opp_wave[item],
                                       0.50 * fallback_wave.get(item, 0.0)))
        if agent_mode == "FRONT_RUNNER" and item in ("MELON", "STRAWBERRY", "MILK", "WOOL"):
            opp_wave[item] *= 1.5

    def marginal(item, extra=0.0):
        multiplier = 1.0
        if opp_archetype == "HEAVY_GRAZER":
            if item in ("EGG", "CARROT", "TOMATO"):
                multiplier = 2.5
            elif item in ("MILK", "WOOL", "STRAWBERRY", "MELON"):
                multiplier = 0.5
        
        if agent_mode == "UNDERDOG":
            if item == "MELON":
                multiplier = 1.5
            elif item == "WHEAT":
                multiplier = 1.3
        
        opp_pressure = opp_wave.get(item, 0.0) * 0.2 if agent_mode == "FRONT_RUNNER" else 0.0
        over = max(0.0, supply.get(item, 0.0) + extra - absorb.get(item, 0.0) + opp_pressure)
        return price(item, int(minv.get(item, I0) + over)) * multiplier"""

    content = content.replace(target2, replacement2)
    
    with open('v98_state_machine.py', 'w') as f:
        f.write(content)
        
    print("Successfully generated v98_state_machine.py")

if __name__ == "__main__":
    main()
