"""Loss opponent 90729118."""

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
