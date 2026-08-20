"""Synthetic checks for v125's shed-pressure relief against its v123b parent.

v125 changes one condition in adjusted_sell_hold: the >= 80 relief branch no
longer requires cash to be stressed as well.  These checks pin down that the
change is confined to that branch, that it moves the reservation in one
direction only, that it unblocks exactly the products measured to be clogging
the shed, and that the early game is untouched.

Run:  python test_v125_shed_drain.py
"""
import importlib.util
import random

PARENT = "a_v123b_harvest_atrisk.py"
CHILD = "a_v125_shed_drain.py"


def load(path):
    key = "t_" + path.replace(".", "_").replace("\\", "_").replace("/", "_")
    spec = importlib.util.spec_from_file_location(key, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


P, C = load(PARENT), load(CHILD)

# Observed late-game spots from probe_v125_shed.py on seed 387276923 seat 1,
# days 20-24 then days 25-29.
OBSERVED_SPOT = {
    "FERTILIZER": (29.8, 17.9), "MILK": (16.0, 18.8),
    "MELON": (4.7, 11.4), "WOOL": (57.2, 57.7), "STRAWBERRY": (45.0, 23.9),
}
# adjusted_sell_hold(base_hold, cash, projected_used, n_beasts, feed_target,
#                    wheat_buy)
ARGS = "base_hold cash projected_used n_beasts feed_target wheat_buy".split()


def call(mod, **kw):
    return mod.adjusted_sell_hold(*[kw[a] for a in ARGS])


def grid():
    """A coarse sweep of the argument space, biased to the observed regime."""
    for base_hold in (0.62, 0.44, 0.35, 0.12, 0.0):
        for cash in (0.0, 400.0, 2000.0, 20000.0, 90000.0):
            for used in (0, 30, 50, 54, 60, 76, 79, 80, 85, 94, 95, 100):
                for beasts in (0, 8, 16):
                    yield {"base_hold": base_hold, "cash": cash,
                           "projected_used": used, "n_beasts": beasts,
                           "feed_target": 6, "wheat_buy": 30.0}


def check(name, condition, detail=""):
    print(f"  {'PASS' if condition else 'FAIL'}  {name}" +
          (f"   {detail}" if detail else ""))
    assert condition, f"{name}: {detail}"


print(f"{CHILD} vs {PARENT}\n")

# 1 -- the defect: healthy cash pins sell_hold at the SHED_SOFT clamp even
# with the shed nearly full, so the >= 80 relief never fires in the parent.
kw = {"base_hold": 0.44, "cash": 60000.0, "projected_used": 92,
      "n_beasts": 16, "feed_target": 6, "wheat_buy": 30.0}
check("1 parent pins sell_hold at 0.35 with a 92/100 shed and healthy cash",
      abs(call(P, **kw) - 0.35) < 1e-9, f"parent={call(P, **kw)}")
check("1 child relaxes it to 0.08 on storage pressure alone",
      abs(call(C, **kw) - 0.08) < 1e-9, f"child={call(C, **kw)}")

# 2 -- confined to the branch: below 80 the two agents are identical
below = [(kw, call(P, **kw), call(C, **kw))
         for kw in grid() if kw["projected_used"] < 80]
check("2 identical for every state with projected_used < 80",
      all(abs(p - c) < 1e-12 for _k, p, c in below),
      f"{len(below)} states checked")

# 3 -- ordering invariant: v125 never reserves MORE than v123b
allst = [(kw, call(P, **kw), call(C, **kw)) for kw in grid()]
check("3 child <= parent for every state (relief is one-directional)",
      all(c <= p + 1e-12 for _k, p, c in allst),
      f"{len(allst)} states checked")

# 4 -- the low-cash path is unchanged: where the parent already relieved,
# the child agrees exactly
stressed = [(k, p, c) for k, p, c in allst
            if k["projected_used"] >= 80
            and k["cash"] < P.hire_bill(min(8, max(2, -(-k["n_beasts"] // 3))))
            + k["feed_target"] * k["wheat_buy"]]
check("4 unchanged wherever the parent already relieved (low cash, >= 80)",
      all(abs(p - c) < 1e-12 for _k, p, c in stressed),
      f"{len(stressed)} states checked")

# 5 -- monotone in shed pressure: more storage stress never raises the
# reservation
for base_hold in (0.62, 0.44, 0.35):
    seq = [call(C, base_hold=base_hold, cash=60000.0, projected_used=u,
                n_beasts=16, feed_target=6, wheat_buy=30.0)
           for u in range(0, 101)]
    check(f"5 monotone non-increasing in projected_used (base {base_hold})",
          all(a >= b - 1e-12 for a, b in zip(seq, seq[1:])))

# 6 -- the >= 95 branch keeps its cash test (single-cause: only one condition
# changed)
kw95 = {"base_hold": 0.44, "cash": 60000.0, "projected_used": 99,
        "n_beasts": 16, "feed_target": 6, "wheat_buy": 30.0}
check("6 the >= 95 branch still requires low cash (not relaxed to 0.0)",
      abs(call(C, **kw95) - 0.08) < 1e-9, f"child={call(C, **kw95)}")
kw95_poor = dict(kw95, cash=100.0)
check("6 the >= 95 branch still fires when cash IS low",
      abs(call(C, **kw95_poor) - 0.0) < 1e-9, f"child={call(C, **kw95_poor)}")

# 7 -- targeting: at 0.08 the reservation clears the two measured clogs and
# still refuses the genuinely worthless product
for item, (spot_a, spot_b) in OBSERVED_SPOT.items():
    r_parent = 0.35 * C.MP[item]["base"]
    r_child = 0.08 * C.MP[item]["base"]
    want = item in ("FERTILIZER", "MILK")
    got = r_child < spot_a and r_parent > spot_a
    if want:
        check(f"7 {item} unblocks at 0.08 and was blocked at 0.35", got,
              f"spot {spot_a}, r 0.35->{r_parent:.1f} 0.08->{r_child:.1f}")
check("7 MELON stays blocked at 0.08 (spot 4.7 below reservation 20.0)",
      0.08 * C.MP["MELON"]["base"] > OBSERVED_SPOT["MELON"][0],
      f"r={0.08 * C.MP['MELON']['base']:.1f} spot={OBSERVED_SPOT['MELON'][0]}")

# 8 -- rank_sales end to end on a synthetic shed matching the measured
# days 20-24 composition.  Derive each market inventory from the spot the
# probe actually observed rather than guessing an overhang.
def inv_for_spot(item, target):
    lo, hi = C.I0, C.I0 + 5000
    while lo < hi:
        mid = (lo + hi) // 2
        if C.price(item, mid) > target:
            lo = mid + 1
        else:
            hi = mid
    return lo


minv = {k: C.I0 for k in C.MP}
for item in ("FERTILIZER", "MILK", "MELON"):
    minv[item] = inv_for_spot(item, OBSERVED_SPOT[item][0])
check("8 synthetic market reproduces the observed spots",
      all(abs(C.price(i, minv[i]) - OBSERVED_SPOT[i][0]) <= 2.0
          for i in ("FERTILIZER", "MILK", "MELON")),
      ", ".join(f"{i} {C.price(i, minv[i]):.1f}"
                for i in ("FERTILIZER", "MILK", "MELON")))
projected = {"FERTILIZER": 20, "MILK": 13, "MELON": 5, "WHEAT": 25}
opp_wave = {k: 0.0 for k in C.MP}
step = 22 * C.TPD
sold_p = {i: a for _r, _v, i, a in
          P.rank_sales(projected, minv, opp_wave, call(P, base_hold=0.44,
                       cash=60000.0, projected_used=88, n_beasts=16,
                       feed_target=6, wheat_buy=30.0), 12, step)}
sold_c = {i: a for _r, _v, i, a in
          C.rank_sales(projected, minv, opp_wave, call(C, base_hold=0.44,
                       cash=60000.0, projected_used=88, n_beasts=16,
                       feed_target=6, wheat_buy=30.0), 12, step)}
check("8 parent sells no FERTILIZER from an 88/100 shed with healthy cash",
      sold_p.get("FERTILIZER", 0) == 0, f"parent sold {sold_p}")
check("8 child does sell FERTILIZER from the same shed",
      sold_c.get("FERTILIZER", 0) > 0, f"child sold {sold_c}")
check("8 child sells no MELON (spot far below even the relaxed reservation)",
      sold_c.get("MELON", 0) == 0, f"child sold {sold_c}")
check("8 child never sells less of any item than the parent",
      all(sold_c.get(i, 0) >= sold_p.get(i, 0) for i in projected),
      f"parent {sold_p} child {sold_c}")

# 9 -- randomized differential over the full argument space
rng = random.Random(20260814)
changed = total = 0
for _ in range(5000):
    kw = {"base_hold": rng.choice([0.0, 0.12, 0.35, 0.44, 0.62]),
          "cash": rng.uniform(0.0, 100000.0),
          "projected_used": rng.randint(0, 100),
          "n_beasts": rng.randint(0, 20),
          "feed_target": rng.randint(0, 10),
          "wheat_buy": rng.uniform(10.0, 60.0)}
    p, c = call(P, **kw), call(C, **kw)
    total += 1
    changed += abs(p - c) > 1e-12
check("9 randomized differential stays a narrow intervention",
      changed / total < 0.25,
      f"{changed}/{total} = {100.0 * changed / total:.2f}% of states change")

print(f"\nall checks passed  ({100.0 * changed / total:.2f}% differential)")
