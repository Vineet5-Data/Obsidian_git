with open('C:/Users/Vinee/Desktop/Kaggriculture/selector_agent.py') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if 'rows.sort(reverse=True)' in line:
        new_lines.append('    impact_weights = {"MELON": 3.5, "STRAWBERRY": 2.0, "MILK": 2.0, "WOOL": 3.2}\n')
        new_lines.append('    rows.sort(key=lambda r: (impact_weights.get(r[2], 1.0) * r[3], r[0]), reverse=True)\n')
    elif 'reservation = max(1.0, sell_hold * MP[item]["base"])' in line:
        new_lines.append('            shop_demand = {"WHEAT": 0, "STRAWBERRY": 0, "MILK": 0, "EGG": 0, "CARROT": 0, "TOMATO": 0, "WOOL": 0, "MELON": 0}\n')
        new_lines.append('            for s in shops:\n')
        new_lines.append('                if s == "YARN_STORE": shop_demand["WOOL"] += 2\n')
        new_lines.append('                elif s == "BAKERY": shop_demand["WHEAT"] += 1; shop_demand["EGG"] += 1; shop_demand["MILK"] += 1\n')
        new_lines.append('                elif s == "GREENGROCER": shop_demand["CARROT"] += 1; shop_demand["TOMATO"] += 1; shop_demand["STRAWBERRY"] += 1\n')
        new_lines.append('                elif s == "DAIRY": shop_demand["MILK"] += 2\n')
        new_lines.append('                elif s == "FARMERS_MARKET": shop_demand["WHEAT"] += 1; shop_demand["STRAWBERRY"] += 1\n')
        new_lines.append('            drain_ratio = shop_demand.get(item, 0) / max(1, qty)\n')
        new_lines.append('            scaled_hold = sell_hold * max(1.0, drain_ratio * 1.5)\n')
        new_lines.append('            reservation = max(1.0, scaled_hold * MP[item]["base"])\n')
    else:
        new_lines.append(line)

with open('C:/Users/Vinee/Desktop/Kaggriculture/selector_agent.py', 'w') as f:
    f.writelines(new_lines)
