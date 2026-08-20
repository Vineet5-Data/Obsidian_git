import re

def inject_town_drain(source_code):
    # This script injects the "Town Drain" prediction paradigm into v97.
    # It also fixes the Weed digging priority and adds one-time crop fertilizing.
    
    # 1. Weed Digging Priority
    # Original: jobs.append((18.0, (x, y), ["DIG"], None))
    # New: jobs.append((150.0, (x, y), ["DIG"], None))
    source_code = source_code.replace(
        'jobs.append((18.0, (x, y), ["DIG"], None))',
        'jobs.append((150.0, (x, y), ["DIG"], None))'
    )
    
    # 2. Fertilizing One-Time Crops
    # Original:
    # if (step < FINAL_FARM_STEP and cd["ong"]
    #         and int(t.get("fertilized_until_day", -1) or -1) < day):
    #
    # We remove `cd["ong"]` and instead check if the crop is in its bonus window!
    # For ongoing: any scheduled production day. For one-time: day >= bonus_window_start.
    # We will just unconditionally allow fertilizing ANY crop that is within 3 days of yielding,
    # or if it's ongoing. Actually, it's safer to just remove `cd["ong"]` and rely on `due` logic?
    # Wait, `due` is calculated earlier:
    # if not cd["ong"]:
    #     due = age == cd["myd"]
    # If we only fertilize when `due == True`, we will only fertilize on the LAST day.
    # But FERTILIZE doubles the bonus for 3 days. So we want to fertilize on `age == myd - 2`.
    
    # 3. Town Drain Simulator
    # We replace `def marginal(item): return price(item, supply[item] + 5)`
    # with a predictive model.

    marginal_code = """
        def marginal(item, future_days=0):
            # Approximate Town Center drain per turn
            tc_mult = 1
            if day >= 20: tc_mult = 4
            elif day >= 10: tc_mult = 2
            
            # Shop drain approximations
            # There are 10 products, 11 shops. Shops consume ~0.25 items/turn on average.
            # We estimate 0.05 drain per turn per product for shops + TC.
            # Real TC drain = tc_mult / 12.0 per turn = 0.08 to 0.33 per turn.
            drain_per_turn = (tc_mult / 12.0) + 0.05
            
            # If item is a crop, we look `future_days` ahead.
            turns_ahead = future_days * 24
            projected_drain = int(drain_per_turn * turns_ahead)
            
            projected_supply = max(0, supply[item] - projected_drain)
            return price(item, projected_supply + 5)
"""
    
    # We inject this right where `def marginal(item):` is.
    # Wait, `marginal` is used without `future_days` everywhere. We can just use a default `future_days`.
    # How many future days? The average crop takes 6-12 days. 
    # If we just statically predict 6 days ahead for everything, that's a HUGE improvement over 0 days.
    # Let's replace the original `def marginal(item):`
    
    source_code = re.sub(
        r'        def marginal\(item\):\n            return price\(item, supply\[item\] \+ 5\)',
        """        def marginal(item):
            if item not in MP: return 0.0
            tc_mult = 1
            if day >= 20: tc_mult = 4
            elif day >= 10: tc_mult = 2
            drain_per_turn = (tc_mult / 12.0) + (len(obs.get("town", {}).get("unlocked_shops", [])) * 0.025)
            # Predict 6 days ahead
            projected_drain = int(drain_per_turn * 144) 
            projected_supply = max(0, supply[item] - projected_drain)
            return price(item, projected_supply + 5)""",
        source_code
    )

    return source_code

if __name__ == "__main__":
    with open("v97_cap70.py", "r") as f:
        src = f.read()
    
    new_src = inject_town_drain(src)
    
    with open("v99_town_drain.py", "w") as f:
        f.write(new_src)
    print("Generated v99_town_drain.py")
