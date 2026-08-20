"""Loss opponent 90711580."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vHMmR/C985gPngxR1b1xpfBLMFQVK8sBeEIsF7IMBw/ewd28H//fTisPuns7IyMis6hG18tuAnOmuyqquzoyMjPzp/87+'
    '65df//m3X8/+46ez9zcfPpw9nJ/9/Zf//uv/fP7D54///OXXf/ztfz9//unszdv73ef/ah9++PTnn2/evf3x5vbs/OzDm93u/dn5'
    '2vzj1d1+8ucPu93rz3/cv9ndfDw7fzH784+727t3Z+er9cPDv86PRv321R8/vZ9cbRj/T2f73YePX8bz7u7+45svnw6TnPxuOrzH'
    'HxxP/LdBvL+/e/3p1cdxeGYYP3x6e/v6589X//jpiw0moxhvzoYxXHj83nQc81nf3rzaHSat38z8k9zhYLvJpedThLdwv0RuRWw3'
    'rODnCb8b7X9swoMtHhey0X5P93ncb1/2xM3H3f3xHf/w256cjurw7ZQ5x+uOk3y6waubg/EOX+pkvHFSw52G79itH87Argmwld0Q'
    's5/xVTq6gWg9uyFiMz5dL2m+YSc0mI9utWEn6Fttfl3RauNO6GIs/KDOJxxZbf5OEq02+ZNuNnOrTtYCc/AtYv41ebgKxgIG8W0k'
    'PJBkKuZDJxPZD47Ruo17Zqtu4z7+cPrLHs4Sx8GDfs7GdbeGL6SuZ/ymwwHadI350fq1xlGwr7nGk0v1u5jM7qZ9YXqM49Xd7e3u'
    '1cef/7C7//j29u1fjl9elSt+uPvUvkz9h/X6/u79sk/Th93tb6HbZMhjBLfIhghPoFXj9Z7NE8cMX945mX3b6yYgpk3uJhVjKKwu'
    'RwXiyHG+0tPLjM66fr35+XZ0PbQCxsOCJh0fDsdSq4cwQBkHAvxf69M13NsadXTCrFG7TrvJ/rEREodjDiKIjZC5NQnoSmvfa9og'
    'bPlO5w1OkoUm7kZEne49dwLgdIcPj99e7tbfwaz5i1yJhRezAbn179MEhdD+ud657/W/pavN/Nttxr/dqv4td3S3OJumeFZKUuxw'
    'MQV1ZA4UuMX89kKklHJVk7dsM9dRFqnm7c9R0t62QgEQcytn/6vc0hrRzgjkJOFBW3XiyR0LU8y8ydhrvX5DYtMQgu8Bu4n3a4kK'
    'Nx1f2okXWWJABj35CmN4dkYBic3v3ibg0P23UXpltZ7lEL7pxOBSl5VzhZ6f7Lz9u3jQlx7xrI8HPQ3QevvQlMe1kBM9MF2anGhC'
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
