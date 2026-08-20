"""Head-to-head config duel: the only metric that matches the leaderboard.

Evaluating against `starter` is misleading - it sells almost nothing, so a solo agent
gets the whole town drain to itself and every premium price stays high. Two real agents
split that same pool, which changes the optimal build. So configs are compared by playing
them against each other, both sides, over N seeds.

Usage:  python duel.py            # built-in candidate list vs the current default
"""
import importlib.util
import sys

from kaggle_environments import make


def load(path, cfg=None):
    spec = importlib.util.spec_from_file_location("cand_" + str(id(cfg)), path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    for k, v in (cfg or {}).items():
        setattr(m, k, v)
    return m


def duel(path_a, cfg_a, path_b, cfg_b, seeds):
    """Play A vs B on every seed, both seatings. Returns (a_wins, b_wins, a_mean, b_mean)."""
    aw = bw = 0
    a_tot = b_tot = 0.0
    n = 0
    for sd in seeds:
        for swap in (False, True):
            ma, mb = load(path_a, cfg_a), load(path_b, cfg_b)
            agents = [mb.agent, ma.agent] if swap else [ma.agent, mb.agent]
            env = make("kaggriculture", configuration={"seed": sd})
            env.run(agents)
            r = env.steps[-1]
            a = r[1]["reward"] if swap else r[0]["reward"]
            b = r[0]["reward"] if swap else r[1]["reward"]
            aw += a > b
            bw += b > a
            a_tot += a
            b_tot += b
            n += 1
    return aw, bw, a_tot / n, b_tot / n


if __name__ == "__main__":
    seeds = (1000, 1001, 1002)
    base = ("v2.py", {})
    cands = {
        "3quad_noCarrot": ("v2.py", dict(MAX_EXTRA_QUADS=2, CARROT_FROM=99)),
        "3quad_carrot":   ("v2.py", dict(MAX_EXTRA_QUADS=2)),
        "4quad":          ("v2.py", dict(MAX_EXTRA_QUADS=3)),
        "v1_oldmarket":   ("main.py", {}),
    }
    ref_name, ref = "3quad_noCarrot", cands["3quad_noCarrot"]
    for name, (p, c) in cands.items():
        if name == ref_name:
            continue
        aw, bw, am, bm = duel(ref[0], ref[1], p, c, seeds)
        print("%-16s vs %-16s  %d-%d   mean %7.0f vs %7.0f" % (ref_name, name, aw, bw, am, bm), flush=True)
