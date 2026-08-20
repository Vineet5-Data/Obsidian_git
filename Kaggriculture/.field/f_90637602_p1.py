"""Pool route 90637602_p1."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    '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'
    'p914fAXgMtUIpH2XkQYfm/9s/gtMN9F3'
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
