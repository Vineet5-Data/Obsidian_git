"""Cap sell VOLUME per item per turn.  The strawberry leak.

Measured live (seed 12345, v27 vs Seb), realized revenue per unit:

    STRAWBERRY   we sell 292 @ $108.4      he sells 286 @ $139.5
    MILK         we sell 213 @ $176.6      he sells 287 @ $184.2
    MELON        we sell 144 @ $142.7      he sells 138 @ $158.5

Strawberry is essentially the SAME volume at 22% worse price: -$9,081 of pure
execution loss, no production difference at all.

Why: strawberry moves $119 per 100 units (p=$120, so 100 units nearly floors
it), and settlement is per-unit lockstep -- our tape dumps 22 units in ONE turn
at step 648, walking its own price down the whole way.  Exogenous drain only
clears roughly one strawberry per step, so the book cannot absorb a 22-unit
block.  Seb averages ~5 units per order against our 8.2.

So the lever is order SIZE, not order count and not phase.  Splitting inside a
turn is provably useless (per-unit lockstep prices every unit off the same
running inventory) -- the split has to be ACROSS turns, so drain can refill
between the pieces.

This necessarily DELAYS some cash, which is the direction that has failed
before.  Two mitigations, both measured: it only runs after SMOOTH_START (the
step-168 BUY_LAND turn is long past), and the queue is flushed before the
episode ends so nothing dies unsold.

Usage:  python _split.py [opponent.py] [n_seeds]
"""
import importlib.util
import multiprocessing as mp
import os
import statistics
import sys

BASE = "v27.py"

PRESETS = {
    "off":      None,
    "v4":       {"cap": 4},
    "v6":       {"cap": 6},
    "v8":       {"cap": 8},
    "v10":      {"cap": 10},
    # illiquid goods only: wheat moves $4/100u, it does not need splitting
    "v6_prem":  {"cap": 6, "items": ("STRAWBERRY", "MILK", "WOOL", "MELON")},
    "v4_prem":  {"cap": 4, "items": ("STRAWBERRY", "MILK", "WOOL", "MELON")},
}


def fresh(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def splitter(preset, tag):
    module = fresh(BASE, "sp_" + tag)
    P = PRESETS[preset]
    if P is None:
        return module.agent
    inner = module._smooth_sells
    limit = P["cap"]
    items = set(P.get("items") or ())
    state = {0: {}, 1: {}}

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

            # last turns: dump everything, unsold goods score nothing
            if step >= len(module._ACTIONS) - 8:
                st["queue"] = []
                merged = {}
                for order in queue + sells:
                    merged[order[1]] = merged.get(order[1], 0) + int(order[2])
                action["market"] = ([["SELL", k, v] for k, v in merged.items()]
                                    + others)[:10]
                return action

            # No shed gate here: unlike the ADVANCE path, splitting only
            # re-times orders the tape already scheduled, so the goods exist.
            # The observation's shed predates this turn's DROP and gating on it
            # blocks every sale permanently -- that is what produced the -90k.
            room_slots = max(0, 10 - len(others))
            emit, sent, leftover = [], {}, []
            for order in queue + sells:
                item, want = order[1], int(order[2])
                if items and item not in items:
                    emit.append(order)
                    continue
                take = min(want, max(0, limit - sent.get(item, 0)))
                if take > 0 and len(emit) < room_slots:
                    emit.append(["SELL", item, take])
                    sent[item] = sent.get(item, 0) + take
                else:
                    take = 0
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
    preset, opponent_path, seed, seat = job
    from kaggle_environments import make
    tag = f"{preset}_{seed}_{seat}_{os.getpid()}"
    agent = splitter(preset, tag)
    rival = fresh(opponent_path, "riv_" + tag).agent
    pair = [agent, rival] if seat == 0 else [rival, agent]
    env = make("kaggriculture",
               configuration={"episodeSteps": 720, "seed": seed})
    env.run(pair)
    final = env.steps[-1]
    return preset, final[seat].reward - final[1 - seat].reward


def main():
    opponent = sys.argv[1] if len(sys.argv) > 1 else ".field/f_90639963_p1.py"
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, n + 1)]
    jobs = [(p, opponent, s, seat)
            for p in PRESETS for s in seeds for seat in (0, 1)]
    with mp.Pool(max(1, (os.cpu_count() or 4) - 2)) as pool:
        results = pool.map(one, jobs)

    table = {}
    for preset, margin in results:
        table.setdefault(preset, []).append(margin)
    print(f"per-item volume cap vs {os.path.basename(opponent)} "
          f"({n} seeds x 2 seats)\n")
    print(f"{'preset':10s} {'W-L':>8} {'win%':>6} {'mean':>9} "
          f"{'worst':>9} {'best':>9}")
    for preset in PRESETS:
        margins = table.get(preset, [])
        if not margins:
            continue
        w = sum(1 for m in margins if m > 0)
        tag = "  <= control (v27)" if preset == "off" else ""
        print(f"{preset:10s} {f'{w}-{len(margins) - w}':>8} "
              f"{100 * w / len(margins):>5.1f}% "
              f"{statistics.mean(margins):>+9,.0f} {min(margins):>+9,.0f} "
              f"{max(margins):>+9,.0f}{tag}")


if __name__ == "__main__":
    mp.freeze_support()
    main()
