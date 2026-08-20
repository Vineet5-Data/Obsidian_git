"""Does the agent survive a market regime change?

The stated worry: "as the kaggle market price will change our agent will not
perform."  That is directly testable -- the engine takes a `marketParams`
override and _resolve_market_params merges it sparsely onto the defaults.  So
we can rewrite the price model under the agent's feet and re-measure.

If the agent's edge holds across regimes, the market layer is robust and the
clone risk is confined to production.  If it collapses, the worry is confirmed
and the market layer must be rebuilt.
"""
import importlib.util
import multiprocessing as mp
import os
import statistics
import sys

SCENARIOS = {
    "baseline": {},
    # the good we depend on most gets cut in half
    "milk_crash": {"MILK": {"base": 80}},
    # the good we under-produce doubles
    "wool_boom": {"WOOL": {"base": 400}},
    # the only balanced market collapses
    "wheat_collapse": {"WHEAT": {"base": 10}},
    # every premium good loses 40%
    "premium_bear": {"STRAWBERRY": {"base": 72}, "MILK": {"base": 96},
                     "WOOL": {"base": 120}, "MELON": {"base": 150}},
    # gluts bite twice as hard everywhere
    "steep_glut": {"STRAWBERRY": {"above_target": 3.2},
                   "MILK": {"above_target": 3.2},
                   "WOOL": {"above_target": 6.4},
                   "MELON": {"above_target": 7.2}},
    # demand-side shock: the town drains far less
    "thin_demand": {"WHEAT": {"T": 200}, "STRAWBERRY": {"T": 50},
                    "MILK": {"T": 61}, "WOOL": {"T": 52}},
}


def fresh(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def one(job):
    scenario, a_path, b_path, seed, seat = job
    from kaggle_environments import make
    a = fresh(a_path, f"a_{seed}_{seat}").agent
    b = fresh(b_path, f"b_{seed}_{seat}").agent
    pair = [a, b] if seat == 0 else [b, a]
    config = {"episodeSteps": 720, "seed": seed,
              "marketParams": SCENARIOS[scenario]}
    env = make("kaggriculture", configuration=config)
    env.run(pair)
    final = env.steps[-1]
    return scenario, final[seat].reward - final[1 - seat].reward


def main():
    agent = sys.argv[1] if len(sys.argv) > 1 else "v26.py"
    opponent = sys.argv[2] if len(sys.argv) > 2 else ".loss/o_90711580.py"
    n = int(sys.argv[3]) if len(sys.argv) > 3 else 8
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, n + 1)]
    jobs = [(s, agent, opponent, seed, seat)
            for s in SCENARIOS for seed in seeds for seat in (0, 1)]
    with mp.Pool(max(1, (os.cpu_count() or 4) - 2)) as pool:
        results = pool.map(one, jobs)

    table = {}
    for scenario, margin in results:
        table.setdefault(scenario, []).append(margin)
    print(f"{os.path.basename(agent)} vs {os.path.basename(opponent)}  "
          f"-- {n} seeds x 2 seats per regime\n")
    print(f"{'regime':16s} {'W-L':>8} {'win%':>6} {'mean':>9} {'worst':>9}")
    for scenario in SCENARIOS:
        margins = table.get(scenario, [])
        if not margins:
            continue
        w = sum(1 for m in margins if m > 0)
        print(f"{scenario:16s} {f'{w}-{len(margins) - w}':>8} "
              f"{100 * w / len(margins):>5.1f}% "
              f"{statistics.mean(margins):>+9,.0f} {min(margins):>+9,.0f}")


if __name__ == "__main__":
    mp.freeze_support()
    main()
