"""Diagnose v124's collapse on seed 654878655.

v124 rescues near-cap animals whose product price has crashed. The 16-seed
screen rejected it (-647.8 paired mean, 202-118 against v122's 212-108) with
individual games falling 23,000+. This measures the suspected mechanism:
harvested MILK/WOOL floods a fixed-size shed, and the shed is shared with the
crop harvests that are actually worth money.

Usage:  python probe_v124_regression.py SEED SEAT AGENT.py [AGENT.py ...]
"""
import importlib.util
import sys

from kaggle_environments import make

TPD = 24
SHED_CAP = 100


def load(path):
    spec = importlib.util.spec_from_file_location(
        "p_" + path.replace(".", "_").replace("\\", "_").replace("/", "_"), path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def probe(path, seed, seat, opponent_path):
    mod = load(path)
    opp = load(opponent_path)
    players = [mod.agent, opp.agent] if seat == 0 else [opp.agent, mod.agent]
    env = make("kaggriculture",
               configuration={"episodeSteps": 720, "seed": seed})
    env.run(players)

    shed_peak = 0
    shed_full_steps = 0
    shed_by_day = {}
    low_milk = low_wool = 0
    cap_ticks = 0
    for step, frame in enumerate(env.steps):
        obs = frame[0]["observation"]
        inv = obs["market"]["inventory"]
        if mod.price("MILK", inv["MILK"]) < 50:
            low_milk += 1
        if mod.price("WOOL", inv["WOOL"]) < 50:
            low_wool += 1
        own = frame[seat]["observation"]
        private = own.get("private") or {}
        shed = private.get("shed") or {}
        used = sum(int(v or 0) for v in shed.values())
        farm = obs["farms"][seat]
        shed_peak = max(shed_peak, used)
        shed_full_steps += used >= SHED_CAP - 5
        shed_by_day.setdefault(step // TPD, []).append(used)
        for row in farm["tiles"]:
            for tile in row:
                if isinstance(tile, dict) and "animal" in tile:
                    a = mod.ANIMALS.get(tile["animal"])
                    if a and int(tile.get("yield_units", 0) or 0) >= a["mh"]:
                        cap_ticks += 1

    final = env.steps[-1]
    shed_final = ((env.steps[-1][seat]["observation"].get("private") or {})
                  .get("shed") or {})
    return {
        "score": int(final[seat].reward),
        "opp": int(final[1 - seat].reward),
        "shed_peak": shed_peak,
        "shed_full_steps": shed_full_steps,
        "low_milk_steps": low_milk,
        "low_wool_steps": low_wool,
        "animal_cap_ticks": cap_ticks,
        "shed_mid": {d: round(sum(v) / len(v)) for d, v in
                     sorted(shed_by_day.items()) if d in (10, 15, 20, 25, 29)},
        "shed_final": {k: v for k, v in sorted(shed_final.items()) if v},
    }


if __name__ == "__main__":
    seed, seat = int(sys.argv[1]), int(sys.argv[2])
    opponent = ".top/t_91636055_0.py"
    for path in sys.argv[3:]:
        r = probe(path, seed, seat, opponent)
        print(f"\n{path}")
        print(f"  score {r['score']:>9,} vs {r['opp']:>9,}   "
              f"margin {r['score'] - r['opp']:+,}")
        print(f"  shed peak {r['shed_peak']:>3}/100   "
              f"steps at >=95: {r['shed_full_steps']:>4}   "
              f"animal cap ticks {r['animal_cap_ticks']:>5}")
        print(f"  steps with MILK<50: {r['low_milk_steps']:>4}   "
              f"WOOL<50: {r['low_wool_steps']:>4}")
        print(f"  mean shed used by day: {r['shed_mid']}")
        print(f"  final shed contents: {r['shed_final']}")
