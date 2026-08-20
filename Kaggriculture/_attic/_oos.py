"""Out-of-sample: the real seeds from the two lost Kaggle episodes."""
import importlib.util, itertools, sys
from kaggle_environments import make
_u = itertools.count()
def load(p):
    s = importlib.util.spec_from_file_location("m%d" % next(_u), p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
SEEDS = [("ep90487461", 1934697975), ("ep90489800", 112972794)]
for path in sys.argv[1:]:
    won = 0; tot = 0; out = []
    for label, seed in SEEDS:
        for seat in (0, 1):
            ours, opp = load(path).agent, load("ref_top30.py").agent
            pair = (ours, opp) if seat == 0 else (opp, ours)
            env = make("kaggriculture", configuration={"seed": seed})
            env.run(list(pair)); f = env.steps[-1]
            us, them = f[seat]["reward"], f[1-seat]["reward"]
            won += us > them; tot += us
            out.append("%s/s%d %.0f/%.0f%s" % (label, seat, us, them, "W" if us > them else "L"))
    print("%-10s wins=%d/4 mean=$%-9.0f | %s" % (path, won, tot/4, "  ".join(out)), flush=True)
