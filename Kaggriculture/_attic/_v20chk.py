import importlib.util, itertools
from collections import Counter
from kaggle_environments import make
_u = itertools.count()
def load(p):
    s = importlib.util.spec_from_file_location("m%d" % next(_u), p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
v20 = load("v20.py")
crew_acts = Counter()
orig = v20._run_crew
def traced(obs, action):
    step = int(obs.get("step", 0) or 0)
    before = [list(o or ["PASS"]) for o in (action.get("hands") or [])]
    r = orig(obs, action)
    after = [list(o or ["PASS"]) for o in (r.get("hands") or [])]
    rh = v20._route_hand_count(step)
    for i in range(rh, max(len(before), len(after))):
        a = after[i] if i < len(after) else ["PASS"]
        if a[0] != "PASS":
            crew_acts[a[0]] += 1
    return r
v20._run_crew = traced
env = make("kaggriculture", configuration={"seed": 464721713})
env.run([v20.agent, load("seb_agent.py").agent])
st = env.steps
print("crew actions:", dict(crew_acts.most_common()))
print("day | money   quads animals pens empty hands routeH shedCOW")
for day in range(6, 30, 2):
    i = min(day*24+12, len(st)-1)
    o = st[i][0]["observation"]; f = o["farms"][0]
    an = pens = em = 0
    for row in f["tiles"]:
        for t in row:
            if t is None: em += 1
            elif isinstance(t, dict):
                if t.get("animal"): an += 1
                elif t.get("kind") == "PASTURE": pens += 1
    print("d%-2d | %-8.0f %d     %-7d %-4d %-5d %-5d %-6d %d" % (
        day, f["money"], len(f["unlocked_quadrants"]), an, pens, em,
        len(f["hands"] or []), v20._route_hand_count(i),
        int(o["private"]["shed"].get("COW", 0) or 0)))
print("final", st[-1][0]["reward"])
