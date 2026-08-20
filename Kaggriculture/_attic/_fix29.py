"""Close v29's last losing matchup (family B) without breaking the other five.

v29 is 97.2% on 6 seeds / 72 games, 93.1% on the 24-seed panel.  Every remaining
loss is family B and every one is narrow (worst -457 here, -2,754 on the wide
panel).  Re-tuning SMOOTH_START does nothing -- 200/250/266/300 are identical --
so the gate is not the lever.

These are the execution layers that LOST on v27's route.  That verdict does not
automatically carry: v29 out-produces v27 by ~60k and its realised revenue mix
is different, so the price-impact arithmetic that made splitting unprofitable
there may invert here.  Scored per-opponent on all six, counting LOSSES rather
than mean, because a mean carrying a +170k rout against Seb would hide exactly
the two games that matter.

Usage:  python _fix29.py [n_seeds]
"""
import importlib.util
import multiprocessing as mp
import os
import statistics
import sys

BASE = "v29.py"

PANEL = [(".loss/o_90711580.py", "familyB"),
         (".field/f_90635979_p1.py", "Khanh"),
         (".field/f_90635229_p1.py", "Youssef"),
         (".loss/o_90729118.py", "mirror"),
         (".field/f_90639963_p1.py", "Seb"),
         ("wufang_agent.py", "Wufang")]

PRESETS = {
    "off":       None,
    "tol20":     {"kind": "impact", "tol": 0.20},
    "tol35":     {"kind": "impact", "tol": 0.35},
    "cap8":      {"kind": "split", "cap": 8},
    "cap12":     {"kind": "split", "cap": 12},
    "flush16":   {"kind": "flush", "n": 16},
    "flush4":    {"kind": "flush", "n": 4},
}


def fresh(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def variant(preset, tag):
    module = fresh(BASE, "f_" + tag)
    P = PRESETS[preset]
    if P is None:
        return module.agent
    if P["kind"] == "flush":
        module.SMOOTH_FLUSH = P["n"]
        return module.agent

    inner = module._smooth_sells
    state = {0: {}, 1: {}}
    premium = ("STRAWBERRY", "MILK", "WOOL", "MELON")

    def allowed(item, inventory, want):
        price = module._market_price(item, inventory)
        if price <= 0:
            return want
        budget = P["tol"] * price
        if price - module._market_price(item, inventory + want) <= budget:
            return want
        low, high = 1, want
        while low < high:
            mid = (low + high + 1) // 2
            if price - module._market_price(item, inventory + mid) <= budget:
                low = mid
            else:
                high = mid - 1
        return max(1, low)

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
                for o in queue + sells:
                    merged[o[1]] = merged.get(o[1], 0) + int(o[2])
                action["market"] = ([["SELL", k, v] for k, v in merged.items()]
                                    + others)[:10]
                return action

            inv = {k: int(v or 0) for k, v in dict(module._get(module._get(
                obs, "market", {}) or {}, "inventory", {}) or {}).items()}
            room = max(0, 10 - len(others))
            emit, leftover = [], []
            for o in queue + sells:
                item, want = o[1], int(o[2])
                if len(emit) >= room:
                    leftover.append(o)
                    continue
                if P["kind"] == "impact":
                    take = allowed(item, inv.get(item, 10000), want)
                elif item in premium:
                    take = min(want, P["cap"])
                else:
                    take = want
                emit.append(["SELL", item, take])
                inv[item] = inv.get(item, 10000) + take
                if want - take > 0:
                    leftover.append(["SELL", item, want - take])
            st["queue"] = leftover[:60]
            action["market"] = (emit + others)[:10]
        except Exception:
            pass
        return action

    module._smooth_sells = smooth
    return module.agent


def one(job):
    preset, path, seed, seat = job
    from kaggle_environments import make
    tag = f"{preset}_{seed}_{seat}_{os.getpid()}"
    a = variant(preset, tag)
    b = fresh(path, "o_" + tag).agent
    env = make("kaggriculture",
               configuration={"episodeSteps": 720, "seed": seed})
    env.run([a, b] if seat == 0 else [b, a])
    final = env.steps[-1]
    return (preset, path), final[seat].reward - final[1 - seat].reward


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, n + 1)]
    jobs = [(p, path, s, seat) for p in PRESETS for path, _ in PANEL
            if os.path.exists(path) for s in seeds for seat in (0, 1)]
    with mp.Pool(max(1, (os.cpu_count() or 4) - 2)) as pool:
        results = pool.map(one, jobs)

    table = {}
    for key, margin in results:
        table.setdefault(key, []).append(margin)
    print(f"v29 last-mile -- {len(PANEL)} opponents x {n} seeds x 2 seats\n")
    print(f"{'preset':10s}" + "".join(f"{l:>10s}" for _, l in PANEL)
          + f"{'LOSSES':>8s}{'win%':>8s}{'worst':>10s}")
    for preset in PRESETS:
        cells, grand = [], []
        for path, _ in PANEL:
            margins = table.get((preset, path), [])
            grand += margins
            cells.append(f"{sum(1 for m in margins if m <= 0)}/{len(margins)}"
                         .rjust(10) if margins else "-".rjust(10))
        losses = sum(1 for m in grand if m <= 0)
        tag = "  <= shipped" if preset == "off" else ""
        print(f"{preset:10s}" + "".join(cells)
              + f"{losses:>8d}{100 * (len(grand) - losses) / len(grand):>7.1f}%"
              + f"{min(grand):>+10,.0f}{tag}")


if __name__ == "__main__":
    mp.freeze_support()
    main()
