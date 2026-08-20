"""Local screen: patched v140 vs pristine v140 baseline, N seeds x both seats.

Not the 1600-game benchmark -- just enough seeds to tell a real move from noise.
Effective sample size is SEEDS, not games, so both seats of one seed count once.
"""
import argparse
import importlib.util
import multiprocessing as mp
import statistics
import sys
from pathlib import Path

ROOT = Path(r"C:\Users\Vinee\Desktop\Kaggriculture")
NEW_PATH = ROOT / "a_v140_market_dominance.py"
OLD_PATH = ROOT / "a_v140_market_dominance.baseline.py"




def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def duel(job):
    seed, seat, new_path, old_path = job
    from kaggle_environments import make
    new = load("cand_new", new_path)
    old = load("cand_old", old_path)
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    players = [new.agent, old.agent] if seat == 0 else [old.agent, new.agent]
    env.run(players)
    last = env.steps[-1]
    if last[0].status != "DONE" or last[1].status != "DONE":
        return seed, seat, None
    return seed, seat, int(last[seat].reward) - int(last[1 - seat].reward)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seeds", type=int, default=12)
    ap.add_argument("--workers", type=int, default=14)
    ap.add_argument("--new", default=str(NEW_PATH))
    ap.add_argument("--old", default=str(OLD_PATH))
    args = ap.parse_args()

    print(f"\n  {Path(args.new).name}  vs  {Path(args.old).name}")
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, args.seeds + 1)]
    jobs = [(s, seat, args.new, args.old) for s in seeds for seat in (0, 1)]
    with mp.Pool(min(args.workers, len(jobs))) as pool:
        rows = pool.map(duel, jobs)

    margins = [m for _s, _seat, m in rows if m is not None]
    crashed = sum(1 for _s, _seat, m in rows if m is None)
    wins = sum(1 for m in margins if m > 0)
    if not margins:
        print("  every game crashed")
        return

    by_seed = {}
    for seed, _seat, m in rows:
        if m is not None:
            by_seed.setdefault(seed, []).append(m)
    seed_means = [statistics.mean(v) for v in by_seed.values()]

    print(f"\n  games        {len(margins)} ({wins}W-{len(margins) - wins}L)"
          f"  crashed={crashed}")
    print(f"  win rate     {100.0 * wins / max(1, len(margins)):.1f}%")
    print(f"  mean margin  {statistics.mean(margins):+,.0f}")
    print(f"  median       {statistics.median(margins):+,.0f}")
    print(f"  best/worst   {max(margins):+,} / {min(margins):+,}")
    print(f"\n  per-seed (n={len(seed_means)} effective samples):")
    print(f"    seeds won  {sum(1 for m in seed_means if m > 0)}/{len(seed_means)}")
    print(f"    mean       {statistics.mean(seed_means):+,.0f}")
    if len(seed_means) > 1:
        sd = statistics.stdev(seed_means)
        se = sd / (len(seed_means) ** 0.5)
        print(f"    stdev      {sd:,.0f}   sem {se:,.0f}"
              f"   t {statistics.mean(seed_means) / se:+.2f}")


if __name__ == "__main__":
    main()
