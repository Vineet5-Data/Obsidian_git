"""Money + wins across many seeds vs ref_top30, both seats."""
import importlib.util, itertools, statistics, sys
from kaggle_environments import make
_u = itertools.count()
def load(p):
    s = importlib.util.spec_from_file_location("m%d" % next(_u), p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
SEEDS = [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007]
for path in sys.argv[1:]:
    vals = []; wins = 0; detail = []
    for seed in SEEDS:
        for seat in (0, 1):
            ours, opp = load(path).agent, load("ref_top30.py").agent
            pair = (ours, opp) if seat == 0 else (opp, ours)
            env = make("kaggriculture", configuration={"seed": seed})
            env.run(list(pair)); f = env.steps[-1]
            us, them = f[seat]["reward"], f[1-seat]["reward"]
            vals.append(us); wins += us > them
            if seat == 0:
                detail.append("s%d:%.0f%s" % (seed, us, "W" if us > them else "L"))
    print("%-9s wins=%2d/16 mean=$%-9.0f median=$%-9.0f min=$%-9.0f | %s"
          % (path, wins, statistics.mean(vals), statistics.median(vals), min(vals), " ".join(detail)), flush=True)
