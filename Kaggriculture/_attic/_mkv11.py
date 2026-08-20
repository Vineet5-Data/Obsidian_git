src = open("v10.py", encoding="utf-8").read()

old = '''def _idle_targets(farm):
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
    return water, care'''
new = '''# Watering is rationed by crop value, not by proximity: strawberry runs 45%
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
    return jobs'''
assert old in src
src = src.replace(old, new, 1)

old_sel = '''        water, care = _idle_targets(farm)'''
new_sel = '''        jobs = _idle_targets(farm)'''
assert old_sel in src
src = src.replace(old_sel, new_sel, 1)

old_best = '''            best = None
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
            if best is None:'''
new_best = '''            best = None
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
            if best is None:'''
assert old_best in src
src = src.replace(old_best, new_best, 1)

old_use = '''            out, tx, ty, verb = best'''
new_use = '''            _score, out, tx, ty, verb = best'''
assert old_use in src
src = src.replace(old_use, new_use, 1)

open("v11.py", "w", encoding="utf-8").write(src)
print("v11.py written")
