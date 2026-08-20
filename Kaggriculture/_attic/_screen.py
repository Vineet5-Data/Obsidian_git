"""Seat-swapped screen of candidate routes against the incumbent (v13).

Held-out seeds only: none of these were used to tune v13.
"""
import importlib.util
import sys

from kaggle_environments import make

SEEDS = [9101, 9102, 9103]


def load(path, name=None):
    name = name or path.replace(".py", "").replace("/", "_")
    spec = importlib.util.spec_from_file_location(f"kagri_{name}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.agent


def duel(a, b, seeds=SEEDS):
    wins = losses = ties = 0
    margins = []
    banks = []
    for seed in seeds:
        for seat in (0, 1):
            pair = [a, b] if seat == 0 else [b, a]
            env = make("kaggriculture",
                       configuration={"episodeSteps": 720, "seed": seed},
                       debug=False)
            env.run(pair)
            final = env.steps[-1]
            mine, theirs = final[seat].reward, final[1 - seat].reward
            if mine is None or theirs is None:
                continue
            banks.append(mine)
            margins.append(mine - theirs)
            if mine > theirs:
                wins += 1
            elif mine < theirs:
                losses += 1
            else:
                ties += 1
    return wins, losses, ties, sum(margins) / max(1, len(margins)), sum(banks) / max(1, len(banks))


if __name__ == "__main__":
    incumbent = load("v13.py", "v13")
    candidates = sys.argv[1:] or [
        "cand_khanh.py", "cand_youssef.py", "cand_thunder.py",
        "cand_tman.py", "cand_venks.py", "cand_ocean.py",
    ]
    print(f"seeds={SEEDS}  (6 games each, seat-swapped)  vs v13\n")
    results = []
    for path in candidates:
        agent = load(path)
        w, l, t, margin, bank = duel(agent, incumbent)
        results.append((w - l, margin, path, w, l, t, bank))
        print(f"{path:20s} {w}-{l}-{t}  margin {margin:+9,.0f}  mean bank {bank:9,.0f}",
              flush=True)
    print("\n=== ranked ===")
    for _, margin, path, w, l, t, bank in sorted(results, reverse=True):
        print(f"{path:20s} {w}-{l}-{t}  margin {margin:+9,.0f}  bank {bank:9,.0f}")
