"""Pool route 90630478_p1."""

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
