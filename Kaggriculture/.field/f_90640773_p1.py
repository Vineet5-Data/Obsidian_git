"""Pool route 90640773_p1."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vHMmR/C985oPmgxTlN640tgRzRYGSbuBbEIsFbMPAwfewd2+H++/WijPdPZ2RkZFZ1SNp5bcBOdNdlVVdnRkZGfnT/138'
    '/Zdf//m3Xy/+8NPFu9v37y8eLy/+8ct///V/Pv3h08d//vLrf/3tfz99/uni9ZuH3af/ah9++PiXn2/fvvnx9u7i8uL9693u3cXl'
    '2vzj5f1+8uf3u92rT3/cv97dfri4fD7784+7u/u3F5er9ePj/1+ejPrNyz9/fDe52jD+ny72u/cfPo/n7f3Dh9efPx0mOfnddHhP'
    'Pzid+G+DePdw/+rjyw/j8Mwwfvj45u7Vz5+u/uHjZxtMRjHenA1juPD4vek45rO+u325O0xav5n5J7nDwXaTS8+nCG/hfoncithu'
    'WMFPE3472v/UhAdbPC1ko/2O93nab5/3xO2H3cPpHf/4256cjurw7ZQ5x+uOkzze4OXtwXiHL3Uy3jip4U7Dd+zWD2dg1wTYym6I'
    '2c/4Kp3cQLSe3RCxGY/XS5pv2AkN5qNbbdgJ+labX1e02rgTuhgLP6jzCUdWm7+TRKtN/qSbzdyqk7XAHHyLmH9NHq6CsYBBfBsJ'
    'DySZivnQyUT2g2O0buOe2arbuE8/nP+yh7PEcfCgn7Nx3a3hC6nrGb/pcIA2XWN+tH6pcRTsa65xdKl+F5PZ3bYvTI9xvLy/u9u9'
    '/PDzH3cPH97cvfnP05dX5Yrv7z+2L1P/Yb16uH+37NP0fnf3W+g2GfIYwS2yIcITaNV4va/miWOGL++czL7tdRMQ0yZ3k4oxFFaX'
    'owJx5Dhf6ellRmddv978fDu5HloB42FBk44Ph2Op1WMYoIwDAf6v9eka7m2NOjph1qhdp91k/9gIicMxBxHERsjcmgR0pbXvNW0Q'
    'tnyn8wYnyUITdyOiTveeOwFwusOHp28vd+vvYNb8Ra7EwovZgNz692mCQmj/td657/W/pavN/Nttxr/dqv4td3S3OJumeFZKUuxw'
    'MQV1ZA4UuMX89kKklHJVk7dsM9dJFqnm7c9R0t62QgEQcytn/6vc0hrRzgjkJOFBW3XiyR0LU8y8ydhrvX5DYtMQgu8Bu4n3a4kK'
    'Nx1f2okXWWJABj35AmP46owCEpvfvU3Aoftvo/TKan2VQ/imE4NLXVbOFXp+svP27+JBX3nEsz4e9DRA6+1DUx7XQk70wHRpcqIJ'
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
