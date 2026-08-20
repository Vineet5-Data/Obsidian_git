"""Co-adapted evolution over v26's market channel, seeded from the current tape.

Why this and not another bolt-on layer.  Seventy-five parametric policies were
measured and every one lost; the tape is a tightly-coupled local optimum across
production, timing AND cash, so nothing that wraps it helps.  The only lever
left is editing the tape itself, co-adapted against live opponents.

Why the MARKET channel only.  farmer/hands ops are relative moves -- one edit
desyncs every later step and the genome dies before it can be scored.  Market
orders are position-independent, so an edit is always semantically valid.  And
the channel is not just selling: HIRE / BUY_ANIMAL / BUY_SEED live there, so
mutating it changes the PRODUCTION PLAN (labour, herd, crop mix) while leaving
the movement tape intact.  That is the co-adaptation the bolt-on layers could
not reach.

Genome: sparse {step: market_list} overriding the base tape.  Empty = v26, so
generation 0 starts exactly at the current agent and can only improve.

Honesty: training seeds are disjoint from _panel.py's (i=1..24), so the 288-game
panel stays an out-of-sample test of whatever this finds.

Usage:  python _evolve.py [gens] [pop]        # resumes from .evo/state.json
"""
import copy
import hashlib
import importlib.util
import json
import multiprocessing as mp
import os
import random
import statistics
import sys
import time

BASE = "v26.py"
STATE = ".evo/state.json"

# equal weight per opponent; the two structural losses are half the train set
TRAIN = [
    ".loss/o_90729118.py",      # mirror -- we are 0-48 here
    ".field/f_90639963_p1.py",  # Seb 4-quadrant milk flood -- 6-42
    ".loss/o_90711580.py",      # family B (Nat Bel)
    "wufang_agent.py",          # current ladder top
]
# disjoint from _panel.py (i = 1..24) so the panel stays out of sample
TRAIN_SEEDS = [(i * 2654435761) % 2147483647 for i in (1001, 1002)]

POP, ELITES = 20, 6
MAX_ORDERS = 10             # engine cap: maxMarketOrdersPerTurn
MAX_EDITS = 40              # genome size cap -- keeps edits interpretable
QTY_ITEMS = ("WHEAT", "MELON", "STRAWBERRY", "MILK", "WOOL", "FERTILIZER")


# --------------------------------------------------------------------------
# genome
# --------------------------------------------------------------------------
def fresh(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_BASE_TAPE = None


def base_tape():
    global _BASE_TAPE
    if _BASE_TAPE is None:
        _BASE_TAPE = fresh(BASE, "_evo_base")._ACTIONS
    return _BASE_TAPE


def key(genome):
    return hashlib.sha1(json.dumps(genome, sort_keys=True).encode()).hexdigest()


def mutate(genome, rng):
    """One minimal edit, then a single size guard (all exits route here)."""
    genome = _edit(genome, rng)
    while len(genome) > MAX_EDITS:
        del genome[rng.choice(list(genome))]
    return genome


def _edit(genome, rng):
    """One minimal edit.  Minimal because the herd search proved the opposite:

    a bulk 'move everything toward the target' operator scored -54,329 where a
    keep-what-works single substitution reproduced the passthrough exactly.  A
    tightly-coupled tape only survives small perturbations."""
    genome = {int(k): copy.deepcopy(v) for k, v in genome.items()}
    tape = base_tape()

    def orders(step):
        if step in genome:
            return genome[step]
        return copy.deepcopy(list(tape[step].get("market") or []))

    op = rng.choice(["qty", "swap", "drop", "shift", "insert", "hire", "herd",
                     "revert"])

    if op == "revert" and genome:                    # escape a bad edit
        del genome[rng.choice(list(genome))]
        return genome

    if op in ("hire", "herd"):                       # production levers
        step = rng.randrange(0, 96)                  # first 4 days only
        cur = orders(step)
        if len(cur) < MAX_ORDERS:
            cur = cur + ([["HIRE"]] if op == "hire" else
                         [["BUY_ANIMAL", rng.choice(("COW", "SHEEP")),
                           rng.randint(1, 2)]])
            genome[step] = cur
        return genome

    # steps that actually carry orders -- editing an empty turn does nothing
    live = [s for s in range(len(tape)) if orders(s)]
    if not live:
        return genome
    step = rng.choice(live)
    cur = orders(step)

    if op == "qty":
        i = rng.randrange(len(cur))
        order = list(cur[i])
        if len(order) >= 3 and isinstance(order[2], int):
            order[2] = max(1, order[2] + rng.choice((-3, -2, -1, 1, 2, 3)))
            cur = cur[:i] + [order] + cur[i + 1:]
    elif op == "swap" and len(cur) > 1:
        # slot index IS the match index against the rival -- reordering is real
        i, j = rng.sample(range(len(cur)), 2)
        cur = list(cur)
        cur[i], cur[j] = cur[j], cur[i]
    elif op == "drop":
        cur = cur[:rng.randrange(len(cur))] + cur[rng.randrange(len(cur)) + 1:]
    elif op == "shift":
        i = rng.randrange(len(cur))
        dest = min(len(tape) - 1, max(0, step + rng.choice((-4, -2, -1, 1, 2, 4))))
        moved = cur[i]
        cur = cur[:i] + cur[i + 1:]
        target = orders(dest)
        if len(target) < MAX_ORDERS:
            genome[dest] = target + [moved]
    elif op == "insert" and len(cur) < MAX_ORDERS:
        cur = cur + [["SELL", rng.choice(QTY_ITEMS), rng.randint(1, 6)]]

    genome[step] = cur[:MAX_ORDERS]
    return genome


def build(genome, tag):
    module = fresh(BASE, "evo_" + tag)
    for step, market in genome.items():
        module._ACTIONS[int(step)]["market"] = copy.deepcopy(market)
    return module.agent


# --------------------------------------------------------------------------
# fitness
# --------------------------------------------------------------------------
def one(job):
    payload, opponent_path, seed, seat = job
    from kaggle_environments import make
    tag = f"{seed}_{seat}_{os.getpid()}"
    agent = build(json.loads(payload), tag)
    rival = fresh(opponent_path, "riv_" + tag).agent
    pair = [agent, rival] if seat == 0 else [rival, agent]
    env = make("kaggriculture",
               configuration={"episodeSteps": 720, "seed": seed})
    env.run(pair)
    final = env.steps[-1]
    return opponent_path, final[seat].reward - final[1 - seat].reward


def jobs_for(payload):
    return [(payload, o, s, seat)
            for o in TRAIN if os.path.exists(o)
            for s in TRAIN_SEEDS for seat in (0, 1)]


def score(results):
    """Equal weight per opponent, plus a nudge toward flipping whole games.

    Plain mean lets a +90k rout against one archetype hide an 0-4 against the
    mirror, which is the exact failure we are trying to fix."""
    by_opponent = {}
    for path, margin in results:
        by_opponent.setdefault(path, []).append(margin)
    margins = [m for _, m in results]
    wins = sum(1 for m in margins if m > 0)
    per_opponent = statistics.mean(
        statistics.mean(v) for v in by_opponent.values())
    return per_opponent + 5000 * wins / len(margins), wins, len(margins)


# --------------------------------------------------------------------------
# driver
# --------------------------------------------------------------------------
def main():
    gens = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    pop_size = int(sys.argv[2]) if len(sys.argv) > 2 else POP
    rng = random.Random(20260807)
    os.makedirs(".evo", exist_ok=True)

    if os.path.exists(STATE):
        saved = json.load(open(STATE))
        pop = [(f, {int(k): v for k, v in g.items()}) for f, g in saved["pop"]]
        cache = saved["cache"]
        gen0 = saved["gen"]
        print(f"resumed at gen {gen0}, best {pop[0][0]:+,.0f}", flush=True)
    else:
        pop, cache, gen0 = [], {}, 0

    workers = max(1, (os.cpu_count() or 4) - 2)
    n_games = len(jobs_for("{}"))
    with mp.Pool(workers) as pool:
        if not pop:                                   # gen 0 == plain v26
            results = pool.map(one, jobs_for("{}"))
            fitness, wins, total = score(results)
            cache[key({})] = fitness
            pop = [(fitness, {})]
            print(f"gen  0  baseline v26  fit {fitness:+,.0f}  "
                  f"{wins}-{total - wins}", flush=True)

        for gen in range(gen0 + 1, gens + 1):
            t0 = time.time()
            children = []
            while len(children) < pop_size - min(ELITES, len(pop)):
                parent = pop[rng.randrange(min(ELITES, len(pop)))][1]
                child = mutate(parent, rng)
                for _ in range(rng.randint(0, 2)):    # occasional double edit
                    child = mutate(child, rng)
                if key(child) not in cache:
                    children.append(child)
                    cache[key(child)] = None          # reserve
            flat = [j for c in children for j in jobs_for(json.dumps(c))]
            raw = pool.map(one, flat)
            scored = []
            for i, child in enumerate(children):
                chunk = raw[i * n_games:(i + 1) * n_games]
                fitness, wins, total = score(chunk)
                cache[key(child)] = fitness
                scored.append((fitness, child, wins))
            pop = sorted(pop + [(f, c) for f, c, _ in scored],
                         key=lambda r: -r[0])[:pop_size]
            best_wins = max((w for _, _, w in scored), default=0)
            print(f"gen {gen:2d}  best {pop[0][0]:+,.0f}  "
                  f"edits {len(pop[0][1]):2d}  child_best_wins {best_wins}/"
                  f"{n_games}  {time.time() - t0:.0f}s", flush=True)
            json.dump({"gen": gen, "pop": pop, "cache": cache},
                      open(STATE, "w"))
            json.dump(pop[0][1], open(".evo/best.json", "w"))

    print(f"\nbest fitness {pop[0][0]:+,.0f} with {len(pop[0][1])} edits "
          f"-> .evo/best.json", flush=True)
    print("validate out-of-sample:  python _evoval.py", flush=True)


def demo():
    """Self-check: empty genome must reproduce v26 byte-for-byte, and every
    mutation operator must leave a tape the engine will accept."""
    rng = random.Random(0)
    assert build({}, "chk").__module__.startswith("evo_")
    plain = fresh(BASE, "plain")._ACTIONS
    assert build({}, "chk2") is not None and plain == base_tape()
    g = {}
    for _ in range(400):
        g = mutate(g, rng)
        assert len(g) <= MAX_EDITS, len(g)
        for step, market in g.items():
            assert 0 <= int(step) < 720
            assert len(market) <= MAX_ORDERS
            for order in market:
                assert isinstance(order, list) and order
    build(g, "chk3")
    print(f"ok -- {len(g)} edits survive, tape valid")


if __name__ == "__main__":
    mp.freeze_support()
    if "--demo" in sys.argv:
        demo()
    else:
        main()
