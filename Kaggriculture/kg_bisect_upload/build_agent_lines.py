import json

def build():
    with open('v97_cap70.py') as f:
        lines = f.read().split('\n')
        
    with open('archetypes.json') as f:
        archetypes = f.read()

    start_idx, end_idx = -1, -1
    for i, line in enumerate(lines):
        if line.startswith('    if days_left < 8:'):
            start_idx = i
        if line.startswith('    remaining_crop_slots = crop_slots - sum(want_crop.values())'):
            end_idx = i
            break

    loader_code = f"""
    if not hasattr(_plan, 'archetypes'):
        _plan.archetypes = json.loads('''{archetypes}''')
        with open('payoff.json') as f:
            _plan.payoff = json.load(f)
        _plan.current_arch_idx = 0
        
    def get_focus(opp_crops, opp_animals):
        c_val = sum(opp_crops.values())
        a_val = sum(opp_animals.values())
        if a_val > c_val:
            if opp_animals.get('COW', 0) > opp_animals.get('SHEEP', 0):
                return "MILK"
            return "WOOL"
        else:
            if opp_crops.get('MELON', 0) > 0.2:
                return "MELON"
            return "STRAWBERRY"

    if step % 24 == 0:  # Evaluate every day at hour 0
        opp_focus = get_focus(opp_crop_counts, opp_animal_counts)
        
        demands = {{'WHEAT': 0, 'STRAWBERRY': 0, 'MILK': 0, 'EGG': 0, 'CARROT': 0, 'TOMATO': 0, 'WOOL': 0, 'MELON': 0}}
        town = obs.get('town', {{}}) or {{}}
        shops = town.get('unlocked_shops', []) or []
        for shop in shops:
            if shop == 'YARN_STORE': demands['WOOL'] += 2
            elif shop == 'BAKERY': demands['WHEAT'] += 1; demands['EGG'] += 1; demands['MILK'] += 1
            elif shop == 'GREENGROCER': demands['CARROT'] += 1; demands['TOMATO'] += 1; demands['STRAWBERRY'] += 1
            elif shop == 'DAIRY': demands['MILK'] += 2
            elif shop == 'FARMERS_MARKET': demands['WHEAT'] += 1; demands['STRAWBERRY'] += 1
        
        top_demand = max(demands.items(), key=lambda x: x[1])[0]
        if demands[top_demand] == 0:
            top_demand = "WHEAT"
        
        key = f"{{top_demand}}_{{opp_focus}}"
        best_idx = _plan.payoff.get(key, 0)
        
        # fallback to original logic if we don't know this matchup
        if key in _plan.payoff:
            _plan.current_arch_idx = best_idx
        
    ACTIVE_SPEC = _plan.archetypes[_plan.current_arch_idx]
    spec_animals = ACTIVE_SPEC.get('animals', {{}})
    
    if days_left < 8:
        animal_target = current_animal_assets
    elif day < 3:
        animal_target = 4
    else:
        animal_target = sum(spec_animals.values())
        
    animal_need = max(0, animal_target - len(beasts) - pending_animals)
    structure_need = min(slots, max(0, animal_target - current_animal_assets))
    
    want_animal = {{}}
    for name, target in spec_animals.items():
        owned = (own_animal_counts.get(name, 0)
                 + int(shed.get(name, 0) or 0)
                 + int(carried_all.get(name, 0) or 0))
        if target > owned:
            want_animal[name] = target - owned
            
    crop_slots = max(0, min(60, slots - structure_need))
    portfolio_size = len(plants) + crop_slots
    want_crop = {{}}
    spec_crops = ACTIVE_SPEC.get('crops', {{}})
    for crop, ratio in spec_crops.items():
        target = int(round(portfolio_size * ratio))
        already = own_crop_counts.get(crop, 0)
        if target > already:
            want_crop[crop] = target - already
"""
    new_lines = ["import json"] + lines[:start_idx] + [loader_code] + lines[end_idx:]
    with open('selector_agent.py', 'w') as f:
        f.write('\n'.join(new_lines))
        
if __name__ == '__main__':
    build()
