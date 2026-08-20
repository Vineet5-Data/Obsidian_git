"""Pool route 90630455_p1."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vHMmR/C985oPmgxR1b1xpbBHmigIleWAviMUC9uGAg+9h7bfD/ffTipzuns7IyMis6hG18ttgyOmuyqquzoyMjPzpf8/+'
    '85df//H3X8/+46ez99cfPpw9nJ/91y//87d/fv7i88d//PLrf//9X58//3T29uZ+9/mv2ocfPv3l5+t3Nz9e356dn314u9u9Pztf'
    'mz+8vttPvv6w2735/OX+7e7649n5y9nXP+5u796dna/WDw//d3406pvXf/r0fnK1Yfw/ne13Hz5+Gc+7u/uPb798eprk5HfT4T3+'
    '4Hjivw3i/f3dm0+vP47DM8P44dPN7ZufP1/946cvNpiMYrw5G8Zw4fH/puOYz/r2+vXuadL6zcwfyR2ebDe59HyK8BbuP5FbEdsN'
    'K/h5wu9G+x+b8MkWjwvZaL/DfR7325c9cf1xd398xz/8tieno3r675Q5x+uOkzzc4PX1k/Ge/qmT8cZJDXca/sdu/XAGdk2AreyG'
    'mP2Mr9LRDUTr2Q0Rm/FwvaT5hp3QYD661YadoG+1+XVFq407oYux8IM6n3Bktfk7SbTa5CvdbOZWnawF5uBbxPxp8nAVjAUM4ttI'
    'eCDJVMyHTiayHxyjdRv3zFbdxn384fSXfTpLHAcP+jkb190a/iF1PeM3PR2gTdeYH61faxwF+5prHFyq38VkdtftC9NjHK/vbm93'
    'rz/+/Ifd/ceb25u/Hr+8Klf8cPepfZn6D+vN/d37ZZ+mD7vb30K3yZDHCG6RDRGeQKvG6z2bJ44ZvrxzMvu2101ATJvcTSrGUFhd'
    'jgrEkeN8paeXGZ11/Xrz8+3oemgFjIcFTTo+HI6lVg9hgDIOBPi/1qdruLc16uiEWaN2nXaT/WMjJA7HHEQQGyFzaxLQlda+17RB'
    '2PKdzhucJAtN3I2IOt177gTA6Q4fHv97uVt/B7PmL3IlFl7MBuTWv08TFEL753rnvtf/lq4282+3Gf92q/q33NHd4mya4lkpSbGn'
    'iymoI3OgwC3mtxcipZSrmrxlm7mOskg1b3+Okva2FQqAmFs5+1vlltaIdkYgJwkP2qoTT+5YmGLmTcZe6/UbEpuGEHwP2E28X0tU'
    'uOn40k68yBIDMujJVxjDszMKSGx+9zYBh+6/jdIrq/Ush/BNJwaXuqycK/T8ZOft38WDvvCIZ3086GmA1tuHpjyuhZzogenS5EQT'
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
