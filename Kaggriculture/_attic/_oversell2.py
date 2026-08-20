"""Over-request every SELL and let the engine clamp to the shed.

Mohit Rao (top-10) requests 2,363 STRAWBERRY while producing ~300; the engine
sells min(request, shed) so the surplus request is free.  Effect: the shed is
drained every turn, so nothing is stranded when production exceeds what the
tape assumed -- and our idle CARE/WATER layer does raise production above the
recorded plan.

Shed capacity is 100 with end-of-day overflow DISCARDED, so under-selling is
not neutral, it destroys goods.

Variants: exact shed amount, tape qty + margin, and a flat large request.
Panel = the six real losses plus the distinct top-leaderboard builds, all on
engine 1.32.6 where every recorded game reproduces exactly.
"""
import glob, importlib.util, multiprocessing as mp, os, statistics

BASE = "v33.py"
PANEL = sorted(glob.glob(".pure/p_*.py")) + [
    ".top/t_90914286_0.py",   # Seb (allegedly), top scorer 137,616
    ".top/t_90913514_1.py",   # Mohit Rao, over-request build
    ".top/t_90916037_1.py",   # mrgrishninsb
    ".top/t_90920155_1.py",   # CemBas
    ".top/t_90904143_0.py",   # kakuteki
    ".top/t_90916074_1.py",   # Ueddy wheat-heavy
]
# Dumping the whole shed starved the herd: FEED consumes WHEAT from the shed
# via PICKUP, so WHEAT in store is INPUT, not surplus.  Protect the inputs and
# over-request only true produce.
FEED = {"WHEAT"}
INPUTS = {"WHEAT", "FERTILIZER"}
PRESETS = {
    "off":        None,
    "nowheat":    {"mode": "shed", "skip": FEED},
    "produce":    {"mode": "shed", "skip": INPUTS},
    "produce+8":  {"mode": "shed", "skip": INPUTS, "pad": 8},
}

def load(p, n):
    s = importlib.util.spec_from_file_location(n, p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def build(preset, tag):
    m = load(BASE, "o_" + tag)
    P = PRESETS[preset]
    if P is None:
        return m.agent
    inner = m.agent
    def agent(obs):
        act = inner(obs)
        try:
            shed = {k: max(0, int(v or 0)) for k, v in dict(m._get(
                m._get(obs, "private", {}) or {}, "shed", {}) or {}).items()}
            out = []
            for o in (act.get("market") or []):
                if (o and o[0] == "SELL" and len(o) >= 3
                        and o[1] not in P.get("skip", ())):
                    q = max(int(o[2]), shed.get(o[1], 0) + P.get("pad", 0))
                    out.append([o[0], o[1], max(1, q)])
                else:
                    out.append(o)
            act["market"] = out[:10]
        except Exception:
            pass
        return act
    return agent

def one(job):
    preset, opp, seed, seat = job
    from kaggle_environments import make
    tag = f"{preset}_{abs(hash(opp))%999}_{seed}_{seat}_{os.getpid()}"
    a = build(preset, tag); b = load(opp, "r_" + tag).agent
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run([a, b] if seat == 0 else [b, a])
    f = env.steps[-1]
    return (preset, opp), f[seat].reward - f[1 - seat].reward

def main():
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, 4)]
    jobs = [(p, o, s, seat) for p in PRESETS for o in PANEL if os.path.exists(o)
            for s in seeds for seat in (0, 1)]
    print(f"{len(jobs)} games", flush=True)
    with mp.Pool(10) as pool:
        res = pool.map(one, jobs)
    t = {}
    for k, v in res: t.setdefault(k, []).append(v)
    print(f"\n{'preset':9s}{'W-L':>10s}{'win%':>8s}{'mean':>11s}{'worst':>11s}   per-opponent losses")
    for p in PRESETS:
        grand, cells = [], []
        for o in PANEL:
            v = t.get((p, o), [])
            if not v: continue
            grand += v
            n = sum(1 for x in v if x <= 0)
            if n: cells.append(f"{os.path.basename(o)[2:10]}:{n}")
        w = sum(1 for x in grand if x > 0)
        print(f"{p:9s}{f'{w}-{len(grand)-w}':>10s}{100*w/len(grand):>7.1f}%"
              f"{statistics.mean(grand):>+11,.0f}{min(grand):>+11,.0f}   {' '.join(cells)}")

if __name__ == "__main__":
    mp.freeze_support(); main()
