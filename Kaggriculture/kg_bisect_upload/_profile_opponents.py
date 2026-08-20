"""Quick opponent strategy profiler.

Loads top opponent replays and profiles what they do:
- When they buy land
- Animal mix and timing
- Crop mix  
- Sell patterns (what, when, volume)
- Total revenue
"""
import base64
import json
import zlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TOP_DIR = ROOT / ".top"

def decode_actions(path):
    """Decode compressed action tape from opponent file."""
    text = path.read_text(encoding="utf-8")
    import re
    # Find block between b64decode( ... ))
    match = re.search(r"base64\.b64decode\(\s*\((.*?)\)\s*\)", text, re.DOTALL)
    if not match:
        return None
    block = match.group(1)
    # Extract all quoted strings
    blobs = re.findall(r"'([^']*)'", block)
    if not blobs:
        return None
    combined = ''.join(blobs)
    try:
        raw = zlib.decompress(base64.b64decode(combined))
        return json.loads(raw)
    except Exception as e:
        print(f"  Decode error for {path.name}: {e}")
        return None


def profile_opponent(actions):
    """Profile an action sequence."""
    if not actions:
        return None
    
    stats = {
        "total_steps": len(actions),
        "land_buys": [],
        "animal_buys": {},
        "seed_buys": {},
        "sells": {},
        "hires_per_day": {},
        "total_sell_value": 0,
    }
    
    for step, action in enumerate(actions):
        if not isinstance(action, dict):
            continue
        day = step // 24
        
        market = action.get("market", [])
        for order in market:
            if not isinstance(order, list) or len(order) == 0:
                continue
            op = order[0]
            if op == "BUY_LAND":
                stats["land_buys"].append(day)
            elif op == "BUY_ANIMAL" and len(order) >= 3:
                animal = order[1]
                n = order[2]
                stats["animal_buys"][animal] = stats["animal_buys"].get(animal, 0) + n
            elif op == "BUY_SEED" and len(order) >= 3:
                crop = order[1]
                n = order[2]
                stats["seed_buys"][crop] = stats["seed_buys"].get(crop, 0) + n
            elif op == "SELL" and len(order) >= 3:
                item = order[1]
                n = order[2]
                if item not in stats["sells"]:
                    stats["sells"][item] = {"total": 0, "first_day": day, "last_day": day}
                stats["sells"][item]["total"] += n
                stats["sells"][item]["last_day"] = max(stats["sells"][item]["last_day"], day)
            elif op == "HIRE":
                stats["hires_per_day"][day] = stats["hires_per_day"].get(day, 0) + 1
    
    return stats


def main():
    files = sorted(TOP_DIR.glob("t_*.py"))
    
    profiles = []
    for f in files:  # All opponents
        actions = decode_actions(f)
        if actions is None:
            continue
        stats = profile_opponent(actions)
        if stats is None:
            continue
        profiles.append((f.stem, stats))
    
    with open(".opponent_profiles.txt", "w", encoding="utf-8") as out_f:
        def output(msg):
            print(msg)
            out_f.write(msg + "\n")
            
        output(f"Profiled {len(profiles)} opponents\n")
        
        # Aggregate patterns
        all_animals = {}
        all_seeds = {}
        all_sells = {}
        land_days = []
        hire_totals = []
        
        for name, stats in profiles:
            for a, n in stats["animal_buys"].items():
                all_animals[a] = all_animals.get(a, 0) + n
            for s, n in stats["seed_buys"].items():
                all_seeds[s] = all_seeds.get(s, 0) + n
            for item, info in stats["sells"].items():
                if item not in all_sells:
                    all_sells[item] = {"total": 0, "count": 0}
                all_sells[item]["total"] += info["total"]
                all_sells[item]["count"] += 1
            land_days.extend(stats["land_buys"])
            hire_totals.append(sum(stats["hires_per_day"].values()))
        
        output("=== ANIMAL PURCHASES (across all opponents) ===")
        for a in sorted(all_animals, key=all_animals.get, reverse=True):
            avg = all_animals[a] / len(profiles)
            output(f"  {a}: total={all_animals[a]} avg={avg:.1f}/opponent")
        
        output("\n=== SEED PURCHASES ===")
        for s in sorted(all_seeds, key=all_seeds.get, reverse=True):
            avg = all_seeds[s] / len(profiles)
            output(f"  {s}: total={all_seeds[s]} avg={avg:.1f}/opponent")
        
        output("\n=== SELL VOLUMES ===")
        for item in sorted(all_sells, key=lambda x: all_sells[x]["total"], reverse=True):
            info = all_sells[item]
            avg = info["total"] / max(1, info["count"])
            output(f"  {item}: total={info['total']} by {info['count']} opps, avg={avg:.1f}/seller")
        
        output("\n=== LAND BUY TIMING ===")
        if land_days:
            from collections import Counter
            day_counts = Counter(land_days)
            for d in sorted(day_counts):
                output(f"  Day {d}: {day_counts[d]} land buys")
        
        output("\n=== HIRING ===")
        if hire_totals:
            import statistics
            output(f"  Mean total hires/game: {statistics.mean(hire_totals):.1f}")
            output(f"  Min: {min(hire_totals)}, Max: {max(hire_totals)}")
        
        # Per-opponent detail
        output("\n=== PER-OPPONENT DETAIL ===")
        for name, stats in profiles:
            animals = ", ".join(f"{a}:{n}" for a, n in stats["animal_buys"].items())
            seeds = ", ".join(f"{s}:{n}" for s, n in stats["seed_buys"].items())
            land = ", ".join(f"d{d}" for d in stats["land_buys"])
            total_hires = sum(stats["hires_per_day"].values())
            sells_summary = ", ".join(f"{item}:{info['total']}" for item, info in stats["sells"].items())
            output(f"\n  {name}:")
            output(f"    Animals: {animals or 'none'}")
            output(f"    Seeds: {seeds or 'none'}")
            output(f"    Land: {land or 'none'}")
            output(f"    Hires: {total_hires}")
            output(f"    Sells: {sells_summary or 'none'}")


if __name__ == "__main__":
    main()
