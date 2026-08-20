"""Build v19: spend the route's idle cash on land + animals, and let idle units install them."""

src = open("v13.py", encoding="utf-8").read()

NEW = '''# The route parks its winnings: $18,971 idle on day 12 and $122,670 by day 28,
# on 3 quadrants and 14 animals.  The strongest opponent runs 4 quadrants and
# 19 animals by day 14 and finishes ahead.  Milk and wool clear around $230 a
# unit in that matchup, so a $400 cow returning 39 milk repays itself many
# times over.  This layer spends the idle cash; idle units install it.
EXTRA_ENABLE = 1
EXTRA_FROM_DAY = 8
EXTRA_LAST_DAY = 18
EXTRA_MAX_ANIMALS = 22
EXTRA_CASH_RESERVE = 9000
EXTRA_LAND = 1
_SHED_TILES = ((4, 4), (5, 4), (4, 5), (5, 5))
_LAND_COSTS = (1000, 2000, 4000)
PLACE_VALUE = 5000
BUILD_VALUE = 6000
FEED_VALUE = 4000
PICKUP_VALUE = 3500


def _open_shed_tiles(farm):
    """PICKUP and DROP only work on the four centre tiles, and silently no-op
    on the ones inside a quadrant that is still LOCKED."""
    rows = _get(farm, "tiles", []) or []
    out = []
    for (x, y) in _SHED_TILES:
        if 0 <= y < len(rows) and 0 <= x < len(rows[y] or []) and rows[y][x] != "LOCKED":
            out.append((x, y))
    return out


def _farm_census(farm):
    empty, free_pasture, animals = [], [], 0
    rows = _get(farm, "tiles", []) or []
    for y, row in enumerate(rows):
        for x, tile in enumerate(row or []):
            if tile is None:
                empty.append((x, y))
            elif isinstance(tile, dict):
                if tile.get("animal"):
                    animals += 1
                elif tile.get("kind") == "PASTURE":
                    free_pasture.append((x, y))
    return empty, free_pasture, animals


def _route_reserved(farm, orders):
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


def _extra_investment(obs, action):
    """Convert idle cash into land and animals."""
    if not EXTRA_ENABLE:
        return action
    try:
        farm, private = _farm_private(obs)
        day = int(_get(obs, "day", 0) or 0)
        if day < EXTRA_FROM_DAY or day > EXTRA_LAST_DAY:
            return action
        money = int(_get(farm, "money", 0) or 0)
        orders = [list(o) for o in (action.get("market") or []) if o]
        if len(orders) >= 10:
            return action
        shed = _get(private, "shed", {}) or {}
        empty, free_pasture, animals = _farm_census(farm)
        pending = int(shed.get("COW", 0) or 0) + int(shed.get("SHEEP", 0) or 0)
        for inventory in (_get(private, "inventories", []) or []):
            pending += int((inventory or {}).get("COW", 0) or 0)
            pending += int((inventory or {}).get("SHEEP", 0) or 0)
        budget = money - EXTRA_CASH_RESERVE - _route_reserved(farm, orders)

        unlocked = len(_get(farm, "unlocked_quadrants", []) or [])
        if EXTRA_LAND and unlocked < 4 and not any(o[0] == "BUY_LAND" for o in orders):
            cost = _LAND_COSTS[min(max(0, unlocked - 1), len(_LAND_COSTS) - 1)]
            if budget >= cost:
                orders.append(["BUY_LAND"])
                budget -= cost

        # Only buy what there is somewhere to put.
        room = len(free_pasture) + len(empty)
        want = min(max(0, int(EXTRA_MAX_ANIMALS) - animals - pending),
                   max(0, room - pending))
        if want > 0 and len(orders) < 10:
            count = 0
            while count < want and count < 3 and budget >= ANIMAL_COST["COW"]:
                budget -= ANIMAL_COST["COW"]
                count += 1
            if count > 0:
                orders.append(["BUY_ANIMAL", "COW", count])
        action["market"] = orders[:10]
    except Exception:
        return action
    return action


'''

anchor = "IDLE_WORK = 1"
assert anchor in src
src = src.replace(anchor, NEW + anchor, 1)

OLD_TARGETS = '''def _idle_targets(farm):
    """Every job an idle unit could usefully do, with its value."""
    jobs = []
    rows = _get(farm, "tiles", []) or []
    for y, row in enumerate(rows):
        for x, tile in enumerate(row or []):
            if not isinstance(tile, dict):
                continue
            kind = tile.get("kind")
            if kind == "PLANT" and tile.get("crop") and not tile.get("watered_today"):
                jobs.append((x, y, "WATER", CROP_VALUE.get(tile["crop"], 25)))
            elif kind == "PASTURE" and tile.get("animal") and not tile.get("cared_today"):
                jobs.append((x, y, "CARE", CARE_VALUE))
    return jobs'''

NEW_TARGETS = '''def _idle_targets(farm, carrying=None, shed=None):
    """Every job an idle unit could usefully do, with its value.

    `carrying` is that unit's own inventory, so a unit holding an animal is
    offered a PLACE and a unit holding wheat is offered a FEED.
    """
    carrying = carrying or {}
    shed = shed or {}
    jobs = []
    held_animal = any(int(carrying.get(a, 0) or 0) > 0 for a in ("COW", "SHEEP"))
    held_wheat = int(carrying.get("WHEAT", 0) or 0) > 0
    shed_animals = int(shed.get("COW", 0) or 0) + int(shed.get("SHEEP", 0) or 0)
    rows = _get(farm, "tiles", []) or []
    # A pen must exist before an animal is worth collecting, otherwise every
    # idle unit grabs a cow and carries it back to the shed unplaced.
    free_pens = 0
    for row in rows:
        for tile in row or []:
            if isinstance(tile, dict) and tile.get("kind") == "PASTURE" and not tile.get("animal"):
                free_pens += 1
    need_pens = shed_animals > free_pens
    pastures_wanted = 0
    for y, row in enumerate(rows):
        for x, tile in enumerate(row or []):
            if tile is None:
                if need_pens and pastures_wanted < 4:
                    pastures_wanted += 1
                    jobs.append((x, y, "BUILD_PASTURE", BUILD_VALUE))
                continue
            if not isinstance(tile, dict):
                continue
            kind = tile.get("kind")
            if kind == "PLANT" and tile.get("crop") and not tile.get("watered_today"):
                jobs.append((x, y, "WATER", CROP_VALUE.get(tile["crop"], 25)))
            elif kind == "PASTURE":
                if tile.get("animal"):
                    if not tile.get("cared_today"):
                        jobs.append((x, y, "CARE", CARE_VALUE))
                    if held_wheat and not tile.get("fed_today"):
                        jobs.append((x, y, "FEED", FEED_VALUE))
                elif held_animal:
                    jobs.append((x, y, "PLACE", PLACE_VALUE))
    if not held_animal and shed_animals and free_pens > 0:
        for (x, y) in _open_shed_tiles(farm):
            jobs.append((x, y, "PICKUP", PICKUP_VALUE))
    return jobs'''

assert OLD_TARGETS in src
src = src.replace(OLD_TARGETS, NEW_TARGETS, 1)

OLD_CALL = "        jobs = _idle_targets(farm)"
NEW_CALL = '''        private = _get(obs, "private", {}) or {}
        shed = _get(private, "shed", {}) or {}
        inventories = list(_get(private, "inventories", []) or [])'''
assert OLD_CALL in src
src = src.replace(OLD_CALL, NEW_CALL, 1)

OLD_LOOP = '''            best = None
            for (tx, ty, verb, value) in jobs:'''
NEW_LOOP = '''            carrying = inventories[index] if index < len(inventories) else {}
            jobs = _idle_targets(farm, carrying, shed)
            best = None
            for (tx, ty, verb, value) in jobs:'''
assert OLD_LOOP in src
src = src.replace(OLD_LOOP, NEW_LOOP, 1)

OLD_EMIT = '''            if out == 0:
                orders[index] = [verb]'''
NEW_EMIT = '''            if out == 0:
                if verb == "PICKUP":
                    species = "COW" if int(shed.get("COW", 0) or 0) > 0 else "SHEEP"
                    orders[index] = ["PICKUP", species, 1]
                elif verb == "PLACE":
                    species = "COW" if int((carrying or {}).get("COW", 0) or 0) > 0 else "SHEEP"
                    orders[index] = ["PLACE", species]
                else:
                    orders[index] = [verb]'''
assert OLD_EMIT in src
src = src.replace(OLD_EMIT, NEW_EMIT, 1)

OLD_AGENT = "action = _fill_idle_units(obs, _adapt_animals(obs, _ACTIONS[step]))"
assert OLD_AGENT in src
src = src.replace(
    OLD_AGENT,
    "action = _extra_investment(obs, _adapt_animals(obs, _ACTIONS[step]))\n"
    "        action = _fill_idle_units(obs, action)",
    1,
)

open("v19.py", "w", encoding="utf-8").write(src)
print("v19.py written")
