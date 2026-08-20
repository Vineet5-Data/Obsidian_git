"""Round-robin among family-A candidates on seeds never used to pick them."""
import collections
import importlib.util

from kaggle_environments import make

SEEDS = [9201, 9202, 9203]
CANDS = ["cand_khanh", "cand_youssef", "cand_thunder",
         "cand_tman", "cand_venks", "cand_ocean"]


def load(path, name, idle=None):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if idle is not None:
        module.IDLE_WORK = idle
    return module.agent


def main():
    agents = {c: load(c + ".py", c, idle=0) for c in CANDS}
    wins = collections.Counter()
    losses = collections.Counter()
    margin = collections.defaultdict(list)
    banks = collections.defaultdict(list)
    for i, a in enumerate(CANDS):
        for b in CANDS[i + 1:]:
            for seed in SEEDS:
                for seat in (0, 1):
                    pair = [agents[a], agents[b]] if seat == 0 else [agents[b], agents[a]]
                    env = make("kaggriculture",
                               configuration={"episodeSteps": 720, "seed": seed})
                    env.run(pair)
                    final = env.steps[-1]
                    x, y = final[seat].reward, final[1 - seat].reward
                    banks[a].append(x)
                    banks[b].append(y)
                    margin[a].append(x - y)
                    margin[b].append(y - x)
                    if x > y:
                        wins[a] += 1
                        losses[b] += 1
                    elif y > x:
                        wins[b] += 1
                        losses[a] += 1
            print(f"  {a} vs {b} done", flush=True)
    print("\n=== round robin (seeds %s) ===" % SEEDS)
    rows = [(wins[c] - losses[c], sum(margin[c]) / max(1, len(margin[c])),
             c, wins[c], losses[c], sum(banks[c]) / max(1, len(banks[c])))
            for c in CANDS]
    for _, m, c, w, l, bank in sorted(rows, reverse=True):
        print(f"{c:16s} {w:2d}W-{l:2d}L  mean margin {m:+8,.0f}  mean bank {bank:9,.0f}")


if __name__ == "__main__":
    main()
