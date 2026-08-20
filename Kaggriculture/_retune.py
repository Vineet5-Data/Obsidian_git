"""Re-tune the FUNCTIONAL layers on engine 1.32.6 against the real field.

SMOOTH_START / WINDOW / CAP were fitted on 1.32.4, where the town centre fired
twice as often and demand scaled 4x after day 20.  Under 1.32.6 the town fires
every 24 steps with a flat multiplier, so the drain that makes spreading
profitable is roughly halved -- the old constants have no reason to still hold.

This tunes only our own layers.  No routes are swapped, nothing is copied.
"""
import glob, importlib.util, multiprocessing as mp, os, statistics

BASE = "v33.py"
PANEL = sorted(glob.glob(".pure/p_*.py")) + [
    ".top/t_90914286_0.py", ".top/t_90913514_1.py", ".top/t_90916037_1.py",
    ".top/t_90920155_1.py", ".top/t_90904143_0.py", ".top/t_90916074_1.py"]

# (SMOOTH_START, SMOOTH_WINDOW, SMOOTH_CAP, USE_SMOOTH)
PRESETS = {
    "shipped 250/8/5": (250, 8, 5, 1),
    "off":             (250, 8, 5, 0),
    "0/8/5":           (0, 8, 5, 1),
    "100/8/5":         (100, 8, 5, 1),
    "400/8/5":         (400, 8, 5, 1),
    "250/16/5":        (250, 16, 5, 1),
    "250/4/5":         (250, 4, 5, 1),
    "250/8/10":        (250, 8, 10, 1),
}

def load(p, n):
    s = importlib.util.spec_from_file_location(n, p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def one(job):
    preset, opp, seed, seat = job
    from kaggle_environments import make
    tag = f"{abs(hash(preset))%9999}_{abs(hash(opp))%999}_{seed}_{seat}_{os.getpid()}"
    m = load(BASE, "a_" + tag)
    st, win, cap, use = PRESETS[preset]
    m.SMOOTH_START, m.SMOOTH_WINDOW, m.SMOOTH_CAP, m.USE_SMOOTH = st, win, cap, use
    b = load(opp, "o_" + tag).agent
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run([m.agent, b] if seat == 0 else [b, m.agent])
    f = env.steps[-1]
    return (preset, opp), f[seat].reward - f[1 - seat].reward

def main():
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, 3)]
    jobs = [(p, o, s, seat) for p in PRESETS for o in PANEL if os.path.exists(o)
            for s in seeds for seat in (0, 1)]
    print(f"{len(jobs)} games", flush=True)
    with mp.Pool(10) as pool:
        res = pool.map(one, jobs)
    t = {}
    for k, v in res: t.setdefault(k, []).append(v)
    print(f"\n{'preset':18s}{'W-L':>10s}{'win%':>8s}{'mean':>11s}{'worst':>11s}")
    rows = []
    for p in PRESETS:
        grand = [x for o in PANEL for x in t.get((p, o), [])]
        w = sum(1 for x in grand if x > 0)
        rows.append((w, statistics.mean(grand), p, len(grand), min(grand)))
    for w, mean, p, n, worst in sorted(rows, key=lambda r: (-r[0], -r[1])):
        tag = "  <= shipped" if p.startswith("shipped") else ""
        print(f"{p:18s}{f'{w}-{n-w}':>10s}{100*w/n:>7.1f}%{mean:>+11,.0f}{worst:>+11,.0f}{tag}")

if __name__ == "__main__":
    mp.freeze_support(); main()
