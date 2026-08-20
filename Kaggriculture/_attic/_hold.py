"""Hold WHEAT, dump everything else.  The per-item policy the uniform tests missed.

Measured in a live game (seed 12345, v27 vs Seb):

    step      0   WHEAT inventory 10,000   price $25
    step    648   WHEAT inventory  9,112   price $55

Town drain EXCEEDS total wheat supply, so wheat inventory falls all game and the
wheat price MORE THAN DOUBLES.  The "glut >= 1 everywhere so every price path
declines, therefore sell immediately" claim is simply false for wheat -- and
wheat is the one good whose price rises.

The per-unit impact slopes say the same thing from the other side:

    WHEAT       p= 25.00   selling 100 units moves price   $4    (liquid)
    MILK        p=160.00   selling 100 units moves price $159    (crashes it)
    STRAWBERRY  p=120.00   selling 100 units moves price $119
    WOOL        p=200.00   selling 100 units moves price $199

So wheat is nearly infinitely liquid AND appreciating -> hold it and sell late.
The premium goods are violently illiquid AND flat -> dump them thin and early.

Every earlier holding policy lost because it held EVERY good uniformly.  Two
things punish that: the premium price paths do not rise, and shed capacity is
only 100 with end-of-day overflow DISCARDED, so a shed full of hoarded stock
destroys the harvest.  Hence `headroom`: never let the hoard crowd the shed.

Usage:  python _hold.py [opponent.py] [n_seeds]
"""
import importlib.util
import multiprocessing as mp
import os
import statistics
import sys

BASE = "v27.py"
HOLD_ITEM = "WHEAT"

PRESETS = {
    "off":         None,
    "w400_h40":    {"until": 400, "headroom": 40},
    "w500_h40":    {"until": 500, "headroom": 40},
    "w600_h40":    {"until": 600, "headroom": 40},
    "w600_h20":    {"until": 600, "headroom": 20},
    "w600_h60":    {"until": 600, "headroom": 60},
    "w660_h40":    {"until": 660, "headroom": 40},
}


def fresh(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def holder(preset, tag):
    module = fresh(BASE, "h_" + tag)
    P = PRESETS[preset]
    if P is None:
        return module.agent
    inner = module._smooth_sells

    def smooth(obs, action):
        action = inner(obs, action)
        try:
            step = int(module._get(obs, "step", 0) or 0)
            if step >= P["until"]:
                return action                      # release: sell normally
            orders = [list(o) for o in (action.get("market") or [])]

            shed = {k: max(0, int(v or 0)) for k, v in dict(module._get(
                module._get(obs, "private", {}) or {}, "shed", {}) or {}).items()}
            used = sum(shed.values())
            # Only hoard while the shed has room to spare.  Capacity is 100 and
            # end-of-day overflow is DISCARDED -- a full shed destroys harvest,
            # which is what sank every uniform holding policy.
            if used > 100 - P["headroom"]:
                return action

            action["market"] = [o for o in orders
                                if not (o and o[0] == "SELL" and o[1] == HOLD_ITEM)]
        except Exception:
            pass
        return action

    module._smooth_sells = smooth
    return module.agent


def one(job):
    preset, opponent_path, seed, seat = job
    from kaggle_environments import make
    tag = f"{preset}_{seed}_{seat}_{os.getpid()}"
    agent = holder(preset, tag)
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
    print(f"hold {HOLD_ITEM} vs {os.path.basename(opponent)} "
          f"({n} seeds x 2 seats)\n")
    print(f"{'preset':12s} {'W-L':>8} {'win%':>6} {'mean':>9} "
          f"{'worst':>9} {'best':>9}")
    for preset in PRESETS:
        margins = table.get(preset, [])
        if not margins:
            continue
        w = sum(1 for m in margins if m > 0)
        tag = "  <= control (v27)" if preset == "off" else ""
        print(f"{preset:12s} {f'{w}-{len(margins) - w}':>8} "
              f"{100 * w / len(margins):>5.1f}% "
              f"{statistics.mean(margins):>+9,.0f} {min(margins):>+9,.0f} "
              f"{max(margins):>+9,.0f}{tag}")


if __name__ == "__main__":
    mp.freeze_support()
    main()
