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
for name, cfg in (("off", dict(DAILY_CAP={})),
                  ("s20_m8", {}),
                  ("s16_m6", dict(DAILY_CAP={"STRAWBERRY":16,"MELON":6})),
                  ("s24_m10", dict(DAILY_CAP={"STRAWBERRY":24,"MELON":10})),
                  ("s20only", dict(DAILY_CAP={"STRAWBERRY":20})),
                  ("s30_m12", dict(DAILY_CAP={"STRAWBERRY":30,"MELON":12}))):
    env = make("kaggriculture", configuration={"seed": int(SEED)})
    env.run([load("v18.py", cfg).agent, make_replay_agent(RP, player=0)])
    f = env.steps[-1]; us, them = f[0]["reward"], f[1]["reward"]
    print("%-10s ours=$%-9.0f seb=$%-9.0f %s (%+.0f)" % (name, us, them, "WIN" if us > them else "loss", us-them), flush=True)
