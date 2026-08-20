"""Pool route 90629703_p0."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vG9cR/S965kNIybLTN8XexEIUy5DkEmkgBAGaokCRPqR9K/rfq8gUudyZe+bMx11Sqp9MkxR3du7cu/Nx5sxP/zn52y+/'
    '//br7yd/+unk48Xt7cn94uTvv/zzr/96eOPh5W+//P6PX//98Pqnk/eXN8PDp9yLbz79+PPFh8sfLq5OFidvr9cni5V4+/b9MHwc'
    'fXA7DO8e3l6/Hy7uThavJ2//MFxdfzhZLLdf/3hz/e7T27vdX7y6v//vYu9+Lt9+/+nj7krL0b39dLIebu8eZf1wfXP3/vHV9q3J'
    'i31F3A5XV7urLptX3X5hfNXtp2OlXF69+/lB+XefNtrj5FCVIMTZ/IQmwk4t7UvGdAAuuvmT0/53Pv31kTS7JVcWf/rW+NrTtb66'
    'eDtsNbl3CXlv2kXFK3Cxb8f7Y1+5GzH+sKk/fuvh/x/utntGf8dz5bcXUwVOZHlQ1cXdcDN59XTR3bcmYiDNTs6irRBjyYeL28bV'
    'Xb+8+0Gppu0lti9urz8Z6pJXUAx9K/H2h2vVNbWJcq0JE5DyK9f8/CK28Dt50YpllCaPn9FhkNLWxmqYZV6Mvx3QFzI2uTlrFDc9'
    'CDtokLA3+Q54jETsDqkvci5s3hnJuXundanYBRRlbT+aXDJ4Bzt5xQ9/fuH4XfRV4F6BP3uyQua7rQet4wmJvnp9dTW8vfv52+Hm'
    '7vLq8i+PWqu+hTnkmTp54KtP59kX0dOie7bKl6/CiHYTxIyWYHHWDmcd8ebmC2cw3vTsdNdft+OEnM8P/5oNyrDd+3yEXmryyCDV'
    'VBC5VipJhuK8TyTOPt+l2xre+bemDIqCkQhVKt4FSZaAioIdOlJU7Ig0u9uwDD+qFDwygYDbOQ2fg1He3FdOuNqeR1fgueQ7Zgse'
    'QpFHTw87jD2NE2df/MTr8igJH2/O54Z1HfMoCxxgHZ+9Lo3ZB3n7SRtSmXk0zWpj7vD/Jf1JNOSYvEiFGkw9ZVp98/vai15Riu+H'
    'icDF+MFubvqiLApsZ1cTz6RGiv39xc2f/c+sqYuvZu03ooTzJIob6dQJ8t53vz0tZESefY1EcmrZpFltFyu8cFq+3ky1J1ZQO6NS'
    '8a12A3w4B2NezdoSns14sXY/uPeuf/3kWoEKo+2ZhA65VKFnGyTJ2itj0VSNomnawerK0wtlRZO/2CrcZF2QzUNt9erRDCy3RHoI'
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
