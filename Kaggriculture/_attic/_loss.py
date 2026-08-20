"""Diagnose the recent ladder losses: who beat us, where the money diverged.

Each replay is ~30MB, so nothing gets held in memory longer than one episode.
"""
import collections
import glob
import json
import os

LOSSES = r"C:\Users\Vinee\Desktop\Kaggriculture\recent _loss"
OURS = {55321810, 55316682, 55311135}  # v24, v13, v6


def money_curve(steps, seat):
    """Bank balance per step for one seat."""
    out = []
    for state in steps:
        obs = state[0].get("observation", {})
        farms = obs.get("farms") or []
        if len(farms) > seat:
            out.append(farms[seat].get("money", 0))
    return out


def fingerprint(steps, seat):
    """What the opponent actually built and sold."""
    hires = land = 0
    planted = collections.Counter()
    animals = collections.Counter()
    sold = collections.Counter()
    revenue = collections.Counter()
    first_land = first_animal = None
    for index, state in enumerate(steps[1:], start=0):
        action = state[seat].get("action") or {}
        prev = steps[index][0].get("observation", {})
        prices = (prev.get("market") or {}).get("prices") or {}
        for order in (action.get("market") or []):
            if not order:
                continue
            op = order[0]
            if op == "HIRE":
                hires += 1
            elif op == "BUY_LAND":
                land += 1
                if first_land is None:
                    first_land = index
            elif op == "BUY_ANIMAL" and len(order) >= 3:
                animals[order[1]] += int(order[2])
                if first_animal is None:
                    first_animal = index
            elif op == "SELL" and len(order) >= 3:
                sold[order[1]] += int(order[2])
                revenue[order[1]] += int(order[2]) * int(prices.get(order[1], 0) or 0)
        for unit in [action.get("farmer")] + list(action.get("hands") or []):
            if unit and unit[0] == "PLANT" and len(unit) >= 2:
                planted[unit[1]] += 1
    return {
        "hires": hires, "land": land, "first_land": first_land,
        "first_animal": first_animal,
        "planted": dict(planted), "animals": dict(animals),
        "sold": dict(sold), "revenue": dict(revenue),
    }


def main():
    for path in sorted(glob.glob(os.path.join(LOSSES, "*.json"))):
        with open(path, encoding="utf-8") as handle:
            replay = json.load(handle)
        steps = replay["steps"]
        info = replay.get("info") or {}
        names = [t.get("teamName", "?") for t in (info.get("TeamNames") and
                 [{"teamName": n} for n in info["TeamNames"]] or [])]
        final = steps[-1]
        rewards = [s.get("reward") for s in final]
        # Which seat is ours?  The replay's info has submission ids per agent.
        seat = None
        for i, s in enumerate(replay.get("rewards") or []):
            pass
        subs = info.get("SubmissionIds") or []
        for i, sid in enumerate(subs):
            if sid in OURS:
                seat = i
        if seat is None:
            # fall back: lower reward is presumed ours (these are losses)
            seat = 0 if (rewards[0] or 0) < (rewards[1] or 0) else 1
        opp = 1 - seat

        print("=" * 74)
        print(f"episode {os.path.basename(path)}  steps={len(steps)}")
        print(f"  teams={names}  subs={subs}  seat={seat}")
        print(f"  ME  reward={rewards[seat]:,}   OPP reward={rewards[opp]:,}"
              f"   margin={(rewards[seat] or 0) - (rewards[opp] or 0):+,}")

        mine = money_curve(steps, seat)
        theirs = money_curve(steps, opp)
        # where did the lead flip for good?
        flip = None
        for i in range(len(mine) - 1, 0, -1):
            if mine[i] >= theirs[i]:
                flip = i
                break
        print(f"  last step we led: {flip} (day {flip // 24 if flip else '-'})")
        print("  bank by day:  day: me / opp / delta")
        for day in range(0, 30, 3):
            i = min(day * 24, len(mine) - 1)
            print(f"    d{day:02d} {mine[i]:>8,} / {theirs[i]:>8,} "
                  f"/ {mine[i] - theirs[i]:>+8,}")

        f_me = fingerprint(steps, seat)
        f_op = fingerprint(steps, opp)
        print("  --- build ---")
        for key in ("hires", "land", "first_land", "first_animal",
                    "planted", "animals"):
            print(f"    {key:14s} me={f_me[key]}   opp={f_op[key]}")
        print("  --- sales (qty | revenue) ---")
        items = sorted(set(f_me["sold"]) | set(f_op["sold"]))
        for item in items:
            print(f"    {item:12s} me={f_me['sold'].get(item,0):>5} "
                  f"|{f_me['revenue'].get(item,0):>9,}   "
                  f"opp={f_op['sold'].get(item,0):>5} "
                  f"|{f_op['revenue'].get(item,0):>9,}")
        print(f"    {'TOTAL':12s} me={sum(f_me['revenue'].values()):>15,}   "
              f"opp={sum(f_op['revenue'].values()):>15,}")


if __name__ == "__main__":
    main()
