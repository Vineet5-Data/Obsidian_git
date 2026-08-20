"""Build v20: a dedicated crew, hired past the route's roster, that runs a 4th quadrant.

The recorded route finishes hiring by turn 0-2 of each day and never addresses
more than 14 hands.  Hands are cleared nightly and appended in hire order, so a
hire placed after the route's last hire of the day lands on an index the route
never speaks to.  Those units are therefore free of the desync risk that forced
every earlier idle worker to return to its home tile before the route resumed.
"""

src = open("v13.py", encoding="utf-8").read()

NEW = '''# ---------------------------------------------------------------- extra crew
# The route parks its winnings: $18,971 idle on day 12, $122,670 by day 28, on
# 3 quadrants and 14 animals, while the strongest opponent runs 4 quadrants and
# 19 animals by day 14.  Milk and wool clear ~$230 a unit in that matchup, so a
# $400 cow returning 39 milk repays itself many times over.
EXTRA_ENABLE = 1
EXTRA_HANDS = 2
EXTRA_HIRE_TURN = 3
EXTRA_FROM_DAY = 7
EXTRA_STOP_DAY = 27
EXTRA_MAX_ANIMALS = 24
EXTRA_CASH_RESERVE = 6000
EXTRA_LAND = 1
EXTRA_WHEAT_PER_ANIMAL = 2
ROUTE_MAX_HANDS = 14
_SHED_TILES = ((4, 4), (5, 4), (4, 5), (5, 5))
_LAND_COSTS = (1000, 2000, 4000)
_CARRY_PRODUCTS = ("MILK", "WOOL", "EGG", "STRAWBERRY", "MELON", "CARROT", "TOMATO", "FERTILIZER")


def _route_hand_count(step):
    step = min(max(0, int(step)), len(_ACTIONS) - 1)
    return len(_ACTIONS[step].get("hands") or [])


def _open_shed_tiles(farm):
    """PICKUP and DROP only work on the four centre tiles, and silently no-op
    on any that sit inside a quadrant which is still LOCKED."""
    rows = _get(farm, "tiles", []) or []
    out = []
    for (x, y) in _SHED_TILES:
        if 0 <= y < len(rows) and 0 <= x < len(rows[y] or []) and rows[y][x] != "LOCKED":
            out.append((x, y))
    return out


def _census(farm):
    empty, pens, animals = [], [], []
    rows = _get(farm, "tiles", []) or []
    for y, row in enumerate(rows):
        for x, tile in enumerate(row or []):
            if tile is None:
                empty.append((x, y))
            elif isinstance(tile, dict):
                if tile.get("animal"):
                    animals.append((x, y, tile))
                elif tile.get("kind") == "PASTURE":
                    pens.append((x, y))
    return empty, pens, animals


def _reserved(farm, orders):
    need = 0
    hires = int(_get(farm, "hires_today", 0) or 0)
    for order in orders:
        if order[0] == "HIRE":
            need += _hire_cost(hires)
            hires += 1
        elif order[0] == "BUY_SEED" and len(order) >= 3:
            need += SEED_COST.get(order[1], 0) * max(0, int(order[2] or 0))
        elif order[0] == "BUY_PRODUCT" and len(order) >= 3:
            need += PRODUCT_COST.get(order[1], 0) * max(0, int(order[2] or 0))
        elif order[0] == "BUY_ANIMAL" and len(order) >= 3:
            need += ANIMAL_COST.get(order[1], 0) * max(0, int(order[2] or 0))
    return need


def _extra_market(obs, action):
    """Hire the crew, unlock the 4th quadrant, and stock it with cows."""
    if not EXTRA_ENABLE:
        return action
    try:
        farm, private = _farm_private(obs)
        step = int(_get(obs, "step", 0) or 0)
        day = int(_get(obs, "day", 0) or 0)
        turn = step % 24
        if day < EXTRA_FROM_DAY or day > EXTRA_STOP_DAY:
            return action
        orders = [list(o) for o in (action.get("market") or []) if o]
        money = int(_get(farm, "money", 0) or 0)
        budget = money - EXTRA_CASH_RESERVE - _reserved(farm, orders)
        shed = _get(private, "shed", {}) or {}
        empty, pens, animals = _census(farm)

        # Hire only once the route has placed every hire it wants today, so our
        # units land on indices past its roster.
        if turn == int(EXTRA_HIRE_TURN):
            have = len(_get(farm, "hands", []) or [])
            hires = int(_get(farm, "hires_today", 0) or 0)
            for _ in range(int(EXTRA_HANDS)):
                if len(orders) >= 10:
                    break
                cost = _hire_cost(hires)
                if budget < cost:
                    break
                orders.append(["HIRE"])
                budget -= cost
                hires += 1
                have += 1

        unlocked = len(_get(farm, "unlocked_quadrants", []) or [])
        if EXTRA_LAND and unlocked < 4 and not any(o[0] == "BUY_LAND" for o in orders):
            cost = _LAND_COSTS[min(max(0, unlocked - 1), len(_LAND_COSTS) - 1)]
            if budget >= cost and len(orders) < 10:
                orders.append(["BUY_LAND"])
                budget -= cost

        pending = int(shed.get("COW", 0) or 0) + int(shed.get("SHEEP", 0) or 0)
        for inventory in (_get(private, "inventories", []) or []):
            pending += int((inventory or {}).get("COW", 0) or 0)
            pending += int((inventory or {}).get("SHEEP", 0) or 0)
        room = len(pens) + len(empty)
        want = min(max(0, int(EXTRA_MAX_ANIMALS) - len(animals) - pending),
                   max(0, room - pending), 2)
        if want > 0 and len(orders) < 10 and day <= EXTRA_STOP_DAY - 6:
            count = 0
            while count < want and budget >= ANIMAL_COST["COW"]:
                budget -= ANIMAL_COST["COW"]
                count += 1
            if count > 0:
                orders.append(["BUY_ANIMAL", "COW", count])

        # The crew eats into the same wheat the route bought for its own herd.
        need_wheat = int(EXTRA_WHEAT_PER_ANIMAL) * max(0, len(animals) - ROUTE_MAX_HANDS)
        if need_wheat > 0 and int(shed.get("WHEAT", 0) or 0) < need_wheat and len(orders) < 10:
            if budget >= PRODUCT_COST["WHEAT"] * need_wheat:
                orders.append(["BUY_PRODUCT", "WHEAT", need_wheat])

        action["market"] = orders[:10]
    except Exception:
        return action
    return action


def _crew_job(farm, shed, carrying, animals, pens, empty, claimed, sheds):
    """Pick one job for a free crew unit, highest value first."""
    held_animal = "COW" if int(carrying.get("COW", 0) or 0) > 0 else (
        "SHEEP" if int(carrying.get("SHEEP", 0) or 0) > 0 else None)
    held_wheat = int(carrying.get("WHEAT", 0) or 0)
    held_goods = sum(int(carrying.get(p, 0) or 0) for p in _CARRY_PRODUCTS)
    shed_animals = int(shed.get("COW", 0) or 0) + int(shed.get("SHEEP", 0) or 0)
    jobs = []

    if held_animal:
        for (x, y) in pens:
            if (x, y) not in claimed:
                jobs.append((9000, x, y, ["PLACE", held_animal]))
    else:
        if shed_animals and pens:
            for (x, y) in sheds:
                jobs.append((8000, x, y, ["PICKUP", "COW" if int(shed.get("COW", 0) or 0) else "SHEEP", 1]))
        elif shed_animals and empty:
            for (x, y) in empty[:6]:
                if (x, y) not in claimed:
                    jobs.append((7500, x, y, ["BUILD_PASTURE"]))

    # Feeding outranks everything else: two unfed days and the animal escapes.
    for (x, y, tile) in animals:
        if (x, y) in claimed:
            continue
        if not tile.get("fed_today"):
            urgency = 12000 if int(tile.get("consecutive_unfed", 0) or 0) >= 1 else 6000
            if held_wheat > 0:
                jobs.append((urgency, x, y, ["FEED"]))
    if held_wheat <= 0 and any(not t.get("fed_today") for (_x, _y, t) in animals):
        for (x, y) in sheds:
            jobs.append((5800, x, y, ["PICKUP", "WHEAT", 6]))

    if held_goods >= 6:
        for (x, y) in sheds:
            jobs.append((5600, x, y, ["DROP"]))

    for (x, y, tile) in animals:
        if (x, y) in claimed:
            continue
        if int(tile.get("yield_units", 0) or 0) > 0 and held_goods < 8:
            jobs.append((5000, x, y, ["HARVEST"]))
        if not tile.get("cared_today"):
            jobs.append((4200, x, y, ["CARE"]))

    rows = _get(farm, "tiles", []) or []
    for y, row in enumerate(rows):
        for x, tile in enumerate(row or []):
            if isinstance(tile, dict) and tile.get("kind") == "PLANT" and tile.get("crop"):
                if not tile.get("watered_today") and (x, y) not in claimed:
                    jobs.append((CROP_VALUE.get(tile["crop"], 25), x, y, ["WATER"]))
    return jobs


def _run_crew(obs, action):
    """Drive every hand the recorded route does not address."""
    if not EXTRA_ENABLE:
        return action
    try:
        farm, private = _farm_private(obs)
        step = int(_get(obs, "step", 0) or 0)
        positions = list(_get(farm, "hands", []) or [])
        route_hands = _route_hand_count(step)
        if len(positions) <= route_hands:
            return action
        shed = _get(private, "shed", {}) or {}
        inventories = list(_get(private, "inventories", []) or [])
        empty, pens, animals = _census(farm)
        sheds = _open_shed_tiles(farm)
        if not sheds:
            return action

        orders = [list(action.get("farmer") or ["PASS"])]
        orders.extend([list(o or ["PASS"]) for o in (action.get("hands") or [])])
        while len(orders) < len(positions) + 1:
            orders.append(["PASS"])

        claimed = set()
        for index in range(route_hands + 1, len(positions) + 1):
            position = positions[index - 1]
            try:
                px, py = int(position[0]), int(position[1])
            except (TypeError, ValueError, IndexError):
                continue
            carrying = inventories[index] if index < len(inventories) else {}
            jobs = _crew_job(farm, shed, carrying or {}, animals, pens, empty, claimed, sheds)
            best = None
            for (value, tx, ty, verb) in jobs:
                distance = abs(px - tx) + abs(py - ty)
                score = value - 25 * distance
                if best is None or score > best[0]:
                    best = (score, distance, tx, ty, verb)
            if best is None:
                continue
            _score, distance, tx, ty, verb = best
            claimed.add((tx, ty))
            if distance == 0:
                orders[index] = list(verb)
            else:
                move = _step_toward(farm, (px, py), (tx, ty))
                if move:
                    orders[index] = move
        action["farmer"] = orders[0]
        action["hands"] = orders[1:]
    except Exception:
        return action
    return action


def _surplus_sales(obs, action):
    """Sell what the crew adds; the recorded route has no orders for it."""
    if not EXTRA_ENABLE:
        return action
    try:
        private = _get(obs, "private", {}) or {}
        shed = _get(private, "shed", {}) or {}
        day = int(_get(obs, "day", 0) or 0)
        orders = [list(o) for o in (action.get("market") or []) if o]
        planned = {}
        for order in orders:
            if order[0] == "SELL" and len(order) >= 3:
                planned[order[1]] = planned.get(order[1], 0) + int(order[2] or 0)
        if day < EXTRA_FROM_DAY:
            return action
        for item in ("MILK", "WOOL"):
            if len(orders) >= 10:
                break
            surplus = int(shed.get(item, 0) or 0) - planned.get(item, 0) - 12
            if surplus > 0:
                orders.append(["SELL", item, surplus])
        action["market"] = orders[:10]
    except Exception:
        return action
    return action


'''

anchor = "IDLE_WORK = 1"
assert anchor in src
src = src.replace(anchor, NEW + anchor, 1)

# CROP_VALUE is defined further down in v13; hoist it above the crew code.
assert 'CROP_VALUE = {"MELON": 250' in src
src = src.replace(
    'CROP_VALUE = {"MELON": 250, "STRAWBERRY": 120, "TOMATO": 60, "CARROT": 35, "WHEAT": 25}\n',
    "", 1)
src = src.replace(
    "# ---------------------------------------------------------------- extra crew",
    'CROP_VALUE = {"MELON": 250, "STRAWBERRY": 120, "TOMATO": 60, "CARROT": 35, "WHEAT": 25}\n'
    "# ---------------------------------------------------------------- extra crew", 1)

OLD_AGENT = "action = _fill_idle_units(obs, _adapt_animals(obs, _ACTIONS[step]))"
assert OLD_AGENT in src
src = src.replace(
    OLD_AGENT,
    "action = _extra_market(obs, _adapt_animals(obs, _ACTIONS[step]))\n"
    "        action = _fill_idle_units(obs, action)\n"
    "        action = _run_crew(obs, action)\n"
    "        action = _surplus_sales(obs, action)",
    1,
)

open("v20.py", "w", encoding="utf-8").write(src)
print("v20.py written")
