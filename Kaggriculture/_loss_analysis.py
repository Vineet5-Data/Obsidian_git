"""Where do our agents lose, and what's different when they do?

Combines four existing diagnostics instead of a new methodology:
  - _oppdiff.py / _topops.py's per-1000-unit-turn op-mix normalisation
  - _analyze_losses.py's day-by-day money/asset turning points
  - run_bisect.py's mount-robust opponent glob + multiprocessing skeleton
  - _econ_loss_analysis.py's day-windowed economic loss analysis

Usage:  python _loss_analysis.py [agent1.py agent2.py ...] [--workers N] [--out path.json]
        [--opponents N] [--seeds N] [--offset N]
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
TELEMETRY_WINDOWS = [("0-14", 0, 14), ("15-19", 15, 19),
                     ("20-24", 20, 24), ("25-29", 25, 29)]
DEFAULT_AGENTS = ["v108_nopump.py", "v97_cap70.py", "100v.py"]

TURNS_PER_DAY = 24
WINDOWS = [("0-19", 0, 19), ("20-24", 20, 24), ("25-29", 25, 29)]

CROPS = {
    "WHEAT":      {"seed": 10},
    "CARROT":     {"seed": 20},
    "TOMATO":     {"seed": 50},
    "STRAWBERRY": {"seed": 100},
    "MELON":      {"seed": 80},
}
ANIMALS = {
    "GOOSE": {"cost": 300}, "COW": {"cost": 400}, "SHEEP": {"cost": 500},
}
PRODUCTS = ["WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON", "EGG", "MILK", "WOOL", "FERTILIZER"]
LAND_PRICES = [1000, 2000, 4000]

def _fib(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def find_opponents():
    """Locate the .top/ opponent tapes.

    Mount path varies: the grid-search dataset may land flat under
    /kaggle/input/<slug>/ or nested in a .top/ subdirectory, at a depth that
    is not fixed.  recursive=True is load-bearing -- without it "**" collapses
    to a single "*" and only matches one directory level.
    """
    for pattern in ("/kaggle/input/**/.top/t_*.py",
                    "/kaggle/input/**/t_*.py",
                    str(HERE / ".top" / "t_*.py"),
                    str(HERE / "t_*.py"),
                    ".top/t_*.py",
                    "t_*.py"):
        hits = sorted(glob.glob(pattern, recursive=True))
        if hits:
            return hits
    raise SystemExit(
        "no t_*.py opponent tapes found -- attach the grid_search dataset, or "
        "copy the tapes into a .top/ subdirectory next to this script")


def load_module(path):
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "m_" + os.path.basename(path).replace(".", "_"), path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

def op_mix(steps, seat):
    """-> per-1000-unit-turn op profile."""
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
    """-> (plant tiles, animal tiles) for one farm."""
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

def snapshot_at(steps, i, seat):
    """Full economic state for `seat` at step i."""
    obs = steps[i][seat]["observation"]
    farm = obs["farms"][seat]
    plants, animals = Counter(), Counter()
    for row in (farm.get("tiles") or []):
        for t in (row or []):
            if isinstance(t, dict):
                if t.get("kind") == "PLANT":
                    plants[t["crop"]] += 1
                elif "animal" in t:
                    animals[t["animal"]] += 1
    return {
        "money": farm.get("money", 0.0),
        "shed": dict(obs["private"]["shed"]),
        "hires_today": farm.get("hires_today", 0),
        "land": len(farm.get("unlocked_quadrants") or []),
        "plants": plants, "animals": animals,
    }

def day_end_step(steps, day):
    return min(len(steps) - 1, day * TURNS_PER_DAY + 23)

# Economic accounting lives in _econ_loss_analysis so there is exactly one
# copy of the market replay.  Both files ship side by side in every
# deployment (repo, kg-bisect, grid_search), so a flat import is enough.
from _econ_loss_analysis import replay_market, scan_orders, window_econ  # noqa: E402


def one(job):
    """Run one game, return a compact diagnostic summary."""
    agent_path, opp_path, seed, seat, opp_name = job
    from kaggle_environments import make
    agent_module = load_module(agent_path)
    opponent_module = load_module(opp_path)
    if hasattr(agent_module, "reset_telemetry"):
        agent_module.reset_telemetry()
    pair = ([agent_module.agent, opponent_module.agent] if seat == 0
            else [opponent_module.agent, agent_module.agent])
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

    telemetry = (agent_module.telemetry_snapshot()
                 if hasattr(agent_module, "telemetry_snapshot") else None)

    fills, replay_stats = replay_market(steps)

    our_day_snaps = [snapshot_at(steps, day_end_step(steps, d), seat) for d in range(30)]
    opp_day_snaps = [snapshot_at(steps, day_end_step(steps, d), 1 - seat) for d in range(30)]
    our_init = snapshot_at(steps, 0, seat)
    opp_init = snapshot_at(steps, 0, 1 - seat)

    windows = {}
    for label, lo, hi in WINDOWS:
        our_start = our_day_snaps[lo - 1] if lo > 0 else our_init
        opp_start = opp_day_snaps[lo - 1] if lo > 0 else opp_init
        windows[label] = {
            "us": window_econ(steps, lo, hi, seat, our_start, our_day_snaps, fills),
            "opp": window_econ(steps, lo, hi, 1 - seat, opp_start, opp_day_snaps, fills),
        }

    return {"opponent": opp_name, "seed": seed, "seat": seat, "margin": margin,
            "win": margin > 0, "our_prof": our_prof, "our_unit": our_unit,
            "opp_prof": opp_prof, "opp_unit": opp_unit, "curve": curve,
            "telemetry": telemetry, "windows": windows,
            "replay_stats": dict(replay_stats)}

def avg_prof(rows, key):
    acc, n = Counter(), 0
    for r in rows:
        if r[key]:
            for k, v in r[key].items():
                acc[k] += v
            n += 1
    return {k: v / n for k, v in acc.items()} if n else {}

def telemetry_window_totals(rows, lo_day, hi_day):
    stages = ("created", "admitted", "assigned", "emitted", "executed", "failed", "unknown")
    totals = {stage: Counter() for stage in stages}
    caps, expiries = Counter(), Counter()
    movement = passes = 0
    games = 0
    for result in rows:
        snapshot = result.get("telemetry")
        if not snapshot: continue
        games += 1
        for episode in snapshot.get("episodes", []):
            for day_key, day_row in episode.get("days", {}).items():
                try: day = int(day_key)
                except: continue
                if not lo_day <= day <= hi_day: continue
                for stage in stages:
                    totals[stage].update(day_row.get(stage, {}))
                caps.update(day_row.get("animal_cap_ticks", {}))
                expiries.update(day_row.get("crop_expiry_with_yield", {}))
                movement += int(day_row.get("movement_turns", 0) or 0)
                passes += int(day_row.get("pass_turns", 0) or 0)
    return games, totals, caps, expiries, movement, passes

def report_telemetry(cut_name, rows):
    if not any(r.get("telemetry") for r in rows): return
    print(f"\n-- SERVICE TELEMETRY: {cut_name} --")
    for label, lo_day, hi_day in TELEMETRY_WINDOWS:
        games, totals, caps, expiries, movement, passes = telemetry_window_totals(rows, lo_day, hi_day)
        if not games: continue
        game_days = games * (hi_day - lo_day + 1)
        operations = sorted(set().union(*(set(v) for v in totals.values())))
        print(f"\n  days {label} (telemetry games={games})")
        print(f"    {'operation':<20}{'created/g':>11}{'admit%':>9}"
              f"{'assign%':>10}{'emitted/g':>11}{'exec/day':>10}"
              f"{'exec%':>8}{'unknown%':>10}")
        for operation in operations:
            created = totals["created"][operation]
            admitted = totals["admitted"][operation]
            assigned = totals["assigned"][operation]
            emitted = totals["emitted"][operation]
            executed = totals["executed"][operation]
            failed = totals["failed"][operation]
            unknown = totals["unknown"][operation]
            admit_rate = 100.0 * admitted / created if created else 0.0
            assign_rate = 100.0 * assigned / admitted if admitted else 0.0
            known = executed + failed
            execution_rate = 100.0 * executed / known if known else 0.0
            unknown_rate = 100.0 * unknown / emitted if emitted else 0.0
            print(f"    {operation:<20}{created / games:>11.1f}"
                  f"{admit_rate:>8.1f}%{assign_rate:>9.1f}%"
                  f"{emitted / games:>11.1f}{executed / game_days:>10.2f}"
                  f"{execution_rate:>7.1f}%{unknown_rate:>9.1f}%")
        print(f"    movement turns/game-day: {movement / game_days:.2f}"
              f"   PASS turns/game-day: {passes / game_days:.2f}")
        if caps:
            cap_text = ", ".join(f"{item}={count / game_days:.2f}/day" for item, count in sorted(caps.items()))
            print(f"    animal cap ticks: {cap_text}")
        if expiries:
            expiry_text = ", ".join(f"{item}={count / games:.2f}/game" for item, count in sorted(expiries.items()))
            print(f"    crop expiry with held yield: {expiry_text}")

SCALAR_FIELDS = {"net_cash", "cash_residual", "spend_land", "spend_wage",
                 "feed_actions", "fertilize_actions"}
SCALAR_LABELS = {"net_cash": "net cash generated",
                  "cash_residual": "cash residual (should be ~0)", "spend_land": "land spend",
                  "spend_wage": "wage spend", "feed_actions": "feed actions (count)",
                  "fertilize_actions": "fertilize actions (count)"}
DICT_LABELS = {"revenue": "revenue (filled, exact)", "production": "production (units, exact)",
               "spend_seed": "seed spend", "spend_animal": "animal spend",
               "spend_buy_product": "buy_product spend (filled, exact)",
               "plants_end": "crop tiles, end of window", "animals_end": "herd, end of window",
               "realized_price": "avg realized price / unit (revenue/sold)"}

def report_window(label, rows, field):
    us_vals, opp_vals = [], []
    us_prod, opp_prod = Counter(), Counter()
    n = len(rows)
    if n == 0: return
    for r in rows:
        w = r["windows"][label]
        if field in SCALAR_FIELDS:
            us_vals.append(w["us"][field])
            opp_vals.append(w["opp"][field])
        else:
            for k, v in w["us"][field].items(): us_prod[k] += v
            for k, v in w["opp"][field].items(): opp_prod[k] += v

    if field in SCALAR_FIELDS:
        us_mean = sum(us_vals) / n
        opp_mean = sum(opp_vals) / n
        print(f"  {SCALAR_LABELS[field]}, day {label:<8} us {us_mean:>+12,.1f}   "
              f"opp {opp_mean:>+12,.1f}   gap (opp-us) {opp_mean - us_mean:>+12,.1f}   (n={n})")
        return opp_mean - us_mean

    if field == "realized_price":
        # A price is a ratio, not an additive quantity: average it as
        # total revenue / total units, not as the mean of per-game ratios
        # divided by ALL games (which silently counts a game that sold none
        # of an item as a $0 price and halves the reported figure).
        us_avg, opp_avg = {}, {}
        for side, out in (("us", us_avg), ("opp", opp_avg)):
            rev, qty = Counter(), Counter()
            for r in rows:
                w = r["windows"][label][side]
                rev.update(w["revenue"])
                qty.update(w["units_sold"])
            for k, q in qty.items():
                if q:
                    out[k] = rev.get(k, 0) / q
    else:
        us_avg = {k: v / n for k, v in us_prod.items()}
        opp_avg = {k: v / n for k, v in opp_prod.items()}
    keys = sorted(set(us_avg) | set(opp_avg), key=lambda k: -abs(opp_avg.get(k, 0) - us_avg.get(k, 0)))
    print(f"    {DICT_LABELS.get(field, field)}:")
    for k in keys:
        u, o = us_avg.get(k, 0.0), opp_avg.get(k, 0.0)
        if abs(u) < 0.1 and abs(o) < 0.1: continue
        print(f"      {k:<12} us {u:>+10,.2f}   opp {o:>+10,.2f}   gap {o - u:>+10,.2f}")

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

    divergence = {k: loss_prof.get(k, 0.0) - win_prof.get(k, 0.0) for k in set(win_prof) | set(loss_prof)}
    keys = sorted(set(win_prof) | set(loss_prof) | set(opp_loss_prof), key=lambda k: -abs(divergence.get(k, 0.0)))

    print(f"{'op':<20}{'US/win':>9}{'US/loss':>9}{'OPP/loss':>10}{'loss-win':>10}{'opp-us(loss)':>13}")
    for k in keys:
        w, l, o = win_prof.get(k, 0.0), loss_prof.get(k, 0.0), opp_loss_prof.get(k, 0.0)
        if max(w, l, o) < 1.0: continue
        print(f"{k:<20}{w:>9.1f}{l:>9.1f}{o:>10.1f}{l - w:>+10.1f}{o - l:>+13.1f}")

    if losses:
        print(f"\nmoney delta by day, avg across {len(losses)} losses (negative = behind):")
        for day in CHECK_DAYS:
            pts = [tp for r in losses for tp in r["curve"] if tp["day"] == day]
            if pts:
                md = sum(p["money_delta"] for p in pts) / len(pts)
                op_ = sum(p["our_plants"] for p in pts) / len(pts)
                ap_ = sum(p["opp_plants"] for p in pts) / len(pts)
                oa_ = sum(p["our_animals"] for p in pts) / len(pts)
                aa_ = sum(p["opp_animals"] for p in pts) / len(pts)
                print(f"  day {day:>2}: money {md:>+9,.0f}  plants {op_:.1f}/{ap_:.1f}  animals {oa_:.1f}/{aa_:.1f}")

    worst = sorted(losses, key=lambda r: r["margin"])[:10]
    if worst:
        print(f"\nworst {len(worst)} losses:")
        for r in worst:
            print(f"  {r['opponent']:<20} seed={r['seed']:<12} margin={r['margin']:>+10,.0f}")

    report_telemetry("ALL GAMES", rows)
    report_telemetry("LOSSES ONLY", losses)

    print(f"\n{'=' * 78}\n{name}: {len(wins)}-{len(losses)} "
          f"({100 * len(wins) / len(rows):.1f}%)\n{'=' * 78}")
    for cut_name, cut_rows in (("ALL GAMES", rows), ("LOSSES ONLY", losses)):
        if not cut_rows: continue
        print(f"\n-- {cut_name} (n={len(cut_rows)}) --")
        for label, _, _ in WINDOWS:
            report_window(label, cut_rows, "net_cash")
            report_window(label, cut_rows, "cash_residual")
            report_window(label, cut_rows, "revenue")
            report_window(label, cut_rows, "realized_price")
            report_window(label, cut_rows, "production")
            report_window(label, cut_rows, "spend_seed")
            report_window(label, cut_rows, "spend_animal")
            report_window(label, cut_rows, "spend_buy_product")
            report_window(label, cut_rows, "spend_land")
            report_window(label, cut_rows, "spend_wage")
            report_window(label, cut_rows, "feed_actions")
            report_window(label, cut_rows, "fertilize_actions")
            report_window(label, cut_rows, "plants_end")
            report_window(label, cut_rows, "animals_end")

    return {"agent": name, "rows": rows, "divergence": divergence}

def main():
    argv = sys.argv[1:]
    workers = max(1, (os.cpu_count() or 4) - 2)
    
    out_path = Path("loss_analysis.json")
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
        agents = sorted(glob.glob(str(HERE / "a_*.py")))
        if not agents:
            agents = [str(HERE / a) for a in DEFAULT_AGENTS if (HERE / a).exists()]
        if not agents:
            raise SystemExit("no agent given and none of the defaults exist here")

    seeds = json.loads((HERE / "seeds.json").read_text()) if (HERE / "seeds.json").exists() else {}
    opps = find_opponents()
    if n_opponents:
        opps = opps[:n_opponents]
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
