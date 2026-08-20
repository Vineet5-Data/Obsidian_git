"""Does Seb's inner-ring layout actually cut travel time?

Seb (allegedly) is the one route in the 37-route field that beats v24 (0-6).
Compare tile usage and walking cost against our own build.

Shed access tiles are the four centre tiles (4,4) (5,4) (4,5) (5,5), so
Chebyshev-ish distance from centre is the real cost of a plot.
"""
import collections
import json
import sys

SHED = [(4, 4), (5, 4), (4, 5), (5, 5)]
MOVES = {"NORTH", "SOUTH", "EAST", "WEST"}


def shed_dist(x, y):
    return min(abs(x - sx) + abs(y - sy) for sx, sy in SHED)


def quadrant(x, y):
    return ("NW" if x < 5 and y < 5 else "NE" if x >= 5 and y < 5
            else "SW" if x < 5 else "SE")


def analyse(path, seat, label):
    with open(path, encoding="utf-8") as handle:
        replay = json.load(handle)
    steps = replay["steps"]

    used = collections.Counter()     # tile -> how many productive ops there
    kinds = {}                       # tile -> what was grown/built there
    moves = 0
    prod = 0
    # Track each unit's position from the observation, then credit the op.
    for index, state in enumerate(steps[1:], start=0):
        obs = steps[index][0].get("observation", {})
        farms = obs.get("farms") or []
        if len(farms) <= seat:
            continue
        farm = farms[seat]
        positions = [farm.get("farmer")] + list(farm.get("hands") or [])
        action = state[seat].get("action") or {}
        units = [action.get("farmer")] + list(action.get("hands") or [])
        for pos, unit in zip(positions, units):
            if not unit or not pos:
                continue
            op = unit[0]
            if op in MOVES:
                moves += 1
                continue
            if op in ("PASS",):
                continue
            x, y = int(pos[0]), int(pos[1])
            used[(x, y)] += 1
            prod += 1
            if op == "PLANT" and len(unit) >= 2:
                kinds[(x, y)] = unit[1]
            elif op in ("BUILD_COOP", "BUILD_PASTURE"):
                kinds[(x, y)] = op.replace("BUILD_", "")

    quads = collections.Counter(quadrant(x, y) for x, y in used)
    dist_hist = collections.Counter(shed_dist(x, y) for x, y in used)
    weighted = sum(shed_dist(x, y) * n for (x, y), n in used.items())

    print(f"--- {label} ---")
    print(f"  distinct worked tiles : {len(used)}")
    print(f"  quadrants used        : {dict(quads)}")
    print(f"  move ops              : {moves:,}   productive ops: {prod:,}"
          f"   move share: {100*moves/max(1,moves+prod):.1f}%")
    print(f"  mean shed distance of worked tiles (op-weighted): "
          f"{weighted/max(1,prod):.2f}")
    print(f"  tiles by shed distance: "
          + "  ".join(f"d{d}:{n}" for d, n in sorted(dist_hist.items())))
    grid = []
    for y in range(10):
        row = ""
        for x in range(10):
            if (x, y) in kinds:
                row += kinds[(x, y)][0]
            elif (x, y) in used:
                row += "."
            else:
                row += " "
        grid.append(row)
    print("  layout (letter=planted/built, .=worked, space=unused):")
    for y, row in enumerate(grid):
        print(f"    {y} |{row}|")


if __name__ == "__main__":
    analyse(r"Top_fresh-21\90639963.json", 1, "Seb (allegedly) 90639963_p1")
    analyse(r"Top_fresh-21\90631991.json", 1, "v24 route (Wufang 90631991_p1)")
