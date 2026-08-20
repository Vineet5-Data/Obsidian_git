src = open("v13.py", encoding="utf-8").read()

old = '''            if kind == "PLANT" and tile.get("crop") and not tile.get("watered_today"):
                jobs.append((x, y, "WATER", CROP_VALUE.get(tile["crop"], 25)))
            elif kind == "PASTURE" and tile.get("animal") and not tile.get("cared_today"):
                jobs.append((x, y, "CARE", CARE_VALUE))
    return jobs'''
new = '''            if kind == "PLANT" and tile.get("crop"):
                if int(tile.get("yield_units", 0) or 0) > 0:
                    jobs.append((x, y, "HARVEST",
                                 HARVEST_VALUE * int(tile.get("yield_units", 0) or 0)))
                if not tile.get("watered_today"):
                    jobs.append((x, y, "WATER", CROP_VALUE.get(tile["crop"], 25)))
            elif kind == "PASTURE" and tile.get("animal"):
                if not tile.get("cared_today"):
                    jobs.append((x, y, "CARE", CARE_VALUE))
                if int(tile.get("yield_units", 0) or 0) > 0:
                    jobs.append((x, y, "HARVEST",
                                 HARVEST_VALUE * int(tile.get("yield_units", 0) or 0)))
                if tile.get("fertilizer_available"):
                    jobs.append((x, y, "COLLECT_FERTILIZER", FERT_VALUE))
    return jobs'''
assert old in src
src = src.replace(old, new, 1)
src = src.replace("IDLE_DIST_PENALTY = 20",
                  "IDLE_DIST_PENALTY = 20\nHARVEST_VALUE = 0\nFERT_VALUE = 0", 1)

# Harvesting and fertilizer collection load the unit's inventory, so they are
# only safe while the shed still has room to take the drop at end of day.
old_guard = '''        jobs = _idle_targets(farm)'''
new_guard = '''        jobs = _idle_targets(farm)
        shed_used = sum(
            max(0, int(v or 0))
            for k, v in ((_get(obs, "private", {}) or {}).get("shed", {}) or {}).items()
        )
        if shed_used >= SHED_ROOM_LIMIT:
            jobs = [j for j in jobs if j[2] in ("WATER", "CARE")]'''
assert old_guard in src
src = src.replace(old_guard, new_guard, 1)
src = src.replace("HARVEST_VALUE = 0", "HARVEST_VALUE = 0\nSHED_ROOM_LIMIT = 80", 1)

open("v14.py", "w", encoding="utf-8").write(src)
print("v14.py written")
