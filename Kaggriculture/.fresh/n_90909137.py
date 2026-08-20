"""Route 90729118 (best of 42 under our layers) + v27 functional stack (v30)."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vHMmR/C985oPmgxR1b1xpfBLMFQVK8sBeEIsF7IMBw/ewd28H//fTijPdPZ2RkZFZ1SNp5bcBOdNdlVVdnRkZGfnT'
    '/1381y+//vNvv178x08X727fv794vLz4+y///df/+fSHTx//+cuv//jb/376/NPF6zcPu0//1T788PHPP9++ffPj7d3F5cX7'
    '17vdu4vLtfnHy/v95M/vd7tXn/64f727/XBx+Xz25x93d/dvLy5X68fHf12ejPrNyz9+fDe52jD+ny72u/cfPo/n7f3Dh9ef'
    'Px0mOfnddHhPPzid+G+DePdw/+rjyw/j8Mwwfvj45u7Vz5+u/uHjZxtMRjHenA1juPD4vek45rO+u325O0xav5n5J7nDwXaT'
    'S8+nCG/hfoncithuWMFPE3472v/UhAdbPC1ko/2O93nab5/3xO2H3cPpHf/w256cjurw7ZQ5x+uOkzze4OXtwXiHL3Uy3jip'
    '4U7Dd+zWD2dg1wTYym6I2c/4Kp3cQLSe3RCxGY/XS5pv2AkN5qNbbdgJ+labX1e02rgTuhgLP6jzCUdWm7+TRKtN/qSbzdyq'
    'k7XAHHyLmH9NHq6CsYBBfBsJDySZivnQyUT2g2O0buOe2arbuE8/nP+yh7PEcfCgn7Nx3a3hC6nrGb/pcIA2XWN+tH6pcRTs'
    'a65xdKl+F5PZ3bYvTI9xvLy/u9u9/PDzH3YPH97cvfnL6curcsX39x/bl6n/sF493L9b9ml6v7v7LXSbDHmM4BbZEOEJtGq8'
    '3lfzxDHDl3dOZt/2ugmIaZO7ScUYCqvLUYE4cpyv9PQyo7OuX29+vp1cD62A8bCgSceHw7HU6jEMUMaBAP/X+nQN97ZGHZ0w'
    'a9Su026yf2yExOGYgwhiI2RuTQK60tr3mjYIW77TeYOTZKGJuxFRp3vPnQA43eHD07eXu/V3MGv+Ildi4cVsQG79+zRBIbT/'
    'Wu/c9/rf0tVm/u02499uVf+WO7pbnE1TPCslKXa4mII6MgcK3GJ+eyFSSrmqyVu2meski1Tz9ucoaW9boQCIuZWz/1VuaY1o'
    'ZwRykvCgrTrx5I6FKWbeZOy1Xr8hsWkIwfeA3cT7tUSFm44v7cSLLDEgg558gTF8dUYBic3v3ibg0P23UXpltb7KIXzTicGl'
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
