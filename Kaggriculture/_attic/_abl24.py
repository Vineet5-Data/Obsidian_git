"""Ablate v24's three overlay layers against v13, on seeds used for nothing else."""
import importlib.util

from kaggle_environments import make

SEEDS = [9301, 9302, 9303]
VARIANTS = [
    ("route only",   dict(USE_WEED=0, USE_IDLE=0, USE_IMPACT=0)),
    ("+weed",        dict(USE_WEED=1, USE_IDLE=0, USE_IMPACT=0)),
    ("+idle",        dict(USE_WEED=0, USE_IDLE=1, USE_IMPACT=0)),
    ("+impact",      dict(USE_WEED=0, USE_IDLE=0, USE_IMPACT=1)),
    ("all three",    dict(USE_WEED=1, USE_IDLE=1, USE_IMPACT=1)),
]


def load(path, name, **flags):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for key, value in flags.items():
        setattr(module, key, value)
    return module.agent


def duel(a, b, seeds=SEEDS):
    wins = losses = ties = 0
    margins, banks = [], []
    for seed in seeds:
        for seat in (0, 1):
            pair = [a, b] if seat == 0 else [b, a]
            env = make("kaggriculture",
                       configuration={"episodeSteps": 720, "seed": seed})
            env.run(pair)
            final = env.steps[-1]
            mine, theirs = final[seat].reward, final[1 - seat].reward
            margins.append(mine - theirs)
            banks.append(mine)
            wins += mine > theirs
            losses += mine < theirs
            ties += mine == theirs
    return wins, losses, ties, sum(margins) / len(margins), sum(banks) / len(banks)


if __name__ == "__main__":
    v13 = load("v13.py", "v13")
    print(f"v24_venks overlay ablation vs v13, seeds {SEEDS}\n")
    for label, flags in VARIANTS:
        agent = load("v24_venks.py", "v24_" + label.replace(" ", "_"), **flags)
        w, l, t, margin, bank = duel(agent, v13)
        print(f"{label:12s} {w}-{l}-{t}  margin {margin:+9,.0f}  bank {bank:9,.0f}",
              flush=True)
