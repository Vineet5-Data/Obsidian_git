"""Full opponent set incl. Seb, both seats."""
import importlib.util, itertools, sys
from kaggle_environments import make
from replay_opponent import make_replay_agent, replay_seed
_u = itertools.count()
def load(p, cfg=None):
    s = importlib.util.spec_from_file_location("m%d" % next(_u), p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    for k, v in (cfg or {}).items(): setattr(m, k, v)
    return m
ELITE = ".tmp_replay_90452532.json"; SEB = ".tmp_replay_90503598.json"
MATCHES = [
    ("seb",       replay_seed(SEB),   lambda: make_replay_agent(SEB, player=0)),
    ("elite_p0",  replay_seed(ELITE), lambda: make_replay_agent(ELITE, player=0)),
    ("elite_p1",  replay_seed(ELITE), lambda: make_replay_agent(ELITE, player=1)),
    ("ref_s1000", 1000, lambda: load("ref_top30.py").agent),
    ("ref_s1001", 1001, lambda: load("ref_top30.py").agent),
]
def run(label, path, cfg):
    won = 0; tot = 0.0; out = []
    for name, seed, mk in MATCHES:
        for seat in (0, 1):
            ours, opp = load(path, cfg).agent, mk()
            pair = (ours, opp) if seat == 0 else (opp, ours)
            env = make("kaggriculture", configuration={"seed": int(seed)})
            env.run(list(pair)); f = env.steps[-1]
            us, them = f[seat]["reward"], f[1-seat]["reward"]
            won += us > them; tot += us
            out.append("%s/s%d %.0f/%.0f%s" % (name, seat, us, them, "W" if us > them else "L"))
    print("%-16s wins=%2d/10 mean=$%-9.0f | %s" % (label, won, tot/10, "  ".join(out)), flush=True)

import sys
CANDS = [("v23 lead2", "v23.py", dict(SELL_LEAD=2)),
         ("v23 lead4", "v23.py", dict(SELL_LEAD=4)),
         ("v23 lead0", "v23.py", dict(SELL_LEAD=0))]
for label, path, cfg in CANDS:
    run(label, path, cfg)
