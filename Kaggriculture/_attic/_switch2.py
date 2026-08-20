"""Opponent-conditional route selection, decided at step 1.

v30 (route o_90729118) and v31 (route f_90635979_p1) are exact complements:

    v30  100% vs mirror / Seb / Wufang,  loses 8 familyB, 6 Khanh, 4 Youssef
    v31  100% vs familyB / Khanh / Youssef, loses 40 mirror, 34 Seb, 17 Wufang

so whoever picks the right tape wins everything.  The opponents are
deterministic replays and their farm is public, but the useful split is not
free: at step 1 only familyB ($158) and Seb ($1,807) separate from the pack
($22), and mirror/Khanh/Youssef/Wufang stay identical until step 169 -- past the
BUY_LAND turn, far too late to switch a route.

What IS available at step 1 is familyB, and familyB is 8 of the 18 losses.  So:
default to v30, switch to v31 only on the familyB signature.  Ceiling is
278/288 = 96.5% if the switch itself is free.

The switch cannot be entirely free -- step 0's purchases came from the other
tape -- so the cost is measured here rather than assumed, at several switch
points, against both the opponent we switch FOR and the ones we must not break.

Usage:  python _switch.py [n_seeds]
"""
import importlib.util
import multiprocessing as mp
import os
import statistics
import sys

A_ROUTE = "v30.py"                       # default
B_ROUTE = "v31.py"                       # switch target

PANEL = [(".loss/o_90711580.py", "familyB"),
         (".field/f_90635979_p1.py", "Khanh"),
         (".field/f_90635229_p1.py", "Youssef"),
         (".loss/o_90729118.py", "mirror"),
         (".field/f_90639963_p1.py", "Seb"),
         ("wufang_agent.py", "Wufang")]

# the six seeds that carry every one of v30's losses, plus clean controls
ADVERSARIAL = [654878655, 774553846, 894229037, 1042155578, 1429432501,
               2056059806]

# switch@1 == switch@24, so a late switch is free.  The Khanh/Youssef split
# only appears at step 169, so measure how late a switch can still be made:
# ORACLE presets switch on ground truth, isolating switch COST from detection.
NEEDS_B = {"familyB", "Khanh", "Youssef"}

PRESETS = {
    "v30":        None,
    "switch@1":   {"mode": "detect", "at": 1},
    "oracle@1":   {"mode": "oracle", "at": 1},
    "oracle@100": {"mode": "oracle", "at": 100},
    "oracle@169": {"mode": "oracle", "at": 169},
    "oracle@240": {"mode": "oracle", "at": 240},
    "oracle@360": {"mode": "oracle", "at": 360},
}


def fresh(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def hybrid(preset, tag, label=None):
    module = fresh(A_ROUTE, "s_" + tag)
    P = PRESETS[preset]
    if P is None:
        return module.agent
    tape_b = fresh(B_ROUTE, "b_" + tag)._ACTIONS
    if P["mode"] == "always":
        module._ACTIONS = tape_b
        return module.agent

    tape_a = module._ACTIONS
    inner = module.agent
    state = {"switched": None}

    def agent(obs):
        try:
            step = int(module._get(obs, "step", 0) or 0)
            if step <= 0:
                state["switched"] = None
            if state["switched"] is None and step >= P["at"] and P["mode"] == "oracle":
                state["switched"] = label in NEEDS_B
                module._ACTIONS = tape_b if state["switched"] else tape_a
            elif state["switched"] is None and step >= P["at"]:
                # familyB is the only rival separable this early: it has spent
                # down to ~$158 by step 1 where everyone else sits at $22.
                seat = module._seat(obs)
                farms = module._get(obs, "farms", []) or []
                rival = farms[1 - seat] if len(farms) > 1 else {}
                money = int(module._get(rival, "money", 0) or 0)
                state["switched"] = 100 <= money <= 400
                module._ACTIONS = tape_b if state["switched"] else tape_a
        except Exception:
            pass
        return inner(obs)

    return agent


def one(job):
    preset, path, seed, seat = job
    from kaggle_environments import make
    tag = f"{preset}_{seed}_{seat}_{os.getpid()}"
    label = dict((p, l) for p, l in PANEL)[path]
    a = hybrid(preset, tag, label)
    b = fresh(path, "o_" + tag).agent
    env = make("kaggriculture",
               configuration={"episodeSteps": 720, "seed": seed})
    env.run([a, b] if seat == 0 else [b, a])
    final = env.steps[-1]
    return (preset, path), final[seat].reward - final[1 - seat].reward


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    seeds = ADVERSARIAL + [(i * 2654435761) % 2147483647 for i in range(1, n + 1)]
    jobs = [(p, path, s, seat) for p in PRESETS for path, _ in PANEL
            if os.path.exists(path) for s in seeds for seat in (0, 1)]
    with mp.Pool(max(1, (os.cpu_count() or 4) - 2)) as pool:
        results = pool.map(one, jobs)

    table = {}
    for key, margin in results:
        table.setdefault(key, []).append(margin)
    print(f"route switching -- {len(PANEL)} opponents x {len(seeds)} seeds "
          f"(6 adversarial + {n} clean) x 2 seats\n")
    print(f"{'preset':12s}" + "".join(f"{l:>10s}" for _, l in PANEL)
          + f"{'LOSSES':>8s}{'win%':>8s}{'worst':>10s}")
    for preset in PRESETS:
        cells, grand = [], []
        for path, _ in PANEL:
            margins = table.get((preset, path), [])
            grand += margins
            cells.append(f"{sum(1 for m in margins if m <= 0)}/{len(margins)}"
                         .rjust(10) if margins else "-".rjust(10))
        losses = sum(1 for m in grand if m <= 0)
        tag = "  <= v30" if preset == "v30" else ""
        print(f"{preset:12s}" + "".join(cells)
              + f"{losses:>8d}{100 * (len(grand) - losses) / len(grand):>7.1f}%"
              + f"{min(grand):>+10,.0f}{tag}")


if __name__ == "__main__":
    mp.freeze_support()
    main()
