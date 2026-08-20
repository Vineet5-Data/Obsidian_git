import importlib.util, itertools, json
from kaggle_environments import make
from replay_opponent import make_replay_agent
_u = itertools.count()
def load(p):
    s = importlib.util.spec_from_file_location("m%d" % next(_u), p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
RP = ".tmp_replay_90503598.json"
m = load("v16.py")
ref = make_replay_agent(RP, player=0)
diffs = []
def probe(obs):
    step = min(max(0, int(obs.get("step", 0) or 0)), len(m._ACTIONS) - 1)
    mine = m._aligned(m._ACTIONS[step], obs)
    theirs = ref(obs)
    if mine != theirs and len(diffs) < 5:
        diffs.append((step, json.dumps(mine)[:220], json.dumps(theirs)[:220]))
    return theirs          # follow the reference so the run stays on-route
env = make("kaggriculture", configuration={"seed": 464721713})
env.run([probe, make_replay_agent(RP, player=0)])
print("divergences:", len(diffs))
for s, a, b in diffs:
    print("step", s); print("  aligned:", a); print("  replay :", b)
