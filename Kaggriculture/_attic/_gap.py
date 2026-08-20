import importlib.util, itertools
from kaggle_environments import make
_u = itertools.count()
def load(p):
    s = importlib.util.spec_from_file_location("m%d" % next(_u), p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
env = make("kaggriculture", configuration={"seed": 1001})
env.run([load("v7a.py").agent, load("ref_top30.py").agent])
st = env.steps
tot_unw = tot_unc = tot_crop = tot_an = 0
for day in range(30):
    i = min(day * 24 + 23, len(st) - 1)
    o = st[i][0]["observation"]
    unw = unc = crop = an = 0
    for row in o["farms"][0]["tiles"]:
        for t in row:
            if not isinstance(t, dict): continue
            if t.get("kind") == "PLANT":
                crop += 1
                if not t.get("watered_today"): unw += 1
            elif t.get("kind") == "PASTURE" and t.get("animal"):
                an += 1
                if not t.get("cared_today"): unc += 1
    tot_unw += unw; tot_unc += unc; tot_crop += crop; tot_an += an
    if day % 4 == 0 or unc:
        print("d%-2d crops=%-3d unwatered=%-3d animals=%-3d uncared=%d" % (day, crop, unw, an, unc))
print("TOTAL crop-days=%d unwatered=%d (%.1f%%) | animal-days=%d uncared=%d (%.1f%%)"
      % (tot_crop, tot_unw, 100.0*tot_unw/max(1,tot_crop), tot_an, tot_unc, 100.0*tot_unc/max(1,tot_an)))
