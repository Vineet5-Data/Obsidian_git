import re

with open('v59_perfect_hoard.py', 'r') as f:
    s = f.read()

s = s.replace('crop_slots = min(60, max(0, slots - structure_need))', 'crop_slots = max(0, slots - structure_need)')

s = s.replace('step >= int(t["max_lifespan_step"]) - 24', 'step >= int(t["max_lifespan_step"])')

old_gain = '''            over = max(0.0, sim_supply.get(crop, 0.0) - absorb.get(crop, 0.0))
            p = price(crop, int(minv.get(crop, I0) + over))
            gain = y[0] * p - y[2]
            if gain <= 0:
                continue'''

new_gain = '''            over = max(0.0, sim_supply.get(crop, 0.0) - absorb.get(crop, 0.0))
            base_inv = int(minv.get(crop, I0) + over)
            total_rev, _ = sale_value(crop, base_inv, y[0])
            avg_p = total_rev / float(max(1, y[0]))
            gain = total_rev - y[2]
            if gain <= 0:
                continue'''
s = s.replace(old_gain, new_gain)

old_premium = re.search(r'    # Compete for fragile premium markets.*?sim_supply\[crop\] = sim_supply\.get\(crop, 0\.0\) \+ n \* y\[0\]\n', s, re.DOTALL)
if old_premium:
    s = s.replace(old_premium.group(0), '    # Let remaining slots handle it based on avg price\n')

s = s.replace('time_risk * (1.0 + 0.02 * crowd)', 'time_risk * (1.0 + 0.005 * crowd)')

with open('v62_unbeatable.py', 'w') as f:
    f.write(s)
