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

# 2. Force Wheat fallback for all empty tiles
fallback_old = """        if best is None:
            break"""

fallback_new = """        if best is None:
            # Wheat internal value is high (feed), so fill remaining slots with Wheat
            want_crop["WHEAT"] = want_crop.get("WHEAT", 0) + (remaining_crop_slots - _)
            break"""

code = code.replace(fallback_old, fallback_new)

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

with open(r"c:\Users\Vinee\Desktop\Kaggriculture\v102_counter_play.py", "w") as f:
    f.write(code)

print("Generated v102_counter_play.py successfully.")
