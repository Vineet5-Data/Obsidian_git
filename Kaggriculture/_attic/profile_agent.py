"""Profile an agent: action efficiency, tile utilization, revenue by product, waste.

Usage: python profile_agent.py [agent_file] [opponent] [seed]
"""
import copy
import json
import sys
from collections import Counter, defaultdict

from kaggle_environments import make
from kaggle_environments.envs.kaggriculture import kaggriculture as K

AGENT = sys.argv[1] if len(sys.argv) > 1 else "main.py"
OPP = sys.argv[2] if len(sys.argv) > 2 else "starter"
SEED = int(sys.argv[3]) if len(sys.argv) > 3 else 1000

ops = Counter()          # (player, op) -> count
noops = Counter()        # (player, op) -> count of no-effect actions
revenue = defaultdict(float)   # (player, item) -> $
sold = Counter()
spent = defaultdict(float)
daily = []               # per-day snapshots for player 0

_orig_apply = K._apply_unit_action
_orig_commit = K._commit_unit
_orig_drop = K._drop_inventories_to_shed
overflow_lost = Counter()

CUR_PLAYER = [0]
LIVE = {"farms": None, "privs": None}


def apply_hook(farm, private, idx, action, board_size, day, turns_per_day, shed_capacity=100):
    p = CUR_PLAYER[0]
    op = action[0] if isinstance(action, list) and action else "NONE"
    pos = K._farmer_position(farm, idx)
    before = None
    if pos:
        x, y = pos[0], pos[1]
        before = (copy.deepcopy(farm["tiles"][y][x]), tuple(pos),
                  tuple(sorted(K._farmer_inventory(private, idx).items())),
                  tuple(sorted(private["seeds"].items())),
                  tuple(sorted(private["shed"].items())))
    _orig_apply(farm, private, idx, action, board_size, day, turns_per_day, shed_capacity)
    ops[(p, op)] += 1
    if before is not None:
        pos2 = K._farmer_position(farm, idx)
        x2, y2 = pos2[0], pos2[1]
        after = (farm["tiles"][y2][x2], tuple(pos2),
                 tuple(sorted(K._farmer_inventory(private, idx).items())),
                 tuple(sorted(private["seeds"].items())),
                 tuple(sorted(private["shed"].items())))
        if before == after and op != "PASS":
            noops[(p, op)] += 1


def commit_hook(op, item, price, farm, private, market, shed_capacity=100):
    ok = _orig_commit(op, item, price, farm, private, market, shed_capacity)
    if ok:
        p = 0 if (LIVE["farms"] and farm is LIVE["farms"][0]) else 1
        if op == "SELL":
            revenue[(p, item)] += price
            sold[(p, item)] += 1
        else:
            spent[(p, op + ":" + str(item))] += price
    return ok


def drop_hook(private, capacity):
    before = sum(sum(inv.values()) for inv in private["inventories"])
    room = max(0, capacity - sum(private["shed"].values()))
    lost = max(0, before - room)
    p = 0 if (LIVE["privs"] and private is LIVE["privs"][0]) else 1
    overflow_lost[p] += lost
    _orig_drop(private, capacity)


K._apply_unit_action = apply_hook
K._commit_unit = commit_hook
K._drop_inventories_to_shed = drop_hook

env = make("kaggriculture", configuration={"seed": SEED})
env.reset(2)
FARMS = env.state[0].observation.farms
PRIVS = [s.observation.private for s in env.state]

# patch interpreter to track current player during unit actions + daily snapshot
_orig_interp = K.interpreter


def interp(state, env_):
    obs0 = state[0].observation
    LIVE["farms"] = obs0.farms
    LIVE["privs"] = [s.observation.private for s in state]
    step = K.get(obs0, "step", 0)
    # tag player during apply by wrapping per-player: easiest is patch inside loop
    res = _orig_interp(state, env_)
    if (step + 1) % 24 == 0:
        farm = obs0.farms[0]
        tc = Counter()
        for row in farm["tiles"]:
            for t in row:
                if t is None:
                    tc["empty"] += 1
                elif t == "LOCKED":
                    tc["locked"] += 1
                elif t.get("kind") == "WEED":
                    tc["weed"] += 1
                elif t.get("kind") == "PLANT":
                    tc["crop:" + t["crop"]] += 1
                elif "animal" in t:
                    tc["animal:" + t["animal"]] += 1
                else:
                    tc["struct:" + t["kind"]] += 1
        daily.append({
            "day": step // 24,
            "money": round(farm["money"]),
            "opp_money": round(obs0.farms[1]["money"]),
            "tiles": dict(tc),
            "shed": dict(state[0].observation.private["shed"]),
            "quads": len(farm["unlocked_quadrants"]),
        })
    return res


# Need per-player tagging: wrap apply to detect player via farm identity
def apply_hook2(farm, private, idx, action, board_size, day, turns_per_day, shed_capacity=100):
    CUR_PLAYER[0] = 0 if (LIVE["farms"] and farm is LIVE["farms"][0]) else 1
    return apply_hook(farm, private, idx, action, board_size, day, turns_per_day, shed_capacity)


K._apply_unit_action = apply_hook2
K.interpreter = interp
env.interpreter = interp

env.run([AGENT, OPP])
last = env.steps[-1]
print(f"FINAL: me=${last[0]['reward']:.0f}  opp=${last[1]['reward']:.0f}  (seed {SEED} vs {OPP})\n")

print("=== DAILY (player 0) ===")
for d in daily:
    t = d["tiles"]
    prod = sum(v for k, v in t.items() if k.startswith(("crop:", "animal:")))
    print(f"d{d['day']:2d} ${d['money']:>7d} (opp ${d['opp_money']:>6d}) quads={d['quads']} "
          f"productive={prod:>3d} empty={t.get('empty',0):>3d} weed={t.get('weed',0):>2d} "
          f"structs={sum(v for k,v in t.items() if k.startswith('struct:')):>2d} "
          f"shed={sum(d['shed'].values()):>3d} | " +
          " ".join(f"{k.split(':')[1]}={v}" for k, v in sorted(t.items()) if k.startswith(("crop:", "animal:"))))

print("\n=== ACTIONS (player 0) — total, wasted ===")
tot = sum(v for (p, _), v in ops.items() if p == 0)
for (p, op), n in sorted(ops.items(), key=lambda kv: -kv[1]):
    if p != 0:
        continue
    w = noops.get((0, op), 0)
    print(f"  {op:20s} {n:6d} ({100*n/tot:4.1f}%)   wasted {w:5d} ({100*w/max(1,n):4.1f}%)")
print(f"  TOTAL {tot} actions, wasted {sum(v for (p,_),v in noops.items() if p==0)} "
      f"({100*sum(v for (p,_),v in noops.items() if p==0)/max(1,tot):.1f}%)")

print("\n=== REVENUE (player 0) ===")
for (p, item), amt in sorted(revenue.items(), key=lambda kv: -kv[1]):
    if p == 0:
        print(f"  {item:12s} ${amt:>9.0f}  units={sold[(0,item)]:>5d}  avg ${amt/max(1,sold[(0,item)]):.1f}")
print(f"  TOTAL REVENUE ${sum(a for (p,_),a in revenue.items() if p==0):.0f}")
print("\n=== SPEND (player 0) ===")
for (pl, k), amt in sorted(spent.items(), key=lambda kv: -kv[1]):
    if pl == 0:
        print(f"  {k:28s} ${amt:>8.0f}")
print(f"  TOTAL SPEND ${sum(a for (pl,_),a in spent.items() if pl==0):.0f}")
print(f"\nOVERFLOW DISCARDED at end-of-day (p0): {overflow_lost[0]} items")

print("\n=== OPPONENT REVENUE ===")
for (p, item), amt in sorted(revenue.items(), key=lambda kv: -kv[1]):
    if p == 1:
        print(f"  {item:12s} ${amt:>9.0f}  units={sold[(1,item)]:>5d}")
