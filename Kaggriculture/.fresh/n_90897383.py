"""Route 90729118 (best of 42 under our layers) + v27 functional stack (v30)."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vW9cR/S9acxFSH7a7U+yXWIhiGZJcIjWEIEBTFCjSRdpd0f9exabIxzczZ87M3PtIq16Zpki++31nzpw58/E/J3/7'
    '5ffffv395E8fT95f3t2dPCxO/v7LP//6r8c3Hl/+9svv//j134+vP568vbodHv/Kvfj2w08/X767+vHy+mRx8vpmfbJYibfv'
    '3g7D+9Ef7obhzePb67fD5f3J4sXk7R+H65t3J4vl9uPvb2/efHh9v/vG+cPDfxd7/bl6/cOH97snLUd9+3iyHu7uP7X13c3t'
    '/dtPr7ZvTV7sD8TdcH29e+rSfOr2A+Onbv86HpSr6zc/Pw7+/YfN6HHtUAdBNGfzE1oTdsNiPzI3BuChm6+c9u/59NdHrdlN'
    'uTL507fGz57O9fXl62E7knuPkH3THipegYd9N94f+4O7acYfa+qP33r8/7v77Z7R34k8+fXldAAnbXkcqsv74Xby6umhu09N'
    'moFGdnIWbRsxbvlweWc8PfTLux+Uw7R9xPbF3c0HZ7jkE5SFvm3x9ofbDtd0TTQfNbEEZPuVZ35+kZv4XXvRjFUGTR4/o8Og'
    'NFqbVcNM82L86cR4ocUmN2ebgZsehB1GkFhv8h1wjWTWHRq+zLmweWfUzt071qNyD1AGa/unySOTPdi1V/zw5xeB30UfBeYV'
    '+NrTKmQ+a120gRsSffTm+np4ff/zd8Pt/dX11V8+jVrrLszRnqmRBz76dJ59bXq56ZGt8vWj0KPdODGjKVic2e5swN/cfOAM'
    '+puRnR76tu0n1Gx++G3WKcPrPmYj9BqmSBvkMDXwXFsOknTFeZtInH2xR9sjvLNv3TYoA4ya0GqId06S10BlgANjpAxxwNPs'
    'voal+9FqgEdLIGF2Tt3npJc395MLpnbk6krcS7FjtsEllLl6eqzD3G1cOPvyJ16XqyR9vAXvDe857lGWOMA63r2hEfMPcvum'
    'TQ2ZezTNusbC7v9z+krW5Zi8KLkaTDxlGn2L29qLXl5K7IcJx8X5wW5m+qKZF2ijq4U7yYDY317e/jl+Z01NfBW13zQljZMo'
    'ZmRwTJD1vvvtaSAjc/cZQHJp2uSy2k5WeuI0vN6F2gszqJ1RJf9W6wDvzkGfV1ttBctmPFm7H9x7Nz5/cq5AhNG3TFKHXCnQ'
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
