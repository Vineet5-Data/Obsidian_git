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
for name, cfg in (("baseline", {}),
                  ("buy700", dict(WHEAT_BUY_CAP=700)),
                  ("buy500", dict(WHEAT_BUY_CAP=500)),
                  ("buy372", dict(WHEAT_BUY_CAP=372)),
                  ("nosell", dict(WHEAT_SELL_CAP=70)),
                  ("buy500_nosell", dict(WHEAT_BUY_CAP=500, WHEAT_SELL_CAP=70))):
    env = make("kaggriculture", configuration={"seed": int(SEED)})
    env.run([load("v15.py", cfg).agent, make_replay_agent(RP, player=0)])
    f = env.steps[-1]; us, them = f[0]["reward"], f[1]["reward"]
    print("%-15s ours=$%-9.0f seb=$%-9.0f %s (%+.0f)" % (name, us, them, "WIN" if us > them else "loss", us-them), flush=True)
