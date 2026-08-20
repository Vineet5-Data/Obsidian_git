import importlib.util, itertools
from kaggle_environments import make
_u = itertools.count()
def load(p, cfg=None):
    s = importlib.util.spec_from_file_location("m%d" % next(_u), p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    for k, v in (cfg or {}).items(): setattr(m, k, v)
    return m
for lead in (0, 1, 2):
    env = make("kaggriculture", configuration={"seed": 1001})
    env.run([load("v21.py", dict(SELL_LEAD=lead)).agent, load("ref_top30.py").agent])
    f = env.steps[-1]
    print("v21 lead=%d on seed1001: ours=$%.0f ref=$%.0f" % (lead, f[0]["reward"], f[1]["reward"]), flush=True)
env = make("kaggriculture", configuration={"seed": 1001})
env.run([load("v16.py").agent, load("ref_top30.py").agent])
f = env.steps[-1]
print("v16 (no lead)     seed1001: ours=$%.0f ref=$%.0f" % (f[0]["reward"], f[1]["reward"]))
