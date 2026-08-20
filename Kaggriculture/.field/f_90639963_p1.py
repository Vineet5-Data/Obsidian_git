"""Pool route 90639963_p1."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    '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'
    'm+xcE3O+u12epadfvf9//DSwWg=='
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
