"""Race or retreat?  Ordering the advance queue by observed rival supply.

v27 advances pending sells in tape order.  But against a rival who FLOODS one
good (Seb: 287 milk to my 213, and almost no wheat), tape order is arbitrary --
the question is whether to get into the contested good BEFORE his supply lands
(race) or to spend the scarce advance slots on the goods he ignores (retreat).

Rival supply is not a latent variable here, it is exactly identified:

    delta_inventory = our_sales + rival_sales - drain

We know our own sales and the market inventory is public, so a per-item EWMA of
(delta_inventory + our_sales) ranks which goods the rival is pushing.  No
instrument, no identification assumption -- only two sellers exist and the drain
is deterministic.  (Drain is not subtracted: it is a per-item constant offset
and we only need the RANKING across items.)

Both directions are tested because the theory is genuinely ambiguous: reward is
relative margin, so crashing a good the rival is concentrated in can pay even
when it costs us -- which argues race -- while price impact per unit argues
retreat.

Usage:  python _race.py [opponent.py] [n_seeds]
"""
import importlib.util
import multiprocessing as mp
import os
import statistics
import sys

BASE = "v27.py"
ALPHA = 0.15

PRESETS = {
    "off":        None,       # v27 as shipped: advance in tape order
    "race":       {"dir": -1, "slots": 0},
    "retreat":    {"dir": +1, "slots": 0},
    "race_slot":  {"dir": -1, "slots": 1},
    "retreat_slot": {"dir": +1, "slots": 1},
}


def fresh(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def raced(preset, tag):
    module = fresh(BASE, "r_" + tag)
    P = PRESETS[preset]
    if P is None:
        return module.agent

    inner_smooth = module._smooth_sells
    state = {0: {}, 1: {}}

    def pressure(obs, seat):
        """EWMA of per-item rival supply, from public inventory alone."""
        st = state[seat]
        market = module._get(obs, "market", {}) or {}
        inventory = {k: int(v or 0) for k, v in
                     dict(module._get(market, "inventory", {}) or {}).items()}
        previous = st.get("inv")
        ewma = st.setdefault("ewma", {})
        if previous:
            ours = st.get("ours", {})
            for item, now in inventory.items():
                delta = now - previous.get(item, now) + ours.get(item, 0)
                ewma[item] = (ALPHA * delta + (1 - ALPHA) * ewma.get(item, 0.0))
        st["inv"] = inventory
        return ewma

    def smooth(obs, action):
        try:
            seat = module._seat(obs)
            step = int(module._get(obs, "step", 0) or 0)
            if step <= 0 or step < state[seat].get("last", -1):
                state[seat].clear()
            state[seat]["last"] = step
            ewma = pressure(obs, seat)

            # rank the tape's upcoming sells so the advance loop meets the
            # contested (or uncontested) goods first
            window = module._ACTIONS[step + 1:step + 1 + module.SMOOTH_WINDOW]
            for entry in window:
                orders = entry.get("market") or []
                sells = [o for o in orders if o and o[0] == "SELL" and len(o) >= 3]
                if len(sells) > 1:
                    rest = [o for o in orders if not (o and o[0] == "SELL")]
                    sells.sort(key=lambda o: P["dir"] * ewma.get(o[1], 0.0))
                    entry["market"] = sells + rest

            action = inner_smooth(obs, action)

            if P["slots"]:
                orders = [list(o) for o in (action.get("market") or [])]
                sells = [o for o in orders if o and o[0] == "SELL" and len(o) >= 3]
                rest = [o for o in orders if not (o and o[0] == "SELL")]
                sells.sort(key=lambda o: P["dir"] * ewma.get(o[1], 0.0))
                action["market"] = (sells + rest)[:10]

            # remember what we are about to sell, for the next turn's estimate
            state[seat]["ours"] = {}
            for order in (action.get("market") or []):
                if order and order[0] == "SELL" and len(order) >= 3:
                    state[seat]["ours"][order[1]] = (
                        state[seat]["ours"].get(order[1], 0) + int(order[2]))
            return action
        except Exception:
            return inner_smooth(obs, action)

    module._smooth_sells = smooth
    return module.agent


def one(job):
    preset, opponent_path, seed, seat = job
    from kaggle_environments import make
    tag = f"{preset}_{seed}_{seat}_{os.getpid()}"
    agent = raced(preset, tag)
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
    print(f"race vs retreat -- opponent {os.path.basename(opponent)} "
          f"({n} seeds x 2 seats)\n")
    print(f"{'preset':14s} {'W-L':>8} {'win%':>6} {'mean':>9} "
          f"{'worst':>9} {'best':>9}")
    for preset in PRESETS:
        margins = table.get(preset, [])
        if not margins:
            continue
        w = sum(1 for m in margins if m > 0)
        tag = "  <= control (v27)" if preset == "off" else ""
        print(f"{preset:14s} {f'{w}-{len(margins) - w}':>8} "
              f"{100 * w / len(margins):>5.1f}% "
              f"{statistics.mean(margins):>+9,.0f} {min(margins):>+9,.0f} "
              f"{max(margins):>+9,.0f}{tag}")


if __name__ == "__main__":
    mp.freeze_support()
    main()
