"""Mid-day DROP: relieve the constraint that makes the advance loop inert.

SELL draws from the SHED only (engine line 353), and the tape contains ZERO DROP
ops -- it relies entirely on the automatic end-of-day _drop_inventories_to_shed.
So anything harvested today cannot be sold until tomorrow.  That is exactly why
SMOOTH_CAP and SMOOTH_WINDOW measured inert: the advance loop is shed-limited,
not cap-limited.

DROP is a stationary op (no movement, cannot desync the route), needs only that
the unit stands on one of the four shed-access tiles (4,4) (5,4) (4,5) (5,5) --
and _spawn_hand places new hands on precisely those tiles.  Units idling there
currently get NO job at all, because _idle_tile returns None for a non-dict tile
and _idle_job never sees them.

Cash arriving EARLIER is the one intervention direction that has ever worked on
this tape (smoothing +572; every delaying policy lost).  A mid-day DROP is pure
acceleration: same goods, same route, one day sooner into sellable form.

THE HAZARD: DROP dumps the unit's ENTIRE inventory and takes no item argument,
while FEED consumes WHEAT from that same unit inventory (engine line 487).
Dropping a unit that is carrying feed starves the animal, and an animal unfed
two days running ESCAPES.  Hence the guarded variants.

Usage:  python _drop.py [opponent.py] [n_seeds]
"""
import importlib.util
import multiprocessing as mp
import os
import statistics
import sys

BASE = "v27.py"
SHED_TILES = {(4, 4), (5, 4), (4, 5), (5, 5)}

PRESETS = {
    "off":           None,
    "drop_all":      {"guard": "none"},
    "drop_nowheat":  {"guard": "wheat"},
    "drop_produce":  {"guard": "produce"},
}


def fresh(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def dropper(preset, tag):
    module = fresh(BASE, "d_" + tag)
    P = PRESETS[preset]
    if P is None:
        return module.agent
    inner = module._idle_fill
    sellable = set(module.SELLABLE_PRODUCTS)

    def wants_drop(inventory):
        inventory = {k: int(v or 0) for k, v in dict(inventory or {}).items()
                     if int(v or 0) > 0}
        if not inventory:
            return False
        if P["guard"] == "none":
            return True
        # never dump a unit's feed: FEED takes WHEAT from this same inventory
        if inventory.get("WHEAT"):
            return False
        if P["guard"] == "produce":
            return any(item in sellable for item in inventory)
        return True

    def idle_fill(obs, action):
        action = inner(obs, action)
        try:
            farm = module._farm(obs)
            private = module._get(obs, "private", {}) or {}
            inventories = list(module._get(private, "inventories", []) or [])

            def inv(index):
                return inventories[index] if index < len(inventories) else {}

            def on_shed(position):
                try:
                    return (int(position[0]), int(position[1])) in SHED_TILES
                except (TypeError, ValueError, IndexError):
                    return False

            order = action.get("farmer") or ["PASS"]
            if order[0] == "PASS" and on_shed(
                    module._get(farm, "farmer", [0, 0])) and wants_drop(inv(0)):
                action["farmer"] = ["DROP"]

            hands = list(action.get("hands") or [])
            positions = list(module._get(farm, "hands", []) or [])
            for i, order in enumerate(hands):
                if not (order and order[0] == "PASS") or i >= len(positions):
                    continue
                if on_shed(positions[i]) and wants_drop(inv(i + 1)):
                    hands[i] = ["DROP"]
            action["hands"] = hands
        except Exception:
            pass
        return action

    module._idle_fill = idle_fill
    return module.agent


def one(job):
    preset, opponent_path, seed, seat = job
    from kaggle_environments import make
    tag = f"{preset}_{seed}_{seat}_{os.getpid()}"
    agent = dropper(preset, tag)
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
    print(f"mid-day DROP vs {os.path.basename(opponent)} "
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
