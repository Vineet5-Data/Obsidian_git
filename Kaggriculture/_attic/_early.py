"""Seb runs 7 hands/day from day 0; we run 5,0,2,1,4,1,2.  Is that usable?

Hire cost is mult*fib(hires_today) with fib = [1,1,2,3,5,8,13,21,34,55,89] and
hires_today RESETTING EVERY DAY (hands are wiped nightly by _end_of_day).  So 7
hands for a full day costs $33 against $3,000 of starting cash -- the early
labour gap is not a money problem.

The open question is whether extra hands are USABLE: the tape scripts movement
only for the hands it actually hires, so surplus hands get PASS from _aligned,
and they spawn on the four shed-access tiles where _idle_fill finds no job.
An earlier injection at step 300 lost heavily, but that is the window where we
already hire 7-14/day.  This tests the starved early days instead.
"""
import importlib.util, multiprocessing as mp, os, statistics, sys

BASE = "v27.py"
PANEL = [(".field/f_90639963_p1.py", "Seb"), (".loss/o_90711580.py", "family B"),
         ("wufang_agent.py", "Wufang")]
# Both tapes hire ONLY at hours 0-1 of each day, so injecting from hour 2
# leaves every scripted hand index intact (the tape's own hires still come
# first) while the extra hands still get 22 working turns before the nightly
# wipe.  `hour` is the knob that separates a real extra hand from a desync.
PRESETS = {
    "off":         None,
    "h2_d0_6_to9":  {"days": range(0, 7),  "target": 9,  "hour": 2},
    "h2_all_to9":   {"days": range(0, 30), "target": 9,  "hour": 2},
    "h2_all_to12":  {"days": range(0, 30), "target": 12, "hour": 2},
    "h2_all_to14":  {"days": range(0, 30), "target": 14, "hour": 2},
    "h0_d0_6_to9":  {"days": range(0, 7),  "target": 9,  "hour": 0},
}

def fresh(path, name):
    s = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def built(preset, tag):
    module = fresh(BASE, "e_" + tag)
    P = PRESETS[preset]
    if P is None:
        return module.agent
    tape = module._ACTIONS
    for day in P["days"]:
        have = sum(1 for st in tape[day*24:(day+1)*24]
                   for o in (st.get("market") or []) if o and o[0] == "HIRE")
        need = P["target"] - have
        step = day * 24 + P.get("hour", 0)
        while need > 0 and step < (day + 1) * 24:
            cur = list(tape[step].get("market") or [])
            room = min(10 - len(cur), need)
            if room > 0:
                tape[step]["market"] = cur + [["HIRE"]] * room
                need -= room
            step += 1
    return module.agent

def one(job):
    preset, path, seed, seat = job
    from kaggle_environments import make
    tag = f"{preset}_{seed}_{seat}_{os.getpid()}"
    a = built(preset, tag); b = fresh(path, "o_" + tag).agent
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run([a, b] if seat == 0 else [b, a])
    f = env.steps[-1]
    return (preset, path), f[seat].reward - f[1 - seat].reward

def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, n + 1)]
    jobs = [(p, path, s, seat) for p in PRESETS for path, _ in PANEL
            if os.path.exists(path) for s in seeds for seat in (0, 1)]
    with mp.Pool(max(1, (os.cpu_count() or 4) - 2)) as pool:
        res = pool.map(one, jobs)
    t = {}
    for k, m in res: t.setdefault(k, []).append(m)
    print(f"early hiring -- {len(PANEL)} opponents x {n} seeds x 2 seats\n")
    print(f"{'preset':12s}" + "".join(f"{l:>12s}" for _, l in PANEL) + f"{'OVERALL':>12s}{'win%':>8s}")
    for p in PRESETS:
        cells, grand = [], []
        for path, _ in PANEL:
            ms = t.get((p, path), []); grand += ms
            cells.append(f"{statistics.mean(ms):>+12,.0f}" if ms else f"{'-':>12s}")
        w = sum(1 for m in grand if m > 0)
        tag = "  <= control (v27)" if p == "off" else ""
        print(f"{p:12s}" + "".join(cells) + f"{statistics.mean(grand):>+12,.0f}{100*w/len(grand):>7.1f}%{tag}")

if __name__ == "__main__":
    mp.freeze_support(); main()
