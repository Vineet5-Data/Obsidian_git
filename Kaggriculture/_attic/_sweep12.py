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
for cap in (14, 12, 11, 10, 9):
    tot = won = 0; out = []
    for label, seed, mk in M:
        env = make("kaggriculture", configuration={"seed": int(seed)})
        env.run([load("v12.py", dict(MAX_HANDS=cap)).agent, mk()])
        f = env.steps[-1]; us, them = f[0]["reward"], f[1]["reward"]
        tot += us; won += us > them
        out.append("%s %.0f/%.0f%s" % (label, us, them, "W" if us > them else "L"))
    print("MAX_HANDS=%-3d wins=%d/2 mean=$%-9.0f | %s" % (cap, won, tot/2, "  ".join(out)), flush=True)
