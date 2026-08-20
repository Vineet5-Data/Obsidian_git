"""v36 -- observation-driven Kaggriculture policy.

The principle
-------------
Score is money, and money is bounded by what the MARKET ABSORBS, not by what
the farm grows.  Absorption is set by the town: each unlocked shop drains its
products every 4 steps, the town centre drains one of everything every 24, and
the shops are drawn at random per seed, revealed every 3 days in
`obs.town.unlocked_shops`.

So the profitable product mix is a per-seed random variable that only becomes
observable during the episode.  A fixed action tape cannot react to it.  This
policy is built entirely around reacting to it:

  1. read the drain implied by the shops seen so far (+ the mean of the shops
     still to be drawn),
  2. project our own future supply from what is already planted and placed,
  3. allocate every free tile by GREEDY MARGINAL VALUE -- each additional tile
     of a product is priced after the supply the previous tiles already added,
     so a market self-limits instead of being flooded,
  4. hire cheap early-day labour against the live maintenance/development queue,
  5. continuously turn shed stock into cash before placing purchase orders,
  6. keep feed distributed between shed and workers without repeatedly buying it,
  7. stop investing early enough to harvest, return, and liquidate everything.

Nothing here is derived from an opponent trajectory.
"""

import math as _math


class math:
    """Useful numeric helpers for the policy module."""

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("division by zero")
        return a / b

    @staticmethod
    def power(base, exponent):
        return base ** exponent

    @staticmethod
    def sqrt(value):
        return _math.sqrt(value)

    @staticmethod
    def log(value):
        return _math.log(value)

    @staticmethod
    def ceil(value):
        return _math.ceil(value)

    @staticmethod
    def floor(value):
        return _math.floor(value)

    @staticmethod
    def abs(value):
        return _math.fabs(value) if isinstance(value, float) else abs(value)

    @staticmethod
    def clamp(value, lo, hi):
        return max(lo, min(hi, value))

    @staticmethod
    def average(values):
        values = list(values)
        if not values:
            return 0.0
        return sum(values) / float(len(values))

    @classmethod
    def __getattr__(cls, name):
        return getattr(_math, name)


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

MAX_HANDS = 12
HIRE_WINDOW = 9
JOBS_PER_UNIT = 2.5      # tightened to limit idling
HOLD_EARLY = 0.62
HOLD_LATE = 0.12
RELAX_DAY = 18
DUMP_STEP = 648          # day 27: cash out while workers can still reach the shed
FINAL_FARM_STEP = 696    # last day is harvest/collection/liquidation only
SHED_SOFT = 50
FEED_CARRY = 5
FERT_CARRY = 4
HUNGARIAN_JOBS = 60      # increased to cover more jobs
FEED_DAYS = 1
FEED_BUFFER = 0.25
MAX_BUY_ORDERS = 5
WHEAT_BUY_MAX = 45
MOVE_FRAC = 2.5          # massively increased to aggressively penalize walking
PREMIUM_PRICE_FLOOR = 150


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
        return _math.sqrt(x)
    if func == "log":
        return _math.log(1.0 + x)
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


def sale_value(item, inv, qty):
    """Exact engine proceeds and post-sale inventory for one product batch."""
    total = 0
    inv = int(inv)
    for _ in range(max(0, int(qty))):
        p = price(item, inv)
        total += p
        # The engine deliberately does not advance supply for floor-price sales.
        if p > 1:
            inv += 1
    return total, inv


def race_score(item, inv, ours, rival):
    """Coin-margin swing from selling our batch before rather than after theirs."""
    mine_first, after_mine = sale_value(item, inv, ours)
    rival_first, after_rival = sale_value(item, inv, rival)
    rival_late, _ = sale_value(item, after_mine, rival)
    mine_late, _ = sale_value(item, after_rival, ours)
    return ((mine_first - mine_late) + (rival_first - rival_late),
            mine_first)


def _fib(n):
    a, b = 1, 1
    for _ in range(int(max(0, n))):
        a, b = b, a + b
    return a


def hire_bill(n):
    return sum(_fib(i) for i in range(max(0, n)))


def _hungarian(cost):
    """Kuhn-Munkres min-cost assignment; cost is n x m with n <= m.

    Replaces the greedy `pairs.sort(reverse=True)`, which is locally optimal
    only: it hands out the single best (worker, job) pair first, routinely
    sending one worker across the board for a high-value job while another
    walks past three adjacent cheap jobs.  Global matching removes that
    crossing-paths waste for the identical objective.  O(n^2 m) -- 13 workers
    x 48 jobs is microseconds.
    """
    n, m = len(cost), len(cost[0])
    INF = float("inf")
    u = [0.0] * (n + 1)
    v = [0.0] * (m + 1)
    p = [0] * (m + 1)
    way = [0] * (m + 1)
    for i in range(1, n + 1):
        p[0] = i
        j0 = 0
        minv = [INF] * (m + 1)
        used = [False] * (m + 1)
        while True:
            used[j0] = True
            i0 = p[j0]
            delta = INF
            j1 = 0
            for j in range(1, m + 1):
                if used[j]:
                    continue
                cur = cost[i0 - 1][j - 1] - u[i0] - v[j]
                if cur < minv[j]:
                    minv[j] = cur
                    way[j] = j0
                if minv[j] < delta:
                    delta = minv[j]
                    j1 = j
            if delta == INF:
                break
            for j in range(m + 1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    minv[j] -= delta
            j0 = j1
            if p[j0] == 0:
                break
        while j0:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
    res = [-1] * n
    for j in range(1, m + 1):
        if p[j] > 0:
            res[p[j] - 1] = j - 1
    return res


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
    """(units, tile-actions, days occupied) for one cycle started now."""
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
    """Value every complete cycle a tile can still finish this season."""
    y = crop_yield(cd, days_left)
    if not y:
        return None
    units, actions, _span = y
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
    # CARE is banked every fed day and paid on a production tick.  The held
    # amount is capped, so value the first long interval and later short ones
    # separately instead of the old flat two-units-per-tick approximation.
    first = min(a["mh"], 1 + a["fyd"])
    later = min(a["mh"], 1 + max(1, a["iv"]))
    units = first + max(0, n - 1) * later
    actions = 2.0 * days_left + n * 2.0 / max(1, a["mh"])
    return units, actions, a["fyd"]


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
    # A center tile is usable for shed actions only after its quadrant is
    # unlocked.  The engine rejects PICKUP/DROP/PLACE while standing on a
    # locked tile, so derive the legal access set from the live board.
    shed_access = [s for s in ((4, 4), (5, 4), (4, 5), (5, 5))
                   if tiles[s[1]][s[0]] != "LOCKED"]
    shed_access_set = set(shed_access)
    hires_today = int(_get(farm, "hires_today", 0) or 0)
    quads = list(_get(farm, "unlocked_quadrants", ["NW"]) or ["NW"])

    private = _get(obs, "private", {}) or {}
    shed = {k: int(v or 0) for k, v in (_get(private, "shed", {}) or {}).items()}
    seeds = {k: int(v or 0) for k, v in (_get(private, "seeds", {}) or {}).items()}
    invs = list(_get(private, "inventories", []) or [{}])
    carried_all = {}
    for inv in invs:
        for item, qty in dict(inv or {}).items():
            qty = int(qty or 0)
            if qty > 0:
                carried_all[item] = carried_all.get(item, 0) + qty

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
    empties.sort(key=lambda p: (min(dist(p, s) for s in shed_access_set), p[1], p[0]))

    # ---- absorption -------------------------------------------------------
    absorb = dict.fromkeys(PRODUCTS, 0.0)
    for s in shops:
        prods = SHOPS.get(s)
        if not prods:
            continue
        mult = 2.0 if len(prods) == 1 else 1.0
        for it in prods:
            absorb[it] += mult * steps_left / 4.0
    # The current competition engine consumes one unit per town-centre tick.
    # Use the observed 24-turn cadence; the old tier multiplier substantially
    # overestimated demand and encouraged one-product gluts.
    center_ticks = steps_left / float(TPD)
    for it in TOWN_CENTER:
        absorb[it] += center_ticks
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
    for it, n in carried_all.items():
        if it in supply:
            supply[it] += n
    for _, _, t in plants:
        cd = CROPS.get(t.get("crop"))
        if not cd:
            continue
        held = int(t.get("yield_units", 0) or 0)
        age = day - int(t.get("planted_day", day) or 0)
        future = 0
        if cd["ong"]:
            interval = max(1, cd["iv"])
            produced = (1 + max(0, age - cd["fyd"]) // interval) if age >= cd["fyd"] else 0
            future = max(0, cd["my"] - produced)
            if age < cd["fyd"]:
                horizon = max(0, days_left - max(0, cd["fyd"] - age))
                future = min(future, 1 + horizon // interval)
            else:
                future = min(future, days_left // interval + 1)
        elif age <= cd["myd"] and cd["myd"] - age <= days_left:
            future = max(0, cd["my"] - held)
        supply[t["crop"]] += held + future
    for _, _, t in beasts:
        a = ANIMALS.get(t.get("animal"))
        if not a:
            continue
        age = day - int(t.get("placed_day", day) or 0)
        d, n = max(0, a["fyd"] - age), 0
        while d <= days_left:
            n += 1
            d += max(1, a["iv"])
        first = min(a["mh"], 1 + max(0, a["fyd"] - age))
        later = min(a["mh"], 1 + max(1, a["iv"]))
        supply[a["prod"]] += (int(t.get("yield_units", 0) or 0)
                              + (first + max(0, n - 1) * later if n else 0))

    own_crop_counts = {name: 0 for name in CROPS}
    own_animal_counts = {name: 0 for name in ANIMALS}
    for _, _, t in plants:
        crop = t.get("crop")
        if crop in own_crop_counts:
            own_crop_counts[crop] += 1
    for _, _, t in beasts:
        name = t.get("animal")
        if name in own_animal_counts:
            own_animal_counts[name] += 1

    # Public opponent assets are legitimate forward information.  Discount
    # their technically possible output because routes can miss care/watering,
    # but account for it before committing to the same crash-prone product.
    opp_crop_counts = {name: 0 for name in CROPS}
    opp_animal_counts = {name: 0 for name in ANIMALS}
    opp_wave = {name: 0.0 for name in PRODUCTS}
    if len(farms) > 1:
        opponent = farms[1 - seat]
        for row in (_get(opponent, "tiles", []) or []):
            for t in (row or []):
                if not isinstance(t, dict):
                    continue
                if t.get("kind") == "PLANT" and t.get("crop") in CROPS:
                    crop = t["crop"]
                    cd = CROPS[crop]
                    opp_crop_counts[crop] += 1
                    held = int(t.get("yield_units", 0) or 0)
                    opp_wave[crop] += held
                    age = day - int(t.get("planted_day", day) or 0)
                    if cd["ong"]:
                        interval = max(1, cd["iv"])
                        produced = (1 + max(0, age - cd["fyd"]) // interval
                                    if age >= cd["fyd"] else 0)
                        future = max(0, cd["my"] - produced)
                    else:
                        future = (max(0, cd["my"] - held)
                                  if age <= cd["myd"] else 0)
                    supply[crop] += 0.80 * (held + future)

                    # Add the production wave due at the next refresh.  Held
                    # yield is public; this one-day forecast covers product that
                    # can disappear into the rival's hidden inventory next turn.
                    planted_day = t.get("planted_day", day)
                    planted_day = day if planted_day is None else int(planted_day)
                    if cd["ong"]:
                        since_first = day + 1 - planted_day - cd["fyd"]
                        due = (since_first >= 0
                               and since_first % max(1, cd["iv"]) == 0
                               and since_first // max(1, cd["iv"]) < cd["my"])
                        if due:
                            opp_wave[crop] += 1.2
                    elif held <= 0 and age < cd["fyd"] <= age + 1:
                        opp_wave[crop] += max(1.0, 0.8 * cd["my"])
                elif "animal" in t and t.get("animal") in ANIMALS:
                    name = t["animal"]
                    a = ANIMALS[name]
                    opp_animal_counts[name] += 1
                    age = day - int(t.get("placed_day", day) or 0)
                    delay = max(0, a["fyd"] - age)
                    productive_days = max(0, days_left - delay + 1)
                    daily_rate = {"GOOSE": 2.0, "COW": 1.5,
                                  "SHEEP": 4.0 / 3.0}[name]
                    held = int(t.get("yield_units", 0) or 0)
                    supply[a["prod"]] += 0.80 * (held + productive_days * daily_rate)
                    opp_wave[a["prod"]] += held
                    placed_day = t.get("placed_day", day)
                    placed_day = day if placed_day is None else int(placed_day)
                    since_first = day + 1 - placed_day - a["fyd"]
                    if (since_first >= 0
                            and since_first % max(1, a["iv"]) == 0):
                        opp_wave[a["prod"]] += 0.8 * daily_rate * max(1, a["iv"])
                    if t.get("fertilizer_available"):
                        opp_wave["FERTILIZER"] += 0.8

    # Dynamic Strategy Switcher
    premium_count = (opp_animal_counts.get("COW", 0) + opp_animal_counts.get("SHEEP", 0) +
                     opp_crop_counts.get("MELON", 0) + opp_crop_counts.get("STRAWBERRY", 0))
    staple_count = (opp_animal_counts.get("GOOSE", 0) + 
                    opp_crop_counts.get("CARROT", 0) + 
                    opp_crop_counts.get("TOMATO", 0))
    opp_quads = len(_get(farms[1 - seat] if len(farms) > 1 else {}, "unlocked_quadrants", []))
    
    if opp_quads >= 4 or staple_count >= 10:
        mode = "EXPAND"
        allowed_crops = tuple(CROPS.keys())
        allowed_animals = tuple(ANIMALS.keys())
        max_quadrants = 4
    elif premium_count >= 8:
        mode = "MIRROR"
        allowed_crops = ("WHEAT", "STRAWBERRY", "MELON")
        allowed_animals = ("COW", "SHEEP")
        max_quadrants = 3
    else:
        mode = "EXPAND"
        allowed_crops = tuple(CROPS.keys())
        allowed_animals = tuple(ANIMALS.keys())
        max_quadrants = 4

    # Hidden carried/shed stock cannot be observed after a harvest.  Retain a
    # small, asset-derived fallback so a visibly contested market never appears
    # falsely uncontested merely because its current tile yield is zero.
    fallback_wave = {
        "WHEAT": 2.0 * opp_crop_counts.get("WHEAT", 0),
        "CARROT": 1.5 * opp_crop_counts.get("CARROT", 0),
        "TOMATO": 1.0 * opp_crop_counts.get("TOMATO", 0),
        "STRAWBERRY": 1.0 * opp_crop_counts.get("STRAWBERRY", 0),
        "MELON": 3.0 * opp_crop_counts.get("MELON", 0),
        "EGG": 1.5 * opp_animal_counts.get("GOOSE", 0),
        "MILK": 1.5 * opp_animal_counts.get("COW", 0),
        "WOOL": 2.0 * opp_animal_counts.get("SHEEP", 0),
        "FERTILIZER": float(sum(opp_animal_counts.values())),
    }
    for item in PRODUCTS:
        opp_wave[item] = min(100.0, max(opp_wave[item],
                                       0.50 * fallback_wave.get(item, 0.0)))

    def marginal(item, extra=0.0):
        over = max(0.0, supply.get(item, 0.0) + extra - absorb.get(item, 0.0))
        return price(item, int(minv.get(item, I0) + over))

    def spot(item):
        return price(item, minv.get(item, I0))

    wheat_buy = price("WHEAT", minv.get("WHEAT", I0) - 1)

    # ---- marginal portfolio allocation of free tiles ----------------------
    # Reserve animal capacity first, then diversify crops.  Every selection
    # updates projected supply so the choice remains live-price adaptive.
    slots = len(empties) + len(weeds)
    sim_supply = dict(supply)
    pending_animals = sum(int(shed.get(name, 0) or 0)
                          + int(carried_all.get(name, 0) or 0)
                          for name in ANIMALS)
    current_animal_assets = len(beasts) + len(structs)
    if days_left < 8:
        animal_target = current_animal_assets
    elif day < 3:
        animal_target = 4
    else:
        animal_target = min(20, max(6, int(round(25 * len(quads) * 0.22))))
    animal_need = max(0, animal_target - len(beasts) - pending_animals)
    structure_need = min(slots, max(0, animal_target - current_animal_assets))
    want_animal = {}
    species_cap = max(2, int(math.ceil(max(1, animal_target) * 0.45)))
    # Match visible profitable livestock capacity before taking an uncontested
    # fallback.  Shared-market denial is valuable: conceding all milk/wool
    # demand to the rival can increase their bank more than diversification
    # increases ours.
    for name in sorted(ANIMALS, key=lambda n: -opp_animal_counts.get(n, 0)):
        if name not in allowed_animals: continue
        if sum(want_animal.values()) >= animal_need:
            break
        owned = (own_animal_counts.get(name, 0)
                 + int(shed.get(name, 0) or 0)
                 + int(carried_all.get(name, 0) or 0))
        strategic_target = min(species_cap, opp_animal_counts.get(name, 0))
        n = min(max(0, strategic_target - owned),
                animal_need - sum(want_animal.values()))
        if n <= 0:
            continue
        want_animal[name] = n
        y = animal_yield(ANIMALS[name], days_left)
        if y:
            sim_supply[ANIMALS[name]["prod"]] += n * y[0]

    for _ in range(max(0, animal_need - sum(want_animal.values()))):
        best = None
        for name, a in ANIMALS.items():
            if name not in allowed_animals: continue
            y = animal_yield(a, days_left)
            if not y:
                continue
            already = (own_animal_counts.get(name, 0)
                       + int(shed.get(name, 0) or 0)
                       + int(carried_all.get(name, 0) or 0)
                       + want_animal.get(name, 0))
            if already >= species_cap:
                continue
            item = a["prod"]
            over = max(0.0, sim_supply.get(item, 0.0) - absorb.get(item, 0.0))
            p = price(item, int(minv.get(item, I0) + over))
            feed_cost = max(0, days_left) * wheat_buy
            fertilizer_value = max(0, days_left) * marginal("FERTILIZER")
            gain = y[0] * p + fertilizer_value - a["cost"] - feed_cost
            if gain <= 0:
                continue
            actions = y[1] + max(0, days_left)  # include fertilizer collection
            crowd = already
            score = gain / (max(1.0, actions) * (1.0 + 0.10 * crowd))
            if best is None or score > best[0]:
                best = (score, name, y[0], item)
        if best is None:
            break
        want_animal[best[1]] = want_animal.get(best[1], 0) + 1
        sim_supply[best[3]] = sim_supply.get(best[3], 0.0) + best[2]

    crop_slots = max(0, min(60, slots - structure_need))
    want_crop = {}
    # Quick wheat creates the opening cash cycle and becomes feed instead of an
    # expensive market purchase.  This is a phase constraint, not a route.
    if day < 3 and crop_slots > 0:
        quick = min(crop_slots, max(6, int(round(crop_slots * 0.40))))
        want_crop["WHEAT"] = quick
        sim_supply["WHEAT"] = sim_supply.get("WHEAT", 0.0) + 4 * quick

    portfolio_size = len(plants) + crop_slots
    crop_cap = max(3, int(math.ceil(max(1, portfolio_size)
                                    * (0.42 if len(shops) < 2 else 0.52))))
    # Compete for fragile premium markets when the rival has visibly committed
    # production.  Targets come from the live board, never an identity or tape.
    for crop in ("STRAWBERRY", "MELON"):
        room = crop_slots - sum(want_crop.values())
        if room <= 0:
            break
        strategic_target = min(crop_cap,
                               int(math.ceil(0.90 * opp_crop_counts.get(crop, 0))))
        deficit = max(0, strategic_target - own_crop_counts.get(crop, 0))
        n = min(room, deficit)
        if n <= 0:
            continue
        want_crop[crop] = want_crop.get(crop, 0) + n
        y = crop_yield(CROPS[crop], days_left)
        if y:
            sim_supply[crop] = sim_supply.get(crop, 0.0) + n * y[0]

    remaining_crop_slots = crop_slots - sum(want_crop.values())
    for _ in range(remaining_crop_slots):
        best = None
        for crop, cd in CROPS.items():
            if crop not in allowed_crops: continue
            y = crop_season(cd, days_left)
            if not y:
                continue
            already = own_crop_counts.get(crop, 0) + want_crop.get(crop, 0)
            if already >= crop_cap:
                continue
            over = max(0.0, sim_supply.get(crop, 0.0) - absorb.get(crop, 0.0))
            p = price(crop, int(minv.get(crop, I0) + over))
            gain = y[0] * p - y[2]
            if gain <= 0:
                continue
            crowd = already
            time_risk = 1.0 + 0.025 * cd["fyd"]
            score = gain / (max(1.0, y[1]) * time_risk * (1.0 + 0.055 * crowd))
            if best is None or score > best[0]:
                best = (score, crop, y[0])
        if best is None:
            break
        want_crop[best[1]] = want_crop.get(best[1], 0) + 1
        sim_supply[best[1]] = sim_supply.get(best[1], 0.0) + best[2]

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
    fertilize_needed = 0
    for x, y, t in beasts:
        a = ANIMALS.get(t.get("animal"))
        if not a:
            continue
        p = spot(a["prod"])
        held = int(t.get("yield_units", 0) or 0)
        if held > 0:
            near_cap = held >= a["mh"] - 1
            terminal = 5.0 if step >= DUMP_STEP else 1.0
            # Batch harvests create a market shock that cannot be absorbed
            # between tiny sales, while the near-cap multiplier still protects
            # the next production tick.  A fixed urgency tier caused premature
            # one-unit sales and restored monopoly prices for the rival.
            jobs.append((held * p * (2.0 if near_cap else 1.0) * terminal,
                         (x, y), ["HARVEST"], None))
        if t.get("fertilizer_available"):
            jobs.append((1.15 * spot("FERTILIZER"),
                         (x, y), ["COLLECT_FERTILIZER"], None))
        if step < FINAL_FARM_STEP and not t.get("fed_today"):
            unfed += 1
            starving = int(t.get("consecutive_unfed", 0) or 0) >= 1
            jobs.append(((14.0 if starving else 2.2) * p,
                         (x, y), ["FEED"], "WHEAT"))
        if step < FINAL_FARM_STEP and not t.get("cared_today"):
            jobs.append((0.95 * p, (x, y), ["CARE"], None))

    for x, y, t in plants:
        cd = CROPS.get(t.get("crop"))
        if not cd:
            continue
        p = spot(t["crop"])
        age = day - int(t.get("planted_day", day) or 0)
        held = int(t.get("yield_units", 0) or 0)
        if held > 0 and age >= cd["fyd"]:
            terminal = 5.0 if step >= DUMP_STEP else 1.0
            # Wait for a useful batch, then harvest decisively once the crop's
            # production cycle is complete.  This realizes the crop before
            # decay without turning every one-unit tick into a price-supporting
            # trickle sale.
            batch_ready = ((cd["ong"] and t.get("max_lifespan_step") is not None)
                           or (not cd["ong"] and age >= cd["myd"]))
            batch_tier = 0.0
            jobs.append((batch_tier + (held * p + (14 if not cd["ong"] else 0)) * terminal,
                         (x, y), ["HARVEST"], None))
        # Ongoing crops can produce two units instead of one when both watered
        # and fertilized on a scheduled production day.  One application lasts
        # through the next two days, so this naturally covers two strawberry
        # ticks without a fixed route.
        if (step < FINAL_FARM_STEP and cd["ong"]
                and int(t.get("fertilized_until_day", -1) or -1) < day):
            planted_day = t.get("planted_day", day)
            planted_day = day if planted_day is None else int(planted_day)
            since_first = day + 1 - planted_day - cd["fyd"]
            due = (since_first >= 0 and since_first % max(1, cd["iv"]) == 0
                   and since_first // max(1, cd["iv"]) < cd["my"])
            incremental = p - spot("FERTILIZER")
            strategic_denial = (t.get("crop") in ("STRAWBERRY", "TOMATO")
                                and opp_crop_counts.get(t.get("crop"), 0) > 0)
            if due and (incremental > 12.0 or strategic_denial):
                fertilize_needed += 1
                jobs.append((max(80.0, 2.0 * p - spot("FERTILIZER")),
                              (x, y), ["FERTILIZE"], "FERTILIZER"))
        if step < FINAL_FARM_STEP and not t.get("watered_today"):
            if cd["ong"]:
                gain = float(p)
            else:
                w0 = (cd["myd"] + 1) // 2
                gain = float(p) if w0 <= age <= cd["myd"] else 0.0
            if int(t.get("consecutive_unwatered", 0) or 0) >= 1:
                gain += 50000.0 + 3.0 * p * max(1, cd["my"] - held)
            if gain > 0:
                jobs.append((gain, (x, y), ["WATER"], None))

    carried = {k: int(carried_all.get(k, 0) or 0) for k in ANIMALS}
    carried_wheat = int(carried_all.get("WHEAT", 0) or 0)
    carried_fertilizer = int(carried_all.get("FERTILIZER", 0) or 0)

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

    desired_struct_raw = {}
    for name, n_want in want_animal.items():
        st = ANIMALS[name]["st"]
        desired_struct_raw[st] = desired_struct_raw.get(st, 0) + n_want
    # Keep a productive crop/animal mix instead of letting the marginal model
    # fill the first 25-tile quadrant with crops before any structure exists.
    animal_cap = min(20, max(6, int(25 * len(quads) * 0.27)))
    remaining_structs = max(0, animal_cap - len(beasts))
    desired_struct = {}
    for st, raw in sorted(desired_struct_raw.items(), key=lambda kv: -kv[1]):
        n = min(raw, remaining_structs)
        if n > 0:
            desired_struct[st] = n
            remaining_structs -= n
    animal_sites = set()
    site_cursor = 0
    for st, n_want in desired_struct.items():
        have = len(free_struct.get(st, []))
        short = min(n_want, len(empties)) - have
        if short <= 0:
            continue
        op = "BUILD_COOP" if st == "COOP" else "BUILD_PASTURE"
        candidates = [n for n in want_animal if ANIMALS[n]["st"] == st]
        values = []
        for name in candidates:
            y = animal_yield(ANIMALS[name], days_left)
            if y:
                values.append((y[0] * marginal(ANIMALS[name]["prod"])
                               - ANIMALS[name]["cost"]) / 12.0)
        per = max(values or [40.0])
        sites = empties[site_cursor:site_cursor + short]
        site_cursor += len(sites)
        animal_sites.update(sites)
        for x, yy in sites:
            d_shed = min(dist((x, yy), s) for s in shed_access_set)
            dist_multiplier = 5.0 if d_shed <= 1 else (1.5 if d_shed == 2 else 0.1)
            jobs.append((max(90.0, 2.0 * per) * dist_multiplier, (x, yy), [op], None))

    crop_empties = [p for p in empties if p not in animal_sites]
    for crop, n_want in sorted(want_crop.items(), key=lambda kv: -kv[1]):
        if seeds.get(crop, 0) <= 0:
            continue
        cd = CROPS[crop]
        y = crop_yield(cd, days_left)
        if not y:
            continue
        per = (y[0] * marginal(crop) - cd["seed"]) / 4.0
        for x, yy in crop_empties[:n_want + 4]:
            d_shed = min(dist((x, yy), s) for s in shed_access_set)
            if cd["ong"]:
                dist_multiplier = 2.5 if d_shed <= 2 else 0.4
            else:
                dist_multiplier = 0.3 if d_shed <= 2 else 1.5
            jobs.append((max(5.0, per) * dist_multiplier, (x, yy), ["PLANT", crop], None))

    if days_left >= 3 and step < DUMP_STEP:
        for x, y in weeds:
            jobs.append((18.0, (x, y), ["DIG"], None))

    uncovered_feed = max(0, unfed - carried_wheat)
    pickup_workers = min(len(shed_access),
                         int(math.ceil(uncovered_feed / float(FEED_CARRY))))
    if pickup_workers > 0 and shed.get("WHEAT", 0) > 0:
        v = max([j[0] for j in jobs if j[2][0] == "FEED"] or [0.0])
        for s in shed_access[:pickup_workers]:
            jobs.append((v * 0.95, s, ["PICKUP", "WHEAT", 0], None))
    fertilizer_pickups = min(len(shed_access), max(
        0, int(math.ceil(max(0, fertilize_needed - carried_fertilizer)
                         / float(FERT_CARRY)))))
    if fertilizer_pickups > 0 and shed.get("FERTILIZER", 0) > 0:
        # ``fertilizer_pickups`` is already the number of additional carrier
        # loads required after accounting for every carried unit.  Subtracting
        # the carrier count again under-filled large scheduled crop waves.
        for s in shed_access[:fertilizer_pickups]:
            jobs.append((600.0, s, ["PICKUP", "FERTILIZER", 0], None))
    for name in ANIMALS:
        if shed.get(name, 0) > 0 and free_struct.get(ANIMALS[name]["st"]):
            for s in shed_access:
                jobs.append((600.0, s, ["PICKUP", name, 1], None))

    jobs.sort(key=lambda j: -j[0])
    jobs = jobs[:240]

    # ---- assignment: global greedy over (unit, job) ------------------------
    units = [(0, tuple(_get(farm, "farmer", [4, 4]) or [4, 4]))]
    for i, pos in enumerate(hands):
        units.append((i + 1, tuple(pos or [4, 4])))
    upos = dict(units)

    # Bank useful loads regularly.  During liquidation this becomes mandatory,
    # otherwise a final harvest can sit on a worker after the last market tick.
    forced = {}
    # Survival is a deadline constraint, not a spot-price auction.  Match
    # wheat carriers to second-miss animals before banking/economic jobs.
    # Rebuilding this deterministic matching from each observation keeps it
    # replay-agnostic while cargo and decreasing distance provide commitment.
    critical_feed = [(x, y) for x, y, t in beasts
                     if (step < FINAL_FARM_STEP and not t.get("fed_today")
                         and int(t.get("consecutive_unfed", 0) or 0) >= 1)]
    feasible = {}
    feed_pairs = []
    remaining_today = max(0, TPD - hour - 1)
    for idx, pos in units:
        inv = dict(invs[idx] or {}) if idx < len(invs) else {}
        if int(inv.get("WHEAT", 0) or 0) <= 0:
            continue
        for tgt in critical_feed:
            d = dist(pos, tgt)
            if d <= remaining_today:
                feasible[tgt] = feasible.get(tgt, 0) + 1
                feed_pairs.append((d, idx, tgt))
    feed_pairs.sort(key=lambda z: (feasible.get(z[2], 999), z[0],
                                   z[2][1], z[2][0], z[1]))
    feed_units, feed_targets = set(), set()
    for d, idx, tgt in feed_pairs:
        if idx in feed_units or tgt in feed_targets:
            continue
        pos = upos[idx]
        forced[idx] = ["FEED"] if d == 0 else step_toward(pos, tgt)
        feed_units.add(idx)
        feed_targets.add(tgt)

    bank_room = max(0, SHED_CAP - shed_used)
    for idx, pos in units:
        if idx in forced:
            continue
        inv = dict(invs[idx] or {}) if idx < len(invs) else {}
        if any(int(inv.get(k, 0) or 0) > 0 for k in ANIMALS):
            continue
        sale_load = sum(int(inv.get(k, 0) or 0) for k in MP)
        if sale_load <= 0:
            continue
        feed_load = int(inv.get("WHEAT", 0) or 0)
        must_bank = (step >= DUMP_STEP or sale_load >= 4 or money < 300.0)
        if feed_load > 0 and unfed > 0 and step < FINAL_FARM_STEP:
            must_bank = False
        if (int(inv.get("FERTILIZER", 0) or 0) > 0
                and fertilize_needed > 0 and step < FINAL_FARM_STEP):
            must_bank = False
        if not must_bank:
            continue
        near = min(shed_access_set, key=lambda s: dist(pos, s))
        if pos not in shed_access_set:
            forced[idx] = step_toward(pos, near)
            continue
        total_load = sum(max(0, int(v or 0)) for v in inv.values())
        if bank_room >= total_load:
            forced[idx] = ["DROP"]
            bank_room -= total_load
        elif bank_room > 0:
            item = max((k for k in MP if int(inv.get(k, 0) or 0) > 0),
                       key=lambda k: spot(k))
            n = min(bank_room, int(inv.get(item, 0) or 0))
            forced[idx] = ["PLACE", item, int(n)]
            bank_room -= n

    free_units = [(idx, pos) for idx, pos in units if idx not in forced]
    ncand = min(len(jobs), HUNGARIAN_JOBS)
    BIG = 1e9
    turns_left_today = max(0, TPD - hour - 1)
    # Opportunity cost of one worker-turn, calibrated live off this turn's own
    # job board rather than a tuned constant: walking one tile costs one turn,
    # and the turn is worth roughly what a typical available job pays.  `jobs`
    # is already sorted by descending value, so the midpoint is its median.
    move_rate = MOVE_FRAC * (jobs[ncand // 2][0] if ncand else 0.0)
    cost, meta = [], []
    for idx, pos in free_units:
        inv = dict(invs[idx] or {}) if idx < len(invs) else {}
        holding = next((k for k in ANIMALS if inv.get(k, 0) > 0), None)
        row, feas = [], {}
        for j in range(ncand):
            value, tgt, op, req = jobs[j]
            ok = True
            if holding:
                if op[0] not in ("PLACE", "BUILD_COOP", "BUILD_PASTURE"):
                    ok = False
                elif op[0] == "PLACE" and op[1] != holding:
                    ok = False
            elif op[0] == "PLACE":
                ok = False
            if ok and op[0] == "PICKUP":
                cap = (FEED_CARRY if op[1] == "WHEAT" else
                       (FERT_CARRY if op[1] == "FERTILIZER" else 1))
                if int(inv.get(op[1], 0) or 0) >= cap:
                    ok = False
            if ok and req in ("WHEAT", "FERTILIZER") and inv.get(req, 0) <= 0:
                ok = False
            d = dist(pos, tgt)
            if ok and (d > steps_left or d > turns_left_today):
                ok = False
            # A new plant must leave one later action for WATER before EOD;
            # otherwise it immediately becomes a weed.
            if ok and op[0] == "PLANT" and hour + d > TPD - 2:
                ok = False
            # WUFANG IDLE CUTOFF:
            # Replicate the TAS efficiency by aggressively filtering out distant, low-value jobs.
            # If the job is worth less than 40 and requires walking more than 2 steps, or
            # worth less than 80 and requires walking more than 4 steps, skip it and idle instead.
            # Disable this completely if we or the opponent are playing a 4-quadrant swarm game.
            if len(quads) < 4:
                if ok and ((value < 40.0 and d > 2) or (value < 80.0 and d > 4)):
                    ok = False
            if ok:
                feas[j] = d
                # Linear travel charge instead of the `value / (1 + d)` ratio.
                # The ratio is a value-DENSITY, which is the right objective for
                # work that repeats; for a one-shot assignment it lets a large
                # value drag a worker clear across the board, because dividing
                # by 9 still leaves a big number.  Subtracting the turns the
                # walk actually costs makes a worker travel only when the job
                # beats what it could have done nearer.  This changes the FORM
                # of the cost -- hysteresis (v52), a wider job list (v53) and a
                # reachability filter (v54) all changed only its inputs.
                row.append(-(value - move_rate * d))
            else:
                row.append(BIG)
        cost.append(row)
        meta.append((idx, feas))

    # Kuhn-Munkres needs n <= m; pad when workers outnumber candidate jobs.
    if cost and len(cost) > len(cost[0]):
        pad = len(cost) - len(cost[0])
        for row in cost:
            row.extend([BIG] * pad)

    pairs = []
    if cost:
        for i, j in enumerate(_hungarian(cost)):
            if j < 0:
                continue
            idx, feas = meta[i]
            if j not in feas:
                continue      # matched only to an infeasible filler column
            pairs.append((-cost[i][j], idx, j, feas[j]))
    pairs.sort(reverse=True)

    acts, busy, done = dict(forced), set(forced), set()
    claimed_tiles = set()
    seed_budget = dict(seeds)
    shed_left = dict(shed)
    for _s, idx, j, d in pairs:
        if idx in busy or j in done:
            continue
        value, tgt, op, req = jobs[j]
        op = list(op)
        exclusive = op[0] in ("PLANT", "BUILD_COOP", "BUILD_PASTURE", "DIG", "PLACE")
        if exclusive and tgt in claimed_tiles:
            continue
        if op[0] == "PLANT" and seed_budget.get(op[1], 0) <= 0:
            continue
        if op[0] == "PICKUP" and shed_left.get(op[1], 0) <= 0:
            continue
        busy.add(idx)
        done.add(j)
        if exclusive:
            claimed_tiles.add(tgt)
        if op[0] == "PLANT":
            seed_budget[op[1]] -= 1
        if d == 0:
            if op[0] == "PICKUP":
                if op[1] == "WHEAT":
                    carry_cap = FEED_CARRY
                elif op[1] == "FERTILIZER":
                    carry_cap = FERT_CARRY
                else:
                    carry_cap = 1
                existing = int((invs[idx] or {}).get(op[1], 0) or 0)
                n = min(max(0, carry_cap - existing),
                        shed_left.get(op[1], 0))
                shed_left[op[1]] = shed_left.get(op[1], 0) - n
                op = ["PICKUP", op[1], int(n)]
            acts[idx] = op
        else:
            if op[0] == "PICKUP":
                carry_cap = (FEED_CARRY if op[1] == "WHEAT" else
                             (FERT_CARRY if op[1] == "FERTILIZER" else 1))
                existing = int((invs[idx] or {}).get(op[1], 0) or 0)
                shed_left[op[1]] = (shed_left.get(op[1], 0)
                                      - max(0, carry_cap - existing))
            acts[idx] = step_toward(upos[idx], tgt)

    for idx, pos in units:
        if idx in acts:
            continue
        inv = dict(invs[idx] or {}) if idx < len(invs) else {}
        near = min(shed_access_set, key=lambda s: dist(pos, s))
        total_load = sum(max(0, int(v or 0)) for v in inv.values())
        if inv and pos in shed_access_set and bank_room >= total_load:
            acts[idx] = ["DROP"]
            bank_room -= total_load
        elif inv and pos in shed_access_set and bank_room > 0:
            candidates = [k for k, v in inv.items() if int(v or 0) > 0]
            item = max(candidates,
                       key=lambda k: spot(k) if k in MP else ANIMALS.get(k, {}).get("cost", 0))
            n = min(bank_room, int(inv.get(item, 0) or 0))
            acts[idx] = ["PLACE", item, int(n)]
            bank_room -= n
        elif inv:
            acts[idx] = step_toward(pos, near)
        elif beasts and pos not in shed_access_set:
            acts[idx] = step_toward(pos, near)     # pre-position for feed runs
        else:
            acts[idx] = ["PASS"]

    # ---- market: deposits -> sales -> necessities -> investment -----------
    # Unit actions execute before market orders, so inventory deposited by a
    # DROP/PLACE this turn is genuinely sellable in this same ordered queue.
    projected = dict(shed)
    projected_used = shed_used
    deposited = {}
    for idx in sorted(acts):
        if idx >= len(invs):
            continue
        op = acts[idx]
        pos = upos.get(idx, (4, 4))
        inv = dict(invs[idx] or {})
        if not op or pos not in shed_access_set:
            continue
        if op[0] == "DROP":
            for item, qty in inv.items():
                room = max(0, SHED_CAP - projected_used)
                accepted = min(room, max(0, int(qty or 0)))
                if accepted <= 0:
                    break
                projected[item] = projected.get(item, 0) + accepted
                deposited[item] = deposited.get(item, 0) + accepted
                projected_used += accepted
        elif op[0] == "PICKUP" and len(op) >= 3:
            item = op[1]
            taken = min(max(0, int(op[2] or 0)),
                        max(0, int(projected.get(item, 0) or 0)))
            if taken > 0:
                projected[item] = max(0, int(projected.get(item, 0)) - taken)
                projected_used = max(0, projected_used - taken)
        elif op[0] == "PLACE" and len(op) >= 3 and op[1] in MP:
            item = op[1]
            room = max(0, SHED_CAP - projected_used)
            accepted = min(room, int(op[2] or 0), int(inv.get(item, 0) or 0))
            if accepted > 0:
                projected[item] = projected.get(item, 0) + accepted
                deposited[item] = deposited.get(item, 0) + accepted
                projected_used += accepted

    orders = []
    cash = money
    n_beasts = len(beasts)
    feed_target = (n_beasts + int(math.ceil(n_beasts * FEED_BUFFER))
                   if step < FINAL_FARM_STEP else 0)
    sim = dict(minv)

    sell_hold = hold
    if cash < 500.0:
        sell_hold = min(sell_hold, 0.32)
    if projected_used > SHED_SOFT:
        sell_hold = min(sell_hold, 0.35)
    operating_need = hire_bill(min(8, max(2, int(math.ceil(n_beasts / 3.0)))))
    operating_need += feed_target * wheat_buy
    if projected_used >= 80 and cash < operating_need:
        sell_hold = min(sell_hold, 0.08)
    if projected_used >= 95 and cash < max(500.0, 0.55 * operating_need):
        sell_hold = 0.0
    feed_keep = feed_target
    keep_wheat = min(int(projected.get("WHEAT", 0) or 0), feed_keep)

    rows = []
    for item, raw_qty in projected.items():
        qty = int(raw_qty or 0)
        if item not in MP or qty <= 0:
            continue
        
        # Dynamic Shed Holding logic
        if item in ("MILK", "WOOL", "MELON", "STRAWBERRY") and spot(item) < PREMIUM_PRICE_FLOOR and projected_used < 90:
            continue
        if item == "WHEAT":
            qty -= keep_wheat
        if qty <= 0:
            continue
        rival_qty = int(math.ceil(max(0.0, opp_wave.get(item, 0.0))))
        if sell_hold <= 0.0:
            n = qty
        else:
            # Maximize immediate score margin, not just our standalone quote.
            # Selling below the normal reservation price is rational when that
            # same batch destroys more value in a larger visible rival wave.
            reservation = max(1.0, sell_hold * MP[item]["base"])
            rival_early, _ = sale_value(item, minv.get(item, I0), rival_qty)
            best_sale = (0.0, 0)
            for candidate_n in range(1, qty + 1):
                own_value, after_ours = sale_value(
                    item, minv.get(item, I0), candidate_n)
                rival_late, _ = sale_value(item, after_ours, rival_qty)
                utility = (own_value - reservation * candidate_n
                           + rival_early - rival_late)
                if utility > best_sale[0]:
                    best_sale = (utility, candidate_n)
            n = best_sale[1]
        if n <= 0:
            continue
        race, exact_value = race_score(item, minv.get(item, I0), n, rival_qty)
        rows.append((race, exact_value, item, n))
    rows.sort(reverse=True)

    # Sales are deliberately first: they can finance later orders and can
    # never be crowded out by a long string of cheap hires. Queue positions are
    # market barriers, so contested crash-prone batches go first according to
    # exact head-to-head margin swing rather than gross stack value.
    for _race, _value, item, n in rows:
        if len(orders) >= 10:
            break
        orders.append(["SELL", item, int(n)])
        average_price = price(item, sim.get(item, I0) + max(0, int(n) // 2))
        cash += int(n) * average_price
        sim[item] = sim.get(item, I0) + int(n)
        projected[item] = max(0, int(projected.get(item, 0)) - int(n))
        projected_used = max(0, projected_used - int(n))

    purchase_orders = 0

    # Feed stock is counted across the shed and all unit inventories.  Feeding
    # actions consume one this turn; deposited wheat is not counted twice.
    feed_actions = sum(1 for op in acts.values() if op and op[0] == "FEED")
    loose_wheat = max(0, carried_wheat - int(deposited.get("WHEAT", 0) or 0))
    total_wheat = max(0, int(projected.get("WHEAT", 0) or 0) + loose_wheat - feed_actions)
    target_wheat = feed_target
    need_wheat = max(0, target_wheat - total_wheat)
    if wheat_buy > WHEAT_BUY_MAX and total_wheat >= unfed:
        need_wheat = 0
    if need_wheat > 0 and len(orders) < 10 and purchase_orders < MAX_BUY_ORDERS:
        room = max(0, SHED_CAP - projected_used)
        n = min(need_wheat, room, 16,
                int(max(0.0, cash - 40.0) // max(1, wheat_buy)))
        if n > 0:
            orders.append(["BUY_PRODUCT", "WHEAT", int(n)])
            cash -= n * wheat_buy
            projected["WHEAT"] = projected.get("WHEAT", 0) + n
            projected_used += n
            purchase_orders += 1

    # Count distinct work, not duplicated crop/species proposals for one tile.
    work_keys = set()
    development = set()
    for _v, tgt, op, _req in jobs:
        name = op[0]
        if name in ("PLANT", "BUILD_COOP", "BUILD_PASTURE", "DIG", "PLACE"):
            key = ("TILE", tgt)
            development.add(tgt)
        elif name in ("WATER", "FEED", "CARE", "HARVEST", "COLLECT_FERTILIZER"):
            key = (name, tgt)
        else:
            continue
        work_keys.add(key)
    open_jobs = len(work_keys)
    footprint = len(plants) + len(beasts)
    hours_available = max(1, TPD - hour - 1)
    per_hand = max(1.0, min(JOBS_PER_UNIT, hours_available * 0.30))
    computed_hands = int(_math.ceil(open_jobs / per_hand)) if open_jobs else 0
    # Dynamic Workforce Scaling: purely scale to open jobs, zero floor.
    want_hands = min(MAX_HANDS, computed_hands)

    # Hires remain profitable after hour zero; cap the window so late hands do
    # not consume Fibonacci wages without enough turns to work.
    if hour <= HIRE_WINDOW and open_jobs and len(orders) < 10:
        n_hired = hires_today
        wheat_on_hand = int(shed.get("WHEAT", 0) or 0) + carried_wheat
        feed_shortfall = max(0, feed_target - wheat_on_hand)
        feed_reserve = max(20.0, feed_shortfall * wheat_buy)
        critical_hands = (min(8, max(2, int(_math.ceil(n_beasts / 3.0))))
                          if n_beasts else min(4, want_hands))
        while (n_hired < want_hands and len(orders) < 10
               and purchase_orders < MAX_BUY_ORDERS):
            c = _fib(n_hired)
            if n_hired >= critical_hands and cash - c < feed_reserve:
                break
            if cash < c:
                break
            if n_hired >= 10 and c > max(55.0, cash * 0.16):
                break
            orders.append(["HIRE"])
            cash -= c
            n_hired += 1
            purchase_orders += 1

    reserve = (max(60.0, feed_target * wheat_buy)
               + 0.35 * hire_bill(min(want_hands, 10))) if days_left > 0 else 0.0

    # Expansion is pressure/ROI driven, with minimum maturity gates.  It tends
    # to open the productive middle quadrants first but skips land that cannot
    # repay before the season ends.
    owned_extra = max(0, len(quads) - 1)
    if (owned_extra < max_quadrants - 1 and days_left >= 7 and len(orders) < 10
            and purchase_orders < MAX_BUY_ORDERS):
        unlock_day = (4, 7, 10)[owned_extra]
        occupied = len(plants) + len(beasts) + len(structs) + len(weeds)
        available = max(1, 25 * len(quads))
        pressure = (occupied + sum(want_crop.values()) + sum(want_animal.values())) / available
        c = LAND_PRICES[owned_extra]
        se_gate = (owned_extra < max_quadrants - 1)
        if (day >= unlock_day and pressure >= 0.66 and cash - c >= reserve
                and se_gate):
            orders.append(["BUY_LAND"])
            cash -= c
            purchase_orders += 1

    # Structures built by a unit this turn exist before these market buys.
    built = {"COOP": 0, "PASTURE": 0}
    for op in acts.values():
        if op and op[0] == "BUILD_COOP":
            built["COOP"] += 1
        elif op and op[0] == "BUILD_PASTURE":
            built["PASTURE"] += 1

    if step < DUMP_STEP:
        animal_rank = []
        for name, desired in want_animal.items():
            y = animal_yield(ANIMALS[name], days_left)
            if not y:
                continue
            unit_value = y[0] * marginal(ANIMALS[name]["prod"]) - ANIMALS[name]["cost"]
            animal_rank.append((unit_value, desired, name))
        animal_rank.sort(reverse=True)
        capacity = {}
        for st in ("COOP", "PASTURE"):
            pending = sum(shed.get(n, 0) + carried.get(n, 0)
                          for n in ANIMALS if ANIMALS[n]["st"] == st)
            capacity[st] = max(0, len(free_struct.get(st, [])) + built[st] - pending)
        for _value, desired, name in animal_rank:
            if len(orders) >= 10 or purchase_orders >= MAX_BUY_ORDERS:
                break
            st = ANIMALS[name]["st"]
            pending = shed.get(name, 0) + carried.get(name, 0)
            need = max(0, desired - pending)
            cost = ANIMALS[name]["cost"]
            room = max(0, SHED_CAP - projected_used)
            n = min(need, capacity.get(st, 0), room, 4,
                    int(max(0.0, cash - reserve) // cost))
            if n <= 0:
                continue
            orders.append(["BUY_ANIMAL", name, int(n)])
            cash -= n * cost
            projected_used += n
            capacity[st] -= n
            purchase_orders += 1

        crop_rank = []
        for crop, desired in want_crop.items():
            y = crop_yield(CROPS[crop], days_left)
            if not y:
                continue
            unit_value = y[0] * marginal(crop) - CROPS[crop]["seed"]
            crop_rank.append((unit_value, desired, crop))
        crop_rank.sort(reverse=True)
        seed_room = max(0, len(empties) + len(weeds) - len(animal_sites)
                        - sum(max(0, int(v or 0)) for v in seeds.values()))
        for _value, desired, crop in crop_rank:
            if len(orders) >= 10 or purchase_orders >= MAX_BUY_ORDERS:
                break
            c = CROPS[crop]["seed"]
            need = max(0, min(desired, len(empties) + len(weeds))
                       - seeds.get(crop, 0))
            n = min(need, seed_room, 16, int(max(0.0, cash - reserve) // c))
            if n <= 0:
                continue
            orders.append(["BUY_SEED", crop, int(n)])
            cash -= n * c
            seed_room -= n
            purchase_orders += 1

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
    print("v36 mirror:", int(last[0].reward), int(last[1].reward))
