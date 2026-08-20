"""Benchmark v75_merged against top-player agent files in a directory.

Usage:
  python bench/benchmark_vs_top.py --top-dir PATH --agent PATH --episodes N

Produces a JSON summary to `bench/results.json` with per-opponent average rewards.
"""

import argparse
import importlib.util
import json
import os
import sys
from statistics import mean


def load_agent(path):
    spec = importlib.util.spec_from_file_location(os.path.splitext(os.path.basename(path))[0], path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if not hasattr(mod, "agent"):
        raise RuntimeError(f"agent module {path} must define agent(obs, config=None)")
    return mod.agent


def run_match(env, left_agent, right_agent, seed, steps=720):
    env = env
    env.configuration["seed"] = seed
    env.reset()
    env.run([left_agent, right_agent])
    last = env.steps[-1]
    # last is list of two obs
    if isinstance(last, (list, tuple)):
        return [last[0].get("reward"), last[1].get("reward")]
    return [None, None]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--top-dir", required=True)
    parser.add_argument("--agent", required=True)
    parser.add_argument("--episodes", type=int, default=5)
    args = parser.parse_args()

    try:
        from kaggle_environments import make
    except Exception as e:
        print("kaggle_environments not available:", e, file=sys.stderr)
        sys.exit(2)

    top_files = [os.path.join(args.top_dir, f) for f in os.listdir(args.top_dir)
                 if f.endswith('.py')]
    top_files = [f for f in top_files if os.path.basename(f).lower() != 'seb.py']
    agent_fn = load_agent(args.agent)

    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": 7})

    results = {}
    for top_path in sorted(top_files):
        name = os.path.splitext(os.path.basename(top_path))[0]
        try:
            top_fn = load_agent(top_path)
        except Exception as e:
            print(f"Skipping {top_path}: {e}")
            continue
        rewards_v75 = []
        rewards_top = []
        for i in range(args.episodes):
            seed = 1000 + i
            # v75 as player 0
            r0, r1 = run_match(env, agent_fn, top_fn, seed)
            rewards_v75.append(r0)
            rewards_top.append(r1)
            # swap seats
            r0b, r1b = run_match(env, top_fn, agent_fn, seed + 999)
            # when swapping, v75 reward is r1b
            rewards_v75.append(r1b)
            rewards_top.append(r0b)
        results[name] = {
            "v75_mean": mean([r for r in rewards_v75 if r is not None]),
            "top_mean": mean([r for r in rewards_top if r is not None]),
            "v75_rewards": rewards_v75,
            "top_rewards": rewards_top,
        }
        print(f"Finished vs {name}: v75_mean={results[name]['v75_mean']:.1f} top_mean={results[name]['top_mean']:.1f}")

    out_dir = os.path.join(os.path.dirname(__file__), '..', 'bench')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'results.json')
    with open(out_path, 'w', encoding='utf-8') as fh:
        json.dump(results, fh, indent=2)
    print('Wrote', out_path)


if __name__ == '__main__':
    main()
