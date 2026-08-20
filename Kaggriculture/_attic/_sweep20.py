import importlib.util, itertools, sys
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
    ("v13 base",        "v13.py", {}),
    ("d13 r15k a20 h2", "v20.py", dict(EXTRA_FROM_DAY=13, EXTRA_CASH_RESERVE=15000, EXTRA_MAX_ANIMALS=20, EXTRA_HANDS=2)),
    ("d13 r15k a20 h1", "v20.py", dict(EXTRA_FROM_DAY=13, EXTRA_CASH_RESERVE=15000, EXTRA_MAX_ANIMALS=20, EXTRA_HANDS=1)),
    ("d15 r25k a24 h2", "v20.py", dict(EXTRA_FROM_DAY=15, EXTRA_CASH_RESERVE=25000, EXTRA_MAX_ANIMALS=24, EXTRA_HANDS=2)),
    ("d11 r10k a20 h2", "v20.py", dict(EXTRA_FROM_DAY=11, EXTRA_CASH_RESERVE=10000, EXTRA_MAX_ANIMALS=20, EXTRA_HANDS=2)),
    ("d13 r15k a30 h3", "v20.py", dict(EXTRA_FROM_DAY=13, EXTRA_CASH_RESERVE=15000, EXTRA_MAX_ANIMALS=30, EXTRA_HANDS=3)),
]
for name, path, cfg in CFGS:
    env = make("kaggriculture", configuration={"seed": int(SEED)})
    env.run([load(path, cfg).agent, make_replay_agent(RP, player=0)])
    f = env.steps[-1]; us, them = f[0]["reward"], f[1]["reward"]
    print("%-18s ours=$%-9.0f seb=$%-9.0f %s (%+.0f)" % (name, us, them, "WIN" if us > them else "loss", us-them), flush=True)
