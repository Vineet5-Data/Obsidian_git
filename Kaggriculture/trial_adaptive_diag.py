"""Summarize one candidate's observable trajectory against named fixtures."""

from __future__ import annotations

import argparse
import importlib.util
import json
from collections import Counter
from pathlib import Path

from kaggle_environments import make

import top_tournament


ROOT = Path(__file__).resolve().parent


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.agent


def assets(tiles) -> dict[str, int]:
    counts = Counter()
    for row in tiles or []:
        for tile in row or []:
            if not isinstance(tile, dict):
                continue
            if tile.get("kind") == "PLANT":
                counts[f"crop:{tile.get('crop')}"] += 1
            elif tile.get("animal"):
                counts[f"animal:{tile.get('animal')}"] += 1
            else:
                counts[f"kind:{tile.get('kind')}"] += 1
    return dict(counts)


def run(agent_path: Path, fixture: str, seat: int) -> dict:
    replay_id = fixture.rsplit("_", 1)[0]
    seed = top_tournament.replay_seed(replay_id)
    candidate = load(agent_path, f"candidate_{fixture}_{seat}")
    opponent = load(ROOT / ".top" / f"t_{fixture}.py", f"opponent_{fixture}_{seat}")
    pair = [candidate, opponent] if seat == 0 else [opponent, candidate]
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run(pair)

    field_ops = Counter()
    market_ops = Counter()
    purchases = Counter()
    snapshots = {}
    for turn, states in enumerate(env.steps):
        state = states[seat]
        action = state.get("action") or {}
        obs = state.get("observation") or {}
        farm = (obs.get("farms") or [{}, {}])[seat]
        rival = (obs.get("farms") or [{}, {}])[1 - seat]
        farmer = action.get("farmer") or ["NONE"]
        field_ops[f"farmer:{farmer[0]}"] += 1
        for hand in action.get("hands") or []:
            field_ops[f"hand:{(hand or ['NONE'])[0]}"] += 1
        for order in action.get("market") or []:
            if not order:
                continue
            market_ops[str(order[0])] += 1
            if order[0].startswith("BUY"):
                quantity = int(order[-1]) if isinstance(order[-1], int) else 1
                purchases[":".join(map(str, order[:2]))] += quantity
            elif order[0] == "HIRE":
                purchases["HIRE"] += 1
        if turn in (0, 120, 240, 360, 480, 600, 719):
            snapshots[str(turn)] = {
                "money": farm.get("money"),
                "quadrants": len(farm.get("unlocked_quadrants") or []),
                "hands": len(farm.get("hands") or []),
                "assets": assets(farm.get("tiles")),
                "shed": dict((obs.get("private") or {}).get("shed") or {}),
                "rival_money": rival.get("money"),
                "rival_quadrants": len(rival.get("unlocked_quadrants") or []),
                "rival_hands": len(rival.get("hands") or []),
                "rival_assets": assets(rival.get("tiles")),
            }

    final = env.steps[-1]
    return {
        "fixture": fixture,
        "seat": seat,
        "margin": final[seat].reward - final[1 - seat].reward,
        "ours": final[seat].reward,
        "opponent": final[1 - seat].reward,
        "snapshots": snapshots,
        "field_ops": dict(field_ops),
        "market_ops": dict(market_ops),
        "purchases": dict(purchases),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("agent")
    parser.add_argument("fixtures", nargs="+")
    parser.add_argument("--seat", type=int, choices=(0, 1), default=0)
    parser.add_argument("--json-out", type=Path, required=True)
    args = parser.parse_args()
    rows = [run((ROOT / args.agent).resolve(), fixture, args.seat)
            for fixture in args.fixtures]
    args.json_out.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    print(json.dumps(rows, indent=2))


if __name__ == "__main__":
    main()
