import sys
import os
import glob

# Local run: add current directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import v107_hybrid
import v97_cap70
from kaggle_environments import make
from multiprocessing import Pool
import random
import time

def play_match(seed):
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run([v107_hybrid.agent, v97_cap70.agent])
    scores = [step.reward for step in env.steps[-1]]
    return {"seed": seed, "v107": scores[0], "v97": scores[1]}

if __name__ == '__main__':
    games = 10
    seeds = [random.randint(0, 100000000) for _ in range(games)]
    
    t0 = time.time()
    with Pool() as pool:
        results = pool.map(play_match, seeds)
        
    wins = sum(1 for r in results if r["v107"] >= r["v97"])
    
    print(f"Games Played: {games}")
    print(f"v107 Hybrid Win Rate: {wins / games * 100:.2f}%")
    print(f"Time Taken: {time.time() - t0:.1f}s")
    for r in results:
        print(f"Seed {r['seed']}: v107={r['v107']}, v97={r['v97']} -> {'WIN' if r['v107']>=r['v97'] else 'LOSS'}")
