"""Seb's episode-90503598 route as a plain agent module (for harnesses)."""
from pathlib import Path
from replay_opponent import make_replay_agent

agent = make_replay_agent(str(Path(__file__).resolve().with_name(".tmp_replay_90503598.json")), player=0)
