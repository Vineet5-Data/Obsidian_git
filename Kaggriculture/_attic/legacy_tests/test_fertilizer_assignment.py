import sys
import a_v138_fertilizer_denial as agent_module

def test_fertilizer_assignment():
    print("Running test_fertilizer_assignment...")
    
    # Mock observation with a worker, an animal, a shed with fertilizer, and a crop needing fertilizer
    obs = {
        "player": 0,
        "step": 500,
        "day": 20,
        "hour": 10,
        "farms": [
            {
                "money": 0,
                "tiles": [[None for _ in range(10)] for _ in range(10)],
                "farmer": [4, 4], # Worker at shed center
                "hands": [],
                "unlocked_quadrants": ["NW", "NE", "SW", "SE"],
                "hires_today": 0
            },
            {
                "money": 5000,
                "tiles": [[None for _ in range(10)] for _ in range(10)],
                "farmer": [4, 4],
                "hands": [],
                "unlocked_quadrants": ["NW", "NE", "SW", "SE"],
                "hires_today": 0
            }
        ],
        "private": {
            "shed": {"FERTILIZER": 10, "WHEAT": 10},
            "seeds": {},
            "inventories": [{}] # Worker empty-handed
        },
        "market": {
            "inventory": {p: 10000 for p in ["WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON", "EGG", "MILK", "WOOL", "FERTILIZER"]},
            "prices": {p: (200 if p == "STRAWBERRY" else 1) for p in ["WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON", "EGG", "MILK", "WOOL", "FERTILIZER"]}
        },
        "town": {
            "unlocked_shops": []
        }
    }
    
    # Add a plant needing fertilizer at (0, 0)
    obs["farms"][0]["tiles"][0][0] = {
        "kind": "PLANT",
        "crop": "STRAWBERRY",
        "planted_day": 11,
        "watered_today": False,
        "consecutive_unwatered": 0,
        "yield_units": 0,
        "max_lifespan_step": 720,
        "fertilized_until_day": -1
    }
    
    actions = agent_module.agent(obs)
    print("Action output (empty worker):", actions)
    
    # Check if worker picked up fertilizer
    action = actions.get("farmer")
    if action and action[0] == "PICKUP" and action[1] == "FERTILIZER":
        print("PASS: Worker prioritized picking up fertilizer.")
    else:
        print("FAIL: Expected PICKUP FERTILIZER, got", action)
        
    # Now test with a worker already carrying fertilizer
    obs["private"]["inventories"] = [{"FERTILIZER": 5}]
    
    actions = agent_module.agent(obs)
    # The agent module might save created_jobs into telemetry, but we can't easily access it.
    print("Action output (carrying fertilizer):", actions)
    print("Telemetry:", agent_module.telemetry_snapshot())
    
    # Check if worker fertilizes the plant
    action = actions.get("farmer")
    if action and action[0] == "FERTILIZE":
        print("PASS: Worker prioritized FERTILIZE since it has fertilizer.")
    else:
        print("FAIL: Expected FERTILIZE, got", action)

if __name__ == "__main__":
    test_fertilizer_assignment()
