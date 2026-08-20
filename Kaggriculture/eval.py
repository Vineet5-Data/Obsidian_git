"""Evaluation harness: run main.py against the built-in baselines over full 720-step episodes.

Usage:  python eval.py [N_EPISODES] [opponent ...]
        python eval.py 3 starter random
"""

import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
AGENT = os.path.join(HERE, "main.py")


def _ensure_env():
    try:
        import kaggle_environments  # noqa: F401
    except ImportError:
        print("installing kaggle-environments ...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "kaggle-environments"])


def run_episode(opponent, seed, debug=False):
    from kaggle_environments import make
    env = make("kaggriculture", configuration={"seed": seed}, debug=debug)
    env.run([AGENT, opponent])
    last = env.steps[-1]
    return float(last[0]["reward"] or 0.0), float(last[1]["reward"] or 0.0)


def main():
    _ensure_env()
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    opponents = sys.argv[2:] or ["starter", "random"]

    summary = {}
    for opp in opponents:
        wins = 0
        mine = []
        theirs = []
        for i in range(n):
            seed = 1000 + i
            t0 = time.time()
            a, b = run_episode(opp, seed)
            win = a > b
            wins += win
            mine.append(a)
            theirs.append(b)
            print("vs %-8s seed=%-5d  me=$%-10.0f opp=$%-10.0f  %s   (%.1fs)"
                  % (opp, seed, a, b, "WIN " if win else "LOSS", time.time() - t0))
        summary[opp] = (wins, n, sum(mine) / n, sum(theirs) / n, min(mine))

    print("\n" + "=" * 72)
    for opp, (w, tot, am, at, worst) in summary.items():
        print("vs %-8s  win-rate %d/%d (%.0f%%)   mean me $%.0f   mean opp $%.0f   worst me $%.0f"
              % (opp, w, tot, 100.0 * w / tot, am, at, worst))
    print("=" * 72)


if __name__ == "__main__":
    main()
