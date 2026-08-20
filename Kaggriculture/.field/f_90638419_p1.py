"""Pool route 90638419_p1."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vHMmR/C985oPmgxR5b1xpbBHmigIleeBbEIsFzoaBg+9h794O999PK81093RGRkZmVc9Klt8G5Ex3VVZ1dWZkZORP/3vx'
    't19+/cdff734t58u3t29f3/xfHnx91/+6z/++9MfPn38xy+//udf/+fT558u3tw/7T79V/vww8e//Hz39v7Hu4eLy4v3b3a7dxeX'
    'a/OPV4/7yZ/f73avP/1x/2Z39+Hi8uXszz/uHh7fXlyu1s/P/3d5Mur7V3/6+G5ytWH8P13sd+8/fB7P28enD28+fzpMcvK76fC+'
    '/OB04r8N4t3T4+uPrz6MwzPD+OHj/cPrnz9d/cPHzzaYjGK8ORvGcOHxe9NxzGf9cPdqd5i0fjPzT3KHg+0ml55PEd7C/RK5FbHd'
    'sIKfJvx2tP+pCQ+2+LKQjfY73ufLfvu8J+4+7J5O7/iH3/bkdFSHb6fMOV53nOTxBq/uDsY7fKmT8cZJDXcavmO3fjgDuybAVnZD'
    'zH7GV+nkBqL17IaIzXi8XtJ8w05oMB/dasNO0Lfa/Lqi1cad0MVY+EGdTziy2vydJFpt8ifdbOZWnawF5uBbxPxr8nAVjAUM4ttI'
    'eCDJVMyHTiayHxyjdRv3zFbdxn364fyXPZwljoMH/ZyN624NX0hdz/hNhwO06Rrzo/X3GkfBvuYaR5fqn2Iyu7v2hekxjlePDw+7'
    'Vx9+/sPu6cP9w/2/n768Kld8//ixfZn6D+v10+O7ZZ+m97uH30K3yZDHCG6RDRGeQKvG6301TxwzfHnnZPZtr5uAmDa5m1SMobC6'
    'HBWII8f5Sk8vMzrr+vXm59vJ9dAKGA8LmnR8OBxLrZ7DAGUcCPB/rU/XcG9r1NEJs0btOu0m+8dGSByOOYggNkLm1iSgK619r2mD'
    'sOU7nTc4SRaauBsRdbr33AmA0x0+fPn2crf+DmbNX+RKLLyYDcit/zlNUAjtv9Y7973+t3S1mX+7zfi3W9W/5Y7uFmfTFM9KSYod'
    'LqagjsyBAreY316IlFKuavKWbeY6ySLVvP05StrbVigAYm7l7H+VW1oj2hmBnCQ8aKtOPLljYYqZNxl7rddvSGwaQvA9YDfxfi1R'
    '4abjSzvxIksMyKAnv8MYvjqjgMTmd28TcOj+yyi9slpf5RC+6cTgUpeVc4Wen+y8/bt40Fce8ayPBz0N0Hr70JTHtZATPTBdmpxo'
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
