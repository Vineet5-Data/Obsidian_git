"""v24: family-A route Youssef 145950, fresh pool 90635229_p1, plus weed repair + price-impact SELL ordering."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    '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'
    'M3rC9jfjw/8A7NdbHw=='
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
