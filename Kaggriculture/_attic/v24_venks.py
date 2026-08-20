"""v24: family-A route venks 143251, fresh pool 90630506_p1, plus weed repair + price-impact SELL ordering."""

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
