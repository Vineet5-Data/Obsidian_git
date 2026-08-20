"""Pool route 90639951_p1."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vHEly/C985gPngxTlN640dyKOKwqUdIPzglgs4DMMGOeHtd8M/3drxWF3T2dkZGRW9Sy1urcBOdNdlVVdnRkZGfnT/579'
    '+y+//uPvv579y09nH24+fjx7PD/7j1/+69/++8sfvnz8xy+//uff/+fL55/O3t0+7L78V/vww+e//Xzz/vbHm7uz87OP73a7D2fn'
    'a/OPN/f7yZ8/7nZvv/xx/2538+ns/NXszz/u7u7fn52v1o+P/3d+NOrbN3/5/GFytWH8P53tdx8/fR3P+/uHT+++fjpMcvK76fCe'
    'fnA88d8G8eHh/u3nN5/G4Zlh/PD59u7tz1+u/unzVxtMRjHenA1juPD4vek45rO+u3mzO0xav5n5J7nDwXaTS8+nCG/hfoncithu'
    'WMEvE34/2v/YhAdbPC1ko/2e7/O0377uiZtPu4fjO/7ptz05HdXh2ylzjtcdJ/l8gzc3B+MdvtTJeOOkhjsN37FbP5yBXRNgK7sh'
    'Zj/jq3R0A9F6dkPEZny+XtJ8w05oMB/dasNO0Lfa/Lqi1cad0MVY+EGdTziy2vydJFpt8ifdbOZWnawF5uBbxPxr8nAVjAUM4ttI'
    'eCDJVMyHTiayHxyjdRv3zFbdxn384fSXPZwljoMH/ZyN624NX0hdz/hNhwO06Rrzo/X3GkfBvuYazy7VH2Iyu5v2hekxjjf3d3e7'
    'N59+/tPu4dPt3e2/Hr+8Klf8eP+5fZn6D+vtw/2HZZ+mj7u730K3yZDHCG6RDRGeQKvG672YJ44ZvrxzMvu2101ATJvcTSrGUFhd'
    'jgrEkeN8paeXGZ11/Xrz8+3oemgFjIcFTTo+HI6lVo9hgDIOBPi/1qdruLc16uiEWaN2nXaT/WMjJA7HHEQQGyFzaxLQlda+17RB'
    '2PKdzhucJAtN3I2IOt177gTA6Q4fnr693K2/g1nzF7kSCy9mA3LrP6YJCqH9S71z3+t/S1eb+bfbjH+7Vf1b7uhucTZN8ayUpNjh'
    'YgrqyBwocIv57YVIKeWqJm/ZZq6jLFLN25+jpL1thQIg5lbO/le5pTWinRHIScKDturEkzsWpph5k7HXev2GxKYhBN8DdhPv1xIV'
    'bjq+tBMvssSADHryO4zhxRkFJDa/e5uAQ/efRumV1XqRQ/imE4NLXVbOFXp+svP27+JBX3rEsz4e9DRA6+1DUx7XQk70wHRpcqIJ'
    '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'
    '/H9hrQiC'
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
