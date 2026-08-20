import re

with open('v60_unbeatable.py', 'r') as f:
    s = f.read()

s = s.replace('crop_slots = max(0, min(60, slots - structure_need))', 'crop_slots = max(0, slots - structure_need)')
s = s.replace('step >= int(t["max_lifespan_step"]) - 24', 'step >= int(t["max_lifespan_step"])')

s = re.sub(r'    for crop in \("STRAWBERRY", "MELON", "TOMATO"\):.*?    remaining_crop_slots = crop_slots - sum\(want_crop\.values\(\)\)', '    remaining_crop_slots = crop_slots - sum(want_crop.values())', s, flags=re.DOTALL)
s = s.replace('1.0 + 0.055 * crowd', '1.0 + 0.01 * crowd')

with open('v60_unbeatable.py', 'w') as f:
    f.write(s)
