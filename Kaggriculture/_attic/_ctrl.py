"""Functional production controller -- the non-clone half of the agent.

Every market experiment failed because the market optimum is state-independent
(sell now).  The fragility the tape actually carries is on the PRODUCTION side,
and the panel shows it: mirror 0-48 (a strictly more productive family-A tape
beats ours) and Seb 6-42 (19 animals flood milk and our fixed plan cannot
respond).

A tape cannot react.  A controller can, because unit positions are public
(farms[p].farmer, farms[p].hands) -- actor-local dead reckoning only breaks
tape REPLAY, not a policy that reads the board.

Policy, all parametric:

    score(job) = W[kind] * marginal_value(job) / (1 + DIST_PENALTY * steps_away)

marginal_value is priced off the LIVE market, so when a rival floods milk the
controller stops spending unit-turns on cows and waters strawberries instead.
That is the behaviour the tape structurally cannot produce.

Hybrid by design: the tape's opening build-out (hire ramp, land, herd) is a good
schedule and hard to beat from scratch, so the controller only takes over from
SWITCH_STEP onward -- which is also exactly where all four ladder losses
happened (ahead at day 24, lost by day 30).

Usage:  python _ctrl.py [switch_step ...]
"""
import glob
import importlib.util
import json
import os
import sys

LOSSES = r"C:\Users\Vinee\Desktop\Kaggriculture\recent _loss"
LOSSDIR = r"C:\Users\Vinee\Desktop\Kaggriculture\.loss"

SHED_TILES = ((4, 4), (5, 4), (4, 5), (5, 5))
MOVES = (("NORTH", 0, -1), ("SOUTH", 0, 1), ("EAST", 1, 0), ("WEST", -1, 0))
CROP_PRODUCT = {"WHEAT": "WHEAT", "CARROT": "CARROT", "TOMATO": "TOMATO",
                "STRAWBERRY": "STRAWBERRY", "MELON": "MELON"}
ANIMAL_PRODUCT = {"COW": "MILK", "SHEEP": "WOOL", "GOOSE": "EGG"}

DEFAULTS = {
    "switch": 528,       # step the controller takes over from the tape
    "w_harvest": 1.0,
    "w_care": 1.0,
    "w_water": 0.8,
    "w_feed": 1.5,       # unfed twice = animal escapes, so protect production
    "w_fert": 0.35,      # fertilizer has zero consumers; price ratchets down
    "w_dig": 0.05,
    "dist_penalty": 0.6,
    "carry_drop": 6,
    "feed_load": 8,     # inventory size that triggers a shed run
}


def fresh(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def make_controller(module, P):
    def price(obs, item):
        prices = module._get(module._get(obs, "market", {}) or {}, "prices", {}) or {}
        return float(module._get(prices, item, 1) or 1)

    def jobs_for(obs, farm):
        """Every productive op available on our board, with a live price tag."""
        out = []
        tiles = list(module._get(farm, "tiles", []) or [])
        for y, row in enumerate(tiles):
            for x, tile in enumerate(row or []):
                if not isinstance(tile, dict):
                    continue
                kind = tile.get("kind")
                if kind == "WEED":
                    out.append((x, y, ["DIG"], P["w_dig"] * 10.0))
                    continue
                animal = tile.get("animal")
                if animal:
                    item = ANIMAL_PRODUCT.get(animal, "MILK")
                    unit_price = price(obs, item)
                    held = int(tile.get("yield_units", 0) or 0)
                    if held > 0:
                        out.append((x, y, ["HARVEST"],
                                    P["w_harvest"] * unit_price * held))
                    if not tile.get("fed_today"):
                        out.append((x, y, ["FEED"], P["w_feed"] * unit_price))
                    elif not tile.get("cared_today"):
                        out.append((x, y, ["CARE"], P["w_care"] * unit_price))
                    if tile.get("fertilizer_available"):
                        out.append((x, y, ["COLLECT_FERTILIZER"],
                                    P["w_fert"] * price(obs, "FERTILIZER")))
                elif kind == "PLANT" and tile.get("crop"):
                    item = CROP_PRODUCT.get(tile.get("crop"), "WHEAT")
                    unit_price = price(obs, item)
                    held = int(tile.get("yield_units", 0) or 0)
                    if held > 0:
                        out.append((x, y, ["HARVEST"],
                                    P["w_harvest"] * unit_price * held))
                    if not tile.get("watered_today"):
                        out.append((x, y, ["WATER"], P["w_water"] * unit_price))
        return out

    def step_toward(px, py, tx, ty):
        if px == tx and py == ty:
            return None
        if px != tx:
            return "EAST" if tx > px else "WEST"
        return "SOUTH" if ty > py else "NORTH"

    def control(obs, action):
        farm = module._farm(obs)
        private = module._get(obs, "private", {}) or {}
        inventories = list(module._get(private, "inventories", []) or [])
        positions = [module._get(farm, "farmer", [0, 0])]
        positions += [list(h) for h in (module._get(farm, "hands", []) or [])]

        pool = jobs_for(obs, farm)
        taken = set()
        ops = []
        for index, pos in enumerate(positions):
            if not isinstance(pos, (list, tuple)) or len(pos) < 2:
                ops.append(["PASS"])
                continue
            px, py = int(pos[0]), int(pos[1])
            inventory = inventories[index] if index < len(inventories) else {}
            carried = sum(max(0, int(v or 0)) for v in (inventory or {}).values())

            # Feeding needs WHEAT in hand.  Two missed feeds and the animal
            # escapes permanently, so fetching feed outranks every other job.
            wheat_held = int((inventory or {}).get("WHEAT", 0) or 0)
            shed_wheat = int(module._get(
                module._get(private, "shed", {}) or {}, "WHEAT", 0) or 0)
            need_feed = any(op[0] == "FEED" for _, _, op, _ in pool)
            if need_feed and wheat_held <= 0 and shed_wheat > 0:
                if (px, py) in SHED_TILES:
                    ops.append(["PICKUP", "WHEAT",
                                min(P["feed_load"], shed_wheat)])
                    continue
                target = min(SHED_TILES,
                             key=lambda t: abs(t[0] - px) + abs(t[1] - py))
                move = step_toward(px, py, target[0], target[1])
                ops.append([move] if move else ["PASS"])
                continue

            # full hands go bank the goods; nothing sells from a field inventory
            if carried >= P["carry_drop"]:
                if (px, py) in SHED_TILES:
                    ops.append(["DROP"])
                    continue
                target = min(SHED_TILES,
                             key=lambda t: abs(t[0] - px) + abs(t[1] - py))
                move = step_toward(px, py, target[0], target[1])
                ops.append([move] if move else ["PASS"])
                continue

            best = None
            for jx, jy, op, value in pool:
                if (jx, jy, op[0]) in taken:
                    continue
                if op[0] == "FEED" and int((inventory or {}).get("WHEAT", 0) or 0) <= 0:
                    continue
                distance = abs(jx - px) + abs(jy - py)
                score = value / (1.0 + P["dist_penalty"] * distance)
                if best is None or score > best[0]:
                    best = (score, jx, jy, op)
            if best is None:
                ops.append(["PASS"])
                continue
            _, jx, jy, op = best
            taken.add((jx, jy, op[0]))
            if (px, py) == (jx, jy):
                ops.append(list(op))
            else:
                move = step_toward(px, py, jx, jy)
                ops.append([move] if move else ["PASS"])

        action["farmer"] = ops[0] if ops else ["PASS"]
        action["hands"] = ops[1:]
        return action

    return control


def build(switch, tag, base="v26.py", overrides=None):
    module = fresh(base, "c_" + tag)
    P = dict(DEFAULTS)
    P["switch"] = switch
    if overrides:
        P.update(overrides)
    control = make_controller(module, P)
    original = module.agent

    def agent(obs):
        try:
            step = int(module._get(obs, "step", 0) or 0)
            if step < P["switch"]:
                return original(obs)
            action = original(obs)          # keeps the market layer intact
            action = control(obs, action)
            return module._aligned(action, obs)
        except Exception:
            return original(obs)

    return agent


def episodes():
    out = []
    for path in sorted(glob.glob(os.path.join(LOSSES, "*.json"))):
        episode = os.path.splitext(os.path.basename(path))[0]
        with open(path, encoding="utf-8") as handle:
            replay = json.load(handle)
        info = replay.get("info") or {}
        names = info.get("TeamNames") or ["p0", "p1"]
        seat = 0 if "vineet" in names[0].lower() else 1
        out.append({"episode": episode, "seat": seat, "seed": info.get("seed"),
                    "opp": os.path.join(LOSSDIR, f"o_{episode}.py")})
    return out


def main():
    from kaggle_environments import make
    switches = [int(a) for a in sys.argv[1:]] or [720, 672, 600, 528, 456, 384]
    eps = episodes()
    opponents = {e["episode"]: fresh(e["opp"], "o_" + e["episode"]).agent
                 for e in eps}
    print(f"{'switch':>7} " + " ".join(f"{e['episode'][-5:]:>8}" for e in eps)
          + f" {'total':>9} {'W':>2}")
    for switch in switches:
        margins = []
        for e in eps:
            agent = build(switch, f"{switch}_{e['episode']}")
            config = {"episodeSteps": 720}
            if e["seed"] is not None:
                config["seed"] = e["seed"]
            pair = [agent, opponents[e["episode"]]]
            if e["seat"] == 1:
                pair = pair[::-1]
            env = make("kaggriculture", configuration=config)
            env.run(pair)
            final = env.steps[-1]
            margins.append(final[e["seat"]].reward - final[1 - e["seat"]].reward)
        print(f"{switch:>7} " + " ".join(f"{m:>+8,.0f}" for m in margins)
              + f" {sum(margins):>+9,.0f} {sum(1 for m in margins if m > 0):>2}",
              flush=True)


if __name__ == "__main__":
    main()
