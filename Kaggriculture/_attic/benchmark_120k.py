"""Deterministic score gate for the Kaggriculture agent.

The benchmark uses both sides of the supplied elite replay, the reusable
``ref_top30.py`` route, and mirror play.  Every candidate is evaluated in both
seats where that is meaningful.  The process exits non-zero unless the
candidate's aggregate mean final money reaches ``--target``.

Usage:
    python benchmark_120k.py
    python benchmark_120k.py --agent main.py --seeds 1000 1001 1002 --target 120000
"""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import statistics
from pathlib import Path
from typing import Any, Callable

from kaggle_environments import make

from replay_opponent import make_replay_agent, replay_seed


ROOT = Path(__file__).resolve().parent
DEFAULT_REPLAY = ROOT / ".tmp_replay_90452532.json"
_MODULE_IDS = itertools.count()


def load_agent(path: Path) -> Callable[[Any], dict[str, Any]]:
    """Load a fresh agent module so module state cannot leak between games."""
    spec = importlib.util.spec_from_file_location(
        f"benchmark_candidate_{next(_MODULE_IDS)}", path
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load agent module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.agent


def play(
    agent0: Callable[[Any], dict[str, Any]],
    agent1: Callable[[Any], dict[str, Any]],
    seed: int,
) -> tuple[float, float, str, str]:
    env = make("kaggriculture", configuration={"seed": int(seed)})
    env.run([agent0, agent1])
    final = env.steps[-1]
    return (
        float(final[0]["reward"] or 0.0),
        float(final[1]["reward"] or 0.0),
        str(final[0]["status"]),
        str(final[1]["status"]),
    )


def add_match(
    rows: list[dict[str, Any]],
    label: str,
    our_seat: int,
    seed: int,
    ours: Callable[[Any], dict[str, Any]],
    opponent: Callable[[Any], dict[str, Any]],
) -> None:
    pair = (ours, opponent) if our_seat == 0 else (opponent, ours)
    score0, score1, status0, status1 = play(*pair, seed)
    scores = (score0, score1)
    statuses = (status0, status1)
    rows.append(
        {
            "opponent": label,
            "seat": our_seat,
            "seed": seed,
            "money": scores[our_seat],
            "opponent_money": scores[1 - our_seat],
            "status": statuses[our_seat],
            "opponent_status": statuses[1 - our_seat],
        }
    )


def summarize(rows: list[dict[str, Any]], target: float) -> dict[str, Any]:
    values = [float(row["money"]) for row in rows]
    opponent_values = [float(row["opponent_money"]) for row in rows]
    return {
        "games": len(rows),
        "mean": statistics.mean(values),
        "median": statistics.median(values),
        "minimum": min(values),
        "maximum": max(values),
        "stdev": statistics.pstdev(values),
        "opponent_mean": statistics.mean(opponent_values),
        "wins": sum(a > b for a, b in zip(values, opponent_values)),
        "target": target,
        "passed": statistics.mean(values) >= target,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent", type=Path, default=ROOT / "main.py")
    parser.add_argument("--replay", type=Path, default=DEFAULT_REPLAY)
    parser.add_argument("--reference", type=Path, default=ROOT / "ref_top30.py")
    parser.add_argument("--seeds", type=int, nargs="+", default=[1000, 1001, 1002])
    parser.add_argument("--target", type=float, default=120_000.0)
    parser.add_argument(
        "--suite",
        choices=("all", "replay", "reference", "mirror"),
        default="all",
    )
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    agent_path = args.agent.resolve()
    replay_path = args.replay.resolve()
    reference_path = args.reference.resolve()
    rows: list[dict[str, Any]] = []

    if args.suite in ("all", "replay"):
        if not replay_path.exists():
            raise FileNotFoundError(f"elite replay not found: {replay_path}")
        elite_seed = replay_seed(str(replay_path))
        if elite_seed is None:
            raise RuntimeError("elite replay does not contain info.seed")
        for replay_player in (0, 1):
            for seat in (0, 1):
                add_match(
                    rows,
                    f"elite_replay_p{replay_player}",
                    seat,
                    elite_seed,
                    load_agent(agent_path),
                    make_replay_agent(str(replay_path), player=replay_player),
                )

    if args.suite in ("all", "reference"):
        for seed in args.seeds:
            for seat in (0, 1):
                add_match(
                    rows,
                    "ref_top30",
                    seat,
                    seed,
                    load_agent(agent_path),
                    load_agent(reference_path),
                )

    if args.suite in ("all", "mirror"):
        for seed in args.seeds:
            score0, score1, status0, status1 = play(
                load_agent(agent_path), load_agent(agent_path), seed
            )
            for seat, money, opponent_money, status, opponent_status in (
                (0, score0, score1, status0, status1),
                (1, score1, score0, status1, status0),
            ):
                rows.append(
                    {
                        "opponent": "mirror",
                        "seat": seat,
                        "seed": seed,
                        "money": money,
                        "opponent_money": opponent_money,
                        "status": status,
                        "opponent_status": opponent_status,
                    }
                )

    summary = summarize(rows, args.target)
    report = {"summary": summary, "rows": rows}
    if args.as_json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        for row in rows:
            print(
                "{opponent:<18} seat={seat} seed={seed:<10} "
                "money=${money:>9.0f} opponent=${opponent_money:>9.0f} "
                "status={status}/{opponent_status}".format(**row)
            )
        print(
            "SUMMARY games={games} mean=${mean:,.1f} median=${median:,.1f} "
            "min=${minimum:,.0f} max=${maximum:,.0f} stdev=${stdev:,.1f} "
            "opponent_mean=${opponent_mean:,.1f} wins={wins} "
            "target=${target:,.0f} passed={passed}".format(**summary)
        )
    return 0 if summary["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
