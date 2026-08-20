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
for name, cfg in (("off", dict(RESERVE={})),
                  ("s0.9_m0.6", dict(RESERVE={"STRAWBERRY":0.9,"MELON":0.6})),
                  ("s1.05_m0.7", dict(RESERVE={"STRAWBERRY":1.05,"MELON":0.7})),
                  ("s1.25_m0.85", dict(RESERVE={"STRAWBERRY":1.25,"MELON":0.85})),
                  ("s1.05_only", dict(RESERVE={"STRAWBERRY":1.05})),
                  ("m0.7_only", dict(RESERVE={"MELON":0.7}))):
    env = make("kaggriculture", configuration={"seed": int(SEED)})
    env.run([load("v17.py", cfg).agent, make_replay_agent(RP, player=0)])
    f = env.steps[-1]; us, them = f[0]["reward"], f[1]["reward"]
    print("%-14s ours=$%-9.0f seb=$%-9.0f %s (%+.0f)" % (name, us, them, "WIN" if us > them else "loss", us-them), flush=True)
