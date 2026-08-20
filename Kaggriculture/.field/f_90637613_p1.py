"""Pool route 90637613_p1."""

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
