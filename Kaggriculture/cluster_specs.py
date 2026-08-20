import json
import math
import random

def get_features(spec):
    return [
        spec['layout'].get('PASTURE', 0),
        spec['layout'].get('COOP', 0),
        spec['layout'].get('CROP', 0),
        spec['crops'].get('WHEAT', 0.0),
        spec['crops'].get('STRAWBERRY', 0.0),
        spec['crops'].get('MELON', 0.0),
        spec['crops'].get('CARROT', 0.0),
        spec['crops'].get('TOMATO', 0.0)
    ]

def dist(f1, f2):
    return math.sqrt(sum((a-b)**2 for a,b in zip(f1, f2)))

def k_means(specs, k=12, iters=100):
    if len(specs) <= k:
        return specs
    
    random.seed(42)
    centroids = random.sample([get_features(s) for s in specs], k)
    
    for _ in range(iters):
        clusters = [[] for _ in range(k)]
        for spec in specs:
            f = get_features(spec)
            closest_idx = min(range(k), key=lambda i: dist(f, centroids[i]))
            clusters[closest_idx].append(spec)
            
        new_centroids = []
        for c in clusters:
            if not c:
                new_centroids.append(random.choice([get_features(s) for s in specs]))
                continue
            feats = [get_features(s) for s in c]
            new_c = [sum(col)/len(col) for col in zip(*feats)]
            new_centroids.append(new_c)
        centroids = new_centroids
        
    # pick the real spec closest to each centroid
    archetypes = []
    for c in clusters:
        if not c:
            archetypes.append(specs[len(archetypes)])
            continue
        c_feat = [sum(col)/len(col) for col in zip(*[get_features(s) for s in c])]
        best = min(c, key=lambda s: dist(get_features(s), c_feat))
        archetypes.append(best)
        
    return archetypes

if __name__ == '__main__':
    with open('mined_specs.json') as f:
        specs = json.load(f)
        
    k = min(12, len(specs))
    archetypes = k_means(specs, k=k)
    print(f"Clustered {len(specs)} into {len(archetypes)} archetypes.")
    
    with open('archetypes.json', 'w') as f:
        json.dump(archetypes, f, indent=2)
