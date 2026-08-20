"""Paired screen for v119's terminal-liquidation boundary."""

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
DEFAULT_AGENT = Path(r"C:\Users\Vinee\Downloads\a_v119_midgame_fertilizer_collect.py")


def load(path: str, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def play(job):
    dump_step, agent_path, opponent_path, seed, seat = job
    from kaggle_environments import make

    tag = f"{dump_step}_{Path(opponent_path).stem}_{seed}_{seat}"
    candidate = load(agent_path, "candidate_" + tag)
    opponent = load(opponent_path, "opponent_" + tag)
    candidate.DUMP_STEP = dump_step
    pair = ([candidate.agent, opponent.agent] if seat == 0
            else [opponent.agent, candidate.agent])
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run(pair)
    final = env.steps[-1]
    return dump_step, Path(opponent_path).stem, seed, seat, float(
        final[seat].reward - final[1 - seat].reward)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent", type=Path, default=DEFAULT_AGENT)
    parser.add_argument("--steps", type=int, nargs="+", default=[624, 648, 672, 696])
    parser.add_argument("--seeds", type=int, default=1)
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--workers", type=int, default=max(1, (os.cpu_count() or 4) - 2))
    parser.add_argument('--opponents', type=int, default=0)
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()

    opponents = sorted(glob.glob(str(ROOT / ".top" / "t_*.py")))
    if args.opponents:
        opponents = opponents[:args.opponents]
    seeds = [(i * 2654435761) % 2147483647
             for i in range(args.offset + 1, args.offset + args.seeds + 1)]
    jobs = [(step, str(args.agent), opponent, seed, seat)
            for step in args.steps for opponent in opponents
            for seed in seeds for seat in (0, 1)]
    print(f"{len(opponents)} opponents, {len(jobs)} games, {args.workers} workers", flush=True)
    with mp.Pool(args.workers) as pool:
        rows = list(pool.imap_unordered(play, jobs, chunksize=1))
    if args.out:
        args.out.write_text(json.dumps(rows, indent=2), encoding='utf-8')

    by_step = {step: [] for step in args.steps}
    by_key = {}
    for step, opponent, seed, seat, margin in rows:
        by_step[step].append(margin)
        by_key[step, opponent, seed, seat] = margin
    baseline = 648
    for step in args.steps:
        margins = by_step[step]
        wins = sum(m > 0 for m in margins)
        ties = sum(m == 0 for m in margins)
        delta = []
        flips_up = flips_down = 0
        if baseline in by_step:
            for key, margin in [(k[1:], v) for k, v in by_key.items() if k[0] == step]:
                old = by_key[baseline, *key]
                delta.append(margin - old)
                flips_up += old <= 0 < margin
                flips_down += old > 0 >= margin
        print(
            f"DUMP_STEP={step}: {wins}-{len(margins) - wins - ties}-{ties} "
            f"mean={statistics.mean(margins):+.1f} median={statistics.median(margins):+.1f} "
            f"paired_delta={statistics.mean(delta):+.1f} flips=+{flips_up}/-{flips_down}"
        )


if __name__ == "__main__":
    mp.freeze_support()
    main()
