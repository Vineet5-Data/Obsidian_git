"""Route 90729118 (best of 42 under our layers) + v27 functional stack (v30)."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    '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'
    )
)))


USE_WEED = 1
# Measured OFF: the stationary idle layer lost 0-12-0 (margin -519) to the same
# agent with it disabled.  rayk's +258 on a different host does not transfer to
# this route - the extra output depresses our own premium prices.
USE_IDLE = 1
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
    """Best stationary op for an idle unit, ranked by what the turn is worth.

    CARE banks +1 product on the next production (milk 193 / wool 241); WATER
    adds +1 yield unit in a one-time crop's bonus window.  HARVEST and
    COLLECT_FERTILIZER are deliberately NOT here: they load produce into a unit
    inventory the tape may never DROP, orphaning the goods and desyncing the
    scripted HARVEST that expects to find the tile still loaded.  Measured on
    the four reproduced ladder losses: this ordering +205, the old
    fertilizer-first ordering -3,829.
    """
    if tile.get("animal"):
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


# --------------------------------------------------------------------------
# sell-schedule smoothing
# --------------------------------------------------------------------------
# Settlement is a per-unit lockstep loop: unit k of a SELL is priced against an
# inventory already raised by units 1..k-1, so a bunched sale walks its own
# price down.  Between turns the shops (every 4 steps) and the town centre
# (every 12) drain that inventory back.  Same goods spread over more turns
# therefore realise a higher average price.
#
# So: pull a future sell forward into a spare slot whenever the shed verifiably
# already holds the goods.  Advance, never defer -- this tape spends its cash to
# the bone, so delaying revenue starves the next purchase (measured -35,572),
# while arriving early is free.
#
# CAP is an interior optimum, not a "more is better" knob: cap 5 window 8 gives
# -271 against the mirror where cap 10 window 24 gives -1,920, WORSE than doing
# nothing, because pulling everything forward simply re-bunches it earlier.
#
# The rule reads no price, no base, no amplitude and no opponent -- only the
# pending sell queue and turn occupancy -- so it holds in any regime where price
# decreases in inventory and drain is positive.
# SMOOTH_START is the load-bearing knob, and it is a ROBUSTNESS knob, not a
# performance one.  Smoothing from step 0 scores best at baseline (+3,245 vs
# +3,080) but detonates under a 40% premium haircut: -28,327 against -8,037.
# Advancing a sale moves when cash lands, which changes which Fibonacci-priced
# HIREs clear; with fat revenue that is harmless, with thin revenue it cascades
# through the whole labour schedule.  The cliff is sharp and it is located: step
# 168 is the tape's biggest capital turn (BUY_LAND + 3x HIRE + BUY_ANIMAL COW 2
# + BUY_SEED STRAWBERRY 19).  Smoothing across it can starve BUY_LAND, and the
# farm never gets the plot.  Measured in premium_bear: start 100 -> -28,327,
# start 200 -> -9,778, start 250 -> -7,492.  250 clears the land purchase with
# room, and costs nothing at baseline (+3,252 vs +3,245 ungated) because the
# bisection already showed the value is late anyway -- steps 568-718 carried
# +1,073 of the +1,258, everything earlier carried +154.
USE_SMOOTH = 1
SMOOTH_START = 250
SMOOTH_CAP = 5
SMOOTH_WINDOW = 8
SMOOTH_FLUSH = 16            # last turns: dump everything, unsold goods score 0
_SMOOTH_STATE = {0: {}, 1: {}}


def _tape_sells(step):
    if not 0 <= step < len(_ACTIONS):
        return []
    return [list(o) for o in (_ACTIONS[step].get("market") or [])
            if o and o[0] == "SELL" and len(o) >= 3]


def _smooth_sells(obs, action):
    if not USE_SMOOTH:
        return action
    try:
        seat = _seat(obs)
        step = int(_get(obs, "step", 0) or 0)
        state = _SMOOTH_STATE[seat]
        if step <= 0 or step < state.get("last", -1):
            state.clear()
            state.update({"last": step, "taken": set()})
        state["last"] = step

        orders = [list(o) for o in (action.get("market") or [])]
        sells = [o for o in orders if o and o[0] == "SELL" and len(o) >= 3]
        others = [o for o in orders if not (o and o[0] == "SELL")]

        # a sell already pulled forward must not fire again at its own step
        for key in list(state["taken"]):
            pulled_step, item, quantity = key
            if pulled_step != step:
                continue
            for i, order in enumerate(sells):
                if order[1] == item and int(order[2]) == quantity:
                    sells.pop(i)
                    state["taken"].discard(key)
                    break

        if step < SMOOTH_START:
            return action

        if step >= len(_ACTIONS) - SMOOTH_FLUSH:
            action["market"] = (sells + others)[:10]
            return action

        # the observation's shed predates this turn's DROP, so it is a
        # conservative floor -- we never advance a sale of goods we lack.
        shed = {k: max(0, int(v or 0)) for k, v in
                dict(_get(_get(obs, "private", {}) or {}, "shed", {}) or {}).items()}
        for order in sells:
            shed[order[1]] = shed.get(order[1], 0) - int(order[2])
        free = 10 - len(sells) - len(others)
        slack = SMOOTH_CAP - len(sells)
        for ahead in range(step + 1, step + 1 + SMOOTH_WINDOW):
            if free <= 0 or slack <= 0:
                break
            for order in _tape_sells(ahead):
                key = (ahead, order[1], int(order[2]))
                if key in state["taken"] or shed.get(order[1], 0) < int(order[2]):
                    continue
                sells.append(order)
                shed[order[1]] -= int(order[2])
                state["taken"].add(key)
                free -= 1
                slack -= 1
                if free <= 0 or slack <= 0:
                    break
        action["market"] = (sells + others)[:10]
    except Exception:
        pass
    return action


def agent(obs):
    try:
        step = min(max(0, int(_get(obs, "step", 0) or 0)), len(_ACTIONS) - 1)
        action = _aligned(_ACTIONS[step], obs)
        action = _weed_repair(obs, action, step)
        action = _fix_animal_species(obs, action)
        action = _idle_fill(obs, action)
        action = _impact_slots(obs, action)
        action = _terminal_liquidation(obs, _aligned(action, obs))
        return _smooth_sells(obs, action)
    except Exception:
        return {
            "farmer": ["PASS"],
            "hands": [["PASS"] for _ in (_get(_farm(obs), "hands", []) or [])],
            "market": [],
        }
