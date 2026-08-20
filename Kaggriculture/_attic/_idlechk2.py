import importlib.util, itertools, copy
from collections import Counter
from kaggle_environments import make
_u = itertools.count()
def load(p):
    s = importlib.util.spec_from_file_location("m%d" % next(_u), p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

import sys
v9 = load(sys.argv[1] if len(sys.argv)>1 else "v9.py")
stats = Counter()
orig = v9._fill_idle_units
def fill(obs, action):
    before = copy.deepcopy(action)
    r = orig(obs, action)
    b = [before.get("farmer")] + list(before.get("hands") or [])
    a = [r.get("farmer")] + list(r.get("hands") or [])
    for x, y in zip(b, a):
        if (x or ["PASS"])[0] == "PASS" and (y or ["PASS"])[0] != "PASS":
            stats["SUB_" + y[0]] += 1
    return r
v9._fill_idle_units = fill
env = make("kaggriculture", configuration={"seed": int(sys.argv[3]) if len(sys.argv)>3 else 1001})
env.run([v9.agent, load(sys.argv[2] if len(sys.argv)>2 else "ref_top30.py").agent])
print("substitutions:", dict(stats))
print("final money:", env.steps[-1][0]["reward"], "opp", env.steps[-1][1]["reward"])
