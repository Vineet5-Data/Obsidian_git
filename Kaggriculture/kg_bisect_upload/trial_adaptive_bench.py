"""Small recorded-seed benchmark for explicitly named extracted fixtures."""

from __future__ import annotations

import argparse
import json
import multiprocessing as mp
import statistics
from pathlib import Path

import _duel
import top_tournament


ROOT = Path(__file__).resolve().parent


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("agent")
    parser.add_argument("fixtures", nargs="+")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--json-out", type=Path, required=True)
    args = parser.parse_args()

    agent = str((ROOT / args.agent).resolve())
    jobs = []
    for fixture in args.fixtures:
        opponent = str((ROOT / ".top" / f"t_{fixture}.py").resolve())
        replay_id = fixture.rsplit("_", 1)[0]
        seed = top_tournament.replay_seed(replay_id)
        jobs.extend((agent, opponent, seed, seat) for seat in (0, 1))

    with mp.Pool(max(1, min(args.workers, len(jobs)))) as pool:
        rows = pool.map(_duel.one, jobs)

    details = {}
    margins = []
    for fixture, offset in zip(args.fixtures, range(0, len(rows), 2)):
        pair = [float(rows[offset][2]), float(rows[offset + 1][2])]
        margins.extend(pair)
        details[fixture] = {
            "wins": sum(value > 0 for value in pair),
            "losses": sum(value < 0 for value in pair),
            "mean_margin": statistics.mean(pair),
            "margins": pair,
        }

    report = {
        "agent": args.agent,
        "games": len(margins),
        "wins": sum(value > 0 for value in margins),
        "losses": sum(value < 0 for value in margins),
        "mean_margin": statistics.mean(margins),
        "median_margin": statistics.median(margins),
        "minimum_margin": min(margins),
        "details": details,
    }
    args.json_out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    mp.freeze_support()
    main()
