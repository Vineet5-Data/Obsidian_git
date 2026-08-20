"""Pool route 90635979_p1."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vW9cR/S9acxFSsuJ0p9ovsRDFMiS5RGoIQYCmKFCki7S7Iv+9isyPxzczZ87M3PtIu16Zpki++31nzpw58+G/Z3//+bdf'
    'f/nt7E8fzt5d3d+fPS7O/vHzv/7276c3nl7++vNv//zlP0+vP5y9ub4bnv7Kvfjz+x9/unp7/cPVzdni7NXt+myxEm/fvxmGd6M/'
    '3A/D66e312+Gq4ezxdeTt38Ybm7fni2Wu4+/u7t9/f7Vw/4bLx4ff18c9Of61ffv3+2ftBz17cPZerh/eG7r29u7hzfPr3ZvTV4c'
    'DsT9cHOzf+rSfOruA+On7v46HpTrm9c/PQ3+w/vN6HHtUAdBNGfzE1oT9sNiPzI3BuChm6+c9+/59NdHrdlPuTL507fGz57O9c3V'
    'q2E3kgePkH3THipegYd9O94fh4O7acYfa+qP33r6/9uH3Z7R34k8+dXVdAAnbXkaqquH4W7yavvQ/acmzUAjOzmLdo0Yt3y4ujee'
    'Hvrl/Q/KYdo9Yvfi/va9M1zyCcpC37V498Nth2u6JpqPmlgCsv3KMz++yE38vr1oxiqDJo+f0WFQGq3NqmGmeTH+dGK80GKTm7PN'
    'wE0Pwg4jSKw3+Q64RjLrDg1f5lzYvDNq5/4d61G5ByiDtfvT5JHJHuzbK37444vA76KPAvMKfG27CpnPWhdt4IZEH729uRlePfz0'
    '7XD3cH1z/dfnUWvdhTnaMzXywEe359mXppebHtkqXz4KPdqNEzOagsWF7c4G/M3NBy6gvxnZ6aFv235CzeaH32adMrzuYzZCr2GK'
    'tEEOUwPPteUgSVect4nE2Rd7tD3Ce/vWbYMywKgJrYZ47yR5DVQGODBGyhAHPM3ua1i6H60GeLQEEmbn1H1OenlzP7lgakeursS9'
    'FDtmG1xCmaunxzrM3caFsy9/4nW5StLHW/De8J7jHmWJA6zj3RsaMf8gt2/a1JC5R9Osayzs/n9OX8m6HJMXJVeDiadMo29xW3vR'
    'y0uJ/TDhuDg/2M1MXzTzAm10tXAnGRD7m6u7v8TvrKmJr6L2m6akcRLFjAyOCbLe9789DWRk7j4DSC5Nm1xWu8lKT5yG17tQe2EG'
    'tTOq5N9qHeDdOejzaqutYNmMJ2v/gwfvxudPzhWIMPqWSeqQKwV6dk6SjL0yK5qKUZhLOxld2b5QZrT4i1bgpmqCbC611YvnZeCZ'
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
