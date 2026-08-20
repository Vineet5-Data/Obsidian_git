"""Find a discriminator that separates Khanh/Youssef from Wufang on ALL seeds.

v32 is 286-2 (99.3%).  Both remaining losses are Youssef, worst -57, and route
B beats Youssef 48-0 on its own -- so they are MISCLASSIFICATIONS, not route
failures: on those seeds Youssef's money delta fell below the -133 threshold and
we kept route A.

Money alone is a thin signal (the Khanh/Wufang gap measured only ~5 on seven
seeds).  This measures richer public features at the switch step across all 24
panel seeds so the threshold can be replaced by something with real margin.

Features are all observable: the rival's farm is fully visible, and its
cumulative sales are exactly identified from shared-market inventory deltas
minus our own sales.
"""
import importlib.util
import multiprocessing as mp
import os
import sys

GROUP_B = {"Khanh", "Youssef", "familyB"}
OPP = [(".field/f_90635229_p1.py", "Youssef"),
       (".field/f_90635979_p1.py", "Khanh"),
       ("wufang_agent.py", "Wufang"),
       (".loss/o_90729118.py", "mirror"),
       (".loss/o_90711580.py", "familyB")]
STEP = 200


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def probe(job):
    path, label, seed = job
    from kaggle_environments import make
    tag = f"{label}_{seed}_{os.getpid()}"
    me = load("v30.py", "me_" + tag).agent
    rival = load(path, "op_" + tag).agent
    env = make("kaggriculture",
               configuration={"episodeSteps": 720, "seed": seed})
    env.run([me, rival])
    obs = env.steps[STEP][0]["observation"]
    farms = obs["farms"]
    animals = plants = 0
    for row in (farms[1].get("tiles") or []):
        for tile in (row or []):
            if isinstance(tile, dict):
                if tile.get("animal"):
                    animals += 1
                elif tile.get("kind") == "PLANT":
                    plants += 1
    # rival cumulative sales, exactly identified from the shared book
    inv0 = env.steps[0][0]["observation"]["market"]["inventory"]
    inv = obs["market"]["inventory"]
    mine = {}
    for i in range(STEP):
        for o in ((env.steps[i + 1][0].get("action") or {}).get("market") or []):
            if o and o[0] == "SELL" and len(o) >= 3:
                mine[o[1]] = mine.get(o[1], 0) + int(o[2])
    rival_supply = sum(inv[k] - inv0[k] + mine.get(k, 0) for k in inv)
    return (label, seed,
            int(farms[1]["money"]) - int(farms[0]["money"]),
            animals, plants, int(rival_supply))


def main():
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, 25)]
    jobs = [(p, l, s) for p, l in OPP if os.path.exists(p) for s in seeds]
    with mp.Pool(max(1, (os.cpu_count() or 4) - 2)) as pool:
        rows = pool.map(probe, jobs)

    by = {}
    for label, seed, delta, animals, plants, supply in rows:
        by.setdefault(label, []).append((delta, animals, plants, supply, seed))

    print(f"features at step {STEP}, 24 seeds each\n")
    print(f"{'opp':9s} {'grp':4s} {'delta range':>20s} {'animals':>9s} "
          f"{'plants':>8s} {'rival_supply range':>22s}")
    for label, _ in [(l, p) for p, l in OPP]:
        v = by.get(label)
        if not v:
            continue
        d = sorted(x[0] for x in v)
        s = sorted(x[3] for x in v)
        print(f"{label:9s} {'B' if label in GROUP_B else 'A':4s} "
              f"{f'{d[0]} .. {d[-1]}':>20s} "
              f"{sorted({x[1] for x in v})!s:>9s} "
              f"{sorted({x[2] for x in v})!s:>8s} "
              f"{f'{s[0]} .. {s[-1]}':>22s}")

    # the only ambiguous pair: Khanh/Youssef (B) against Wufang (A)
    b = [x for l in ("Khanh", "Youssef") for x in by.get(l, [])]
    a = by.get("Wufang", [])
    for idx, name in ((0, "money delta"), (3, "rival supply")):
        bv = [x[idx] for x in b]
        av = [x[idx] for x in a]
        gap = min(bv) - max(av)
        print(f"\n{name}: B min {min(bv)}, A max {max(av)}, gap {gap} "
              f"-> {'SEPARABLE' if gap > 0 else 'OVERLAP'}")
        if gap > 0:
            print(f"   safe threshold: {(min(bv) + max(av)) // 2}")


if __name__ == "__main__":
    mp.freeze_support()
    main()
