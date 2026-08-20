"""Measure how often v122's <50 HARVEST gate switches STRAWBERRY off.

Not a benchmark.  A handful of paired seasons against one real panel opponent,
instrumented per step:

  * the STRAWBERRY spot the agent actually sees,
  * how long it sits below the 50 gate,
  * expired-tile-steps holding unharvested yield, per day window, which is the
    same counter the 1600-game telemetry reports as STRAWBERRY=776/game.

Self-play is not a valid probe here: both seats self-limit supply through the
same greedy marginal allocator, so the market never crashes.  The panel
opponent produces ~160 STRAWBERRY units in days 20-24 against our ~61.

Usage:
  python probe_strawberry_gate.py OPPONENT.py CANDIDATE.py [CANDIDATE.py ...]
"""
import importlib.util
import sys

from kaggle_environments import make

TPD = 24
GATE = 50
WINDOWS = ((0, 14), (15, 19), (20, 24), (25, 29))
SEEDS = (267601732, 387276923)


def load(path):
    spec = importlib.util.spec_from_file_location(
        "p_" + path.replace(".", "_").replace("\\", "_").replace("/", "_"), path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def window_of(day):
    for lo, hi in WINDOWS:
        if lo <= day <= hi:
            return (lo, hi)
    return None


def probe(cand_path, opp_path, seed, seat):
    mod = load(cand_path)
    opp = load(opp_path)
    players = [mod.agent, opp.agent] if seat == 0 else [opp.agent, mod.agent]

    env = make("kaggriculture",
               configuration={"episodeSteps": 720, "seed": seed})
    env.run(players)

    below = 0
    lowest = 10 ** 9
    expired = {w: 0 for w in WINDOWS}
    ripe_below = {w: 0 for w in WINDOWS}
    for step, frame in enumerate(env.steps):
        obs = frame[0]["observation"]
        spot = mod.price("STRAWBERRY", obs["market"]["inventory"]["STRAWBERRY"])
        lowest = min(lowest, spot)
        if spot < GATE:
            below += 1
        window = window_of(step // TPD)
        if window is None:
            continue
        farm = obs["farms"][seat]
        for row in farm["tiles"]:
            for tile in row:
                if not (isinstance(tile, dict) and tile.get("kind") == "PLANT"):
                    continue
                if tile.get("crop") != "STRAWBERRY":
                    continue
                if int(tile.get("yield_units", 0) or 0) <= 0:
                    continue
                if spot < GATE:
                    ripe_below[window] += 1
                mls = tile.get("max_lifespan_step", -1)
                if mls is not None and mls >= 0 and int(mls) <= step:
                    expired[window] += 1

    final = env.steps[-1][seat]
    return {
        "score": int(final.reward),
        "opp_score": int(env.steps[-1][1 - seat].reward),
        "below": below,
        "lowest": lowest,
        "expired": expired,
        "ripe_below": ripe_below,
        "status": str(final.status),
    }


if __name__ == "__main__":
    opponent, candidates = sys.argv[1], sys.argv[2:]
    for seed in SEEDS:
        for seat in (0, 1):
            print(f"\n=== seed {seed} seat {seat} vs {opponent} ===")
            for path in candidates:
                r = probe(path, opponent, seed, seat)
                win = "WIN " if r["score"] > r["opp_score"] else "loss"
                exp = " ".join(f"d{lo}-{hi}={r['expired'][(lo, hi)]}"
                               for lo, hi in WINDOWS)
                rb = sum(r["ripe_below"].values())
                print(f"  {path:34s} {win} {r['score']:>8,} vs "
                      f"{r['opp_score']:>8,}  min STRAWBERRY spot "
                      f"{r['lowest']:>4}  steps below gate {r['below']:>4}  "
                      f"ripe-tile-steps below gate {rb:>5}")
                print(f"  {'':34s} expired-tile-steps holding yield: {exp}")
