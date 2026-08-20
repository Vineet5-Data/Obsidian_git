"""Win-rate panel against every agent in Top_players/.

Differences from benchmark_vs_top.py, and why each one matters:

* **Win rate, not mean reward.**  Ranking is head-to-head; an agent that loses
  ten games by 100 and wins one by 50,000 has a great mean and a terrible
  record.  Mean margin is still reported, as a tiebreak.
* **Paired seat swap.**  Both seats play the SAME seed, so the board, the
  weather rolls and the market are identical and only the seat differs.
  Swapping seat *and* seed at once (seed vs seed+999) makes the two halves
  independent samples instead of a control, which is the whole point of
  swapping.
* **Seb.py included.**  It is a top-player file sitting in the directory.
* **Import failures are fatal, not skipped.**  A silently dropped opponent is
  indistinguishable from an opponent that never existed.

Usage:
  python bench/panel_top.py v75.py v67_lin.py --seeds 6
"""
import argparse
import importlib.util
import os
import sys
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
TOP_DIRS = [os.path.join(ROOT, "Top_fresh-21"),
            os.path.join(ROOT, "v27_losses")]

_cache = {}


def load(path):
    """Import a bot once per worker process and hand back its `agent`."""
    if path not in _cache:
        name = "m_" + os.path.splitext(os.path.basename(path))[0]
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        _cache[path] = mod.agent
    return _cache[path]


def play(job):
    """One episode.  Returns (opponent, seed, our_reward, their_reward)."""
    cand_path, opp_path, seed, our_seat = job
    from kaggle_environments import make
    ours, theirs = load(cand_path), load(opp_path)
    env = make("kaggriculture",
               configuration={"episodeSteps": 720, "seed": seed})
    pair = [ours, theirs] if our_seat == 0 else [theirs, ours]
    env.run(pair)
    last = env.steps[-1]
    r = [last[0].reward, last[1].reward]
    name = os.path.splitext(os.path.basename(opp_path))[0]
    return name, seed, r[our_seat], r[1 - our_seat]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("agents", nargs="+")
    ap.add_argument("--seeds", type=int, default=6)
    # The 17-bot field lived briefly in Top_players/; it has since been split
    # back into its two source folders, so accept several dirs and pool them.
    ap.add_argument("--top-dir", nargs="+", default=TOP_DIRS)
    ap.add_argument("--workers", type=int, default=0)
    args = ap.parse_args()

    dirs = [args.top_dir] if isinstance(args.top_dir, str) else args.top_dir
    opps = sorted(os.path.join(d, f)
                  for d in dirs for f in os.listdir(d) if f.endswith(".py"))
    if not opps:
        sys.exit(f"no .py opponents in {dirs}")

    # Same generator as the retired _real.py panel so seeds stay comparable
    # across sessions.
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, args.seeds + 1)]
    workers = args.workers or max(1, (os.cpu_count() or 4) - 2)

    print(f"TOP field: {len(opps)} opponents x {len(seeds)} seeds x 2 seats "
          f"= {len(opps) * len(seeds) * 2} games/agent")
    print(f"{'agent':16s} {'W-L':>9s} {'win%':>7s} {'mean':>10s} "
          f"{'worst':>10s}  losing matchups (losses of "
          f"{len(seeds) * 2})")

    for cand in args.agents:
        jobs = [(cand, o, s, seat)
                for o in opps for s in seeds for seat in (0, 1)]
        with Pool(workers) as pool:
            out = pool.map(play, jobs, chunksize=1)

        wins = losses = 0
        margins = []
        per = {}
        for name, _seed, ours, theirs in out:
            m = (ours or 0) - (theirs or 0)
            margins.append(m)
            w, l = per.get(name, (0, 0))
            if m > 0:
                wins += 1
                per[name] = (w + 1, l)
            else:
                losses += 1
                per[name] = (w, l + 1)
        n = len(margins)
        # Show every opponent that took a game, not only the ones holding a
        # winning record -- against a weak field the majority test hides the
        # entire signal (a 196-8 record printed as "no losing matchups").
        bad = " ".join(f"{k}:{v[1]}" for k, v in sorted(per.items())
                       if v[1] > 0)
        print(f"{os.path.basename(cand):16s} {wins}-{losses:<5d} "
              f"{100.0 * wins / n:6.1f}% {sum(margins) / n:10,.0f} "
              f"{min(margins):10,.0f}  {bad}")


if __name__ == "__main__":
    main()
