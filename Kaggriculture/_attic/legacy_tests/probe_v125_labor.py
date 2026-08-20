"""Why did v123b's harvest-price fix move the STRAWBERRY expiry counter only 2%?

v123b raised the value of a below-gate STRAWBERRY HARVEST job from 0.0 to
hold_fraction*base.  The 1600-game benchmark moved
`crop expiry with held yield: STRAWBERRY` from 776.02 to 760.75 per game in
days 20-24 -- 2%, against the 86-93% the single-seed probe predicted.

Competing hypothesis: pricing was never the binding constraint.  Only the top
HUNGARIAN_JOBS=48 jobs by value enter the assignment matrix, and a WATER job on
a tile with consecutive_unwatered >= 1 is worth 50000+.  If enough tiles are in
water panic, every HARVEST job is pushed out of the matrix regardless of price.

Instruments crop_service_jobs in-place and reports, per day window:
  - jobs on the board per step, and how many bid >= 50000 (water panic)
  - where the best STRAWBERRY HARVEST job ranks, and whether it makes top 48
  - storage_load, to test the competing `storage_load > 90 -> gain *= 0.1` path
  - STRAWBERRY spot, to test whether the <50 gate is even reached

Usage:  python probe_v125_labor.py SEED SEAT OPPONENT.py AGENT.py [AGENT.py ...]
"""
import collections
import importlib.util
import sys

from kaggle_environments import make

TPD = 24
WINDOWS = ((0, 14), (15, 19), (20, 24), (25, 29))
PANIC = 50000.0


def load(path):
    key = "p_" + path.replace(".", "_").replace("\\", "_").replace("/", "_")
    spec = importlib.util.spec_from_file_location(key, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def window_of(day):
    for lo, hi in WINDOWS:
        if lo <= day <= hi:
            return (lo, hi)
    return None


def instrument(mod):
    """Wrap crop_service_jobs; accumulate one record per (step, tile)."""
    original = mod.crop_service_jobs
    steps = collections.defaultdict(list)

    def wrapped(x, y, tile, step, day, storage_load, spot, opponent_crop_counts):
        jobs, fert = original(x, y, tile, step, day, storage_load, spot,
                              opponent_crop_counts)
        crop = tile.get("crop")
        held = int(tile.get("yield_units", 0) or 0)
        max_step = tile.get("max_lifespan_step")
        try:
            expired = max_step is not None and int(max_step) <= step
        except (TypeError, ValueError):
            expired = False
        for gain, _pos, ops, _req in jobs:
            steps[step].append({
                "op": ops[0], "gain": float(gain), "crop": crop,
                "held": held, "expired": expired,
                "load": storage_load, "spot": float(spot(crop)),
            })
        return jobs, fert

    mod.crop_service_jobs = wrapped
    return steps


def summarize(steps, admit):
    """Aggregate the per-step job boards into the day windows."""
    out = {w: collections.defaultdict(float) for w in WINDOWS}
    counts = {w: 0 for w in WINDOWS}
    for step, board in steps.items():
        w = window_of(step // TPD)
        if w is None:
            continue
        counts[w] += 1
        row = out[w]
        board_sorted = sorted(board, key=lambda r: -r["gain"])
        panic = sum(1 for r in board if r["gain"] >= PANIC)
        row["jobs"] += len(board)
        row["panic"] += panic
        row["load"] += board[0]["load"] if board else 0.0
        row["load_over90"] += 1.0 if board and board[0]["load"] > 90 else 0.0
        # >= 80 is the threshold v125's sell-side relief branch fires on
        row["load_over80"] += 1.0 if board and board[0]["load"] >= 80 else 0.0
        straw = [r for r in board if r["crop"] == "STRAWBERRY"]
        if straw:
            row["straw_spot"] += straw[0]["spot"]
            row["straw_spot_n"] += 1
            row["straw_low"] += 1.0 if straw[0]["spot"] < 50 else 0.0
        # One entry per (step, tile), which is exactly what the benchmark's
        # `crop expiry with held yield` counter increments.  hv_n below counts
        # STEPS and saturates at the window length, so it cannot be compared
        # against the benchmark; expiry_ticks can.
        row["expiry_ticks"] += sum(
            1 for r in board
            if r["op"] == "HARVEST" and r["crop"] == "STRAWBERRY"
            and r["expired"] and r["held"] > 0)
        # best STRAWBERRY HARVEST job on an expired tile, and its board rank
        cand = [r for r in board
                if r["op"] == "HARVEST" and r["crop"] == "STRAWBERRY"
                and r["expired"] and r["held"] > 0]
        if cand:
            best = max(cand, key=lambda r: r["gain"])
            rank = board_sorted.index(best) + 1
            row["hv_n"] += 1
            row["hv_gain"] += best["gain"]
            row["hv_rank"] += rank
            row["hv_zero"] += 1.0 if best["gain"] <= 0.0 else 0.0
            row["hv_admitted"] += 1.0 if rank <= admit else 0.0
    return out, counts


def probe(path, seed, seat, opponent_path):
    mod = load(path)
    opp = load(opponent_path)
    steps = instrument(mod)
    players = [mod.agent, opp.agent] if seat == 0 else [opp.agent, mod.agent]
    env = make("kaggriculture",
               configuration={"episodeSteps": 720, "seed": seed})
    env.run(players)
    final = env.steps[-1]
    out, counts = summarize(steps, mod.HUNGARIAN_JOBS)
    return int(final[seat].reward), int(final[1 - seat].reward), out, counts


if __name__ == "__main__":
    seed, seat, opponent = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    for path in sys.argv[4:]:
        score, oscore, out, counts = probe(path, seed, seat, opponent)
        print(f"\n{path}   score {score:,} vs {oscore:,}  "
              f"margin {score - oscore:+,}")
        print(f"  {'window':8} {'jobs/step':>9} {'load':>6} {'>=80%':>7} "
              f"{'>90%':>6} {'straw spot':>10} {'<50%':>6} "
              f"{'expiry':>7} {'HV gain':>9} {'HV rank':>8} {'admit%':>7}")
        for w in WINDOWS:
            r, n = out[w], max(1, counts[w])
            hv = max(1.0, r["hv_n"])
            sn = max(1.0, r["straw_spot_n"])
            print(f"  {str(w):8} {r['jobs']/n:9.1f} "
                  f"{r['load']/n:6.1f} {100*r['load_over80']/n:6.1f}% "
                  f"{100*r['load_over90']/n:5.1f}% "
                  f"{r['straw_spot']/sn:10.1f} {100*r['straw_low']/sn:5.1f}% "
                  f"{int(r['expiry_ticks']):7d} {r['hv_gain']/hv:9.1f} "
                  f"{r['hv_rank']/hv:8.1f} {100*r['hv_admitted']/hv:6.1f}%")
