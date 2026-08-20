"""Family-A route: OceanMix 139289 (fresh pool 90629703_p0)."""

import base64
import copy
import json
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vG9cR/S965kNIybLTN8XexEIUy5DkEmkgBAGaokCRPqR9K/rfq8gUudyZe+bMx11Sqp9MkxR3du7cu/Nx5sxP/zn52y+/'
    '//br7yd/+unk48Xt7cn94uTvv/zzr/96eOPh5W+//P6PX//98Pqnk/eXN8PDp9yLbz79+PPFh8sfLq5OFidvr9cni5V4+/b9MHwc'
    'fXA7DO8e3l6/Hy7uThavJ2//MFxdfzhZLLdf/3hz/e7T27vdX7y6v//vYu9+Lt9+/+nj7krL0b39dLIebu8eZf1wfXP3/vHV9q3J'
    'i31F3A5XV7urLptX3X5hfNXtp2OlXF69+/lB+XefNtrj5FCVIMTZ/IQmwk4t7UvGdAAuuvmT0/53Pv31kTS7JVcWf/rW+NrTtb66'
    'eDtsNbl3CXlv2kXFK3Cxb8f7Y1+5GzH+sKk/fuvh/x/utntGf8dz5bcXUwVOZHlQ1cXdcDN59XTR3bcmYiDNTs6irRBjyYeL28bV'
    'Xb+8+0Gppu0lti9urz8Z6pJXUAx9K/H2h2vVNbWJcq0JE5DyK9f8/CK28Dt50YpllCaPn9FhkNLWxmqYZV6Mvx3QFzI2uTlrFDc9'
    'CDtokLA3+Q54jETsDqkvci5s3hnJuXundanYBRRlbT+aXDJ4Bzt5xQ9/fuH4XfRV4F6BP3uyQua7rQet4wmJvnp9dTW8vfv52+Hm'
    '7vLq8i+PWqu+hTnkmTp54KtP59kX0dOie7bKl6/CiHYTxIyWYHHWDmcd8ebmC2cw3vTsdNdft+OEnM8P/5oNyrDd+3yEXmryyCDV'
    'VBC5VipJhuK8TyTOPt+l2xre+bemDIqCkQhVKt4FSZaAioIdOlJU7Ig0u9uwDD+qFDwygYDbOQ2fg1He3FdOuNqeR1fgueQ7Zgse'
    'QpFHTw87jD2NE2df/MTr8igJH2/O54Z1HfMoCxxgHZ+9Lo3ZB3n7SRtSmXk0zWpj7vD/Jf1JNOSYvEiFGkw9ZVp98/vai15Riu+H'
    'icDF+MFubvqiLApsZ1cTz6RGiv39xc2f/c+sqYuvZu03ooTzJIob6dQJ8t53vz0tZESefY1EcmrZpFltFyu8cFq+3ky1J1ZQO6NS'
    '8a12A3w4B2NezdoSns14sXY/uPeuf/3kWoEKo+2ZhA65VKFnGyTJ2itj0VSNomnawerK0wtlRZO/2CrcZF2QzUNt9erRDCy3RHoI'
    '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'
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


IDLE_WORK = 1
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
