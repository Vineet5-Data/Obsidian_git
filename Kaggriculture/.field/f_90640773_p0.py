"""Pool route 90640773_p0."""

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
