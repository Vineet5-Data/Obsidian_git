src = open("v7a.py", encoding="utf-8").read()

NEW = '''IDLE_WORK = 1
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


def _idle_targets(farm):
    """Dry crops first: 38% of crop-days go unwatered while units idle."""
    water, care = [], []
    rows = _get(farm, "tiles", []) or []
    for y, row in enumerate(rows):
        for x, tile in enumerate(row or []):
            if not isinstance(tile, dict):
                continue
            kind = tile.get("kind")
            if kind == "PLANT" and tile.get("crop") and not tile.get("watered_today"):
                water.append((x, y))
            elif kind == "PASTURE" and tile.get("animal") and not tile.get("cared_today"):
                care.append((x, y))
    return water, care


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

        water, care = _idle_targets(farm)
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
            for pool, verb in ((water, "WATER"), (care, "CARE")):
                for (tx, ty) in pool:
                    if (tx, ty) in claimed:
                        continue
                    out = abs(px - tx) + abs(py - ty)
                    back = abs(tx - home[0]) + abs(ty - home[1])
                    if out + 1 + back > budget - int(IDLE_MARGIN):
                        continue
                    if best is None or out < best[0]:
                        best = (out, tx, ty, verb)
            if best is None:
                if dist_home > 0:
                    move = _step_toward(farm, (px, py), home)
                    if move:
                        orders[index] = move
                continue
            out, tx, ty, verb = best
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


'''
anchor = "def _terminal_liquidation(obs, action):"
assert anchor in src
src = src.replace(anchor, NEW + anchor, 1)

old_call = "return _terminal_liquidation(obs, _adapt_animals(obs, _ACTIONS[step]))"
assert old_call in src
src = src.replace(
    old_call,
    "action = _fill_idle_units(obs, _adapt_animals(obs, _ACTIONS[step]))\n"
    "        return _terminal_liquidation(obs, _aligned(action, obs))",
    1,
)
open("v10.py", "w", encoding="utf-8").write(src)
print("v10.py written")
