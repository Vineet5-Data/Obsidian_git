import importlib.util, itertools
from collections import defaultdict
from kaggle_environments import make
_u = itertools.count()
def load(p):
    s = importlib.util.spec_from_file_location("m%d" % next(_u), p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
env = make("kaggriculture", configuration={"seed": 464721713})
env.run([load("v13.py").agent, load("seb_agent.py").agent])
st = env.steps
for item in ("STRAWBERRY", "MELON"):
    print("=====", item)
    for k, nm in ((0, "v13"), (1, "seb")):
        agg = defaultdict(lambda: [0, 0])
        first = None
        for i, s in enumerate(st):
            a = s[k].get("action")
            if not isinstance(a, dict): continue
            for mo in (a.get("market") or []):
                if mo and mo[0] == "SELL" and mo[1] == item:
                    d = i // 24
                    if first is None: first = d
                    agg[d][0] += mo[2]
                    agg[d][1] = st[i][k]["observation"]["market"]["prices"][item]
        print("  %-4s first_day=%s  %s" % (nm, first,
              " ".join("d%d:%dq@$%d" % (d, v[0], v[1]) for d, v in sorted(agg.items()))))
