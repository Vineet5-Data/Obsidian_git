"""g1 -- pure adaptive policy for Kaggriculture.  No replay tape, no cloned route.

Principle the agent is built on
-------------------------------
Final score is money, and money is bounded by what the MARKET CAN ABSORB, not
by what the farm can grow.  Absorption is set by the town: every unlocked shop
drains its products every `townShopSellInterval` steps, and the town centre
drains one of everything every 24 steps.  Shops are drawn at random per seed
(`rng.choice(sorted(SHOPS))`, keyed off the episode seed) and revealed every 3
days in `obs.town.unlocked_shops`.

So the profitable product mix is a per-seed random variable that only becomes
observable during the episode.  A fixed action tape cannot react to it; a
policy can.  Everything here derives from that:

  * production is allocated to whatever the observed drain will absorb,
  * animals are bought late, after the shop draw is known,
  * sell size per turn is capped so the realised price stays near base.

No opponent trajectory is used anywhere in this file.
"""

import math

BOARD = 10
TPD = 24
I0 = 10000
PRICE_FLOOR = 1

CROPS = {
    "WHEAT":      {"seed": 10,  "fyd": 2,  "myd": 4,  "iv": 0, "my": 6, "ong": False},
    "CARROT":     {"seed": 20,  "fyd": 2,  "myd": 3,  "iv": 0, "my": 4, "ong": False},
    "TOMATO":     {"seed": 50,  "fyd": 8,  "myd": 8,  "iv": 1, "my": 4, "ong": True},
    "STRAWBERRY": {"seed": 100, "fyd": 10, "myd": 10, "iv": 2, "my": 4, "ong": True},
    "MELON":      {"seed": 80,  "fyd": 10, "myd": 12, "iv": 0, "my": 6, "ong": False},
}

ANIMALS = {
    "GOOSE": {"cost": 300, "st": "COOP",    "fyd": 4, "iv": 1, "mh": 4, "prod": "EGG"},
    "COW":   {"cost": 400, "st": "PASTURE", "fyd": 8, "iv": 2, "mh": 6, "prod": "MILK"},
    "SHEEP": {"cost": 500, "st": "PASTURE", "fyd": 6, "iv": 3, "mh": 6, "prod": "WOOL"},
}

PRODUCTS = ["WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON",
            "EGG", "MILK", "WOOL", "FERTILIZER"]

MP = {
    "WHEAT":      {"base": 25,  "T": 400, "bf": "sqrt",   "bt": 0.80, "af": "log",    "at": 0.20},
    "CARROT":     {"base": 35,  "T": 450, "bf": "log",    "bt": 0.20, "af": "sqrt",   "at": 0.70},
    "TOMATO":     {"base": 60,  "T": 200, "bf": "linear", "bt": 0.40, "af": "sqrt",   "at": 0.60},
    "STRAWBERRY": {"base": 120, "T": 100, "bf": "sqrt",   "bt": 0.70, "af": "linear", "at": 1.60},
    "MELON":      {"base": 250, "T": 300, "bf": "log",    "bt": 0.20, "af": "sq",     "at": 3.60},
    "EGG":        {"base": 50,  "T": 332, "bf": "linear", "bt": 0.40, "af": "log",    "at": 0.20},
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
TOWN_CENTER = [p for p in PRODUCTS if p != "FERTILIZER"]
LAND_PRICES = [1000, 2000, 4000]
SHED_CAP = 100

# ---- tunables (all re-derivable from the mechanics above) ----
MAX_HANDS = 14           # marginal hand value ~= 24 actions; fib(14)=610 breaks even
HOLD_EARLY = 0.90        # keep realised price >= 90% of base while there is time
HOLD_LATE = 0.25
RELAX_DAY = 20           # start relaxing the price floor
DUMP_STEP = 706          # unconditional liquidation window
SHED_SOFT = 62           # keep room for the end-of-day inventory drop
FEED_CARRY = 5           # wheat picked up per trip


# --------------------------------------------------------------------------
# observation plumbing
# --------------------------------------------------------------------------
def _get(value, key, default=None):
    if isinstance(value, dict):
        return value.get(key, default)
    getter = getattr(value, "get", None)
    if callable(getter):
        return getter(key, default)
    return getattr(value, key, default)


def _seat(obs):
    return 1 if int(_get(obs, "player", 0) or 0) == 1 else 0


# --------------------------------------------------------------------------
# market model (mirrors the interpreter exactly)
# --------------------------------------------------------------------------
def _shape(func, x):
    x = max(0.0, x)
    if func == "linear":
        return x
    if func == "sq":
        return x * x
    if func == "sqrt":
        return math.sqrt(x)
    if func == "log":
        return math.log(1.0 + x)
    return x


def price(item, inv):
    p = MP.get(item)
    if p is None:
        return 0
    base, T = p["base"], p["T"]
    if inv < I0:
        amp = p["bt"] * base / _shape(p["bf"], T)
        v = base + amp * _shape(p["bf"], I0 - inv)
    else:
        amp = p["at"] * base / _shape(p["af"], T)
        v = base - amp * _shape(p["af"], inv - I0)
    return max(PRICE_FLOOR, int(round(v)))


def sell_cap(item, inv, floor_price, hi=600):
    """Largest n whose LAST unit still clears floor_price."""
    if price(item, inv) < floor_price:
        return 0
    lo = 0
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if price(item, inv + mid) >= floor_price:
            lo = mid
        else:
            hi = mid - 1
    return lo


def drain_rate(town):
    """Units per step the town removes from the market, per product."""
    rate = dict.fromkeys(PRODUCTS, 0.0)
    for shop in (_get(town, "unlocked_shops", []) or []):
        prods = SHOPS.get(shop)
        if not prods:
            continue
        mult = 2.0 if len(prods) == 1 else 1.0
        for item in prods:
            rate[item] += mult / 4.0
    for item in TOWN_CENTER:
        rate[item] += 1.0 / 24.0
    return rate


# --------------------------------------------------------------------------
# valuation
# --------------------------------------------------------------------------
def _fib(n):
    a, b = 1, 1
    for _ in range(int(max(0, n))):
        a, b = b, a + b
    return a


def crop_plan(day, days_left, unit_price):
    """(score, crop) for every crop that can still finish; score = $ per action."""
    out = []
    for crop, cd in CROPS.items():
        p = unit_price(crop)
        if cd["ong"]:
            n = 0
            span = 0
            for k in range(cd["my"]):
                d = cd["fyd"] + k * max(1, cd["iv"])
                if d <= days_left:
                    n, span = n + 1, d
            if n <= 0:
                continue
            units, actions = n, 1 + span
        else:
            if cd["myd"] > days_left:
                continue
            waters = cd["myd"] - (cd["myd"] + 1) // 2 + 1
            units = min(cd["my"], 1 + waters)
            actions = 2 + waters
            span = cd["myd"]
        gain = units * p - cd["seed"]
        if gain <= 0:
            continue
        out.append((gain / float(actions), crop, units, span))
    out.sort(reverse=True)
    return out


def animal_plan(day, days_left, unit_price, wheat_cost):
    out = []
    for name, a in ANIMALS.items():
        if a["fyd"] > days_left:
            continue
        n_prod = 0
        d = a["fyd"]
        while d <= days_left:
            n_prod += 1
            d += max(1, a["iv"])
        units = n_prod * 2                      # fed + cared => 2 per production
        feed_days = max(0, days_left)
        gain = units * unit_price(a["prod"]) - a["cost"] - feed_days * wheat_cost
        out.append((gain, name, a["st"]))
    out.sort(reverse=True)
    return out


# --------------------------------------------------------------------------
# geometry
# --------------------------------------------------------------------------
def shed_tiles():
    h = BOARD // 2
    return [(h - 1, h - 1), (h, h - 1), (h - 1, h), (h, h)]


SHED_SET = set(shed_tiles())


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def step_toward(pos, target):
    dx, dy = target[0] - pos[0], target[1] - pos[1]
    if abs(dx) >= abs(dy):
        if dx > 0:
            return ["EAST"]
        if dx < 0:
            return ["WEST"]
    if dy > 0:
        return ["SOUTH"]
    if dy < 0:
        return ["NORTH"]
    return ["PASS"]


# --------------------------------------------------------------------------
# the policy
# --------------------------------------------------------------------------
def agent(obs, config=None):
    try:
        return _plan(obs)
    except Exception:
        farm = (list(_get(obs, "farms", []) or []) + [{}])[_seat(obs)]
        n = len(_get(farm, "hands", []) or [])
        return {"farmer": ["PASS"], "hands": [["PASS"]] * n, "market": []}


def _plan(obs):
    seat = _seat(obs)
    step = int(_get(obs, "step", 0) or 0)
    day = step // TPD
    hour = step % TPD
    days_left = max(0, 29 - day)
    steps_left = max(0, 719 - step)

    farms = list(_get(obs, "farms", []) or [])
    farm = farms[seat] if seat < len(farms) else {}
    money = float(_get(farm, "money", 0) or 0)
    tiles = _get(farm, "tiles", []) or []
    hands = list(_get(farm, "hands", []) or [])
    hires_today = int(_get(farm, "hires_today", 0) or 0)

    private = _get(obs, "private", {}) or {}
    shed = dict(_get(private, "shed", {}) or {})
    seeds = dict(_get(private, "seeds", {}) or {})
    invs = list(_get(private, "inventories", []) or [{}])

    market = _get(obs, "market", {}) or {}
    minv = {k: int(v or 0) for k, v in (_get(market, "inventory", {}) or {}).items()}
    town = _get(obs, "town", {}) or {}
    rate = drain_rate(town)

    shed_used = sum(int(v or 0) for v in shed.values())

    # ---- price floor schedule -------------------------------------------
    if step >= DUMP_STEP:
        hold = 0.0
    elif day < RELAX_DAY:
        hold = HOLD_EARLY
    else:
        t = (day - RELAX_DAY) / float(max(1, 29 - RELAX_DAY))
        hold = HOLD_EARLY + (HOLD_LATE - HOLD_EARLY) * t
    if shed_used > SHED_SOFT:                    # overflow risk beats price
        hold = min(hold, 0.45)

    def sale_price(item):
        """Marginal price we expect to realise for one more unit."""
        return price(item, minv.get(item, I0))

    def plan_price(item):
        """Price used for PRODUCTION decisions: what the drain can absorb."""
        absorbed = rate.get(item, 0.0) * steps_left
        return price(item, max(I0 - 400, minv.get(item, I0) - absorbed * 0.5))

    # ---- scan the board --------------------------------------------------
    plants, animals, empties, weeds, structs = [], [], [], [], []
    for y in range(min(BOARD, len(tiles))):
        row = tiles[y] or []
        for x in range(min(BOARD, len(row))):
            t = row[x]
            if t == "LOCKED" or t is None:
                if t is None:
                    empties.append((x, y))
                continue
            if not isinstance(t, dict):
                continue
            kind = t.get("kind")
            if kind == "PLANT":
                plants.append((x, y, t))
            elif "animal" in t:
                animals.append((x, y, t))
            elif kind == "WEED":
                weeds.append((x, y))
            elif kind in ("COOP", "PASTURE"):
                structs.append((x, y, kind))

    # ---- what to grow / raise -------------------------------------------
    crops = crop_plan(day, days_left, plan_price)
    best_crop = crops[0][1] if crops else None
    wheat_cost = price("WHEAT", minv.get("WHEAT", I0) - 1)
    beasts = animal_plan(day, days_left, plan_price, wheat_cost)
    best_beast = beasts[0] if beasts and beasts[0][0] > 0 else None

    # ---- job board -------------------------------------------------------
    # (value, target, op, needs)  -- needs: None | ("WHEAT",) | ("ANIMAL", name)
    jobs = []

    for x, y, t in animals:
        a = ANIMALS.get(t.get("animal"), None)
        if a is None:
            continue
        p = sale_price(a["prod"])
        held = int(t.get("yield_units", 0) or 0)
        if held > 0:
            jobs.append((held * p, (x, y), ["HARVEST"], None))
        if not t.get("fed_today"):
            # unfed twice => the animal escapes; that is the whole future stream
            urgency = 4.0 if int(t.get("consecutive_unfed", 0) or 0) >= 1 else 1.0
            jobs.append((urgency * 2 * p, (x, y), ["FEED"], ("WHEAT",)))
        if t.get("fed_today") and not t.get("cared_today"):
            jobs.append((0.9 * p, (x, y), ["CARE"], None))

    for x, y, t in plants:
        crop = t.get("crop")
        cd = CROPS.get(crop)
        if cd is None:
            continue
        p = sale_price(crop)
        age = day - int(t.get("planted_day", day) or 0)
        held = int(t.get("yield_units", 0) or 0)
        ripe = held > 0 and age >= cd["fyd"]
        if ripe:
            # non-ongoing crops free the tile; ongoing ones keep producing
            jobs.append((held * p + (12 if not cd["ong"] else 0),
                         (x, y), ["HARVEST"], None))
        if not t.get("watered_today"):
            if cd["ong"]:
                gain = p                       # one more unit at the next tick
            else:
                w0 = (cd["myd"] + 1) // 2
                gain = p if w0 <= age <= cd["myd"] else 0.0
            # a plant that misses today dies tonight -> the whole tile is lost
            if int(t.get("consecutive_unwatered", 0) or 0) >= 1:
                gain += 2.0 * p * max(1, cd["my"] - held)
            if gain > 0:
                jobs.append((gain, (x, y), ["WATER"], None))

    if best_beast is not None:
        want_struct = best_beast[2]
        free_struct = [(x, y) for x, y, k in structs if k == want_struct]
        held_animals = [k for k in ANIMALS if shed.get(k, 0) > 0]
        for x, y in free_struct:
            if held_animals:
                jobs.append((best_beast[0] / 10.0, (x, y),
                             ["PLACE", held_animals[0]], ("ANIMAL", held_animals[0])))
        # build more housing while there is payback time left
        if len(free_struct) < 2 and best_beast[0] > 0:
            op = "BUILD_COOP" if want_struct == "COOP" else "BUILD_PASTURE"
            for x, y in empties[:3]:
                jobs.append((best_beast[0] / 14.0, (x, y), [op], None))

    if best_crop is not None:
        score = crops[0][0]
        for x, y in empties:
            if seeds.get(best_crop, 0) > 0:
                jobs.append((score * 3.0, (x, y), ["PLANT", best_crop], None))

    for x, y in weeds:
        if days_left >= 4:
            jobs.append((6.0, (x, y), ["DIG"], None))

    jobs.sort(key=lambda j: -j[0])

    # ---- assign units ----------------------------------------------------
    units = [(0, list(_get(farm, "farmer", [4, 4]) or [4, 4]))]
    for i, pos in enumerate(hands):
        units.append((i + 1, list(pos or [4, 4])))

    acts = {}
    claimed = set()
    # PLANT is validated atomically: over-requesting a crop drops ALL of them
    seed_budget = dict(seeds)

    for idx, pos in units:
        inv = invs[idx] if idx < len(invs) else {}
        inv = dict(inv or {})
        p = (int(pos[0]), int(pos[1]))
        best = None
        for value, tgt, op, needs in jobs:
            if tgt in claimed:
                continue
            if op[0] == "FEED" and inv.get("WHEAT", 0) <= 0:
                continue
            if op[0] == "PLACE" and inv.get(op[1], 0) <= 0:
                continue
            if op[0] == "PLANT" and seed_budget.get(op[1], 0) <= 0:
                continue
            d = dist(p, tgt)
            if d > steps_left:
                continue
            score = value / float(1 + d)
            if best is None or score > best[0]:
                best = (score, tgt, op, d)
        # nothing productive: fetch what unlocks the blocked jobs
        if best is None:
            need_wheat = any(o[0] == "FEED" for _, _, o, _ in jobs)
            need_beast = any(o[0] == "PLACE" for _, _, o, _ in jobs)
            tgt = min(SHED_SET, key=lambda s: dist(p, s))
            if p in SHED_SET and need_wheat and shed.get("WHEAT", 0) > 0:
                take = min(FEED_CARRY, shed.get("WHEAT", 0))
                shed["WHEAT"] -= take
                acts[idx] = ["PICKUP", "WHEAT", take]
                continue
            if p in SHED_SET and need_beast:
                got = next((k for k in ANIMALS if shed.get(k, 0) > 0), None)
                if got:
                    shed[got] -= 1
                    acts[idx] = ["PICKUP", got, 1]
                    continue
            if (need_wheat and shed.get("WHEAT", 0) > 0) or need_beast:
                acts[idx] = step_toward(p, tgt)
                continue
            if inv and p in SHED_SET:
                acts[idx] = ["DROP"]
                continue
            acts[idx] = step_toward(p, tgt) if inv else ["PASS"]
            continue

        _, tgt, op, d = best
        claimed.add(tgt)
        if d == 0:
            if op[0] == "PLANT":
                seed_budget[op[1]] = seed_budget.get(op[1], 0) - 1
            acts[idx] = list(op)
        else:
            acts[idx] = step_toward(p, tgt)

    # ---- market orders ---------------------------------------------------
    orders = []

    # 1. hire in the morning; a hand costs fib(n) once and works ~24 turns
    if hour <= 1 and days_left >= 1:
        want = MAX_HANDS if day >= 2 else min(MAX_HANDS, 6 + 2 * day)
        budget = money * 0.25
        spent = 0.0
        n = hires_today
        while n < want and len(orders) < 9:
            c = _fib(n)
            if c > budget - spent or c > money * 0.5:
                break
            orders.append(["HIRE"])
            spent += c
            n += 1

    reserve = 250.0
    cash = money

    # 2. land: more tiles only pay while there is a full crop cycle left
    owned_extra = len(_get(farm, "unlocked_quadrants", ["NW"]) or ["NW"]) - 1
    if owned_extra < 3 and days_left >= 8 and len(orders) < 10:
        c = LAND_PRICES[owned_extra]
        if cash - c >= reserve + 400 and len(empties) <= 6:
            orders.append(["BUY_LAND"])
            cash -= c

    # 3. seeds for the tiles we can actually work
    if best_crop and len(orders) < 10:
        want = min(14, len(empties) + 4)
        have = seeds.get(best_crop, 0)
        need = max(0, want - have)
        c = CROPS[best_crop]["seed"]
        afford = int(max(0, (cash - reserve)) // c)
        n = min(need, afford)
        if n > 0:
            orders.append(["BUY_SEED", best_crop, n])
            cash -= n * c

    # 4. wheat for feed -- animals starve in 2 days and the structure empties
    n_animals = len(animals)
    if n_animals and len(orders) < 10:
        want = max(0, n_animals * 2 - shed.get("WHEAT", 0))
        room = max(0, SHED_CAP - shed_used - 4)
        n = min(want, room, int(max(0, (cash - reserve)) // max(1, wheat_cost)))
        if n > 0:
            orders.append(["BUY_PRODUCT", "WHEAT", n])
            cash -= n * wheat_cost

    # 5. livestock -- deliberately late: the shop draw is only known by day 3+
    if best_beast is not None and len(orders) < 10 and day >= 2:
        name = best_beast[1]
        want_struct = ANIMALS[name]["st"]
        slots = sum(1 for _, _, k in structs if k == want_struct)
        pending = sum(shed.get(k, 0) for k in ANIMALS)
        if slots > pending and cash - ANIMALS[name]["cost"] >= reserve:
            if shed_used < SHED_CAP - 2:
                orders.append(["BUY_ANIMAL", name, 1])
                cash -= ANIMALS[name]["cost"]

    # 6. sell -- size each order so the LAST unit still clears the floor
    sellable = []
    for item, qty in shed.items():
        qty = int(qty or 0)
        if qty <= 0 or item not in MP:
            continue
        sellable.append((sale_price(item) * qty, item, qty))
    sellable.sort(reverse=True)

    inv_sim = dict(minv)
    for _, item, qty in sellable:
        if len(orders) >= 10:
            break
        floor_price = max(1.0, hold * MP[item]["base"])
        n = qty if hold <= 0.0 else min(qty, sell_cap(item, inv_sim.get(item, I0),
                                                      floor_price))
        if n <= 0:
            continue
        orders.append(["SELL", item, int(n)])
        inv_sim[item] = inv_sim.get(item, I0) + int(n)

    return {
        "farmer": list(acts.get(0, ["PASS"])),
        "hands": [list(acts.get(i + 1, ["PASS"])) for i in range(len(hands))],
        "market": orders[:10],
    }


if __name__ == "__main__":
    # smallest check that fails if the policy stops emitting legal actions
    from kaggle_environments import make
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": 7})
    env.run([agent, "random"])
    last = env.steps[-1]
    assert last[0].status == "DONE", last[0].status
    print("g1 vs random:", int(last[0].reward), "-", int(last[1].reward))
