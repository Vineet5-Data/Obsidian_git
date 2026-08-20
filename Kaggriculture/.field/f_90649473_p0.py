"""Pool route 90649473_p0."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vHMmR/C985gPngxTlN640tgRzRYGSbuBbEIsFbMPAwfewd2+H++/WSjPdPZ2RkZFZ1SNp5bcBOdNdlVVdnRkZGfnT/138'
    '/Zdf//m3Xy/+8NPF27t37y6eLi/+8ct///V/Pv7h48d//vLrf/3tfz9+/uni1evH3cf/ah9++PCXn+/evP7x7v7i8uLdq93u7cXl'
    '2vzjxcN+8ud3u93Lj3/cv9rdvb+4fDb784+7+4c3F5er9dPT/1+ejPr1iz9/eDu52jD+ny72u3fvP43nzcPj+1efPh0mOfnddHif'
    'f3A68d8G8fbx4eWHF+/H4Zlh/PDh9f3Lnz9e/f2HTzaYjGK8ORvGcOHxe9NxzGd9f/did5i0fjPzT3KHg+0ml55PEd7C/RK5FbHd'
    'sIIfJ/xmtP+pCQ+2+LyQjfY73ufzfvu0J+7e7x5P7/jH3/bkdFSHb6fMOV53nOTxBi/uDsY7fKmT8cZJDXcavmO3fjgDuybAVnZD'
    'zH7GV+nkBqL17IaIzXi8XtJ8w05oMB/dasNO0Lfa/Lqi1cad0MVY+EGdTziy2vydJFpt8ifdbOZWnawF5uBbxPxr8nAVjAUM4ttI'
    'eCDJVMyHTiayHxyjdRv3zFbdxn364fyXPZwljoMH/ZyN624NX0hdz/hNhwO06Rrzo/VLjaNgX3ONo0v1u5jM7q59YXqM48XD/f3u'
    'xfuf/7h7fP/6/vV/nr68Kld89/ChfZn6D+vl48PbZZ+md7v730K3yZDHCG6RDRGeQKvG6301TxwzfHnnZPZtr5uAmDa5m1SMobC6'
    'HBWII8f5Sk8vMzrr+vXm59vJ9dAKGA8LmnR8OBxLrZ7CAGUcCPB/rU/XcG9r1NEJs0btOu0m+8dGSByOOYggNkLm1iSgK619r2mD'
    'sOU7nTc4SRaauBsRdbr33AmA0x0+fP72crf+DmbNX+RKLLyYDcitf58mKIT2X+ud+17/W7razL/dZvzbrerfckd3i7NpimelJMUO'
    'F1NQR+ZAgVvMby9ESilXNXnLNnOdZJFq3v4cJe1tKxQAMbdy9r/KLa0R7YxAThIetFUnntyxMMXMm4y91us3JDYNIfgesJt4v5ao'
    'cNPxpZ14kSUGZNCTLzCGr84oILH53dsEHLr/NkqvrNZXOYRvOjG41GXlXKHnJztv/y4e9LVHPOvjQU8DtN4+NOVxLeRED0yXJiea'
    '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'
    )
)))


USE_WEED = 1
# Measured OFF: the stationary idle layer lost 0-12-0 (margin -519) to the same
# agent with it disabled.  rayk's +258 on a different host does not transfer to
# this route - the extra output depresses our own premium prices.
USE_IDLE = 0
USE_IMPACT = 1

_WEED_REPLAY_STEPS = 8
_WEED_STATE = {0: {}, 1: {}}

SELLABLE_PRODUCTS = {
    "WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON",
    "EGG", "MILK", "WOOL", "FERTILIZER",
}

# base, equilibrium, scale, below shape/target, above shape/target
_MARKET_PARAMS = {
    "WHEAT": (25, 10000, 400, "sqrt", 0.8, "log", 0.2),
    "CARROT": (35, 10000, 450, "log", 0.2, "sqrt", 0.7),
    "TOMATO": (60, 10000, 200, "linear", 0.4, "sqrt", 0.6),
    "STRAWBERRY": (120, 10000, 100, "sqrt", 0.7, "linear", 1.6),
    "MELON": (250, 10000, 300, "log", 0.2, "sq", 3.6),
    "EGG": (50, 10000, 332, "linear", 0.4, "log", 0.2),
    "MILK": (160, 10000, 122, "sqrt", 0.6, "linear", 1.6),
    "WOOL": (200, 10000, 105, "log", 0.2, "sq", 3.2),
    "FERTILIZER": (100, 10000, 200, "linear", 0.4, "linear", 0.4),
}


def _get(value, key, default=None):
    if isinstance(value, dict):
        return value.get(key, default)
    getter = getattr(value, "get", None)
    if callable(getter):
        return getter(key, default)
    return getattr(value, key, default)


def _seat(obs):
    return 1 if int(_get(obs, "player", 0) or 0) == 1 else 0


def _farm(obs):
    farms = list(_get(obs, "farms", []) or [])
    seat = _seat(obs)
    return farms[seat] if seat < len(farms) else {}


def _aligned(action, obs):
    action = copy.deepcopy(action or {})
    expected = len(_get(_farm(obs), "hands", []) or [])
    hands = [list(order or ["PASS"]) for order in (action.get("hands") or [])]
    if len(hands) < expected:
        hands.extend([["PASS"] for _ in range(expected - len(hands))])
    return {
        "farmer": list(action.get("farmer") or ["PASS"]),
        "hands": hands[:expected],
        "market": [list(order) for order in (action.get("market") or [])][:10],
    }


# --------------------------------------------------------------------------
# weed repair
# --------------------------------------------------------------------------
def _tile_at(farm, position):
    try:
        x, y = int(position[0]), int(position[1])
        return (_get(farm, "tiles", []) or [])[y][x]
    except (IndexError, TypeError, ValueError):
        return "LOCKED"


def _trace_actor_action(step, actor):
    trace = _ACTIONS[min(max(int(step), 0), len(_ACTIONS) - 1)] or {}
    if actor == "farmer":
        return list(trace.get("farmer") or ["PASS"])
    hands = trace.get("hands", []) or []
    return list(hands[actor] if actor < len(hands) else ["PASS"])


def _weed_repair(obs, action, step):
    if not USE_WEED:
        return action
    action = _aligned(action, obs)
    seat = _seat(obs)
    game = _WEED_STATE[seat]
    if step == 0 or step < game.get("last_step", -1):
        game = {"last_step": step, "active": {}}
        _WEED_STATE[seat] = game
    game["last_step"] = step
    farm = _farm(obs)
    positions = [_get(farm, "farmer"), *list(_get(farm, "hands", []) or [])]
    units = [action.get("farmer", ["PASS"]), *list(action.get("hands") or [])]
    active = game["active"]

    for actor, transaction in list(active.items()):
        index = 0 if actor == "farmer" else int(actor) + 1
        if index >= len(units):
            active.pop(actor, None)
            continue
        age = step - transaction["start"]
        if age == 1:
            units[index] = list(transaction["intended"])
        elif 2 <= age <= 1 + _WEED_REPLAY_STEPS:
            units[index] = _trace_actor_action(step - 1, actor)
        else:
            active.pop(actor, None)

    for index, (position, intended) in enumerate(zip(positions, units)):
        actor = "farmer" if index == 0 else index - 1
        if actor in active or not isinstance(intended, list) or not intended:
            continue
        if intended[0] not in ("BUILD_PASTURE", "PLANT"):
            continue
        tile = _tile_at(farm, position)
        if not isinstance(tile, dict) or tile.get("kind") != "WEED":
            continue
        active[actor] = {"start": step, "intended": list(intended)}
        units[index] = ["DIG"]

    action["farmer"] = units[0] if units else ["PASS"]
    action["hands"] = units[1:]
    return _aligned(action, obs)


# --------------------------------------------------------------------------
# stationary idle work -- NOTHING MOVES
# --------------------------------------------------------------------------
def _idle_tile(farm, position):
    try:
        x, y = int(position[0]), int(position[1])
    except (TypeError, ValueError, IndexError):
        return None
    rows = _get(farm, "tiles", []) or []
    if not (0 <= y < len(rows) and 0 <= x < len(rows[y] or [])):
        return None
    tile = rows[y][x]
    return tile if isinstance(tile, dict) else None


def _idle_job(tile, inventory):
    """Best stationary op for this tile, or None. Fertilizer outranks the rest."""
    if tile.get("animal"):
        if tile.get("fertilizer_available"):
            return ["COLLECT_FERTILIZER"]
        if not tile.get("fed_today") and int((inventory or {}).get("WHEAT", 0) or 0) > 0:
            return ["FEED"]
        if int(tile.get("yield_units", 0) or 0) > 0:
            return ["HARVEST"]
        # The engine banks the care bonus only on a day the animal is also fed,
        # so caring an unfed animal spends the op for nothing.
        if tile.get("fed_today") and not tile.get("cared_today"):
            return ["CARE"]
        return None
    if tile.get("kind") == "PLANT" and tile.get("crop") and not tile.get("watered_today"):
        return ["WATER"]
    return None


def _idle_fill(obs, action):
    if not USE_IDLE:
        return action
    farm = _farm(obs)
    private = _get(obs, "private", {}) or {}
    inventories = list(_get(private, "inventories", []) or [])

    def inventory_of(index):
        return inventories[index] if index < len(inventories) else {}

    def job_for(position, inventory):
        tile = _idle_tile(farm, position)
        return _idle_job(tile, inventory) if tile is not None else None

    order = action.get("farmer") or ["PASS"]
    if order and order[0] == "PASS":
        job = job_for(_get(farm, "farmer", [0, 0]), inventory_of(0))
        if job:
            action["farmer"] = job

    hands = list(action.get("hands") or [])
    positions = list(_get(farm, "hands", []) or [])
    for index, order in enumerate(hands):
        if not (order and order[0] == "PASS") or index >= len(positions):
            continue
        job = job_for(positions[index], inventory_of(index + 1))
        if job:
            hands[index] = job
    action["hands"] = hands
    return action


# --------------------------------------------------------------------------
# price-impact SELL slot ranking
# --------------------------------------------------------------------------
def _shape(name, value):
    value = max(0.0, float(value))
    if name == "linear":
        return value
    if name == "sq":
        return value * value
    if name == "sqrt":
        return math.sqrt(value)
    if name == "log":
        return math.log1p(value)
    raise ValueError(name)


def _market_price(item, inventory):
    base, equilibrium, scale, below_f, below_t, above_f, above_t = _MARKET_PARAMS[item]
    if inventory < equilibrium:
        amplitude = below_t * base / _shape(below_f, scale)
        price = base + amplitude * _shape(below_f, equilibrium - inventory)
    else:
        amplitude = above_t * base / _shape(above_f, scale)
        price = base - amplitude * _shape(above_f, inventory - equilibrium)
    return max(1, int(round(price)))


def _is_sell(order):
    return (isinstance(order, (list, tuple)) and len(order) >= 3
            and order[0] == "SELL" and order[1] in _MARKET_PARAMS)


def _impact_score(obs, order):
    if not _is_sell(order):
        return float("-inf")
    item = str(order[1])
    try:
        quantity = max(0, int(order[2]))
    except (TypeError, ValueError):
        return 0.0
    market = _get(obs, "market", {}) or {}
    inventory = _get(market, "inventory", {}) or {}
    prices = _get(market, "prices", {}) or {}
    current_inventory = int(_get(inventory, item, 10000) or 0)
    current_quote = float(_get(prices, item, _market_price(item, current_inventory)) or 0)
    later_quote = float(_market_price(item, current_inventory + quantity))
    return float(quantity) * max(0.0, current_quote - later_quote)


def _impact_slots(obs, action):
    if not USE_IMPACT:
        return action
    market = list(action.get("market") or [])
    rows = [(_impact_score(obs, order), -index, list(order))
            for index, order in enumerate(market) if _is_sell(order)]
    if len(rows) < 2:
        return action
    rows.sort(reverse=True)
    ranked = iter(row[2] for row in rows)
    action["market"] = [next(ranked) if _is_sell(o) else o for o in market]
    return action


# --------------------------------------------------------------------------
def _fix_animal_species(obs, action):
    """Keep a scripted PICKUP/PLACE legal if the two species got swapped."""
    private = _get(obs, "private", {}) or {}
    shed = _get(private, "shed", {}) or {}
    inventories = list(_get(private, "inventories", []) or [])
    units = [action.get("farmer", ["PASS"]), *list(action.get("hands") or [])]
    for index, unit in enumerate(units):
        if not unit or len(unit) < 2 or unit[1] not in ("COW", "SHEEP"):
            continue
        other = "SHEEP" if unit[1] == "COW" else "COW"
        if unit[0] == "PICKUP":
            if int(shed.get(unit[1], 0) or 0) <= 0 and int(shed.get(other, 0) or 0) > 0:
                unit[1] = other
        elif unit[0] == "PLACE":
            inventory = dict(inventories[index] or {}) if index < len(inventories) else {}
            if int(inventory.get(unit[1], 0) or 0) <= 0 and int(inventory.get(other, 0) or 0) > 0:
                unit[1] = other
    action["farmer"] = units[0]
    action["hands"] = units[1:]
    return action


def _terminal_liquidation(obs, action):
    if int(_get(obs, "step", 0) or 0) < len(_ACTIONS) - 1:
        return action
    private = _get(obs, "private", {}) or {}
    shed = _get(private, "shed", {}) or {}
    prices = _get(_get(obs, "market", {}) or {}, "prices", {}) or {}
    stock = [(item, max(0, int(quantity or 0)))
             for item, quantity in shed.items()
             if item in SELLABLE_PRODUCTS and int(quantity or 0) > 0]
    stock.sort(key=lambda pair: (-max(1, int(prices.get(pair[0], 1) or 1)), pair[0]))
    action["market"] = [["SELL", item, quantity] for item, quantity in stock[:10]]
    return _aligned(action, obs)


def agent(obs):
    try:
        step = min(max(0, int(_get(obs, "step", 0) or 0)), len(_ACTIONS) - 1)
        action = _aligned(_ACTIONS[step], obs)
        action = _weed_repair(obs, action, step)
        action = _fix_animal_species(obs, action)
        action = _idle_fill(obs, action)
        action = _impact_slots(obs, action)
        return _terminal_liquidation(obs, _aligned(action, obs))
    except Exception:
        return {
            "farmer": ["PASS"],
            "hands": [["PASS"] for _ in (_get(_farm(obs), "hands", []) or [])],
            "market": [],
        }
