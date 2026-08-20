"""Is the stationary idle layer worth it? 6 fresh seeds, three ways of asking."""
import importlib.util

from kaggle_environments import make

SEEDS = [9401, 9402, 9403, 9404, 9405, 9406]


def load(name, **flags):
    spec = importlib.util.spec_from_file_location(name, "v24_venks.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for key, value in flags.items():
        setattr(module, key, value)
    return module.agent


def load_v13():
    spec = importlib.util.spec_from_file_location("v13", "v13.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
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
    no_idle = load("no_idle", USE_WEED=1, USE_IDLE=0, USE_IMPACT=1)
    with_idle = load("with_idle", USE_WEED=1, USE_IDLE=1, USE_IMPACT=1)
    v13 = load_v13()

    print(f"seeds {SEEDS} (12 games per row)\n")
    for label, agent in (("idle OFF vs v13", no_idle), ("idle ON  vs v13", with_idle)):
        w, l, t, margin, bank = duel(agent, v13)
        print(f"{label:18s} {w:2d}-{l}-{t}  margin {margin:+9,.0f}  bank {bank:9,.0f}",
              flush=True)

    # Most sensitive test: the two configs against each other. Same route, so any
    # separation is the idle layer alone.
    w, l, t, margin, bank = duel(with_idle, no_idle)
    print(f"\n{'idle ON vs idle OFF':18s} {w:2d}-{l}-{t}  margin {margin:+9,.0f}  bank {bank:9,.0f}")
