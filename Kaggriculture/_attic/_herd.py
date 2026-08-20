"""Genome-level production search: herd composition.

Not a clone and not a from-scratch controller -- the third path.  The tape's
production INPUTS are all market orders (HIRE / BUY_LAND / BUY_ANIMAL /
BUY_SEED), and market orders carry no positional state, so they can be mutated
without breaking the tape's actor-local dead reckoning.  COW and SHEEP both
occupy a PASTURE, and v26's _fix_animal_species already repairs a scripted
PICKUP/PLACE to whichever species is actually in hand, so the swap self-heals.

Why herd mix is the right gene: the two matchups that beat us are both supply
floods, and milk is the flooded good.

    MILK  glut 1.45  above_target 1.6   3 shops
    WOOL  glut 1.20  above_target 3.2   1 shop x2 multiplier

Seb dumps 287 milk on top of our 213.  Moving our herd toward wool moves our
revenue out of the market he is crushing and into one he ignores.  That is a
strategy derived from a top player's behaviour, not a copy of it.

Usage:  python _herd.py <opponent.py> [n_seeds]
"""
import importlib.util
import multiprocessing as mp
import os
import statistics
import sys

BASE = "v26.py"
MIXES = [None, (8, 6), (6, 8), (4, 10), (0, 14), (10, 4)]


def fresh(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def herd_agent(n_cow, n_sheep, tag):
    """v26 with its BUY_ANIMAL orders remapped to a target herd composition."""
    module = fresh(BASE, "h_" + tag)
    inner = module.agent
    state = {}

    def agent(obs):
        action = inner(obs)
        try:
            seat = module._seat(obs)
            step = int(module._get(obs, "step", 0) or 0)
            st = state.get(seat)
            if st is None or step <= 0 or step < st["last"]:
                st = {"last": step, "COW": 0, "SHEEP": 0}
                state[seat] = st
            st["last"] = step

            target = {"COW": n_cow, "SHEEP": n_sheep}
            out = []
            for order in list(action.get("market") or []):
                if (order and order[0] == "BUY_ANIMAL" and len(order) >= 3
                        and order[1] in ("COW", "SHEEP")):
                    want = max(0, int(order[2]))
                    scripted = order[1]
                    other = "SHEEP" if scripted == "COW" else "COW"
                    picked = {"COW": 0, "SHEEP": 0}
                    for _ in range(want):
                        # Minimal edit from the tape: keep the scripted species
                        # while its quota lasts, else substitute.  Preserving
                        # the purchase SEQUENCE matters -- reordering it
                        # front-loads cash and starves later buys (-54,329).
                        if st[scripted] < target[scripted]:
                            pick = scripted
                        elif st[other] < target[other]:
                            pick = other
                        else:
                            break
                        st[pick] += 1
                        picked[pick] += 1
                    for species in (scripted, other):
                        if picked[species]:
                            out.append(["BUY_ANIMAL", species, picked[species]])
                else:
                    out.append(order)
            action["market"] = out[:10]
        except Exception:
            pass
        return action

    return agent


def one(job):
    mix, opponent_path, seed, seat = job
    from kaggle_environments import make
    if mix is None:   # control: untouched v26, must reproduce the panel number
        agent = fresh(BASE, f"base_{seed}_{seat}").agent
    else:
        n_cow, n_sheep = mix
        agent = herd_agent(n_cow, n_sheep, f"{n_cow}_{n_sheep}_{seed}_{seat}")
    opponent = fresh(opponent_path, "opp_%d_%d" % (seed % 9973, seat)).agent
    pair = [agent, opponent] if seat == 0 else [opponent, agent]
    env = make("kaggriculture",
               configuration={"episodeSteps": 720, "seed": seed})
    env.run(pair)
    final = env.steps[-1]
    return mix, final[seat].reward - final[1 - seat].reward


def main():
    opponent = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, n + 1)]
    jobs = [(mix, opponent, s, seat)
            for mix in MIXES for s in seeds for seat in (0, 1)]
    workers = max(1, (os.cpu_count() or 4) - 2)
    with mp.Pool(workers) as pool:
        results = pool.map(one, jobs)

    table = {}
    for mix, margin in results:
        table.setdefault(mix, []).append(margin)
    print(f"herd mix vs {os.path.basename(opponent)}  "
          f"({n} seeds x 2 seats = {2 * n} games each)\n")
    print(f"{'COW':>4} {'SHEEP':>6} {'W-L':>8} {'win%':>6} {'mean':>9} "
          f"{'worst':>9}")
    rows = []
    for mix in MIXES:
        margins = table.get(mix, [])
        if not margins:
            continue
        w = sum(1 for m in margins if m > 0)
        rows.append((statistics.mean(margins), mix, w, len(margins),
                     min(margins)))
    for mean, mix, w, total, worst in sorted(rows, key=lambda r: -r[0]):
        marker = ("  <= PASSTHRU CONTROL" if mix is None else "  <= tape default" if mix == (8, 6) else "")
        label = "  -" if mix is None else f"{mix[0]:>4} {mix[1]:>6}"
        print(f"{label:>11} {f'{w}-{total - w}':>8} "
              f"{100 * w / total:>5.1f}% {mean:>+9,.0f} {worst:>+9,.0f}{marker}")


if __name__ == "__main__":
    mp.freeze_support()
    main()
