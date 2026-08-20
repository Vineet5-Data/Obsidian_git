"""Day-windowed economic loss analysis: net cash generated per window, by product.

Three windows (per the observed pattern -- competitive early, falls apart late):
  0-19    baseline
  20-24   first collapse window
  25-29   second / terminal collapse window

Mechanics below are copied verbatim from the installed engine
(kaggle_environments/envs/kaggriculture/kaggriculture.py) so costs that are
fixed-price are EXACT, not estimated:
  - BUY_SEED  = CROPS[item]["seed"]            (engine L12-17, L590)
  - BUY_ANIMAL= ANIMALS[item]["cost"]           (engine L20-23, L592)
  - BUY_LAND  = LAND_PRICES[n_already_unlocked] (engine L84, L699-712)
  - HIRE      = mult * fib(hires_today)         (engine L677-694)
  - FEED costs no money -- it consumes 1 WHEAT from hand inventory (L492-500);
    reported as an action count, not a $ figure.

Only SELL / BUY_PRODUCT are dynamically priced (engine's per-unit lockstep,
L531-615): each unit's price depends on live shared market inventory, which
shifts as BOTH players trade the same step. Replaying that loop exactly needs
the joint order stream; instead this uses the PRE-TRADE quoted price
(market["prices"][item], read straight from the observation -- market_price()
itself is reproduced verbatim below so the quote is exact) x units requested.
That is an approximation only in how much a single multi-unit order walks the
price against itself/the opponent intra-step -- T constants (100-450) are
large versus a typical order, so slippage is small. Marked ~ in the report.
Reconciled against net_cash (money delta, always exact) so any gap is visible.

"Production" per product = shed delta across the window + units sold + units
consumed as BUY_PRODUCT outflow -- shed is the only place harvested/bought
goods sit before being sold, so this is an exact mass balance, not an estimate,
regardless of whether it came from crop yield, animal product, or purchase.

Usage:  python _econ_loss_analysis.py [agent1.py agent2.py ...] [--workers N] [--out path.json]
        [--opponents N] [--seeds N] [--offset N]
--opponents N: use only first N .top/ opponents (fewer opponents, not more games).
--seeds N: N fresh seeds per opponent instead of its 1 recorded/home seed
  (same generator as run_bisect.py's random mode) -- games/agent = 2*opponents*N.
--offset N: skip the first N seeds (only matters with --seeds).
No agents given -> flat a_*.py (Kaggle/kg-bisect convention), else local dev filenames.
Opponents from .top/ (any attached dataset, mount path auto-detected).
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
    """.top/ lives in the grid-search dataset, not here. Mount path varies."""
    for pattern in ("/kaggle/input/**/t_*.py",
                     str(HERE / ".top" / "t_*.py"),
                     str(HERE / "t_*.py"),
                     ".top/t_*.py",
                     "t_*.py"):
        hits = sorted(glob.glob(pattern, recursive=True))
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


def snapshot_at(steps, i, seat):
    """Full economic state for `seat` at step i. i=0 is the pre-day-0 initial state."""
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


def scan_orders(steps, day_lo, day_hi, seat):
    """Sum SELL/BUY_SEED/BUY_ANIMAL/BUY_PRODUCT order quantities across
    [day_lo, day_hi] inclusive. Revenue/spend on SELL/BUY_PRODUCT use the
    pre-trade quoted price (~approx, see module docstring); seed/animal
    costs are fixed (exact)."""
    lo_step = 0 if day_lo == 0 else day_end_step(steps, day_lo - 1)
    hi_step = day_end_step(steps, day_hi)
    revenue, units_sold = Counter(), Counter()
    spend_seed, spend_animal = Counter(), Counter()
    buy_prod_spend, buy_prod_units = Counter(), Counter()
    # FEED/FERTILIZE pull 1 WHEAT/FERTILIZER out of shed-via-inventory with no
    # market order attached (engine L492-500, L462-469) -- without subtracting
    # these, the shed mass-balance below misreads consumption as negative
    # production. Counts attempted actions, not verified-successful ones (same
    # requested-not-verified tradeoff as BUY_SEED/BUY_ANIMAL qty above).
    feed_actions = fertilize_actions = 0

    for i in range(lo_step + 1, hi_step + 1):
        a = steps[i][seat].get("action") or {}
        if not isinstance(a, dict):
            continue
        for u in [a.get("farmer")] + list(a.get("hands") or []):
            if isinstance(u, list) and u:
                if u[0] == "FEED":
                    feed_actions += 1
                elif u[0] == "FERTILIZE":
                    fertilize_actions += 1
        if not a.get("market"):
            continue
        prices = steps[i - 1][0]["observation"]["market"]["prices"]
        for order in a["market"]:
            if not order or len(order) < 3:
                continue
            op, item = order[0], order[1]
            try:
                qty = int(order[2])
            except (TypeError, ValueError):
                continue
            if qty <= 0:
                continue
            if op == "SELL" and item in PRODUCTS:
                units_sold[item] += qty
                revenue[item] += qty * prices.get(item, 0)
            elif op == "BUY_SEED" and item in CROPS:
                spend_seed[item] += qty * CROPS[item]["seed"]
            elif op == "BUY_ANIMAL" and item in ANIMALS:
                spend_animal[item] += qty * ANIMALS[item]["cost"]
            elif op == "BUY_PRODUCT" and item in ("WHEAT", "FERTILIZER"):
                buy_prod_units[item] += qty
                buy_prod_spend[item] += qty * prices.get(item, 0)

    return (revenue, units_sold, spend_seed, spend_animal, buy_prod_spend, buy_prod_units,
            feed_actions, fertilize_actions)


def window_econ(steps, lo_day, hi_day, seat, start_snap, day_snaps):
    end_snap = day_snaps[hi_day]
    (revenue, units_sold, spend_seed, spend_animal, buy_prod_spend, buy_prod_units,
     feed_actions, fertilize_actions) = scan_orders(steps, lo_day, hi_day, seat)

    wages = sum(sum(_fib(k) for k in range(day_snaps[d]["hires_today"]))
                for d in range(lo_day, hi_day + 1))

    land_spend, prev_land = 0.0, start_snap["land"]
    for d in range(lo_day, hi_day + 1):
        L = day_snaps[d]["land"]
        if L > prev_land:
            land_spend += sum(LAND_PRICES[k - 1] for k in range(prev_land, L))
        prev_land = L

    consumed = {"WHEAT": feed_actions, "FERTILIZER": fertilize_actions}
    production = {item: (end_snap["shed"].get(item, 0) - start_snap["shed"].get(item, 0)
                          + units_sold.get(item, 0) - buy_prod_units.get(item, 0)
                          + consumed.get(item, 0))
                  for item in PRODUCTS}

    return {
        "net_cash": end_snap["money"] - start_snap["money"],
        "revenue": dict(revenue), "units_sold": dict(units_sold),
        "realized_price": {k: revenue[k] / units_sold[k] for k in units_sold if units_sold[k]},
        "spend_seed": dict(spend_seed), "spend_animal": dict(spend_animal),
        "spend_buy_product": dict(buy_prod_spend),
        "feed_actions": feed_actions, "fertilize_actions": fertilize_actions,
        "spend_land": land_spend, "spend_wage": wages,
        "production": production,
        "plants_end": dict(end_snap["plants"]), "animals_end": dict(end_snap["animals"]),
    }


def one(job):
    """Run one game, return exact per-window economics for both seats (never raw steps)."""
    agent_path, opp_path, seed, seat, opp_name = job
    from kaggle_environments import make
    a, b = load(agent_path), load(opp_path)
    pair = [a, b] if seat == 0 else [b, a]
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run(pair)
    steps = env.steps
    margin = steps[-1][seat].reward - steps[-1][1 - seat].reward

    our_day_snaps = [snapshot_at(steps, day_end_step(steps, d), seat) for d in range(30)]
    opp_day_snaps = [snapshot_at(steps, day_end_step(steps, d), 1 - seat) for d in range(30)]
    our_init = snapshot_at(steps, 0, seat)
    opp_init = snapshot_at(steps, 0, 1 - seat)

    windows = {}
    for label, lo, hi in WINDOWS:
        our_start = our_day_snaps[lo - 1] if lo > 0 else our_init
        opp_start = opp_day_snaps[lo - 1] if lo > 0 else opp_init
        windows[label] = {
            "us": window_econ(steps, lo, hi, seat, our_start, our_day_snaps),
            "opp": window_econ(steps, lo, hi, 1 - seat, opp_start, opp_day_snaps),
        }

    return {"opponent": opp_name, "seed": seed, "seat": seat, "margin": margin,
            "win": margin > 0, "windows": windows}


SCALAR_FIELDS = {"net_cash", "spend_land", "spend_wage", "feed_actions", "fertilize_actions"}
SCALAR_LABELS = {"net_cash": "net cash generated", "spend_land": "land spend",
                  "spend_wage": "wage spend", "feed_actions": "feed actions (count)",
                  "fertilize_actions": "fertilize actions (count)"}
DICT_LABELS = {"revenue": "revenue ~(pre-trade quote)", "production": "production (units, exact)",
               "spend_seed": "seed spend", "spend_animal": "animal spend",
               "spend_buy_product": "buy_product spend ~(pre-trade quote)",
               "plants_end": "crop tiles, end of window", "animals_end": "herd, end of window"}


def report_window(label, rows, field):
    """field: scalar (SCALAR_FIELDS) or a per-product dict field name."""
    us_vals, opp_vals = [], []
    us_prod, opp_prod = Counter(), Counter()
    n = len(rows)
    if n == 0:
        return
    for r in rows:
        w = r["windows"][label]
        if field in SCALAR_FIELDS:
            us_vals.append(w["us"][field])
            opp_vals.append(w["opp"][field])
        else:
            for k, v in w["us"][field].items():
                us_prod[k] += v
            for k, v in w["opp"][field].items():
                opp_prod[k] += v

    if field in SCALAR_FIELDS:
        us_mean = sum(us_vals) / n
        opp_mean = sum(opp_vals) / n
        print(f"  {SCALAR_LABELS[field]}, day {label:<8} us {us_mean:>+12,.1f}   "
              f"opp {opp_mean:>+12,.1f}   gap (opp-us) {opp_mean - us_mean:>+12,.1f}   (n={n})")
        return opp_mean - us_mean

    us_avg = {k: v / n for k, v in us_prod.items()}
    opp_avg = {k: v / n for k, v in opp_prod.items()}
    keys = sorted(set(us_avg) | set(opp_avg),
                  key=lambda k: -abs(opp_avg.get(k, 0) - us_avg.get(k, 0)))
    print(f"    {DICT_LABELS.get(field, field)}:")
    for k in keys:
        u, o = us_avg.get(k, 0.0), opp_avg.get(k, 0.0)
        if abs(u) < 0.5 and abs(o) < 0.5:
            continue
        print(f"      {k:<12} us {u:>+10,.1f}   opp {o:>+10,.1f}   gap {o - u:>+10,.1f}")


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
    print(f"\n{'=' * 78}\n{name}: {len(wins)}-{len(losses)} "
          f"({100 * len(wins) / len(rows):.1f}%)\n{'=' * 78}")

    for cut_name, cut_rows in (("ALL GAMES", rows), ("LOSSES ONLY", losses)):
        if not cut_rows:
            continue
        print(f"\n-- {cut_name} (n={len(cut_rows)}) --")
        for label, _, _ in WINDOWS:
            report_window(label, cut_rows, "net_cash")
            report_window(label, cut_rows, "revenue")
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

    return {"agent": name, "rows": rows}


def main():
    argv = sys.argv[1:]
    workers = max(1, (os.cpu_count() or 4) - 2)
    out_path = Path("/kaggle/working/econ_loss_analysis.json")
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

    out_path.write_text(json.dumps(
        {r["agent"]: r["rows"] for r in results}, indent=2, default=str), encoding="utf-8")
    print(f"\nwrote {out_path}")


if __name__ == "__main__":
    mp.freeze_support()
    main()
