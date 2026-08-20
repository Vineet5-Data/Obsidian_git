"""What actually occupies the shed when storage_load > 90 damps every harvest?

probe_v125_labor.py established that in days 20-29 the shed sits at 68-76 of 100
and crosses 90 on 23-52% of steps, and that `storage_load > 90 -> gain *= 0.1`
in crop_service_jobs then drops a rescued STRAWBERRY HARVEST job to rank ~28 of
43 -- unassignable with 12 hands.  So the shed, not the harvest price, is the
binding resource.

rank_sales has a STRAWBERRY-specific escape (`rival_qty > 0 -> reservation 1.0`)
that should keep strawberries moving, so the occupant is probably something
else.  This records, per product and day window:

  - units resident in the shed
  - spot price, and the reservation `sell_hold * MP[item]["base"]` we insist on
  - whether rank_sales actually emitted a sell row for it

A product whose reservation sits above its spot for most of a window is one we
have decided never to sell, and it is paying for that decision with shed slots.

Usage:  python probe_v125_shed.py SEED SEAT OPPONENT.py AGENT.py [AGENT.py ...]
"""
import collections
import importlib.util
import sys

from kaggle_environments import make

TPD = 24
WINDOWS = ((0, 14), (15, 19), (20, 24), (25, 29))


def load(path):
    key = "p_" + path.replace(".", "_").replace("\\", "_").replace("/", "_")
    spec = importlib.util.spec_from_file_location(key, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def window_of(day):
    for lo, hi in WINDOWS:
        if lo <= day <= hi:
            return (lo, hi)
    return None


def instrument(mod):
    """Wrap rank_sales; one record per (step, item) with reservation vs spot."""
    original = mod.rank_sales
    recs = []

    def wrapped(projected, minv, opp_wave, sell_hold, keep_wheat, step):
        rows = original(projected, minv, opp_wave, sell_hold, keep_wheat, step)
        sold = {item: amount for _r, _v, item, amount in rows}
        for item, qty in projected.items():
            if item not in mod.MP or int(qty or 0) <= 0:
                continue
            rival = int(max(0.0, opp_wave.get(item, 0.0)))
            base = mod.MP[item]["base"]
            reservation = max(1.0, (0.0 if step >= mod.DUMP_STEP else sell_hold)
                              * base)
            if item == "STRAWBERRY" and rival > 0:
                reservation = 1.0
            recs.append({
                "step": step, "item": item, "qty": int(qty),
                "spot": float(mod.price(item, minv.get(item, mod.I0))),
                "reservation": float(reservation),
                "sell_hold": float(sell_hold),
                "sold": int(sold.get(item, 0)),
            })
        return rows

    mod.rank_sales = wrapped
    return recs


def probe(path, seed, seat, opponent_path):
    mod = load(path)
    opp = load(opponent_path)
    recs = instrument(mod)
    players = [mod.agent, opp.agent] if seat == 0 else [opp.agent, mod.agent]
    env = make("kaggriculture",
               configuration={"episodeSteps": 720, "seed": seed})
    env.run(players)

    agg = collections.defaultdict(lambda: collections.defaultdict(float))
    for r in recs:
        w = window_of(r["step"] // TPD)
        if w is None:
            continue
        k = (w, r["item"])
        a = agg[k]
        a["n"] += 1
        a["qty"] += r["qty"]
        a["spot"] += r["spot"]
        a["reservation"] += r["reservation"]
        a["blocked"] += 1.0 if r["reservation"] > r["spot"] else 0.0
        a["sold"] += r["sold"]
        a["sold_steps"] += 1.0 if r["sold"] > 0 else 0.0
    final = env.steps[-1]
    return int(final[seat].reward), int(final[1 - seat].reward), agg


if __name__ == "__main__":
    seed, seat, opponent = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    for path in sys.argv[4:]:
        score, oscore, agg = probe(path, seed, seat, opponent)
        print(f"\n{path}   score {score:,} vs {oscore:,}  "
              f"margin {score - oscore:+,}")
        for w in WINDOWS:
            rows = [(k[1], v) for k, v in agg.items() if k[0] == w]
            if not rows:
                continue
            rows.sort(key=lambda kv: -kv[1]["qty"] / max(1.0, kv[1]["n"]))
            print(f"  days {w[0]}-{w[1]}")
            print(f"    {'item':11} {'held':>6} {'spot':>7} {'reserv':>7} "
                  f"{'blocked':>8} {'sold/step':>10} {'sell steps':>11}")
            for item, v in rows[:6]:
                n = max(1.0, v["n"])
                print(f"    {item:11} {v['qty']/n:6.1f} {v['spot']/n:7.1f} "
                      f"{v['reservation']/n:7.1f} {100*v['blocked']/n:7.1f}% "
                      f"{v['sold']/n:10.2f} {100*v['sold_steps']/n:10.1f}%")
