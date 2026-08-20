"""Family-A pool route 90666168_p0."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    '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'
    'M63knpC6J5Es4/0f9/8DtQV2bQ=='
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
