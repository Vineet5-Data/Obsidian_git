"""What is the mirror's market timing actually worth, and which edits carry it?

Discovery: .loss/o_90729118.py is not a rival strategy.  It is OUR OWN family-A
route -- farmer and hands channels identical over all 719 shared steps -- with
68 steps of market-channel differences.  So the 0-48 record and its tight
-869..-2,001 band is a pure market-timing deficit, not a production deficit.

Phase 1 measures the ceiling: graft all 68 mirror market steps onto v26 and
replay against the mirror.  If the margin goes to ~0 the deficit is fully
explained by timing.

Phase 2 bisects to the minimal carrying subset, so we can read a RULE out of it
instead of shipping 68 copied cells.  Copying the cells would be the cloning the
brief forbids; the rule is the deliverable.

Usage:  python _mirror.py [phase] [n_seeds]
        phase: ceiling | bisect
"""
import json
import multiprocessing as mp
import os
import statistics
import sys

import _evolve

MIRROR = ".loss/o_90729118.py"
EDITS = ".evo/mirror_market.json"


def one(job):
    payload, opponent, seed, seat = job
    from kaggle_environments import make
    tag = f"{seed}_{seat}_{os.getpid()}"
    agent = _evolve.build(json.loads(payload), tag)
    rival = _evolve.fresh(opponent, "riv_" + tag).agent
    pair = [agent, rival] if seat == 0 else [rival, agent]
    env = make("kaggriculture",
               configuration={"episodeSteps": 720, "seed": seed})
    env.run(pair)
    final = env.steps[-1]
    return final[seat].reward - final[1 - seat].reward


def measure(variants, seeds, opponent=MIRROR):
    """variants: list of (label, genome).  Returns label -> margins."""
    jobs, index = [], []
    for label, genome in variants:
        payload = json.dumps({str(k): v for k, v in genome.items()})
        for seed in seeds:
            for seat in (0, 1):
                jobs.append((payload, opponent, seed, seat))
                index.append(label)
    workers = max(1, (os.cpu_count() or 4) - 2)
    with mp.Pool(workers) as pool:
        raw = pool.map(one, jobs)
    out = {}
    for label, margin in zip(index, raw):
        out.setdefault(label, []).append(margin)
    return out


def report(table):
    print(f"{'variant':22s} {'W-L':>8} {'win%':>6} {'mean':>9} "
          f"{'worst':>9} {'best':>9}")
    for label, margins in table.items():
        w = sum(1 for m in margins if m > 0)
        print(f"{label:22s} {f'{w}-{len(margins) - w}':>8} "
              f"{100 * w / len(margins):>5.1f}% "
              f"{statistics.mean(margins):>+9,.0f} "
              f"{min(margins):>+9,.0f} {max(margins):>+9,.0f}")


def main():
    phase = sys.argv[1] if len(sys.argv) > 1 else "ceiling"
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, n + 1)]
    full = {int(k): v for k, v in json.load(open(EDITS)).items()}
    steps = sorted(full)

    if phase == "ceiling":
        variants = [("v26 (control)", {}), ("all 68 mirror edits", full)]
        # halves already, so a positive result localises immediately
        half = len(steps) // 2
        variants.append(("first half (34)",
                         {s: full[s] for s in steps[:half]}))
        variants.append(("second half (34)",
                         {s: full[s] for s in steps[half:]}))
        table = measure(variants, seeds)
        print(f"vs mirror -- {n} seeds x 2 seats\n")
        report(table)
        return

    # bisect: leave-one-block-out over the surviving side
    keep = [int(s) for s in (sys.argv[3].split(",") if len(sys.argv) > 3
                             else [str(s) for s in steps])]
    blocks = 8
    size = max(1, len(keep) // blocks)
    variants = [("all kept", {s: full[s] for s in keep})]
    for b in range(0, len(keep), size):
        drop = set(keep[b:b + size])
        variants.append((f"drop {keep[b]}..{keep[min(b + size, len(keep)) - 1]}",
                         {s: full[s] for s in keep if s not in drop}))
    table = measure(variants, seeds)
    print(f"leave-block-out over {len(keep)} edits -- {n} seeds x 2 seats\n")
    report(table)


if __name__ == "__main__":
    mp.freeze_support()
    main()
