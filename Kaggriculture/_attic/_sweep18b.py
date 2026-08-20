import importlib.util, itertools
from kaggle_environments import make
from replay_opponent import make_replay_agent
_u = itertools.count()
def load(p, cfg=None):
    s = importlib.util.spec_from_file_location("m%d" % next(_u), p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    for k, v in (cfg or {}).items(): setattr(m, k, v)
    return m
RP1 = ".tmp_replay_90503598.json"
CFGS = [("v13 base", "v13.py", {}),
        ("off",      "v18.py", dict(DAILY_CAP={})),
        ("s24_m12",  "v18.py", dict(DAILY_CAP={"STRAWBERRY":24,"MELON":12})),
        ("s20_m10",  "v18.py", dict(DAILY_CAP={"STRAWBERRY":20,"MELON":10})),
        ("s30",      "v18.py", dict(DAILY_CAP={"STRAWBERRY":30})),
        ("s24m12mi16", "v18.py", dict(DAILY_CAP={"STRAWBERRY":24,"MELON":12,"MILK":16}))]
for name, path, cfg in CFGS:
    env = make("kaggriculture", configuration={"seed": 464721713})
    env.run([load(path, cfg).agent, make_replay_agent(RP1, player=0)])
    f = env.steps[-1]; us, them = f[0]["reward"], f[1]["reward"]
    print("%-12s vs Seb-1: ours=$%-9.0f seb=$%-9.0f %s (%+.0f)" % (name, us, them, "WIN" if us > them else "loss", us-them), flush=True)
