"""Seb's route as recorded in episode 90473753 (p1, $136,063 on seed 1250560110)."""
from pathlib import Path
from replay_opponent import make_replay_agent

agent = make_replay_agent(str(Path(__file__).resolve().with_name(".tmp_replay_90473753.json")), player=1)
