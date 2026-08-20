src = open("v7a.py", encoding="utf-8").read()

NEW = '''IDLE_WORK = 1


def _tile_at(farm, position):
    try:
        x, y = int(position[0]), int(position[1])
    except (TypeError, ValueError, IndexError):
        return None
    rows = _get(farm, "tiles", []) or []
    if 0 <= y < len(rows):
        row = rows[y] or []
        if 0 <= x < len(row):
            return row[x]
    return None


def _idle_task(tile):
    """A useful in-place action for a unit that the route left idle.

    Movement is never emitted: the recorded route addresses units by index and
    assumes their positions, so relocating one would desynchronise every later
    order.  Only same-tile buffs are used.
    """
    if not isinstance(tile, dict):
        return None
    if tile.get("kind") == "PASTURE" and tile.get("animal"):
        if not tile.get("cared_today"):
            return ["CARE"]
    elif tile.get("kind") == "PLANT" and tile.get("crop"):
        if not tile.get("watered_today"):
            return ["WATER"]
    return None


def _fill_idle_units(obs, action):
    if not IDLE_WORK:
        return action
    farm, _private = _farm_private(obs)
    units = [(_get(farm, "farmer", None), action.get("farmer") or ["PASS"])]
    hands = [list(order or ["PASS"]) for order in (action.get("hands") or [])]
    positions = list(_get(farm, "hands", []) or [])
    for index, order in enumerate(hands):
        units.append((positions[index] if index < len(positions) else None, order))

    filled = []
    for position, order in units:
        if order and order[0] != "PASS":
            filled.append(order)
            continue
        task = _idle_task(_tile_at(farm, position)) if position is not None else None
        filled.append(task or ["PASS"])
    action["farmer"] = filled[0]
    action["hands"] = filled[1:]
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
open("v9.py", "w", encoding="utf-8").write(src)
print("v9.py written")
