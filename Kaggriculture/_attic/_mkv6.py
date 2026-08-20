src = open("main.py", encoding="utf-8").read()

assert "import copy" in src
src = src.replace("import copy\nimport json", "import copy\nimport json\nimport math", 1)

NEW = '''
# ---------------------------------------------------------------- market layer
# Exact replica of the engine price curve (validated 180/180 against replays).
_I0 = 10000
_MP = {
    "WHEAT": (25, 400, "sqrt", 0.80, "log", 0.20),
    "CARROT": (35, 450, "log", 0.20, "sqrt", 0.70),
    "TOMATO": (60, 200, "linear", 0.40, "sqrt", 0.60),
    "STRAWBERRY": (120, 100, "sqrt", 0.70, "linear", 1.60),
    "MELON": (250, 300, "log", 0.20, "sq", 3.60),
    "EGG": (50, 332, "linear", 0.40, "log", 0.20),
    "MILK": (160, 122, "sqrt", 0.60, "linear", 1.60),
    "WOOL": (200, 105, "log", 0.20, "sq", 3.20),
    "FERTILIZER": (100, 200, "linear", 0.40, "linear", 0.40),
}
# Reserve price as a fraction of base.  MELON and WOOL ride `sq` curves into a
# thin town drain (140 and 331 units per season), so they collapse to $1 when
# dumped; the recorded route sold 210 melons and 240 wool that way.
_FLOOR = {
    "MELON": 0.62, "WOOL": 0.62, "STRAWBERRY": 0.72, "MILK": 0.68,
    "WHEAT": 0.50, "FERTILIZER": 0.50, "CARROT": 0.50, "EGG": 0.50, "TOMATO": 0.50,
}
_LAND_COSTS = (1000, 2000, 4000)
CASH_FLOOR = 5000
TRIM = 1
FLOOR_SCALE = 1.0
SHED_TIGHT = 70
SHED_PANIC = 88
LIQUIDATE_DAY = 29
TOPUP_DAY = 5
TOPUP_ITEMS = ("MILK", "WOOL", "EGG", "STRAWBERRY", "MELON", "CARROT", "TOMATO")


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
    spec = _MP.get(item)
    if spec is None:
        return 1
    base, target, below_f, below_t, above_f, above_t = spec
    delta = int(inventory) - _I0
    if delta < 0:
        amp = below_t * base / _shape(below_f, target)
        return max(1, int(round(base + amp * _shape(below_f, -delta))))
    amp = above_t * base / _shape(above_f, target)
    return max(1, int(round(base - amp * _shape(above_f, delta))))


def _sell_units(item, inventory, have, floor):
    """Largest n <= have where every unit still clears `floor`."""
    low, high = 0, max(0, int(have))
    while low < high:
        mid = (low + high + 1) // 2
        if _price_at(item, inventory + mid - 1) >= floor:
            low = mid
        else:
            high = mid - 1
    return low


def _sell_value(item, inventory, count):
    total = 0
    for offset in range(max(0, int(count))):
        total += _price_at(item, inventory + offset)
    return total


def _route_cash_need(obs, farm, orders):
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


def _adaptive_market(obs, action):
    """Trim the recorded SELL schedule down to units that clear a reserve price.

    The route is left in charge of cash flow: orders are only ever *reduced*,
    and only while the farm is liquid enough that skipping a sale cannot stall
    the build.  Withholding sales unconditionally was tested and starved the
    route of the cash it needs for animals (final money fell to $32.9k).
    """
    farm, private = _farm_private(obs)
    shed = _get(private, "shed", {}) or {}
    market = _get(obs, "market", {}) or {}
    inventories = _get(market, "inventory", {}) or {}
    step = int(_get(obs, "step", 0) or 0)
    day = int(_get(obs, "day", 0) or 0)
    money = int(_get(farm, "money", 0) or 0)

    orders = [list(order) for order in (action.get("market") or []) if order]
    if not any(order[0] == "SELL" for order in orders):
        return action

    keep = [order for order in orders if order[0] != "SELL"]
    need = _route_cash_need(obs, farm, keep)
    pressure = sum(
        max(0, int(quantity or 0))
        for item, quantity in shed.items()
        if item in SELLABLE_PRODUCTS
    )

    # Reserve pricing is a luxury: it only applies with cash in hand, room in
    # the shed, and season left to wait for the town to drain the market.
    liquid = bool(TRIM) and money >= CASH_FLOOR + need
    if step >= len(_ACTIONS) - 1 or day >= LIQUIDATE_DAY or pressure >= SHED_PANIC:
        liquid = False

    relax = 1.0
    if day >= LIQUIDATE_DAY - 1:
        relax = 0.65
    if pressure >= SHED_TIGHT:
        relax *= 0.75

    remaining = dict(shed)
    rebuilt = []
    for order in orders:
        if order[0] != "SELL" or len(order) < 3:
            rebuilt.append(order)
            continue
        item = order[1]
        have = max(0, int(remaining.get(item, 0) or 0))
        count = min(max(0, int(order[2] or 0)), have)
        if liquid and item in _MP and count > 0:
            start = int(inventories.get(item, _I0) or _I0)
            floor = _MP[item][0] * _FLOOR.get(item, 0.55) * relax * FLOOR_SCALE
            count = _sell_units(item, start, count, floor)
        if count > 0:
            remaining[item] = have - count
            rebuilt.append(["SELL", item, count])

    # Trimmed units must come back to market or they simply rot: the recorded
    # route has no later order for them.  Every step, any surplus output that
    # clears the reserve is re-offered using whatever order slots are spare.
    sim = {}
    for order in rebuilt:
        if order[0] == "SELL":
            item = order[1]
            sim[item] = sim.get(item, int(inventories.get(item, _I0) or _I0)) + int(order[2])
    if day >= TOPUP_DAY:
        extras = []
        for item, quantity in remaining.items():
            if item not in TOPUP_ITEMS or item not in _MP:
                continue
            have = max(0, int(quantity or 0))
            if have <= 0:
                continue
            start = sim.get(item, int(inventories.get(item, _I0) or _I0))
            floor = _MP[item][0] * _FLOOR.get(item, 0.55) * relax * FLOOR_SCALE
            count = _sell_units(item, start, have, floor)
            if count > 0:
                extras.append((_sell_value(item, start, count), item, count))
        extras.sort(reverse=True)
        slots = max(0, 10 - len(rebuilt))
        for _, item, count in extras[:slots]:
            rebuilt.append(["SELL", item, count])

    action["market"] = rebuilt[:10]
    return action
'''

anchor = "def _terminal_liquidation(obs, action):"
assert anchor in src
src = src.replace(anchor, NEW.strip() + "\n\n\n" + anchor, 1)

old_call = "return _terminal_liquidation(obs, _adapt_animals(obs, _ACTIONS[step]))"
assert old_call in src
src = src.replace(
    old_call,
    "action = _adapt_animals(obs, _ACTIONS[step])\n"
    "        action = _aligned(_adaptive_market(obs, action), obs)\n"
    "        return _terminal_liquidation(obs, action)",
    1,
)

open("v6.py", "w", encoding="utf-8").write(src)
print("v6.py written", len(src), "bytes")
