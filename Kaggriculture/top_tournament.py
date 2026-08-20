"""Both-seat tournament against every extracted Top_players player.

The extracted ``.top`` modules are test fixtures only. Candidate agents are
loaded from their own file and must not import, decode, fingerprint, or copy
these fixtures.
"""

from __future__ import annotations

import argparse
import glob
import json
import multiprocessing as mp
import os
import statistics
from pathlib import Path

import _duel


ROOT = Path(__file__).resolve().parent
TOP_DIR = ROOT / ".top"
REPLAY_DIR = ROOT / "Top_players"


def replay_seed(replay_id: str) -> int:
    data = json.loads((REPLAY_DIR / f"{replay_id}.json").read_text(encoding="utf-8"))
    return int((data.get("info") or {}).get("seed", 0))


def opponents() -> list[str]:
    return sorted(glob.glob(str(TOP_DIR / "t_*.py")))


def label(path: str) -> str:
    return Path(path).stem.removeprefix("t_")


def jobs(agent: str, mode: str, n: int) -> list[tuple[str, str, int, int]]:
    result = []
    random_seeds = [(index * 2654435761) % 2147483647 for index in range(1, n + 1)]
    for opponent in opponents():
        replay_id = label(opponent).rsplit("_", 1)[0]
        seeds = [replay_seed(replay_id)] if mode == "recorded" else random_seeds
        for seed in seeds:
            for seat in (0, 1):
                result.append((agent, opponent, seed, seat))
    return result


def summarize(agent: str, work: list[tuple[str, str, int, int]], rows: list[tuple[int, int, float]]) -> dict:
    per_opponent: dict[str, list[float]] = {}
    all_margins = []
    for job, row in zip(work, rows):
        opponent = label(job[1])
        margin = float(row[2])
        per_opponent.setdefault(opponent, []).append(margin)
        all_margins.append(margin)
    details = {}
    for opponent, margins in sorted(per_opponent.items()):
        details[opponent] = {
            "wins": sum(value > 0 for value in margins),
            "losses": sum(value < 0 for value in margins),
            "ties": sum(value == 0 for value in margins),
            "mean_margin": statistics.mean(margins),
            "minimum_margin": min(margins),
            "margins": margins,
        }
    wins = sum(value > 0 for value in all_margins)
    losses = sum(value < 0 for value in all_margins)
    return {
        "agent": agent,
        "games": len(all_margins),
        "opponents": len(details),
        "wins": wins,
        "losses": losses,
        "ties": len(all_margins) - wins - losses,
        "win_rate": wins / max(1, len(all_margins)),
        "mean_margin": statistics.mean(all_margins),
        "median_margin": statistics.median(all_margins),
        "minimum_margin": min(all_margins),
        "maximum_margin": max(all_margins),
        "unbeaten_opponents": sum(item["losses"] == 0 for item in details.values()),
        "details": details,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("agent")
    parser.add_argument("--mode", choices=("recorded", "random"), default="recorded")
    parser.add_argument("--seeds", type=int, default=1, help="random-mode seed count")
    parser.add_argument("--workers", type=int, default=max(1, (os.cpu_count() or 4) - 2))
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()

    work = jobs(str(Path(args.agent).resolve()), args.mode, max(1, args.seeds))
    with mp.Pool(args.workers) as pool:
        rows = pool.map(_duel.one, work)
    report = summarize(args.agent, work, rows)
    if args.json_out:
        args.json_out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    compact = {key: value for key, value in report.items() if key != "details"}
    compact["losing_opponents"] = [
        name for name, item in report["details"].items() if item["losses"] > 0
    ]
    print(json.dumps(compact, indent=2))


if __name__ == "__main__":
    mp.freeze_support()
    main()
