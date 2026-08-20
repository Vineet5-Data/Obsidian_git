"""Sell on the drain clock, not on the tape's clock.

The engine's interpreter runs, in this order:

    917     _process_market(state, env)      # our SELLs settle
    918     _town_consume(env, state, step)  # shops (step%4==0) + town (step%12==0)

so a sale executed AT a drain step settles against the pre-drain, MAXIMUM
inventory.  The freshest book is at step%4 == 1, right after the pulse, and
best of all at step%12 == 1 where the shop and town-centre pulses coincide.

Our tape sells 927 of 1,281 units (72%) at step%4 == 0 -- the worst phase in the
cycle.  Both opponents that beat us sit near 14% in phase 1 against our 7.7%.

Two ways to fix the phase, and they are NOT equivalent under a cash-saturated
tape:
  advance -- pull a sale back to an earlier phase-1 step.  Cash arrives sooner;
             cannot starve a purchase.
  defer   -- push a phase-0 sale one step to phase 1.  Lands the phase exactly,
             but delays cash into turns that may hold HIREs (steps 600/648/672
             carry both), which is the -35,572 cascade direction.

Both are measured.  This is the refinement the execution literature points at:
under periodic (not exponential) resilience the optimal schedule is a TWAP
synchronised to the drain clock, not a block shape.

Usage:  python _phase.py [opponent.py] [n_seeds]
"""
import importlib.util
import multiprocessing as mp
import os
import statistics
import sys

BASE = "v27.py"

PRESETS = {
    "off":          None,
    "adv_p1_k5":    {"mode": "advance", "cap": 5,  "window": 8},
    "adv_p1_k8":    {"mode": "advance", "cap": 8,  "window": 8},
    "adv_p1_k10w12": {"mode": "advance", "cap": 10, "window": 12},
    "adv_p1_k10w16": {"mode": "advance", "cap": 10, "window": 16},
    "defer1":       {"mode": "defer"},
    "defer1_safe":  {"mode": "defer", "safe": 1},   # never delay a buying turn
}


def fresh(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def phased(preset, tag):
    module = fresh(BASE, "p_" + tag)
    P = PRESETS[preset]
    if P is None:
        return module.agent

    inner = module._smooth_sells
    state = {0: {}, 1: {}}

    if P["mode"] == "advance":
        module.SMOOTH_CAP = P["cap"]
        module.SMOOTH_WINDOW = P["window"]

        def smooth(obs, action):
            step = int(module._get(obs, "step", 0) or 0)
            # only let the advance loop fire on a post-drain turn, so everything
            # it pulls forward lands on the freshest book
            if step % 4 != 1:
                return action
            return inner(obs, action)
    else:
        def smooth(obs, action):
            action = inner(obs, action)
            try:
                seat = module._seat(obs)
                step = int(module._get(obs, "step", 0) or 0)
                st = state[seat]
                if step <= 0 or step < st.get("last", -1):
                    st.clear()
                st["last"] = step
                if step < module.SMOOTH_START or step >= len(module._ACTIONS) - 8:
                    return action

                orders = [list(o) for o in (action.get("market") or [])]
                sells = [o for o in orders if o and o[0] == "SELL" and len(o) >= 3]
                others = [o for o in orders if not (o and o[0] == "SELL")]
                held = st.setdefault("held", [])

                if step % 4 == 0 and sells:
                    if P.get("safe") and others:
                        return action          # turn buys something: do not delay
                    st["held"] = held + sells
                    action["market"] = others[:10]
                    return action
                if held:
                    room = 10 - len(sells) - len(others)
                    emit = held[:max(0, room)]
                    st["held"] = held[len(emit):]
                    action["market"] = (sells + emit + others)[:10]
            except Exception:
                pass
            return action

    module._smooth_sells = smooth
    return module.agent


def one(job):
    preset, opponent_path, seed, seat = job
    from kaggle_environments import make
    tag = f"{preset}_{seed}_{seat}_{os.getpid()}"
    agent = phased(preset, tag)
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
    print(f"drain-clock phasing vs {os.path.basename(opponent)} "
          f"({n} seeds x 2 seats)\n")
    print(f"{'preset':15s} {'W-L':>8} {'win%':>6} {'mean':>9} "
          f"{'worst':>9} {'best':>9}")
    for preset in PRESETS:
        margins = table.get(preset, [])
        if not margins:
            continue
        w = sum(1 for m in margins if m > 0)
        tag = "  <= control (v27)" if preset == "off" else ""
        print(f"{preset:15s} {f'{w}-{len(margins) - w}':>8} "
              f"{100 * w / len(margins):>5.1f}% "
              f"{statistics.mean(margins):>+9,.0f} {min(margins):>+9,.0f} "
              f"{max(margins):>+9,.0f}{tag}")


if __name__ == "__main__":
    mp.freeze_support()
    main()
