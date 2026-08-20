"""Pool route 90630455_p0."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vW9kN/S9eaxFJjpN05yavE6OeOLCdCu3AGAzQFgWKdjHtruh/r+vI0tMjeXhI3vukeGYVRZb0eHm/+HF4+MN/zv7608//'
    '+MvPZ7/54ezz5d3d2cPi7G8//fPP/3p84/HlP376+e9/+ffj6x/OPl7dDo9/5V789ssff7z8dPX95fXZ4uz9zeZssRJv330chs+j'
    'P9wNw4fHtzcfh8v7s8WbydvfD9c3n84Wy93HP9/efPjy/n7/jdcPD/9dHIzn6v3vv3zeP2k5GtsPZ5vh7v5J1k83t/cfn17t3pq8'
    'OFTE3XB9vX/q0nzq7gPjp+7+OlbK1fWHHx+Vf/9lqz1ODlUJQpztT2gi7NViPzKnA/DQ7VfW/Uc+/fWRNPspVyZ/+tb42dO5vr58'
    'P+w0efAIOTbtoeIVeNjvxvvjULlbMf6/pv7/W4///3S/2zP6O5Env7+cKnAiy6OqLu+H28mr54fuPzURA2l2chbthBhLPlzeGU8P'
    '/fL+B6Wado/Yvbi7+eKoSz5BWeg7iXc/3FZd0zXRXGtiCUj5lWd+fZGb+L28aMYqSpPHz+gwKGlru2qYaV6MP53QF1pscnO2Udz0'
    'IOygQWK9yXfANZJZd0h9mXNh+85Izv071qNyD1CUtfvT5JHJEezlFT/89UXgd9FHgXkFvva8CpnPWhdt4IZEH725vh7e3//4u+H2'
    '/ur66k9PWms9hDnkmRp54KPP59mvopdFj2yVXz8KPdqtEzOagsW57c4G/M3tB86hvxnZ6aFv235CzeaH32adMrzuYzZCLzVFZJBq'
    'auC5tlSSdMV5m0icfbFH2xre27euDIqCkQitVLx3kjwBFQUHdKSoOOBpdl/D0v1opeDREkiYnVP3Oenlzf3kgqkduboS91LsmG1w'
    'CWWunh7rMHcbF86+/InX5SpJH2/Be8N7jnuUJQ6wjndvSGP+QW7ftCmVuUfTrGss7P6/pK9kXY7Ji5KrweRTptm3uK296OWlxH6Y'
    'cFycH+xmpi+aeYF2dLVwJxkh9o+Xt3+I31lTE1+N2m9FScdJFDMyqBNkve9/e5rIyNx9RiC5NG1yWe0mKz1xWrzeDbUXZlA7o0r+'
    'rTYA3p2DPq+22gqWzXiy9j948G58/uRcgQyjb5mkDrlSomfnJMncK7OiqRyFubST2ZXnF8qMFn/RStxUTZDtpbZ6/bQMPLNEWgjL'
    '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'
    'M2/RUw=='
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
