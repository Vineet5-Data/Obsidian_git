"""Extract every 719-action route tape from the Top_fresh-21 pool.

Writes one compressed tape per (episode, seat) into .routes/ and prints a
strategy fingerprint for each: hand usage, land, animals, crops, sales.

Kaggle stores the initial observation as steps[0]; the action applied for
observation step N is recorded in replay steps[N + 1].
"""
import collections
import hashlib
import json
import os
import zlib

DIR = r"C:\Users\Vinee\Desktop\Kaggriculture\Top_fresh-21"
OUT = r"C:\Users\Vinee\Desktop\Kaggriculture\.routes"


def tape_for(steps, seat):
    actions = []
    for index in range(len(steps)):
        src = steps[index + 1] if index + 1 < len(steps) else None
        raw = src[seat].get("action") if src and seat < len(src) else None
        if not isinstance(raw, dict):
            raw = {}
        actions.append({
            "farmer": list(raw.get("farmer") or ["PASS"]),
            "hands": [list(h or ["PASS"]) for h in (raw.get("hands") or [])],
            "market": [list(m) for m in (raw.get("market") or [])],
        })
    return actions


def fingerprint(tape):
    """Compact description of what this route actually does."""
    buys = collections.Counter()
    sells = collections.Counter()
    sell_qty = collections.Counter()
    ops = collections.Counter()
    hires = 0
    land = 0
    max_hands = 0
    planted = collections.Counter()
    placed = collections.Counter()
    first_land_step = None
    first_animal_step = None
    for step, act in enumerate(tape):
        max_hands = max(max_hands, len(act["hands"]))
        for unit in [act["farmer"], *act["hands"]]:
            if not unit:
                continue
            ops[unit[0]] += 1
            if unit[0] == "PLANT" and len(unit) >= 2:
                planted[unit[1]] += 1
            if unit[0] == "PLACE" and len(unit) >= 2:
                placed[unit[1]] += 1
        for order in act["market"]:
            if not order:
                continue
            verb = order[0]
            if verb == "HIRE":
                hires += 1
            elif verb == "BUY_LAND":
                land += 1
                if first_land_step is None:
                    first_land_step = step
            elif verb == "SELL" and len(order) >= 3:
                sells[order[1]] += 1
                sell_qty[order[1]] += int(order[2] or 0)
            elif verb == "BUY_ANIMAL" and len(order) >= 3:
                buys[order[1]] += int(order[2] or 0)
                if first_animal_step is None:
                    first_animal_step = step
            elif verb in ("BUY_SEED", "BUY_PRODUCT") and len(order) >= 3:
                buys[order[1]] += int(order[2] or 0)
    return {
        "max_hands": max_hands,
        "hires": hires,
        "land_buys": land,
        "first_land_step": first_land_step,
        "first_animal_step": first_animal_step,
        "animals": {k: v for k, v in buys.items() if k in ("COW", "SHEEP", "GOOSE")},
        "seeds": {k: v for k, v in buys.items() if k not in ("COW", "SHEEP", "GOOSE")},
        "planted": dict(planted),
        "placed": dict(placed),
        "sell_qty": dict(sell_qty.most_common()),
        "pass_ops": ops.get("PASS", 0),
        "total_ops": sum(ops.values()),
    }


def main():
    os.makedirs(OUT, exist_ok=True)
    rows = []
    for name in sorted(os.listdir(DIR)):
        if not name.endswith(".json"):
            continue
        episode = name[:-5]
        with open(os.path.join(DIR, name), encoding="utf-8") as handle:
            replay = json.load(handle)
        steps = replay.get("steps") or []
        teams = (replay.get("info") or {}).get("TeamNames") or ["?", "?"]
        final = steps[-1]
        for seat in (0, 1):
            tape = tape_for(steps, seat)
            payload = json.dumps(tape, separators=(",", ":")).encode()
            digest = hashlib.sha256(payload).hexdigest()[:16]
            path = os.path.join(OUT, f"{episode}_p{seat}.json.z")
            with open(path, "wb") as handle:
                handle.write(zlib.compress(payload, 9))
            rows.append({
                "episode": episode,
                "seat": seat,
                "team": teams[seat] if seat < len(teams) else "?",
                "bank": final[seat].get("reward"),
                "hash": digest,
                "fp": fingerprint(tape),
            })
        print(f"{episode} done", flush=True)
    with open(os.path.join(OUT, "index.json"), "w", encoding="utf-8") as handle:
        json.dump(rows, handle, indent=1)
    print(f"\nwrote {len(rows)} tapes to {OUT}")


if __name__ == "__main__":
    main()
