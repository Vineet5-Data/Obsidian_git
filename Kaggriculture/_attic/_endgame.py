"""Where exactly do the last six days bleed?

Per-day revenue by item for both seats, plus what each side was doing with its
units, for the endgame window only.
"""
import collections
import glob
import json
import os
import sys

LOSSES = r"C:\Users\Vinee\Desktop\Kaggriculture\recent _loss"
START_DAY = 22


def analyse(path):
    with open(path, encoding="utf-8") as handle:
        replay = json.load(handle)
    steps = replay["steps"]
    names = (replay.get("info") or {}).get("TeamNames") or ["p0", "p1"]
    seat = 0 if "vineet" in names[0].lower() else 1
    opp = 1 - seat

    rev = {seat: collections.defaultdict(collections.Counter),
           opp: collections.defaultdict(collections.Counter)}
    qty = {seat: collections.defaultdict(collections.Counter),
           opp: collections.defaultdict(collections.Counter)}
    ops = {seat: collections.Counter(), opp: collections.Counter()}
    idle = {seat: 0, opp: 0}
    unit_turns = {seat: 0, opp: 0}

    for index, state in enumerate(steps[1:], start=0):
        day = index // 24
        prev = steps[index][0].get("observation", {})
        prices = (prev.get("market") or {}).get("prices") or {}
        for who in (seat, opp):
            action = state[who].get("action") or {}
            for order in (action.get("market") or []):
                if order and order[0] == "SELL" and len(order) >= 3:
                    item, n = order[1], int(order[2])
                    rev[who][day][item] += n * int(prices.get(item, 0) or 0)
                    qty[who][day][item] += n
            if day >= START_DAY:
                units = [action.get("farmer")] + list(action.get("hands") or [])
                for unit in units:
                    unit_turns[who] += 1
                    op = unit[0] if unit else "PASS"
                    ops[who][op] += 1
                    if op == "PASS":
                        idle[who] += 1
    return names, seat, opp, rev, qty, ops, idle, unit_turns


def main():
    for path in sorted(glob.glob(os.path.join(LOSSES, "*.json"))):
        names, seat, opp, rev, qty, ops, idle, unit_turns = analyse(path)
        print("=" * 78)
        print(f"{os.path.basename(path)}   me=seat{seat} ({names[seat]})  "
              f"opp={names[opp]}")
        print(f"  {'day':>4} {'me rev':>9} {'opp rev':>9} {'delta':>8}   "
              f"top item diffs (opp-me qty)")
        cum = 0
        for day in range(START_DAY, 30):
            m = sum(rev[seat][day].values())
            o = sum(rev[opp][day].values())
            cum += o - m
            diffs = collections.Counter()
            for item in set(qty[seat][day]) | set(qty[opp][day]):
                d = qty[opp][day][item] - qty[seat][day][item]
                if d:
                    diffs[item] = d
            top = "  ".join(f"{k}{v:+d}" for k, v in
                            sorted(diffs.items(), key=lambda kv: -abs(kv[1]))[:4])
            print(f"  d{day:02d} {m:>9,} {o:>9,} {o - m:>+8,}   {top}")
        print(f"  cumulative endgame revenue gap (opp-me): {cum:+,}")
        print(f"  --- unit ops, days {START_DAY}-29 ---")
        print(f"  idle PASS:  me {idle[seat]:>5}/{unit_turns[seat]}  "
              f"({100*idle[seat]/max(1,unit_turns[seat]):.1f}%)   "
              f"opp {idle[opp]:>5}/{unit_turns[opp]} "
              f"({100*idle[opp]/max(1,unit_turns[opp]):.1f}%)")
        allops = set(ops[seat]) | set(ops[opp])
        rows = sorted(allops, key=lambda k: -abs(ops[opp][k] - ops[seat][k]))
        for op in rows[:8]:
            d = ops[opp][op] - ops[seat][op]
            if d:
                print(f"    {op:20s} me={ops[seat][op]:>5} opp={ops[opp][op]:>5}"
                      f"  {d:+d}")


if __name__ == "__main__":
    main()
