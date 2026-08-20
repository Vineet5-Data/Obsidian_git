"""Identify which engine version produced a recorded Kaggle episode.

A replay stores both `market.inventory` and `market.prices` at every step, and
the price is a pure function of the inventory under a given engine version. So
the recorded pairs alone identify the version -- no re-run required.

1.32.7 moved CARROT / TOMATO / EGG onto a "hinge" scarcity curve and raised
CARROT's below_target 0.20 -> 1.00, so those three products disagree between
versions whenever the market is short. WHEAT / STRAWBERRY / MELON / MILK /
WOOL / FERTILIZER are identical in both and act as a control: if even they
mismatch, the episode came from something neither table describes.

Usage:  python _which_engine.py <episode.json> [more.json ...]

Get an episode JSON from the Kaggle API (the same source _extract_fresh.py
consumes), e.g. an episode behind one of the .top/ tapes.
"""
import json
import math
import sys

MARKET_I0 = 10000
PRICE_FLOOR = 1
HINGE_GAIN = 8.0

# below-I0 side is what differs; above-I0 is identical in both versions.
V1326 = {
    "WHEAT":      {"base":  25, "T": 400, "bf": "sqrt",   "bt": 0.80, "af": "log",    "at": 0.20},
    "CARROT":     {"base":  35, "T": 450, "bf": "log",    "bt": 0.20, "af": "sqrt",   "at": 0.70},
    "TOMATO":     {"base":  60, "T": 200, "bf": "linear", "bt": 0.40, "af": "sqrt",   "at": 0.60},
    "STRAWBERRY": {"base": 120, "T": 100, "bf": "sqrt",   "bt": 0.70, "af": "linear", "at": 1.60},
    "MELON":      {"base": 250, "T": 300, "bf": "log",    "bt": 0.20, "af": "sq",     "at": 3.60},
    "EGG":        {"base":  50, "T": 332, "bf": "linear", "bt": 0.40, "af": "log",    "at": 0.20},
    "MILK":       {"base": 160, "T": 122, "bf": "sqrt",   "bt": 0.60, "af": "linear", "at": 1.60},
    "WOOL":       {"base": 200, "T": 105, "bf": "log",    "bt": 0.20, "af": "sq",     "at": 3.20},
    "FERTILIZER": {"base": 100, "T": 200, "bf": "linear", "bt": 0.40, "af": "linear", "at": 0.40},
}
V1327 = {k: dict(v) for k, v in V1326.items()}
V1327["CARROT"].update(bf="hinge", bt=1.00)
V1327["TOMATO"].update(bf="hinge")
V1327["EGG"].update(bf="hinge")

DIFFER = ("CARROT", "TOMATO", "EGG")
CONTROL = tuple(k for k in V1326 if k not in DIFFER)


def _shape(func, x, T=None):
    x = max(0.0, x)
    if func == "linear":
        return x
    if func == "sq":
        return x * x
    if func == "sqrt":
        return math.sqrt(x)
    if func == "log":
        return math.log(1.0 + x)
    if func == "hinge":
        if not T or T <= 0:
            return x
        u = x / T
        return u + HINGE_GAIN * max(0.0, u - 1.0) ** 2
    return x


def price(params, item, inventory):
    p = params[item]
    base, T = p["base"], p["T"]
    if inventory < MARKET_I0:
        amp = p["bt"] * base / _shape(p["bf"], T, T)
        v = base + amp * _shape(p["bf"], MARKET_I0 - inventory, T)
    else:
        amp = p["at"] * base / _shape(p["af"], T, T)
        v = base - amp * _shape(p["af"], inventory - MARKET_I0, T)
    return max(PRICE_FLOOR, int(round(v)))


def check(path):
    ep = json.load(open(path, encoding="utf-8"))
    steps = ep["steps"] if isinstance(ep, dict) and "steps" in ep else ep
    hits = {"1.32.6": 0, "1.32.7": 0}
    tested = control_bad = 0
    decisive = 0
    for st in steps:
        try:
            mk = st[0]["observation"]["market"]
            inv, pr = mk["inventory"], mk["prices"]
        except (KeyError, IndexError, TypeError):
            continue
        for item in CONTROL:
            if item in inv and item in pr:
                tested += 1
                if price(V1326, item, inv[item]) != pr[item]:
                    control_bad += 1
        for item in DIFFER:
            if item not in inv or item not in pr:
                continue
            a, b = price(V1326, item, inv[item]), price(V1327, item, inv[item])
            if a == b:
                continue  # market not short enough to tell them apart
            decisive += 1
            if pr[item] == a:
                hits["1.32.6"] += 1
            elif pr[item] == b:
                hits["1.32.7"] += 1
    print(f"\n{path}")
    print(f"  control pairs checked: {tested}  mismatched: {control_bad}"
          f"{'   <-- neither table fits; engine is something else' if control_bad else ''}")
    print(f"  decisive pairs (CARROT/TOMATO/EGG while short): {decisive}")
    if not decisive:
        print("  VERDICT: inconclusive -- those three never went short enough "
              "in this episode. Try another.")
        return
    for v, n in sorted(hits.items(), key=lambda kv: -kv[1]):
        print(f"    {v}: {n}/{decisive} ({100*n/decisive:.1f}%)")
    best = max(hits, key=hits.get)
    print(f"  VERDICT: leaderboard episode ran on {best}"
          if hits[best] == decisive else
          f"  VERDICT: ambiguous -- best is {best}, but not a clean sweep")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    for p in sys.argv[1:]:
        check(p)
