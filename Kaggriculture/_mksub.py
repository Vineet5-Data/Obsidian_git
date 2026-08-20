"""Package an agent into a Kaggriculture submission tarball, with a smoke test.

Matches the layout codex already used for submission_v36_final.tar.gz:

    main.py        -- entry point, re-exports `agent`
    <agent>.py     -- the policy itself

Usage:
    python _mksub.py v38.py submission_v36_final.tar.gz

Refuses to write the archive unless the agent imports cleanly, is stdlib-only,
plays a full 720-step episode to status DONE, and stays inside the per-turn
time budget.  A submission that fails any of those is worse than no submission.
"""
import ast
import importlib.util
import os
import sys
import tarfile
import time

BUDGET_MS = 1000.0
STDLIB_OK = {"math", "json", "zlib", "base64", "random", "collections",
             "itertools", "functools", "heapq", "bisect", "sys", "os", "time"}


def load(path):
    spec = importlib.util.spec_from_file_location("subagent", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def check_imports(path):
    """Only MODULE-LEVEL imports matter: those run when Kaggle imports the
    agent.  Imports nested inside `if __name__ == "__main__":` (the local
    self-test) never execute there, so walking the whole tree would reject a
    perfectly good submission over its own smoke test.
    """
    tree = ast.parse(open(path, encoding="utf-8").read())
    mods = set()
    for node in tree.body:                      # top level only, not ast.walk
        if isinstance(node, ast.Import):
            mods.update(a.name.split(".")[0] for a in node.names)
        elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
            mods.add(node.module.split(".")[0])
    return sorted(mods), sorted(mods - STDLIB_OK)


def smoke(path, seed=7):
    from kaggle_environments import make
    m = load(path)
    worst = [0.0]

    def timed(obs, cfg=None):
        t = time.perf_counter()
        r = m.agent(obs, cfg)
        worst[0] = max(worst[0], (time.perf_counter() - t) * 1000.0)
        return r

    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run([timed, m.agent])
    last = env.steps[-1]
    return str(last[0].status), int(last[0].reward), int(last[1].reward), worst[0]


def build(agent_path, out_path):
    name = os.path.basename(agent_path)
    stem = name[:-3]
    mods, bad = check_imports(agent_path)
    print(f"imports: {mods}")
    if bad:
        print(f"REFUSING: non-stdlib imports {bad}")
        return False
    status, mine, theirs, worst = smoke(agent_path)
    print(f"smoke: status={status} score={mine:,} vs {theirs:,} worst_turn={worst:.1f}ms")
    if status != "DONE":
        print(f"REFUSING: episode status {status}")
        return False
    if worst > BUDGET_MS:
        print(f"REFUSING: worst turn {worst:.1f}ms exceeds {BUDGET_MS:.0f}ms budget")
        return False

    entry = f'"""Kaggriculture submission entry point."""\n\nfrom {stem} import agent\n\n__all__ = ["agent"]\n'
    tmp = os.path.join(os.path.dirname(os.path.abspath(out_path)) or ".", "_main_entry.py")
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(entry)
    with tarfile.open(out_path, "w:gz") as tar:
        tar.add(tmp, arcname="main.py")
        tar.add(agent_path, arcname=name)
    os.remove(tmp)
    size = os.path.getsize(out_path)
    print(f"\nwrote {out_path} ({size:,} bytes)")
    with tarfile.open(out_path) as tar:
        for ti in tar.getmembers():
            print(f"   {ti.name:24} {ti.size:,} bytes")
    return True


if __name__ == "__main__":
    a = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else "submission.tar.gz"
    sys.exit(0 if build(a, out) else 1)
