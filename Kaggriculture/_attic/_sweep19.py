import importlib.util, itertools
from kaggle_environments import make
from replay_opponent import make_replay_agent, replay_seed
_u = itertools.count()
def load(p, cfg=None):
    s = importlib.util.spec_from_file_location("m%d" % next(_u), p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    for k, v in (cfg or {}).items(): setattr(m, k, v)
    return m
RP = ".tmp_replay_90503598.json"; SEED = replay_seed(RP)
CFGS = [
    ("v13 baseline", "v13.py", {}),
    ("frontrun s0.05", "v17.py", dict(RESERVE={"STRAWBERRY": 0.05})),
    ("frontrun s+m 0.05", "v17.py", dict(RESERVE={"STRAWBERRY": 0.05, "MELON": 0.05})),
    ("frontrun s0.35", "v17.py", dict(RESERVE={"STRAWBERRY": 0.35, "MELON": 0.35})),
    ("frontrun s0.60", "v17.py", dict(RESERVE={"STRAWBERRY": 0.60, "MELON": 0.60})),
]
for name, path, cfg in CFGS:
    env = make("kaggriculture", configuration={"seed": int(SEED)})
    env.run([load(path, cfg).agent, make_replay_agent(RP, player=0)])
    f = env.steps[-1]; us, them = f[0]["reward"], f[1]["reward"]
    print("%-20s ours=$%-9.0f seb=$%-9.0f %s (%+.0f)" % (name, us, them, "WIN" if us > them else "loss", us-them), flush=True)
