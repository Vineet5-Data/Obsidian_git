import importlib.util, itertools
from kaggle_environments import make
_u = itertools.count()
def load(p):
    s = importlib.util.spec_from_file_location("m%d" % next(_u), p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

v6 = load("v6.py")
errs = []
orig = v6._adaptive_market
def traced(obs, action):
    try:
        return orig(obs, action)
    except Exception as e:
        errs.append(repr(e)); raise

v6._adaptive_market = traced
# also catch the agent-level swallow
fails = [0]
real_agent = v6.agent
def wrapped(obs):
    r = real_agent(obs)
    if r.get("farmer") == ["PASS"] and not r.get("market") and int(obs.get("step",0)) < 700:
        fails[0] += 1
    return r

env = make("kaggriculture", configuration={"seed": 1000})
env.run([wrapped, load("ref_top30.py").agent])
print("adaptive_market exceptions:", len(errs), errs[:3])
print("suspicious PASS steps:", fails[0])
st = env.steps
for day in (6, 10, 14, 18, 22, 26, 29):
    i = min(day*24+23, len(st)-1)
    o = st[i][0]["observation"]
    shed = {k: v for k, v in o["private"]["shed"].items() if v}
    print("d%-2d money=%-8.0f shed=%s" % (day, o["farms"][0]["money"], shed))
