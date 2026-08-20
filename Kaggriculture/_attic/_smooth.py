"""Sell-schedule smoothing: the rule read out of the mirror, as a function.

WHAT THE MIRROR ACTUALLY DOES.  .loss/o_90729118.py is our own family-A route --
farmer and hands channels byte-identical over all 719 shared steps -- with 68
market-channel differences worth +1,258 of the +1,327 deficit.  Every carrying
edit is the same move: v26 bunches many SELLs into one turn, the mirror spreads
the same volume over adjacent turns.

WHY IT PAYS.  Settlement is a per-unit lockstep loop, so unit k of a SELL is
priced against inventory already raised by units 1..k-1: a bunched sale walks
its own price down.  Between turns the shops (every 4 steps) and the town centre
(every 12) drain inventory back.  Same goods over more turns = higher average
realised price.

WHY IT IS NOT CLONING.  The rule references no price, no base, no amplitude and
no opponent -- only the pending sell queue and turn occupancy.  It holds in any
regime where price decreases in inventory and drain is positive, which the glut
table says is every product.  A copied tape cell would not survive a reprice;
this does.

Two phase directions, because they are not equivalent under a cash-saturated
tape (adding purchases is silently rejected, removing them cascades: measured
-35,572 in the evolve run):
  advance -- pull a future sell into a spare slot now, gated on the observed
             shed so we never sell goods we do not hold.  Cash arrives EARLIER.
  defer   -- push the surplus beyond the cap into later turns.  Cash arrives
             LATER, which is the direction that risks the cascade.

Usage:  python _smooth.py [opponent.py] [n_seeds]
"""
import importlib.util
import multiprocessing as mp
import os
import statistics
import sys

BASE = "v26.py"
MAX_ORDERS = 10

PRESETS = {
    "off":      None,
    "s100_w8":  {"mode": "advance", "cap": 5, "window": 8, "start": 100},
    "s200_w8":  {"mode": "advance", "cap": 5, "window": 8, "start": 200},
    "s250_w8":  {"mode": "advance", "cap": 5, "window": 8, "start": 250},
    "s300_w8":  {"mode": "advance", "cap": 5, "window": 8, "start": 300},
    "s400_w8":  {"mode": "advance", "cap": 5, "window": 8, "start": 400},
}

REGIMES = {
    "baseline": {},
    "premium_bear": {"STRAWBERRY": {"base": 72}, "MILK": {"base": 96},
                     "WOOL": {"base": 120}, "MELON": {"base": 150}},
}


def fresh(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def smoothed(preset, tag):
    module = fresh(BASE, "s_" + tag)
    inner = module.agent
    tape = module._ACTIONS
    P = PRESETS[preset]
    state = {}

    def tape_sells(step):
        if not 0 <= step < len(tape):
            return []
        return [list(o) for o in (tape[step].get("market") or [])
                if o and o[0] == "SELL" and len(o) >= 3]

    def agent(obs):
        action = inner(obs)
        if P is None:
            return action
        try:
            seat = module._seat(obs)
            step = int(module._get(obs, "step", 0) or 0)
            st = state.get(seat)
            if st is None or step <= 0 or step < st["last"]:
                st = {"last": step, "taken": set(), "queue": []}
                state[seat] = st
            st["last"] = step

            orders = [list(o) for o in (action.get("market") or [])]
            sells = [o for o in orders if o and o[0] == "SELL" and len(o) >= 3]
            others = [o for o in orders if not (o and o[0] == "SELL")]

            # goods already pulled forward must not be sold twice
            for key in list(st["taken"]):
                pulled_step, item, qty = key
                if pulled_step != step:
                    continue
                for i, o in enumerate(sells):
                    if o[1] == item and int(o[2]) == qty:
                        sells.pop(i)
                        st["taken"].discard(key)
                        break

            # the last turns must flush: goods unsold at 719 are worth nothing
            if step >= len(tape) - 8:
                action["market"] = (sells + st["queue"] + others)[:MAX_ORDERS]
                st["queue"] = []
                return action

            if step < P.get("start", 0):
                return action

            if P["mode"] == "defer":
                keep, spill = sells[:P["cap"]], sells[P["cap"]:]
                room = MAX_ORDERS - len(keep) - len(others)
                emit = st["queue"][:max(0, min(room, P["cap"] - len(keep)))]
                st["queue"] = st["queue"][len(emit):] + spill
                action["market"] = (keep + emit + others)[:MAX_ORDERS]
                return action

            # advance: only what the shed verifiably holds.  The observation's
            # shed predates this turn's DROP, so it is a conservative floor.
            shed = {k: max(0, int(v or 0)) for k, v in dict(module._get(
                module._get(obs, "private", {}) or {}, "shed", {}) or {}).items()}
            for o in sells:
                shed[o[1]] = shed.get(o[1], 0) - int(o[2])
            free = MAX_ORDERS - len(sells) - len(others)
            slack = P["cap"] - len(sells)
            for ahead in range(step + 1, step + 1 + P["window"]):
                if free <= 0 or slack <= 0:
                    break
                for o in tape_sells(ahead):
                    key = (ahead, o[1], int(o[2]))
                    if key in st["taken"] or shed.get(o[1], 0) < int(o[2]):
                        continue
                    sells.append(o)
                    shed[o[1]] -= int(o[2])
                    st["taken"].add(key)
                    free -= 1
                    slack -= 1
                    if free <= 0 or slack <= 0:
                        break
            action["market"] = (sells + others)[:MAX_ORDERS]
        except Exception:
            pass
        return action

    return agent


def one(job):
    preset, regime, opponent_path, seed, seat = job
    from kaggle_environments import make
    tag = f"{preset}_{seed}_{seat}_{os.getpid()}"
    agent = smoothed(preset, tag)
    rival = fresh(opponent_path, "riv_" + tag).agent
    pair = [agent, rival] if seat == 0 else [rival, agent]
    env = make("kaggriculture",
               configuration={"episodeSteps": 720, "seed": seed,
                              "marketParams": REGIMES[regime]})
    env.run(pair)
    final = env.steps[-1]
    return (preset, regime), final[seat].reward - final[1 - seat].reward


def main():
    opponent = sys.argv[1] if len(sys.argv) > 1 else ".loss/o_90729118.py"
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, n + 1)]
    jobs = [(p, r, opponent, s, seat)
            for r in REGIMES for p in PRESETS for s in seeds for seat in (0, 1)]
    with mp.Pool(max(1, (os.cpu_count() or 4) - 2)) as pool:
        results = pool.map(one, jobs)

    table = {}
    for key, margin in results:
        table.setdefault(key, []).append(margin)
    print(f"sell smoothing vs {os.path.basename(opponent)} "
          f"({n} seeds x 2 seats)\n")
    print(f"{'preset':12s} {'W-L':>8} {'win%':>6} {'mean':>9} "
          f"{'worst':>9} {'best':>9}")
    for regime in REGIMES:
      print(f"-- {regime} --")
      for preset in PRESETS:
        margins = table.get((preset, regime), [])
        if not margins:
            continue
        w = sum(1 for m in margins if m > 0)
        tag = "  <= control" if preset == "off" else ""
        print(f"{preset:12s} {f'{w}-{len(margins) - w}':>8} "
              f"{100 * w / len(margins):>5.1f}% "
              f"{statistics.mean(margins):>+9,.0f} {min(margins):>+9,.0f} "
              f"{max(margins):>+9,.0f}{tag}")


if __name__ == "__main__":
    mp.freeze_support()
    main()
