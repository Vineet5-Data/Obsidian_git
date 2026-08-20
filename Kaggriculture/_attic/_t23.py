import importlib.util, itertools
from kaggle_environments import make
from replay_opponent import make_replay_agent
_u = itertools.count()
def load(p, cfg=None):
    s = importlib.util.spec_from_file_location("m%d" % next(_u), p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    for k, v in (cfg or {}).items(): setattr(m, k, v)
    return m
for lead in (2, 4):
    env = make("kaggriculture", configuration={"seed": 1001})
    env.run([load("v23.py", dict(SELL_LEAD=lead)).agent, load("ref_top30.py").agent])
    f = env.steps[-1]
    print("v23 lead%d seed1001 vs ref: ours=$%.0f ref=$%.0f" % (lead, f[0]["reward"], f[1]["reward"]), flush=True)
    env = make("kaggriculture", configuration={"seed": 464721713})
    env.run([load("v23.py", dict(SELL_LEAD=lead)).agent, make_replay_agent(".tmp_replay_90503598.json", player=0)])
    f = env.steps[-1]
    print("v23 lead%d vs SEB:          ours=$%.0f seb=$%.0f" % (lead, f[0]["reward"], f[1]["reward"]), flush=True)
