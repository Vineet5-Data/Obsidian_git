"""Route 90729118 (best of 42 under our layers) + v27 functional stack (v30)."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vHMmR/C985oPmgxR1b1xpfBLMFQWK8sBeEIsF7IMBw/ewd28H//fTipzuns7IyMis6hG18tuAnOmuyqquzoyMjPzp'
    '/87+65df//m3X8/+46ezD9cfP549nJ/9/Zf//uv/fP7D54///OXXf/ztfz9//uns7bu73ef/ah9++PTnn6/fv/vx+ubs/Ozj'
    '293uw9n52vzj9e1+8uePu92bz3/cv91d35+dv5z9+cfdze37s/PV+uHhX+dHo373+o+fPkyuNoz/p7P97uP9l/G8v727f/vl'
    '09MkJ7+bDu/xB8cT/20QH+5u33x6fT8Ozwzjh0/vbt78/Pnq95++2GAyivHmbBjDhcfvTccxn/XN9evd06T1m5l/kjs82W5y'
    '6fkU4S3cL5FbEdsNK/h5wu9H+x+b8MkWjwvZaL/DfR7325c9cX2/uzu+4x9+25PTUT19O2XO8brjJA83eH39ZLynL3Uy3jip'
    '4U7Dd+zWD2dg1wTYym6I2c/4Kh3dQLSe3RCxGQ/XS5pv2AkN5qNbbdgJ+labX1e02rgTuhgLP6jzCUdWm7+TRKtN/qSbzdyq'
    'k7XAHHyLmH9NHq6CsYBBfBsJDySZivnQyUT2g2O0buOe2arbuI8/nP6yT2eJ4+BBP2fjulvDF1LXM37T0wHadI350fq1xlGw'
    'r7nGwaX6XUxmd92+MD3G8fr25mb3+v7nP+zu7t/dvPvL8curcsWPt5/al6n/sN7c3X5Y9mn6uLv5LXSbDHmM4BbZEOEJtGq8'
    '3rN54pjhyzsns2973QTEtMndpGIMhdXlqEAcOc5XenqZ0VnXrzc/346uh1bAeFjQpOPD4Vhq9RAGKONAgP9rfbqGe1ujjk6Y'
    'NWrXaTfZPzZC4nDMQQSxETK3JgFdae17TRuELd/pvMFJstDE3Yio073nTgCc7vDh8dvL3fo7mDV/kSux8GI2ILf+fZqgENo/'
    '1zv3vf63dLWZf7vN+Ldb1b/lju4WZ9MUz0pJij1dTEEdmQMFbjG/vRAppVzV5C3bzHWURap5+3OUtLetUADE3MrZ/yq3tEa0'
    'MwI5SXjQVp14csfCFDNvMvZar9+Q2DSE4HvAbuL9WqLCTceXduJFlhiQQU++whienVFAYvO7twk4dP9tlF5ZrWc5hG86MbjU'
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
