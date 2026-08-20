"""Pool route 90634316_p0."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vHMmR/C985oPmgxTpN640tgRzRYGSbuBbEIsFbMPAwfewd2+H++/WisPuns7IyMis6hG18tuAnOmuyqquzoyMjPzp/87+'
    '/suv//zbr2d/+Ons/c2HD2cP52f/+OW///o/n//w+eM/f/n1v/72v58//3T25u397vN/tQ8/fPrLzzfv3v54c3t2fvbhzW73/ux8'
    'bf7x6m4/+fOH3e715z/u3+xuPp6dv5z9+cfd7d27s/PV+uHh/8+PRv321Z8/vZ9cbRj/T2f73YePX8bz7u7+45svnw6TnPxuOrzH'
    'HxxP/LdBvL+/e/3p1cdxeGYYP3x6e/v6589X//jpiw0moxhvzoYxXHj83nQc81nf3rzaHSat38z8k9zhYLvJpedThLdwv0RuRWw3'
    'rODnCb8b7X9swoMtHhey0X5P93ncb1/2xM3H3f3xHf/4256cjurw7ZQ5x+uOk3y6waubg/EOX+pkvHFSw52G79itH87Argmwld0Q'
    's5/xVTq6gWg9uyFiMz5dL2m+YSc0mI9utWEn6Fttfl3RauNO6GIs/KDOJxxZbf5OEq02+ZNuNnOrTtYCc/AtYv41ebgKxgIG8W0k'
    'PJBkKuZDJxPZD47Ruo17Zqtu4z7+cPrLHs4Sx8GDfs7GdbeGL6SuZ/ymwwHadI350fq1xlGwr7nGk0v1u5jM7qZ9YXqM49Xd7e3u'
    '1cef/7i7//j29u1/Hr+8Klf8cPepfZn6D+v1/d37ZZ+mD7vb30K3yZDHCG6RDRGeQKvG6z2bJ44ZvrxzMvu2101ATJvcTSrGUFhd'
    'jgrEkeN8paeXGZ11/Xrz8+3oemgFjIcFTTo+HI6lVg9hgDIOBPi/1qdruLc16uiEWaN2nXaT/WMjJA7HHEQQGyFzaxLQlda+17RB'
    '2PKdzhucJAtN3I2IOt177gTA6Q4fHr+93K2/g1nzF7kSCy9mA3Lr36cJCqH9c71z3+t/S1eb+bfbjH+7Vf1b7uhucTZN8ayUpNjh'
    'YgrqyBwocIv57YVIKeWqJm/ZZq6jLFLN25+jpL1thQIg5lbO/le5pTWinRHIScKDturEkzsWpph5k7HXev2GxKYhBN8DdhPv1xIV'
    'bjq+tBMvssSADHryFcbw7IwCEpvfvU3Aoftvo/TKaj3LIXzTicGlLivnCj0/2Xn7d/GgLzziWR8Pehqg9fahKY9rISd6YLo0OdGE'
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
