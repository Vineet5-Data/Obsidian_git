"""Extract the 12 fresh top-leaderboard episodes as pure-replay opponents.

These are current leaderboard winners, so BOTH seats are candidate routes and
candidate opponents unless one of them is us (v27's sales fingerprint).
"""
import base64, collections, glob, json, os, textwrap, zlib

OURS = {"STRAWBERRY": 292, "WHEAT": 273, "MILK": 213, "FERTILIZER": 210}
TMPL = open(".pure/p_90874645.py", encoding="utf-8").read()
HEAD = TMPL[:TMPL.index("_ACTIONS =")]
TAIL = TMPL[TMPL.index(")))") + 4:]

os.makedirs(".top", exist_ok=True)
rows = []
for path in sorted(glob.glob("Top_fresh-21/*.json")):
    ep = os.path.basename(path).split(".")[0]
    rep = json.load(open(path, encoding="utf-8"))
    steps, seed = rep["steps"], rep["info"]["seed"]
    rew = [steps[-1][i].get("reward") for i in (0, 1)]
    sold = [collections.Counter(), collections.Counter()]
    hires = [0, 0]
    for i in range(len(steps) - 1):
        for seat in (0, 1):
            for o in ((steps[i+1][seat].get("action") or {}).get("market") or []):
                if not o: continue
                if o[0] == "SELL" and len(o) >= 3: sold[seat][o[1]] += int(o[2])
                elif o[0] == "HIRE": hires[seat] += 1
    names = rep["info"].get("TeamNames", ["?", "?"])
    for seat in (0, 1):
        if all(sold[seat].get(k) == v for k, v in OURS.items()):
            continue                                  # that's our own agent
        tape = [{"farmer": (steps[i+1][seat].get("action") or {}).get("farmer") or ["PASS"],
                 "hands": (steps[i+1][seat].get("action") or {}).get("hands") or [],
                 "market": (steps[i+1][seat].get("action") or {}).get("market") or []}
                for i in range(len(steps) - 1)]
        blob = base64.b64encode(zlib.compress(
            json.dumps(tape, separators=(",", ":")).encode(), 9)).decode()
        body = "\n".join(f"    {l!r}" for l in textwrap.wrap(blob, 96))
        open(f".top/t_{ep}_{seat}.py", "w", encoding="utf-8").write(
            HEAD + "_ACTIONS = json.loads(zlib.decompress(base64.b64decode(\n    (\n"
            + body + "\n    )\n)))\n" + TAIL)
        rows.append((ep, seat, names[seat][:16], rew[seat], hires[seat],
                     sum(sold[seat].values()), dict(sold[seat].most_common(3))))
print(f"{'episode':11s}{'st':>3s}{'player':18s}{'reward':>10s}{'hires':>7s}{'units':>8s}  top sales")
for r in rows:
    print(f"{r[0]:11s}{r[1]:>3d}{r[2]:18s}{r[3]:>10,.0f}{r[4]:>7d}{r[5]:>8,d}  {r[6]}")
print(f"\nextracted {len(rows)} candidate routes -> .top/")
