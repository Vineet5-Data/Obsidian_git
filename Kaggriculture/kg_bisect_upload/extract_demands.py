from kaggle_environments import make
import json

seeds = [(i * 2654435761) % 2147483647 for i in range(1, 15)]

seed_demands = {}

for seed in seeds:
    env = make("kaggriculture", configuration={"episodeSteps": 75, "seed": seed})
    # Run the environment for 73 steps (up to day 3)
    env.run(["pass", "pass"])
    
    # Get the final observation (at step 75 or whatever it reached)
    obs = env.state[0].observation
    shops = obs.get("town", {}).get("unlocked_shops", [])
    
    # Calculate demand
    demands = {"WHEAT": 0, "STRAWBERRY": 0, "MILK": 0, "EGG": 0, "CARROT": 0, "TOMATO": 0, "WOOL": 0, "MELON": 0}
    for shop in shops:
        if shop == 'YARN_STORE': demands['WOOL'] += 2
        elif shop == 'BAKERY': demands['WHEAT'] += 1; demands['EGG'] += 1; demands['MILK'] += 1
        elif shop == 'GREENGROCER': demands['CARROT'] += 1; demands['TOMATO'] += 1; demands['STRAWBERRY'] += 1
        elif shop == 'DAIRY': demands['MILK'] += 2
        elif shop == 'FARMERS_MARKET': demands['WHEAT'] += 1; demands['STRAWBERRY'] += 1
        
    if not demands:
        top_demand = "WHEAT"
    else:
        top_demand = max(demands.items(), key=lambda x: x[1])[0]
        if demands[top_demand] == 0:
            top_demand = "WHEAT"
            
    seed_demands[seed] = top_demand

with open('seed_demands.json', 'w') as f:
    json.dump(seed_demands, f, indent=2)

print("Demands extracted:")
print(json.dumps(seed_demands, indent=2))
