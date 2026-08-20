"""Compare agent files across the matchups we lose. Usage: _cmp.py a.py b.py ..."""
import importlib.util, itertools, sys
from kaggle_environments import make
from replay_opponent import make_replay_agent, replay_seed
_u = itertools.count()

def load(p):
    s = importlib.util.spec_from_file_location("m%d" % next(_u), p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

RP = ".tmp_replay_90452532.json"
ESEED = replay_seed(RP)
MATCHES = [
    ("elite_p0", ESEED, lambda: make_replay_agent(RP, player=0)),
    ("elite_p1", ESEED, lambda: make_replay_agent(RP, player=1)),
    ("ref_s1000", 1000, lambda: load("ref_top30.py").agent),
    ("ref_s1001", 1001, lambda: load("ref_top30.py").agent),
]
for path in sys.argv[1:]:
    tot = won = 0; out = []
    for label, seed, mk in MATCHES:
        for seat in (0, 1):
            ours, opp = load(path).agent, mk()
            pair = (ours, opp) if seat == 0 else (opp, ours)
            env = make("kaggriculture", configuration={"seed": int(seed)})
            env.run(list(pair))
            f = env.steps[-1]
            us, them = f[seat]["reward"], f[1 - seat]["reward"]
            tot += us; won += us > them
            out.append("%s/s%d %.0f/%.0f%s" % (label, seat, us, them, "W" if us > them else "L"))
    print("%-12s wins=%d/8 mean=$%-9.0f | %s" % (path, won, tot / 8, "  ".join(out)), flush=True)
