"""Where do our agents lose, and what's different when they do?

Combines three existing diagnostics instead of a new methodology:
  - _oppdiff.py / _topops.py's per-1000-unit-turn op-mix normalisation
    (raw counts aren't comparable -- more hands do more of everything)
  - _analyze_losses.py's day-by-day money/asset turning points
  - run_bisect.py's mount-robust opponent glob + multiprocessing skeleton

For each agent, runs the full .top/ opponent set (recorded mode: each
opponent replays on its own home seed from seeds.json, same as
run_bisect.py's default). Splits games into wins/losses and reports:
  1. our op-mix in wins vs losses (within-agent -- how do WE play
     differently when we lose)
  2. our op-mix vs the opponent's, in losses only (what do THEY do that
     we don't, when they beat us)
  3. money-delta-vs-opponent by day, averaged across losses (WHEN we
     fall behind)
  4. ops that diverge the same direction across every agent tested --
     a shared v97_cap70-lineage weakness, not one variant's mistake

Usage:  python _loss_analysis.py [agent1.py agent2.py ...] [--workers N] [--out path.json]
        [--opponents N] [--seeds N] [--offset N]
--opponents N: use only first N .top/ opponents (fewer opponents, not more games).
--seeds N: N fresh seeds per opponent instead of its 1 recorded/home seed
  (same generator as run_bisect.py's random mode) -- games/agent = 2*opponents*N.
--offset N: skip the first N seeds (only matters with --seeds).
No agents given -> v108_nopump.py, v97_cap70.py, 100v.py (round-9 trio) if present.
Opponents come from .top/ (any attached Kaggle dataset, mount path auto-detected).
"""
import glob
import json
import multiprocessing as mp
import os
import sys
import time
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHECK_DAYS = [5, 10, 15, 20, 25]
DEFAULT_AGENTS = ["v108_nopump.py", "v97_cap70.py", "100v.py"]


def find_opponents():
    """.top/ lives in the grid-search dataset, not here. Mount path varies."""
    for pattern in ("/kaggle/input/*/t_*.py",
                     "/kaggle/input/*/*/t_*.py",
                     "/kaggle/input/*/.top/t_*.py",
                     "/kaggle/input/*/*/.top/t_*.py",
                     "/kaggle/input/*/*/*/.top/t_*.py",
                     str(HERE / ".top" / "t_*.py"),
                     str(HERE / "t_*.py"),
                     ".top/t_*.py",
                     "t_*.py"):
        hits = sorted(glob.glob(pattern))
        if hits:
            return hits
    raise SystemExit("no .top/t_*.py found -- attach the grid-search dataset")


def load(path):
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "m_" + os.path.basename(path).replace(".", "_"), path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.agent


def op_mix(steps, seat):
    """-> per-1000-unit-turn op profile. Same shape as _topops.py:count_actions."""
    ops = Counter()
    for st in steps[1:]:
        a = (st[seat].get("action") or {}) if seat < len(st) else {}
        if not isinstance(a, dict):
            continue
        for u in [a.get("farmer")] + list(a.get("hands") or []):
            if isinstance(u, list) and u:
                ops[u[0]] += 1
        for o in (a.get("market") or []):
            if o:
                ops["mkt:" + o[0]] += 1
    unit = sum(v for k, v in ops.items() if not k.startswith("mkt:"))
    return ({k: 1000.0 * v / unit for k, v in ops.items()} if unit else {}), unit


def assets(obs, seat):
    """-> (plant tiles, animal tiles) for one farm. Same logic as _gdiag.py."""
    farm = (obs.get("farms") or [None, None])[seat] or {}
    pl = an = 0
    for row in (farm.get("tiles") or []):
        for t in (row or []):
            if isinstance(t, dict):
                if t.get("kind") == "PLANT":
                    pl += 1
                elif "animal" in t:
                    an += 1
    return pl, an, farm.get("money", 0)


def one(job):
    """Run one game, return a compact diagnostic summary (never the raw steps)."""
    agent_path, opp_path, seed, seat, opp_name = job
    from kaggle_environments import make
    a, b = load(agent_path), load(opp_path)
    pair = [a, b] if seat == 0 else [b, a]
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run(pair)
    steps = env.steps
    margin = steps[-1][seat].reward - steps[-1][1 - seat].reward

    our_prof, our_unit = op_mix(steps, seat)
    opp_prof, opp_unit = op_mix(steps, 1 - seat)

    curve = []
    for day in CHECK_DAYS:
        i = min(len(steps) - 1, day * 24 + 23)
        obs = steps[i][0].get("observation") or {}
        our_p, our_a, our_m = assets(obs, seat)
        opp_p, opp_a, opp_m = assets(obs, 1 - seat)
        curve.append({"day": day, "money_delta": our_m - opp_m,
                      "our_plants": our_p, "opp_plants": opp_p,
                      "our_animals": our_a, "opp_animals": opp_a})

    return {"opponent": opp_name, "seed": seed, "seat": seat, "margin": margin,
            "win": margin > 0, "our_prof": our_prof, "our_unit": our_unit,
            "opp_prof": opp_prof, "opp_unit": opp_unit, "curve": curve}


def avg_prof(rows, key):
    acc, n = Counter(), 0
    for r in rows:
        if r[key]:
            for k, v in r[key].items():
                acc[k] += v
            n += 1
    return {k: v / n for k, v in acc.items()} if n else {}


def analyze_agent(agent_path, opps, seeds, workers, pool_seeds=None):
    jobs = []
    for o in opps:
        if pool_seeds:
            seed_list = pool_seeds
        else:
            ep = Path(o).stem.removeprefix("t_").rsplit("_", 1)[0]
            seed_list = [seeds.get(ep, 12345)]
        for seed in seed_list:
            for seat in (0, 1):
                jobs.append((agent_path, o, seed, seat, Path(o).stem))

    name = Path(agent_path).stem
    print(f"\n{name}: {len(jobs)} games queued...", flush=True)
    t0 = time.time()
    rows = []
    with mp.Pool(workers) as pool:
        for n, row in enumerate(pool.imap(one, jobs, chunksize=1), 1):
            rows.append(row)
            if n % 200 == 0 or n == len(jobs):
                el = time.time() - t0
                print(f"  {n}/{len(jobs)}  {el:.0f}s  eta {el / n * (len(jobs) - n):.0f}s", flush=True)

    wins = [r for r in rows if r["win"]]
    losses = [r for r in rows if not r["win"]]

    print(f"\n{'=' * 70}\n{name}: {len(wins)}-{len(losses)} "
          f"({100 * len(wins) / len(rows):.1f}%)\n{'=' * 70}")

    win_prof = avg_prof(wins, "our_prof")
    loss_prof = avg_prof(losses, "our_prof")
    opp_loss_prof = avg_prof(losses, "opp_prof")

    divergence = {k: loss_prof.get(k, 0.0) - win_prof.get(k, 0.0)
                  for k in set(win_prof) | set(loss_prof)}
    keys = sorted(set(win_prof) | set(loss_prof) | set(opp_loss_prof),
                  key=lambda k: -abs(divergence.get(k, 0.0)))

    print(f"{'op':<20}{'US/win':>9}{'US/loss':>9}{'OPP/loss':>10}"
          f"{'loss-win':>10}{'opp-us(loss)':>13}")
    for k in keys:
        w, l, o = win_prof.get(k, 0.0), loss_prof.get(k, 0.0), opp_loss_prof.get(k, 0.0)
        if max(w, l, o) < 1.0:
            continue
        print(f"{k:<20}{w:>9.1f}{l:>9.1f}{o:>10.1f}{l - w:>+10.1f}{o - l:>+13.1f}")

    if losses:
        print(f"\nmoney delta by day, avg across {len(losses)} losses "
              f"(negative = behind):")
        for day in CHECK_DAYS:
            pts = [tp for r in losses for tp in r["curve"] if tp["day"] == day]
            if pts:
                md = sum(p["money_delta"] for p in pts) / len(pts)
                op_ = sum(p["our_plants"] for p in pts) / len(pts)
                ap_ = sum(p["opp_plants"] for p in pts) / len(pts)
                oa_ = sum(p["our_animals"] for p in pts) / len(pts)
                aa_ = sum(p["opp_animals"] for p in pts) / len(pts)
                print(f"  day {day:>2}: money {md:>+9,.0f}  "
                      f"plants {op_:.1f}/{ap_:.1f}  animals {oa_:.1f}/{aa_:.1f}")

    worst = sorted(losses, key=lambda r: r["margin"])[:10]
    if worst:
        print(f"\nworst {len(worst)} losses:")
        for r in worst:
            print(f"  {r['opponent']:<20} seed={r['seed']:<12} margin={r['margin']:>+10,.0f}")

    return {"agent": name, "rows": rows, "divergence": divergence}


def main():
    argv = sys.argv[1:]
    workers = max(1, (os.cpu_count() or 4) - 2)
    out_path = Path("/kaggle/working/loss_analysis.json")
    n_opponents = None
    n_seeds = 0
    offset = 0
    agents = []
    i = 0
    while i < len(argv):
        if argv[i] == "--workers":
            workers = int(argv[i + 1]); i += 2
        elif argv[i] == "--out":
            out_path = Path(argv[i + 1]); i += 2
        elif argv[i] == "--opponents":
            n_opponents = int(argv[i + 1]); i += 2
        elif argv[i] == "--seeds":
            n_seeds = int(argv[i + 1]); i += 2
        elif argv[i] == "--offset":
            offset = int(argv[i + 1]); i += 2
        else:
            agents.append(argv[i]); i += 1
    if not agents:
        # Kaggle/kg-bisect convention: agents-under-test are flat a_*.py
        # (same glob run_bisect.py uses). Fall back to local dev filenames.
        agents = sorted(glob.glob(str(HERE / "a_*.py")))
        if not agents:
            agents = [str(HERE / a) for a in DEFAULT_AGENTS if (HERE / a).exists()]
        if not agents:
            raise SystemExit("no agent given and none of the defaults exist here")

    seeds = json.loads((HERE / "seeds.json").read_text()) if (HERE / "seeds.json").exists() else {}
    opps = find_opponents()
    if n_opponents:
        opps = opps[:n_opponents]
    # same generator run_bisect.py's n_random mode / top_tournament.py --mode
    # random use, so seeds line up across tools. n_seeds=0 keeps recorded mode
    # (1 game/opponent/seat, its own home tape seed) -- unchanged default.
    pool_seeds = [(k * 2654435761) % 2147483647
                  for k in range(offset + 1, offset + n_seeds + 1)] if n_seeds else None
    games_per_agent = 2 * len(opps) * (n_seeds if n_seeds else 1)
    mode = f"random x{n_seeds} offset {offset}" if n_seeds else "recorded"
    print(f"agents={len(agents)} opponents={len(opps)} mode={mode} "
          f"games/agent={games_per_agent} workers={workers}", flush=True)

    t0 = time.time()
    results = [analyze_agent(a, opps, seeds, workers, pool_seeds) for a in agents]
    print(f"\n({time.time() - t0:.0f}s total)")

    if len(results) > 1:
        print(f"\n{'=' * 70}\nSHARED ACROSS ALL {len(results)} AGENTS "
              f"(same-direction divergence, |avg| >= 5)\n{'=' * 70}")
        all_keys = set()
        for r in results:
            all_keys |= set(r["divergence"])
        for k in sorted(all_keys, key=lambda k: -abs(
                sum(r["divergence"].get(k, 0.0) for r in results) / len(results))):
            vals = [r["divergence"].get(k, 0.0) for r in results]
            if all(v > 0 for v in vals) or all(v < 0 for v in vals):
                avg = sum(vals) / len(vals)
                if abs(avg) >= 5:
                    per_agent = "  ".join(f"{r['agent']}={v:+.1f}" for r, v in zip(results, vals))
                    print(f"  {k:<20} avg {avg:+.1f}   {per_agent}")

    out_path.write_text(json.dumps(
        {r["agent"]: r["rows"] for r in results}, indent=2, default=str), encoding="utf-8")
    print(f"\nwrote {out_path}")


if __name__ == "__main__":
    mp.freeze_support()
    main()
