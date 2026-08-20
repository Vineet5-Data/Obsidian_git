"""Pool route 90635229_p0."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vHEly/C985gPngxTlN640dxKOKwoU5cF5QSwWuDMMGOeHtd8M/3drxWF3T2dkZGRW9Sy1urcBOdNdlVVdnRkZGfnT/579'
    '+y+//uPvv579y09nH28+fTp7PD/7j1/+62///eUPXz7+45df//Pv//Pl809n797f7778V/vww+e//nzz4f2PN7dn52ef3u12H8/O'
    '1+Yfb+72kz9/2u3efvnj/t3u5uHs/NXszz/ubu8+nJ2v1o+P/3d+NOr3b/7y+ePkasP4fzrb7z49fB3Ph7v7h3dfPx0mOfnddHhP'
    'Pzie+G+D+Hh/9/bzm4dxeGYYP3x+f/v25y9Xf/j81QaTUYw3Z8MYLjx+bzqO+axvb97sDpPWb2b+Se5wsN3k0vMpwlu4XyK3IrYb'
    'VvDLhD+M9j824cEWTwvZaL/n+zztt6974uZhd398xz/9tienozp8O2XO8brjJJ9v8ObmYLzDlzoZb5zUcKfhO3brhzOwawJsZTfE'
    '7Gd8lY5uIFrPbojYjM/XS5pv2AkN5qNbbdgJ+labX1e02rgTuhgLP6jzCUdWm7+TRKtN/qSbzdyqk7XAHHyLmH9NHq6CsYBBfBsJ'
    'DySZivnQyUT2g2O0buOe2arbuI8/nP6yh7PEcfCgn7Nx3a3hC6nrGb/pcIA2XWN+tP5e4yjY11zj2aX6Q0xmd9O+MD3G8ebu9nb3'
    '5uHnP+3uH97fvv+345dX5Yqf7j63L1P/Yb29v/u47NP0aXf7W+g2GfIYwS2yIcITaNV4vRfzxDHDl3dOZt/2ugmIaZO7ScUYCqvL'
    'UYE4cpyv9PQyo7OuX29+vh1dD62A8bCgSceHw7HU6jEMUMaBAP/X+nQN97ZGHZ0wa9Su026yf2yExOGYgwhiI2RuTQK60tr3mjYI'
    'W77TeYOTZKGJuxFRp3vPnQA43eHD07eXu/V3MGv+Ildi4cVsQG79xzRBIbR/qXfue/1v6Woz/3ab8W+3qn/LHd0tzqYpnpWSFDtc'
    'TEEdmQMFbjG/vRAppVzV5C3bzHWURap5+3OUtLetUADE3MrZ/yq3tEa0MwI5SXjQVp14csfCFDNvMvZar9+Q2DSE4HvAbuL9WqLC'
    'TceXduJFlhiQQU9+hzG8OKOAxOZ3bxNw6P7TKL2yWi9yCN90YnCpy8q5Qs9Pdt7+XTzoS4941seDngZovX1oyuNayIkemC5NTjSh'
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
