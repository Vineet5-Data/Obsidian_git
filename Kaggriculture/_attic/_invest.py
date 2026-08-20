"""Spend the idle mid-game capital.  The window the evolve run never sampled.

Measured on seed 12345 vs Seb: our median cash is 18,549 against his 9,374, and
from step 288 to 384 we sit on 13k-19k doing nothing while he runs under $500
on 149 turns.  He crosses us at ~step 430 and never gives it back.

The earlier evolutionary search concluded "inserted purchases are always
rejected for want of money" -- but its operator drew step from range(0, 96),
the first four days, which is exactly when we ARE broke.  The cash-rich window
was never tested.  This tests it.

Each preset injects extra purchases at steps where the money is already idle,
respecting the 10-order-per-turn cap by spilling across consecutive turns.

Usage:  python _invest.py [opponent.py] [n_seeds]
"""
import importlib.util
import multiprocessing as mp
import os
import statistics
import sys

BASE = "v27.py"

PRESETS = {
    "off":        None,
    "hire10@300": {"step": 300, "orders": [["HIRE"]] * 10},
    "hire20@300": {"step": 300, "orders": [["HIRE"]] * 20},
    "hire40@300": {"step": 300, "orders": [["HIRE"]] * 40},
    "hire20@250": {"step": 250, "orders": [["HIRE"]] * 20},
    "hire20@380": {"step": 380, "orders": [["HIRE"]] * 20},
    "cow4@300":   {"step": 300, "orders": [["BUY_ANIMAL", "COW", 2]] * 2},
    "land1@300":  {"step": 300, "orders": [["BUY_LAND"]]},
    "mix@300":    {"step": 300, "orders": [["BUY_LAND"]] + [["HIRE"]] * 10
                   + [["BUY_ANIMAL", "COW", 2]] * 2},
}


def fresh(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def invested(preset, tag):
    module = fresh(BASE, "i_" + tag)
    P = PRESETS[preset]
    if P is None:
        return module.agent
    tape = module._ACTIONS
    step, queue = P["step"], list(P["orders"])
    while queue:
        existing = list(tape[step].get("market") or [])
        room = 10 - len(existing)
        if room > 0:
            tape[step]["market"] = existing + queue[:room]
            queue = queue[room:]
        step += 1
        if step >= len(tape):
            break
    return module.agent


def one(job):
    preset, opponent_path, seed, seat = job
    from kaggle_environments import make
    tag = f"{preset}_{seed}_{seat}_{os.getpid()}"
    agent = invested(preset, tag)
    rival = fresh(opponent_path, "riv_" + tag).agent
    pair = [agent, rival] if seat == 0 else [rival, agent]
    env = make("kaggriculture",
               configuration={"episodeSteps": 720, "seed": seed})
    env.run(pair)
    final = env.steps[-1]
    return preset, final[seat].reward - final[1 - seat].reward


def main():
    opponent = sys.argv[1] if len(sys.argv) > 1 else ".field/f_90639963_p1.py"
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, n + 1)]
    jobs = [(p, opponent, s, seat)
            for p in PRESETS for s in seeds for seat in (0, 1)]
    with mp.Pool(max(1, (os.cpu_count() or 4) - 2)) as pool:
        results = pool.map(one, jobs)

    table = {}
    for preset, margin in results:
        table.setdefault(preset, []).append(margin)
    print(f"mid-game reinvestment vs {os.path.basename(opponent)} "
          f"({n} seeds x 2 seats)\n")
    print(f"{'preset':13s} {'W-L':>8} {'win%':>6} {'mean':>9} "
          f"{'worst':>9} {'best':>9}")
    for preset in PRESETS:
        margins = table.get(preset, [])
        if not margins:
            continue
        w = sum(1 for m in margins if m > 0)
        tag = "  <= control (v27)" if preset == "off" else ""
        print(f"{preset:13s} {f'{w}-{len(margins) - w}':>8} "
              f"{100 * w / len(margins):>5.1f}% "
              f"{statistics.mean(margins):>+9,.0f} {min(margins):>+9,.0f} "
              f"{max(margins):>+9,.0f}{tag}")


if __name__ == "__main__":
    mp.freeze_support()
    main()
