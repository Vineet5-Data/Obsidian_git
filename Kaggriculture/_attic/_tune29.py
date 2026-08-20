"""Re-tune the smoothing gate for v29's route, scored on the FULL panel.

SMOOTH_START=250 was fitted to the old build against the step-168 BUY_LAND turn.
This route has a SECOND land purchase at step 264 plus an animal buy at 265,
both of which currently sit INSIDE the smoothing window -- exactly the
cash-starvation pattern that made start=100 score -28,327 in the bear regime.

v29's 20 remaining losses are narrow: family B worst -2,754, Khanh -1,092,
Youssef -528.  A gain of one to three thousand flips most of them, so this is
scored per-opponent on all six, not on an aggregate that would hide them.

Usage:  python _tune29.py [n_seeds]
"""
import importlib.util
import multiprocessing as mp
import os
import statistics
import sys

BASE = "v29.py"

PANEL = [(".loss/o_90711580.py", "familyB"),
         (".field/f_90635979_p1.py", "Khanh"),
         (".field/f_90635229_p1.py", "Youssef"),
         (".loss/o_90729118.py", "mirror"),
         (".field/f_90639963_p1.py", "Seb"),
         ("wufang_agent.py", "Wufang")]

# (SMOOTH_START, SMOOTH_WINDOW, SMOOTH_CAP)
PRESETS = {
    "s250_w8":  (250, 8, 5),      # shipped v29 config
    "s266_w8":  (266, 8, 5),      # clears the step-264 BUY_LAND
    "s266_w16": (266, 16, 5),
    "s300_w8":  (300, 8, 5),
    "s250_w16": (250, 16, 5),
    "s200_w8":  (200, 8, 5),
    "s266_w8c8": (266, 8, 8),
}


def fresh(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def one(job):
    preset, path, seed, seat = job
    from kaggle_environments import make
    tag = f"{preset}_{seed}_{seat}_{os.getpid()}"
    module = fresh(BASE, "t_" + tag)
    start, window, cap = PRESETS[preset]
    module.SMOOTH_START, module.SMOOTH_WINDOW, module.SMOOTH_CAP = start, window, cap
    rival = fresh(path, "o_" + tag).agent
    env = make("kaggriculture",
               configuration={"episodeSteps": 720, "seed": seed})
    env.run([module.agent, rival] if seat == 0 else [rival, module.agent])
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
    print(f"v29 smoothing re-tune -- {len(PANEL)} opponents x {n} seeds "
          f"x 2 seats\n")
    print(f"{'preset':12s}" + "".join(f"{l:>10s}" for _, l in PANEL)
          + f"{'LOSSES':>8s}{'win%':>8s}{'worst':>10s}")
    for preset in PRESETS:
        cells, grand = [], []
        for path, _ in PANEL:
            margins = table.get((preset, path), [])
            grand += margins
            losses = sum(1 for m in margins if m <= 0)
            cells.append(f"{losses}/{len(margins)}".rjust(10) if margins
                         else "-".rjust(10))
        total_losses = sum(1 for m in grand if m <= 0)
        w = len(grand) - total_losses
        tag = "  <= shipped" if preset == "s250_w8" else ""
        print(f"{preset:12s}" + "".join(cells)
              + f"{total_losses:>8d}{100 * w / len(grand):>7.1f}%"
              + f"{min(grand):>+10,.0f}{tag}")


if __name__ == "__main__":
    mp.freeze_support()
    main()
