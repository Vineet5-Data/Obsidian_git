import importlib.util, itertools, sys
from kaggle_environments import make
from replay_opponent import make_replay_agent
_u = itertools.count()
def load(p):
    s = importlib.util.spec_from_file_location("m%d" % next(_u), p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
RP2 = ".tmp_replay_90473753.json"; SEED2 = 1250560110
print("--- vs Seb-2 (episode 90473753, seed %d) ---" % SEED2)
for path in sys.argv[1:]:
    won = 0; tot = 0; out = []
    for seat in (0, 1):
        ours, opp = load(path).agent, make_replay_agent(RP2, player=1)
        pair = (ours, opp) if seat == 0 else (opp, ours)
        env = make("kaggriculture", configuration={"seed": SEED2})
        env.run(list(pair)); f = env.steps[-1]
        us, them = f[seat]["reward"], f[1-seat]["reward"]
        won += us > them; tot += us
        out.append("seat%d %.0f/%.0f%s" % (seat, us, them, "W" if us > them else "L"))
    print("%-9s wins=%d/2 mean=$%-9.0f | %s" % (path, won, tot/2, "  ".join(out)), flush=True)
