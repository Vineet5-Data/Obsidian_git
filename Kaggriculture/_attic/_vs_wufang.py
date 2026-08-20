"""Can we beat Wufang Hong (current top player, episode 90666168 seat 1)?"""
import importlib.util

from kaggle_environments import make

SEEDS = [9701, 9702, 9703, 9704, 9705]


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.agent


def duel(a, b, seeds=SEEDS):
    wins = losses = ties = 0
    rows = []
    for seed in seeds:
        for seat in (0, 1):
            pair = [a, b] if seat == 0 else [b, a]
            env = make("kaggriculture",
                       configuration={"episodeSteps": 720, "seed": seed})
            env.run(pair)
            final = env.steps[-1]
            mine, theirs = final[seat].reward, final[1 - seat].reward
            rows.append((seed, seat, mine, theirs, mine - theirs))
            wins += mine > theirs
            losses += mine < theirs
            ties += mine == theirs
    margins = [r[4] for r in rows]
    banks = [r[2] for r in rows]
    return wins, losses, ties, rows, sum(margins) / len(margins), sum(banks) / len(banks)


def main():
    wufang = load("wufang_agent.py", "wufang")
    challengers = [
        ("v13 (live agent)", "v13.py"),
        ("v24_youssef", "v24_youssef.py"),
        ("v24_khanh", "v24_khanh.py"),
        ("v24_thunder", "v24_thunder.py"),
        ("v24_venks", "v24_venks.py"),
    ]
    print(f"vs Wufang Hong (ep 90666168 p1) - seeds {SEEDS}, 10 games each\n")
    for label, path in challengers:
        agent = load(path, label.replace(" ", "_"))
        w, l, t, rows, margin, bank = duel(agent, wufang)
        print(f"{label:18s} {w:2d}-{l}-{t}  margin {margin:+9,.0f}  bank {bank:9,.0f}",
              flush=True)
        detail = "  ".join(f"{s}/{seat}:{m:+,.0f}" for s, seat, _, _, m in rows)
        print(f"                   {detail}", flush=True)


if __name__ == "__main__":
    main()
