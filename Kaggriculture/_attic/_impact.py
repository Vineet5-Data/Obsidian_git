"""Self-calibrating order size: never walk your own price down by more than tol.

v28 (fixed 4-unit cap on premium goods) gained +726 against Seb and then scored
6.6% on the full panel -- I tuned one opponent over 8 seeds and overfit, exactly
the trap the earlier wheat-barbell build fell into.  So this harness scores FOUR
opponents at once, and nothing gets baked until the panel agrees.

The diagnosis behind the fixed cap was still right: strawberry is the same
volume as the rival's at 22% worse price, -$9,081, because a 22-unit block walks
its own price down under per-unit lockstep settlement.  What was wrong was the
CONSTANT.  A flat 4-unit cap delays cash unconditionally, and cash delay is the
one direction this tape reliably punishes.

So size the order off the price function instead:

    n = max k such that  p(I) - p(I+k) <= tol * p(I)

which is large where the book is deep and small where it is thin -- at $120
strawberry, 5% is 3-4 units; at $25 wheat with its $4-per-100-units slope it is
30+.  Self-calibrating across items AND across regimes, since it reads the live
price curve rather than a tuned constant, and it stops binding entirely once a
sale is small enough to be harmless.

Usage:  python _impact.py [n_seeds]
"""
import importlib.util
import multiprocessing as mp
import os
import statistics
import sys

BASE = "v27.py"

PANEL = [
    (".loss/o_90729118.py", "mirror"),
    (".field/f_90639963_p1.py", "Seb"),
    (".loss/o_90711580.py", "family B"),
    ("wufang_agent.py", "Wufang"),
]

# Splitting improves Seb monotonically and damages the mirror/Wufang
# monotonically, so it is CONDITIONAL, not wrong: it pays only when a rival is
# also loading the same book.  Gate it on that, two ways.
#   rival -- estimated rival supply of the item is positive.  Exactly
#            identified: delta_inventory = our_sales + rival_sales - drain, and
#            we know our own sales, so (delta + ours) tracks rival supply up to
#            a per-item drain constant.
#   price -- the item trades below its own EWMA, i.e. the book is already loaded.
#            Needs no rival model at all and re-calibrates under any reprice.
PRESETS = {
    "off":        None,
    "tol20":      {"tol": 0.20},
    "adapt_rival": {"tol": 0.20, "gate": "rival"},
    "adapt_price": {"tol": 0.20, "gate": "price"},
    "adapt_r10":   {"tol": 0.10, "gate": "rival"},
    "adapt_p10":   {"tol": 0.10, "gate": "price"},
}


def fresh(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def capped(preset, tag):
    module = fresh(BASE, "im_" + tag)
    P = PRESETS[preset]
    if P is None:
        return module.agent
    inner = module._smooth_sells
    tol = P["tol"]
    state = {0: {}, 1: {}}

    def allowed(item, inventory, want):
        """Largest k <= want whose walkdown stays inside tol."""
        price = module._market_price(item, inventory)
        if price <= 0:
            return want
        budget = tol * price
        low, high = 1, want
        if price - module._market_price(item, inventory + want) <= budget:
            return want
        while low < high:                       # monotone in k -> bisect
            mid = (low + high + 1) // 2
            if price - module._market_price(item, inventory + mid) <= budget:
                low = mid
            else:
                high = mid - 1
        return max(1, low)

    def gate_open(item, st, inventory):
        if not P.get("gate"):
            return True
        if P["gate"] == "rival":
            return st.get("rival", {}).get(item, 0.0) > 0.0
        ewma = st.get("pewma", {}).get(item)
        price = module._market_price(item, inventory.get(item, 10000))
        return ewma is not None and price < ewma

    def smooth(obs, action):
        action = inner(obs, action)
        try:
            seat = module._seat(obs)
            step = int(module._get(obs, "step", 0) or 0)
            st = state[seat]
            if step <= 0 or step < st.get("last", -1):
                st.clear()
            st["last"] = step
            queue = st.setdefault("queue", [])
            if step < module.SMOOTH_START:
                return action

            orders = [list(o) for o in (action.get("market") or [])]
            sells = [o for o in orders if o and o[0] == "SELL" and len(o) >= 3]
            others = [o for o in orders if not (o and o[0] == "SELL")]

            if step >= len(module._ACTIONS) - module.SMOOTH_FLUSH:
                st["queue"] = []
                merged = {}
                for order in queue + sells:
                    merged[order[1]] = merged.get(order[1], 0) + int(order[2])
                action["market"] = ([["SELL", k, v] for k, v in merged.items()]
                                    + others)[:10]
                return action

            inventory = {k: int(v or 0) for k, v in dict(module._get(
                module._get(obs, "market", {}) or {}, "inventory", {}) or {}).items()}

            # rival supply estimate and price EWMA, both from public data
            previous, ours = st.get("inv"), st.get("ours", {})
            rival = st.setdefault("rival", {})
            pewma = st.setdefault("pewma", {})
            for item, now in inventory.items():
                if previous is not None:
                    delta = now - previous.get(item, now) + ours.get(item, 0)
                    rival[item] = 0.15 * delta + 0.85 * rival.get(item, 0.0)
                price = module._market_price(item, now)
                pewma[item] = (price if item not in pewma
                               else 0.02 * price + 0.98 * pewma[item])
            st["inv"] = inventory
            room = max(0, 10 - len(others))
            emit, leftover = [], []
            for order in queue + sells:
                item, want = order[1], int(order[2])
                if len(emit) >= room:
                    leftover.append(order)
                    continue
                have = inventory.get(item, 10000)
                take = (allowed(item, have, want)
                        if gate_open(item, st, inventory) else want)
                emit.append(["SELL", item, take])
                inventory[item] = have + take
                if want - take > 0:
                    leftover.append(["SELL", item, want - take])
            st["queue"] = leftover[:60]
            action["market"] = (emit + others)[:10]
            st["ours"] = {}
            for order in action["market"]:
                if order and order[0] == "SELL" and len(order) >= 3:
                    st["ours"][order[1]] = st["ours"].get(order[1], 0) + int(order[2])
        except Exception:
            pass
        return action

    module._smooth_sells = smooth
    return module.agent


def one(job):
    preset, opponent_path, seed, seat = job
    from kaggle_environments import make
    tag = f"{preset}_{seed}_{seat}_{os.getpid()}"
    agent = capped(preset, tag)
    rival = fresh(opponent_path, "riv_" + tag).agent
    pair = [agent, rival] if seat == 0 else [rival, agent]
    env = make("kaggriculture",
               configuration={"episodeSteps": 720, "seed": seed})
    env.run(pair)
    final = env.steps[-1]
    return (preset, opponent_path), final[seat].reward - final[1 - seat].reward


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, n + 1)]
    jobs = [(p, path, s, seat)
            for p in PRESETS for path, _ in PANEL if os.path.exists(path)
            for s in seeds for seat in (0, 1)]
    with mp.Pool(max(1, (os.cpu_count() or 4) - 2)) as pool:
        results = pool.map(one, jobs)

    table = {}
    for key, margin in results:
        table.setdefault(key, []).append(margin)
    print(f"impact-budgeted order size -- {len(PANEL)} opponents x {n} seeds "
          f"x 2 seats\n")
    header = "".join(f"{label:>12s}" for _, label in PANEL)
    print(f"{'preset':10s}{header}{'OVERALL':>12s}{'win%':>8s}")
    for preset in PRESETS:
        cells, grand = [], []
        for path, _ in PANEL:
            margins = table.get((preset, path), [])
            grand += margins
            cells.append(f"{statistics.mean(margins):>+12,.0f}" if margins
                         else f"{'-':>12s}")
        w = sum(1 for m in grand if m > 0)
        tag = "  <= control (v27)" if preset == "off" else ""
        print(f"{preset:10s}{''.join(cells)}{statistics.mean(grand):>+12,.0f}"
              f"{100 * w / len(grand):>7.1f}%{tag}")


if __name__ == "__main__":
    mp.freeze_support()
    main()
