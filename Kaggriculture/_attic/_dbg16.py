import importlib.util, itertools, traceback
from kaggle_environments import make
from replay_opponent import make_replay_agent
_u = itertools.count()
def load(p, cfg=None):
    s = importlib.util.spec_from_file_location("m%d" % next(_u), p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    for k, v in (cfg or {}).items(): setattr(m, k, v)
    return m

m = load("v16.py")
errs = []
real = m.agent
import copy as _c
def probe(obs):
    step = int(obs.get("step", 0) or 0)
    try:
        act = m._ACTIONS[min(step, len(m._ACTIONS)-1)]
        a = m._adapt_animals(obs, act)
        a = m._fill_idle_units(obs, a)
        a = m._terminal_liquidation(obs, m._aligned(a, obs))
    except Exception as e:
        if len(errs) < 3: errs.append(traceback.format_exc())
        raise
    return real(obs)

env = make("kaggriculture", configuration={"seed": 464721713})
env.run([probe, make_replay_agent(".tmp_replay_90503598.json", player=0)])
print("errors:", len(errs))
for e in errs[:2]: print(e)
# compare emitted vs recorded on early steps
st = env.steps
for i in (1, 5, 20, 60):
    emitted = st[i][0].get("action")
    rec = m._ACTIONS[i]
    print("step", i, "hands_expected", len(st[i][0]["observation"]["farms"][0].get("hands") or []),
          "rec_hands", len(rec["hands"]), "emitted", str(emitted)[:150])
