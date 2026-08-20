import importlib.util, itertools
from collections import Counter
from kaggle_environments import make
_u = itertools.count()
def load(p):
    s = importlib.util.spec_from_file_location("m%d" % next(_u), p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
env = make("kaggriculture", configuration={"seed": 1001})
env.run([load("v7a.py").agent, load("ref_top30.py").agent])
st = env.steps
dry = Counter(); allc = Counter()
for day in range(30):
    o = st[min(day*24+23, len(st)-1)][0]["observation"]
    for row in o["farms"][0]["tiles"]:
        for t in row:
            if isinstance(t, dict) and t.get("kind") == "PLANT" and t.get("crop"):
                allc[t["crop"]] += 1
                if not t.get("watered_today"): dry[t["crop"]] += 1
print("crop-days total vs unwatered:")
for c in allc: print("  %-11s total=%-5d dry=%-5d (%.0f%%)" % (c, allc[c], dry[c], 100.0*dry[c]/allc[c]))
