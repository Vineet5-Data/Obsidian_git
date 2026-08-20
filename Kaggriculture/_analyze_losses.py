"""Analyze losing matches from top_tournament results.

Runs losing matchups with diagnostics, extracting:
- Per-day money curve for both players
- Product sales comparison  
- Tile utilization comparison
- Key strategic moments where opponent gained advantage
"""
import argparse
import importlib.util
import json
import math
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def load_agent(path):
    name = "m_" + os.path.basename(path).replace(".", "_")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.agent


def replay_seed(replay_id):
    replay_dir = ROOT / "Top_players"
    data = json.loads((replay_dir / f"{replay_id}.json").read_text(encoding="utf-8"))
    return int((data.get("info") or {}).get("seed", 0))


def analyze_game(agent_path, opp_path, seed, seat):
    """Run one game and extract diagnostic data."""
    from kaggle_environments import make
    a = load_agent(agent_path)
    b = load_agent(opp_path)
    pair = [a, b] if seat == 0 else [b, a]
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run(pair)
    
    steps = env.steps
    final = steps[-1]
    our_reward = final[seat].reward
    opp_reward = final[1 - seat].reward
    margin = our_reward - opp_reward
    
    # Extract per-step money curves
    our_money = []
    opp_money = []
    our_tiles = []
    opp_tiles = []
    our_animals = []
    opp_animals = []
    
    for step_data in steps:
        if not step_data or len(step_data) < 2:
            continue
        obs0 = step_data[0].observation if hasattr(step_data[0], 'observation') else {}
        if not obs0:
            continue
        farms = obs0.get("farms") or []
        if len(farms) < 2:
            continue
        
        our_farm = farms[seat]
        opp_farm = farms[1 - seat]
        
        our_money.append(our_farm.get("money", 0))
        opp_money.append(opp_farm.get("money", 0))
        
        # Count tiles
        our_plant_count = 0
        our_animal_count = 0
        opp_plant_count = 0
        opp_animal_count = 0
        
        for row in (our_farm.get("tiles") or []):
            for t in (row or []):
                if isinstance(t, dict):
                    if t.get("kind") == "PLANT":
                        our_plant_count += 1
                    elif "animal" in t:
                        our_animal_count += 1
        
        for row in (opp_farm.get("tiles") or []):
            for t in (row or []):
                if isinstance(t, dict):
                    if t.get("kind") == "PLANT":
                        opp_plant_count += 1
                    elif "animal" in t:
                        opp_animal_count += 1
        
        our_tiles.append(our_plant_count)
        opp_tiles.append(opp_plant_count)
        our_animals.append(our_animal_count)
        opp_animals.append(opp_animal_count)
    
    # Find turning points (where opponent overtakes)
    turning_points = []
    for i in range(1, len(our_money)):
        if i % 24 == 0:  # Check at day boundaries
            day = i // 24
            our_m = our_money[i]
            opp_m = opp_money[i]
            delta = our_m - opp_m
            turning_points.append({
                "day": day,
                "our_money": our_m,
                "opp_money": opp_m,
                "delta": delta,
                "our_plants": our_tiles[i] if i < len(our_tiles) else 0,
                "opp_plants": opp_tiles[i] if i < len(opp_tiles) else 0,
                "our_animals": our_animals[i] if i < len(our_animals) else 0,
                "opp_animals": opp_animals[i] if i < len(opp_animals) else 0,
            })
    
    # Market state at end
    market = {}
    if steps and steps[-1]:
        last_obs = steps[-1][0].observation if hasattr(steps[-1][0], 'observation') else {}
        market = last_obs.get("market", {}) or {}
    
    return {
        "seed": seed,
        "seat": seat,
        "our_reward": our_reward,
        "opp_reward": opp_reward,
        "margin": margin,
        "turning_points": turning_points,
        "final_our_money": our_money[-1] if our_money else 0,
        "final_opp_money": opp_money[-1] if opp_money else 0,
        "market_inv": dict(market.get("inventory", {}) or {}),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", type=Path, default=ROOT / ".top_results.json")
    parser.add_argument("--agent", type=str, default=str(ROOT / "main.py"))
    parser.add_argument("--top-n", type=int, default=10, help="Analyze top N worst losses")
    parser.add_argument("--out", type=Path, default=ROOT / ".loss_analysis.json")
    args = parser.parse_args()
    
    results = json.loads(args.results.read_text(encoding="utf-8"))
    
    # Find opponents we lose to
    losers = []
    for opp_name, detail in results["details"].items():
        if detail["losses"] > 0:
            replay_id = opp_name.rsplit("_", 1)[0]
            opp_seat = int(opp_name.rsplit("_", 1)[1])
            worst_margin = detail["minimum_margin"]
            losers.append({
                "opponent": opp_name,
                "replay_id": replay_id,
                "opp_seat": opp_seat,
                "wins": detail["wins"],
                "losses": detail["losses"],
                "ties": detail["ties"],
                "mean_margin": detail["mean_margin"],
                "worst_margin": worst_margin,
                "margins": detail["margins"],
            })
    
    losers.sort(key=lambda x: x["worst_margin"])
    print(f"\n{'='*70}")
    print(f"LOSING OPPONENTS: {len(losers)} / {results['opponents']}")
    print(f"{'='*70}")
    
    for i, l in enumerate(losers[:20]):
        print(f"\n{i+1}. {l['opponent']}: W{l['wins']}-L{l['losses']}-T{l['ties']} "
              f"mean={l['mean_margin']:+,.0f} worst={l['worst_margin']:+,.0f}")
        for m in l['margins']:
            marker = "W" if m > 0 else ("L" if m < 0 else "T")
            print(f"    {marker} {m:+,.0f}")
    
    # Deep analyze worst losses
    print(f"\n{'='*70}")
    print(f"DEEP ANALYSIS: Top {min(args.top_n, len(losers))} worst losses")
    print(f"{'='*70}")
    
    analyses = []
    top_dir = ROOT / ".top"
    for l in losers[:args.top_n]:
        opp_file = top_dir / f"t_{l['opponent']}.py"
        if not opp_file.exists():
            print(f"  Skipping {l['opponent']}: opponent file not found")
            continue
        
        seed = replay_seed(l['replay_id'])
        # Run the losing seat
        for seat in (0, 1):
            # Check which seat we lost on
            margin_idx = seat  # margins[0] = seat 0, margins[1] = seat 1
            if len(l['margins']) > margin_idx and l['margins'][margin_idx] < 0:
                print(f"\n  Analyzing: {l['opponent']} seat {seat} (margin {l['margins'][margin_idx]:+,.0f})")
                try:
                    analysis = analyze_game(
                        args.agent, str(opp_file), seed, seat
                    )
                    analysis["opponent"] = l["opponent"]
                    analyses.append(analysis)
                    
                    # Print summary
                    print(f"    Final: us=${analysis['our_reward']:,.0f} vs opp=${analysis['opp_reward']:,.0f}")
                    print(f"    Day-by-day money delta:")
                    for tp in analysis["turning_points"]:
                        indicator = ">>>" if tp["delta"] < -5000 else ("<<" if tp["delta"] < 0 else "  ")
                        print(f"      {indicator} Day {tp['day']:2d}: us=${tp['our_money']:>8,.0f} "
                              f"opp=${tp['opp_money']:>8,.0f} delta={tp['delta']:+>8,.0f} "
                              f"plants={tp['our_plants']}/{tp['opp_plants']} "
                              f"animals={tp['our_animals']}/{tp['opp_animals']}")
                except Exception as e:
                    print(f"    Error: {e}")
    
    # Aggregate patterns
    print(f"\n{'='*70}")
    print(f"AGGREGATE PATTERNS ACROSS LOSSES")
    print(f"{'='*70}")
    
    if analyses:
        # When do we fall behind?
        behind_days = {}
        for a in analyses:
            for tp in a["turning_points"]:
                if tp["delta"] < 0:
                    behind_days[tp["day"]] = behind_days.get(tp["day"], 0) + 1
        
        if behind_days:
            print("\nDays we're behind (count):")
            for day in sorted(behind_days):
                print(f"  Day {day}: behind in {behind_days[day]}/{len(analyses)} games")
        
        # Asset comparison at key days
        for check_day in [5, 10, 15, 20, 25]:
            our_avg_plants = []
            opp_avg_plants = []
            our_avg_animals = []
            opp_avg_animals = []
            for a in analyses:
                for tp in a["turning_points"]:
                    if tp["day"] == check_day:
                        our_avg_plants.append(tp["our_plants"])
                        opp_avg_plants.append(tp["opp_plants"])
                        our_avg_animals.append(tp["our_animals"])
                        opp_avg_animals.append(tp["opp_animals"])
            if our_avg_plants:
                print(f"\n  Day {check_day} avg: "
                      f"us plants={sum(our_avg_plants)/len(our_avg_plants):.1f} "
                      f"animals={sum(our_avg_animals)/len(our_avg_animals):.1f} | "
                      f"opp plants={sum(opp_avg_plants)/len(opp_avg_plants):.1f} "
                      f"animals={sum(opp_avg_animals)/len(opp_avg_animals):.1f}")
    
    # Save full analysis
    output = {
        "losers": losers,
        "deep_analyses": analyses,
    }
    args.out.write_text(json.dumps(output, indent=2, default=str), encoding="utf-8")
    print(f"\nFull analysis saved to {args.out}")


if __name__ == "__main__":
    main()
