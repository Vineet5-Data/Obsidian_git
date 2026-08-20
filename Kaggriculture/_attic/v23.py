"""Route agent distilled from episode 90503598 (Seb, $148,637 in contested play).

That route buys all four quadrants and 19 animals and skips the wheat
round-trip the previous clone spent $31,968 on.  Runtime hand alignment keeps
it legal when stochastic state changes alter accepted hires; the idle-unit
layer and terminal liquidation are carried over unchanged.
"""

import base64
import copy
import json
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtnVtvXFluhf+LnvXQqpLcdt7Udg1sjNo2fElh0hAaDWQGAwSTh07egvz3uC2pLofkx0XuXZIH8ZMLJVmH+3L2JhcXF3/5n7O/'
    '/fb7P/76+9m//HL20+c3N69+fX/98dPnD5uz2/Ozv//2n//+X19+8uXjP377/T/++t9fPv9y9vrN1592P/z0+S+/ftxsXp2dn/28'
    'uXn39ux8vfh6+3pz/ens/GL18P312zc/X998+cnLd9uz89Xt7f+eH9r9/s3LP39+v//x3vBfzrabj5++Pvbtuw+fXn/99GWAHxdf'
    'hb91PHJrozXx4+vN5r1j5KsP796fHZm2f5Zj23ItXGutjdHM7KySDfCm5Ob67afd2DUDbq5fbnbPP3r6w1+72wSdabj+tPmgmfHw'
    'nw43xv5/G0Noh8Dk3+2E9x/evfr88tPBPr7VJ+Xju8/B6NzJcEyvr9HDM10zaGfsTaSlkGcF3uLdzw5fu2io094eZ9f86Y+3P1ge'
    'fFGEZVEn6n4A7ou8GJz7ZG3Zgj37x+IEM2IeffCgiW+Psyovrxfvg7MlHBMmrkk4PfhCK/uksEbOi7x8cdbpSu0+5VdhPi2ORbRX'
    'd9/sZ61xnm2ul+9HuuTuj+Klg4ffb0XxyNh/RSfW1HfFOdB3H/YjHloAe0Dt5oCeeb9uc24Tuw77Q8LYsHuyc8Me/zKdkHe/6b77'
    '9pHpk+Y/Mv1QetJuziY/yB5YpwtDjuMKs4fud+0po4nWK3zsKV18/fuug/Rg2st3Nzebl59+/dPmw6c3N2/+7f7t2r0RZGfB+XAm'
    'Zb8fAxsKj4blsOfLfbh18AFdj4+bmz/2wYFx+9DOrNFKWKPd0+DYcWapMQnHrod4BCysmnPC2sknC/z9MGCP9wc961yfaM7qeB6Y'
    'Ex7Ez1qcqs1HOVGA+bBYo/R1MPNt3azS8/UrwSInu/8LfoXyoGCg57LXb27F6AWbfv2Gu/N0T2rc+N/4g5RzasqDTu2MfX/Q/9sH'
    'Gd9jnpdc8ERdeKHkJJPPeR8PegElwQnez4yfPD2sjgFq36S7m6IJQ0poisF0WqijXYTdHecAfTkI2AwynFHR7N7N1KQBWwxRhMfr'
    'A3ZQI5rbvR3ygFe3k2bdmYx0TzuT68Ft2vR6nn8TNeHEx+6JOw/l7sPwwzxs2HhDjWct/q8YewzPZxDbKUbszpT7ySk9d+fPKd53'
    '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'
    '+3+e7u7U'
    )
)))


def _get(value, key, default=None):
    if isinstance(value, dict):
        return value.get(key, default)
    getter = getattr(value, "get", None)
    if callable(getter):
        return getter(key, default)
    return getattr(value, key, default)


def _aligned(action, obs):
    action = copy.deepcopy(action or {})
    farms = list(_get(obs, "farms", []) or [])
    seat = 1 if int(_get(obs, "player", 0) or 0) == 1 else 0
    farm = farms[seat] if seat < len(farms) else {}
    expected = len(_get(farm, "hands", []) or [])
    hands = [list(order or ["PASS"]) for order in (action.get("hands") or [])]
    if len(hands) < expected:
        hands.extend([["PASS"] for _ in range(expected - len(hands))])
    return {
        "farmer": list(action.get("farmer") or ["PASS"]),
        "hands": hands[:expected],
        "market": [list(order) for order in (action.get("market") or [])][:10],
    }


ANIMAL_SWITCH_DAY = 999
MAX_ONE_ANIMAL = 10
_RUNTIME = {"raw_opponent": False}
ANIMAL_COST = {"COW": 400, "SHEEP": 500}
# Cared season output per animal, measured in-engine.
ANIMAL_YIELD = {"COW": 39, "SHEEP": 38}
COW_BIAS = 1.0
SEED_COST = {"WHEAT": 10, "CARROT": 20, "TOMATO": 50, "STRAWBERRY": 100, "MELON": 80}
PRODUCT_COST = {"WHEAT": 25, "FERTILIZER": 100}
SELLABLE_PRODUCTS = {
    "WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON",
    "EGG", "MILK", "WOOL", "FERTILIZER",
}


def _farm_private(obs):
    farms = list(_get(obs, "farms", []) or [])
    seat = 1 if int(_get(obs, "player", 0) or 0) == 1 else 0
    return (farms[seat] if seat < len(farms) else {}), (_get(obs, "private", {}) or {})


def _animal_counts(farm, private):
    counts = _placed_animal_counts(farm)
    shed = _get(private, "shed", {}) or {}
    inventories = list(_get(private, "inventories", []) or [])
    for animal in counts:
        counts[animal] += max(0, int(shed.get(animal, 0) or 0))
        counts[animal] += sum(max(0, int((inventory or {}).get(animal, 0) or 0)) for inventory in inventories)
    return counts


def _placed_animal_counts(farm):
    counts = {"COW": 0, "SHEEP": 0}
    for row in (_get(farm, "tiles", []) or []):
        for tile in row or []:
            if isinstance(tile, dict) and tile.get("animal") in counts:
                counts[tile["animal"]] += 1
    return counts


def _hire_cost(index):
    a, b = 1, 1
    for _ in range(max(0, int(index))):
        a, b = b, a + b
    return a


def _projected_raw_balance(obs, action, farm, private):
    balance = int(_get(farm, "money", 0) or 0)
    prices = _get(_get(obs, "market", {}) or {}, "prices", {}) or {}
    available = dict(_get(private, "shed", {}) or {})
    hires = int(_get(farm, "hires_today", 0) or 0)
    unlocked = len(_get(farm, "unlocked_quadrants", []) or [])
    land_costs = (1000, 2000, 4000)
    for order in (action.get("market", []) or []):
        if not order:
            continue
        op = order[0]
        if op == "SELL" and len(order) >= 3:
            item = order[1]
            quantity = min(max(0, int(order[2] or 0)), max(0, int(available.get(item, 0) or 0)))
            balance += quantity * max(1, int(prices.get(item, 1) or 1))
            available[item] = max(0, int(available.get(item, 0) or 0) - quantity)
        elif op == "HIRE":
            balance -= _hire_cost(hires)
            hires += 1
        elif op == "BUY_SEED" and len(order) >= 3:
            balance -= SEED_COST.get(order[1], 0) * max(0, int(order[2] or 0))
        elif op == "BUY_PRODUCT" and len(order) >= 3:
            balance -= PRODUCT_COST.get(order[1], 0) * max(0, int(order[2] or 0))
        elif op == "BUY_ANIMAL" and len(order) >= 3:
            balance -= ANIMAL_COST.get(order[1], 0) * max(0, int(order[2] or 0))
        elif op == "BUY_LAND" and unlocked > 0:
            index = min(max(0, unlocked - 1), len(land_costs) - 1)
            balance -= land_costs[index]
            unlocked += 1
    return balance


def _recorded_animal_counts_before(step):
    counts = {"COW": 0, "SHEEP": 0}
    for recorded in _ACTIONS[: max(0, int(step))]:
        for order in (recorded.get("market", []) or []):
            if len(order) >= 3 and order[0] == "BUY_ANIMAL" and order[1] in counts:
                counts[order[1]] += max(0, int(order[2] or 0))
    return counts


def _detect_recorded_opponent(obs, farm):
    farms = list(_get(obs, "farms", []) or [])
    seat = 1 if int(_get(obs, "player", 0) or 0) == 1 else 0
    if len(farms) < 2:
        return False
    ours = _placed_animal_counts(farm)
    opponent = _placed_animal_counts(farms[1 - seat])
    expected = _recorded_animal_counts_before(_get(obs, "step", 0))
    return ours != opponent and opponent == expected


def _preferred_animal(obs, counts):
    prices = _get(_get(obs, "market", {}) or {}, "prices", {}) or {}
    cow_value = 1.5 * max(1, int(prices.get("MILK", 160) or 160))
    sheep_value = (4.0 / 3.0) * max(1, int(prices.get("WOOL", 200) or 200))
    if counts["COW"] >= int(MAX_ONE_ANIMAL):
        return "SHEEP"
    if counts["SHEEP"] >= int(MAX_ONE_ANIMAL):
        return "COW"
    return "COW" if cow_value >= sheep_value else "SHEEP"


def _adapt_animals(obs, action):
    action = _aligned(action, obs)
    farm, private = _farm_private(obs)
    counts = _animal_counts(farm, private)
    day = int(_get(obs, "day", 0) or 0)
    shed = _get(private, "shed", {}) or {}
    inventories = list(_get(private, "inventories", []) or [])

    if day >= int(ANIMAL_SWITCH_DAY) + 2 and _detect_recorded_opponent(obs, farm):
        _RUNTIME["raw_opponent"] = True

    # Follow the price signal while the opponent does too.  If a fixed replay
    # route is detected, retain the recorded purchases; buying extra animals
    # to catch up was tested and amplified the opponent's scarcity rents.
    if not _RUNTIME["raw_opponent"] and day >= int(ANIMAL_SWITCH_DAY):
        market = []
        planned = dict(counts)
        extra_budget = max(0, _projected_raw_balance(obs, action, farm, private))
        for raw in action.get("market", []) or []:
            order = list(raw)
            if len(order) >= 3 and order[0] == "BUY_ANIMAL" and order[1] in planned:
                recorded_animal = order[1]
                animal = _preferred_animal(obs, planned)
                quantity = max(0, int(order[2] or 0))
                if planned[animal] + quantity > int(MAX_ONE_ANIMAL):
                    animal = "SHEEP" if animal == "COW" else "COW"
                extra_cost = (ANIMAL_COST[animal] - ANIMAL_COST[recorded_animal]) * quantity
                if extra_cost > extra_budget:
                    # Cannot afford the upgrade: keep the recorded species.
                    # Skipping the order outright loses the animal for the whole
                    # season (11 placed vs the winner's 15 in episode 90487461).
                    animal = recorded_animal
                    extra_cost = 0
                    if planned[animal] + quantity > int(MAX_ONE_ANIMAL):
                        market.append(order)
                        continue
                extra_budget -= extra_cost
                order[1] = animal
                planned[animal] += quantity
            market.append(order)
        action["market"] = market[:10]

    unit_actions = [action.get("farmer", ["PASS"]), *list(action.get("hands") or [])]
    for index, unit_action in enumerate(unit_actions):
        if not unit_action or len(unit_action) < 2 or unit_action[1] not in counts:
            continue
        raw_animal = unit_action[1]
        other = "SHEEP" if raw_animal == "COW" else "COW"
        if unit_action[0] == "PICKUP":
            if int(shed.get(raw_animal, 0) or 0) <= 0 and int(shed.get(other, 0) or 0) > 0:
                unit_action[1] = other
        elif unit_action[0] == "PLACE":
            inventory = dict(inventories[index] or {}) if index < len(inventories) else {}
            if int(inventory.get(raw_animal, 0) or 0) <= 0 and int(inventory.get(other, 0) or 0) > 0:
                unit_action[1] = other
    action["farmer"] = unit_actions[0]
    action["hands"] = unit_actions[1:]
    return _aligned(action, obs)


IDLE_WORK = 1
IDLE_MARGIN = 1
_DIRS = (("NORTH", 0, -1), ("SOUTH", 0, 1), ("EAST", 1, 0), ("WEST", -1, 0))


def _unit_busy_steps():
    """Steps at which the recorded route gives each unit a real order.

    Index 0 is the farmer, index n the n-th hand.  Idle work must always hand a
    unit back on its home tile before the next of these steps, or every later
    recorded order for that unit addresses the wrong tile.
    """
    busy = {}
    for step, recorded in enumerate(_ACTIONS):
        units = [recorded.get("farmer") or ["PASS"]]
        units.extend(list(recorded.get("hands") or []))
        for index, order in enumerate(units):
            if order and order[0] != "PASS":
                busy.setdefault(index, []).append(step)
    return busy


_BUSY = _unit_busy_steps()
_IDLE_HOME = {}


def _next_busy(index, step):
    for candidate in _BUSY.get(index, ()):  # short per-unit lists
        if candidate > step:
            return candidate
    return len(_ACTIONS)


def _passable(farm, x, y):
    rows = _get(farm, "tiles", []) or []
    if not (0 <= y < len(rows)):
        return False
    row = rows[y] or []
    if not (0 <= x < len(row)):
        return False
    return row[x] != "LOCKED"


def _step_toward(farm, position, target):
    px, py = position
    tx, ty = target
    options = []
    for name, dx, dy in _DIRS:
        nx, ny = px + dx, py + dy
        gain = (abs(px - tx) + abs(py - ty)) - (abs(nx - tx) + abs(ny - ty))
        if gain > 0 and _passable(farm, nx, ny):
            options.append((gain, name))
    if not options:
        return None
    options.sort(reverse=True)
    return [options[0][1]]


# Watering is rationed by crop value, not by proximity: strawberry runs 45%
# dry across the season (314 crop-days) and is worth five wheat.
CROP_VALUE = {"MELON": 250, "STRAWBERRY": 120, "TOMATO": 60, "CARROT": 35, "WHEAT": 25}
CARE_VALUE = 300
IDLE_DIST_PENALTY = 20


def _idle_targets(farm):
    """Every job an idle unit could usefully do, with its value."""
    jobs = []
    rows = _get(farm, "tiles", []) or []
    for y, row in enumerate(rows):
        for x, tile in enumerate(row or []):
            if not isinstance(tile, dict):
                continue
            kind = tile.get("kind")
            if kind == "PLANT" and tile.get("crop") and not tile.get("watered_today"):
                jobs.append((x, y, "WATER", CROP_VALUE.get(tile["crop"], 25)))
            elif kind == "PASTURE" and tile.get("animal") and not tile.get("cared_today"):
                jobs.append((x, y, "CARE", CARE_VALUE))
    return jobs


def _fill_idle_units(obs, action):
    if not IDLE_WORK:
        return action
    try:
        farm, _private = _farm_private(obs)
        step = int(_get(obs, "step", 0) or 0)
        if step == 0:
            _IDLE_HOME.clear()
        positions = [_get(farm, "farmer", None)]
        positions.extend(list(_get(farm, "hands", []) or []))
        orders = [list(action.get("farmer") or ["PASS"])]
        orders.extend([list(order or ["PASS"]) for order in (action.get("hands") or [])])

        jobs = _idle_targets(farm)
        claimed = set()
        for index, order in enumerate(orders):
            if index >= len(positions) or positions[index] is None:
                continue
            if order and order[0] != "PASS":
                _IDLE_HOME.pop(index, None)
                continue
            try:
                px, py = int(positions[index][0]), int(positions[index][1])
            except (TypeError, ValueError, IndexError):
                continue
            home = _IDLE_HOME.setdefault(index, (px, py))
            budget = _next_busy(index, step) - step
            dist_home = abs(px - home[0]) + abs(py - home[1])
            slack = budget - dist_home - int(IDLE_MARGIN)

            if slack <= 0:
                if dist_home > 0:
                    move = _step_toward(farm, (px, py), home)
                    if move:
                        orders[index] = move
                continue

            best = None
            for (tx, ty, verb, value) in jobs:
                if (tx, ty) in claimed:
                    continue
                out = abs(px - tx) + abs(py - ty)
                back = abs(tx - home[0]) + abs(ty - home[1])
                if out + 1 + back > budget - int(IDLE_MARGIN):
                    continue
                score = value - IDLE_DIST_PENALTY * out
                if best is None or score > best[0]:
                    best = (score, out, tx, ty, verb)
            if best is None:
                if dist_home > 0:
                    move = _step_toward(farm, (px, py), home)
                    if move:
                        orders[index] = move
                continue
            _score, out, tx, ty, verb = best
            claimed.add((tx, ty))
            if out == 0:
                orders[index] = [verb]
            else:
                move = _step_toward(farm, (px, py), (tx, ty))
                if move:
                    orders[index] = move

        action["farmer"] = orders[0]
        action["hands"] = orders[1:]
    except Exception:
        return action
    return action


SELL_LEAD = 4
_LEAD_DEBT = {}


def _sell_lead(obs, action):
    """Post the next few steps' scripted sales now, then skip them when due.

    Nothing extra is sold over the game: the same units leave on an earlier
    turn.  In a mirror that is the whole margin, because the opponent's
    identical order lands after ours and takes the lower price.
    """
    if not SELL_LEAD:
        return action
    try:
        step = int(_get(obs, "step", 0) or 0)
        if step == 0:
            _LEAD_DEBT.clear()
        private = _get(obs, "private", {}) or {}
        shed = dict(_get(private, "shed", {}) or {})
        orders = [list(o) for o in (action.get("market") or []) if o]

        # Settle what was already pulled forward.
        rebuilt = []
        for order in orders:
            if order[0] == "SELL" and len(order) >= 3:
                item = order[1]
                owed = int(_LEAD_DEBT.get(item, 0) or 0)
                quantity = max(0, int(order[2] or 0))
                if owed > 0:
                    used = min(owed, quantity)
                    _LEAD_DEBT[item] = owed - used
                    quantity -= used
                if quantity <= 0:
                    continue
                # Never clamp a scripted sale to the shed reading: harvests are
                # dropped into the shed before market orders are processed, so
                # the recorded quantity is legal even when it looks short here.
                shed[item] = max(0, int(shed.get(item, 0) or 0) - quantity)
                rebuilt.append(["SELL", item, quantity])
            else:
                rebuilt.append(order)

        # Pull forward the upcoming ones that we can already cover.
        last = len(_ACTIONS) - 1
        for ahead in range(1, int(SELL_LEAD) + 1):
            future = step + ahead
            if future > last or len(rebuilt) >= 10:
                break
            for order in (_ACTIONS[future].get("market") or []):
                if not order or order[0] != "SELL" or len(order) < 3:
                    continue
                if len(rebuilt) >= 10:
                    break
                item = order[1]
                quantity = min(max(0, int(order[2] or 0)), max(0, int(shed.get(item, 0) or 0)))
                if quantity <= 0:
                    continue
                shed[item] = int(shed.get(item, 0) or 0) - quantity
                _LEAD_DEBT[item] = int(_LEAD_DEBT.get(item, 0) or 0) + quantity
                rebuilt.append(["SELL", item, quantity])

        action["market"] = rebuilt[:10]
    except Exception:
        return action
    return action


RETRY_PURCHASES = 1
RETRY_BUFFER = 250
_RETRY_LAND_COSTS = (1000, 2000, 4000)


def _intended_by(step):
    """Cumulative land and animal purchases the route has ordered by `step`."""
    land = 0
    animals = {"COW": 0, "SHEEP": 0}
    for recorded in _ACTIONS[: max(0, int(step)) + 1]:
        for order in (recorded.get("market") or []):
            if not order:
                continue
            if order[0] == "BUY_LAND":
                land += 1
            elif order[0] == "BUY_ANIMAL" and len(order) >= 3 and order[1] in animals:
                animals[order[1]] += max(0, int(order[2] or 0))
    return land, animals


def _owned_animals(farm, private):
    counts = _placed_animal_counts(farm)
    shed = _get(private, "shed", {}) or {}
    for animal in counts:
        counts[animal] += max(0, int(shed.get(animal, 0) or 0))
    for inventory in (_get(private, "inventories", []) or []):
        for animal in counts:
            counts[animal] += max(0, int((inventory or {}).get(animal, 0) or 0))
    return counts


def _retry_purchases(obs, action):
    """Re-issue land and animals the route ordered but could not afford."""
    if not RETRY_PURCHASES:
        return action
    try:
        farm, private = _farm_private(obs)
        step = int(_get(obs, "step", 0) or 0)
        money = int(_get(farm, "money", 0) or 0)
        orders = [list(o) for o in (action.get("market") or []) if o]
        if len(orders) >= 10:
            return action
        want_land, want_animals = _intended_by(step)
        unlocked = len(_get(farm, "unlocked_quadrants", []) or [])
        budget = money - RETRY_BUFFER

        # Land first: an unbought quadrant caps every later placement.
        have_land = max(0, unlocked - 1)
        pending_land = sum(1 for o in orders if o[0] == "BUY_LAND")
        if have_land + pending_land < want_land and unlocked < 4:
            cost = _RETRY_LAND_COSTS[min(max(0, unlocked - 1), len(_RETRY_LAND_COSTS) - 1)]
            if budget >= cost and len(orders) < 10:
                orders.append(["BUY_LAND"])
                budget -= cost

        owned = _owned_animals(farm, private)
        pending = {"COW": 0, "SHEEP": 0}
        for order in orders:
            if order[0] == "BUY_ANIMAL" and len(order) >= 3 and order[1] in pending:
                pending[order[1]] += max(0, int(order[2] or 0))
        for animal in ("COW", "SHEEP"):
            if len(orders) >= 10:
                break
            short = want_animals[animal] - owned.get(animal, 0) - pending[animal]
            if short <= 0:
                continue
            count = 0
            while count < short and budget >= ANIMAL_COST[animal]:
                budget -= ANIMAL_COST[animal]
                count += 1
            if count > 0:
                orders.append(["BUY_ANIMAL", animal, count])
        action["market"] = orders[:10]
    except Exception:
        return action
    return action


def _terminal_liquidation(obs, action):
    if int(_get(obs, "step", 0) or 0) < len(_ACTIONS) - 1:
        return action
    private = _get(obs, "private", {}) or {}
    shed = _get(private, "shed", {}) or {}
    prices = _get(_get(obs, "market", {}) or {}, "prices", {}) or {}
    stock = [
        (item, max(0, int(quantity or 0)))
        for item, quantity in shed.items()
        if item in SELLABLE_PRODUCTS and int(quantity or 0) > 0
    ]
    stock.sort(key=lambda pair: (-max(1, int(prices.get(pair[0], 1) or 1)), pair[0]))
    action["market"] = [["SELL", item, quantity] for item, quantity in stock[:10]]
    return _aligned(action, obs)


def agent(obs):
    try:
        step = min(max(0, int(_get(obs, "step", 0) or 0)), len(_ACTIONS) - 1)
        if step == 0:
            _RUNTIME["raw_opponent"] = False
        action = _fill_idle_units(obs, _adapt_animals(obs, _ACTIONS[step]))
        action = _retry_purchases(obs, action)
        action = _sell_lead(obs, action)
        return _terminal_liquidation(obs, _aligned(action, obs))
    except Exception:
        farms = list(_get(obs, "farms", []) or [])
        seat = 1 if int(_get(obs, "player", 0) or 0) == 1 else 0
        farm = farms[seat] if seat < len(farms) else {}
        return {
            "farmer": ["PASS"],
            "hands": [["PASS"] for _ in (_get(farm, "hands", []) or [])],
            "market": [],
        }
