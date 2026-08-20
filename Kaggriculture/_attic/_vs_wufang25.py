"""Does premium preemption convert the Wufang coin flip into a win?"""
import importlib.util

from kaggle_environments import make

SEEDS = [9701, 9702, 9703, 9704, 9705]


def load(path, name, **flags):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for key, value in flags.items():
        setattr(module, key, value)
    return module


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
            rows.append((seed, seat, mine - theirs))
            wins += mine > theirs
            losses += mine < theirs
            ties += mine == theirs
    margins = [r[2] for r in rows]
    return wins, losses, ties, rows, sum(margins) / len(margins)


def main():
    wufang = load("wufang_agent.py", "wufang").agent
    v24 = load("v24_youssef.py", "v24").agent
    v25 = load("v25_youssef.py", "v25").agent
    v25_off = load("v25_youssef.py", "v25off", USE_PREEMPT=0).agent

    print(f"seeds {SEEDS}, 10 games each\n")
    for label, agent, opponent, opp_label in (
        ("v24 (no preempt)", v24, wufang, "Wufang"),
        ("v25 (preempt ON)", v25, wufang, "Wufang"),
        ("v25 preempt OFF", v25_off, wufang, "Wufang"),
        ("v25 vs v24", v25, v24, "v24"),
    ):
        w, l, t, rows, margin = duel(agent, opponent)
        print(f"{label:18s} vs {opp_label:8s} {w:2d}-{l}-{t}  margin {margin:+9,.0f}",
              flush=True)
        print("   " + "  ".join(f"{s}/{seat}:{m:+,.0f}" for s, seat, m in rows),
              flush=True)


if __name__ == "__main__":
    main()
