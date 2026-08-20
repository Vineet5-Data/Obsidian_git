import importlib.util, itertools
from kaggle_environments import make
from replay_opponent import make_replay_agent
_u = itertools.count()
def load(p, cfg=None):
    s = importlib.util.spec_from_file_location("m%d" % next(_u), p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    for k, v in (cfg or {}).items(): setattr(m, k, v)
    return m
RP = ".tmp_replay_90503598.json"

def run(label, make_agent):
    env = make("kaggriculture", configuration={"seed": 464721713})
    env.run([make_agent(), make_replay_agent(RP, player=0)])
    f = env.steps[-1]
    print("%-22s ours=$%-9.0f seb=$%-9.0f" % (label, f[0]["reward"], f[1]["reward"]), flush=True)

run("raw replay agent", lambda: make_replay_agent(RP, player=0))

m0 = load("v16.py")
def pure():
    def a(obs):
        step = min(max(0, int(obs.get("step", 0) or 0)), len(m0._ACTIONS)-1)
        return m0._aligned(m0._ACTIONS[step], obs)
    return a
run("aligned only", pure)

m1 = load("v16.py")
def align_animals():
    def a(obs):
        step = min(max(0, int(obs.get("step", 0) or 0)), len(m1._ACTIONS)-1)
        return m1._adapt_animals(obs, m1._ACTIONS[step])
    return a
run("+_adapt_animals", align_animals)

run("+idle (IDLE_WORK=1)", lambda: load("v16.py", dict(IDLE_WORK=1)).agent)
run("-idle (IDLE_WORK=0)", lambda: load("v16.py", dict(IDLE_WORK=0)).agent)
