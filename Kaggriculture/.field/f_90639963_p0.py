"""Pool route 90639963_p0."""

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
