"""Build v21: the Seb route, selling a step ahead of its own schedule.

v16 clones episode 90503598 exactly and therefore draws with it, 77,539 apiece.
Both sides post identical SELL orders into one order book, so the price each
receives is set by who reaches the town first.  Pulling our scripted sales a
few steps forward puts our units in front of the mirrored ones.
"""

src = open("v16.py", encoding="utf-8").read()

NEW = '''SELL_LEAD = 4
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


'''

anchor = "def _terminal_liquidation(obs, action):"
assert anchor in src
src = src.replace(anchor, NEW + anchor, 1)

OLD = "action = _fill_idle_units(obs, _adapt_animals(obs, _ACTIONS[step]))"
assert OLD in src
src = src.replace(
    OLD,
    "action = _fill_idle_units(obs, _adapt_animals(obs, _ACTIONS[step]))\n"
    "        action = _sell_lead(obs, action)",
    1,
)

open("v21.py", "w", encoding="utf-8").write(src)
print("v21.py written")
