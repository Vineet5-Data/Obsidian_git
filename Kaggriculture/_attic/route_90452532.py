"""Local counterfactual wrapper for player 0's episode-90452532 route."""

from pathlib import Path

from replay_opponent import make_replay_agent


agent = make_replay_agent(
    str(Path(__file__).resolve().with_name(".tmp_replay_90452532.json")), player=0
)
