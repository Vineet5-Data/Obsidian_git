src = open("v13.py", encoding="utf-8").read()

NEW = '''WHEAT_BUY_CAP = 10000
WHEAT_SELL_CAP = 10000
_WHEAT = {"bought": 0, "sold": 0}


def _cap_wheat(obs, action):
    """Throttle the route's wheat round-trip.

    The recorded route buys 929 wheat ($31,968, its largest single cost) and
    sells 776 back.  The strongest observed opponent buys 372 and sells 70,
    spending the difference on land and animals instead.
    """
    if int(_get(obs, "step", 0) or 0) == 0:
        _WHEAT["bought"] = 0
        _WHEAT["sold"] = 0
    orders = []
    for order in (action.get("market") or []):
        if order and len(order) >= 3 and order[1] == "WHEAT":
            quantity = max(0, int(order[2] or 0))
            if order[0] == "BUY_PRODUCT":
                allowed = max(0, int(WHEAT_BUY_CAP) - _WHEAT["bought"])
                quantity = min(quantity, allowed)
                if quantity <= 0:
                    continue
                _WHEAT["bought"] += quantity
                order = [order[0], order[1], quantity]
            elif order[0] == "SELL":
                allowed = max(0, int(WHEAT_SELL_CAP) - _WHEAT["sold"])
                quantity = min(quantity, allowed)
                if quantity <= 0:
                    continue
                _WHEAT["sold"] += quantity
                order = [order[0], order[1], quantity]
        orders.append(order)
    action["market"] = orders
    return action


'''
anchor = "def _terminal_liquidation(obs, action):"
assert anchor in src
src = src.replace(anchor, NEW + anchor, 1)
old = "action = _fill_idle_units(obs, _adapt_animals(obs, _ACTIONS[step]))"
assert old in src
src = src.replace(old, "action = _cap_wheat(obs, _fill_idle_units(obs, _adapt_animals(obs, _ACTIONS[step])))", 1)
open("v15.py", "w", encoding="utf-8").write(src)
print("v15.py written")
