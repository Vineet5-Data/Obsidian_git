"""Final validation of the chosen route against every opponent we have."""
import importlib.util

from kaggle_environments import make

SEEDS = [9801, 9802, 9803, 9804, 9805]
CHAMPION = "v24_wufangB.py"


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.agent


def duel(a, b, seeds=SEEDS):
    wins = losses = ties = 0
    margins, banks, worst = [], [], None
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
            if worst is None or mine - theirs < worst[0]:
                worst = (mine - theirs, seed, seat)
            wins += mine > theirs
            losses += mine < theirs
            ties += mine == theirs
    return (wins, losses, ties, sum(margins) / len(margins),
            sum(banks) / len(banks), min(banks), worst)


def main():
    champion = load(CHAMPION, "champion")
    opponents = [
        ("v13 (incumbent)", load("v13.py", "v13")),
        ("Wufang ep90666168", load("wufang_agent.py", "wufang")),
        ("v24_youssef (peer)", load("v24_youssef.py", "youssef")),
        ("Seb ep90503598", load("seb_agent.py", "seb")),
        ("Seb ep90473753", load("seb2_agent.py", "seb2")),
        ("ref_top30", load("ref_top30.py", "ref")),
    ]
    print(f"{CHAMPION} - seeds {SEEDS}, 10 games each (seat-swapped)\n")
    total_w = total_l = total_t = 0
    for label, opponent in opponents:
        w, l, t, margin, bank, floor, worst = duel(champion, opponent)
        total_w += w
        total_l += l
        total_t += t
        print(f"{label:18s} {w:2d}-{l}-{t}  margin {margin:+9,.0f}  "
              f"bank {bank:9,.0f}  floor {floor:9,.0f}  worst {worst[0]:+8,.0f} "
              f"(seed {worst[1]} seat {worst[2]})", flush=True)
    print(f"\nTOTAL {total_w}-{total_l}-{total_t}")


if __name__ == "__main__":
    main()
