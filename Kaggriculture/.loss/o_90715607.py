"""Loss opponent 90715607."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vHEly/C985gPngxTpN640ZwnHFQVKusF5QSwW8BkGjPPD2m/G/XdrRU53T2dkZGRW9Sy1urcBOdNdlVVdnRkZGfnT/539'
    'xy+//v1vv579y09nH24/fjx7PD/7z1/++9//58sfvnz8+y+//tff/vfL55/O3r572H35r/bhh89//fn2/bsfb+/Ozs8+vt3tPpyd'
    'r80/Xt/vJ3/+uNu9+fLH/dvd7aez81ezP/+4u7t/f3a+Wj8+/uP8aNTvXv/584fJ1Ybx/3S233389HU87+8fPr39+ul5kpPfTYf3'
    '9IPjif82iA8P928+v/40Ds8M44fP7+7e/Pzl6p8+f7XBZBTjzdkwhguP35uOYz7ru9vXu+dJ6zcz/yR3eLbd5NLzKcJbuF8ityK2'
    'G1bwy4Tfj/Y/NuGzLZ4WstF+h/s87beve+L20+7h+I5/+m1PTkf1/O2UOcfrjpM83OD17bPxnr/UyXjjpIY7Dd+xWz+cgV0TYCu7'
    'IWY/46t0dAPRenZDxGY8XC9pvmEnNJiPbrVhJ+hbbX5d0WrjTuhiLPygziccWW3+ThKtNvmTbjZzq07WAnPwLWL+NXm4CsYCBvFt'
    'JDyQZCrmQycT2Q+O0bqNe2arbuM+/nD6yz6fJY6DB/2cjetuDV9IXc/4Tc8HaNM15kfr7zWOgn3NNQ4u1R9iMrvb9oXpMY7X93d3'
    'u9effv7T7uHTu7t3/3b88qpc8eP95/Zl6j+sNw/3H5Z9mj7u7n4L3SZDHiO4RTZEeAKtGq/3Yp44Zvjyzsns2143ATFtcjepGENh'
    'dTkqEEeO85WeXmZ01vXrzc+3o+uhFTAeFjTp+HA4llo9hgHKOBDg/1qfruHe1qijE2aN2nXaTfaPjZA4HHMQQWyEzK1JQFda+17T'
    'BmHLdzpvcJIsNHE3Iup077kTAKc7fHj69nK3/g5mzV/kSiy8mA3Irf+YJiiE9i/1zn2v/y1dbebfbjP+7Vb1b7mju8XZNMWzUpJi'
    'zxdTUEfmQIFbzG8vREopVzV5yzZzHWWRat7+HCXtbSsUADG3cva/yi2tEe2MQE4SHrRVJ57csTDFzJuMvdbrNyQ2DSH4HrCbeL+W'
    'qHDT8aWdeJElBmTQk99hDC/OKCCx+d3bBBy6/zRKr6zWixzCN50YXOqycq7Q85Odt38XD/rSI5718aCnAVpvH5ryuBZyogemS5MT'
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
