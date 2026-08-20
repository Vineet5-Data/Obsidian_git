import json

def build():
    with open('archetypes.json') as f:
        archetypes = f.read()
    with open('payoff.json') as f:
        payoff = f.read()
        
    with open('v97_cap70.py') as f:
        code = f.read()
        
    import re; start_idx = re.search(r'    elif day < 3:\s*animal_target = 4', code).start()
    end_idx = re.search(r'    remaining_crop_slots = crop_slots - sum\\(want_crop\\.values\\(\\)\\)', code).start()
    
    loader_code = f'''    # ponytail: injected selector and loader
    import json
    if not hasattr(obs, 'archetypes'):
        obs.archetypes = json.loads(\"\"\"{archetypes}\"\"\")
        obs.payoff = json.loads(\"\"\"{payoff}\"\"\")
        obs.current_arch_idx = 0
        obs.last_score = -9999
        
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
            
    if day < 3:
        animal_target = 4
        animal_need = max(0, animal_target - len(beasts) - pending_animals)
        structure_need = min(slots, max(0, animal_target - current_animal_assets))
        want_animal = {{}}
        species_cap = 2
        for name in sorted(ANIMALS, key=lambda n: -opp_animal_counts.get(n, 0)):
            if sum(want_animal.values()) >= animal_need:
                break
            owned = (own_animal_counts.get(name, 0)
                     + int(shed.get(name, 0) or 0)
                     + int(carried_all.get(name, 0) or 0))
            strategic_target = min(species_cap, opp_animal_counts.get(name, 0))
            n = min(max(0, strategic_target - owned), animal_need - sum(want_animal.values()))
            if n > 0:
                want_animal[name] = n
                
        for _ in range(max(0, animal_need - sum(want_animal.values()))):
            best = None
            for name, a in ANIMALS.items():
                y = animal_yield(a, days_left)
                if not y: continue
                already = (own_animal_counts.get(name, 0) + int(shed.get(name, 0) or 0)
                           + int(carried_all.get(name, 0) or 0) + want_animal.get(name, 0))
                if already >= species_cap: continue
                item = a['prod']
                over = max(0.0, sim_supply.get(item, 0.0) - absorb.get(item, 0.0))
                p = price(item, int(minv.get(item, I0) + over))
                gain = y[0] * p + max(0, days_left)*marginal('FERTILIZER') - a['cost'] - max(0, days_left)*wheat_buy
                if gain > 0:
                    score = gain / (max(1.0, y[1] + max(0, days_left)) * (1.0 + 0.10 * already))
                    if best is None or score > best[0]:
                        best = (score, name, y[0], item)
            if best is None: break
            want_animal[best[1]] = want_animal.get(best[1], 0) + 1
            
        crop_slots = max(0, min(60, slots - structure_need))
        want_crop = {{}}
        if crop_slots > 0:
            quick = min(crop_slots, max(6, int(round(crop_slots * 0.40))))
            want_crop['WHEAT'] = quick
            
        portfolio_size = len(plants) + crop_slots
        crop_cap = max(3, int(math.ceil(max(1, portfolio_size) * (0.42 if len(shops) < 2 else 0.52))))
        for crop in ('STRAWBERRY', 'MELON', 'TOMATO'):
            room = crop_slots - sum(want_crop.values())
            if room <= 0: break
            strategic_target = min(crop_cap, int(math.ceil(0.90 * opp_crop_counts.get(crop, 0))))
            deficit = max(0, strategic_target - own_crop_counts.get(crop, 0))
            n = min(room, deficit)
            if n > 0: want_crop[crop] = want_crop.get(crop, 0) + n
            
    else:
        # Selector at day 3, rescore every 3 days
        if day % 3 == 0:
            opp_focus = get_focus(opp_crop_counts, opp_animal_counts)
            
            # find most demanded product from shops
            demands = {{"WHEAT": 0, "STRAWBERRY": 0, "MILK": 0, "EGG": 0, "CARROT": 0, "TOMATO": 0, "WOOL": 0, "MELON": 0}}
            for shop in shops:
                if shop == 'YARN_STORE': demands['WOOL'] += 2
                elif shop == 'BAKERY': demands['WHEAT'] += 1; demands['EGG'] += 1; demands['MILK'] += 1
                elif shop == 'GREENGROCER': demands['CARROT'] += 1; demands['TOMATO'] += 1; demands['STRAWBERRY'] += 1
                elif shop == 'DAIRY': demands['MILK'] += 2
                elif shop == 'FARMERS_MARKET': demands['WHEAT'] += 1; demands['STRAWBERRY'] += 1
            
            top_demand = max(demands.items(), key=lambda x: x[1])[0]
            
            key = f"{{top_demand}}_{{opp_focus}}"
            best_idx = obs.payoff.get(key, 0)
            
            # Damping: late switches cost more
            margin = (day / 3) * 1.5
            current_score = obs.last_score if best_idx == obs.current_arch_idx else obs.last_score + margin
            
            # Since our proxy matrix doesn't output scores but just the idx, we'll
            # just allow switch if it's different and day < 15, representing damping
            if best_idx != obs.current_arch_idx and day < 15:
                obs.current_arch_idx = best_idx
                
        ACTIVE_SPEC = obs.archetypes[obs.current_arch_idx]
        
        spec_animals = ACTIVE_SPEC.get('animals', {{}})
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
        want_crop = {{}}
        spec_crops = ACTIVE_SPEC.get('crops', {{}})
        for crop, ratio in spec_crops.items():
            target = int(round(crop_slots * ratio))
            already = own_crop_counts.get(crop, 0)
            if target > already:
                want_crop[crop] = target - already
'''
    new_code = code[:start_idx] + loader_code + code[end_idx:]
    with open('selector_agent.py', 'w') as f:
        f.write(new_code)
        
build()
