"""Realized-price diagnostic: run agent vs ref, report per-item qty and net revenue."""
import importlib.util, itertools, sys
from collections import defaultdict
from kaggle_environments import make

_u = itertools.count()
def load(p):
    s = importlib.util.spec_from_file_location("m%d" % next(_u), p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

cand, opp, seed = sys.argv[1], sys.argv[2], int(sys.argv[3])
env = make("kaggriculture", configuration={"seed": seed})
env.run([load(cand).agent, load(opp).agent])
st = env.steps
for k, name in ((0, cand), (1, opp)):
    qty = defaultdict(int); gross = defaultdict(float); dumped = defaultdict(int)
    for i, s in enumerate(st):
        a = s[k].get("action")
        if not isinstance(a, dict): continue
        pr = st[i][k]["observation"]["market"]["prices"]
        for mo in (a.get("market") or []):
            if mo and mo[0] == "SELL":
                qty[mo[1]] += mo[2]; gross[mo[1]] += pr.get(mo[1], 0) * mo[2]
                if pr.get(mo[1], 0) < 0.35 * {"WOOL":200,"MELON":250,"MILK":160,"STRAWBERRY":120,
                                              "WHEAT":25,"FERTILIZER":100,"CARROT":35,"EGG":50,"TOMATO":60}.get(mo[1],1):
                    dumped[mo[1]] += mo[2]
    print("p%d %-14s final=$%-9.0f" % (k, name, st[-1][k]["observation"]["farms"][k]["money"]))
    for it in sorted(qty, key=lambda x: -gross[x]):
        print("    %-11s q=%5d  avg_ask=$%6.1f  dumped_below_35pct=%d" %
              (it, qty[it], gross[it] / max(1, qty[it]), dumped[it]))
