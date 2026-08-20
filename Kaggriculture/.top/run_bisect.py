"""18-hunk bisect: which v97 -> v106 change costs the win rate?

Each agents/hNN.py is v97_cap70 with exactly ONE hunk of v106 applied, so the
win-rate column reads directly as that hunk's cost.  base_v97 and full_v106 run
in the same batch as anchors -- never compare against a number from another run.

    python run_bisect.py [workers] [out.json]

20 agents x 80 opponents x 2 seats = 3200 games, each on that opponent's own
recorded seed.  Opponents come from the .top/ dir of any attached dataset.
Agents exposing reset_telemetry()/telemetry_snapshot() are captured inside the
same worker process and written to <out-stem>_telemetry.json automatically.
"""
import glob, json, multiprocessing as mp, os, statistics as st, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


def find_opponents():
    """.top/ lives in the grid-search dataset, not here. Mount path varies."""
    # depth varies: /kaggle/input/<slug>/ vs /kaggle/input/datasets/<user>/<slug>/
    for pattern in ("/kaggle/input/*/.top/t_*.py",
                    "/kaggle/input/*/*/.top/t_*.py",
                    "/kaggle/input/*/*/*/.top/t_*.py",
                    str(HERE / ".top" / "t_*.py"),
                    str(HERE.parent / "*" / ".top" / "t_*.py"),
                    ".top/t_*.py"):
        hits = sorted(glob.glob(pattern))
        if hits:
            return hits
    raise SystemExit("no .top/t_*.py found -- attach the grid-search dataset")


def load_module(path):
    """Load a fresh module so game-local telemetry cannot leak across jobs."""
    import importlib.util
    name = "m_" + Path(path).stem.replace(".", "_")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def one(job):
    """Run one duel and return its margin plus same-process agent telemetry."""
    agent_path, opp_path, seed, seat = job
    from kaggle_environments import make
    agent_module = load_module(agent_path)
    opponent_module = load_module(opp_path)
    if hasattr(agent_module, "reset_telemetry"):
        agent_module.reset_telemetry()
    pair = ([agent_module.agent, opponent_module.agent] if seat == 0
            else [opponent_module.agent, agent_module.agent])
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run(pair)
    last = env.steps[-1]
    margin = float(last[seat].reward - last[1 - seat].reward)
    telemetry = (agent_module.telemetry_snapshot()
                 if hasattr(agent_module, "telemetry_snapshot") else None)
    return margin, telemetry


def main():
    workers = int(sys.argv[1]) if len(sys.argv) > 1 else max(1, (os.cpu_count() or 4) - 2)
    out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("/kaggle/working/bisect_hunks.json")
    # arg 3: how many fresh seeds per opponent. 0 = recorded mode, i.e. each
    # opponent replays its own tape on its home map -- the exam v97 was tuned
    # against. Anything > 0 measures whether a result survives new maps.
    n_random = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    # arg 4: skip this many seeds first. Rounds 4-6 all used seeds 1..8, and a
    # parameter picked by maximising over that fixed set is fitted to it. An
    # offset gives a set the tuning has never seen.
    offset = int(sys.argv[4]) if len(sys.argv) > 4 else 0

    seeds = json.loads((HERE / "seeds.json").read_text())
    opps = find_opponents()
    agents = sorted(glob.glob(str(HERE / "a_*.py")))   # flat: Kaggle mangles subdirs
    if n_random:
        # same generator top_tournament.py --mode random uses, so the two agree
        pool_seeds = [(i * 2654435761) % 2147483647
                      for i in range(offset + 1, offset + n_random + 1)]
        work = [(a, o, s, seat)
                for a in agents for o in opps for s in pool_seeds for seat in (0, 1)]
    else:
        work = [(a, o, seeds[Path(o).stem.removeprefix("t_").rsplit("_", 1)[0]], seat)
                for a in agents for o in opps for seat in (0, 1)]
    print(f"mode={'random x%d offset %d' % (n_random, offset) if n_random else 'recorded'}", flush=True)

    print(f"agents={len(agents)} opponents={len(opps)} games={len(work)} workers={workers}", flush=True)
    t0 = time.time()
    per = {}
    telemetry_rows = []
    with mp.Pool(workers) as pool:
        # chunksize 1: with ~96 workers an uneven tail costs more than dispatch
        for n, (job, result) in enumerate(
                zip(work, pool.imap(one, work, chunksize=1)), 1):
            margin, telemetry = result
            agent_name = Path(job[0]).stem.removeprefix("a_")
            per.setdefault(agent_name, []).append(margin)
            if telemetry is not None:
                telemetry_rows.append({
                    "agent": agent_name,
                    "opponent": Path(job[1]).stem,
                    "seed": job[2],
                    "seat": job[3],
                    "margin": margin,
                    "win": margin > 0,
                    "telemetry": telemetry,
                })
            if n % 200 == 0 or n == len(work):
                el = time.time() - t0
                print(f"  {n}/{len(work)}  {el:.0f}s  eta {el / n * (len(work) - n):.0f}s", flush=True)

    out = {name: {"wins": sum(v > 0 for v in m), "games": len(m),
                  "win_rate": sum(v > 0 for v in m) / len(m),
                  "mean": st.mean(m), "median": st.median(m), "min": min(m)}
           for name, m in sorted(per.items())}
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    if telemetry_rows:
        telemetry_path = out_path.with_name(out_path.stem + "_telemetry.json")
        telemetry_path.write_text(json.dumps(telemetry_rows, indent=2),
                                  encoding="utf-8")
        print(f"wrote {telemetry_path} ({len(telemetry_rows)} games)")

    base = out.get("base_v97", {}).get("win_rate")
    print(f"\n{'agent':<12} {'W-L':>10} {'rate':>7} {'vs v97':>8} {'mean':>9} {'median':>9} {'min':>9}")
    for n, d in sorted(out.items(), key=lambda kv: -kv[1]["win_rate"]):
        delta = f"{100 * (d['win_rate'] - base):+.1f}" if base is not None else "-"
        print(f"{n:<12} {d['wins']:>4}-{d['games'] - d['wins']:<5} {100 * d['win_rate']:>6.1f}% "
              f"{delta:>8} {d['mean']:>9.0f} {d['median']:>9.0f} {d['min']:>9.0f}", flush=True)
    print(f"\nwrote {out_path}")


if __name__ == "__main__":
    mp.freeze_support()
    main()
