"""Summarise the six fresh v27 losses: seat, margin, money curve, opponent build."""
import collections, glob, json, os

for path in sorted(glob.glob("v27_losses/*.json")):
    with open(path, encoding="utf-8") as fh:
        rep = json.load(fh)
    steps = rep["steps"]
    final = steps[-1]
    rewards = [final[i].get("reward") for i in range(2)]
    # our agent is whichever seat used our tape; detect by matching step-0 market
    mkt0 = [(steps[1][i].get("action") or {}).get("market") for i in range(2)]
    n_hire = [sum(1 for o in (m or []) if o and o[0] == "HIRE") for m in mkt0]
    ours = 0 if rewards[0] is not None and rewards[1] is not None else 0
    # margin from our perspective for both seats, then pick the losing one
    print(f"\n=== {os.path.basename(path)}  steps={len(steps)} ===")
    print(f"    rewards p0={rewards[0]} p1={rewards[1]}  step0 HIREs p0={n_hire[0]} p1={n_hire[1]}")
    for seat in (0, 1):
        ops = collections.Counter(); sold = collections.Counter()
        hires = 0; animals = 0
        for i in range(len(steps) - 1):
            act = steps[i + 1][seat].get("action") or {}
            for o in (act.get("market") or []):
                if o[0] == "HIRE": hires += 1
                elif o[0] == "SELL" and len(o) >= 3: sold[o[1]] += int(o[2])
                elif o[0] == "BUY_ANIMAL": animals += int(o[2]) if len(o) > 2 else 1
            for u in [act.get("farmer")] + list(act.get("hands") or []):
                if u: ops[u[0]] += 1
        print(f"    seat{seat}: hires={hires:4d} animals={animals:3d} "
              f"sold={dict(sold.most_common(4))}")
