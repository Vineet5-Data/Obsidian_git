"""Extract the six fresh ladder opponents from the v27 loss replays.

Each becomes (a) a new PANEL opponent and (b) a new ROUTE candidate -- the same
treatment every earlier top player got.  Our seat is identified by v27's exact
sales fingerprint (STRAWBERRY 292 / WHEAT 273 / MILK 213 / FERTILIZER 210).

Replay off-by-one: the action taken against observation step N is stored in
steps[N+1].
"""
import base64, collections, glob, json, os, textwrap, zlib

OURS = {"STRAWBERRY": 292, "WHEAT": 273, "MILK": 213, "FERTILIZER": 210}
os.makedirs(".fresh", exist_ok=True)
tmpl = open("v30.py", encoding="utf-8").read().splitlines(keepends=True)
s = next(i for i, l in enumerate(tmpl) if l.startswith("_ACTIONS ="))
e = next(i for i in range(s, len(tmpl)) if tmpl[i].rstrip() == ")))")

made = []
for path in sorted(glob.glob("v27_losses/*.json")):
    ep = os.path.basename(path).split(".")[0]
    steps = json.load(open(path, encoding="utf-8"))["steps"]
    sold = [collections.Counter(), collections.Counter()]
    for i in range(len(steps) - 1):
        for seat in (0, 1):
            for o in ((steps[i + 1][seat].get("action") or {}).get("market") or []):
                if o and o[0] == "SELL" and len(o) >= 3:
                    sold[seat][o[1]] += int(o[2])
    us = 0 if all(sold[0].get(k) == v for k, v in OURS.items()) else 1
    opp = 1 - us
    tape = []
    for i in range(len(steps) - 1):
        act = steps[i + 1][opp].get("action") or {}
        tape.append({"farmer": act.get("farmer") or ["PASS"],
                     "hands": act.get("hands") or [],
                     "market": act.get("market") or []})
    blob = base64.b64encode(zlib.compress(
        json.dumps(tape, separators=(",", ":")).encode(), 9)).decode()
    body = "\n".join(f"    {l!r}" for l in textwrap.wrap(blob, 96))
    out = ("".join(tmpl[:s])
           + "_ACTIONS = json.loads(zlib.decompress(base64.b64decode(\n    (\n"
           + body + "\n    )\n)))\n" + "".join(tmpl[e + 1:]))
    dest = f".fresh/n_{ep}.py"
    open(dest, "w", encoding="utf-8").write(out)
    margin = steps[-1][us].get("reward", 0) - steps[-1][opp].get("reward", 0)
    made.append((ep, us, margin, sum(sold[opp].values())))
    print(f"{dest}  ourseat={us}  our margin {margin:+,.0f}  "
          f"opp total units sold {sum(sold[opp].values()):,}  "
          f"(ours {sum(sold[us].values()):,})")
print(f"\nextracted {len(made)} fresh opponents")
