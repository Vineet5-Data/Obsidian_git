"""Pool route 90640790_p1."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    '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'
    'efjfw/8B8qz8MA=='
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
