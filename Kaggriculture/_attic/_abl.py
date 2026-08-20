"""Ablate main.py knobs across the matchups we currently lose."""
import importlib.util, itertools, sys
from kaggle_environments import make
from replay_opponent import make_replay_agent, replay_seed
_u = itertools.count()

def load(p, cfg=None):
    s = importlib.util.spec_from_file_location("m%d" % next(_u), p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    for k, v in (cfg or {}).items(): setattr(m, k, v)
    return m

RP = ".tmp_replay_90452532.json"
ESEED = replay_seed(RP)
MATCHES = [
    ("elite_p0", ESEED, lambda: make_replay_agent(RP, player=0)),
    ("elite_p1", ESEED, lambda: make_replay_agent(RP, player=1)),
    ("ref_s1001", 1001, lambda: load("ref_top30.py").agent),
]
CFGS = {
    "base":            {},
    "no_animal_adapt": dict(ANIMAL_SWITCH_DAY=999),
    "maxone_13":       dict(MAX_ONE_ANIMAL=13),
    "maxone_7":        dict(MAX_ONE_ANIMAL=7),
    "always_adapt":    dict(ANIMAL_SWITCH_DAY=0),
}
agent_path = sys.argv[1] if len(sys.argv) > 1 else "main.py"
for name, cfg in CFGS.items():
    tot = won = 0
    out = []
    for label, seed, mk in MATCHES:
        for seat in (0, 1):
            ours = load(agent_path, cfg).agent
            opp = mk()
            pair = (ours, opp) if seat == 0 else (opp, ours)
            env = make("kaggriculture", configuration={"seed": int(seed)})
            env.run(list(pair))
            f = env.steps[-1]
            us, them = f[seat]["reward"], f[1 - seat]["reward"]
            tot += us; won += us > them
            out.append("%s/s%d %.0f vs %.0f" % (label, seat, us, them))
    print("%-18s wins=%d/6 mean=$%-9.0f | %s" % (name, won, tot / 6, "  ".join(out)), flush=True)
