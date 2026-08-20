"""Screen every family-A pool route against Wufang Hong. Find one that beats him."""
import importlib.util

from kaggle_environments import make

SEEDS = [9701, 9702, 9703]
CANDS = ["v24_youssef", "v24_khanh", "v24_tman2", "v24_ocean2", "v24_manual",
         "v24_jiajun", "v24_lemon", "v24_azelearn", "v24_wufangA", "v24_wufangB"]


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.agent


def duel(a, b, seeds=SEEDS):
    wins = losses = ties = 0
    margins = []
    for seed in seeds:
        for seat in (0, 1):
            pair = [a, b] if seat == 0 else [b, a]
            env = make("kaggriculture",
                       configuration={"episodeSteps": 720, "seed": seed})
            env.run(pair)
            final = env.steps[-1]
            mine, theirs = final[seat].reward, final[1 - seat].reward
            margins.append(mine - theirs)
            wins += mine > theirs
            losses += mine < theirs
            ties += mine == theirs
    return wins, losses, ties, sum(margins) / len(margins)


def main():
    wufang = load("wufang_agent.py", "wufang")
    print(f"vs Wufang Hong - seeds {SEEDS}, 6 games each\n")
    results = []
    for name in CANDS:
        agent = load(name + ".py", name)
        w, l, t, margin = duel(agent, wufang)
        results.append((w - l, margin, name, w, l, t))
        print(f"{name:16s} {w}-{l}-{t}  margin {margin:+9,.0f}", flush=True)
    print("\n=== ranked ===")
    for _, margin, name, w, l, t in sorted(results, reverse=True):
        print(f"{name:16s} {w}-{l}-{t}  margin {margin:+9,.0f}")


if __name__ == "__main__":
    main()
