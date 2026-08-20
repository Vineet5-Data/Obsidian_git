"""Slot-ranking sweep on the four reproduced ladder losses.

Orders are matched by SLOT INDEX in the engine's lockstep market loop, so which
SELL sits in slot 0 decides who drains the good prices.  v24 ranks by
self-inflicted walkdown.  This sweeps other rules against the real defeats.

No rebuild: v24.py is loaded fresh per variant and _impact_slots is replaced on
the module object, so the shipped file is never touched.
"""
import glob
import importlib.util
import json
import os
import sys

from kaggle_environments import make

LOSSES = r"C:\Users\Vinee\Desktop\Kaggriculture\recent _loss"
LOSSDIR = r"C:\Users\Vinee\Desktop\Kaggriculture\.loss"


def fresh(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def episodes():
    out = []
    for path in sorted(glob.glob(os.path.join(LOSSES, "*.json"))):
        episode = os.path.splitext(os.path.basename(path))[0]
        with open(path, encoding="utf-8") as handle:
            replay = json.load(handle)
        info = replay.get("info") or {}
        names = info.get("TeamNames") or ["p0", "p1"]
        seat = 0 if "vineet" in names[0].lower() else 1
        out.append({
            "episode": episode, "seat": seat, "seed": info.get("seed"),
            "opp_name": names[1 - seat],
            "opp_path": os.path.join(LOSSDIR, f"o_{episode}.py"),
        })
    return out


# ---------------------------------------------------------------- rank rules
def make_ranker(mode):
    def rank(module, obs, action):
        market = list(action.get("market") or [])
        rows = []
        for index, order in enumerate(market):
            if not module._is_sell(order):
                continue
            item = str(order[1])
            try:
                quantity = max(0, int(order[2]))
            except (TypeError, ValueError):
                quantity = 0
            mk = module._get(obs, "market", {}) or {}
            inventory = int(module._get(module._get(mk, "inventory", {}) or {},
                                        item, 10000) or 0)
            price = float(module._get(module._get(mk, "prices", {}) or {}, item,
                                      module._market_price(item, inventory)) or 0)
            later = float(module._market_price(item, inventory + quantity))
            if mode == "impact":
                score = quantity * max(0.0, price - later)
            elif mode == "revenue":
                score = quantity * price
            elif mode == "unitprice":
                score = price
            elif mode == "risk":
                # what being second costs: assume rival dumps a like-sized load
                rival = module._market_price(item, inventory + quantity)
                score = quantity * max(0.0, price - rival) + quantity * price / 100.0
            else:
                score = 0.0
            rows.append((score, -index, list(order)))
        if len(rows) < 2:
            return action
        rows.sort(reverse=True)
        ranked = iter(row[2] for row in rows)
        action["market"] = [next(ranked) if module._is_sell(o) else o
                            for o in market]
        return action
    return rank


def patched(mode, tag):
    module = fresh("v24.py", "cand_" + tag)
    if mode == "off":
        module.USE_IMPACT = 0
    else:
        ranker = make_ranker(mode)
        module._impact_slots = lambda obs, action: ranker(module, obs, action)
    return module.agent


def main():
    modes = sys.argv[1:] or ["impact", "off", "revenue", "unitprice", "risk"]
    eps = episodes()
    opponents = {e["episode"]: fresh(e["opp_path"], "opp_" + e["episode"]).agent
                 for e in eps}
    print(f"{'mode':11s} " + " ".join(f"{e['episode'][-5:]:>8}" for e in eps)
          + f" {'total':>9} {'W':>2}")
    for mode in modes:
        margins = []
        for e in eps:
            agent = patched(mode, f"{mode}_{e['episode']}")
            config = {"episodeSteps": 720}
            if e["seed"] is not None:
                config["seed"] = e["seed"]
            seat = e["seat"]
            pair = [agent, opponents[e["episode"]]]
            if seat == 1:
                pair = pair[::-1]
            env = make("kaggriculture", configuration=config)
            env.run(pair)
            final = env.steps[-1]
            margins.append(final[seat].reward - final[1 - seat].reward)
        wins = sum(1 for m in margins if m > 0)
        print(f"{mode:11s} " + " ".join(f"{m:>+8,.0f}" for m in margins)
              + f" {sum(margins):>+9,.0f} {wins:>2}", flush=True)


if __name__ == "__main__":
    main()
