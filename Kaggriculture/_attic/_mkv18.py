src = open("v13.py", encoding="utf-8").read()

NEW = '''# The town drains a fixed number of units per day (roughly 18 strawberry and
# 5 melon).  The recorded route hoards both, then dumps 47 strawberries at once
# into a $12 market on day 24 while the strongest opponent sells 16-38 a day
# from day 15 and clears $155.  A daily quota converts the burst into a stream.
DAILY_CAP = {"STRAWBERRY": 20, "MELON": 8}
CAP_LAST_DAY = 27
_SOLD = {"day": -1, "n": {}}


def _quota_market(obs, action):
    try:
        farm, private = _farm_private(obs)
        shed = _get(private, "shed", {}) or {}
        step = int(_get(obs, "step", 0) or 0)
        day = int(_get(obs, "day", 0) or 0)
        if step == 0 or _SOLD["day"] != day:
            _SOLD["day"] = day
            _SOLD["n"] = {}
        if day > CAP_LAST_DAY or step >= len(_ACTIONS) - 1:
            return action

        orders = [list(order) for order in (action.get("market") or []) if order]
        remaining = dict(shed)
        rebuilt = []
        for order in orders:
            if order[0] != "SELL" or len(order) < 3 or order[1] not in DAILY_CAP:
                rebuilt.append(order)
                continue
            item = order[1]
            allowed = int(DAILY_CAP[item]) - int(_SOLD["n"].get(item, 0))
            # No shed clamp: harvests drop into the shed before market orders
            # are processed, so the recorded quantity is legal as written.
            count = min(max(0, int(order[2] or 0)), max(0, allowed))
            if count <= 0:
                continue
            _SOLD["n"][item] = _SOLD["n"].get(item, 0) + count
            remaining[item] = max(0, int(remaining.get(item, 0) or 0) - count)
            rebuilt.append(["SELL", item, count])

        # Start the stream as soon as there is stock, rather than on the day the
        # recorded route happens to begin selling.
        for item in DAILY_CAP:
            have = max(0, int(remaining.get(item, 0) or 0))
            allowed = int(DAILY_CAP[item]) - int(_SOLD["n"].get(item, 0))
            count = min(have, max(0, allowed))
            if count > 0 and len(rebuilt) < 10:
                _SOLD["n"][item] = _SOLD["n"].get(item, 0) + count
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
src = src.replace(old, "action = _quota_market(obs, _fill_idle_units(obs, _adapt_animals(obs, _ACTIONS[step])))", 1)
open("v18.py", "w", encoding="utf-8").write(src)
print("v18.py written")
