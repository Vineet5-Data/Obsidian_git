import json
import os

with open('C:/Users/Vinee/Desktop/Kaggriculture/v97_cap70.py') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if line.startswith('    elif day < 3:') and 'animal_target = 4' in lines[i+1]:
        start_idx = i
    if line.startswith('    remaining_crop_slots = crop_slots - sum(want_crop.values())'):
        end_idx = i
        break

with open('C:/Users/Vinee/Desktop/Kaggriculture/archetypes.json') as f:
    archetypes = f.read()

for arch_idx in range(len(json.loads(archetypes))):
    loader_code = f'''
    import json
    if not hasattr(obs, 'archetypes'):
        obs.archetypes = json.loads(\"\"\"{archetypes}\"\"\")
        
    ACTIVE_SPEC = obs.archetypes[{arch_idx}]
    
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
    new_lines = lines[:start_idx] + [loader_code] + lines[end_idx:]
    with open(f'C:/Users/Vinee/Desktop/Kaggriculture/arch_agent_{arch_idx}.py', 'w') as f:
        f.writelines(new_lines)
