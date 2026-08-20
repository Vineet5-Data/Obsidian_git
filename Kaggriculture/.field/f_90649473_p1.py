"""Pool route 90649473_p1."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vHMmR/C985gPngxR1b1xpbAnmigIleWAviMUC9uGAg+9h7bfD/ffTSjPdPZ2RkZFZ1SNp5bcBOdNdlVVdnRkZGfnT/178'
    '5y+//uPvv178x08Xb+/evbt4urz4r1/+52///PiHjx//8cuv//33f338/NPFq9ePu4//1T788OEvP9+9ef3j3f3F5cW7V7vd24vL'
    'tfnHi4f95M/vdruXH/+4f7W7e39x+Wz25x939w9vLi5X66en/7s8GfXrF3/68HZytWH8P13sd+/efxrPm4fH968+fTpMcvK76fA+'
    '/+B04r8N4u3jw8sPL96PwzPD+OHD6/uXP3+8+vsPn2wwGcV4czaM4cLj96bjmM/6/u7F7jBp/Wbmn+QOB9tNLj2fIryF+yVyK2K7'
    'YQU/TvjNaP9TEx5s8XkhG+13vM/n/fZpT9y93z2e3vEPv+3J6agO306Zc7zuOMnjDV7cHYx3+FIn442TGu40fMdu/XAGdk2AreyG'
    'mP2Mr9LJDUTr2Q0Rm/F4vaT5hp3QYD661YadoG+1+XVFq407oYux8IM6n3Bktfk7SbTa5E+62cytOlkLzMG3iPnX5OEqGAsYxLeR'
    '8ECSqZgPnUxkPzhG6zbuma26jfv0w/kvezhLHAcP+jkb190avpC6nvGbDgdo0zXmR+uXGkfBvuYaR5fqdzGZ3V37wvQYx4uH+/vd'
    'i/c//2H3+P71/eu/nr68Kld89/ChfZn6D+vl48PbZZ+md7v730K3yZDHCG6RDRGeQKvG6301TxwzfHnnZPZtr5uAmDa5m1SMobC6'
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
