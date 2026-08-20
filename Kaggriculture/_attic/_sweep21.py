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
for lead in (0, 1, 2, 4, 8):
    env = make("kaggriculture", configuration={"seed": int(SEED)})
    env.run([load("v21.py", dict(SELL_LEAD=lead)).agent, make_replay_agent(RP, player=0)])
    f = env.steps[-1]; us, them = f[0]["reward"], f[1]["reward"]
    print("SELL_LEAD=%-2d ours=$%-9.0f seb=$%-9.0f %s (%+.0f)" % (lead, us, them, "WIN" if us > them else "loss", us-them), flush=True)
