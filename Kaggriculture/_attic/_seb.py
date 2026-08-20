"""Fight the new top contender (Seb, $148,637) from episode 90503598."""
import importlib.util, itertools, sys
from kaggle_environments import make
from replay_opponent import make_replay_agent, replay_seed
_u = itertools.count()
def load(p):
    s = importlib.util.spec_from_file_location("m%d" % next(_u), p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
RP = ".tmp_replay_90503598.json"
SEED = replay_seed(RP)
print("seed", SEED)
for path in sys.argv[1:]:
    won = 0; tot = 0; out = []
    for seat in (0, 1):
        ours = load(path).agent
        opp = make_replay_agent(RP, player=0)   # Seb
        pair = (ours, opp) if seat == 0 else (opp, ours)
        env = make("kaggriculture", configuration={"seed": int(SEED)})
        env.run(list(pair)); f = env.steps[-1]
        us, them = f[seat]["reward"], f[1-seat]["reward"]
        won += us > them; tot += us
        out.append("seat%d %.0f/%.0f%s" % (seat, us, them, "W" if us > them else "L"))
    print("%-10s wins=%d/2 mean=$%-9.0f | %s" % (path, won, tot/2, "  ".join(out)), flush=True)
