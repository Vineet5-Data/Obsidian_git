"""Build v25 = v24 + order-safe premium preemption.

In a near-mirror the two farms post the same premium SELL within a turn of each
other, and the one that lands first takes the better price.  The pool says when
that happens: at step 384, 97.7% of top routes post SELL MILK; at 432, 97.7%
post STRAWBERRY.

v25 moves a bounded slice of the NEXT turn's scheduled premium SELL to this
turn, then deducts exactly that much from the sale when it comes due.  The
two-turn quantity is conserved - this changes timing, never production.

Guards, all of them load-bearing:
  * only fires when the opponent looks like a clone (public-state distance <= 6)
  * only for STRAWBERRY / MELON / MILK / WOOL, only in 120 <= step < 680
  * appends rather than inserting at 0 (boatlee's R3 finding: jumping ahead of
    our own same-turn STRAWBERRY order reverses the gain)
  * every SELL is clamped to the shed we will actually have, counting the
    DROP/PLACE deposits this same turn makes -- the naive clamp against the
    raw shed reading deletes legal scripted sales and cost v21 its whole game

Usage:  python _mkv25.py <tape.json.z> <out.py> ["docstring"]
"""
import base64
import json
import sys
import textwrap
import zlib

import _mkv24

HAZARD_BLOB = open("_hazard_blob.txt", encoding="utf-8").read().strip()

PREEMPT = '''

# ---------------------------------------------------------------------------
# order-safe premium preemption
# ---------------------------------------------------------------------------
USE_PREEMPT = 1
PREEMPT_THRESHOLD = 0.5
PREEMPT_FRACTION = 2.0
PREEMPT_MAX_BATCH = 30
PREEMPT_COOLDOWN = 1
PREEMPT_MAX_CLONE_DISTANCE = 6
PREEMPT_START = 120
PREEMPT_STOP = 680
_PREMIUM = ("STRAWBERRY", "MELON", "MILK", "WOOL")
_SHED_CAP = 100

_HAZARD = json.loads(zlib.decompress(base64.b64decode(
%s
)).decode("utf-8"))

_SHIFT_STATE = {
    0: {"last_step": -1, "due_step": -1, "due": {}, "last_preempt": -10 ** 9},
    1: {"last_step": -1, "due_step": -1, "due": {}, "last_preempt": -10 ** 9},
}


def _shed_access(size):
    half = size // 2
    return {(half - 1, half - 1), (half, half - 1),
            (half - 1, half), (half, half)}


def _projected_shed(obs, action):
    """The shed as it will read after this turn's DROP/PLACE deposits land.

    Harvests are dropped into the shed before market orders are processed, so
    clamping a scripted SELL against the raw shed reading silently deletes a
    legal order.  This projects the deposits first.
    """
    farm = _farm(obs)
    private = _get(obs, "private", {}) or {}
    projected = {key: max(0, int(value or 0))
                 for key, value in dict(_get(private, "shed", {}) or {}).items()}
    inventories = list(_get(private, "inventories", []) or [])
    positions = [_get(farm, "farmer", [0, 0]), *list(_get(farm, "hands", []) or [])]
    units = [action.get("farmer", ["PASS"]), *list(action.get("hands") or [])]
    tiles = list(_get(farm, "tiles", []) or [])
    access = _shed_access(len(tiles) or 10)
    for index, unit in enumerate(units):
        if index >= len(positions) or index >= len(inventories):
            continue
        position = positions[index]
        if not isinstance(position, (list, tuple)) or len(position) < 2:
            continue
        x, y = int(position[0]), int(position[1])
        if (x, y) not in access or not (0 <= y < len(tiles) and 0 <= x < len(tiles[y] or [])):
            continue
        inventory = {key: max(0, int(value or 0))
                     for key, value in dict(inventories[index] or {}).items()}
        if unit and unit[0] == "DROP":
            deposits = list(inventory.items())
        elif unit and unit[0] == "PLACE" and len(unit) >= 2:
            item = unit[1]
            tile = tiles[y][x]
            structure = {"COW": "PASTURE", "SHEEP": "PASTURE", "GOOSE": "COOP"}.get(item)
            if (structure and isinstance(tile, dict)
                    and tile.get("kind") == structure and not tile.get("animal")):
                continue
            try:
                requested = int(unit[2]) if len(unit) >= 3 else 1
            except (TypeError, ValueError):
                continue
            deposits = ((item, min(max(0, requested), inventory.get(item, 0))),)
        else:
            continue
        for item, quantity in deposits:
            room = max(0, _SHED_CAP - sum(projected.values()))
            amount = min(max(0, int(quantity or 0)), room)
            if amount:
                projected[item] = projected.get(item, 0) + amount
    return projected


def _public_signature(farm):
    counts = {key: 0 for key in ("WHEAT", "CARROT", "TOMATO", "STRAWBERRY",
                                 "MELON", "COW", "SHEEP", "GOOSE",
                                 "PASTURE", "COOP", "WEED")}
    for row in (_get(farm, "tiles", []) or []):
        for tile in (row if isinstance(row, list) else [row]):
            if not isinstance(tile, dict):
                continue
            for field in ("crop", "animal", "kind"):
                value = str(tile.get(field, "")).upper()
                if value in counts:
                    counts[value] += 1
                    break
    return (len(_get(farm, "hands", []) or []),
            len(_get(farm, "unlocked_quadrants", []) or []),
            tuple(counts[key] for key in sorted(counts)))


def _clone_distance(obs):
    farms = list(_get(obs, "farms", []) or [])
    if len(farms) < 2:
        return 10 ** 9
    left, right = _public_signature(farms[0]), _public_signature(farms[1])
    return (abs(left[0] - right[0]) + 3 * abs(left[1] - right[1])
            + sum(abs(a - b) for a, b in zip(left[2], right[2])))


def _safe_market(obs, action):
    remaining = _projected_shed(obs, action)
    market = []
    for raw in (action.get("market") or []):
        order = list(raw)
        if len(order) >= 3 and order[0] == "SELL":
            item = order[1]
            try:
                requested = max(0, int(order[2]))
            except (TypeError, ValueError):
                requested = 0
            quantity = min(requested, max(0, int(remaining.get(item, 0) or 0)))
            if quantity <= 0:
                continue
            order[2] = quantity
            remaining[item] = max(0, int(remaining.get(item, 0) or 0) - quantity)
        market.append(order)
    action["market"] = market[:10]
    return action


def _shift_state(obs, step):
    state = _SHIFT_STATE[_seat(obs)]
    if step == 0 or step < int(state.get("last_step", -1)):
        state = {"last_step": step, "due_step": -1, "due": {},
                 "last_preempt": -10 ** 9}
        _SHIFT_STATE[_seat(obs)] = state
    state["last_step"] = step
    return state


def _repay_shift(obs, action, step):
    """Deduct whatever was sold a turn early from the sale now coming due."""
    state = _shift_state(obs, step)
    if int(state.get("due_step", -1)) != step:
        if int(state.get("due_step", -1)) < step:
            state["due_step"], state["due"] = -1, {}
        return action
    due = {item: max(0, int(quantity))
           for item, quantity in dict(state.get("due") or {}).items()}
    market = []
    for raw in (action.get("market") or []):
        order = list(raw)
        if len(order) >= 3 and order[0] == "SELL" and due.get(order[1], 0) > 0:
            item = order[1]
            requested = max(0, int(order[2]))
            paid = min(requested, due[item])
            requested -= paid
            due[item] -= paid
            if requested <= 0:
                continue
            order[2] = requested
        market.append(order)
    action["market"] = market
    state["due_step"], state["due"] = -1, {}
    return action


def _future_base_sells(step):
    if step + 1 >= len(_ACTIONS):
        return {}
    result = {}
    for raw in (_ACTIONS[step + 1].get("market") or []):
        if len(raw) >= 3 and raw[0] == "SELL" and raw[1] in _PREMIUM:
            result[raw[1]] = result.get(raw[1], 0) + max(0, int(raw[2] or 0))
    return result


def _remaining_shed(obs, action):
    remaining = _projected_shed(obs, action)
    for raw in (action.get("market") or []):
        if len(raw) >= 3 and raw[0] == "SELL":
            item = raw[1]
            remaining[item] = max(0, int(remaining.get(item, 0) or 0)
                                  - max(0, int(raw[2] or 0)))
    return remaining


def _preempt_shift(obs, action, step):
    if not USE_PREEMPT or not (PREEMPT_START <= step < PREEMPT_STOP):
        return action
    state = _shift_state(obs, step)
    if state.get("due") or step - int(state.get("last_preempt", -10 ** 9)) < PREEMPT_COOLDOWN:
        return action
    if _clone_distance(obs) > PREEMPT_MAX_CLONE_DISTANCE:
        return action
    future_base = _future_base_sells(step)
    if not future_base:
        return action
    hazards = {row[0]: row for row in _HAZARD.get(str(step + 1), [])
               if row[0] in _PREMIUM and float(row[1]) >= PREEMPT_THRESHOLD}
    if not hazards:
        return action

    market = list(action.get("market") or [])
    remaining = _remaining_shed(obs, action)
    shifted = {}
    for item in _PREMIUM:
        row = hazards.get(item)
        if row is None:
            continue
        target = min(max(0, int(remaining.get(item, 0) or 0)),
                     max(0, int(future_base.get(item, 0) or 0)),
                     PREEMPT_MAX_BATCH,
                     max(1, int(round(float(row[2]) * PREEMPT_FRACTION))))
        if target <= 0:
            continue
        existing = next((index for index, order in enumerate(market)
                         if len(order) >= 3 and order[0] == "SELL" and order[1] == item),
                        None)
        if existing is not None:
            market[existing][2] = int(market[existing][2]) + target
        elif len(market) < 10:
            # Target is the opponent's NEXT-turn sale, so this order does not
            # need to jump our own same-turn orders.  Appending preserves the
            # route's same-turn priority; prepending reverses the gain.
            market.append(["SELL", item, target])
        else:
            continue
        remaining[item] = max(0, int(remaining.get(item, 0) or 0) - target)
        shifted[item] = target
    if shifted:
        action["market"] = market[:10]
        state["due_step"] = step + 1
        state["due"] = shifted
        state["last_preempt"] = step
    return action
''' % ("\n".join("    '%s'" % line
                 for line in textwrap.wrap(HAZARD_BLOB, 100)))

OLD_AGENT = """        action = _idle_fill(obs, action)
        action = _impact_slots(obs, action)"""

NEW_AGENT = """        action = _idle_fill(obs, action)
        action = _repay_shift(obs, action, step)
        action = _safe_market(obs, action)
        action = _preempt_shift(obs, action, step)
        action = _safe_market(obs, action)
        action = _impact_slots(obs, action)"""


def build(tape_path, out_path, note=""):
    overlay = _mkv24.OVERLAY
    assert OLD_AGENT in overlay, "v24 agent body changed - re-check the splice"
    index = overlay.index("def agent(obs):")
    overlay = overlay[:index] + PREEMPT.strip() + "\n\n\n" + overlay[index:]
    overlay = overlay.replace(OLD_AGENT, NEW_AGENT, 1)

    with open(tape_path, "rb") as handle:
        tape = json.loads(zlib.decompress(handle.read()).decode("utf-8"))
    blob = base64.b64encode(
        zlib.compress(json.dumps(tape, separators=(",", ":")).encode(), 9)
    ).decode()
    literal = "\n".join("    '%s'" % line for line in textwrap.wrap(blob, 100))

    header = '''"""%s"""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
%s
    )
)))

''' % (note or "Fresh route + tape-safe overlay + premium preemption.", literal)

    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(header + overlay)
    return len(tape)


if __name__ == "__main__":
    steps = build(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "")
    print(f"{sys.argv[2]}: {steps} steps")
