src = open("v7a.py", encoding="utf-8").read()

NEW = '''MAX_HANDS = 14


def _cap_hires(obs, action):
    """Drop the priciest hires of the day.

    Hire cost is Fibonacci in the day's hire index, so hands 13 and 14 alone
    cost 233 + 377 per day.  Roughly a sixth of all unit slots are already
    PASS and output is capped by town demand, so the marginal hand earns far
    less than it costs.
    """
    farm, _private = _farm_private(obs)
    have = len(_get(farm, "hands", []) or [])
    orders = []
    for order in (action.get("market") or []):
        if order and order[0] == "HIRE":
            if have >= int(MAX_HANDS):
                continue
            have += 1
        orders.append(order)
    action["market"] = orders
    return action


'''
anchor = "def _terminal_liquidation(obs, action):"
assert anchor in src
src = src.replace(anchor, NEW + anchor, 1)
old_call = "return _terminal_liquidation(obs, _adapt_animals(obs, _ACTIONS[step]))"
assert old_call in src
src = src.replace(old_call,
    "action = _cap_hires(obs, _adapt_animals(obs, _ACTIONS[step]))\n"
    "        return _terminal_liquidation(obs, _aligned(action, obs))", 1)
open("v12.py", "w", encoding="utf-8").write(src)
print("v12.py written")
