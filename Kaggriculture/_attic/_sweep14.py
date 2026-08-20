import importlib.util, itertools
from kaggle_environments import make
from replay_opponent import make_replay_agent, replay_seed
_u = itertools.count()
def load(p, cfg=None):
    s = importlib.util.spec_from_file_location("m%d" % next(_u), p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    for k, v in (cfg or {}).items(): setattr(m, k, v)
    return m
RP = ".tmp_replay_90452532.json"; ESEED = replay_seed(RP)
M = [("elite", ESEED, lambda: make_replay_agent(RP, player=0)),
     ("ref1001", 1001, lambda: load("ref_top30.py").agent)]
for name, cfg in (("harvest0_fert0", dict(HARVEST_VALUE=0, FERT_VALUE=0)),
                  ("harvest60_fert0", dict(HARVEST_VALUE=60, FERT_VALUE=0)),
                  ("harvest0_fert90", dict(HARVEST_VALUE=0, FERT_VALUE=90)),
                  ("harvest60_fert90", dict(HARVEST_VALUE=60, FERT_VALUE=90))):
    tot = won = 0; out = []
    for label, seed, mk in M:
        env = make("kaggriculture", configuration={"seed": int(seed)})
        env.run([load("v14.py", cfg).agent, mk()])
        f = env.steps[-1]; us, them = f[0]["reward"], f[1]["reward"]
        tot += us; won += us > them
        out.append("%s %.0f/%.0f%s(+%.0f)" % (label, us, them, "W" if us > them else "L", us-them))
    print("%-17s wins=%d/2 mean=$%-9.0f | %s" % (name, won, tot/2, "  ".join(out)), flush=True)
