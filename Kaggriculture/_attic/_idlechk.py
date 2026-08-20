import importlib.util, itertools
from collections import Counter
from kaggle_environments import make
_u = itertools.count()
def load(p):
    s = importlib.util.spec_from_file_location("m%d" % next(_u), p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

v9 = load("v9.py")
stats = Counter()
orig_task = v9._idle_task
orig_fill = v9._fill_idle_units
def fill(obs, action):
    farm, _ = v9._farm_private(obs)
    n_pass = sum(1 for o in [action.get("farmer")] + list(action.get("hands") or []) if not o or o[0] == "PASS")
    stats["pass_slots"] += n_pass
    # what are idle units standing on?
    pos = [v9._get(farm, "farmer", None)] + list(v9._get(farm, "hands", []) or [])
    orders = [action.get("farmer") or ["PASS"]] + [list(o or ["PASS"]) for o in (action.get("hands") or [])]
    for p, o in zip(pos, orders):
        if o and o[0] != "PASS": continue
        t = v9._tile_at(farm, p)
        if not isinstance(t, dict): stats["idle_on_" + (str(t) if t else "empty")] += 1
        else: stats["idle_on_" + str(t.get("kind"))] += 1
    r = orig_fill(obs, action)
    subs = sum(1 for o in [r.get("farmer")] + list(r.get("hands") or []) if o and o[0] in ("CARE", "WATER"))
    stats["after_care_or_water"] += subs
    return r
v9._fill_idle_units = fill
env = make("kaggriculture", configuration={"seed": 1001})
env.run([v9.agent, load("ref_top30.py").agent])
for k, v in stats.most_common(): print("%-26s %d" % (k, v))
