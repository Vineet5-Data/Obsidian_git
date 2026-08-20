"""Pool route 90637565_p0."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
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
