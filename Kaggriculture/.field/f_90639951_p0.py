"""Pool route 90639951_p0."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vHMmR/C985gPngxTlN640tgRzRYGSbuBbEIsFbMPAwfewd2+H++/WisPuns7IyMis6hG18tuAnOmuyqquzoyMjPzp/87+'
    '/suv//zbr2d/+Ons/c2HD2cP52f/+OW///o/n//w+eM/f/n1v/72v58//3T25u397vN/tQ8/fPrLzzfv3v54c3t2fvbhzW73/ux8'
    'bf7x6m4/+fOH3e715z/u3+xuPp6dv5j9+cfd7d27s/PV+uHh/8+PRv321Z8/vZ9cbRj/T2f73YePX8bz7u7+45svnw6TnPxuOrzH'
    'HxxP/LdBvL+/e/3p1cdxeGYYP3x6e/v6589X//jpiw0moxhvzoYxXHj83nQc81nf3rzaHSat38z8k9zhYLvJpedThLdwv0RuRWw3'
    'rODnCb8b7X9swoMtHhey0X5P93ncb1/2xM3H3f3xHf/4256cjurw7ZQ5x+uOk3y6waubg/EOX+pkvHFSw52G79itH87Argmwld0Q'
    's5/xVTq6gWg9uyFiMz5dL2m+YSc0mI9utWEn6Fttfl3RauNO6GIs/KDOJxxZbf5OEq02+ZNuNnOrTtYCc/AtYv41ebgKxgIG8W0k'
    'PJBkKuZDJxPZD47Ruo17Zqtu4z7+cPrLHs4Sx8GDfs7GdbeGL6SuZ/ymwwHadI350fq1xlGwr7nGk0v1u5jM7qZ9YXqM49Xd7e3u'
    '1cef/7i7//j29u1/Hr+8Klf8cPepfZn6D+v1/d37ZZ+mD7vb30K3yZDHCG6RDRGeQKvG6z2bJ44ZvrxzMvu2101ATJvcTSrGUFhd'
    'jgrEkeN8paeXGZ11/Xrz8+3oemgFjIcFTTo+HI6lVg9hgDIOBPi/1qdruLc16uiEWaN2nXaT/WMjJA7HHEQQGyFzaxLQlda+17RB'
    '2PKdzhucJAtN3I2IOt177gTA6Q4fHr+93K2/g1nzF7kSCy9mA3Lr36cJCqH9c71z3+t/S1eb+bfbjH+7Vf1b7uhucTZN8ayUpNjh'
    'YgrqyBwocIv57YVIKeWqJm/ZZq6jLFLN25+jpL1thQIg5lbO/le5pTWinRHIScKDturEkzsWpph5k7HXev2GxKYhBN8DdhPv1xIV'
    'bjq+tBMvssSADHryFcbw7IwCEpvfvU3Aoftvo/TKaj3LIXzTicGlLivnCj0/2Xn7d/GgLz3iWR8Pehqg9fahKY9rISd6YLo0OdGE'
    '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'
    'B/fwL4RsJ5E='
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
