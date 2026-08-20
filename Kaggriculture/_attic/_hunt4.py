"""Find a route that sweeps the three opponents v30 still loses to.

v30 = route o_90729118 + our functional stack: 93.8% on 288 games, and every
one of the 18 losses is family B (8/48), Khanh (6/48) or Youssef (4/48).
The search that picked that route scored all six opponents jointly on 2 seeds,
so it never asked the question that matters now: does some OTHER route beat
these three specifically?

If one does, and o_90729118 beats the other three, the two can be combined --
the opponent is identifiable from its opening market orders long before the
routes diverge in any way that matters.

Scored on losses, not mean.  Mean is useless here: it is dominated by a +172k
rout against Seb that hides exactly the games in question.

Usage:  python _hunt3.py [n_seeds]
"""
import glob
import importlib.util
import multiprocessing as mp
import os
import statistics
import sys

BASE = "v30.py"
TARGETS = [(".loss/o_90711580.py", "familyB"),
           (".field/f_90635979_p1.py", "Khanh"),
           (".field/f_90635229_p1.py", "Youssef")]


def fresh(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def routes():
    return sorted(glob.glob(".field/f_*.py")) + sorted(glob.glob(".loss/o_*.py"))


def one(job):
    route_path, opponent_path, seed, seat = job
    from kaggle_environments import make
    tag = f"{abs(hash(route_path)) % 99999}_{seed}_{seat}_{os.getpid()}"
    try:
        module = fresh(BASE, "h_" + tag)
        if route_path != BASE:
            module._ACTIONS = fresh(route_path, "t_" + tag)._ACTIONS
        rival = fresh(opponent_path, "o_" + tag).agent
    except Exception:
        return (route_path, opponent_path), None
    env = make("kaggriculture",
               configuration={"episodeSteps": 720, "seed": seed})
    env.run([module.agent, rival] if seat == 0 else [rival, module.agent])
    final = env.steps[-1]
    return (route_path, opponent_path), final[seat].reward - final[1 - seat].reward


# The 18 losses concentrate on exactly six seeds, and each is identical in both
# seats -- so the seed alone (weed spawns, shop unlock order) decides them, and
# one seat per seed is sufficient.  Hunt on the adversarial seeds directly.
ADVERSARIAL = [654878655, 774553846, 894229037, 1042155578, 1429432501,
               2056059806]


def main():
    seeds = ADVERSARIAL
    candidates = [BASE] + routes()
    jobs = [(r, o, s, 0) for r in candidates for o, _ in TARGETS
            if os.path.exists(o) for s in seeds]
    print(f"{len(candidates)} routes x {len(TARGETS)} opponents x "
          f"{len(seeds)} ADVERSARIAL seeds = {len(jobs)} games", flush=True)
    with mp.Pool(max(1, (os.cpu_count() or 4) - 2)) as pool:
        results = pool.map(one, jobs)

    table = {}
    for key, margin in results:
        if margin is not None:
            table.setdefault(key, []).append(margin)

    rows = []
    for route_path in candidates:
        cells, total_losses, worst = [], 0, None
        ok = True
        for opponent_path, _ in TARGETS:
            margins = table.get((route_path, opponent_path), [])
            if not margins:
                ok = False
                break
            losses = sum(1 for m in margins if m <= 0)
            total_losses += losses
            worst = min(margins) if worst is None else min(worst, min(margins))
            cells.append(f"{losses}/{len(margins)}")
        if ok:
            rows.append((total_losses, -(worst or 0), route_path, cells, worst))
    rows.sort(key=lambda r: (r[0], r[1]))

    print(f"\n{'route':30s}" + "".join(f"{l:>10s}" for _, l in TARGETS)
          + f"{'LOSSES':>8s}{'worst':>11s}")
    for losses, _, path, cells, worst in rows[:16]:
        mark = "  <= v30 base" if path == BASE else ""
        print(f"{os.path.basename(path):30s}"
              + "".join(c.rjust(10) for c in cells)
              + f"{losses:>8d}{worst:>+11,.0f}{mark}")
    clean = [r for r in rows if r[0] == 0]
    print(f"\nroutes losing NOTHING to all three: {len(clean)}")
    for r in clean:
        print("   ", os.path.basename(r[2]), f"worst {r[4]:+,.0f}")


if __name__ == "__main__":
    mp.freeze_support()
    main()
