"""Re-fight the exact agents that beat us, from their downloaded replays.

Usage: python refight.py [agent.py ...]
"""
import importlib.util
import itertools
import sys

from kaggle_environments import make

from replay_opponent import make_replay_agent, replay_seed

FIGHTS = [
    ("Ragav $84,337",    "replays/episode-90436326-replay.json", "Ragav"),
    ("yuto083 $117,622", "replays/episode-90441743-replay.json", "yuto083"),
]
_uid = itertools.count()


def load(path):
    spec = importlib.util.spec_from_file_location("cand%d" % next(_uid), path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main():
    agents = sys.argv[1:] or ["main.py", "v2.py"]
    tally = {a: [0, 0] for a in agents}
    for label, path, team in FIGHTS:
        seed = replay_seed(path)
        print("\n=== %s (seed %s) ===" % (label, seed), flush=True)
        for f in agents:
            for swap in (False, True):
                us, opp = load(f), make_replay_agent(path, team=team)
                pair = [opp, us.agent] if swap else [us.agent, opp]
                env = make("kaggriculture", configuration={"seed": seed} if seed is not None else {})
                env.run(pair)
                r = env.steps[-1]
                ours = r[1]["reward"] if swap else r[0]["reward"]
                them = r[0]["reward"] if swap else r[1]["reward"]
                win = ours > them
                tally[f][0 if win else 1] += 1
                print("  %-10s seat%d  ours=%8.0f  them=%8.0f  %s"
                      % (f, int(swap), ours, them, "WIN " if win else "LOSS"), flush=True)
    print("\n=== TALLY ===")
    for f, (w, l) in tally.items():
        print("  %-10s %d-%d" % (f, w, l))


if __name__ == "__main__":
    main()
