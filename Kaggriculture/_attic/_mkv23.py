"""Build v23: v21 (Seb route + mirror front-run) with failed purchases retried.

Seb's route deliberately runs at near-zero cash - $16 on day 4, $10 on day 8.
On its own seed every purchase clears.  On seed 1001 one fails, the 4th
quadrant is never bought, the herd stalls at 13 animals instead of 19, and the
game is lost 57,151 to 109,944.  A recorded purchase that does not clear is
gone for the season, so the shortfall is re-issued once cash allows.
"""

src = open("v21.py", encoding="utf-8").read()

NEW = '''RETRY_PURCHASES = 1
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


'''

anchor = "def _terminal_liquidation(obs, action):"
assert anchor in src
src = src.replace(anchor, NEW + anchor, 1)

OLD = "        action = _sell_lead(obs, action)"
assert OLD in src
src = src.replace(OLD, "        action = _retry_purchases(obs, action)\n" + OLD, 1)

open("v23.py", "w", encoding="utf-8").write(src)
print("v23.py written")
