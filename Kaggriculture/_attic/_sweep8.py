import importlib.util, itertools, sys
from kaggle_environments import make
from replay_opponent import make_replay_agent, replay_seed
_u = itertools.count()
def load(p, cfg=None):
    s = importlib.util.spec_from_file_location("m%d" % next(_u), p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    for k, v in (cfg or {}).items(): setattr(m, k, v)
    return m
RP = ".tmp_replay_90452532.json"; ESEED = replay_seed(RP)
MATCHES = [("elite_p0", ESEED, lambda: make_replay_agent(RP, player=0)),
           ("ref_s1001", 1001, lambda: load("ref_top30.py").agent),
           ("ref_s1000", 1000, lambda: load("ref_top30.py").agent)]
for lead in (0, 2, 6, 14):
    tot = won = 0; out = []
    for label, seed, mk in MATCHES:
        ours, opp = load("v8.py", dict(LIQ_LEAD=lead)).agent, mk()
        env = make("kaggriculture", configuration={"seed": int(seed)})
        env.run([ours, opp]); f = env.steps[-1]
        us, them = f[0]["reward"], f[1]["reward"]
        tot += us; won += us > them
        out.append("%s %.0f/%.0f%s" % (label, us, them, "W" if us > them else "L"))
    print("LIQ_LEAD=%-3d wins=%d/3 mean=$%-9.0f | %s" % (lead, won, tot/3, "  ".join(out)), flush=True)
