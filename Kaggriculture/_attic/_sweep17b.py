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
    ("v13 base",      "v13.py", {}),
    ("off",           "v17.py", dict(RESERVE={})),
    ("milk+wool.75",  "v17.py", dict(RESERVE={"MILK":0.75,"WOOL":0.75})),
    ("m/w/mel .75",   "v17.py", dict(RESERVE={"MILK":0.75,"WOOL":0.75,"MELON":0.75})),
    ("all4 .75",      "v17.py", dict(RESERVE={"MILK":0.75,"WOOL":0.75,"MELON":0.75,"STRAWBERRY":0.75})),
    ("all4 1.00",     "v17.py", dict(RESERVE={"MILK":1.0,"WOOL":1.0,"MELON":1.0,"STRAWBERRY":1.0})),
]
for name, path, cfg in CFGS:
    env = make("kaggriculture", configuration={"seed": int(SEED)})
    env.run([load(path, cfg).agent, make_replay_agent(RP, player=0)])
    f = env.steps[-1]; us, them = f[0]["reward"], f[1]["reward"]
    print("%-14s ours=$%-9.0f seb=$%-9.0f %s (%+.0f)" % (name, us, them, "WIN" if us > them else "loss", us-them), flush=True)
