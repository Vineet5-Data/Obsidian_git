"""Pool route 90639993_p1."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrlXV1vHEly/C985gPnk0O/caU5SziuKFCUB+cFsVjAZxgwzg9rvxn+79aK89HTGRkZmVU9ku7eBuRMd1ZWdXVlZGTkL/979e+/'
    '/f63v/5+9U+/XH28//Tp6uX66j9++69/++8vf/jy8W+//f6ff/2fL59/uXr3/mn75b/ah58+/+XX+w/vf75/uLq++vRuu/14dT03'
    '/3jzuBv8+dN2+/bLH3fvtvfPV9e3oz//vH14/HB1PZu/vPzf9ZnV79/8+fPHwdWO9v9ytdt+ev5qz4fHp+d3Xz/tBzn43dC81x+c'
    'D/wPIz4+Pb79/Ob5ZJ4x46fP7x/e/vrl6s+fv/pgYMXp5syM44VP3xvaMR71w/2b7X7Q+s3MP8kd9r4bXHo8RHgL90vkVsR3xxn8'
    'MuAPJ/+fu3Dvi9eJbPTf4T6v6+3rmrh/3j6NhvunPxbl0Kz911P+PF0YrNM393v37b/VyX2nYR3dd/yOXfzhEOysIG/ZNTH6HZ+o'
    'sztw/w3HO1oTsR8P19P89+nx83gxNDiQL7fjYtCX2/jCot9OH7q467QuTu4CQ478dvBE2nGnv+meAzejT2rCZeM37Pkm5j2g4CEr'
    'OOw0AQOnHPcA46f4yUSTcjTZfOjkJfvB8Vvq+sAjyDX5CzPDzz9c/rL7TcU57sFTz8I9fB2/kLqeOUXtt9Kma4w32W9lR8G/5hrm'
    'GfuRB7O9b5+YHna8eXx42L55/vVP26fn9w/v//X8LVa54mFv/c7Mevv0+LH1Gjwo/LR9+COQG5h8iudar13bgWaN1/tunji2jZVX'
    'Tmbd9roJiHCTq0lFHAqzC090mTB5PNXw2J654HiHO7sgmgN7FoVePT0fjrNmL2G0Ag695qzd6ebWr6eD2Ck29kPXhlu3zUDshcQO'
    'KYEG4z/1ujeJ76R4capxo0//qAMH+8lEI9cC3oabj4+HUUT/+v3pbm4HbkLoi458/63OA+ev9eGY0aep/XAc8wA+OgS4F3UDM6Sv'
    'EwrR/vd6577X/5GuNjryLjNH3qV65OVn3yVOtykHLXYiPk+3zSQ0kh2o0GtldH8hekqdXcPTHDOg0XtnaadaOADOfYVxqI5Mo+H0'
    'TFY9+9PAIzh8Vw/97nqsjTL11gcuPr6B6ndkfkVv9xF43wOvGwyI37ElmFz0OORUXnkJkwz0Mrz3ca4nNkL3y6Ussvv28c7OJveN'
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
