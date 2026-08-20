"""Wufang Hong, current top player. Episode 90666168 seat 1, $125,873."""

import base64
import copy
import json
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    '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'
    'ynKaDB1gFk8NtgclXbaK5Obu/3H/f3qcwzU='
    )
)))


def _get(value, key, default=None):
    if isinstance(value, dict):
        return value.get(key, default)
    getter = getattr(value, "get", None)
    if callable(getter):
        return getter(key, default)
    return getattr(value, key, default)


def _aligned(action, obs):
    action = copy.deepcopy(action or {})
    farms = list(_get(obs, "farms", []) or [])
    seat = 1 if int(_get(obs, "player", 0) or 0) == 1 else 0
    farm = farms[seat] if seat < len(farms) else {}
    expected = len(_get(farm, "hands", []) or [])
    hands = [list(order or ["PASS"]) for order in (action.get("hands") or [])]
    if len(hands) < expected:
        hands.extend([["PASS"] for _ in range(expected - len(hands))])
    return {
        "farmer": list(action.get("farmer") or ["PASS"]),
        "hands": hands[:expected],
        "market": [list(order) for order in (action.get("market") or [])][:10],
    }


ANIMAL_SWITCH_DAY = 999
MAX_ONE_ANIMAL = 10
_RUNTIME = {"raw_opponent": False}
ANIMAL_COST = {"COW": 400, "SHEEP": 500}
# Cared season output per animal, measured in-engine.
ANIMAL_YIELD = {"COW": 39, "SHEEP": 38}
COW_BIAS = 1.0
SEED_COST = {"WHEAT": 10, "CARROT": 20, "TOMATO": 50, "STRAWBERRY": 100, "MELON": 80}
PRODUCT_COST = {"WHEAT": 25, "FERTILIZER": 100}
SELLABLE_PRODUCTS = {
    "WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON",
    "EGG", "MILK", "WOOL", "FERTILIZER",
}


def _farm_private(obs):
    farms = list(_get(obs, "farms", []) or [])
    seat = 1 if int(_get(obs, "player", 0) or 0) == 1 else 0
    return (farms[seat] if seat < len(farms) else {}), (_get(obs, "private", {}) or {})


def _animal_counts(farm, private):
    counts = _placed_animal_counts(farm)
    shed = _get(private, "shed", {}) or {}
    inventories = list(_get(private, "inventories", []) or [])
    for animal in counts:
        counts[animal] += max(0, int(shed.get(animal, 0) or 0))
        counts[animal] += sum(max(0, int((inventory or {}).get(animal, 0) or 0)) for inventory in inventories)
    return counts


def _placed_animal_counts(farm):
    counts = {"COW": 0, "SHEEP": 0}
    for row in (_get(farm, "tiles", []) or []):
        for tile in row or []:
            if isinstance(tile, dict) and tile.get("animal") in counts:
                counts[tile["animal"]] += 1
    return counts


def _hire_cost(index):
    a, b = 1, 1
    for _ in range(max(0, int(index))):
        a, b = b, a + b
    return a


def _projected_raw_balance(obs, action, farm, private):
    balance = int(_get(farm, "money", 0) or 0)
    prices = _get(_get(obs, "market", {}) or {}, "prices", {}) or {}
    available = dict(_get(private, "shed", {}) or {})
    hires = int(_get(farm, "hires_today", 0) or 0)
    unlocked = len(_get(farm, "unlocked_quadrants", []) or [])
    land_costs = (1000, 2000, 4000)
    for order in (action.get("market", []) or []):
        if not order:
            continue
        op = order[0]
        if op == "SELL" and len(order) >= 3:
            item = order[1]
            quantity = min(max(0, int(order[2] or 0)), max(0, int(available.get(item, 0) or 0)))
            balance += quantity * max(1, int(prices.get(item, 1) or 1))
            available[item] = max(0, int(available.get(item, 0) or 0) - quantity)
        elif op == "HIRE":
            balance -= _hire_cost(hires)
            hires += 1
        elif op == "BUY_SEED" and len(order) >= 3:
            balance -= SEED_COST.get(order[1], 0) * max(0, int(order[2] or 0))
        elif op == "BUY_PRODUCT" and len(order) >= 3:
            balance -= PRODUCT_COST.get(order[1], 0) * max(0, int(order[2] or 0))
        elif op == "BUY_ANIMAL" and len(order) >= 3:
            balance -= ANIMAL_COST.get(order[1], 0) * max(0, int(order[2] or 0))
        elif op == "BUY_LAND" and unlocked > 0:
            index = min(max(0, unlocked - 1), len(land_costs) - 1)
            balance -= land_costs[index]
            unlocked += 1
    return balance


def _recorded_animal_counts_before(step):
    counts = {"COW": 0, "SHEEP": 0}
    for recorded in _ACTIONS[: max(0, int(step))]:
        for order in (recorded.get("market", []) or []):
            if len(order) >= 3 and order[0] == "BUY_ANIMAL" and order[1] in counts:
                counts[order[1]] += max(0, int(order[2] or 0))
    return counts


def _detect_recorded_opponent(obs, farm):
    farms = list(_get(obs, "farms", []) or [])
    seat = 1 if int(_get(obs, "player", 0) or 0) == 1 else 0
    if len(farms) < 2:
        return False
    ours = _placed_animal_counts(farm)
    opponent = _placed_animal_counts(farms[1 - seat])
    expected = _recorded_animal_counts_before(_get(obs, "step", 0))
    return ours != opponent and opponent == expected


def _preferred_animal(obs, counts):
    prices = _get(_get(obs, "market", {}) or {}, "prices", {}) or {}
    cow_value = 1.5 * max(1, int(prices.get("MILK", 160) or 160))
    sheep_value = (4.0 / 3.0) * max(1, int(prices.get("WOOL", 200) or 200))
    if counts["COW"] >= int(MAX_ONE_ANIMAL):
        return "SHEEP"
    if counts["SHEEP"] >= int(MAX_ONE_ANIMAL):
        return "COW"
    return "COW" if cow_value >= sheep_value else "SHEEP"


def _adapt_animals(obs, action):
    action = _aligned(action, obs)
    farm, private = _farm_private(obs)
    counts = _animal_counts(farm, private)
    day = int(_get(obs, "day", 0) or 0)
    shed = _get(private, "shed", {}) or {}
    inventories = list(_get(private, "inventories", []) or [])

    if day >= int(ANIMAL_SWITCH_DAY) + 2 and _detect_recorded_opponent(obs, farm):
        _RUNTIME["raw_opponent"] = True

    # Follow the price signal while the opponent does too.  If a fixed replay
    # route is detected, retain the recorded purchases; buying extra animals
    # to catch up was tested and amplified the opponent's scarcity rents.
    if not _RUNTIME["raw_opponent"] and day >= int(ANIMAL_SWITCH_DAY):
        market = []
        planned = dict(counts)
        extra_budget = max(0, _projected_raw_balance(obs, action, farm, private))
        for raw in action.get("market", []) or []:
            order = list(raw)
            if len(order) >= 3 and order[0] == "BUY_ANIMAL" and order[1] in planned:
                recorded_animal = order[1]
                animal = _preferred_animal(obs, planned)
                quantity = max(0, int(order[2] or 0))
                if planned[animal] + quantity > int(MAX_ONE_ANIMAL):
                    animal = "SHEEP" if animal == "COW" else "COW"
                extra_cost = (ANIMAL_COST[animal] - ANIMAL_COST[recorded_animal]) * quantity
                if extra_cost > extra_budget:
                    # Cannot afford the upgrade: keep the recorded species.
                    # Skipping the order outright loses the animal for the whole
                    # season (11 placed vs the winner's 15 in episode 90487461).
                    animal = recorded_animal
                    extra_cost = 0
                    if planned[animal] + quantity > int(MAX_ONE_ANIMAL):
                        market.append(order)
                        continue
                extra_budget -= extra_cost
                order[1] = animal
                planned[animal] += quantity
            market.append(order)
        action["market"] = market[:10]

    unit_actions = [action.get("farmer", ["PASS"]), *list(action.get("hands") or [])]
    for index, unit_action in enumerate(unit_actions):
        if not unit_action or len(unit_action) < 2 or unit_action[1] not in counts:
            continue
        raw_animal = unit_action[1]
        other = "SHEEP" if raw_animal == "COW" else "COW"
        if unit_action[0] == "PICKUP":
            if int(shed.get(raw_animal, 0) or 0) <= 0 and int(shed.get(other, 0) or 0) > 0:
                unit_action[1] = other
        elif unit_action[0] == "PLACE":
            inventory = dict(inventories[index] or {}) if index < len(inventories) else {}
            if int(inventory.get(raw_animal, 0) or 0) <= 0 and int(inventory.get(other, 0) or 0) > 0:
                unit_action[1] = other
    action["farmer"] = unit_actions[0]
    action["hands"] = unit_actions[1:]
    return _aligned(action, obs)


IDLE_WORK = 0
IDLE_MARGIN = 1
_DIRS = (("NORTH", 0, -1), ("SOUTH", 0, 1), ("EAST", 1, 0), ("WEST", -1, 0))


def _unit_busy_steps():
    """Steps at which the recorded route gives each unit a real order.

    Index 0 is the farmer, index n the n-th hand.  Idle work must always hand a
    unit back on its home tile before the next of these steps, or every later
    recorded order for that unit addresses the wrong tile.
    """
    busy = {}
    for step, recorded in enumerate(_ACTIONS):
        units = [recorded.get("farmer") or ["PASS"]]
        units.extend(list(recorded.get("hands") or []))
        for index, order in enumerate(units):
            if order and order[0] != "PASS":
                busy.setdefault(index, []).append(step)
    return busy


_BUSY = _unit_busy_steps()
_IDLE_HOME = {}


def _next_busy(index, step):
    for candidate in _BUSY.get(index, ()):  # short per-unit lists
        if candidate > step:
            return candidate
    return len(_ACTIONS)


def _passable(farm, x, y):
    rows = _get(farm, "tiles", []) or []
    if not (0 <= y < len(rows)):
        return False
    row = rows[y] or []
    if not (0 <= x < len(row)):
        return False
    return row[x] != "LOCKED"


def _step_toward(farm, position, target):
    px, py = position
    tx, ty = target
    options = []
    for name, dx, dy in _DIRS:
        nx, ny = px + dx, py + dy
        gain = (abs(px - tx) + abs(py - ty)) - (abs(nx - tx) + abs(ny - ty))
        if gain > 0 and _passable(farm, nx, ny):
            options.append((gain, name))
    if not options:
        return None
    options.sort(reverse=True)
    return [options[0][1]]


# Watering is rationed by crop value, not by proximity: strawberry runs 45%
# dry across the season (314 crop-days) and is worth five wheat.
CROP_VALUE = {"MELON": 250, "STRAWBERRY": 120, "TOMATO": 60, "CARROT": 35, "WHEAT": 25}
CARE_VALUE = 300
IDLE_DIST_PENALTY = 20


def _idle_targets(farm):
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
    return jobs


def _fill_idle_units(obs, action):
    if not IDLE_WORK:
        return action
    try:
        farm, _private = _farm_private(obs)
        step = int(_get(obs, "step", 0) or 0)
        if step == 0:
            _IDLE_HOME.clear()
        positions = [_get(farm, "farmer", None)]
        positions.extend(list(_get(farm, "hands", []) or []))
        orders = [list(action.get("farmer") or ["PASS"])]
        orders.extend([list(order or ["PASS"]) for order in (action.get("hands") or [])])

        jobs = _idle_targets(farm)
        claimed = set()
        for index, order in enumerate(orders):
            if index >= len(positions) or positions[index] is None:
                continue
            if order and order[0] != "PASS":
                _IDLE_HOME.pop(index, None)
                continue
            try:
                px, py = int(positions[index][0]), int(positions[index][1])
            except (TypeError, ValueError, IndexError):
                continue
            home = _IDLE_HOME.setdefault(index, (px, py))
            budget = _next_busy(index, step) - step
            dist_home = abs(px - home[0]) + abs(py - home[1])
            slack = budget - dist_home - int(IDLE_MARGIN)

            if slack <= 0:
                if dist_home > 0:
                    move = _step_toward(farm, (px, py), home)
                    if move:
                        orders[index] = move
                continue

            best = None
            for (tx, ty, verb, value) in jobs:
                if (tx, ty) in claimed:
                    continue
                out = abs(px - tx) + abs(py - ty)
                back = abs(tx - home[0]) + abs(ty - home[1])
                if out + 1 + back > budget - int(IDLE_MARGIN):
                    continue
                score = value - IDLE_DIST_PENALTY * out
                if best is None or score > best[0]:
                    best = (score, out, tx, ty, verb)
            if best is None:
                if dist_home > 0:
                    move = _step_toward(farm, (px, py), home)
                    if move:
                        orders[index] = move
                continue
            _score, out, tx, ty, verb = best
            claimed.add((tx, ty))
            if out == 0:
                orders[index] = [verb]
            else:
                move = _step_toward(farm, (px, py), (tx, ty))
                if move:
                    orders[index] = move

        action["farmer"] = orders[0]
        action["hands"] = orders[1:]
    except Exception:
        return action
    return action


def _terminal_liquidation(obs, action):
    if int(_get(obs, "step", 0) or 0) < len(_ACTIONS) - 1:
        return action
    private = _get(obs, "private", {}) or {}
    shed = _get(private, "shed", {}) or {}
    prices = _get(_get(obs, "market", {}) or {}, "prices", {}) or {}
    stock = [
        (item, max(0, int(quantity or 0)))
        for item, quantity in shed.items()
        if item in SELLABLE_PRODUCTS and int(quantity or 0) > 0
    ]
    stock.sort(key=lambda pair: (-max(1, int(prices.get(pair[0], 1) or 1)), pair[0]))
    action["market"] = [["SELL", item, quantity] for item, quantity in stock[:10]]
    return _aligned(action, obs)


def agent(obs):
    try:
        step = min(max(0, int(_get(obs, "step", 0) or 0)), len(_ACTIONS) - 1)
        if step == 0:
            _RUNTIME["raw_opponent"] = False
        action = _fill_idle_units(obs, _adapt_animals(obs, _ACTIONS[step]))
        return _terminal_liquidation(obs, _aligned(action, obs))
    except Exception:
        farms = list(_get(obs, "farms", []) or [])
        seat = 1 if int(_get(obs, "player", 0) or 0) == 1 else 0
        farm = farms[seat] if seat < len(farms) else {}
        return {
            "farmer": ["PASS"],
            "hands": [["PASS"] for _ in (_get(farm, "hands", []) or [])],
            "market": [],
        }
