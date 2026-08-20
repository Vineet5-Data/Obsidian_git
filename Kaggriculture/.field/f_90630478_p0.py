"""Pool route 90630478_p0."""

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
