"""Day-windowed economic loss analysis: net cash generated per window, by product.

Three windows (per the observed pattern -- competitive early, falls apart late):
  0-19    baseline
  20-24   first collapse window
  25-29   second / terminal collapse window

Mechanics below are copied verbatim from the installed engine
(kaggle_environments/envs/kaggriculture/kaggriculture.py) so costs that are
fixed-price are EXACT, not estimated:
  - BUY_SEED  = CROPS[item]["seed"]            (engine L12-17, L590)
  - BUY_ANIMAL= ANIMALS[item]["cost"]           (engine L20-23, L592)
  - BUY_LAND  = LAND_PRICES[n_already_unlocked] (engine L84, L699-712)
  - HIRE      = mult * fib(hires_today)         (engine L677-694)
  - FEED costs no money -- it consumes 1 WHEAT from hand inventory (L492-500);
    reported as an action count, not a $ figure.

Only SELL / BUY_PRODUCT are dynamically priced (engine's per-unit lockstep,
_process_market): each unit's price depends on live shared market inventory,
which shifts as BOTH players trade the same step, and an order ABORTS on the
first unit that cannot commit (empty shed, not enough money, full shed).

This used to price `units REQUESTED x the single pre-trade quote`, which
fabricates both volume and cash for any agent that over-requests: measured on
one game, an opponent's reconstructed cash came out at 4.2x its true money
delta (+104,507 on a real +32,936). `replay_market()` below now replays the
engine's slot/unit loop exactly and reports FILLED units at the price each unit
actually got. Every window carries `cash_residual` -- reconstructed cash minus
the exact money delta -- so the remaining gap is always on the report.

"Production" per product = shed delta across the window + units sold + units
consumed as BUY_PRODUCT outflow -- shed is the only place harvested/bought
goods sit before being sold, so this is an exact mass balance, not an estimate,
regardless of whether it came from crop yield, animal product, or purchase.

Usage:  python _econ_loss_analysis.py [agent1.py agent2.py ...] [--workers N] [--out path.json]
        [--opponents N] [--seeds N] [--offset N]
--opponents N: use only first N .top/ opponents (fewer opponents, not more games).
--seeds N: N fresh seeds per opponent instead of its 1 recorded/home seed
  (same generator as run_bisect.py's random mode) -- games/agent = 2*opponents*N.
--offset N: skip the first N seeds (only matters with --seeds).
No agents given -> flat a_*.py (Kaggle/kg-bisect convention), else local dev filenames.
Opponents from .top/ (any attached dataset, mount path auto-detected).
"""
import glob
import json
import math
import multiprocessing as mp
import os
import sys
import time
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_AGENTS = ["v108_nopump.py", "v97_cap70.py", "100v.py"]

TURNS_PER_DAY = 24
WINDOWS = [("0-19", 0, 19), ("20-24", 20, 24), ("25-29", 25, 29)]

CROPS = {
    "WHEAT":      {"seed": 10},
    "CARROT":     {"seed": 20},
    "TOMATO":     {"seed": 50},
    "STRAWBERRY": {"seed": 100},
    "MELON":      {"seed": 80},
}
ANIMALS = {
    "GOOSE": {"cost": 300}, "COW": {"cost": 400}, "SHEEP": {"cost": 500},
}
PRODUCTS = ["WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON", "EGG", "MILK", "WOOL", "FERTILIZER"]
LAND_PRICES = [1000, 2000, 4000]


def _fib(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# --- engine market mechanics, copied verbatim from the INSTALLED engine -------
# (kaggle_environments/envs/kaggriculture/kaggriculture.py, v1.32.7).  The town
# centre drains 1 unit/product every `townCenterSellInterval` (24) steps -- no
# day-scaled multiplier -- and shops are drawn WITH REPLACEMENT, so the same
# shop can appear in unlocked_shops more than once and every instance consumes.
# _env_src.py in this repo is a verbatim copy of the same file; re-copy it after
# any kaggle_environments upgrade rather than editing it by hand.
MARKET_I0 = 10000
PRICE_FLOOR = 1
MAX_MARKET_ORDERS = 10
SHOP_SELL_INTERVAL = 4
SHED_CAPACITY = 100
CENTER_SELL_INTERVAL = 24
TOWN_CENTER_PRODUCTS = [p for p in PRODUCTS if p != "FERTILIZER"]

MARKET_PARAMS = {
    "WHEAT":      {"base":  25, "T": 400, "bf": "sqrt",   "bt": 0.80, "af": "log",    "at": 0.20},
    "CARROT":     {"base":  35, "T": 450, "bf": "hinge",  "bt": 1.00, "af": "sqrt",   "at": 0.70},
    "TOMATO":     {"base":  60, "T": 200, "bf": "hinge",  "bt": 0.40, "af": "sqrt",   "at": 0.60},
    "STRAWBERRY": {"base": 120, "T": 100, "bf": "sqrt",   "bt": 0.70, "af": "linear", "at": 1.60},
    "MELON":      {"base": 250, "T": 300, "bf": "log",    "bt": 0.20, "af": "sq",     "at": 3.60},
    "EGG":        {"base":  50, "T": 332, "bf": "hinge",  "bt": 0.40, "af": "log",    "at": 0.20},
    "MILK":       {"base": 160, "T": 122, "bf": "sqrt",   "bt": 0.60, "af": "linear", "at": 1.60},
    "WOOL":       {"base": 200, "T": 105, "bf": "log",    "bt": 0.20, "af": "sq",     "at": 3.20},
    "FERTILIZER": {"base": 100, "T": 200, "bf": "linear", "bt": 0.40, "af": "linear", "at": 0.40},
}

SHOPS = {
    "BAKERY":         ["EGG", "WHEAT"],
    "PIZZA_SHOP":     ["MILK", "TOMATO", "WHEAT"],
    "BRUNCH_SPOT":    ["EGG", "WHEAT", "STRAWBERRY"],
    "YARN_STORE":     ["WOOL"],
    "ICE_CREAM_SHOP": ["STRAWBERRY", "MILK", "WHEAT"],
    "PET_CAFE":       ["CARROT"],
    "SMOOTHIE_SHOP":  ["STRAWBERRY", "MILK"],
    "FARMERS_MARKET": ["WHEAT", "CARROT", "TOMATO", "STRAWBERRY"],
}


def _is_int(v):
    try:
        int(v)
        return True
    except (TypeError, ValueError):
        return False


HINGE_GAIN = 8.0


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
    if func == "log10":
        return math.log10(1.0 + x)
    if func == "hinge":
        # 1.32.7: calm until the resource is genuinely scarce, then runs away.
        if not T or T <= 0:
            return x
        u = x / T
        return u + HINGE_GAIN * max(0.0, u - 1.0) ** 2
    return x


def market_price(item, inventory):
    p = MARKET_PARAMS[item]
    base, T = p["base"], p["T"]
    if inventory < MARKET_I0:
        amp = p["bt"] * base / _shape(p["bf"], T, T)
        v = base + amp * _shape(p["bf"], MARKET_I0 - inventory, T)
    else:
        amp = p["at"] * base / _shape(p["af"], T, T)
        v = base - amp * _shape(p["af"], inventory - MARKET_I0, T)
    return max(PRICE_FLOOR, int(round(v)))


def _town_drain(step, shops):
    """Units the town removes from market inventory AFTER the market loop."""
    d = Counter()
    if step % SHOP_SELL_INTERVAL == 0:
        for name in shops:
            prods = SHOPS.get(name)
            if not prods:
                continue
            mult = 2 if len(prods) == 1 else 1
            for item in prods:
                d[item] += mult
    if step % CENTER_SELL_INTERVAL == 0:
        for item in TOWN_CENTER_PRODUCTS:
            d[item] += 1
    return d


def _parse_order(order):
    """Engine's _parse_order, restricted to the ops that enter the unit loop."""
    if not isinstance(order, list) or len(order) < 3:
        return None
    if order[0] not in ("SELL", "BUY_PRODUCT", "BUY_SEED", "BUY_ANIMAL"):
        return None  # HIRE / BUY_LAND are atomic, priced exactly elsewhere
    try:
        n = int(order[2])
    except (TypeError, ValueError):
        return None
    return {"type": order[0], "item": order[1], "remaining": n} if n > 0 else None


def replay_market(steps):
    """Exact per-seat FILLED market volume and cash, for every step.

    The shared market inventory is observable either side of every step and the
    town's consumption is deterministic, so the joint filled volume is exactly
    recoverable:

        traded[item] = inv_post - inv_pre + town_drain
                     = sells_filled(price > PRICE_FLOOR) - buys_filled

    Replaying the engine's slot-by-slot, unit-by-unit lockstep against that
    budget attributes fills to each seat and prices every unit at what it
    actually got.  Step indexing was pinned empirically: the action recorded at
    steps[i] was processed with engine step i-1 against steps[i-1]'s market
    (185/185 match on steps with no market orders).

    Returns (per_step, stats).  per_step[i][seat] is a dict of Counters:
    sell_units / sell_rev / buy_units / buy_spend.
    """
    n = len(steps)
    per_step = [None] * n
    stats = Counter()

    for i in range(1, n):
        pre = steps[i - 1][0]["observation"]
        inv_pre = pre["market"]["inventory"]
        inv_post = steps[i][0]["observation"]["market"]["inventory"]
        drain = _town_drain(i - 1, list(pre["town"].get("unlocked_shops") or []))

        queues = []
        for seat in (0, 1):
            a = steps[i][seat].get("action") or {}
            raw = (a.get("market") or []) if isinstance(a, dict) else []
            raw = list(raw)[:MAX_MARKET_ORDERS]  # engine truncates before parsing
            queues.append([_parse_order(o) for o in raw])

        res = [{"sell_units": Counter(), "sell_rev": Counter(),
                "buy_units": Counter(), "buy_spend": Counter()} for _ in (0, 1)]
        max_len = max((len(q) for q in queues), default=0)
        if max_len == 0:
            per_step[i] = res
            continue

        # A seat can only sell what is in ITS shed when the market runs.  Unit
        # actions are applied before _process_market, so this step's PLACE
        # deposits count and its PICKUP withdrawals do not.  Without this cap a
        # seat that spams SELL against an empty shed soaks up half the joint
        # budget through the lockstep interleave and is credited with the other
        # seat's sales.
        # ponytail: shed adjacency is not checked (worker positions are not
        # tracked), so a deposit by a worker standing away from the shed is
        # counted -- an upper bound.  cash_residual is the ceiling indicator.
        sell_cap = []
        for seat in (0, 1):
            priv = steps[i - 1][seat]["observation"]["private"]
            cap = Counter({p: int(priv["shed"].get(p, 0) or 0) for p in PRODUCTS})
            invs = priv.get("inventories") or []
            room = max(0, SHED_CAPACITY - sum(cap.values()))
            a = steps[i][seat].get("action") or {}
            units = ([a.get("farmer")] + list(a.get("hands") or [])) if isinstance(a, dict) else []
            for idx, u in enumerate(units):
                if not isinstance(u, list) or not u:
                    continue
                winv = (invs[idx] if idx < len(invs) else None) or {}
                if u[0] == "DROP":
                    # bare op: dumps the unit's WHOLE inventory, overflow burnt
                    for item, n in winv.items():
                        if item not in PRODUCTS or int(n or 0) <= 0:
                            continue
                        take = min(int(n), room)
                        cap[item] += take
                        room -= take
                    continue
                if len(u) < 2 or u[1] not in PRODUCTS:
                    continue
                qty = int(u[2]) if len(u) >= 3 and _is_int(u[2]) else 1
                if u[0] == "PLACE":
                    take = min(qty, int(winv.get(u[1], 0) or 0), room)
                    if take > 0:
                        cap[u[1]] += take
                        room -= take
                elif u[0] == "PICKUP" and qty > 0:
                    take = min(qty, cap[u[1]])
                    cap[u[1]] -= take
                    room += take
            sell_cap.append(cap)

        sell_budget, buy_budget = {}, {}
        for item in PRODUCTS:
            traded = inv_post[item] - inv_pre[item] + drain.get(item, 0)
            req_sell = sum(o["remaining"] for q in queues for o in q
                           if o and o["type"] == "SELL" and o["item"] == item)
            req_buy = sum(o["remaining"] for q in queues for o in q
                          if o and o["type"] == "BUY_PRODUCT" and o["item"] == item)
            feasible_sell = min(req_sell, sell_cap[0][item] + sell_cap[1][item])

            if req_sell and req_buy:
                # Both directions on one item in one step (WHEAT mostly: one
                # seat sells while the other buys feed).  A net delta cannot
                # separate them.  Take the smallest volumes consistent with it
                # -- pushing sells up to their shed bound instead was tested and
                # traded a 4x better median for a 2x worse tail, because the
                # shed bound is loose (no adjacency check) and the error lands
                # entirely on the inferred buy side.
                stats["ambiguous_item_steps"] += 1
                sell_budget[item] = max(0, traded)
                buy_budget[item] = max(0, -traded)
            elif req_sell:
                if traded > 0:
                    sell_budget[item] = traded
                elif market_price(item, inv_pre[item]) <= PRICE_FLOOR:
                    # Floor-price sales deliberately do not move supply (engine
                    # _commit_unit), so they are invisible in the delta.  The
                    # only other way a SELL fails is an empty shed, so the shed
                    # bound settles it exactly -- at $1/unit.
                    stats["floor_price_sell_steps"] += 1
                    sell_budget[item] = feasible_sell
            elif req_buy and traded < 0:
                buy_budget[item] = -traded

        inv = dict(inv_pre)
        for slot in range(max_len):
            state = [dict(queues[s][slot]) if slot < len(queues[s]) and queues[s][slot]
                     else None for s in (0, 1)]
            while True:
                quoted = [None, None]
                for s in (0, 1):
                    o = state[s]
                    if not o or o["remaining"] <= 0:
                        continue
                    op, item = o["type"], o["item"]
                    if op == "SELL" and item in MARKET_PARAMS:
                        quoted[s] = (op, item, market_price(item, inv[item]))
                    elif op == "BUY_PRODUCT" and item in ("WHEAT", "FERTILIZER"):
                        # engine quotes a buy at post-buy inventory
                        quoted[s] = (op, item, market_price(item, inv[item] - 1))
                    elif op in ("BUY_SEED", "BUY_ANIMAL"):
                        quoted[s] = (op, item, 0)  # fixed price, accounted elsewhere
                    else:
                        state[s] = None
                if quoted[0] is None and quoted[1] is None:
                    break
                committed = False
                for s in (0, 1):
                    q = quoted[s]
                    if q is None:
                        continue
                    op, item, unit_price = q
                    if op == "SELL":
                        if sell_budget.get(item, 0) <= 0 or sell_cap[s][item] <= 0:
                            state[s] = None
                            continue
                        sell_budget[item] -= 1
                        sell_cap[s][item] -= 1
                        res[s]["sell_units"][item] += 1
                        res[s]["sell_rev"][item] += unit_price
                        if unit_price > PRICE_FLOOR:
                            inv[item] += 1
                    elif op == "BUY_PRODUCT":
                        if buy_budget.get(item, 0) <= 0:
                            state[s] = None
                            continue
                        buy_budget[item] -= 1
                        res[s]["buy_units"][item] += 1
                        res[s]["buy_spend"][item] += unit_price
                        inv[item] -= 1
                    state[s]["remaining"] -= 1
                    committed = True
                if not committed:
                    break
        per_step[i] = res
    return per_step, stats


def find_opponents():
    """Locate the .top/ opponent tapes.

    Mount path varies: the grid-search dataset may land flat under
    /kaggle/input/<slug>/ or nested in a .top/ subdirectory, at a depth that
    is not fixed.  recursive=True is load-bearing -- without it "**" collapses
    to a single "*" and only matches one directory level.
    """
    for pattern in ("/kaggle/input/**/.top/t_*.py",
                    "/kaggle/input/**/t_*.py",
                    str(HERE / ".top" / "t_*.py"),
                    str(HERE / "t_*.py"),
                    ".top/t_*.py",
                    "t_*.py"):
        hits = sorted(glob.glob(pattern, recursive=True))
        if hits:
            return hits
    raise SystemExit(
        "no t_*.py opponent tapes found -- attach the grid_search dataset, or "
        "copy the tapes into a .top/ subdirectory next to this script")


def load(path):
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "m_" + os.path.basename(path).replace(".", "_"), path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.agent


def snapshot_at(steps, i, seat):
    """Full economic state for `seat` at step i. i=0 is the pre-day-0 initial state."""
    obs = steps[i][seat]["observation"]
    farm = obs["farms"][seat]
    plants, animals = Counter(), Counter()
    for row in (farm.get("tiles") or []):
        for t in (row or []):
            if isinstance(t, dict):
                if t.get("kind") == "PLANT":
                    plants[t["crop"]] += 1
                elif "animal" in t:
                    animals[t["animal"]] += 1
    return {
        "money": farm.get("money", 0.0),
        "shed": dict(obs["private"]["shed"]),
        "hires_today": farm.get("hires_today", 0),
        "land": len(farm.get("unlocked_quadrants") or []),
        "plants": plants, "animals": animals,
    }


def day_end_step(steps, day):
    return min(len(steps) - 1, day * TURNS_PER_DAY + 23)


def scan_orders(steps, day_lo, day_hi, seat, fills):
    """Sum SELL/BUY_SEED/BUY_ANIMAL/BUY_PRODUCT order quantities across
    [day_lo, day_hi] inclusive. Revenue/spend on SELL/BUY_PRODUCT use the
    pre-trade quoted price (~approx, see module docstring); seed/animal
    costs are fixed (exact)."""
    lo_step = 0 if day_lo == 0 else day_end_step(steps, day_lo - 1)
    hi_step = day_end_step(steps, day_hi)
    revenue, units_sold = Counter(), Counter()
    spend_seed, spend_animal = Counter(), Counter()
    buy_prod_spend, buy_prod_units = Counter(), Counter()
    # FEED/FERTILIZE pull 1 WHEAT/FERTILIZER out of shed-via-inventory with no
    # market order attached (engine L492-500, L462-469) -- without subtracting
    # these, the shed mass-balance below misreads consumption as negative
    # production. Counts attempted actions, not verified-successful ones (same
    # requested-not-verified tradeoff as BUY_SEED/BUY_ANIMAL qty above).
    feed_actions = fertilize_actions = 0

    for i in range(lo_step + 1, hi_step + 1):
        a = steps[i][seat].get("action") or {}
        if not isinstance(a, dict):
            continue
        for u in [a.get("farmer")] + list(a.get("hands") or []):
            if isinstance(u, list) and u:
                if u[0] == "FEED":
                    feed_actions += 1
                elif u[0] == "FERTILIZE":
                    fertilize_actions += 1
        # SELL / BUY_PRODUCT come from the exact replay, not from the request.
        f = fills[i][seat] if fills[i] else None
        if f:
            units_sold.update(f["sell_units"])
            revenue.update(f["sell_rev"])
            buy_prod_units.update(f["buy_units"])
            buy_prod_spend.update(f["buy_spend"])

        if not a.get("market"):
            continue
        for order in a["market"][:MAX_MARKET_ORDERS]:
            if not order or len(order) < 3:
                continue
            op, item = order[0], order[1]
            try:
                qty = int(order[2])
            except (TypeError, ValueError):
                continue
            if qty <= 0:
                continue
            # Fixed-price ops: still requested-not-verified (a buy fails only
            # when money runs out), but the price per unit is exact.
            if op == "BUY_SEED" and item in CROPS:
                spend_seed[item] += qty * CROPS[item]["seed"]
            elif op == "BUY_ANIMAL" and item in ANIMALS:
                spend_animal[item] += qty * ANIMALS[item]["cost"]

    return (revenue, units_sold, spend_seed, spend_animal, buy_prod_spend, buy_prod_units,
            feed_actions, fertilize_actions)


def window_econ(steps, lo_day, hi_day, seat, start_snap, day_snaps, fills):
    end_snap = day_snaps[hi_day]
    (revenue, units_sold, spend_seed, spend_animal, buy_prod_spend, buy_prod_units,
     feed_actions, fertilize_actions) = scan_orders(steps, lo_day, hi_day, seat, fills)

    wages = sum(sum(_fib(k) for k in range(day_snaps[d]["hires_today"]))
                for d in range(lo_day, hi_day + 1))

    land_spend, prev_land = 0.0, start_snap["land"]
    for d in range(lo_day, hi_day + 1):
        L = day_snaps[d]["land"]
        if L > prev_land:
            land_spend += sum(LAND_PRICES[k - 1] for k in range(prev_land, L))
        prev_land = L

    consumed = {"WHEAT": feed_actions, "FERTILIZER": fertilize_actions}
    production = {item: (end_snap["shed"].get(item, 0) - start_snap["shed"].get(item, 0)
                          + units_sold.get(item, 0) - buy_prod_units.get(item, 0)
                          + consumed.get(item, 0))
                  for item in PRODUCTS}

    net_cash = end_snap["money"] - start_snap["money"]
    # Reconstructed cash must equal the exact money delta.  Any gap left is
    # printed, never hidden -- that is what caught the requested-vs-filled bug.
    reconstructed = (sum(revenue.values())
                     - sum(buy_prod_spend.values()) - sum(spend_seed.values())
                     - sum(spend_animal.values()) - land_spend - wages)

    return {
        "net_cash": net_cash,
        "cash_residual": reconstructed - net_cash,
        "revenue": dict(revenue), "units_sold": dict(units_sold),
        "realized_price": {k: revenue[k] / units_sold[k] for k in units_sold if units_sold[k]},
        "spend_seed": dict(spend_seed), "spend_animal": dict(spend_animal),
        "spend_buy_product": dict(buy_prod_spend),
        "feed_actions": feed_actions, "fertilize_actions": fertilize_actions,
        "spend_land": land_spend, "spend_wage": wages,
        "production": production,
        "plants_end": dict(end_snap["plants"]), "animals_end": dict(end_snap["animals"]),
    }


def one(job):
    """Run one game, return exact per-window economics for both seats (never raw steps)."""
    agent_path, opp_path, seed, seat, opp_name = job
    from kaggle_environments import make
    a, b = load(agent_path), load(opp_path)
    pair = [a, b] if seat == 0 else [b, a]
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run(pair)
    steps = env.steps
    margin = steps[-1][seat].reward - steps[-1][1 - seat].reward

    fills, replay_stats = replay_market(steps)

    our_day_snaps = [snapshot_at(steps, day_end_step(steps, d), seat) for d in range(30)]
    opp_day_snaps = [snapshot_at(steps, day_end_step(steps, d), 1 - seat) for d in range(30)]
    our_init = snapshot_at(steps, 0, seat)
    opp_init = snapshot_at(steps, 0, 1 - seat)

    windows = {}
    for label, lo, hi in WINDOWS:
        our_start = our_day_snaps[lo - 1] if lo > 0 else our_init
        opp_start = opp_day_snaps[lo - 1] if lo > 0 else opp_init
        windows[label] = {
            "us": window_econ(steps, lo, hi, seat, our_start, our_day_snaps, fills),
            "opp": window_econ(steps, lo, hi, 1 - seat, opp_start, opp_day_snaps, fills),
        }

    return {"opponent": opp_name, "seed": seed, "seat": seat, "margin": margin,
            "win": margin > 0, "windows": windows, "replay_stats": dict(replay_stats)}


SCALAR_FIELDS = {"net_cash", "cash_residual", "spend_land", "spend_wage",
                 "feed_actions", "fertilize_actions"}
SCALAR_LABELS = {"net_cash": "net cash generated",
                  "cash_residual": "cash residual (should be ~0)", "spend_land": "land spend",
                  "spend_wage": "wage spend", "feed_actions": "feed actions (count)",
                  "fertilize_actions": "fertilize actions (count)"}
DICT_LABELS = {"revenue": "revenue (filled, exact)", "production": "production (units, exact)",
               "spend_seed": "seed spend", "spend_animal": "animal spend",
               "spend_buy_product": "buy_product spend (filled, exact)",
               "plants_end": "crop tiles, end of window", "animals_end": "herd, end of window"}


def report_window(label, rows, field):
    """field: scalar (SCALAR_FIELDS) or a per-product dict field name."""
    us_vals, opp_vals = [], []
    us_prod, opp_prod = Counter(), Counter()
    n = len(rows)
    if n == 0:
        return
    for r in rows:
        w = r["windows"][label]
        if field in SCALAR_FIELDS:
            us_vals.append(w["us"][field])
            opp_vals.append(w["opp"][field])
        else:
            for k, v in w["us"][field].items():
                us_prod[k] += v
            for k, v in w["opp"][field].items():
                opp_prod[k] += v

    if field in SCALAR_FIELDS:
        us_mean = sum(us_vals) / n
        opp_mean = sum(opp_vals) / n
        print(f"  {SCALAR_LABELS[field]}, day {label:<8} us {us_mean:>+12,.1f}   "
              f"opp {opp_mean:>+12,.1f}   gap (opp-us) {opp_mean - us_mean:>+12,.1f}   (n={n})")
        return opp_mean - us_mean

    us_avg = {k: v / n for k, v in us_prod.items()}
    opp_avg = {k: v / n for k, v in opp_prod.items()}
    keys = sorted(set(us_avg) | set(opp_avg),
                  key=lambda k: -abs(opp_avg.get(k, 0) - us_avg.get(k, 0)))
    print(f"    {DICT_LABELS.get(field, field)}:")
    for k in keys:
        u, o = us_avg.get(k, 0.0), opp_avg.get(k, 0.0)
        if abs(u) < 0.5 and abs(o) < 0.5:
            continue
        print(f"      {k:<12} us {u:>+10,.1f}   opp {o:>+10,.1f}   gap {o - u:>+10,.1f}")


def analyze_agent(agent_path, opps, seeds, workers, pool_seeds=None):
    jobs = []
    for o in opps:
        if pool_seeds:
            seed_list = pool_seeds
        else:
            ep = Path(o).stem.removeprefix("t_").rsplit("_", 1)[0]
            seed_list = [seeds.get(ep, 12345)]
        for seed in seed_list:
            for seat in (0, 1):
                jobs.append((agent_path, o, seed, seat, Path(o).stem))

    name = Path(agent_path).stem
    print(f"\n{name}: {len(jobs)} games queued...", flush=True)
    t0 = time.time()
    rows = []
    with mp.Pool(workers) as pool:
        for n, row in enumerate(pool.imap(one, jobs, chunksize=1), 1):
            rows.append(row)
            if n % 200 == 0 or n == len(jobs):
                el = time.time() - t0
                print(f"  {n}/{len(jobs)}  {el:.0f}s  eta {el / n * (len(jobs) - n):.0f}s", flush=True)

    wins = [r for r in rows if r["win"]]
    losses = [r for r in rows if not r["win"]]
    print(f"\n{'=' * 78}\n{name}: {len(wins)}-{len(losses)} "
          f"({100 * len(wins) / len(rows):.1f}%)\n{'=' * 78}")

    for cut_name, cut_rows in (("ALL GAMES", rows), ("LOSSES ONLY", losses)):
        if not cut_rows:
            continue
        print(f"\n-- {cut_name} (n={len(cut_rows)}) --")
        for label, _, _ in WINDOWS:
            report_window(label, cut_rows, "net_cash")
            report_window(label, cut_rows, "cash_residual")
            report_window(label, cut_rows, "revenue")
            report_window(label, cut_rows, "production")
            report_window(label, cut_rows, "spend_seed")
            report_window(label, cut_rows, "spend_animal")
            report_window(label, cut_rows, "spend_buy_product")
            report_window(label, cut_rows, "spend_land")
            report_window(label, cut_rows, "spend_wage")
            report_window(label, cut_rows, "feed_actions")
            report_window(label, cut_rows, "fertilize_actions")
            report_window(label, cut_rows, "plants_end")
            report_window(label, cut_rows, "animals_end")

    return {"agent": name, "rows": rows}


def main():
    argv = sys.argv[1:]
    workers = max(1, (os.cpu_count() or 4) - 2)
    out_path = Path("/kaggle/working/econ_loss_analysis.json")
    n_opponents = None
    n_seeds = 0
    offset = 0
    agents = []
    i = 0
    while i < len(argv):
        if argv[i] == "--workers":
            workers = int(argv[i + 1]); i += 2
        elif argv[i] == "--out":
            out_path = Path(argv[i + 1]); i += 2
        elif argv[i] == "--opponents":
            n_opponents = int(argv[i + 1]); i += 2
        elif argv[i] == "--seeds":
            n_seeds = int(argv[i + 1]); i += 2
        elif argv[i] == "--offset":
            offset = int(argv[i + 1]); i += 2
        else:
            agents.append(argv[i]); i += 1
    if not agents:
        agents = sorted(glob.glob(str(HERE / "a_*.py")))
        if not agents:
            agents = [str(HERE / a) for a in DEFAULT_AGENTS if (HERE / a).exists()]
        if not agents:
            raise SystemExit("no agent given and none of the defaults exist here")

    seeds = json.loads((HERE / "seeds.json").read_text()) if (HERE / "seeds.json").exists() else {}
    opps = find_opponents()
    if n_opponents:
        opps = opps[:n_opponents]
    # same generator run_bisect.py's n_random mode / top_tournament.py --mode
    # random use, so seeds line up across tools. n_seeds=0 keeps recorded mode
    # (1 game/opponent/seat, its own home tape seed) -- unchanged default.
    pool_seeds = [(k * 2654435761) % 2147483647
                  for k in range(offset + 1, offset + n_seeds + 1)] if n_seeds else None
    games_per_agent = 2 * len(opps) * (n_seeds if n_seeds else 1)
    mode = f"random x{n_seeds} offset {offset}" if n_seeds else "recorded"
    print(f"agents={len(agents)} opponents={len(opps)} mode={mode} "
          f"games/agent={games_per_agent} workers={workers}", flush=True)

    t0 = time.time()
    results = [analyze_agent(a, opps, seeds, workers, pool_seeds) for a in agents]
    print(f"\n({time.time() - t0:.0f}s total)")

    out_path.write_text(json.dumps(
        {r["agent"]: r["rows"] for r in results}, indent=2, default=str), encoding="utf-8")
    print(f"\nwrote {out_path}")


if __name__ == "__main__":
    mp.freeze_support()
    main()
