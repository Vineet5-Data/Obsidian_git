"""Day-by-day diff of two agents over the opening, run solo on the same seed."""
import importlib.util
import itertools
import sys
from collections import Counter

from kaggle_environments import make

_uid = itertools.count()


def load(p):
    s = importlib.util.spec_from_file_location("a%d" % next(_uid), p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def trace(path, seed, last_day):
    env = make("kaggriculture", configuration={"seed": seed})
    env.run([load(path).agent, "pass"])
    rows = []
    for day in range(last_day + 1):
        st = env.steps[day * 24 + 23]
        f = st[0]["observation"]["farms"][0]
        tc = Counter()
        for row in f["tiles"]:
            for t in row:
                if t is None:
                    tc["empty"] += 1
                elif t == "LOCKED":
                    tc["lock"] += 1
                elif isinstance(t, dict) and t.get("kind") == "PLANT":
                    tc[t["crop"][:4]] += 1
                elif isinstance(t, dict) and "animal" in t:
                    tc[t["animal"][:3]] += 1
                else:
                    tc["pen"] += 1
        rows.append((day, f["money"], len(f["unlocked_quadrants"]), tc))
    return rows


if __name__ == "__main__":
    a, b = sys.argv[1], sys.argv[2]
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 1000
    last = int(sys.argv[4]) if len(sys.argv) > 4 else 14
    ra, rb = trace(a, seed, last), trace(b, seed, last)
    keys = ("COW", "SHE", "STRA", "MELO", "WHEA", "empty")
    print("day |            %-22s |            %-22s" % (a, b))
    for (d, ma, qa, ta), (_, mb, qb, tb) in zip(ra, rb):
        fa = " ".join("%s%d" % (k[:2], ta.get(k, 0)) for k in keys)
        fb = " ".join("%s%d" % (k[:2], tb.get(k, 0)) for k in keys)
        print("d%-2d | $%8.0f q%d %-30s | $%8.0f q%d %-30s" % (d, ma, qa, fa, mb, qb, fb))
