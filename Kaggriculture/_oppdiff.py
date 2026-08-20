"""Why do 90880659 / 90909137 / 90896452 beat v46_a 0-12?

These panel opponents are verbatim replay tapes, so we cannot copy them (and
would not want to -- an opaque tape cannot be explained or debugged). But the
tape decodes to a plain list of actions, and an action mix IS explainable.
The goal is to find the mechanism, then build our own version of it.

Counts are normalised per 1000 unit-turns, because a farm with more hands does
more of everything and raw counts would just measure headcount.

Usage:  python _oppdiff.py v46_a.py
"""
import base64
import importlib.util
import json
import re
import sys
import zlib
from collections import Counter

MOVES = {"NORTH", "SOUTH", "EAST", "WEST"}
KILLERS = ["p_90880659", "p_90909137", "p_90896452"]   # beat us 0-12
LOSERS = ["p_90874645"]                                # we beat 12-0


def tape(path):
    """Pull the embedded action list out of a replay module without running it."""
    src = open(path, encoding="utf-8").read()
    blob = "".join(re.findall(r"'([A-Za-z0-9+/=]+)'", src))
    return json.loads(zlib.decompress(base64.b64decode(blob)))


def mix(actions):
    """-> per-1000-unit-turn op profile + a few economy tallies."""
    ops = Counter()
    for a in actions:
        if not isinstance(a, dict):
            continue
        for u in [a.get("farmer")] + list(a.get("hands") or []):
            if isinstance(u, list) and u:
                ops[u[0]] += 1
        for o in (a.get("market") or []):
            if o:
                ops["mkt:" + o[0]] += 1
    unit = sum(v for k, v in ops.items() if not k.startswith("mkt:"))
    prof = {k: 1000.0 * v / unit for k, v in ops.items()} if unit else {}
    return prof, unit


def ours(agent_path, seed=101):
    from kaggle_environments import make
    spec = importlib.util.spec_from_file_location("me", agent_path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run([m.agent, m.agent])
    acts = [st[0].get("action") for st in env.steps[1:]]
    prof, unit = mix(acts)
    return prof, unit, int(env.steps[-1][0].reward)


def avg(paths):
    acc, tot, n = Counter(), 0, 0
    for p in paths:
        prof, unit = mix(tape(p))
        if not prof:
            continue
        for k, v in prof.items():
            acc[k] += v
        tot += unit
        n += 1
    return {k: v / n for k, v in acc.items()}, tot / max(n, 1)


if __name__ == "__main__":
    agent = sys.argv[1] if len(sys.argv) > 1 else "v46_a.py"
    kill, ku = avg([f".pure/{k}.py" for k in KILLERS])
    lose, lu = avg([f".pure/{k}.py" for k in LOSERS])
    mine, mu, score = ours(agent)

    print(f"KILLERS (beat us 0-12): {', '.join(KILLERS)}   avg {ku:,.0f} unit-turns")
    print(f"PUNCHBAG (we beat 12-0): {', '.join(LOSERS)}   avg {lu:,.0f} unit-turns")
    print(f"OURS {agent}: score {score:,}, {mu:,} unit-turns\n")

    keys = sorted(set(kill) | set(mine) | set(lose),
                  key=lambda k: -(kill.get(k, 0)))
    print(f"{'op':<20}{'KILLER/1k':>11}{'OURS/1k':>10}{'BAG/1k':>10}{'ours-killer':>13}")
    for k in keys:
        a, b, c = kill.get(k, 0.0), mine.get(k, 0.0), lose.get(k, 0.0)
        if max(a, b, c) < 1.0:
            continue
        print(f"{k:<20}{a:>11.1f}{b:>10.1f}{c:>10.1f}{b - a:>+13.1f}")

    for name, d in (("MOVE total", MOVES),):
        ka = sum(v for x, v in kill.items() if x in d)
        ma = sum(v for x, v in mine.items() if x in d)
        la = sum(v for x, v in lose.items() if x in d)
        print(f"\n{name:<20}{ka:>11.1f}{ma:>10.1f}{la:>10.1f}{ma - ka:>+13.1f}")
    print(f"{'unit-turns':<20}{ku:>11,.0f}{mu:>10,.0f}{lu:>10,.0f}{mu - ku:>+13,.0f}")
