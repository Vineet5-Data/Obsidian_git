"""Pool route 90634316_p1."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vXNdy/C9cc2EOPyRlR0vzIuHRlkBJIV4MwjCQFwQIXhZOdkH+e2STnLlzu7qqus8ZWTK08ng4uvd8n+7q6uqf/vfk33/5'
    '9R9///Xkn346+f7jm5tXP7+7fv/h4+325P705D9++a9/++9Pf/n08R+//Pqff/+fT59/Onn95ve/eh++//i3n99vt69OTk/uXm+v'
    'P5ycPl99/cP25u2PJ6cvVl+//3B7fff99vb2byenZ09/u/7xzQ/XN5/++vLt3cnpefj6/evt9t1vv7//v9Nlz969efnXj++e/t3Z'
    'oms/ndxt33/4vanxw49vbz+8Xny1HIf1G26uX24fX+A+fj3ezmtIR+Lj9u1f9wS+62Ew392+ffXx5Yf9hF1VRnN7nXaO/OmxeaTj'
    'Tx1YvGrXjF07Dzq6+/NuUUya0b/8tkCTQV28/ub6xw+75c1e9PiPF294ef04LquHLN8E/nT9YXtrzej5vdvXRRcfnn66//HDuB7+'
    'TU/kY9/4eO4GoDOej+sM7cHR8fT7sh+S/YZbfVVaEvH0IH15//ajmIX4gsd/s3jww2IJc7/628g6B6OFFpyeiE9nyfvV4fDwDTnM'
    'rdVKHpwPBftm6JVhSIp7j/WGfDjsxPTnD02v/PDtse89i+LxbricYPetXvG4zafbXOTijM9d/almarx8e3Ozffnh579sbz+8uXnz'
    'r+GwWlxd+KfyrWSQSK/kY+NlKJuaX8Ol5tOByIxTeRTEOUemLbhOdBfoowcvqKfbFT4cPtK/o8DKyW8HMEylMwft006jvVsOmE5H'
    'uiy0O/Dtbvv22G+P/dzmyNlnNUfAIblr0OIeO72wjgx4A4qbq37DAytI3Lyp0dXzSO3XoR/W7LBoElnAVuHBQwYpeDC65XNYbuaz'
    'd6NsmxH73x/46OAxfRvr8V9BY2X/oB1UWO1ENHeTR+2+3r9+8YPeG/aP2n21/lvNRIyP2aM0q7/VHgwes3cydr3QMBJ9NLDj1v0o'
    'YWuLJ8fdWjAQGd5KbFA5zsRYjmjUkIWYPmX6Db5ABac+91jt/XIMGX75D0TU3m9vblbmyOZebp7mBZcEEC7vffMA3ND7/RbAp2HX'
    'X1glnQCFNjZOn6zKAWuwgDGNGIds/pfGg+iNZUO1DJ0qDLP/pC8V04hC+ElnRNAT450uLxY01vF5qNHy0cAe2x/5/JMcENc4QJ/q'
    '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'
    'GRRoeg=='
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
