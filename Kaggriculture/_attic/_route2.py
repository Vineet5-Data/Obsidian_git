"""Route search: v27's functional layers over every route we have.

v27 is already a top player's route (Wufang ep 90631991_p1) plus OUR functional
layers -- weed repair, value-ranked idle allocator, price-impact slot ranking,
sell-schedule smoothing.  The route has been treated as fixed all along, but it
is just one of 41 we hold, and the measured production gap to Seb (19 animals
vs 14, 7 hands/day from day 0 vs our 5,0,2,1,4) lives entirely in the route.

So swap the base and keep the layers.  That is the brief exactly: strategies
FROM the top players, not a clone of one -- the layers are what make it robust
to a reprice, and the winner still has to pass the 7-regime stress test before
anything ships.

Pass 1 shortlists on few seeds; the winner gets the full 288-game panel.

Usage:  python _route.py [n_seeds] [top_k_to_print]
"""
import glob
import importlib.util
import multiprocessing as mp
import os
import statistics
import sys

BASE = "v27.py"
# Full panel: the 4-opponent search that produced v29 never scored family B,
# Khanh or Youssef, which are exactly the 20 remaining losses.
OPPONENTS = [(".loss/o_90711580.py", "familyB"),
             (".loss/o_90729118.py", "mirror"),
             (".field/f_90639963_p1.py", "Seb"),
             (".field/f_90635979_p1.py", "Khanh"),
             (".field/f_90635229_p1.py", "Youssef"),
             ("wufang_agent.py", "Wufang")]


def fresh(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def routes():
    found = sorted(glob.glob(".field/f_*.py")) + sorted(glob.glob(".loss/o_*.py"))
    return [p for p in found if os.path.exists(p)]


def grafted(route_path, tag):
    """v27's layers driving a different route's action tape."""
    module = fresh(BASE, "g_" + tag)
    if route_path != BASE:
        module._ACTIONS = fresh(route_path, "t_" + tag)._ACTIONS
    return module.agent


def one(job):
    route_path, opponent_path, seed, seat = job
    from kaggle_environments import make
    tag = f"{abs(hash(route_path)) % 99999}_{seed}_{seat}_{os.getpid()}"
    try:
        a = grafted(route_path, tag)
        b = fresh(opponent_path, "o_" + tag).agent
    except Exception:
        return route_path, None
    env = make("kaggriculture",
               configuration={"episodeSteps": 720, "seed": seed})
    env.run([a, b] if seat == 0 else [b, a])
    final = env.steps[-1]
    return route_path, final[seat].reward - final[1 - seat].reward


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    top_k = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, n + 1)]
    candidates = [BASE] + routes()
    jobs = [(r, o, s, seat) for r in candidates
            for o, _ in OPPONENTS if os.path.exists(o)
            for s in seeds for seat in (0, 1)]
    print(f"{len(candidates)} routes x {len(OPPONENTS)} opponents x {n} seeds "
          f"x 2 seats = {len(jobs)} games", flush=True)
    with mp.Pool(max(1, (os.cpu_count() or 4) - 2)) as pool:
        results = pool.map(one, jobs)

    table = {}
    for route_path, margin in results:
        if margin is not None:
            table.setdefault(route_path, []).append(margin)
    ranked = []
    for route_path, margins in table.items():
        wins = sum(1 for m in margins if m > 0)
        ranked.append((statistics.mean(margins), 100 * wins / len(margins),
                       min(margins), route_path))
    ranked.sort(key=lambda r: (-r[1], -r[2]))   # win% first, then worst case

    print(f"\n{'route':34s} {'mean':>10s} {'win%':>7s} {'worst':>10s}")
    for mean, win, worst, path in ranked[:top_k]:
        mark = "  <= CURRENT BASE" if path == BASE else ""
        print(f"{os.path.basename(path):34s} {win:>6.1f}% {worst:>+10,.0f} "
              f"{mean:>+11,.0f}{mark}")
    base = next((r for r in ranked if r[3] == BASE), None)
    if base and ranked[0][3] != BASE:
        rank = [r[3] for r in ranked].index(BASE) + 1
        print(f"\ncurrent base ranks {rank}/{len(ranked)} "
              f"({base[0]:+,.0f}); best is {os.path.basename(ranked[0][3])} "
              f"({ranked[0][0]:+,.0f})")


if __name__ == "__main__":
    mp.freeze_support()
    main()
