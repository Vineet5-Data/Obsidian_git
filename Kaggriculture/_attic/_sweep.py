"""Sweep market-layer knobs on a fixed matchup; print our money and the opponent's."""
import importlib.util, itertools, sys
from kaggle_environments import make
_u = itertools.count()
def load(p, cfg=None):
    s = importlib.util.spec_from_file_location("m%d" % next(_u), p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    for k, v in (cfg or {}).items(): setattr(m, k, v)
    return m

opp_path, seed = sys.argv[1], int(sys.argv[2])
CFGS = {
    "baseline_main":   ("main.py", {}),
    "topup_only_f015": ("v6.py", dict(TRIM=0, FLOOR_SCALE=0.15)),
    "topup_only_f050": ("v6.py", dict(TRIM=0, FLOOR_SCALE=0.50)),
    "trim+topup_f100": ("v6.py", dict(TRIM=1, FLOOR_SCALE=1.0)),
    "trim+topup_f050": ("v6.py", dict(TRIM=1, FLOOR_SCALE=0.5)),
}
for name, (p, cfg) in CFGS.items():
    env = make("kaggriculture", configuration={"seed": seed})
    env.run([load(p, cfg).agent, load(opp_path).agent])
    f = env.steps[-1]
    print("%-18s ours=$%-9.0f opp=$%-9.0f %s" % (name, f[0]["reward"], f[1]["reward"],
          "WIN" if f[0]["reward"] > f[1]["reward"] else "loss"), flush=True)
