"""Are the seeds where route A loses identifiable from PUBLIC town state?

Route A's Khanh/Youssef losses sit on three specific seeds, not on the matchup.
Shop unlocks are drawn from a seed-keyed RNG every 3 days and the unlocked set
is public in obs.town, so the seed leaves an observable trace.  If the losing
seeds carry a distinct signature, the switch can be conditioned on it and fire
only when route A is actually going to lose.
"""
import importlib.util, multiprocessing as mp, os

def load(p, n):
    s = importlib.util.spec_from_file_location(n, p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

BAD = {654878655, 774553846, 894229037, 1042155578, 1429432501, 2056059806}
OPP = [(".field/f_90635979_p1.py", "Khanh"), (".field/f_90635229_p1.py", "Youssef"),
       ("wufang_agent.py", "Wufang"), (".loss/o_90729118.py", "mirror")]

def probe(job):
    path, label, seed = job
    from kaggle_environments import make
    tag = f"{label}_{seed}_{os.getpid()}"
    me = load("v30.py", "m_" + tag).agent
    b = load(path, "o_" + tag).agent
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run([me, b])
    shops = tuple(sorted(env.steps[200][0]["observation"]["town"]["unlocked_shops"]))
    margin = env.steps[-1][0].reward - env.steps[-1][1].reward
    return label, seed, shops, margin

def main():
    seeds = [(i * 2654435761) % 2147483647 for i in range(1, 25)]
    jobs = [(p, l, s) for p, l in OPP if os.path.exists(p) for s in seeds]
    with mp.Pool(max(1, (os.cpu_count() or 4) - 2)) as pool:
        rows = pool.map(probe, jobs)
    lose, win = {}, {}
    for label, seed, shops, margin in rows:
        (lose if margin <= 0 else win).setdefault(shops, set()).add(f"{label}")
    print("shop signature at step 200 -> outcome for route A\n")
    allsig = set(lose) | set(win)
    print(f"{'shops (unlocked at step 200)':62s}{'LOSES vs':>22s}{'wins vs':>22s}")
    for sig in sorted(allsig):
        print(f"{','.join(s[:6] for s in sig):62s}"
              f"{','.join(sorted(lose.get(sig, set()))) or '-':>22s}"
              f"{','.join(sorted(win.get(sig, set()))) or '-':>22s}")
    pure_lose = [s for s in allsig if s in lose and s not in win]
    print(f"\nsignatures that ALWAYS lose: {len(pure_lose)} / {len(allsig)}")
    print(f"signatures that ever lose:   {len(lose)} / {len(allsig)}")

if __name__ == "__main__":
    mp.freeze_support(); main()
