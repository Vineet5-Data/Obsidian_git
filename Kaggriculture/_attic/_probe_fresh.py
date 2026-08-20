"""Probe the Top_fresh-21 replay pool: who played, who won, how much."""
import json
import os
import sys

DIR = r"C:\Users\Vinee\Desktop\Kaggriculture\Top_fresh-21"


def probe(path):
    with open(path, encoding="utf-8") as handle:
        replay = json.load(handle)
    info = replay.get("info") or {}
    steps = replay.get("steps") or []
    final = steps[-1] if steps else []
    rewards = [s.get("reward") for s in final]
    statuses = [s.get("status") for s in final]
    return {
        "episode": os.path.splitext(os.path.basename(path))[0],
        "n_steps": len(steps),
        "teams": info.get("TeamNames"),
        "rewards": rewards,
        "statuses": statuses,
    }


if __name__ == "__main__":
    rows = []
    for name in sorted(os.listdir(DIR)):
        if not name.endswith(".json"):
            continue
        try:
            rows.append(probe(os.path.join(DIR, name)))
        except Exception as error:  # keep going, report at the end
            rows.append({"episode": name, "error": repr(error)})
        print(rows[-1], flush=True)
    print("\n=== summary ===")
    for row in rows:
        if "error" in row:
            print(row["episode"], "ERROR", row["error"])
            continue
        r = row["rewards"]
        win = "?" if None in r else (0 if r[0] > r[1] else (1 if r[1] > r[0] else "tie"))
        print(f"{row['episode']} steps={row['n_steps']} teams={row['teams']} "
              f"rewards={r} winner_seat={win}")
