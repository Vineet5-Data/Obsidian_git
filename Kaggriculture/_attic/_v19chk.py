import importlib.util, itertools
from collections import Counter
from kaggle_environments import make
_u = itertools.count()
def load(p):
    s = importlib.util.spec_from_file_location("m%d" % next(_u), p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
env = make("kaggriculture", configuration={"seed": 464721713})
env.run([load("v19.py").agent, load("seb_agent.py").agent])
st = env.steps
print("day | money   quads animals free_past empty shedCOW starving")
for day in range(6, 30, 2):
    o = st[min(day*24+23, len(st)-1)][0]["observation"]
    f = o["farms"][0]
    an = fp = em = starve = 0
    for row in f["tiles"]:
        for t in row:
            if t is None: em += 1
            elif isinstance(t, dict):
                if t.get("animal"):
                    an += 1
                    if int(t.get("consecutive_unfed", 0) or 0) > 0: starve += 1
                elif t.get("kind") == "PASTURE": fp += 1
    print("d%-2d | %-8.0f %d     %-7d %-9d %-5d %-7d %d" % (
        day, f["money"], len(f["unlocked_quadrants"]), an, fp, em,
        int(o["private"]["shed"].get("COW", 0) or 0), starve))
print("final", st[-1][0]["reward"])
