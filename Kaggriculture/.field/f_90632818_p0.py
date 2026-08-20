"""Pool route 90632818_p0."""

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
