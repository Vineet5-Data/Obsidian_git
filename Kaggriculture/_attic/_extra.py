"""Author movement for the SURPLUS hands only.  The last lever with headroom.

Measured gap: Seb runs 7 hands/day from day 0, we run 5,0,2,1,4,1,2.  Seven
hands for a whole day costs $33 (hire cost = fib(hires_today), reset nightly),
so this was never a money constraint.  Adding hands alone measured -27,166 to
-116,037 because the tape scripts movement only for the hands it hires -- every
surplus hand spawns on a shed-access tile and _idle_fill finds it no job.

So give them a job.  This is NOT the from-scratch controller that failed before
(_ctrl.py drove every unit and scored -25k to -166k).  The proven tape still
drives hands 0..k-1 untouched; a controller drives only k..n-1.

Index safety: both tapes hire exclusively at hours 0-1, so extras hired from
hour 2 always land at physical indices >= len(tape["hands"]).  _aligned pads
those with PASS, and we fill exactly those slots -- the scripted mapping cannot
shift.  (Injecting at hour 0 DOES shift it: that produced the +135,828 vs Seb /
-30,077 vs family B chaos, which is a desync, not a strategy.)

WATER first because it needs no inventory and no shed trip: two unwatered days
turn a crop into a WEED, and the fertilizer bonus only applies on watered days.

Usage:  python _extra.py [n_seeds]
"""
import importlib.util
import multiprocessing as mp
import os
import statistics
import sys

BASE = "v27.py"
MOVES = {"NORTH": (0, -1), "SOUTH": (0, 1), "EAST": (1, 0), "WEST": (-1, 0)}
SHED_TILES = {(4, 4), (5, 4), (4, 5), (5, 5)}

PANEL = [(".field/f_90639963_p1.py", "Seb"),
         (".loss/o_90711580.py", "family B"),
         ("wufang_agent.py", "Wufang"),
         (".loss/o_90729118.py", "mirror")]

# Target level is not a "jobs" knob, it is a CASH knob.  to7_both scores -356
# and to9_both -23,006 with the identical controller: 9 hires/day costs
# fib(0..8)=$88/day and days 0-6 is exactly when we are broke (money is $25 at
# step 48), so the hires starve the tape's scheduled seed/animal/land buys.
# From day 10 we are rich ($13,554 at step 288) and 14 hires/day costs $986.
# So hire late, not early -- the same "cash earlier, never later" rule that
# every other surviving change on this tape obeys.
PRESETS = {
    "off":        None,
    "d10_to12":   {"target": 12, "hour": 2, "job": 1, "from_day": 10,
                   "ops": ("COLLECT_FERTILIZER", "HARVEST")},
    "d10_to14":   {"target": 14, "hour": 2, "job": 1, "from_day": 10,
                   "ops": ("COLLECT_FERTILIZER", "HARVEST")},
    "d10_to16":   {"target": 16, "hour": 2, "job": 1, "from_day": 10,
                   "ops": ("COLLECT_FERTILIZER", "HARVEST")},
    "d14_to16":   {"target": 16, "hour": 2, "job": 1, "from_day": 14,
                   "ops": ("COLLECT_FERTILIZER", "HARVEST")},
    "d10_to14_nj": {"target": 14, "hour": 2, "job": 0, "from_day": 10},
}


def fresh(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build(preset, tag):
    module = fresh(BASE, "x_" + tag)
    P = PRESETS[preset]
    if P is None:
        return module.agent
    tape = module._ACTIONS
    days = P.get("days", 30)

    for day in range(P.get("from_day", 0), days):
        have = sum(1 for st in tape[day * 24:(day + 1) * 24]
                   for o in (st.get("market") or []) if o and o[0] == "HIRE")
        need = P["target"] - have
        step = day * 24 + P["hour"]
        while need > 0 and step < (day + 1) * 24:
            current = list(tape[step].get("market") or [])
            room = min(10 - len(current), need)
            if room > 0:
                tape[step]["market"] = current + [["HIRE"]] * room
                need -= room
            step += 1

    if not P["job"]:
        return module.agent

    inner_idle = module._idle_fill

    def controller(obs, action):
        action = inner_idle(obs, action)
        try:
            step = int(module._get(obs, "step", 0) or 0)
            scripted = len(tape[min(step, len(tape) - 1)].get("hands") or [])
            farm = module._farm(obs)
            positions = list(module._get(farm, "hands", []) or [])
            rows = module._get(farm, "tiles", []) or []
            hands = list(action.get("hands") or [])

            ops = P.get("ops", ("WATER",))

            def job_here(tile):
                if not isinstance(tile, dict):
                    return None
                for op in ops:
                    if op == "HARVEST" and tile.get("yield_units", 0) > 0:
                        return ["HARVEST"]
                    if (op == "COLLECT_FERTILIZER" and tile.get("animal")
                            and tile.get("fertilizer_available")):
                        return ["COLLECT_FERTILIZER"]
                    if (op == "WATER" and tile.get("kind") == "PLANT"
                            and tile.get("crop") and not tile.get("watered_today")):
                        return ["WATER"]
                return None

            targets = []
            for y, row in enumerate(rows or []):
                for x, tile in enumerate(row or []):
                    if job_here(tile):
                        targets.append((x, y))
            claimed = set()

            for i in range(scripted, len(hands)):
                if i >= len(positions):
                    break
                order = hands[i]
                if order and order[0] != "PASS":
                    continue
                try:
                    hx, hy = int(positions[i][0]), int(positions[i][1])
                except (TypeError, ValueError, IndexError):
                    continue
                here = (rows[hy][hx] if 0 <= hy < len(rows)
                        and 0 <= hx < len(rows[hy] or []) else None)
                job = job_here(here)
                if job:
                    hands[i] = job
                    claimed.add((hx, hy))
                    continue
                free = [t for t in targets if t not in claimed]
                if not free:
                    continue
                tx, ty = min(free, key=lambda t: abs(t[0] - hx) + abs(t[1] - hy))
                claimed.add((tx, ty))
                if tx != hx:
                    hands[i] = ["EAST"] if tx > hx else ["WEST"]
                elif ty != hy:
                    hands[i] = ["SOUTH"] if ty > hy else ["NORTH"]
            action["hands"] = hands
        except Exception:
            pass
        return action

    module._idle_fill = controller
    return module.agent


def one(job):
    preset, path, seed, seat = job
    from kaggle_environments import make
    tag = f"{preset}_{seed}_{seat}_{os.getpid()}"
    a = build(preset, tag)
    b = fresh(path, "o_" + tag).agent
    env = make("kaggriculture",
               configuration={"episodeSteps": 720, "seed": seed})
    env.run([a, b] if seat == 0 else [b, a])
    final = env.steps[-1]
    return (preset, path), final[seat].reward - final[1 - seat].reward


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, n + 1)]
    jobs = [(p, path, s, seat) for p in PRESETS for path, _ in PANEL
            if os.path.exists(path) for s in seeds for seat in (0, 1)]
    with mp.Pool(max(1, (os.cpu_count() or 4) - 2)) as pool:
        results = pool.map(one, jobs)

    table = {}
    for key, margin in results:
        table.setdefault(key, []).append(margin)
    print(f"surplus-hand controller -- {len(PANEL)} opponents x {n} seeds "
          f"x 2 seats\n")
    print(f"{'preset':18s}" + "".join(f"{l:>11s}" for _, l in PANEL)
          + f"{'OVERALL':>11s}{'win%':>8s}")
    for preset in PRESETS:
        cells, grand = [], []
        for path, _ in PANEL:
            margins = table.get((preset, path), [])
            grand += margins
            cells.append(f"{statistics.mean(margins):>+11,.0f}" if margins
                         else f"{'-':>11s}")
        w = sum(1 for m in grand if m > 0)
        tag = "  <= control (v27)" if preset == "off" else ""
        print(f"{preset:18s}" + "".join(cells)
              + f"{statistics.mean(grand):>+11,.0f}{100 * w / len(grand):>7.1f}%{tag}")


if __name__ == "__main__":
    mp.freeze_support()
    main()
