"""Route 90635979_p1 (sole route losing nothing on the adversarial seeds) + functional stack (v31)."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vW9cR/S9acxFSsuJ0p9ovsRDFMiS5RGoIQYCmKFCki7S7Iv+9isyPxzczZ87M3PtIu16Zpki++31nzpw58+G/Z3//'
    '+bdff/nt7E8fzt5d3d+fPS7O/vHzv/7276c3nl7++vNv//zlP0+vP5y9ub4bnv7Kvfjz+x9/unp7/cPVzdni7NXt+myxEm/f'
    'vxmGd6M/3A/D66e312+Gq4ezxdeTt38Ybm7fni2Wu4+/u7t9/f7Vw/4bLx4ff18c9Of61ffv3+2ftBz17cPZerh/eG7r29u7'
    'hzfPr3ZvTV4cDsT9cHOzf+rSfOruA+On7v46HpTrm9c/PQ3+w/vN6HHtUAdBNGfzE1oT9sNiPzI3BuChm6+c9+/59NdHrdlP'
    'uTL507fGz57O9c3Vq2E3kgePkH3THipegYd9O94fh4O7acYfa+qP33r6/9uH3Z7R34k8+dXVdAAnbXkaqquH4W7yavvQ/acm'
    'zUAjOzmLdo0Yt3y4ujeeHvrl/Q/KYdo9Yvfi/va9M1zyCcpC37V498Nth2u6JpqPmlgCsv3KMz++yE38vr1oxiqDJo+f0WFQ'
    'Gq3NqmGmeTH+dGK80GKTm7PNwE0Pwg4jSKw3+Q64RjLrDg1f5lzYvDNq5/4d61G5ByiDtfvT5JHJHuzbK37444vA76KPAvMK'
    'fG27CpnPWhdt4IZEH729uRlePfz07XD3cH1z/dfnUWvdhTnaMzXywEe359mXppebHtkqXz4KPdqNEzOagsWF7c4G/M3NBy6g'
    'vxnZ6aFv235CzeaH32adMrzuYzZCr2GKtEEOUwPPteUgSVect4nE2Rd7tD3Ce/vWbYMywKgJrYZ47yR5DVQGODBGyhAHPM3u'
    'a1i6H60GeLQEEmbn1H1OenlzP7lgakeursS9FDtmG1xCmaunxzrM3caFsy9/4nW5StLHW/De8J7jHmWJA6zj3RsaMf8gt2/a'
    '1JC5R9Osayzs/n9OX8m6HJMXJVeDiadMo29xW3vRy0uJ/TDhuDg/2M1MXzTzAm10tXAnGRD7m6u7v8TvrKmJr6L2m6akcRLF'
    'jAyOCbLe9789DWRk7j4DSC5Nm1xWu8lKT5yG17tQe2EGtTOq5N9qHeDdOejzaqutYNmMJ2v/gwfvxudPzhWIMPqWSeqQKwV6'
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
