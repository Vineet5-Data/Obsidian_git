src = open("v13.py", encoding="utf-8").read()
src = src.replace("import copy\nimport json", "import copy\nimport json\nimport math", 1)

NEW = '''# Exact replica of the engine price curve (validated 180/180 against replays).
_I0 = 10000
_MP = {
    "STRAWBERRY": (120, 100, "sqrt", 0.70, "linear", 1.60),
    "MELON": (250, 300, "log", 0.20, "sq", 3.60),
}
# Reserve prices apply only to strawberry and melon.  Those are the two goods
# the route dumps into a glut (118 and 96 units below 35% of base against the
# strongest opponent) and the only two whose price reliably recovers.  Milk and
# wool are left alone: milk sits near $50 all season, so withheld milk never
# clears and simply expires unsold.
RESERVE = {"STRAWBERRY": 1.05, "MELON": 0.70}
RESERVE_CASH_FLOOR = 6000
RESERVE_SHED_TIGHT = 70
RESERVE_SHED_PANIC = 88
RESERVE_LAST_DAY = 28
_LAND_COSTS = (1000, 2000, 4000)


def _shape(name, x):
    x = max(0.0, float(x))
    if name == "linear":
        return x
    if name == "sq":
        return x * x
    if name == "sqrt":
        return math.sqrt(x)
    return math.log(1.0 + x)


def _price_at(item, inventory):
    base, target, below_f, below_t, above_f, above_t = _MP[item]
    delta = int(inventory) - _I0
    if delta < 0:
        return max(1, int(round(base + (below_t * base / _shape(below_f, target)) * _shape(below_f, -delta))))
    return max(1, int(round(base - (above_t * base / _shape(above_f, target)) * _shape(above_f, delta))))


def _sell_units(item, inventory, have, floor):
    low, high = 0, max(0, int(have))
    while low < high:
        mid = (low + high + 1) // 2
        if _price_at(item, inventory + mid - 1) >= floor:
            low = mid
        else:
            high = mid - 1
    return low


def _route_cash_need(farm, orders):
    need = 0
    hires = int(_get(farm, "hires_today", 0) or 0)
    unlocked = len(_get(farm, "unlocked_quadrants", []) or [])
    for order in orders:
        op = order[0]
        if op == "HIRE":
            need += _hire_cost(hires)
            hires += 1
        elif op == "BUY_SEED" and len(order) >= 3:
            need += SEED_COST.get(order[1], 0) * max(0, int(order[2] or 0))
        elif op == "BUY_PRODUCT" and len(order) >= 3:
            need += PRODUCT_COST.get(order[1], 0) * max(0, int(order[2] or 0))
        elif op == "BUY_ANIMAL" and len(order) >= 3:
            need += ANIMAL_COST.get(order[1], 0) * max(0, int(order[2] or 0))
        elif op == "BUY_LAND" and unlocked > 0:
            need += _LAND_COSTS[min(max(0, unlocked - 1), len(_LAND_COSTS) - 1)]
            unlocked += 1
    return need


def _reserve_market(obs, action):
    """Hold strawberry and melon back from a glutted market, re-offer on recovery.

    Trimming alone would strand the stock, because the recorded route has no
    later order for it; the top-up pass re-offers every held unit that clears
    the reserve, so nothing expires unsold.
    """
    try:
        farm, private = _farm_private(obs)
        shed = _get(private, "shed", {}) or {}
        inventories = _get(_get(obs, "market", {}) or {}, "inventory", {}) or {}
        step = int(_get(obs, "step", 0) or 0)
        day = int(_get(obs, "day", 0) or 0)
        money = int(_get(farm, "money", 0) or 0)
        orders = [list(order) for order in (action.get("market") or []) if order]
        keep = [order for order in orders if order[0] != "SELL"]
        pressure = sum(max(0, int(v or 0)) for k, v in shed.items() if k in SELLABLE_PRODUCTS)

        active = (
            money >= RESERVE_CASH_FLOOR + _route_cash_need(farm, keep)
            and day <= RESERVE_LAST_DAY
            and pressure < RESERVE_SHED_PANIC
            and step < len(_ACTIONS) - 1
        )
        relax = 0.75 if pressure >= RESERVE_SHED_TIGHT else 1.0

        remaining = dict(shed)
        rebuilt = []
        for order in orders:
            if order[0] != "SELL" or len(order) < 3:
                rebuilt.append(order)
                continue
            item = order[1]
            have = max(0, int(remaining.get(item, 0) or 0))
            # Never clamp a scripted sale to the shed reading: harvests are
            # dropped into the shed before market orders are processed, so the
            # recorded quantity is legal even when it looks short here.
            count = max(0, int(order[2] or 0))
            if active and item in RESERVE and count > 0:
                floor = _MP[item][0] * RESERVE[item] * relax
                inv = int(inventories.get(item, _I0) or _I0)
                count = _sell_units(item, inv, count, floor)
            if count > 0:
                remaining[item] = max(0, have - count)
                rebuilt.append(["SELL", item, count])

        sim = {}
        for order in rebuilt:
            if order[0] == "SELL":
                sim[order[1]] = sim.get(order[1], int(inventories.get(order[1], _I0) or _I0)) + int(order[2])
        extras = []
        for item in RESERVE:
            have = max(0, int(remaining.get(item, 0) or 0))
            if have <= 0:
                continue
            inv = sim.get(item, int(inventories.get(item, _I0) or _I0))
            floor = (_MP[item][0] * RESERVE[item] * relax) if active else 1
            count = _sell_units(item, inv, have, floor)
            if count > 0:
                extras.append((_price_at(item, inv) * count, item, count))
        extras.sort(reverse=True)
        for _value, item, count in extras[: max(0, 10 - len(rebuilt))]:
            rebuilt.append(["SELL", item, count])

        action["market"] = rebuilt[:10]
    except Exception:
        return action
    return action


'''
anchor = "def _terminal_liquidation(obs, action):"
assert anchor in src
src = src.replace(anchor, NEW + anchor, 1)
old = "action = _fill_idle_units(obs, _adapt_animals(obs, _ACTIONS[step]))"
assert old in src
src = src.replace(old, "action = _reserve_market(obs, _fill_idle_units(obs, _adapt_animals(obs, _ACTIONS[step])))", 1)
open("v17.py", "w", encoding="utf-8").write(src)
print("v17.py written")
