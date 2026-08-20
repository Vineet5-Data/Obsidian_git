"""Where does g1's money NOT come from?  Per-day trace of the whole pipeline."""
import importlib.util, sys
from collections import Counter


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "g1.py"
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 7
    from kaggle_environments import make
    me = load(path, "me").agent
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run([me, me])

    sold = Counter()
    revenue = Counter()
    ops = Counter()
    print(f"{'day':>4}{'money':>9}{'shed':>6}{'plants':>7}{'animals':>8}"
          f"{'weeds':>6}{'empty':>6}{'hands':>6}{'shops':>6}")
    for d in range(30):
        s = min(719, d * 24 + 23)
        o = env.steps[s][0]["observation"]
        f = o["farms"][0]
        pl = an = we = em = 0
        for row in f["tiles"]:
            for t in row:
                if t is None:
                    em += 1
                elif isinstance(t, dict):
                    if t.get("kind") == "PLANT":
                        pl += 1
                    elif "animal" in t:
                        an += 1
                    elif t.get("kind") == "WEED":
                        we += 1
        shed = sum(env.steps[s][0]["observation"]["private"]["shed"].values())
        print(f"{d:>4}{int(f['money']):>9,}{shed:>6}{pl:>7}{an:>8}{we:>6}{em:>6}"
              f"{len(f['hands']):>6}{len(o['town']['unlocked_shops']):>6}")

    for i in range(1, 720):
        a = env.steps[i][0].get("action") or {}
        for u in [a.get("farmer")] + list(a.get("hands") or []):
            if isinstance(u, list) and u:
                ops[u[0]] += 1
        prev = env.steps[i - 1][0]["observation"]["market"]["inventory"]
        for o in (a.get("market") or []):
            if o and o[0] == "SELL":
                sold[o[1]] += int(o[2])
            elif o:
                ops["mkt:" + o[0]] += 1

    inv0 = env.steps[0][0]["observation"]["market"]["inventory"]
    invE = env.steps[-1][0]["observation"]["market"]["inventory"]
    print("\nunit ops:", dict(ops.most_common()))
    print("sell requests:", dict(sold.most_common()))
    print("market inv delta:", {k: invE[k] - inv0[k] for k in invE if invE[k] != inv0[k]})
    print("shops:", env.steps[-1][0]["observation"]["town"]["unlocked_shops"])
    print("final:", int(env.steps[-1][0].reward), int(env.steps[-1][1].reward))


if __name__ == "__main__":
    main()
