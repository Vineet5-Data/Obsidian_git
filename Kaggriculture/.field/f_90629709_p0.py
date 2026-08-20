"""Pool route 90629709_p0."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vHMmR/C985oPmgxR5b1xpfBLMFQWKuoFvQSwWOBsGDr6Htd8O999PK81093RGRkZmVc9Klt8G5Ex3VVZ1dWZkZORP/3vx'
    'l19+/duff734t58u3t99+HDxfHnx11/+57/+/ukPnz7+7Zdf//vP//j0+aeLN28fd5/+q3344eOffr579/bHu/uLy4sPb3a79xeX'
    'a/OPVw/7yZ8/7HavP/1x/2Z393Rx+XL25x939w/vLi5X6+fn/7s8GfXbV3/8+H5ytWH8P13sdx+ePo/n3cPj05vPnw6TnPxuOrwv'
    'Pzid+G+DeP/48Prjq6dxeGYYP3x8e//6509Xf/r42QaTUYw3Z8MYLjx+bzqO+azv717tDpPWb2b+Se5wsN3k0vMpwlu4XyK3IrYb'
    'VvDThN+N9j814cEWXxay0X7H+3zZb5/3xN3T7vH0jn/4bU9OR3X4dsqc43XHSR5v8OruYLzDlzoZb5zUcKfhO3brhzOwawJsZTfE'
    '7Gd8lU5uIFrPbojYjMfrJc037IQG89GtNuwEfavNrytabdwJXYyFH9T5hCOrzd9JotUmf9LNZm7VyVpgDr5FzL8mD1fBWMAgvo2E'
    'B5JMxXzoZCL7wTFat3HPbNVt3Kcfzn/Zw1niOHjQz9m47tbwhdT1jN90OECbrjE/Wn+vcRTsa65xdKn+KSazu2tfmB7jePVwf797'
    '9fTzH3aPT2/v3/7n6curcsUPDx/bl6n/sF4/Prxf9mn6sLv/LXSbDHmM4BbZEOEJtGq83lfzxDHDl3dOZt/2ugmIaZO7ScUYCqvL'
    'UYE4cpyv9PQyo7OuX29+vp1cD62A8bCgSceHw7HU6jkMUMaBAP/X+nQN97ZGHZ0wa9Su026yf2yExOGYgwhiI2RuTQK60tr3mjYI'
    'W77TeYOTZKGJuxFRp3vPnQA43eHDl28vd+vvYNb8Ra7EwovZgNz6n9MEhdD+a71z3+t/S1eb+bfbjH+7Vf1b7uhucTZN8ayUpNjh'
    'YgrqyBwocIv57YVIKeWqJm/ZZq6TLFLN25+jpL1thQIg5lbO/le5pTWinRHIScKDturEkzsWpph5k7HXev2GxKYhBN8DdhPv1xIV'
    'bjq+tBMvssSADHryO4zhqzMKSGx+9zYBh+6/jNIrq/VVDuGbTgwudVk5V+j5yc7bv4sHfeURz/p40NMArbcPTXlcCznRA9OlyYkm'
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
