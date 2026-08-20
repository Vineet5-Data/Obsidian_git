"""Moves per productive action -- the metric the loss replays identified.

Kaggle replays (2026-08-10): v67_lin 1.60, opponents 1.01, Wufang ~1.08.
Movement is the tax; everything else is work.  This is the fast inner-loop
signal -- it moves on a handful of episodes, where win% needs a full panel.

  python bench/effmeter.py v67_lin.py v80_block.py --seeds 3
"""
import argparse
import collections
import glob
import importlib.util
import os
import random
import sys

from kaggle_environments import make

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOVES = {"NORTH", "SOUTH", "EAST", "WEST"}


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def census(env, seat):
    c = collections.Counter()
    for step in env.steps:
        act = step[seat].action
        if not isinstance(act, dict):
            continue
        f = act.get("farmer")
        for u in ([f] if f else []) + list(act.get("hands") or []):
            if u:
                c[u[0]] += 1
    return c


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("agents", nargs="+")
    ap.add_argument("--seeds", type=int, default=3)
    ap.add_argument("--opps", type=int, default=4)
    args = ap.parse_args()

    pool = sorted(glob.glob(os.path.join(ROOT, ".top", "*.py")) +
                  glob.glob(os.path.join(ROOT, ".pure", "*.py")))
    rng = random.Random(12345)
    opps = rng.sample(pool, min(args.opps, len(pool)))
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, args.seeds + 1)]

    print(f"opponents: {[os.path.basename(o) for o in opps]}")
    print(f"seeds: {seeds}\n")
    print(f"{'agent':>22} {'mv/prod':>8} {'move%':>7} {'prod':>8} "
          f"{'reward':>10} {'win%':>6}")

    for ap_ in args.agents:
        me = load(os.path.join(ROOT, ap_), "cand_" + os.path.basename(ap_)[:-3])
        mv = prod = passes = 0
        rewards = []
        wins = games = 0
        for opath in opps:
            opp = load(opath, "opp_" + os.path.basename(opath)[:-3])
            for sd in seeds:
                # seat-swap on the SAME seed so board luck cancels
                for seat in (0, 1):
                    env = make("kaggriculture",
                               configuration={"episodeSteps": 720, "seed": sd})
                    pair = [me.agent, opp.agent] if seat == 0 else [opp.agent, me.agent]
                    env.run(pair)
                    c = census(env, seat)
                    m = sum(c[k] for k in MOVES)
                    mv += m
                    prod += sum(c.values()) - m
                    passes += c["PASS"]
                    r_me = env.steps[-1][seat].reward or 0
                    r_op = env.steps[-1][1 - seat].reward or 0
                    rewards.append(r_me)
                    games += 1
                    wins += 1 if r_me > r_op else 0
        # PASS is idling, not work -- counting it as productive flattered any
        # agent that stands still rather than walking to a marginal job.
        work = prod - passes
        ratio = mv / work if work else 0
        tot = mv + prod
        print(f"{os.path.basename(ap_):>22} {ratio:>8.2f} "
              f"{100*mv/tot:>6.1f}% {work:>8,} "
              f"{sum(rewards)/len(rewards):>10,.0f} {100*wins/games:>5.1f}%")


if __name__ == "__main__":
    main()
