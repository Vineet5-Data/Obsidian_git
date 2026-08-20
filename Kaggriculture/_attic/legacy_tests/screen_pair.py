"""Paired local screen between agent FILES on identical seeds and seats.

Same protocol as screen_v119_terminal.py, but the treatment is the agent file
rather than a constant.  The first --agents entry is the baseline every other
entry is paired against.  This is a screen, not the 1600-game promotion gate.

Usage:
  python screen_pair.py --agents a_v122_partial_horizon.py \
      a_v123_harvest_hold_value.py --opponents 20 --seeds 1
"""
from __future__ import annotations

import argparse
import glob
import importlib.util
import json
import multiprocessing as mp
import os
import statistics
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def load(path: str, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def play(job):
    agent_path, opponent_path, seed, seat = job
    from kaggle_environments import make

    tag = f"{Path(agent_path).stem}_{Path(opponent_path).stem}_{seed}_{seat}"
    candidate = load(agent_path, "candidate_" + tag)
    opponent = load(opponent_path, "opponent_" + tag)
    pair = ([candidate.agent, opponent.agent] if seat == 0
            else [opponent.agent, candidate.agent])
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run(pair)
    final = env.steps[-1]
    return (Path(agent_path).name, Path(opponent_path).stem, seed, seat,
            float(final[seat].reward - final[1 - seat].reward))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--agents", nargs="+", required=True)
    parser.add_argument("--seeds", type=int, default=1)
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--workers", type=int,
                        default=max(1, (os.cpu_count() or 4) - 2))
    parser.add_argument("--opponents", type=int, default=0)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    opponents = sorted(glob.glob(str(ROOT / ".top" / "t_*.py")))
    if args.opponents:
        # Spread the sample across the pool: adjacent t_*.py files are often
        # the two seats of one replay and play near-identically, so taking a
        # prefix over-samples a single cluster.  Seeds, not opponents, are the
        # real variance source here -- prefer more seeds over more opponents.
        stride = max(1, len(opponents) // args.opponents)
        opponents = opponents[::stride][:args.opponents]
    seeds = [(i * 2654435761) % 2147483647
             for i in range(args.offset + 1, args.offset + args.seeds + 1)]
    jobs = [(agent, opponent, seed, seat)
            for agent in args.agents for opponent in opponents
            for seed in seeds for seat in (0, 1)]
    print(f"{len(opponents)} opponents, {len(jobs)} games, "
          f"{args.workers} workers", flush=True)
    with mp.Pool(args.workers) as pool:
        rows = list(pool.imap_unordered(play, jobs, chunksize=1))
    if args.out:
        args.out.write_text(json.dumps(rows, indent=2), encoding="utf-8")

    names = [Path(a).name for a in args.agents]
    by_key = {(name, opponent, seed, seat): margin
              for name, opponent, seed, seat, margin in rows}
    baseline = names[0]
    for name in names:
        margins = [v for k, v in by_key.items() if k[0] == name]
        wins = sum(m > 0 for m in margins)
        ties = sum(m == 0 for m in margins)
        delta, flips_up, flips_down, same = [], 0, 0, 0
        for key, margin in [(k[1:], v) for k, v in by_key.items()
                            if k[0] == name]:
            old = by_key[(baseline, *key)]
            delta.append(margin - old)
            flips_up += old <= 0 < margin
            flips_down += old > 0 >= margin
            same += margin == old
        print(
            f"{name:34s} {wins}-{len(margins) - wins - ties}-{ties} "
            f"mean={statistics.mean(margins):+.1f} "
            f"median={statistics.median(margins):+.1f} "
            f"paired_delta_mean={statistics.mean(delta):+.1f} "
            f"paired_delta_median={statistics.median(delta):+.1f} "
            f"identical={same}/{len(delta)} flips=+{flips_up}/-{flips_down}"
        )
        if name == baseline:
            continue
        # Seeds are the variance source, not opponents: a screen run with one
        # or two seeds reports hundreds of "games" that are really one sample.
        # Print the per-seed split so that is impossible to miss.
        per_seed = {}
        for (opponent, seed, seat), margin in [(k[1:], v) for k, v in
                                               by_key.items() if k[0] == name]:
            per_seed.setdefault(seed, []).append(
                margin - by_key[(baseline, opponent, seed, seat)])
        agree = sum(1 for v in per_seed.values() if statistics.mean(v) > 0)
        print(f"{'':34s} per-seed paired delta over {len(per_seed)} seeds "
              f"({agree} positive): " + " ".join(
                  f"{statistics.mean(v):+.0f}"
                  for _, v in sorted(per_seed.items())))


if __name__ == "__main__":
    mp.freeze_support()
    main()
