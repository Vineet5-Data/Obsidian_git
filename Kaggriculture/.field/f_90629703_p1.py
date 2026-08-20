"""Pool route 90629703_p1."""

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
