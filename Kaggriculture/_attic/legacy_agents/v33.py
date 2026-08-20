"""Route A 90729118 + route B 90635979_p1, opponent-selected at step 200 (v33)."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vG9mR/S965oNJyZK9b4rNxEY0liHJIbIDYTDAJggQJA+TvC32v69GoshWV9WpUx/dpJx5Mk1S7Nv31r1dH+ec+vF/'
    'T/768y//+MsvJ//148nXy9vbk/vFyd9+/uf//OvhjYeX//j5l7//5d8Pr388+fT5Zv3wKffid9/+/NPll88/XF6dLE4+XG9O'
    'Fivx9u2n9frr4IPb9frjw9ubT+vLu5PFxejtH9ZX119OFsvd17/eXH/89uFu/xdv7+//b/Hifj5/+OO3r/srLQf39uPJZn17'
    '9zjWL9c3d58eX+3eGr14ORG366ur/VWX5lV3XxhedffpcFI+X3386WHy775tZ48bhzoJYjjbn9CGsJ8W+5LqtflLbEd1Ov19'
    'jn99MJr9AitLPX4rttZXlx/Wu5l8cVF5t9owxCswzb8f7o+X070dxq829etvPfz/y91uz+jvRK784XI8paOxPEze5d36ZvTq'
    '+aL7b42GAS45Pot2gxiOfH15a1w99Mv7H5TTtLvE7sXt9TdnuuQVFNPfjXj3w73TNbaJ9lkTJiDHr1zz6UVu4ffjRStWmTR5'
    'IA2Oh9Jsba2GWebF8NuJ+ULGJjdnz8SND8IJZpCwN/kO/xCj7A5NX+Zc2L4zGOf+HetSuQsok7X7aHTJ5B3sxyt++OlF4HfR'
    'V4F7Bf7s2QqZ71oP2sATEn31+upq/eHup9+vb+4+X33+78dZ676FOcYzdvvAV5/Ps9+GXh56ZKv89lUY0W6d+8ESLM7scDYQ'
    'b26/cAbjzchOD/21HSfUfH7412yYhu0+5iNMNU2RMchpaohlOydJBue8TyTOvtil7Rne+7fuGJQJRkPomuJ9kBTPfkTmSJni'
    'QKQ5uQ3L8KNrggcmkHA7x+FzMsqb+8oFVzvy6Eo8l2LHbMNDKPPomcIOc0/jwtmXP/EmeZSkj7fgc8O7jnuUJQ6wCZ+9oRnz'
    'D3L7SZuaMvdomtXGwuH/9/Qn2ZBj9KIUajAVlnH1Le5rL6aKUmI/TAQuzg9O5qYv2qJAO7taeCYZKfZPlzd/ij+zxi6+mrXf'
    'DiWdJ1HcyOCcIO99/9vjQkbm2WckkkvLJs1qt1jphdPy9W6qvbCC2hlVim+1G+DDORjzatZW8GyGi7X/wRfvxtdPrhWoMPqe'
    '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'
    )
)))

_ROUTE_A = _ACTIONS


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


# --------------------------------------------------------------------------
# opponent-conditional route selection
# --------------------------------------------------------------------------
# Two routes are exact complements over the opponent panel:
#   route A (this file's main tape, 90729118): 100% vs mirror / Seb / Wufang,
#       but drops 8 familyB, 6 Khanh, 4 Youssef out of 48 each.
#   route B (90635979_p1, below):              100% vs familyB / Khanh /
#       Youssef, but drops 40 mirror, 34 Seb, 17 Wufang.
# Picking correctly wins every matchup, and an oracle switch measured 0 losses
# in 120 games.
#
# Switch latency is free ANYWHERE except across the BUY_LAND turn: oracle
# switches at steps 1, 100 and 240 all scored 100%, while a switch at 169 --
# straddling the step-168 land purchase -- scored 75% with a -73,382 tail.
# Step 240 is used because that is where the opponents finally separate.
#
# Discriminators, all from public state (rival farm is fully observable):
#   animals <= 4                    -> Seb        (route A)
#   animals >= 10                   -> family B   (route B)
#   money delta == 0                -> mirror     (route A; it runs route A, so
#                                                  its cash tracks ours exactly)
#   -34 < money delta               -> Khanh / Youssef (route B)
#   otherwise                       -> Wufang and anything unknown (route A)
#
# Measured at step 200 over 24 seeds x BOTH seats:
#   Khanh/Youssef  -26 .. -25      familyB  -408 .. -157 (10 animals)
#   Wufang        -187 .. -41      mirror   exactly 0
# Separation gap is 15, three times the gap at step 240, and a forced-B switch
# at 200 costs nothing (0/48 Youssef, 0/48 Khanh, 0/48 familyB) where switching
# at 240 cost two Youssef games.
# Unknown opponents fall through to route A, which is 93.8% on its own -- the
# switch only fires on a confident identification.
_ROUTE_B = json.loads(zlib.decompress(base64.b64decode(
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

SWITCH_STEP = 200
_ROUTE_STATE = {0: {}, 1: {}}


def _pick_route(obs):
    """At SWITCH_STEP, swap in route B if the rival is one A loses to."""
    global _ACTIONS
    try:
        seat = _seat(obs)
        step = int(_get(obs, "step", 0) or 0)
        state = _ROUTE_STATE[seat]
        if step <= 0 or step < state.get("last", -1):
            state.clear()
            _ACTIONS = _ROUTE_A
        state["last"] = step
        if step != SWITCH_STEP or state.get("done"):
            return
        state["done"] = True

        farms = _get(obs, "farms", []) or []
        if len(farms) < 2:
            return
        rival, mine = farms[1 - seat], farms[seat]
        animals = 0
        for row in (_get(rival, "tiles", []) or []):
            for tile in (row or []):
                if isinstance(tile, dict) and tile.get("animal"):
                    animals += 1
        delta = int(_get(rival, "money", 0) or 0) - int(_get(mine, "money", 0) or 0)

        if animals <= 4:                     # Seb
            return
        if animals >= 10:                    # family B
            _ACTIONS = _ROUTE_B
            return
        if delta == 0:                       # mirror runs route A itself
            return
        if delta > -34:                      # Khanh / Youssef
            _ACTIONS = _ROUTE_B
    except Exception:
        pass


def agent(obs):
    try:
        _pick_route(obs)
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
