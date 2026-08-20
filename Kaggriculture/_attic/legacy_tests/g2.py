"""g2 -- pure adaptive policy for Kaggriculture.  No replay tape, no cloned route.

The principle
-------------
Score is money, and money is bounded by what the MARKET ABSORBS, not by what
the farm grows.  Absorption is set by the town: each unlocked shop drains its
products every 4 steps, and the town centre drains one of everything every 24.
Shops are drawn at random per seed and revealed every 3 days in
`obs.town.unlocked_shops`.

So the profitable product mix is a per-seed random variable, observable only
during the episode.  A fixed action tape cannot react to it.  This policy can:

  1. read the drain implied by the shops seen so far,
  2. project our own future supply from what is already planted/placed,
  3. price the marginal unit at (drain - supply) and rank every production
     option -- crop, animal, land, hand -- on dollars per action,
  4. size each sell order so its last unit still clears a price floor.

Nothing here is derived from an opponent trajectory.
"""

import math

BOARD = 10
TPD = 24
I0 = 10000
LAST_DAY = 29
LAST_STEP = 719

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
MAX_SHOPS = 8

MAX_HANDS = 14
HOLD_EARLY = 0.88
HOLD_LATE = 0.20
RELAX_DAY = 21
DUMP_STEP = 700
SHED_SOFT = 55
FEED_CARRY = 6
RESERVE = 120.0


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
    return max(1, int(round(v)))


def sell_cap(item, inv, floor_price, hi=400):
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


def _fib(n):
    a, b = 1, 1
    for _ in range(int(max(0, n))):
        a, b = b, a + b
    return a


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
def agent(obs, config=None):
    try:
        return _plan(obs)
    except Exception:
        farms = list(_get(obs, "farms", []) or [])
        seat = _seat(obs)
        farm = farms[seat] if seat < len(farms) else {}
        n = len(_get(farm, "hands", []) or [])
        return {"farmer": ["PASS"], "hands": [["PASS"]] * n, "market": []}


def _plan(obs):
    seat = _seat(obs)
    step = int(_get(obs, "step", 0) or 0)
    day, hour = step // TPD, step % TPD
    days_left = max(0, LAST_DAY - day)
    steps_left = max(0, LAST_STEP - step)

    farms = list(_get(obs, "farms", []) or [])
    farm = farms[seat] if seat < len(farms) else {}
    money = float(_get(farm, "money", 0) or 0)
    tiles = _get(farm, "tiles", []) or []
    hands = list(_get(farm, "hands", []) or [])
    hires_today = int(_get(farm, "hires_today", 0) or 0)
    quads = list(_get(farm, "unlocked_quadrants", ["NW"]) or ["NW"])

    private = _get(obs, "private", {}) or {}
    shed = {k: int(v or 0) for k, v in (_get(private, "shed", {}) or {}).items()}
    seeds = {k: int(v or 0) for k, v in (_get(private, "seeds", {}) or {}).items()}
    invs = list(_get(private, "inventories", []) or [{}])

    market = _get(obs, "market", {}) or {}
    minv = {k: int(v or 0) for k, v in (_get(market, "inventory", {}) or {}).items()}
    town = _get(obs, "town", {}) or {}
    shops = list(_get(town, "unlocked_shops", []) or [])
    shed_used = sum(shed.values())

    # ---- board scan ------------------------------------------------------
    plants, beasts, empties, weeds, structs = [], [], [], [], []
    for y in range(min(BOARD, len(tiles))):
        row = tiles[y] or []
        for x in range(min(BOARD, len(row))):
            t = row[x]
            if t is None:
                empties.append((x, y))
                continue
            if not isinstance(t, dict):
                continue
            kind = t.get("kind")
            if kind == "PLANT":
                plants.append((x, y, t))
            elif "animal" in t:
                beasts.append((x, y, t))
            elif kind == "WEED":
                weeds.append((x, y))
            elif kind in ("COOP", "PASTURE"):
                structs.append((x, y, kind))

    # ---- absorption: observed drain, plus the shops still to be drawn ----
    def drain_of(shop_list, steps):
        r = dict.fromkeys(PRODUCTS, 0.0)
        for s in shop_list:
            prods = SHOPS.get(s)
            if not prods:
                continue
            mult = 2.0 if len(prods) == 1 else 1.0
            for it in prods:
                r[it] += mult * steps / 4.0
        for it in TOWN_CENTER:
            r[it] += steps / 24.0
        return r

    absorb = drain_of(shops, steps_left)
    # unknown future shops: every shop is equally likely, so credit the mean
    未 = max(0, min(MAX_SHOPS, (LAST_DAY // 3)) - len(shops))
    if 未 > 0:
        mean = dict.fromkeys(PRODUCTS, 0.0)
        for s in SHOPS:
            prods = SHOPS[s]
            mult = 2.0 if len(prods) == 1 else 1.0
            for it in prods:
                mean[it] += mult / (4.0 * len(SHOPS))
        # they arrive spread over the remaining unlock days -> ~half the window
        for it in PRODUCTS:
            absorb[it] += mean[it] * 未 * steps_left * 0.5

    # ---- our own future supply, from what already exists ------------------
    supply = dict.fromkeys(PRODUCTS, 0.0)
    for it, n in shed.items():
        if it in supply:
            supply[it] += n
    for _, _, t in plants:
        cd = CROPS.get(t.get("crop"))
        if not cd:
            continue
        age = day - int(t.get("planted_day", day) or 0)
        left = max(0, cd["my"] - int(t.get("yield_units", 0) or 0))
        supply[t["crop"]] += int(t.get("yield_units", 0) or 0) + min(left, days_left)
    for _, _, t in beasts:
        a = ANIMALS.get(t.get("animal"))
        if not a:
            continue
        n = 0
        d = a["fyd"] - (day - int(t.get("placed_day", day) or 0))
        d = max(0, d)
        while d <= days_left:
            n += 1
            d += max(1, a["iv"])
        supply[a["prod"]] += int(t.get("yield_units", 0) or 0) + 2 * n

    def plan_price(item):
        """Marginal price for one more unit of planned production."""
        over = max(0.0, supply.get(item, 0.0) - absorb.get(item, 0.0))
        return price(item, int(minv.get(item, I0) + over))

    def spot(item):
        return price(item, minv.get(item, I0))

    wheat_buy = price("WHEAT", minv.get("WHEAT", I0) - 1)

    # ---- rank the production options -------------------------------------
    crop_opts = []
    for crop, cd in CROPS.items():
        p = plan_price(crop)
        if cd["ong"]:
            n, span = 0, 0
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
            units, actions = min(cd["my"], 1 + waters), 2 + waters
        gain = units * p - cd["seed"]
        if gain > 0:
            crop_opts.append((gain / float(actions), gain, crop))
    crop_opts.sort(reverse=True)
    best_crop = crop_opts[0][2] if crop_opts else None
    best_crop_gain = crop_opts[0][1] if crop_opts else 0.0

    beast_opts = []
    for name, a in ANIMALS.items():
        if a["fyd"] > days_left:
            continue
        n, d = 0, a["fyd"]
        while d <= days_left:
            n += 1
            d += max(1, a["iv"])
        units = 2 * n
        feed = max(0, days_left) * wheat_buy
        gain = units * plan_price(a["prod"]) - a["cost"] - feed
        beast_opts.append((gain, name, a["st"]))
    beast_opts.sort(reverse=True)
    best_beast = beast_opts[0] if beast_opts and beast_opts[0][0] > 0 else None

    # ---- price floor ------------------------------------------------------
    if step >= DUMP_STEP:
        hold = 0.0
    elif day < RELAX_DAY:
        hold = HOLD_EARLY
    else:
        t = (day - RELAX_DAY) / float(max(1, LAST_DAY - RELAX_DAY))
        hold = HOLD_EARLY + (HOLD_LATE - HOLD_EARLY) * t
    if shed_used > SHED_SOFT:
        hold = min(hold, 0.40)

    # ---- job board --------------------------------------------------------
    # entry: (value, (x, y), op, require)  require in {None,"WHEAT",animal name}
    jobs = []
    unfed = 0

    for x, y, t in beasts:
        a = ANIMALS.get(t.get("animal"))
        if not a:
            continue
        p = spot(a["prod"])
        held = int(t.get("yield_units", 0) or 0)
        if held > 0:
            jobs.append((held * p, (x, y), ["HARVEST"], None))
        if not t.get("fed_today"):
            unfed += 1
            starving = int(t.get("consecutive_unfed", 0) or 0) >= 1
            v = (6.0 if starving else 1.0) * 2 * p
            jobs.append((v, (x, y), ["FEED"], "WHEAT"))
        elif not t.get("cared_today"):
            jobs.append((0.95 * p, (x, y), ["CARE"], None))

    for x, y, t in plants:
        cd = CROPS.get(t.get("crop"))
        if not cd:
            continue
        p = spot(t["crop"])
        age = day - int(t.get("planted_day", day) or 0)
        held = int(t.get("yield_units", 0) or 0)
        if held > 0 and age >= cd["fyd"]:
            jobs.append((held * p + (14 if not cd["ong"] else 0),
                         (x, y), ["HARVEST"], None))
        if not t.get("watered_today"):
            if cd["ong"]:
                gain = float(p)
            else:
                w0 = (cd["myd"] + 1) // 2
                gain = float(p) if w0 <= age <= cd["myd"] else 0.0
            if int(t.get("consecutive_unwatered", 0) or 0) >= 1:
                gain += 2.5 * p * max(1, cd["my"] - held)   # dies tonight otherwise
            if gain > 0:
                jobs.append((gain, (x, y), ["WATER"], None))

    # placing livestock is the highest-leverage act in the game -- make it a
    # first-class job, not an idle fallback
    carried = {}
    for i in range(len(invs)):
        for k in ANIMALS:
            if int((invs[i] or {}).get(k, 0) or 0) > 0:
                carried[k] = carried.get(k, 0) + 1
    free_struct = {}
    for x, y, k in structs:
        free_struct.setdefault(k, []).append((x, y))

    for name in ANIMALS:
        st = ANIMALS[name]["st"]
        slots = free_struct.get(st, [])
        if not slots:
            continue
        if carried.get(name, 0) <= 0 and shed.get(name, 0) <= 0:
            continue
        gain = next((g for g, n, _ in beast_opts if n == name), 0.0)
        for x, y in slots[:6]:
            jobs.append((max(400.0, gain), (x, y), ["PLACE", name], name))

    # housing: build ahead of the animals we intend to buy
    if best_beast is not None:
        want_st = best_beast[2]
        have = len(free_struct.get(want_st, []))
        pending = shed.get(best_beast[1], 0) + carried.get(best_beast[1], 0)
        short = max(0, min(len(empties), 6) - have) if best_beast[0] > 0 else 0
        if have < pending + 4 and short > 0:
            op = "BUILD_COOP" if want_st == "COOP" else "BUILD_PASTURE"
            per = best_beast[0] / 12.0
            for x, y in sorted(empties, key=lambda e: dist(e, (4, 4)))[:short]:
                jobs.append((per, (x, y), [op], None))

    if best_crop and seeds.get(best_crop, 0) > 0:
        per = best_crop_gain / 4.0
        for x, y in empties:
            jobs.append((per, (x, y), ["PLANT", best_crop], None))

    if days_left >= 3:
        wv = max(best_crop_gain / 8.0, (best_beast[0] / 10.0) if best_beast else 0.0)
        for x, y in weeds:
            jobs.append((max(8.0, wv), (x, y), ["DIG"], None))

    # shed errands: fetch feed and fetch livestock
    if unfed and shed.get("WHEAT", 0) > 0:
        v = 0.0
        for value, _, op, req in jobs:
            if op[0] == "FEED":
                v = max(v, value)
        for s in shed_tiles():
            jobs.append((v * 0.9, s, ["PICKUP", "WHEAT", 0], None))
    for name in ANIMALS:
        if shed.get(name, 0) > 0 and free_struct.get(ANIMALS[name]["st"]):
            gain = next((g for g, n, _ in beast_opts if n == name), 400.0)
            for s in shed_tiles():
                jobs.append((max(400.0, gain) * 0.9, s, ["PICKUP", name, 1], None))

    jobs.sort(key=lambda j: -j[0])
    jobs = jobs[:220]

    # ---- global greedy assignment ----------------------------------------
    units = [(0, tuple(_get(farm, "farmer", [4, 4]) or [4, 4]))]
    for i, pos in enumerate(hands):
        units.append((i + 1, tuple(pos or [4, 4])))

    pairs = []
    for idx, pos in units:
        inv = dict(invs[idx] or {}) if idx < len(invs) else {}
        holding = next((k for k in ANIMALS if inv.get(k, 0) > 0), None)
        for j, (value, tgt, op, req) in enumerate(jobs):
            if holding and op[0] not in ("PLACE", "BUILD_COOP", "BUILD_PASTURE"):
                continue          # deliver the animal first, it is worth ~$3k
            if holding and op[0] == "PLACE" and op[1] != holding:
                continue
            if op[0] == "PLACE" and not holding:
                continue
            if req == "WHEAT" and inv.get("WHEAT", 0) <= 0:
                continue
            if op[0] == "PICKUP" and holding:
                continue
            d = dist(pos, tgt)
            if d > steps_left:
                continue
            pairs.append((value / float(1 + d), idx, j, d))
    pairs.sort(reverse=True)

    acts, taken_unit, taken_job = {}, set(), set()
    seed_budget = dict(seeds)
    shed_left = dict(shed)
    for _score, idx, j, d in pairs:
        if idx in taken_unit or j in taken_job:
            continue
        value, tgt, op, req = jobs[j]
        op = list(op)
        if op[0] == "PLANT":
            if seed_budget.get(op[1], 0) <= 0:
                continue
        if op[0] == "PICKUP":
            avail = shed_left.get(op[1], 0)
            if avail <= 0:
                continue
        taken_unit.add(idx)
        taken_job.add(j)
        pos = dict(units)[idx]
        if d == 0:
            if op[0] == "PLANT":
                seed_budget[op[1]] -= 1
            if op[0] == "PICKUP":
                n = min(FEED_CARRY, shed_left.get(op[1], 0)) if op[1] == "WHEAT" else 1
                shed_left[op[1]] = shed_left.get(op[1], 0) - n
                op = ["PICKUP", op[1], int(n)]
            acts[idx] = op
        else:
            if op[0] == "PICKUP":
                shed_left[op[1]] = shed_left.get(op[1], 0) - (
                    FEED_CARRY if op[1] == "WHEAT" else 1)
            acts[idx] = step_toward(pos, tgt)

    # idle units: unload, else drift to the shed so they start tomorrow close in
    for idx, pos in units:
        if idx in acts:
            continue
        inv = dict(invs[idx] or {}) if idx < len(invs) else {}
        if inv and pos in SHED_SET and shed_used < SHED_CAP:
            acts[idx] = ["DROP"]
        elif inv:
            acts[idx] = step_toward(pos, min(SHED_SET, key=lambda s: dist(pos, s)))
        else:
            acts[idx] = ["PASS"]

    # ---- market -----------------------------------------------------------
    orders = []
    cash = money

    if hour <= 1 and days_left >= 1:
        want = MAX_HANDS if day >= 3 else 4 + 3 * day
        n = hires_today
        while n < want and len(orders) < 8:
            c = _fib(n)
            if c > cash * 0.30:
                break
            orders.append(["HIRE"])
            cash -= c
            n += 1

    owned_extra = len(quads) - 1
    if owned_extra < 3 and days_left >= 7 and len(orders) < 10:
        c = LAND_PRICES[owned_extra]
        crowded = len(empties) <= max(3, len(hands))
        if crowded and cash - c >= RESERVE:
            orders.append(["BUY_LAND"])
            cash -= c

    # livestock first call on cash once the shop draw is informative
    if best_beast is not None and len(orders) < 10:
        name, cost = best_beast[1], ANIMALS[best_beast[1]]["cost"]
        st = ANIMALS[name]["st"]
        slots = len(free_struct.get(st, []))
        pending = shed.get(name, 0) + carried.get(name, 0)
        room = SHED_CAP - shed_used - 2
        n = min(max(0, slots - pending), int(max(0, cash - RESERVE) // cost), 4)
        if n > 0 and room > n:
            orders.append(["BUY_ANIMAL", name, int(n)])
            cash -= n * cost

    if best_crop and len(orders) < 10:
        c = CROPS[best_crop]["seed"]
        want = min(16, len(empties) + len(weeds) + 2)
        need = max(0, want - seeds.get(best_crop, 0))
        n = min(need, int(max(0, cash - RESERVE) // c))
        if n > 0:
            orders.append(["BUY_SEED", best_crop, int(n)])
            cash -= n * c

    n_beasts = len(beasts)
    if n_beasts and len(orders) < 10:
        want = max(0, n_beasts * 2 - shed.get("WHEAT", 0))
        room = max(0, SHED_CAP - shed_used - 4)
        n = min(want, room, int(max(0, cash - RESERVE) // max(1, wheat_buy)))
        if n > 0:
            orders.append(["BUY_PRODUCT", "WHEAT", int(n)])
            cash -= n * wheat_buy

    keep_wheat = 0 if step >= DUMP_STEP else min(shed.get("WHEAT", 0), n_beasts * 2)
    rows = []
    for item, qty in shed.items():
        if item not in MP or qty <= 0:
            continue
        if item == "WHEAT":
            qty -= keep_wheat
        if qty > 0:
            rows.append((spot(item) * qty, item, qty))
    rows.sort(reverse=True)

    sim = dict(minv)
    for _v, item, qty in rows:
        if len(orders) >= 10:
            break
        if hold <= 0.0:
            n = qty
        else:
            n = min(qty, sell_cap(item, sim.get(item, I0),
                                  max(1.0, hold * MP[item]["base"])))
        if n <= 0:
            continue
        orders.append(["SELL", item, int(n)])
        sim[item] = sim.get(item, I0) + int(n)

    return {
        "farmer": list(acts.get(0, ["PASS"])),
        "hands": [list(acts.get(i + 1, ["PASS"])) for i in range(len(hands))],
        "market": orders[:10],
    }


if __name__ == "__main__":
    from kaggle_environments import make
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": 7})
    env.run([agent, agent])
    last = env.steps[-1]
    assert last[0].status == "DONE", last[0].status
    print("g2 mirror:", int(last[0].reward), int(last[1].reward))
