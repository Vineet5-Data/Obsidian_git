"""Single-file route agent distilled from elite episode 90452532.

The episode contains two near-identical top-player policies.  Actions are stored
without observations or identities; runtime hand alignment keeps the public
route legal when stochastic state changes alter accepted hires.
"""

import base64
import copy
import json
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    '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'
    )
)).decode("utf-8"))


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


ANIMAL_SWITCH_DAY = 3
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


def _tile_at(farm, position):
    try:
        x, y = int(position[0]), int(position[1])
    except (TypeError, ValueError, IndexError):
        return None
    rows = _get(farm, "tiles", []) or []
    if 0 <= y < len(rows):
        row = rows[y] or []
        if 0 <= x < len(row):
            return row[x]
    return None


def _idle_task(tile):
    """A useful in-place action for a unit that the route left idle.

    Movement is never emitted: the recorded route addresses units by index and
    assumes their positions, so relocating one would desynchronise every later
    order.  Only same-tile buffs are used.
    """
    if not isinstance(tile, dict):
        return None
    if tile.get("kind") == "PASTURE" and tile.get("animal"):
        if not tile.get("cared_today"):
            return ["CARE"]
    elif tile.get("kind") == "PLANT" and tile.get("crop"):
        if not tile.get("watered_today"):
            return ["WATER"]
    return None


def _fill_idle_units(obs, action):
    if not IDLE_WORK:
        return action
    farm, _private = _farm_private(obs)
    units = [(_get(farm, "farmer", None), action.get("farmer") or ["PASS"])]
    hands = [list(order or ["PASS"]) for order in (action.get("hands") or [])]
    positions = list(_get(farm, "hands", []) or [])
    for index, order in enumerate(hands):
        units.append((positions[index] if index < len(positions) else None, order))

    filled = []
    for position, order in units:
        if order and order[0] != "PASS":
            filled.append(order)
            continue
        task = _idle_task(_tile_at(farm, position)) if position is not None else None
        filled.append(task or ["PASS"])
    action["farmer"] = filled[0]
    action["hands"] = filled[1:]
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
