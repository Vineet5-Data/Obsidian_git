"""Build the SELL-hazard prior from the fresh replay pool.

For each step, for each premium item: how often does a top route post a SELL
for it, and how big is that SELL typically.  boatlee derives the same table
from six top submissions; this one is built from the 2026-08-07 pool, which is
newer, and from both seats of every episode.

Output: {step: [[item, probability, median_quantity], ...]} for steps where at
least one premium item clears the probability floor.
"""
import base64
import collections
import json
import os
import statistics
import zlib

ROUTES = r"C:\Users\Vinee\Desktop\Kaggriculture\.routes"
PREMIUM = ("STRAWBERRY", "MELON", "MILK", "WOOL")
FLOOR = 0.30


def main():
    tapes = []
    for name in sorted(os.listdir(ROUTES)):
        if not name.endswith(".json.z"):
            continue
        with open(os.path.join(ROUTES, name), "rb") as handle:
            tapes.append(json.loads(zlib.decompress(handle.read()).decode("utf-8")))
    print(f"{len(tapes)} tapes")

    counts = collections.defaultdict(lambda: collections.defaultdict(list))
    for tape in tapes:
        for step, action in enumerate(tape):
            posted = collections.Counter()
            for order in (action.get("market") or []):
                if (order and len(order) >= 3 and order[0] == "SELL"
                        and order[1] in PREMIUM):
                    posted[order[1]] += max(0, int(order[2] or 0))
            for item, quantity in posted.items():
                counts[step][item].append(quantity)

    hazard = {}
    total = len(tapes)
    for step, items in counts.items():
        rows = []
        for item, quantities in items.items():
            probability = len(quantities) / total
            if probability < FLOOR:
                continue
            rows.append([item, round(probability, 3),
                         int(statistics.median(quantities))])
        if rows:
            rows.sort(key=lambda row: -row[1])
            hazard[str(step)] = rows

    print(f"hazard steps: {len(hazard)}")
    spread = collections.Counter(row[0] for rows in hazard.values() for row in rows)
    print("by item:", dict(spread))
    peak = sorted(hazard.items(), key=lambda kv: -max(r[1] for r in kv[1]))[:6]
    for step, rows in peak:
        print(f"  step {step}: {rows}")

    payload = json.dumps(hazard, separators=(",", ":")).encode()
    blob = base64.b64encode(zlib.compress(payload, 9)).decode()
    print(f"\nraw {len(payload):,} B -> blob {len(blob):,} B")
    with open("_hazard_blob.txt", "w", encoding="utf-8") as handle:
        handle.write(blob)
    print("wrote _hazard_blob.txt")


if __name__ == "__main__":
    main()
