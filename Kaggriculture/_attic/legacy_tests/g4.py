"""g4 -- pure adaptive policy for Kaggriculture.  No replay tape, no cloned route.

g3 + the six diagnosed fixes from HANDOFF.md §5.  Every one of them came out of
a `_gdiag.py` trace, none are speculative:

  1. FEED_CARRY 6 -> 3, and the PICKUP is sized to the animals still actually
     unfed.  g3 did 212 pickups for 103 feeds; the surplus rode in unit
     inventories until dusk, got dumped to the shed, and overflowed the 100 cap
     into nothing.
  2. Wheat purchases capped at n_beasts per turn and skipped outright once the
     quote passes WHEAT_BUY_MAX.  Unbounded top-ups bought 1,722 wheat and
     bankrupted g3 ($3,925 final).
  3. While the herd is short of feed, WHEAT is valued at REPLACEMENT cost, not
     sale price -- so the tile allocator grows feed instead of buying it into a
     rising price.
  4. Workforce sized to the farm, not the calendar.  g2 hired 14 hands/day
     ($986) on a schedule and sat at $3-$50 from day 12 to 25.
  5. Working capital reserve is feed-only, and the spend order is
     wages -> animals -> seeds -> wheat top-up.  g3's fat reserve meant animals
     never got bought.
  6. Crops are valued over every cycle a tile can complete in the days left.  A
     wheat tile finishes ~5 cycles a season, a melon tile 2; counting one cycle
     undervalues fast crops and let melon monopolise the board.

The principle (unchanged from g3)
---------------------------------
Score is money, and money is bounded by what the MARKET ABSORBS, not by what
the farm grows.  Absorption is set by the town: each unlocked shop drains its
products every 4 steps, the town centre drains one of everything every 24, and
the shops are drawn at random per seed, revealed every 3 days in
`obs.town.unlocked_shops`.  A fixed action tape cannot see that draw; this
policy is built entirely around reacting to it.

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

MIN_HANDS = 3
MAX_HANDS = 14
TILES_PER_HAND = 9.0     # fix 4: farm workload one unit keeps up with
HOLD_EARLY = 0.86
HOLD_LATE = 0.18
RELAX_DAY = 22
DUMP_STEP = 700
SHED_SOFT = 55
FEED_CARRY = 3           # fix 1: was 6; surplus is destroyed at the dusk cap
FEED_DAYS = 3            # days of feed kept in the shed, never sold
WHEAT_BUY_MAX = 45       # fix 2: above this, grow it instead of buying it


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


def hire_bill(n):
    return sum(_fib(i) for i in range(max(0, n)))


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


def crop_yield(cd, days_left):
    """(units, tile-actions, days occupied) for ONE cycle started now."""
    if cd["ong"]:
        n, span = 0, 0
        for k in range(cd["my"]):
            d = cd["fyd"] + k * max(1, cd["iv"])
            if d <= days_left:
                n, span = n + 1, d
        if n <= 0:
            return None
        return n, 1 + span, span
    if cd["myd"] > days_left:
        return None
    waters = cd["myd"] - (cd["myd"] + 1) // 2 + 1
    return min(cd["my"], 1 + waters), 2 + waters, cd["myd"]


def crop_season(cd, days_left):
    """Fix 6: (units, actions, seed spend) over EVERY cycle the tile can finish.

    A wheat tile (myd 4) completes ~5 cycles in 20 days, a melon tile (myd 12)
    only 1-2.  Pricing one cycle made melon look like the best tile on the
    board and starved the opening of cash.
    """
    y = crop_yield(cd, days_left)
    if not y:
        return None
    units, actions, span = y
    cycles = 1 if cd["ong"] else max(1, int(days_left // max(1, cd["myd"])))
    return units * cycles, actions * cycles, float(cd["seed"]) * cycles


def animal_yield(a, days_left):
    """(units, tile-actions, days) assuming fed + cared every day."""
    if a["fyd"] > days_left:
        return None
    n, d = 0, a["fyd"]
    while d <= days_left:
        n += 1
        d += max(1, a["iv"])
    actions = 2.0 * days_left + n * 2.0 / max(1, a["mh"])
    return 2 * n, actions, a["fyd"]


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
    n_beasts = len(beasts)

    # ---- absorption -------------------------------------------------------
    absorb = dict.fromkeys(PRODUCTS, 0.0)
    for s in shops:
        prods = SHOPS.get(s)
        if not prods:
            continue
        mult = 2.0 if len(prods) == 1 else 1.0
        for it in prods:
            absorb[it] += mult * steps_left / 4.0
    for it in TOWN_CENTER:
        absorb[it] += steps_left / 24.0
    unknown = max(0, min(MAX_SHOPS, LAST_DAY // 3) - len(shops))
    if unknown > 0:
        for s in SHOPS:
            prods = SHOPS[s]
            mult = 2.0 if len(prods) == 1 else 1.0
            for it in prods:
                absorb[it] += mult * unknown * steps_left * 0.5 / (4.0 * len(SHOPS))

    # ---- our own committed future supply ----------------------------------
    supply = dict.fromkeys(PRODUCTS, 0.0)
    for it, n in shed.items():
        if it in supply:
            supply[it] += n
    for _, _, t in plants:
        cd = CROPS.get(t.get("crop"))
        if not cd:
            continue
        held = int(t.get("yield_units", 0) or 0)
        supply[t["crop"]] += held + min(max(0, cd["my"] - held), days_left + 1)
    for _, _, t in beasts:
        a = ANIMALS.get(t.get("animal"))
        if not a:
            continue
        age = day - int(t.get("placed_day", day) or 0)
        d, n = max(0, a["fyd"] - age), 0
        while d <= days_left:
            n += 1
            d += max(1, a["iv"])
        supply[a["prod"]] += int(t.get("yield_units", 0) or 0) + 2 * n

    def marginal(item, extra=0.0):
        over = max(0.0, supply.get(item, 0.0) + extra - absorb.get(item, 0.0))
        return price(item, int(minv.get(item, I0) + over))

    def spot(item):
        return price(item, minv.get(item, I0))

    wheat_buy = price("WHEAT", minv.get("WHEAT", I0) - 1)

    # fix 3: feed we are short of is worth what it costs to replace, not what
    # it sells for.  Otherwise the allocator sells wheat and re-buys it dearer.
    feed_target = n_beasts * FEED_DAYS
    wheat_short = shed.get("WHEAT", 0) < feed_target

    def tile_price(item, over):
        p = price(item, int(minv.get(item, I0) + over))
        if item == "WHEAT" and wheat_short:
            return max(p, float(wheat_buy))
        return float(p)

    # ---- greedy marginal allocation of free tiles -------------------------
    # Each extra tile of a product is priced AFTER the supply the earlier tiles
    # already committed, so every market self-limits.
    options = []
    for crop, cd in CROPS.items():
        y = crop_season(cd, days_left)          # fix 6: whole-season value
        if y:
            options.append(("crop", crop, y[0], y[1], y[2], crop))
    for name, a in ANIMALS.items():
        y = animal_yield(a, days_left)
        if y:
            cost = a["cost"] + max(0, days_left) * wheat_buy
            options.append(("animal", name, y[0], y[1], float(cost), a["prod"]))

    slots = len(empties) + len(weeds)
    sim_supply = dict(supply)
    want = {}
    for _ in range(min(slots, 60)):
        best = None
        for kind, name, units, actions, cost, item in options:
            over = max(0.0, sim_supply.get(item, 0.0) - absorb.get(item, 0.0))
            gain = units * tile_price(item, over) - cost
            if gain <= 0:
                continue
            score = gain / max(1.0, actions)
            if best is None or score > best[0]:
                best = (score, kind, name, units, item, gain)
        if best is None:
            break
        key = (best[1], best[2])
        want[key] = want.get(key, 0) + 1
        sim_supply[best[4]] = sim_supply.get(best[4], 0.0) + best[3]

    want_animal = {n: c for (k, n), c in want.items() if k == "animal"}
    want_crop = {n: c for (k, n), c in want.items() if k == "crop"}
    top_beast = max(want_animal, key=want_animal.get) if want_animal else None
    top_crop = max(want_crop, key=want_crop.get) if want_crop else None

    free_struct = {}
    for x, y, k in structs:
        free_struct.setdefault(k, []).append((x, y))

    # ---- price floor ------------------------------------------------------
    if step >= DUMP_STEP:
        hold = 0.0
    elif day < RELAX_DAY:
        hold = HOLD_EARLY
    else:
        f = (day - RELAX_DAY) / float(max(1, LAST_DAY - RELAX_DAY))
        hold = HOLD_EARLY + (HOLD_LATE - HOLD_EARLY) * f
    if shed_used > SHED_SOFT:
        hold = min(hold, 0.40)

    # ---- job board --------------------------------------------------------
    jobs = []
    unfed = 0
    for x, y, t in beasts:
        a = ANIMALS.get(t.get("animal"))
        if not a:
            continue
        p = spot(a["prod"])
        held = int(t.get("yield_units", 0) or 0)
        if held > 0:
            near_cap = held >= a["mh"] - 1
            jobs.append((held * p * (2.0 if near_cap else 1.0),
                         (x, y), ["HARVEST"], None))
        if not t.get("fed_today"):
            unfed += 1
            starving = int(t.get("consecutive_unfed", 0) or 0) >= 1
            # losing the animal forfeits its whole remaining stream
            jobs.append(((14.0 if starving else 2.2) * p, (x, y), ["FEED"], "WHEAT"))
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
                gain += 3.0 * p * max(1, cd["my"] - held)   # dies tonight otherwise
            if gain > 0:
                jobs.append((gain, (x, y), ["WATER"], None))

    carried = {}
    carried_wheat = 0
    for i in range(len(invs)):
        inv = invs[i] or {}
        carried_wheat += int(inv.get("WHEAT", 0) or 0)
        for k in ANIMALS:
            if int(inv.get(k, 0) or 0) > 0:
                carried[k] = carried.get(k, 0) + 1

    for name in ANIMALS:
        st = ANIMALS[name]["st"]
        slots_free = free_struct.get(st, [])
        if not slots_free:
            continue
        if carried.get(name, 0) <= 0 and shed.get(name, 0) <= 0:
            continue
        y = animal_yield(ANIMALS[name], days_left)
        gain = (y[0] * marginal(ANIMALS[name]["prod"]) - ANIMALS[name]["cost"]) if y else 400.0
        for x, yy in slots_free[:8]:
            jobs.append((max(500.0, gain), (x, yy), ["PLACE", name], name))

    if top_beast:
        st = ANIMALS[top_beast]["st"]
        have = len(free_struct.get(st, []))
        short = min(want_animal.get(top_beast, 0), len(empties)) - have
        if short > 0:
            op = "BUILD_COOP" if st == "COOP" else "BUILD_PASTURE"
            y = animal_yield(ANIMALS[top_beast], days_left)
            per = ((y[0] * marginal(ANIMALS[top_beast]["prod"])
                    - ANIMALS[top_beast]["cost"]) / 12.0) if y else 40.0
            for x, yy in sorted(empties, key=lambda e: dist(e, (4, 4)))[:short]:
                jobs.append((max(30.0, per), (x, yy), [op], None))

    for crop, n_want in sorted(want_crop.items(), key=lambda kv: -kv[1]):
        if seeds.get(crop, 0) <= 0:
            continue
        cd = CROPS[crop]
        y = crop_season(cd, days_left)
        if not y:
            continue
        over = max(0.0, supply.get(crop, 0.0) - absorb.get(crop, 0.0))
        per = (y[0] * tile_price(crop, over) - y[2]) / 4.0
        for x, yy in empties[:n_want + 4]:
            jobs.append((max(5.0, per), (x, yy), ["PLANT", crop], None))

    if days_left >= 3:
        for x, y in weeds:
            jobs.append((18.0, (x, y), ["DIG"], None))

    # fix 1: only fetch the feed that is actually going to be eaten today.
    # Wheat riding in a unit's inventory at dusk is dumped to the shed and
    # anything past the 100 cap is destroyed.
    unfed_left = max(0, unfed - carried_wheat)
    if unfed_left and shed.get("WHEAT", 0) > 0:
        v = max([j[0] for j in jobs if j[2][0] == "FEED"] or [0.0])
        for s in shed_tiles():
            jobs.append((v * 0.95, s, ["PICKUP", "WHEAT", 0], None))
    for name in ANIMALS:
        if shed.get(name, 0) > 0 and free_struct.get(ANIMALS[name]["st"]):
            for s in shed_tiles():
                jobs.append((600.0, s, ["PICKUP", name, 1], None))

    jobs.sort(key=lambda j: -j[0])
    jobs = jobs[:240]

    # ---- assignment: global greedy over (unit, job) ------------------------
    units = [(0, tuple(_get(farm, "farmer", [4, 4]) or [4, 4]))]
    for i, pos in enumerate(hands):
        units.append((i + 1, tuple(pos or [4, 4])))
    upos = dict(units)

    pairs = []
    for idx, pos in units:
        inv = dict(invs[idx] or {}) if idx < len(invs) else {}
        holding = next((k for k in ANIMALS if inv.get(k, 0) > 0), None)
        for j, (value, tgt, op, req) in enumerate(jobs):
            if holding:
                if op[0] not in ("PLACE", "BUILD_COOP", "BUILD_PASTURE"):
                    continue
                if op[0] == "PLACE" and op[1] != holding:
                    continue
            elif op[0] == "PLACE":
                continue
            if req == "WHEAT" and inv.get("WHEAT", 0) <= 0:
                continue
            d = dist(pos, tgt)
            if d > steps_left:
                continue
            pairs.append((value / float(1 + d), idx, j, d))
    pairs.sort(reverse=True)

    acts, busy, done = {}, set(), set()
    seed_budget = dict(seeds)
    shed_left = dict(shed)
    feed_left = unfed_left
    for _s, idx, j, d in pairs:
        if idx in busy or j in done:
            continue
        value, tgt, op, req = jobs[j]
        op = list(op)
        if op[0] == "PLANT" and seed_budget.get(op[1], 0) <= 0:
            continue
        if op[0] == "PICKUP" and shed_left.get(op[1], 0) <= 0:
            continue
        if op[0] == "PICKUP" and op[1] == "WHEAT":
            n = min(FEED_CARRY, feed_left, shed_left.get("WHEAT", 0))
            if n <= 0:
                continue
            feed_left -= n
            shed_left["WHEAT"] = shed_left.get("WHEAT", 0) - n
            op = ["PICKUP", "WHEAT", int(n)]
        elif op[0] == "PICKUP":
            shed_left[op[1]] = shed_left.get(op[1], 0) - 1
        busy.add(idx)
        done.add(j)
        if d == 0:
            if op[0] == "PLANT":
                seed_budget[op[1]] -= 1
            acts[idx] = op
        else:
            acts[idx] = step_toward(upos[idx], tgt)

    for idx, pos in units:
        if idx in acts:
            continue
        inv = dict(invs[idx] or {}) if idx < len(invs) else {}
        near = min(SHED_SET, key=lambda s: dist(pos, s))
        if inv and pos in SHED_SET and shed_used < SHED_CAP:
            acts[idx] = ["DROP"]
        elif inv:
            acts[idx] = step_toward(pos, near)
        elif beasts and pos not in SHED_SET:
            acts[idx] = step_toward(pos, near)     # pre-position for feed runs
        else:
            acts[idx] = ["PASS"]

    # ---- market ------------------------------------------------------------
    orders = []
    cash = money

    # fix 4: workforce sized to the FARM, not the calendar.  Hiring 14 hands a
    # day costs $986 whether or not there is work for them.
    workload = len(plants) + 2 * n_beasts + len(empties)
    want_hands = int(max(MIN_HANDS,
                         min(MAX_HANDS, math.ceil(workload / TILES_PER_HAND))))
    if hour == 0 and days_left >= 1:
        n = hires_today
        while n < want_hands and len(orders) < 9:
            c = _fib(n)
            if c > max(6.0, cash * 0.22):
                break
            orders.append(["HIRE"])
            cash -= c
            n += 1

    # fix 5: reserve covers FEED only.  g3 also reserved a day of wages plus a
    # 2,500 floor, which meant the animals it wanted were never affordable.
    reserve = 0.0 if days_left <= 1 else min(600.0, feed_target * wheat_buy)

    # fix 5: spend order wages -> animals -> seeds -> wheat top-up
    if top_beast and len(orders) < 10:
        cost = ANIMALS[top_beast]["cost"]
        st = ANIMALS[top_beast]["st"]
        pending = shed.get(top_beast, 0) + carried.get(top_beast, 0)
        openings = len(free_struct.get(st, [])) - pending
        n = min(max(0, openings), int(max(0.0, cash - reserve) // cost), 3)
        if n > 0 and shed_used + n < SHED_CAP - 2:
            orders.append(["BUY_ANIMAL", top_beast, int(n)])
            cash -= n * cost

    if top_crop and len(orders) < 10:
        c = CROPS[top_crop]["seed"]
        need = max(0, min(want_crop.get(top_crop, 0), len(empties) + len(weeds))
                   - seeds.get(top_crop, 0))
        n = min(need, int(max(0.0, cash - reserve) // c), 12)
        if n > 0:
            orders.append(["BUY_SEED", top_crop, int(n)])
            cash -= n * c

    owned_extra = len(quads) - 1
    if owned_extra < 3 and days_left >= 7 and len(orders) < 10:
        c = LAND_PRICES[owned_extra]
        crowded = len(empties) <= max(2, len(hands) // 2)
        if crowded and cash - c >= reserve:
            orders.append(["BUY_LAND"])
            cash -= c

    # fix 2: top up feed by at most one day's worth, and never into a dear
    # market -- g3 bought 1,722 wheat and spent every dollar it had.
    if n_beasts and len(orders) < 10 and wheat_buy <= WHEAT_BUY_MAX:
        need = max(0, feed_target - shed.get("WHEAT", 0))
        room = max(0, SHED_CAP - shed_used - 4)
        n = min(need, n_beasts, room, int(max(0.0, cash - 40.0) // max(1, wheat_buy)))
        if n > 0:
            orders.append(["BUY_PRODUCT", "WHEAT", int(n)])
            cash -= n * wheat_buy

    keep_wheat = 0 if step >= DUMP_STEP else min(shed.get("WHEAT", 0), feed_target)
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


def _selfcheck():
    """Cheap invariants for the six fixes -- no engine needed."""
    # fix 6: a fast crop must beat a slow one on whole-season units
    w = crop_season(CROPS["WHEAT"], 20)
    m = crop_season(CROPS["MELON"], 20)
    assert w[0] > m[0], (w, m)
    assert crop_season(CROPS["WHEAT"], 20)[2] == 10 * 5, crop_season(CROPS["WHEAT"], 20)
    # ongoing crops stay single-cycle
    assert crop_season(CROPS["TOMATO"], 20)[2] == 50.0
    # crops that cannot finish a cycle are still rejected
    assert crop_season(CROPS["MELON"], 3) is None
    # fix 1/2 constants actually tightened
    assert FEED_CARRY == 3 and WHEAT_BUY_MAX == 45
    # price curve sanity: base at I0, and the quadratic decays floor at 1
    assert price("WOOL", I0) == 200 and price("MELON", I0) == 250
    assert price("MELON", I0 + 400) == 1 and price("WHEAT", I0) == 25
    print("selfcheck ok")


if __name__ == "__main__":
    import sys
    _selfcheck()
    if "--check" not in sys.argv:
        from kaggle_environments import make
        env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": 7})
        env.run([agent, agent])
        last = env.steps[-1]
        assert last[0].status == "DONE", last[0].status
        print("g4 mirror seed 7:", int(last[0].reward), int(last[1].reward))
