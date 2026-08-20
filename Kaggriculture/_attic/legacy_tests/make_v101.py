import os

with open(r"c:\Users\Vinee\Desktop\Kaggriculture\v97_cap70.py", "r") as f:
    code = f.read()

# 1. Remove Tomato, Carrot, and Geese from definitions
code = code.replace(
    '    "CARROT":     {"seed": 20,  "fyd": 2,  "myd": 3,  "iv": 0, "my": 4, "ong": False},\n',
    ''
)
code = code.replace(
    '    "TOMATO":     {"seed": 50,  "fyd": 8,  "myd": 8,  "iv": 1, "my": 4, "ong": True},\n',
    ''
)
code = code.replace(
    '    "GOOSE": {"cost": 300, "st": "COOP",    "fyd": 4, "iv": 1, "mh": 4, "prod": "EGG"},\n',
    ''
)

# Also remove from hardcoded strategic loop
code = code.replace(
    'for crop in ("STRAWBERRY", "MELON", "TOMATO"):',
    'for crop in ("STRAWBERRY", "MELON"):'
)

# 2. Force Wheat planting in the last 10 days
wheat_logic_old = """    if day < 3 and crop_slots > 0:
        quick = min(crop_slots, max(6, int(round(crop_slots * 0.40))))
        want_crop["WHEAT"] = quick
        sim_supply["WHEAT"] = sim_supply.get("WHEAT", 0.0) + 4 * quick"""

wheat_logic_new = """    if day < 3 and crop_slots > 0:
        quick = min(crop_slots, max(6, int(round(crop_slots * 0.40))))
        want_crop["WHEAT"] = quick
        sim_supply["WHEAT"] = sim_supply.get("WHEAT", 0.0) + 4 * quick
    elif day >= 19 and crop_slots > 0:
        quick = crop_slots
        want_crop["WHEAT"] = want_crop.get("WHEAT", 0) + quick
        sim_supply["WHEAT"] = sim_supply.get("WHEAT", 0.0) + 4 * quick"""

code = code.replace(wheat_logic_old, wheat_logic_new)

# 3. Phased Liquidation - Queue Optimization
dump_logic_old = """        race, exact_value = race_score(item, minv.get(item, I0), n, rival_qty)
        rows.append((race, exact_value, item, n))
    rows.sort(reverse=True)"""

dump_logic_new = """        race, exact_value = race_score(item, minv.get(item, I0), n, rival_qty)
        if step >= DUMP_STEP and item in ("STRAWBERRY", "MELON", "MILK", "WOOL"):
            race += 10000.0
        rows.append((race, exact_value, item, n))
    rows.sort(reverse=True)"""

code = code.replace(dump_logic_old, dump_logic_new)


# 4. Fix Land Buying Deadlock
land_old = '''        c = LAND_PRICES[owned_extra]
        se_gate = (owned_extra < 2 or
                   (cash >= 12000.0 + reserve and occupied + sum(want_crop.values())
                    + sum(want_animal.values()) >= 72))
        if (day >= unlock_day and pressure >= 0.60 and cash - c >= reserve
                and se_gate):'''

land_new = '''        c = LAND_PRICES[owned_extra]
        if day >= unlock_day and cash - c >= reserve:'''

code = code.replace(land_old, land_new)

with open(r"c:\Users\Vinee\Desktop\Kaggriculture\v101_counter_play.py", "w") as f:
    f.write(code)

print("Generated v101_counter_play.py successfully.")
