"""Pool route 90631223_p1."""

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
