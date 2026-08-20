"""Final route selection: v24 variants (weed + impact, idle off) vs each other and v13."""
import collections
import importlib.util

from kaggle_environments import make

SEEDS = [9501, 9502, 9503]
CANDS = ["v24_thunder", "v24_khanh", "v24_youssef", "v24_venks"]


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.agent


def duel(a, b, seeds=SEEDS):
    wins = losses = ties = 0
    margins, banks = [], []
    for seed in seeds:
        for seat in (0, 1):
            pair = [a, b] if seat == 0 else [b, a]
            env = make("kaggriculture",
                       configuration={"episodeSteps": 720, "seed": seed})
            env.run(pair)
            final = env.steps[-1]
            mine, theirs = final[seat].reward, final[1 - seat].reward
            margins.append(mine - theirs)
            banks.append(mine)
            wins += mine > theirs
            losses += mine < theirs
            ties += mine == theirs
    return wins, losses, ties, sum(margins) / len(margins), sum(banks) / len(banks)


def main():
    agents = {c: load(c + ".py", c) for c in CANDS}
    v13 = load("v13.py", "v13")

    print(f"seeds {SEEDS}, 6 games per pairing\n--- vs v13 (incumbent) ---")
    for c in CANDS:
        w, l, t, margin, bank = duel(agents[c], v13)
        print(f"  {c:14s} {w}-{l}-{t}  margin {margin:+9,.0f}  bank {bank:9,.0f}",
              flush=True)

    print("\n--- head to head ---")
    wins = collections.Counter()
    losses = collections.Counter()
    margin_of = collections.defaultdict(list)
    bank_of = collections.defaultdict(list)
    for i, a in enumerate(CANDS):
        for b in CANDS[i + 1:]:
            w, l, t, margin, bank = duel(agents[a], agents[b])
            wins[a] += w
            losses[a] += l
            wins[b] += l
            losses[b] += w
            margin_of[a].append(margin)
            margin_of[b].append(-margin)
            bank_of[a].append(bank)
            print(f"  {a:14s} {w}-{l}-{t} {b:14s} margin {margin:+8,.0f}", flush=True)

    print("\n=== field standings (peers only) ===")
    rows = [(wins[c] - losses[c], sum(margin_of[c]) / max(1, len(margin_of[c])), c,
             wins[c], losses[c]) for c in CANDS]
    for _, margin, c, w, l in sorted(rows, reverse=True):
        print(f"  {c:14s} {w:2d}W-{l:2d}L  mean margin {margin:+8,.0f}")


if __name__ == "__main__":
    main()
