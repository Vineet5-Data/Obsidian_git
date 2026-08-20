"""What do top players BUY, and do they resell it?

Distinguishes two hypotheses for their 4.3x BUY_PRODUCT rate:
  (a) feed  -- buys are overwhelmingly WHEAT, consumed by animals
  (b) arbitrage -- buys spread across goods they later SELL at a higher price

For (b) the tell is buying a good the farm also sells, and buying it when the
market inventory is high (price low) while selling when inventory is low.
"""
import glob
import json
import os
from collections import Counter


def analyse(path):
    with open(path, encoding="utf-8") as fh:
        rep = json.load(fh)
    steps = rep.get("steps") or []
    if not steps:
        return None
    final = steps[-1]
    rewards = [(final[s].get("reward") or 0) for s in range(len(final))]
    seat = rewards.index(max(rewards))

    bought, sold = Counter(), Counter()
    buy_inv, sell_inv = {}, {}          # market inventory at trade time
    for i, st in enumerate(steps[1:], 1):
        a = (st[seat].get("action") or {}) if seat < len(st) else {}
        if not isinstance(a, dict):
            continue
        prev = steps[i - 1][0]["observation"]["market"]["inventory"]
        for o in (a.get("market") or []):
            if not o:
                continue
            if o[0] == "BUY_PRODUCT":
                item, qty = o[1], int(o[2])
                bought[item] += qty
                buy_inv.setdefault(item, []).append(prev.get(item, 0))
            elif o[0] == "SELL":
                item, qty = o[1], int(o[2])
                sold[item] += qty
                sell_inv.setdefault(item, []).append(prev.get(item, 0))
    return rewards[seat], bought, sold, buy_inv, sell_inv


if __name__ == "__main__":
    tot_b, tot_s = Counter(), Counter()
    binv, sinv = {}, {}
    for path in sorted(glob.glob("Top_fresh-21/*.json")):
        r = analyse(path)
        if not r:
            continue
        score, b, s, bi, si = r
        tot_b.update(b)
        tot_s.update(s)
        for k, v in bi.items():
            binv.setdefault(k, []).extend(v)
        for k, v in si.items():
            sinv.setdefault(k, []).extend(v)
        print(f"{os.path.basename(path):16} {score:>9,.0f}  "
              f"buys={dict(b.most_common(4))}")

    print("\nTOTAL bought:", dict(tot_b.most_common()))
    print("TOTAL sold  :", dict(tot_s.most_common()))
    print(f"\n{'item':<14}{'bought':>9}{'sold':>9}{'avg inv@buy':>14}{'avg inv@sell':>14}")
    for item in sorted(set(tot_b) | set(tot_s), key=lambda k: -tot_b.get(k, 0)):
        b = tot_b.get(item, 0)
        s = tot_s.get(item, 0)
        ab = sum(binv.get(item, [])) / len(binv[item]) if binv.get(item) else float("nan")
        as_ = sum(sinv.get(item, [])) / len(sinv[item]) if sinv.get(item) else float("nan")
        print(f"{item:<14}{b:>9,}{s:>9,}{ab:>14,.0f}{as_:>14,.0f}")
    print("\nHigher inv@buy than inv@sell => bought cheap, sold dear (arbitrage).")
