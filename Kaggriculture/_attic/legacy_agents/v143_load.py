"""v132 -- residual-market animal species allocator on the v128 frontier.

v128 is the validated frontier at 1132-468 (70.8%). v129, v130 and v131
changed assignment or late service timing and all failed to move the economic
frontier. The remaining loss pattern is set before day 20: the baseline reaches
its 16-animal target while operating materially fewer crop tiles, and then loses
the shared-market cash wave. Broad herd reduction is closed by v121.

Single policy change:
  * keep v128's exact animal TARGET / number of animal slots;
  * compute the literal v128 species plan first, so purchase authorization is
    unchanged;
  * reallocate only those purchasable animal slots across COW/SHEEP/GOOSE by
    projected incremental terminal revenue under residual shared-market supply;
  * current own + discounted visible rival future supply depresses the candidate
    product's expected realized price; currently unlocked shops + town-center
    demand relieve that pressure; unknown future shops are not guessed;
  * each selected animal updates projected supply, so repeated selection of a
    species self-limits on the exact product price curve;
  * species_cap remains unchanged and total animal-slot count is preserved.

No herd-size reduction, crop-policy change, service-priority change, worker
change, route change, fertilizer-denial change, sale-policy change, or replay /
opponent-ID logic is introduced. The intervention changes only WHICH species
fills animal purchases that v128 already authorized.
"""

import math

BOARD = 10
TPD = 24
I0 = 10000
LAST_DAY = 29
LAST_STEP = 719
CASH_WAVE_END_DAY = 24  # loss analysis: first decisive opponent cash wave is days 20-24

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
JOBS_PER_UNIT = 4.0      # conservative allowance for walking between tile ops
HOLD_EARLY = 0.62
HOLD_LATE = 0.12
RELAX_DAY = 18
DUMP_STEP = 648          # day 27: cash out while workers can still reach the shed
FINAL_FARM_STEP = 696    # last day is harvest/collection/liquidation only
SERVICE_CONGESTION_STEP = 15 * TPD
SERVICE_CONGESTION_END_STEP = 20 * TPD
FERTILIZER_CURRENT_UNIT_MULTIPLIER = 4.0
SHED_SOFT = 50
FEED_CARRY = 5
FERT_CARRY = 5
HUNGARIAN_JOBS = 48      # columns in the worker-to-job assignment matrix
FEED_DAYS = 1
FEED_BUFFER = 0.80
MAX_BUY_ORDERS = 5
WHEAT_BUY_MAX = 45
CROP_CAP_EARLY = 0.42   # share of the portfolio one crop may hold
CROP_CAP_LATE = 0.52
SKIP_CROPS = frozenset()   # crops never allocated a new tile
MOVE_FRAC = 1.5          # worker-turn opportunity cost, as a share of the
                         # top available job values

SERVICE_OPERATIONS = frozenset((
    "FEED", "CARE", "WATER", "FERTILIZE", "HARVEST",
    "COLLECT_FERTILIZER", "PLANT",
))
_TELEMETRY_ACTIVE = {}
_TELEMETRY_COMPLETED = []
_TELEMETRY_EPISODE = 0


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


def one_unit_denial_bonus(item, inv, rival_qty):
    """Revenue removed from a visible rival batch by injecting one unit first.

    This is deliberately only the opponent externality.  The value of our own
    incremental crop unit is already present in the FERTILIZE job score.
    """
    rival_qty = max(0, int(math.ceil(float(rival_qty or 0))))
    if item not in MP or rival_qty <= 0:
        return 0.0
    _ours, after_ours = sale_value(item, int(inv), 1)
    rival_early, _ = sale_value(item, int(inv), rival_qty)
    rival_late, _ = sale_value(item, after_ours, rival_qty)
    return max(0.0, float(rival_early - rival_late))


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
    harvest_day = min(cd["myd"], days_left)
    if harvest_day < cd["fyd"]:
        return None
    waters = harvest_day - (cd["myd"] + 1) // 2 + 1
    return min(cd["my"], 1 + waters), 2 + waters, harvest_day


def crop_season(cd, days_left):
    """Value every complete cycle a tile can still finish this season."""
    y = crop_yield(cd, days_left)
    if not y:
        return None
    units, actions, _span = y
    cycles = 1 if cd["ong"] else max(1, int(days_left // max(1, cd["myd"])))
    # For ongoing crops that are fertilized (Strawberry, Tomato), yields are doubled
    # in practice. We use a 1.75x multiplier to reflect realistic fertilized yields.
    yield_multiplier = 1.75 if cd["ong"] else 1.0
    return units * yield_multiplier * cycles, actions * cycles, float(cd["seed"]) * cycles


def remaining_feed_requirement(day, n_beasts):
    """Feed units potentially required before the existing FINAL_FARM_STEP."""
    last_feed_day = max(-1, (FINAL_FARM_STEP - 1) // TPD)
    feed_days = max(0, last_feed_day - int(day) + 1)
    return max(0, int(n_beasts)) * feed_days


def late_project_economics(crop, day, sim_market_supply, sim_own_supply,
                           absorb, minv, wheat_buy, feed_requirement):
    """Incremental terminal economics for one new late crop tile.

    Returns (coins_per_action, net_coins, units, actions, seed_cost), or None
    when the crop cannot finish useful output or has non-positive terminal value.
    """
    cd = CROPS.get(crop)
    if not cd:
        return None
    y = crop_season(cd, max(0, LAST_DAY - int(day)))
    if not y:
        return None
    units, actions, seed_cost = y
    units = max(0, int(units))
    actions = max(1.0, float(actions))
    seed_cost = float(seed_cost)
    if units <= 0:
        return None

    feed_units = 0
    if crop == "WHEAT":
        own_wheat = max(0.0, float(sim_own_supply.get("WHEAT", 0.0)))
        shortfall = max(0.0, float(feed_requirement) - own_wheat)
        if shortfall > 1e-12:
            feed_units = min(units, int(math.ceil(shortfall - 1e-12)))

    sale_units = max(0, units - feed_units)
    overhang = max(0.0, float(sim_market_supply.get(crop, 0.0))
                   - float(absorb.get(crop, 0.0)))
    start_inv = int(minv.get(crop, I0) + math.floor(overhang))
    sale_coins, _ = sale_value(crop, start_inv, sale_units)
    replacement_value = feed_units * max(1, int(wheat_buy))
    net = float(sale_coins + replacement_value) - seed_cost
    if net <= 0.0:
        return None
    return net / actions, net, units, actions, seed_cost


def late_terminal_crop_mix(day, project_slots, market_supply, own_supply, absorb,
                           minv, wheat_buy, n_beasts):
    """Reallocate a FIXED legacy project count by terminal coins/action.

    Keeping project_slots equal to v126's original want_crop count prevents the
    visual diagnosis from being misread as a request for more labor or a larger
    farm. Each selected project updates projected supply so its own market impact
    reduces the value of selecting another identical tile.
    """
    slots = max(0, int(project_slots))
    want = {}
    sim_market = dict(market_supply)
    sim_own = dict(own_supply)
    feed_requirement = remaining_feed_requirement(day, n_beasts)

    for _ in range(slots):
        best = None
        for crop in CROPS:
            if crop in SKIP_CROPS:
                continue
            econ = late_project_economics(
                crop, day, sim_market, sim_own, absorb, minv, wheat_buy,
                feed_requirement)
            if econ is None:
                continue
            score, net, units, actions, seed_cost = econ
            row = (score, net, -actions, crop, units, seed_cost)
            if best is None or row > best:
                best = row
        if best is None:
            break
        _score, _net, _neg_actions, crop, units, _seed_cost = best
        want[crop] = want.get(crop, 0) + 1
        sim_market[crop] = sim_market.get(crop, 0.0) + units
        sim_own[crop] = sim_own.get(crop, 0.0) + units

    return want


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


def forecast_known_absorption(shops, steps_left):
    """Remaining demand from shops visible NOW plus the town center only.

    Unknown future shops are genuine uncertainty.  For species selection, do not
    convert that uncertainty into a hidden seed classifier; react only to public
    demand already revealed in the current state.
    """
    absorb = dict.fromkeys(PRODUCTS, 0.0)
    for shop in shops:
        prods = SHOPS.get(shop)
        if not prods:
            continue
        mult = 2.0 if len(prods) == 1 else 1.0
        for item in prods:
            absorb[item] += mult * max(0, steps_left) / 4.0
    center_ticks = max(0, steps_left) / float(TPD)
    for item in TOWN_CENTER:
        absorb[item] += center_ticks
    return absorb


def projected_incremental_revenue(item, current_inventory, background_supply,
                                  known_demand, candidate_units):
    """Projected candidate revenue on the exact v128 product price curve.

    Existing own supply, visible-rival supply and public town drain are spread
    over the candidate's production horizon instead of pretending that every
    background unit arrives before (or after) us.  The only approximation is the
    timing interpolation; every quoted unit uses the exact local price().
    """
    n = max(0, int(candidate_units or 0))
    if n <= 0:
        return 0.0
    background_net = float(background_supply or 0.0) - float(known_demand or 0.0)
    revenue = 0.0
    for i in range(n):
        frac = (i + 0.5) / float(n)
        inv = float(current_inventory) + frac * background_net + i
        revenue += price(item, inv)
    return revenue


def residual_species_economics(name, days_left, sim_supply, known_absorb, minv):
    """Return (coins/action, net coins, units, actions, revenue) for one animal.

    The total herd size is held fixed, so FEED, CARE and daily fertilizer
    collection are common costs across species.  They therefore cancel in the
    species argmax.  We still include those common worker actions in the
    denominator so the ranking is value-per-committed-service-capacity; the only
    species-specific cash terms are product revenue and purchase cost.
    """
    a = ANIMALS.get(name)
    if not a:
        return None
    y = animal_yield(a, days_left)
    if not y:
        return None
    units = max(0, int(y[0]))
    if units <= 0:
        return None
    product = a["prod"]
    revenue = projected_incremental_revenue(
        product, minv.get(product, I0), sim_supply.get(product, 0.0),
        known_absorb.get(product, 0.0), units)
    feed_cost = max(0, int(days_left)) * 25.0
    net = float(revenue) - float(a["cost"]) - feed_cost

    # Minimal lifecycle burden for comparison. FEED+CARE+fertilizer-collection
    # are common daily obligations; HARVEST frequency differs by species.
    daily_common = 3.0 * max(0, int(days_left))
    harvest_actions = int(math.ceil(units / float(max(1, a["mh"]))))
    actions = max(1.0, daily_common + harvest_actions)
    return net / actions, net, units, actions, revenue


def allocate_residual_species(slot_count, days_left, species_cap,
                              own_animal_counts, shed, carried_all,
                              base_supply, known_absorb, minv):
    """Reallocate a FIXED number of parent-authorized animal slots by residual NPV.

    Species counts self-limit because every selected candidate immediately adds
    its projected units to sim_supply before the next slot is scored.
    """
    slots = max(0, int(slot_count or 0))
    want = {}
    sim_supply = dict(base_supply)
    for _ in range(slots):
        best = None
        for name in ANIMALS:
            already = (int(own_animal_counts.get(name, 0) or 0)
                       + int(shed.get(name, 0) or 0)
                       + int(carried_all.get(name, 0) or 0)
                       + int(want.get(name, 0) or 0))
            if already >= species_cap:
                continue
            econ = residual_species_economics(
                name, days_left, sim_supply, known_absorb, minv)
            if econ is None:
                continue
            score, net, units, actions, revenue = econ
            if net <= 0:
                continue
            # Deterministic economic tie-breakers; no fixed species preference.
            row = (score, net, revenue, -actions, name, units)
            if best is None or row > best:
                best = row
        if best is None:
            break
        _score, _net, _rev, _neg_actions, name, units = best
        want[name] = want.get(name, 0) + 1
        product = ANIMALS[name]["prod"]
        sim_supply[product] = sim_supply.get(product, 0.0) + units
    return want, sim_supply


def aggregate_inventories(inventories):
    """Return positive quantities carried by all controlled units."""
    carried = {}
    for inv in inventories:
        for item, qty in dict(inv or {}).items():
            qty = int(qty or 0)
            if qty > 0:
                carried[item] = carried.get(item, 0) + qty
    return carried


def scan_board(tiles, shed_access_set):
    """Classify board tiles and preserve v110's empty-tile ordering."""
    plants, beasts, empties, weeds, structs = [], [], [], [], []
    for y in range(min(BOARD, len(tiles))):
        row = tiles[y] or []
        for x in range(min(BOARD, len(row))):
            tile = row[x]
            if tile is None:
                empties.append((x, y))
                continue
            if not isinstance(tile, dict):
                continue
            kind = tile.get("kind")
            if kind == "PLANT":
                plants.append((x, y, tile))
            elif "animal" in tile:
                beasts.append((x, y, tile))
            elif kind == "WEED":
                weeds.append((x, y))
            elif kind in ("COOP", "PASTURE"):
                structs.append((x, y, kind))
    empties.sort(key=lambda p: (min(dist(p, s) for s in shed_access_set),
                                p[1], p[0]))
    return plants, beasts, empties, weeds, structs


def forecast_absorption(shops, steps_left):
    """Estimate remaining public demand exactly as v110 did inline."""
    absorb = dict.fromkeys(PRODUCTS, 0.0)
    for shop in shops:
        prods = SHOPS.get(shop)
        if not prods:
            continue
        mult = 2.0 if len(prods) == 1 else 1.0
        for item in prods:
            absorb[item] += mult * steps_left / 4.0
    center_ticks = steps_left / float(TPD)
    for item in TOWN_CENTER:
        absorb[item] += center_ticks
    unknown = max(0, min(MAX_SHOPS, LAST_DAY // 3) - len(shops))
    if unknown > 0:
        for prods in SHOPS.values():
            mult = 2.0 if len(prods) == 1 else 1.0
            for item in prods:
                absorb[item] += (mult * unknown * steps_left * 0.5
                                 / (4.0 * len(SHOPS)))
    return absorb


def forecast_own_supply(shed, carried_all, plants, beasts, day, days_left):
    """Project already committed inventory and future production."""
    supply = dict.fromkeys(PRODUCTS, 0.0)
    for item, qty in shed.items():
        if item in supply:
            supply[item] += qty
    for item, qty in carried_all.items():
        if item in supply:
            supply[item] += qty
    for _, _, tile in plants:
        crop = tile.get("crop")
        cd = CROPS.get(crop)
        if not cd:
            continue
        held = int(tile.get("yield_units", 0) or 0)
        age = day - int(tile.get("planted_day", day) or 0)
        future = 0
        if cd["ong"]:
            interval = max(1, cd["iv"])
            produced = (1 + max(0, age - cd["fyd"]) // interval
                        if age >= cd["fyd"] else 0)
            future = max(0, cd["my"] - produced)
            if age < cd["fyd"]:
                horizon = max(0, days_left - max(0, cd["fyd"] - age))
                future = min(future, 1 + horizon // interval)
            else:
                future = min(future, days_left // interval + 1)
        elif age <= cd["myd"] and cd["myd"] - age <= days_left:
            future = max(0, cd["my"] - held)
        supply[crop] += held + future
    for _, _, tile in beasts:
        animal = ANIMALS.get(tile.get("animal"))
        if not animal:
            continue
        age = day - int(tile.get("placed_day", day) or 0)
        due, ticks = max(0, animal["fyd"] - age), 0
        while due <= days_left:
            ticks += 1
            due += max(1, animal["iv"])
        first = min(animal["mh"], 1 + max(0, animal["fyd"] - age))
        later = min(animal["mh"], 1 + max(1, animal["iv"]))
        future = first + max(0, ticks - 1) * later if ticks else 0
        supply[animal["prod"]] += int(tile.get("yield_units", 0) or 0) + future
    return supply


def count_owned_assets(plants, beasts, day):
    """Count raw and day-20..24-wave-ready owned assets."""
    crop_counts = {name: 0 for name in CROPS}
    wave_ready = {name: 0 for name in CROPS}
    animal_counts = {name: 0 for name in ANIMALS}
    for _, _, tile in plants:
        crop = tile.get("crop")
        if crop not in crop_counts:
            continue
        crop_counts[crop] += 1
        cd = CROPS[crop]
        planted_day = tile.get("planted_day", day)
        planted_day = day if planted_day is None else int(planted_day)
        maturity = cd["fyd"] if cd["ong"] else cd["myd"]
        if planted_day + maturity <= CASH_WAVE_END_DAY:
            wave_ready[crop] += 1
    for _, _, tile in beasts:
        name = tile.get("animal")
        if name in animal_counts:
            animal_counts[name] += 1
    return crop_counts, wave_ready, animal_counts


def animal_allocation_limits(day, days_left, quadrant_count, slots,
                             beast_count, struct_count, pending_animals):
    """Return proportional herd target based on crop footprint."""
    current_assets = beast_count + struct_count
    
    if days_left < 8:
        target = current_assets
    elif day < 15:
        target = 16
    else:
        target = min(20, max(6, int(round(25 * quadrant_count * 0.22))))
    need = max(0, target - beast_count - pending_animals)
    structure_need = min(slots, max(0, target - current_assets))
    species_cap = max(2, int(math.ceil(max(1, target) * 0.70)))
    return target, need, structure_need, species_cap


def hold_fraction(step, day, shed_used):
    """Compute the inventory reservation fraction for the current phase."""
    if step >= DUMP_STEP:
        hold = 0.0
    elif day < RELAX_DAY:
        hold = HOLD_EARLY
    else:
        phase = (day - RELAX_DAY) / float(max(1, LAST_DAY - RELAX_DAY))
        hold = HOLD_EARLY + (HOLD_LATE - HOLD_EARLY) * phase
    if shed_used > SHED_SOFT:
        hold = min(hold, 0.40)
    return hold


def project_shed_after_actions(shed, shed_used, actions, inventories,
                               positions, shed_access_set):
    """Project same-turn deposits and pickups before market orders execute."""
    projected = dict(shed)
    projected_used = shed_used
    deposited = {}
    for idx in sorted(actions):
        if idx >= len(inventories):
            continue
        op = actions[idx]
        pos = positions.get(idx, (4, 4))
        inv = dict(inventories[idx] or {})
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
    return projected, projected_used, deposited


def adjusted_sell_hold(base_hold, cash, projected_used, n_beasts,
                       feed_target, wheat_buy):
    """Relax the reservation price when cash or storage is stressed."""
    sell_hold = base_hold
    if cash < 500.0:
        sell_hold = min(sell_hold, 0.32)
    if projected_used > SHED_SOFT:
        sell_hold = min(sell_hold, 0.35)
    operating_need = hire_bill(min(8, max(2, int(math.ceil(n_beasts / 3.0)))))
    operating_need += feed_target * wheat_buy
    # Keep the validated parent's cash gate here.  v125 removed this condition
    # and drained the shed on storage pressure alone; that raised our own score
    # but also lifted the shared STRAWBERRY price enough to benefit the rival
    # much more.  v126 deliberately abandons that mechanism.
    if projected_used >= 80 and cash < operating_need:
        sell_hold = min(sell_hold, 0.08)
    if projected_used >= 95:
        sell_hold = 0.0
    return sell_hold


def rank_sales(projected, minv, opp_wave, sell_hold, keep_wheat, step):
    """Choose and order sell batches without mutating projected inventory."""
    rows = []
    for item, raw_qty in projected.items():
        qty = int(raw_qty or 0)
        if item not in MP or qty <= 0:
            continue
        if item == "WHEAT":
            qty -= keep_wheat
        if qty <= 0:
            continue
        rival_qty = int(math.ceil(max(0.0, opp_wave.get(item, 0.0))))
        if sell_hold <= 0.0:
            amount = qty
        else:
            reservation = max(
                1.0, (0.0 if step >= DUMP_STEP else sell_hold) * MP[item]["base"])
            if item == "STRAWBERRY" and rival_qty > 0:
                reservation = 1.0
            rival_early, _ = sale_value(item, minv.get(item, I0), rival_qty)
            best_sale = (0.0, 0)
            for candidate in range(1, qty + 1):
                own_value, after_ours = sale_value(
                    item, minv.get(item, I0), candidate)
                rival_late, _ = sale_value(item, after_ours, rival_qty)
                utility = (own_value - reservation * candidate
                           + rival_early - rival_late)
                if utility > best_sale[0]:
                    best_sale = (utility, candidate)
            amount = best_sale[1]
        if amount <= 0:
            continue
        race, exact_value = race_score(
            item, minv.get(item, I0), amount, rival_qty)
        rows.append((race, exact_value, item, amount))
    rows.sort(reverse=True)
    return rows


def feed_stock_need(projected_wheat, carried_wheat, deposited_wheat,
                    feed_actions, feed_target, unfed, wheat_buy):
    """Calculate wheat remaining after this turn and the necessary purchase."""
    loose_wheat = max(0, carried_wheat - deposited_wheat)
    total_wheat = max(0, int(projected_wheat or 0) + loose_wheat - feed_actions)
    need_wheat = max(0, feed_target - total_wheat)
    if wheat_buy > WHEAT_BUY_MAX and total_wheat >= unfed:
        need_wheat = 0
    return total_wheat, need_wheat


def summarize_job_board(jobs):
    """Count distinct current work and expose operation-level diagnostics."""
    work_keys = set()
    development = set()
    by_operation = {}
    for _value, target, op, _requirement in jobs:
        name = op[0]
        if name in ("PLANT", "BUILD_COOP", "BUILD_PASTURE", "DIG", "PLACE"):
            key = ("TILE", target)
            development.add(target)
        elif name in ("WATER", "FEED", "CARE", "HARVEST",
                     "COLLECT_FERTILIZER", "FERTILIZE"):
            key = (name, target)
        elif name == "PICKUP" and len(op) > 1 and op[1] in ("WHEAT", "FERTILIZER"):
            key = (name, op[1], target)
        else:
            continue
        work_keys.add(key)
        by_operation.setdefault(name, set()).add(key)
    return {
        "open_jobs": len(work_keys),
        "development_tiles": len(development),
        "by_operation": {name: len(keys) for name, keys in by_operation.items()},
    }


def workforce_target(jobs, day, hour, footprint):
    """Return desired hands plus the inspectable demand summary."""
    summary = summarize_job_board(jobs)
    open_jobs = summary["open_jobs"]
    hours_available = max(1, TPD - hour - 1)
    per_hand = max(1.0, min(JOBS_PER_UNIT, hours_available * 0.30))
    computed = int(math.ceil(open_jobs / per_hand)) if open_jobs else 0
    if open_jobs and day < LAST_DAY:
        floor = min(10, 6 + footprint // 15
                    + min(2, summary["development_tiles"] // 12))
    elif open_jobs:
        floor = min(7, max(2, int(math.ceil(open_jobs / 3.0))))
    else:
        floor = 0
    return min(MAX_HANDS, max(computed, floor)), summary


def built_structure_counts(actions):
    """Count structures that will exist before same-turn animal purchases."""
    built = {"COOP": 0, "PASTURE": 0}
    for op in actions.values():
        if op and op[0] == "BUILD_COOP":
            built["COOP"] += 1
        elif op and op[0] == "BUILD_PASTURE":
            built["PASTURE"] += 1
    return built


def collect_fertilizer_value(product_price, step):
    """Value the ready unit plus one buffer-unblocking replacement opportunity."""
    multiplier = FERTILIZER_CURRENT_UNIT_MULTIPLIER
    if SERVICE_CONGESTION_STEP <= step < SERVICE_CONGESTION_END_STEP:
        multiplier += 1.0
    return multiplier * product_price


def animal_service_jobs(x, y, tile, step, spot):
    """Build current FEED/CARE/HARVEST/COLLECT jobs for one animal."""
    animal = ANIMALS.get(tile.get("animal"))
    if not animal:
        return [], 0
    jobs = []
    product_price = spot(animal["prod"])
    held = int(tile.get("yield_units", 0) or 0)
    if held > 0:
        near_cap = held >= animal["mh"] - 1
        terminal = 5.0 if step >= DUMP_STEP else 1.0
        harvest_price = (0.0 if (product_price < 50
                         and animal["prod"] in
                         ("MELON", "STRAWBERRY", "MILK", "WOOL"))
                         else product_price)
        jobs.append((held * harvest_price * (2.0 if near_cap else 1.0)
                     * terminal, (x, y), ["HARVEST"], None))
    if tile.get("fertilizer_available"):
        jobs.append((collect_fertilizer_value(spot("FERTILIZER"), step),
                     (x, y), ["COLLECT_FERTILIZER"], None))
    unfed = 0
    if step < FINAL_FARM_STEP and not tile.get("fed_today"):
        unfed = 1
        starving = int(tile.get("consecutive_unfed", 0) or 0) >= 1
        jobs.append(((14.0 if starving else 2.2) * product_price,
                     (x, y), ["FEED"], "WHEAT"))
    if step < FINAL_FARM_STEP and not tile.get("cared_today"):
        jobs.append((0.95 * product_price, (x, y), ["CARE"], None))
    return jobs, unfed


def crop_service_jobs(x, y, tile, step, day, storage_load, spot,
                      opponent_crop_counts, opponent_wave=None, market_inv=None):
    """Build current WATER/FERTILIZE/HARVEST jobs for one crop tile."""
    cd = CROPS.get(tile.get("crop"))
    if not cd:
        return [], 0
    jobs = []
    product_price = spot(tile["crop"])
    age = day - int(tile.get("planted_day", day) or 0)
    held = int(tile.get("yield_units", 0) or 0)
    if held > 0 and age >= cd["fyd"]:
        terminal = 5.0 if step >= DUMP_STEP else 1.0
        try:
            lifespan = int(tile.get("max_lifespan_step", -1) or -1)
        except (TypeError, ValueError):
            lifespan = -1
        expiring = 0 <= lifespan <= step + TPD
        at_cap = cd["ong"] and held >= cd["my"]

        if (product_price < 50
                and tile["crop"] in ("MELON", "STRAWBERRY", "MILK", "WOOL")):
            if at_cap and not expiring:
                harvest_price = max(
                    product_price,
                    hold_fraction(step, day, storage_load) * MP[tile["crop"]]["base"])
            else:
                harvest_price = float(product_price)
        else:
            harvest_price = float(product_price)
        base_gain = (held * harvest_price + (14 if not cd["ong"] else 0)) * terminal
        gain = base_gain
        if storage_load > 90:
            gain *= 0.1
        jobs.append((gain, (x, y), ["HARVEST"], None))
        if expiring and base_gain < 25.0:
            jobs.append((25.0, (x, y), ["DIG"], None))

    fertilizer_jobs = 0
    if (step < FINAL_FARM_STEP and cd["ong"]
            and int(tile.get("fertilized_until_day", -1) or -1) < day):
        planted_day = tile.get("planted_day", day)
        planted_day = day if planted_day is None else int(planted_day)
        since_first = day + 1 - planted_day - cd["fyd"]
        due = (since_first >= 0 and since_first % max(1, cd["iv"]) == 0
               and since_first // max(1, cd["iv"]) < cd["my"])
        fertilizer_spot = spot("FERTILIZER")
        incremental = product_price - fertilizer_spot
        crop_name = tile.get("crop")
        strategic_denial = (crop_name in ("STRAWBERRY", "TOMATO")
                            and opponent_crop_counts.get(crop_name, 0) > 0)
        if due and (incremental > 12.0 or strategic_denial):
            fertilizer_jobs = 1
            denial_bonus = 0.0
            if (crop_name == "STRAWBERRY" and strategic_denial
                    and opponent_wave is not None and market_inv is not None):
                denial_bonus = one_unit_denial_bonus(
                    crop_name, market_inv.get(crop_name, I0),
                    opponent_wave.get(crop_name, 0.0))
            jobs.append((max(80.0, 2.0 * product_price - fertilizer_spot
                             + denial_bonus),
                         (x, y), ["FERTILIZE"], "FERTILIZER"))

    if step < FINAL_FARM_STEP and not tile.get("watered_today"):
        if cd["ong"]:
            gain = float(product_price)
        else:
            water_start = (cd["myd"] + 1) // 2
            gain = float(product_price) if water_start <= age <= cd["myd"] else 0.0
        # If it's in the bonus window, give it a large gain so we don't miss it
        if not cd["ong"] and water_start <= age <= cd["myd"]:
            gain += 1000.0 + product_price
        if int(tile.get("consecutive_unwatered", 0) or 0) >= 1:
            gain += 50000.0 + 3.0 * product_price * max(1, cd["my"] - held)
        if gain > 0:
            jobs.append((gain, (x, y), ["WATER"], None))
    return jobs, fertilizer_jobs


def critical_feed_actions(units, inventories, beasts, step, hour):
    """Match wheat carriers to animals facing a second missed-feed day."""
    targets = [(x, y) for x, y, tile in beasts
               if (step < FINAL_FARM_STEP and not tile.get("fed_today")
                   and int(tile.get("consecutive_unfed", 0) or 0) >= 1)]
    positions = dict(units)
    feasible = {}
    pairs = []
    remaining_today = max(0, TPD - hour - 1)
    for idx, pos in units:
        inv = dict(inventories[idx] or {}) if idx < len(inventories) else {}
        if int(inv.get("WHEAT", 0) or 0) <= 0:
            continue
        for target in targets:
            distance = dist(pos, target)
            if distance <= remaining_today:
                feasible[target] = feasible.get(target, 0) + 1
                pairs.append((distance, idx, target))
    pairs.sort(key=lambda row: (feasible.get(row[2], 999), row[0],
                                row[2][1], row[2][0], row[1]))
    forced, used_units, used_targets = {}, set(), set()
    for distance, idx, target in pairs:
        if idx in used_units or target in used_targets:
            continue
        forced[idx] = (["FEED"] if distance == 0
                       else step_toward(positions[idx], target))
        used_units.add(idx)
        used_targets.add(target)
    return forced


def _increment(mapping, key, amount=1):
    mapping[key] = mapping.get(key, 0) + amount


def _new_telemetry_episode(seat, step):
    global _TELEMETRY_EPISODE
    _TELEMETRY_EPISODE += 1
    episode = {
        "episode_id": _TELEMETRY_EPISODE,
        "seat": seat,
        "first_step": step,
        "last_step": step,
        "days": {},
        "pending": [],
    }
    _TELEMETRY_ACTIVE[seat] = episode
    return episode


def reset_telemetry():
    """Clear all diagnostics without changing policy state."""
    global _TELEMETRY_EPISODE
    _TELEMETRY_ACTIVE.clear()
    _TELEMETRY_COMPLETED[:] = []
    _TELEMETRY_EPISODE = 0


def _day_telemetry(episode, day):
    days = episode["days"]
    if day not in days:
        days[day] = {
            "turns": 0,
            "created": {},
            "admitted": {},
            "assigned": {},
            "emitted": {},
            "executed": {},
            "failed": {},
            "unknown": {},
            "movement_turns": 0,
            "pass_turns": 0,
            "animal_cap_ticks": {},
            "crop_expiry_with_yield": {},
        }
    return days[day]


def _tile_at(tiles, target):
    try:
        x, y = target
        tile = tiles[y][x]
    except (IndexError, KeyError, TypeError, ValueError):
        return {}
    return tile if isinstance(tile, dict) else {}


def _operation_succeeded(pending, tiles):
    """Reconcile a directly emitted tile operation from the next observation."""
    op = pending["operation"]
    before = pending["before"]
    after = _tile_at(tiles, pending["target"])
    if op == "WATER":
        return bool(after.get("watered_today")) or (
            int(after.get("consecutive_unwatered", 99) or 99)
            < int(before.get("consecutive_unwatered", 99) or 99))
    if op == "FEED":
        return bool(after.get("fed_today")) or (
            int(after.get("consecutive_unfed", 99) or 99)
            < int(before.get("consecutive_unfed", 99) or 99))
    if op == "CARE":
        return bool(after.get("cared_today"))
    if op == "HARVEST":
        return int(after.get("yield_units", 0) or 0) < int(
            before.get("yield_units", 0) or 0)
    if op == "COLLECT_FERTILIZER":
        return (bool(before.get("fertilizer_available"))
                and not bool(after.get("fertilizer_available")))
    if op == "FERTILIZE":
        return int(after.get("fertilized_until_day", -1) or -1) > int(
            before.get("fertilized_until_day", -1) or -1)
    if op == "PLANT":
        return after.get("crop") == pending.get("argument")
    return None


def _telemetry_begin(seat, step, tiles):
    """Open/reset an episode and reconcile last turn's direct operations."""
    episode = _TELEMETRY_ACTIVE.get(seat)
    if episode is None or step <= episode["last_step"]:
        if episode is not None:
            archived = dict(episode)
            archived.pop("pending", None)
            _TELEMETRY_COMPLETED.append(archived)
        episode = _new_telemetry_episode(seat, step)
    pending_rows = episode.get("pending", [])
    for pending in pending_rows:
        emitted_step = pending["step"]
        emitted_day = emitted_step // TPD
        row = _day_telemetry(episode, emitted_day)
        if step != emitted_step + 1:
            _increment(row["unknown"], pending["operation"])
            continue
        succeeded = _operation_succeeded(pending, tiles)
        if succeeded is True:
            _increment(row["executed"], pending["operation"])
        elif succeeded is False:
            _increment(row["failed"], pending["operation"])
        else:
            _increment(row["unknown"], pending["operation"])
    episode["pending"] = []
    episode["last_step"] = step
    return episode


def _count_jobs_by_operation(jobs):
    counts = {}
    for _value, _target, operation, _requirement in jobs:
        if operation and operation[0] in SERVICE_OPERATIONS:
            _increment(counts, operation[0])
    return counts


def _telemetry_record(episode, step, tiles, beasts, plants, created_jobs,
                      admitted_jobs, assigned_operations, acts, upos):
    """Aggregate one planner turn; never feeds information back to decisions."""
    day = step // TPD
    row = _day_telemetry(episode, day)
    row["turns"] += 1
    for bucket, jobs in (("created", created_jobs),
                         ("admitted", admitted_jobs)):
        for operation, count in _count_jobs_by_operation(jobs).items():
            _increment(row[bucket], operation, count)
    for operation in assigned_operations:
        if operation in SERVICE_OPERATIONS:
            _increment(row["assigned"], operation)

    pending = []
    for idx, action in acts.items():
        operation = action[0] if action else "PASS"
        if operation in ("NORTH", "SOUTH", "EAST", "WEST"):
            row["movement_turns"] += 1
        elif operation == "PASS":
            row["pass_turns"] += 1
        if operation not in SERVICE_OPERATIONS:
            continue
        _increment(row["emitted"], operation)
        target = upos.get(idx)
        if target is None:
            continue
        pending.append({
            "step": step,
            "operation": operation,
            "argument": action[1] if len(action) > 1 else None,
            "target": tuple(target),
            "before": dict(_tile_at(tiles, target)),
        })
    episode["pending"] = pending

    for _x, _y, tile in beasts:
        animal = ANIMALS.get(tile.get("animal"))
        if animal and int(tile.get("yield_units", 0) or 0) >= animal["mh"]:
            _increment(row["animal_cap_ticks"], animal["prod"])
    for _x, _y, tile in plants:
        held = int(tile.get("yield_units", 0) or 0)
        max_step = tile.get("max_lifespan_step")
        if held <= 0 or max_step is None:
            continue
        try:
            if int(max_step) <= step:
                _increment(row["crop_expiry_with_yield"], tile.get("crop", "UNKNOWN"))
        except (TypeError, ValueError):
            pass


def telemetry_snapshot(include_active=True):
    """Return JSON-serializable aggregate diagnostics for the harness."""
    def clone_episode(source, pending_as_unknown=False):
        cloned = {key: value for key, value in source.items()
                  if key not in ("days", "pending")}
        cloned["days"] = {}
        for day, source_row in source["days"].items():
            cloned["days"][day] = {
                key: (dict(value) if isinstance(value, dict) else value)
                for key, value in source_row.items()
            }
        if pending_as_unknown:
            for pending in source.get("pending", []):
                day = pending["step"] // TPD
                if day not in cloned["days"]:
                    cloned["days"][day] = {
                        "turns": 0, "created": {}, "admitted": {},
                        "assigned": {}, "emitted": {}, "executed": {},
                        "failed": {}, "unknown": {}, "movement_turns": 0,
                        "pass_turns": 0, "animal_cap_ticks": {},
                        "crop_expiry_with_yield": {},
                    }
                _increment(cloned["days"][day]["unknown"],
                           pending["operation"])
        return cloned

    episodes = [clone_episode(row) for row in _TELEMETRY_COMPLETED]
    if include_active:
        for episode in _TELEMETRY_ACTIVE.values():
            episodes.append(clone_episode(episode, pending_as_unknown=True))
    return {"schema": 1, "episodes": episodes}


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
    telemetry_episode = _telemetry_begin(seat, step, tiles)
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
    carried_all = aggregate_inventories(invs)

    market = _get(obs, "market", {}) or {}
    minv = {k: int(v or 0) for k, v in (_get(market, "inventory", {}) or {}).items()}
    town = _get(obs, "town", {}) or {}
    shops = list(_get(town, "unlocked_shops", []) or [])
    shed_used = sum(shed.values())

    # ---- board scan ------------------------------------------------------
    plants, beasts, empties, weeds, structs = scan_board(
        tiles, shed_access_set)

    # ---- absorption -------------------------------------------------------
    absorb = forecast_absorption(shops, steps_left)
    known_absorb = forecast_known_absorption(shops, steps_left)

    # ---- our own committed future supply ----------------------------------
    supply = forecast_own_supply(
        shed, carried_all, plants, beasts, day, days_left)
    own_supply_only = dict(supply)

    own_crop_counts, own_wave_ready_counts, own_animal_counts = (
        count_owned_assets(plants, beasts, day))

    # Public opponent assets are legitimate forward information.  Discount
    # their technically possible output because routes can miss care/watering,
    # but account for it before committing to the same crash-prone product.
    opp_crop_counts = {name: 0 for name in CROPS}
    opp_wave_ready_counts = {name: 0 for name in CROPS}
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
                    planted_day = t.get("planted_day", day)
                    planted_day = day if planted_day is None else int(planted_day)
                    maturity = cd["fyd"] if cd["ong"] else cd["myd"]
                    if planted_day + maturity <= CASH_WAVE_END_DAY:
                        opp_wave_ready_counts[crop] += 1
                    held = int(t.get("yield_units", 0) or 0)
                    opp_wave[crop] += held
                    age = day - planted_day
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
    animal_target, animal_need, structure_need, species_cap = (
        animal_allocation_limits(
            day, days_left, len(quads), slots, len(beasts), len(structs),
            pending_animals))
    want_animal = {}
    # Match visible profitable livestock capacity before taking an uncontested
    # fallback.  Shared-market denial is valuable: conceding all milk/wool
    # demand to the rival can increase their bank more than diversification
    # increases ours.
    for name in sorted(ANIMALS, key=lambda n: -opp_animal_counts.get(n, 0)):
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

    crop_slots = max(0, slots - structure_need)
    want_crop = {}
    # Quick wheat creates the opening cash cycle and becomes feed instead of an
    # expensive market purchase.  This is a phase constraint, not a route.
    if day < 3 and crop_slots > 0:
        quick = min(crop_slots, max(6, int(round(crop_slots * 0.40))))
        want_crop["WHEAT"] = quick
        sim_supply["WHEAT"] = sim_supply.get("WHEAT", 0.0) + 4 * quick

    portfolio_size = len(plants) + crop_slots
    crop_cap = max(3, int(math.ceil(max(1, portfolio_size)
                                    * (CROP_CAP_EARLY if len(shops) < 2
                                       else CROP_CAP_LATE))))
    # Compete for fragile premium markets when the rival has visibly committed
    # production.  Targets come from the live board, never an identity or tape.
    for crop in ("STRAWBERRY", "MELON", "TOMATO"):
        room = crop_slots - sum(want_crop.values())
        if room <= 0:
            break
        if crop in SKIP_CROPS:
            continue
        cd = CROPS[crop]
        y = crop_yield(cd, days_left)
        if not y:
            continue
        # Count-matching is misleading when rival crops are older.  Only force
        # strategic matching while a crop planted *now* can join the day-20..24
        # cash wave, and compare established-by-wave crops rather than raw tiles.
        maturity = cd["fyd"] if cd["ong"] else cd["myd"]
        if day + maturity > CASH_WAVE_END_DAY:
            continue
        strategic_target = min(
            crop_cap, int(math.ceil(0.90 * opp_wave_ready_counts.get(crop, 0))))
        deficit = max(0, strategic_target - own_wave_ready_counts.get(crop, 0))
        n = min(room, deficit)
        if n <= 0:
            continue
        want_crop[crop] = want_crop.get(crop, 0) + n
        own_wave_ready_counts[crop] = own_wave_ready_counts.get(crop, 0) + n
        sim_supply[crop] = sim_supply.get(crop, 0.0) + n * y[0]

    remaining_crop_slots = crop_slots - sum(want_crop.values())
    for _ in range(remaining_crop_slots):
        best = None
        for crop, cd in CROPS.items():
            if crop in SKIP_CROPS:
                continue
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

    if day >= 20 and want_crop:
        # Preserve the legacy amount of late development work; only change the
        # crop mix. This directly addresses the graph's value-per-operation gap
        # and avoids reopening the failed worker-count / PLANT-inflation lines.
        legacy_project_slots = sum(max(0, int(v or 0))
                                   for v in want_crop.values())
        want_crop = late_terminal_crop_mix(
            day, legacy_project_slots, supply, own_supply_only, absorb, minv,
            wheat_buy, len(beasts))

    top_beast = max(want_animal, key=want_animal.get) if want_animal else None
    top_crop = max(want_crop, key=want_crop.get) if want_crop else None

    free_struct = {}
    for x, y, k in structs:
        free_struct.setdefault(k, []).append((x, y))

    # ---- price floor ------------------------------------------------------
    hold = hold_fraction(step, day, shed_used)

    # ---- job board --------------------------------------------------------
    jobs = []
    unfed = 0
    fertilize_needed = 0
    for x, y, t in beasts:
        tile_jobs, tile_unfed = animal_service_jobs(x, y, t, step, spot)
        jobs.extend(tile_jobs)
        unfed += tile_unfed

    for x, y, t in plants:
        tile_jobs, tile_fertilize = crop_service_jobs(
            x, y, t, step, day, shed_used + sum(carried_all.values()), spot,
            opp_crop_counts, opp_wave, minv)
        jobs.extend(tile_jobs)
        fertilize_needed += tile_fertilize

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
            jobs.append((max(90.0, 2.0 * per), (x, yy), [op], None))

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
            jobs.append((max(5.0, per), (x, yy), ["PLANT", crop], None))

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

    telemetry_created_jobs = tuple(jobs)
    jobs.sort(key=lambda j: -j[0])
    jobs = jobs[:240]

    # ---- assignment: global greedy over (unit, job) ------------------------
    units = [(0, tuple(_get(farm, "farmer", [4, 4]) or [4, 4]))]
    for i, pos in enumerate(hands):
        units.append((i + 1, tuple(pos or [4, 4])))
    upos = dict(units)

    # Bank useful loads regularly.  During liquidation this becomes mandatory,
    # otherwise a final harvest can sit on a worker after the last market tick.
    forced = critical_feed_actions(units, invs, beasts, step, hour)
    # Survival is a deadline constraint, not a spot-price auction.  Match
    # wheat carriers to second-miss animals before banking/economic jobs.
    # Rebuilding this deterministic matching from each observation keeps it
    # replay-agnostic while cargo and decreasing distance provide commitment.
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
    telemetry_admitted_jobs = tuple(jobs[:ncand])
    BIG = 1e9
    turns_left_today = max(0, TPD - hour - 1)
    # Opportunity cost of one worker-turn, calibrated live off this turn's own
    # job board rather than a tuned constant: walking one tile costs one turn,
    # and the turn is worth roughly what a typical available job pays.
    # We use the average of the top N jobs (where N is number of free workers)
    # to accurately reflect the real opportunity cost of a worker walking.
    active_jobs = min(ncand, max(1, len(free_units)))
    top_avg = sum(jobs[i][0] for i in range(active_jobs)) / active_jobs if active_jobs else 0.0
    move_rate = MOVE_FRAC * top_avg
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
    telemetry_assigned_operations = []
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
        telemetry_assigned_operations.append(op[0])
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
        # NOTE: no pre-position branch here, deliberately.  A `beasts and pos
        # not in shed_access_set` case used to walk idle empty-handed units
        # toward the shed every turn.  It reached this branch precisely because
        # it had no feasible column and nothing to carry, so it produced zero
        # ops by construction: 829 of 9383 walk-turns per 2 games, and the
        # reason our PASS rate was 6.8% against the top tapes' 14.9%.  Feed runs
        # are already covered three ways -- the PICKUP-WHEAT job (622 admitted /
        # 1 cut per episode), the forced critical-feed matcher above, and the
        # day boundary respawning every hand on a shed tile.  Do not restore it.
        else:
            acts[idx] = ["PASS"]

    # ---- market: deposits -> sales -> necessities -> investment -----------
    # Unit actions execute before market orders, so inventory deposited by a
    # DROP/PLACE this turn is genuinely sellable in this same ordered queue.
    projected, projected_used, deposited = project_shed_after_actions(
        shed, shed_used, acts, invs, upos, shed_access_set)

    orders = []
    cash = money
    n_beasts = len(beasts)
    feed_target = (n_beasts + int(math.ceil(n_beasts * FEED_BUFFER))
                   if step < FINAL_FARM_STEP else 0)
    sim = dict(minv)

    sell_hold = adjusted_sell_hold(
        hold, cash, projected_used, n_beasts, feed_target, wheat_buy)
    feed_keep = feed_target
    keep_wheat = min(int(projected.get("WHEAT", 0) or 0), feed_keep)

    rows = rank_sales(
        projected, minv, opp_wave, sell_hold, keep_wheat, step)

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
    total_wheat, need_wheat = feed_stock_need(
        projected.get("WHEAT", 0), carried_wheat,
        int(deposited.get("WHEAT", 0) or 0), feed_actions, feed_target,
        unfed, wheat_buy)
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

    footprint = len(plants) + len(beasts)
    want_hands, work_summary = workforce_target(jobs, day, hour, footprint)
    open_jobs = work_summary["open_jobs"]

    # Hires remain profitable after hour zero; cap the window so late hands do
    # not consume Fibonacci wages without enough turns to work.
    if hour <= HIRE_WINDOW and open_jobs and len(orders) < 10:
        n_hired = hires_today
        wheat_on_hand = int(shed.get("WHEAT", 0) or 0) + carried_wheat
        feed_shortfall = max(0, feed_target - wheat_on_hand)
        feed_reserve = max(20.0, feed_shortfall * wheat_buy)
        critical_hands = (min(8, max(2, int(math.ceil(n_beasts / 3.0))))
                          if n_beasts else min(4, want_hands))
        while (n_hired < want_hands and len(orders) < 10
               and purchase_orders < MAX_BUY_ORDERS):
            c = _fib(n_hired)
            if n_hired >= critical_hands and cash - c < feed_reserve:
                break
            if cash < c:
                break
            if n_hired >= 11 and c > max(89.0, cash * 0.10):
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
    if (owned_extra < 2 and days_left >= 7 and len(orders) < 10
            and purchase_orders < MAX_BUY_ORDERS):
        unlock_day = (4, 7, 10)[owned_extra]
        occupied = len(plants) + len(beasts) + len(structs) + len(weeds)
        available = max(1, 25 * len(quads))
        pressure = (occupied + sum(want_crop.values()) + sum(want_animal.values())) / available
        c = LAND_PRICES[owned_extra]
        se_gate = (owned_extra < 2 or
                   (cash >= 8000.0 + reserve and occupied + sum(want_crop.values())
                    + sum(want_animal.values()) >= 50))
        if (day >= unlock_day and pressure >= 0.50 and cash - c >= reserve
                and se_gate):
            orders.append(["BUY_LAND"])
            cash -= c
            purchase_orders += 1

    # Structures built by a unit this turn exist before these market buys.
    built = built_structure_counts(acts)

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

    _telemetry_record(
        telemetry_episode, step, tiles, beasts, plants,
        telemetry_created_jobs, telemetry_admitted_jobs,
        telemetry_assigned_operations, acts, upos)
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
    print("v132 self-play:", int(last[0].reward), int(last[1].reward))
