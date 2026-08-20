import subprocess
import json
import os

os.makedirs("kaggle_episodes", exist_ok=True)

episodes = [
    "93095700", "93094783", "93093864", "93092933", "93092007",
    "93091079", "93090150", "93089211", "93088274", "93087343",
    "93086419", "93085487"
]

print("Fetching and analyzing all v142 Kaggle episodes...")
for ep in episodes:
    json_path = f"kaggle_episodes/{ep}.json"
    if not os.path.exists(json_path):
        subprocess.run(["kaggle", "competitions", "replay", ep, "-p", "kaggle_episodes"], capture_output=True)
        # Rename to ep.json if named differently
        # Usually downloaded as kaggle_episodes/<ep>.json or similar
    
    # Check if file exists
    target = f"kaggle_episodes/{ep}.json"
    if not os.path.exists(target):
        # find any file in kaggle_episodes matching ep
        for f in os.listdir("kaggle_episodes"):
            if ep in f:
                target = os.path.join("kaggle_episodes", f)
                break
    
    if os.path.exists(target):
        try:
            with open(target, "r", encoding="utf-8") as f:
                d = json.load(f)
            steps = d["steps"]
            s0 = steps[-1][0].get("reward")
            s1 = steps[-1][1].get("reward")
            
            # Find which seat was v142 (submission 55512465)
            # In metadata or agents
            agents = d.get("agents", ["Unknown", "Unknown"])
            print(f"Episode {ep}: Agents={agents} | Scores: Seat 0 = {s0} vs Seat 1 = {s1}")
        except Exception as e:
            print(f"Episode {ep}: Error reading {e}")
    else:
        print(f"Episode {ep}: File not found")
