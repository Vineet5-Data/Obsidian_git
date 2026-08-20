import math

"""Kaggriculture agent v5.

Every number below was measured against the engine or won a head-to-head duel; the
comments name the experiment so nothing gets "improved" back into a known loss.

Economy (from engine simulation + a 200-run town-drain model):
  * Per tile per season: COW 39 milk > SHEEP 38 wool > MELON 12u/2 waves >
    STRAWBERRY 8u fertilized > GOOSE 56 eggs. CARE triples animal output;
    fertilizer doubles strawberry output.
  * Every premium good is hard-capped by town demand (MILK 437/season, WOOL 331,
    STRAWBERRY 533, MELON 140) and its glut curve floors within 59-158 units, so a
    herd bigger than the drain is worthless. EGG and WHEAT have log glut curves and
    never crash.
  * WHEAT's below-I0 curve is sqrt/0.80: buying wheat raises its own price. Paying
    over $46 for feed cost $20k mean in a sweep, so the cap binds deliberately.

Structure (each fixed a measured failure):
  * 3 quadrants only - the $4,000 SE plot lost 6-0; it drains the animal budget and
    unlocks after strawberries can still be planted.
  * Shed tiles inside locked quadrants are excluded: PICKUP/DROP/PLACE silently no-op
    there (kaggle-environments PR #1391), which was binning 190 PICKUP COW per game.
  * Buy order is melons -> wheat -> land -> animals -> strawberries. Racing to a full
    herd first left us broke on day 4, so land arrived on d10 instead of d7 and we
    fielded 23 strawberries against the reference route's 42.
  * Market orders are slot-budgeted (engine drops everything past 10/turn) with feed
    first; sells are sized by inverting the price curve, and the accepted price floor
    drops as the shed fills, because a full shed blocks buying and stock is worth $0
    at the buzzer.
"""
CROPS = {
    "WHEAT":      {"seed": 10, "first": 2, "maxday": 4, "interval": 0, "max": 6, "ongoing": False},
    "CARROT":     {"seed": 20, "first": 2, "maxday": 3, "interval": 0, "max": 4, "ongoing": False},
    "TOMATO":     {"seed": 50, "first": 8, "maxday": 8, "interval": 1, "max": 4, "ongoing": True},
    "STRAWBERRY": {"seed": 100, "first": 10, "maxday": 10, "interval": 2, "max": 4, "ongoing": True},
    "MELON":      {"seed": 80, "first": 10, "maxday": 12, "interval": 0, "max": 6, "ongoing": False},
}
ANIMALS = {
    "GOOSE": {"cost": 300, "struct": "COOP", "first": 4, "interval": 1, "held": 4, "prod": "EGG"},
    "COW":   {"cost": 400, "struct": "PASTURE", "first": 8, "interval": 2, "held": 6, "prod": "MILK"},
    "SHEEP": {"cost": 500, "struct": "PASTURE", "first": 6, "interval": 3, "held": 6, "prod": "WOOL"},
}
I0 = 10000
PREMIUM = ("MILK", "WOOL", "STRAWBERRY", "MELON", "TOMATO", "CARROT")

# exact copy of the engine's price curve, so we can size an order to a price floor
MP = {
    "WHEAT":      (25, 400, "sqrt", 0.80, "log", 0.20),
    "CARROT":     (35, 450, "log", 0.20, "sqrt", 0.70),
    "TOMATO":     (60, 200, "linear", 0.40, "sqrt", 0.60),
    "STRAWBERRY": (120, 100, "sqrt", 0.70, "linear", 1.60),
    "MELON":      (250, 300, "log", 0.20, "sq", 3.60),
    "EGG":        (50, 332, "linear", 0.40, "log", 0.20),
    "MILK":       (160, 122, "sqrt", 0.60, "linear", 1.60),
    "WOOL":       (200, 105, "log", 0.20, "sq", 3.20),
    "FERTILIZER": (100, 200, "linear", 0.40, "linear", 0.40),
}


def _f(fn, x):
    x = x if x > 0 else 0.0
    if fn == "linear": return x
    if fn == "sq":     return x * x
    if fn == "sqrt":   return x ** 0.5
    return math.log(1.0 + x)


def price_at(item, inv):
    base, T, bf, bt, af, at = MP[item]
    d = inv - I0
    if d < 0:
        return max(1, int(round(base + (bt * base / _f(bf, T)) * _f(bf, -d))))
    return max(1, int(round(base - (at * base / _f(af, T)) * _f(af, d))))


def sell_units(item, inv, have, min_price):
    """Largest n <= have such that every unit sells at >= min_price."""
    lo, hi = 0, have
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if price_at(item, inv + mid - 1) >= min_price:
            lo = mid
        else:
            hi = mid - 1
    return lo

TGT_COW, TGT_SHEEP = 8, 6
TGT_MELON = 12
TGT_STRAW = 50
TGT_WHEAT = 12
MAX_HANDS = 13
LAST_STRAW_DAY = 13
LAST_MELON_DAY = 19
LAST_WHEAT_DAY = 25
STOP_CARE_DAY = 27
STOP_FEED_DAY = 28
SELLOFF_DAY = 27
FERT_SELL_FLOOR = 40
WHEAT_BUY_MAX = 46
WHEAT_CAP = 10
LAND_LAST_DAY = 24
BUY_CHUNK = 14
CARROT_FROM = 12
CARROT_MIN_SLOTS = 3
MAX_EXTRA_QUADS = 2   # the $4,000 SE plot loses 6-0 in duels: it drains the animal
                      # budget and arrives too late to plant strawberries on
EARLY_FLOOR = 300
DIST_PENALTY = 350.0
LAND_FIRST_DAY = 6
LAND_BUFFER = 1500
EARLY_COW_CAP = 4
EARLY_SHEEP_CAP = 2
ANIMAL_RAMP_DAY = 7
STRAW_FROM = 6
FEED_URGENT_MULT = 99.0
LATE_FILL_DAY = 99   # land-fill with wheat measured neutral/negative; kept as a tunable
IDLE_WATER_SCORE = 0     # neutral in duels; kept as a tunable
SELL_SLOTS = 6
HIRE_SLOTS = 5
BUY_SLOTS = 6
WHEAT_PER_ANIMAL = 4
FEED_CAP_HI = 46
FEED_CAP_MID = 46
FEED_CAP_LO = 46
MOVES = {"NORTH": (0, -1), "SOUTH": (0, 1), "EAST": (1, 0), "WEST": (-1, 0)}


def _fib(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def _quad(x, y, n):
    h = n // 2
    return ("NW" if x < h else "NE") if y < h else ("SW" if x < h else "SE")


def _shed_tiles(n):
    h = n // 2
    return [(h - 1, h - 1), (h, h - 1), (h - 1, h), (h, h)]


def _dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def _step_toward(pos, tgt):
    dx, dy = tgt[0] - pos[0], tgt[1] - pos[1]
    if abs(dx) >= abs(dy):
        if dx: return "EAST" if dx > 0 else "WEST"
        if dy: return "SOUTH" if dy > 0 else "NORTH"
    else:
        if dy: return "SOUTH" if dy > 0 else "NORTH"
        if dx: return "EAST" if dx > 0 else "WEST"
    return None


class World:
    def __init__(self, obs):
        self.p = obs.get("player", 0)
        self.farm = obs["farms"][self.p]
        priv = obs.get("private", {}) or {}
        self.n = len(self.farm["tiles"])
        self.day = obs.get("day", 0)
        self.hour = obs.get("hour", 0)
        self.money = self.farm["money"]
        self.tiles = self.farm["tiles"]
        self.shed = dict(priv.get("shed", {}) or {})
        self.seeds = dict(priv.get("seeds", {}) or {})
        self.invs = [dict(i) for i in (priv.get("inventories") or [{}])]
        mkt = obs.get("market", {}) or {}
        self.mkt_inv = mkt.get("inventory", {}) or {}
        self.prices = mkt.get("prices", {}) or {}
        self.quads = set(self.farm.get("unlocked_quadrants") or ["NW"])
        # Hands spawn on any of the four centre tiles, including ones inside quadrants
        # we have not bought. PICKUP/DROP/PLACE all silently no-op on a LOCKED tile
        # (kaggle-environments PR #1391, still open), so those seats are unusable:
        # 190 PICKUP COW and 292 PICKUP WHEAT were being thrown away there.
        self.shed_tiles = [t for t in _shed_tiles(self.n)
                           if self.farm["tiles"][t[1]][t[0]] != "LOCKED"] or [(self.n // 2 - 1,) * 2]
        self.units = [tuple(self.farm["farmer"])] + [tuple(h) for h in (self.farm.get("hands") or [])]
        self.turns_left_today = 24 - self.hour

        self.animals, self.structs, self.plants, self.empty, self.weeds = [], [], [], [], []
        self.counts = {}
        for y in range(self.n):
            for x in range(self.n):
                t = self.tiles[y][x]
                if t == "LOCKED":
                    continue
                if t is None:
                    self.empty.append((x, y))
                elif t.get("kind") == "WEED":
                    self.weeds.append((x, y))
                elif t.get("kind") == "PLANT":
                    self.plants.append(((x, y), t))
                    self.counts[t["crop"]] = self.counts.get(t["crop"], 0) + 1
                elif "animal" in t:
                    self.animals.append(((x, y), t))
                    self.counts[t["animal"]] = self.counts.get(t["animal"], 0) + 1
                else:
                    self.structs.append(((x, y), t))
        self.n_animals = len(self.animals)

    def dist_shed(self, pos):
        return min(_dist(pos, s) for s in self.shed_tiles)


# ------------------------------------------------------------------ agronomy
def needs_water(t, day):
    """Water only when it is survival-critical or yield-positive."""
    if t["watered_today"]:
        return False
    if t.get("consecutive_unwatered", 0) >= 1:
        return True                                    # would turn into a weed tonight
    c = CROPS[t["crop"]]
    age = day - t["planted_day"]
    if not c["ongoing"]:
        return (c["maxday"] + 1) // 2 <= age <= c["maxday"]
    # the production landing at age N is computed at end of day N-1 from that day's water
    nxt = age + 1 - c["first"]
    return nxt >= 0 and nxt % c["interval"] == 0


def wants_fert(t, day):
    """One FERTILIZE covers 3 days => two per strawberry (ages 9 and 13) doubles all four yields."""
    c = CROPS[t["crop"]]
    if not c["ongoing"] or t.get("fertilized_until_day", -1) >= day:
        return False
    age = day - t["planted_day"]
    nxt = age + 1 - c["first"]
    return nxt >= 0 and nxt % (2 * c["interval"]) == 0


def plant_harvestable(t, day):
    c = CROPS[t["crop"]]
    y = t.get("yield_units", 0)
    if y <= 0 or day - t["planted_day"] < c["first"]:
        return False
    if not c["ongoing"]:
        return y >= c["max"] or day - t["planted_day"] >= c["maxday"] or day >= SELLOFF_DAY
    return y >= c["max"] - 1 or day >= SELLOFF_DAY


def animal_harvestable(t, day):
    a = ANIMALS[t["animal"]]
    y = t.get("yield_units", 0)
    return y > 0 and (y >= a["held"] - 2 or day >= SELLOFF_DAY)


# ------------------------------------------------------------------ task list
def build_tasks(w):
    T = []
    feeding = w.day < STOP_FEED_DAY
    caring = w.day < STOP_CARE_DAY
    for pos, t in w.animals:
        if feeding and not t["fed_today"]:
            T.append((10000, pos, "FEED", None))
        if animal_harvestable(t, w.day):
            T.append((5000, pos, "HARVEST", None))
        if caring and t["fed_today"] and not t["cared_today"]:
            T.append((3000, pos, "CARE", None))
        if t.get("fertilizer_available"):
            T.append((2400 if w.day < 10 else 900, pos, "COLLECT_FERTILIZER", None))
    for pos, t in w.plants:
        if needs_water(t, w.day):
            T.append((9000 if t.get("consecutive_unwatered", 0) >= 1 else 2200, pos, "WATER", None))
        elif not t["watered_today"]:
            # Opportunistic top-up. Watering off-schedule adds no yield, but it resets
            # consecutive_unwatered, so a plant survives a day when every unit is busy.
            # The reference top-30 route waters 922 times and ends with 0 weeds; our
            # minimal every-other-day schedule watered 536 times and left 16-41 weeds.
            T.append((IDLE_WATER_SCORE, pos, "WATER", None))
        if plant_harvestable(t, w.day):
            T.append((4000, pos, "HARVEST", None))
        if wants_fert(t, w.day):
            T.append((2600, pos, "FERTILIZE", None))
    for pos in w.weeds:
        T.append((600 if w.day < 24 else 60, pos, "DIG", None))
    return T


def build_placements(w):
    P = []
    pend = {a: w.shed.get(a, 0) + sum(i.get(a, 0) for i in w.invs) for a in ANIMALS}
    free_pen = [p for p, t in w.structs if t["kind"] == "PASTURE"]
    slots = ["COW"] * pend["COW"] + ["SHEEP"] * pend["SHEEP"]
    for pos, animal in zip(free_pen, slots):
        P.append((7000, pos, "PLACE", animal))
    need_pen = max(0, len(slots) - len(free_pen))
    inner = sorted(w.empty, key=w.dist_shed)            # animals hug the shed
    used = set()
    for pos in inner[:need_pen]:
        P.append((6800, pos, "BUILD_PASTURE", None))
        used.add(pos)
    order = []
    if w.day <= LAST_MELON_DAY:
        order += ["MELON"] * w.seeds.get("MELON", 0)
    if w.day <= LAST_STRAW_DAY:
        order += ["STRAWBERRY"] * w.seeds.get("STRAWBERRY", 0)
    if w.day <= LAST_WHEAT_DAY:
        order += ["WHEAT"] * w.seeds.get("WHEAT", 0)
    if w.day <= 26:
        order += ["CARROT"] * w.seeds.get("CARROT", 0)
    outer = [p for p in sorted(w.empty, key=w.dist_shed, reverse=True) if p not in used]
    for crop, pos in zip(order, outer):
        P.append((1800 if crop in ("MELON", "STRAWBERRY") else 1400, pos, "PLANT", crop))
    return P


# ------------------------------------------------------------------ scheduling
def _feasible(jobs, inv, seeds, planted, w):
    for _, op, arg in jobs:
        if op == "FEED" and inv.get("WHEAT", 0) <= 0:
            continue
        if op == "FERTILIZE" and inv.get("FERTILIZER", 0) <= 0:
            continue
        if op == "PLACE" and inv.get(arg, 0) <= 0:
            continue
        if op == "PLANT" and seeds.get(arg, 0) - planted.get(arg, 0) <= 0:
            continue
        return True
    return False


def _take(jobs, inv, seeds, planted):
    for j in list(jobs):
        _, op, arg = j
        if op == "FEED":
            if inv.get("WHEAT", 0) <= 0:
                continue
            inv["WHEAT"] -= 1
        elif op == "FERTILIZE":
            if inv.get("FERTILIZER", 0) <= 0:
                continue
            inv["FERTILIZER"] -= 1
        elif op == "PLACE":
            if inv.get(arg, 0) <= 0:
                continue
            inv[arg] -= 1
        elif op == "PLANT":
            if seeds.get(arg, 0) - planted.get(arg, 0) <= 0:
                continue
            planted[arg] = planted.get(arg, 0) + 1
        elif op == "COLLECT_FERTILIZER":
            inv["FERTILIZER"] = inv.get("FERTILIZER", 0) + 1
        jobs.remove(j)
        return [op] if arg is None else [op, arg]
    return None


def schedule(w):
    by_tile = {}
    for score, pos, op, arg in build_tasks(w) + build_placements(w):
        by_tile.setdefault(pos, []).append((score, op, arg))
    for v in by_tile.values():
        v.sort(reverse=True)

    n = len(w.units)
    acts = [["PASS"] for _ in range(n)]
    claimed = set()
    inv = [dict(w.invs[i]) if i < len(w.invs) else {} for i in range(n)]
    shed = dict(w.shed)
    seeds = dict(w.seeds)
    planted = {}
    unfed = sum(1 for _, t in w.animals if not t["fed_today"]) if w.day < STOP_FEED_DAY else 0
    feed_gap = unfed          # animals still hungry (never consumed by pickups)
    wheat_needed = unfed      # wheat still to be carried out of the shed
    want_fert = sum(1 for _, t in w.plants if wants_fert(t, w.day))
    load = [sum(v for k, v in inv[i].items() if k not in ("WHEAT", "FERTILIZER")) for i in range(n)]

    for i, pos in enumerate(w.units):
        if pos in w.shed_tiles:
            if load[i] and (w.turns_left_today <= 3 or load[i] >= 16):
                acts[i] = ["DROP"]
                continue
            need = min(6, wheat_needed) - inv[i].get("WHEAT", 0)
            if need > 0 and shed.get("WHEAT", 0) > 0:
                k = min(need, shed["WHEAT"])
                shed["WHEAT"] -= k
                inv[i]["WHEAT"] = inv[i].get("WHEAT", 0) + k
                wheat_needed -= k
                acts[i] = ["PICKUP", "WHEAT", k]
                continue
            need = min(4, want_fert) - inv[i].get("FERTILIZER", 0)
            if need > 0 and shed.get("FERTILIZER", 0) > 0:
                k = min(need, shed["FERTILIZER"])
                shed["FERTILIZER"] -= k
                inv[i]["FERTILIZER"] = inv[i].get("FERTILIZER", 0) + k
                want_fert -= k
                acts[i] = ["PICKUP", "FERTILIZER", k]
                continue
            picked = False
            for a in ("COW", "SHEEP", "GOOSE"):
                if shed.get(a, 0) > 0 and not inv[i].get(a):
                    shed[a] -= 1
                    inv[i][a] = 1
                    acts[i] = ["PICKUP", a, 1]
                    picked = True
                    break
            if picked:
                continue
        elif load[i] >= 20 or (w.turns_left_today <= 2 and load[i] > 0):
            mv = _step_toward(pos, min(w.shed_tiles, key=lambda s: _dist(pos, s)))
            acts[i] = [mv] if mv else ["PASS"]
            continue

        here = by_tile.get(pos)
        if here:
            op = _take(here, inv[i], seeds, planted)
            if op:
                acts[i] = op
                if op[0] == "HARVEST":
                    load[i] += 3
                claimed.add(pos)
                continue

        # A unit that is carrying feed is a delivery run, not a general labourer. Without
        # this it wanders off to water a crop, the wheat rides along unused and the herd
        # starves - which is how 6 cows and 3 sheep were lost between day 16 and 22.
        carrying_feed = inv[i].get("WHEAT", 0) > 0 and feed_gap > 0
        best, best_v = None, -1e9
        for tp, jobs in by_tile.items():
            if tp in claimed or tp == pos or not jobs:
                continue
            if carrying_feed and not any(j[1] == "FEED" for j in jobs):
                continue
            if not _feasible(jobs, inv[i], seeds, planted, w):
                continue
            v = jobs[0][0] - DIST_PENALTY * _dist(pos, tp)
            if v > best_v:
                best, best_v = tp, v
        if best is None and carrying_feed:
            for tp, jobs in by_tile.items():
                if tp in claimed or tp == pos or not jobs:
                    continue
                if not _feasible(jobs, inv[i], seeds, planted, w):
                    continue
                v = jobs[0][0] - DIST_PENALTY * _dist(pos, tp)
                if v > best_v:
                    best, best_v = tp, v
        if best is None:
            # nothing actionable: park on the shed ring so next turn can resupply
            best = min(w.shed_tiles, key=lambda s: _dist(pos, s))
        else:
            claimed.add(best)
        mv = _step_toward(pos, best)
        acts[i] = [mv] if mv else ["PASS"]
    return acts


# ------------------------------------------------------------------ market
def market(w):
    """Order slots are the scarce resource here: the engine drops everything past
    maxMarketOrdersPerTurn (10). v2 emitted 6 HIRE + 6 SELL and every seed / feed
    purchase fell off the end of the list, so the wheat crop never got planted and the
    herd starved on day 18. Slots are now budgeted explicitly, feed first."""
    money = w.money
    herd = w.n_animals + sum(w.shed.get(a, 0) for a in ANIMALS) + sum(
        i.get(a, 0) for i in w.invs for a in ANIMALS)
    reserve = (herd + 8) if w.day < STOP_FEED_DAY else 0
    endgame = w.day >= SELLOFF_DAY
    # Day 0 buys animals before it can buy their feed, so 2 sheep starved on day 1.
    # Hold back enough cash on the opening days to cover the first wheat run.
    floor = 0 if endgame else max(EARLY_FLOOR if w.day < 2 else 0, 40 + 25 * herd)
    shed_room = 100 - sum(w.shed.values())

    feed, sells, hires, buys = [], [], [], []

    # --- 1. feed: an unfed cow escapes and takes ~$375/day of output with it --------
    short = reserve - w.shed.get("WHEAT", 0)
    wprice = int(w.prices.get("WHEAT", 99))
    if not endgame and short > 0 and herd > 0 and wprice <= WHEAT_BUY_MAX and shed_room > 2:
        # Topping the shed up to a full reserve every turn ignored the cash floor and
        # held the balance at ~$25 from day 4 to day 10, so NE land and the strawberry
        # block arrived 3 days late. Only a genuine shortfall (under one day of feed)
        # is allowed to spend down to the bone; the rest waits for spare cash.
        urgent = w.shed.get("WHEAT", 0) < herd * FEED_URGENT_MULT
        spendable = (money - 20) if urgent else (money - floor)
        k = min(short, max(0, int(spendable // max(1, wprice))), BUY_CHUNK)
        if k > 0:
            feed.append(["BUY_PRODUCT", "WHEAT", k])
            money -= wprice * k

    # --- 2. sell: stock is worth $0 at the buzzer, and a full shed blocks buying ----
    load = sum(w.shed.values())
    frac = 0.0 if endgame else (0.30 if load >= 85 else (0.55 if load >= 65 else 0.80))
    for item, have in sorted(w.shed.items(), key=lambda kv: -w.prices.get(kv[0], 0) * kv[1]):
        if have <= 0 or item in ANIMALS or item not in MP:
            continue
        if item == "WHEAT":
            have = max(0, have - reserve)
        elif item == "FERTILIZER":
            have = max(0, have - (0 if endgame else (0 if w.day < 8 else 12)))
        if have <= 0:
            continue
        q = sell_units(item, int(w.mkt_inv.get(item, I0)), have,
                       2 if endgame else max(2, int(frac * MP[item][0])))
        if q > 0:
            sells.append(["SELL", item, q])
            money += q * w.prices.get(item, 0)
    sells = sells[:SELL_SLOTS]

    if endgame:
        return (feed + sells)[:10]

    # --- 3. hands: 5 of them cost $12 and carry 120 actions -------------------------
    if w.hour <= 2:
        target = MAX_HANDS if w.day >= 6 else min(MAX_HANDS, 5 + 2 * w.day)
        budget = money - 15
        for k in range(int(w.farm.get("hires_today", 0)), target):
            c = _fib(k)
            if len(hires) >= HIRE_SLOTS or c > budget:
                break
            hires.append(["HIRE"])
            budget -= c
            money -= c

    # --- 4. everything else, in value order ----------------------------------------
    def buy(cost, order, cap=BUY_SLOTS):
        nonlocal money
        if money - cost >= floor and len(buys) < cap:
            buys.append(order)
            money -= cost
            return True
        return False

    slots = max(0, len(w.empty) - sum(w.seeds.get(c, 0) for c in CROPS))

    # Buy order matters more than buy value in the opening. Racing to a full herd left
    # us broke at day 6, so NE land came at d10 instead of d7 and we fielded 23
    # strawberries against the reference route's 42. Melons and land come first now:
    # melons are the day-10 bankroll and land is what makes strawberries plantable.
    have = w.counts.get("MELON", 0) + w.seeds.get("MELON", 0)
    if w.day <= LAST_MELON_DAY and have < TGT_MELON and slots > 0:
        k = min(TGT_MELON - have, slots, int(max(0, money - floor) // 80))
        if k > 0:
            buy(80 * k, ["BUY_SEED", "MELON", k])
            slots -= k

    have = w.counts.get("WHEAT", 0) + w.seeds.get("WHEAT", 0)
    want_wheat = min(WHEAT_CAP, max(TGT_WHEAT, herd + WHEAT_PER_ANIMAL))
    if w.day >= LATE_FILL_DAY:
        want_wheat += slots
    if w.day <= LAST_WHEAT_DAY and have < want_wheat and slots > 0:
        k = min(want_wheat - have, slots, int(max(0, money - floor) // 10))
        if k > 0:
            buy(10 * k, ["BUY_SEED", "WHEAT", k])
            slots -= k

    nq = len(w.quads) - 1
    if nq < MAX_EXTRA_QUADS and LAND_FIRST_DAY <= w.day <= LAND_LAST_DAY:
        cost = (1000, 2000, 4000)[nq]
        if money - cost >= floor + (300 if len(w.empty) < 6 else LAND_BUFFER):
            buy(cost, ["BUY_LAND"])

    n_cow = w.counts.get("COW", 0) + w.shed.get("COW", 0) + sum(i.get("COW", 0) for i in w.invs)
    n_sheep = w.counts.get("SHEEP", 0) + w.shed.get("SHEEP", 0) + sum(i.get("SHEEP", 0) for i in w.invs)
    cow_cap = TGT_COW if w.day >= ANIMAL_RAMP_DAY else min(TGT_COW, EARLY_COW_CAP)
    sheep_cap = TGT_SHEEP if w.day >= ANIMAL_RAMP_DAY else min(TGT_SHEEP, EARLY_SHEEP_CAP)
    if w.day <= 18 and shed_room > 6:
        if n_cow < cow_cap:
            k = min(cow_cap - n_cow, int(max(0, money - floor) // 400), 2)
            if k > 0:
                buy(400 * k, ["BUY_ANIMAL", "COW", k])
        if n_sheep < sheep_cap and n_sheep <= n_cow:
            k = min(sheep_cap - n_sheep, int(max(0, money - floor) // 500), 2)
            if k > 0:
                buy(500 * k, ["BUY_ANIMAL", "SHEEP", k])

    if slots > 0:
        have = w.counts.get("STRAWBERRY", 0) + w.seeds.get("STRAWBERRY", 0)
        if STRAW_FROM <= w.day <= LAST_STRAW_DAY and have < TGT_STRAW:
            k = min(TGT_STRAW - have, slots, int(max(0, money - floor) // 100), 14)
            if k > 0:
                buy(100 * k, ["BUY_SEED", "STRAWBERRY", k])
                slots -= k
        if CARROT_FROM <= w.day <= 26 and slots > CARROT_MIN_SLOTS:
            k = min(slots, int(max(0, money - floor) // 20), 6)
            if k > 0:
                buy(20 * k, ["BUY_SEED", "CARROT", k])

    out = feed + sells + hires + buys
    return out[:10]


def agent(obs):
    w = World(obs)
    acts = schedule(w)
    return {"farmer": acts[0] if acts else ["PASS"], "hands": acts[1:], "market": market(w)}
