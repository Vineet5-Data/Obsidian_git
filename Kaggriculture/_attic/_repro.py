"""Reproduce the four ladder losses locally.

Extracts each opponent's tape straight out of the loss replay (with the
steps[N+1] off-by-one fix), builds an agent from it, and replays v24 against it
at the episode's own seed.  If the local margin matches the replay's margin the
loss is reproducible and we have a target to optimise against.  If v24 wins
locally, the tape does not capture whatever actually beat us.
"""
import glob
import json
import importlib.util
import os
import zlib

from kaggle_environments import make

import _mkv24

LOSSES = r"C:\Users\Vinee\Desktop\Kaggriculture\recent _loss"
OUT = r"C:\Users\Vinee\Desktop\Kaggriculture\.loss"


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.agent


def extract(path):
    with open(path, encoding="utf-8") as handle:
        replay = json.load(handle)
    steps = replay["steps"]
    info = replay.get("info") or {}
    names = info.get("TeamNames") or ["p0", "p1"]
    seat = 0 if "vineet" in names[0].lower() else 1
    opp = 1 - seat
    seed = info.get("seed")
    if seed is None:
        seed = (replay.get("configuration") or {}).get("seed")
    # action applied to observation N is stored in steps[N + 1]
    tape = [steps[i + 1][opp].get("action") or {"farmer": ["PASS"],
                                                "hands": [], "market": []}
            for i in range(len(steps) - 1)]
    final = steps[-1]
    margin = (final[seat].get("reward") or 0) - (final[opp].get("reward") or 0)
    return {
        "episode": os.path.splitext(os.path.basename(path))[0],
        "names": names, "seat": seat, "opp": opp, "seed": seed,
        "tape": tape, "replay_margin": margin,
        "me_reward": final[seat].get("reward"),
        "opp_reward": final[opp].get("reward"),
    }


def main():
    os.makedirs(OUT, exist_ok=True)
    champion = load("v24.py", "champion")
    print(f"{'episode':>12} {'opponent':22} {'seed':>10} "
          f"{'replay':>9} {'local':>9}  reproduced?")
    for path in sorted(glob.glob(os.path.join(LOSSES, "*.json"))):
        info = extract(path)
        blob = os.path.join(OUT, f"{info['episode']}.json.z")
        with open(blob, "wb") as handle:
            handle.write(zlib.compress(
                json.dumps(info["tape"], separators=(",", ":")).encode(), 9))
        agent_path = os.path.join(OUT, f"o_{info['episode']}.py")
        _mkv24.build(blob, agent_path, f"Loss opponent {info['episode']}.")
        opponent = load(agent_path, "o_" + info["episode"])

        config = {"episodeSteps": 720}
        if info["seed"] is not None:
            config["seed"] = info["seed"]
        seat = info["seat"]
        pair = ([champion, opponent] if seat == 0 else [opponent, champion])
        env = make("kaggriculture", configuration=config)
        env.run(pair)
        final = env.steps[-1]
        local = final[seat].reward - final[1 - seat].reward
        same = "YES" if (local < 0) == (info["replay_margin"] < 0) else "NO"
        print(f"{info['episode']:>12} {info['names'][info['opp']][:22]:22} "
              f"{str(info['seed'])[:10]:>10} {info['replay_margin']:>+9,.0f} "
              f"{local:>+9,.0f}  {same}")


if __name__ == "__main__":
    main()
