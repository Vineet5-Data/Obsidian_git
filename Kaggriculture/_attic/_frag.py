import importlib.util, itertools
from kaggle_environments import make
_u = itertools.count()
def load(p):
    s = importlib.util.spec_from_file_location("m%d" % next(_u), p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
m = load("v16.py")
for seed in (464721713, 1001):
    env = make("kaggriculture", configuration={"seed": seed})
    env.run([load("v16.py").agent, load("ref_top30.py").agent])
    st = env.steps
    print("=== seed", seed, "final", st[-1][0]["reward"])
    print("  day money    hands routeH animals quads")
    for day in range(0, 22, 2):
        i = min(day*24+12, len(st)-1)
        o = st[i][0]["observation"]; f = o["farms"][0]
        an = sum(1 for r in f["tiles"] for t in r if isinstance(t, dict) and t.get("animal"))
        print("  d%-2d %-8.0f %-5d %-6d %-7d %d" % (day, f["money"], len(f["hands"] or []),
              m._route_hand_count(i) if hasattr(m, "_route_hand_count") else len(m._ACTIONS[i].get("hands") or []),
              an, len(f["unlocked_quadrants"])))
