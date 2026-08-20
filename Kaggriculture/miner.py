import json
import glob
import os
from collections import defaultdict

def extract_spec(replay_path):
    with open(replay_path) as f:
        d = json.load(f)
    
    steps = d['steps']
    # find winner
    p0_reward = steps[-1][0]['reward'] or 0
    p1_reward = steps[-1][1]['reward'] or 0
    winner = 0 if p0_reward >= p1_reward else 1
    
    obs_list = [s[winner]['observation'] for s in steps if s[winner].get('observation')]
    
    spec = {
        'name': os.path.basename(replay_path).replace('.json', ''),
        'quadrants': 1,
        'land_days': [],
        'layout': {'PASTURE': 0, 'COOP': 0, 'CROP': 0},
        'animals': defaultdict(int),
        'animal_days': [],
        'crops': defaultdict(int),
        'hire_curve': [0]*30,
        'fert_cadence': 0
    }
    
    prev_unlocked = []
    
    for t, obs in enumerate(obs_list):
        day = obs.get('day', t//24)
        farm = obs['farms'][winner]
        
        unlocked = farm['unlocked_quadrants']
        if len(unlocked) > len(prev_unlocked):
            if len(prev_unlocked) > 0:
                spec['land_days'].append(day)
            prev_unlocked = unlocked
            
        spec['quadrants'] = len(unlocked)
        
        hires = farm.get('hires_today', 0)
        if day < len(spec['hire_curve']):
            spec['hire_curve'][day] = max(spec['hire_curve'][day], hires)
        
        action = steps[t][winner].get('action', {})
        for unit, ops in [('farmer', action.get('farmer', []))] + [('hand'+str(i), h_ops) for i, h_ops in enumerate(action.get('hands', []))]:
            if not ops: continue
            op = ops[0]
            if op == 'FERTILIZE':
                spec['fert_cadence'] += 1
            elif op == 'PLANT' and len(ops) > 1:
                spec['crops'][ops[1]] += 1
            elif op == 'PLACE' and len(ops) > 1 and ops[1] in ['SHEEP', 'COW', 'GOOSE']:
                spec['animal_days'].append(day)
                spec['animals'][ops[1]] += 1
                
    # final layout
    last_farm = obs_list[-1]['farms'][winner]
    for row in last_farm['tiles']:
        for tile in row:
            if type(tile) is dict:
                kind = tile.get('kind')
                if kind in ['PASTURE', 'COOP']:
                    spec['layout'][kind] += 1
                elif kind == 'PLANT':
                    spec['layout']['CROP'] += 1
                    
    total_crops = sum(spec['crops'].values())
    if total_crops > 0:
        spec['crops'] = {k: round(v/total_crops, 3) for k, v in spec['crops'].items()}
    
    spec['animals'] = dict(spec['animals'])
    return spec

if __name__ == '__main__':
    replays = glob.glob('Top_players/*.json')
    specs = []
    for r in replays:
        specs.append(extract_spec(r))
    with open('mined_specs.json', 'w') as f:
        json.dump(specs, f, indent=2)
    print(f"Mined {len(specs)} specs.")
