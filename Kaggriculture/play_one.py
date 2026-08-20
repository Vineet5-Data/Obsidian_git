import sys
from kaggle_environments import make

import os
import importlib.util

def load(path):
    spec = importlib.util.spec_from_file_location("m_" + os.path.basename(path).replace(".", "_"), path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.agent

def main():
    agent1 = sys.argv[1]
    agent2 = sys.argv[2]
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 12345
    
    print(f"Playing {agent1} vs {agent2} (seed {seed})")
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed}, debug=True)
    env.run([load(agent1), load(agent2)])
    
    final_step = env.steps[-1]
    obs = final_step[0].observation
    
    print("\n--- Money & Assets over time ---")
    import json
    with open("replay.json", "w") as f:
        json.dump(env.toJSON(), f)
    for step_idx in range(0, 720, 24):
        for p in (0, 1):
            if step_idx > 0:
                prev_s = env.steps[step_idx-1][0].observation
                # to get what they actually sold, we'd have to look at their actions, but kaggle env steps have 'action' in agent state
                pass
        
        s = env.steps[step_idx]
        f0 = s[0].observation["farms"][0]
        f1 = s[0].observation["farms"][1]
        
        def count_plants(tiles):
            counts = {}
            for row in tiles:
                for t in row:
                    if isinstance(t, dict) and t.get("kind") == "PLANT":
                        c = t["crop"]
                        counts[c] = counts.get(c, 0) + 1
            return counts
            
        p0_counts = count_plants(f0["tiles"])
        p1_counts = count_plants(f1["tiles"])
        p0 = sum(p0_counts.values())
        p1 = sum(p1_counts.values())
        
        c0_str = ",".join(f"{k[:2]}:{v}" for k, v in p0_counts.items())
        c1_str = ",".join(f"{k[:2]}:{v}" for k, v in p1_counts.items())
        
        print(f"Day {step_idx//24:2d}: P0 ${f0['money']:6.0f} ({c0_str}) | P1 ${f1['money']:6.0f} ({c1_str}) | Diff ${f0['money']-f1['money']:6.0f}")
    
    for i, (agent_name, agent_state) in enumerate(zip([agent1, agent2], final_step)):
        farm = obs["farms"][i]
        print(f"\n--- Player {i}: {agent_name} ---")
        print(f"Reward (Money): {agent_state.reward}")
        
        # Count crops
        crop_counts = {}
        for row in farm["tiles"]:
            for tile in row:
                if isinstance(tile, dict) and tile.get("kind") == "PLANT":
                    c = tile.get("crop")
                    crop_counts[c] = crop_counts.get(c, 0) + 1
        print("Crops:", crop_counts)
        
        # Count animals
        animal_counts = {}
        for row in farm["tiles"]:
            for tile in row:
                if isinstance(tile, dict) and tile.get("animal"):
                    c = tile.get("animal")
                    animal_counts[c] = animal_counts.get(c, 0) + 1
        print("Animals:", animal_counts)

if __name__ == "__main__":
    main()
