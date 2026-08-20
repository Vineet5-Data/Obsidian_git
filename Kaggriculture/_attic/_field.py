"""True field benchmark: the shipped agent against every unique route in the pool.

Answers "is v24 actually best" rather than "does v24 beat the six opponents we
happen to own".  One agent per unique tape hash, both seats, three seeds.
"""
import collections
import importlib.util
import json
import os

from kaggle_environments import make

import _mkv24

SEEDS = [9901, 9902, 9903]
ROUTES = r"C:\Users\Vinee\Desktop\Kaggriculture\.routes"
BUILD_DIR = r"C:\Users\Vinee\Desktop\Kaggriculture\.field"
CHAMPION = "v24.py"


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.agent


def unique_routes():
    """One representative tape per unique action hash, best bank first."""
    with open(os.path.join(ROUTES, "index.json"), encoding="utf-8") as handle:
        rows = json.load(handle)
    best = {}
    for row in rows:
        key = row["hash"]
        if key not in best or (row["bank"] or 0) > (best[key]["bank"] or 0):
            best[key] = row
    return sorted(best.values(), key=lambda r: -(r["bank"] or 0))


def main():
    os.makedirs(BUILD_DIR, exist_ok=True)
    routes = unique_routes()
    print(f"{len(routes)} unique routes in pool\n")

    champion = load(CHAMPION, "champion")
    wins = losses = ties = 0
    table = []
    for row in routes:
        tag = f"{row['episode']}_p{row['seat']}"
        out = os.path.join(BUILD_DIR, f"f_{tag}.py")
        if not os.path.exists(out):
            _mkv24.build(os.path.join(ROUTES, f"{tag}.json.z"), out,
                         f"Pool route {tag}.")
        opponent = load(out, "f_" + tag)

        w = l = t = 0
        margins = []
        for seed in SEEDS:
            for seat in (0, 1):
                pair = ([champion, opponent] if seat == 0
                        else [opponent, champion])
                env = make("kaggriculture",
                           configuration={"episodeSteps": 720, "seed": seed})
                env.run(pair)
                final = env.steps[-1]
                mine, theirs = final[seat].reward, final[1 - seat].reward
                margins.append(mine - theirs)
                w += mine > theirs
                l += mine < theirs
                t += mine == theirs
        wins += w
        losses += l
        ties += t
        margin = sum(margins) / len(margins)
        table.append((w - l, margin, tag, row["team"][:22], w, l, t))
        print(f"{tag:16s} {row['team'][:22]:22s} {w}-{l}-{t}  "
              f"margin {margin:+9,.0f}", flush=True)

    print(f"\n=== FIELD TOTAL {wins}-{losses}-{ties} "
          f"({100 * wins / max(1, wins + losses + ties):.1f}% win rate) ===")
    beaten_by = [row for row in table if row[0] < 0]
    print(f"\nroutes that beat us: {len(beaten_by)}")
    for _, margin, tag, team, w, l, t in sorted(beaten_by):
        print(f"  {tag:16s} {team:22s} {w}-{l}-{t}  margin {margin:+9,.0f}")


if __name__ == "__main__":
    main()
