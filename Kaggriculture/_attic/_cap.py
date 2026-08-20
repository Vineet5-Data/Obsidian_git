import importlib.util, itertools
from collections import Counter
from kaggle_environments import make
_u = itertools.count()
def load(p):
    s = importlib.util.spec_from_file_location("m%d" % next(_u), p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
env = make("kaggriculture", configuration={"seed": 464721713})
env.run([load("v13.py").agent, load("seb_agent.py").agent])
st = env.steps
print("day |  our money | empty | pasture_free | animals | quads || seb money  animals quads")
for day in range(0, 30, 2):
    o = st[min(day*24+23, len(st)-1)][0]["observation"]
    row = []
    for k in (0, 1):
        c = Counter()
        for r in o["farms"][k]["tiles"]:
            for t in r:
                if t is None: c["empty"] += 1
                elif t == "LOCKED": c["lock"] += 1
                elif isinstance(t, dict):
                    if t.get("animal"): c["animal"] += 1
                    elif t.get("kind") == "PASTURE": c["free_pasture"] += 1
        row.append((o["farms"][k]["money"], c["empty"], c["free_pasture"], c["animal"],
                    len(o["farms"][k]["unlocked_quadrants"])))
    a, b = row
    print("d%-2d | $%9.0f | %5d | %12d | %7d | %5d || $%9.0f %7d %5d"
          % (day, a[0], a[1], a[2], a[3], a[4], b[0], b[3], b[4]))
