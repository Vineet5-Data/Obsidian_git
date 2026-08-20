"""Family-A pool route 90637565_p1."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vW0ly/S961sOQkjWevGntu2thNZYhyUtsBsJggGwQINg8TPIW7H+PVpbIy1tVp059NEU7fjJNkbzd1dXd9XHq1C//e/Lv'
    'v/3+97/9fvIvv5x8ury7O3k4PfmP3/7r3/778Y3Hl3//7ff//Nv/PL7+5eTD1e30+FfuxR8+//XXy49XP19en5yevLvZnJyuxdt3'
    'H6bp0+wPd9P0/vHtzYfp8v7k9MfF2z9P1zcfT05X249/ur15//nd/e4bbx4e/nG6N5+rd3/+/Gn3pNVsbr+cbKa7+6exfry5vf/w'
    '9Gr71uLFviDupuvr3VNX5lO3H5g/dfvXuVCurt//+ij8+8/P0uPGoQpBDOf5J7Qh7MRiPzInA/DQ56+cjZ/58tdno9ktubL4y7fm'
    'z16u9fXlu2kryb1HyLlpDxWvwMP+ON8f+8J9HsY/deqfv/X4/4/32z2jvxN58rvLpQAXY3kU1eX9dLt49fLQ3acWw0CSXZxF20HM'
    'Rz5d3hlPD/3y7gelmLaP2L64u/nsiEs+QVH07Yi3P9wrrqVOtEtNqIAcv/LMLy9yC78bL1qxitDk8TM7DErSetYaZplP559OyAsp'
    'm9ycPYJbHoQDJEjom3wHXCMZvUPiy5wLz+/Mxrl7x3pU7gGKsLZ/WjwyOYPdeMUPf3kR+F30UWBega+9aCHzWeuiDdyQ6KM319fT'
    'u/tf/zjd3l9dX/3rk9S6p3CI8SyNPPDRl/Ps+9DLQ49sle8fhR7tsxMzW4LTc9udDfibzx84h/5mZKeHvm37CTWbH36bdcqw3sds'
    'hFFiioxBiqnBc+0UknTFeZtInH2xR9sS3tm37hgUAaMhdIl45yR5A1QEHJCRIuKApzlch6X70SXgmQokzM6l+5z08g795IKpHbm6'
    'EvdS7JhtuIQyV88IPczdxoWzL3/iDblK0sdb8N7wnuMeZYkDbODdG5KYf5DbN21KZO7RdFAdC7v/39JXsi7H4kXJ1WDyKcvsW9zW'
    'Ph3lpcR+mHBcnB8cZqaftnmBdnS1cCcZIfYPl7d/id9ZSxNfjdo/DyUdJ1HMyKBMkPW+++1lIiNz9xmB5NKySbXaLlZ64bR4vRtq'
    'L6ygdkaV/FttArw7B31eTdsKls18sXY/uPdufP3kWoEMo2+ZpA65UqJn6yTJ3Cuj0VSOwlTtZHbl5YWyosVftBI3VRPk+VJbv3lS'
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
