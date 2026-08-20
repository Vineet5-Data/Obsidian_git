"""Build a route agent from Seb's episode 90503598 (p0, $148,637)."""
import base64, json, zlib, textwrap

data = json.load(open(".tmp_replay_90503598.json", encoding="utf-8"))
steps = data["steps"]
# Kaggle stores the initial observation as steps[0]; the action applied for
# observation step N is recorded in replay steps[N + 1].
actions = []
for index in range(len(steps)):
    src_step = steps[index + 1] if index + 1 < len(steps) else None
    a = src_step[0].get("action") if src_step else None
    if not isinstance(a, dict):
        a = {"farmer": ["PASS"], "hands": [], "market": []}
    actions.append({
        "farmer": list(a.get("farmer") or ["PASS"]),
        "hands": [list(h or ["PASS"]) for h in (a.get("hands") or [])],
        "market": [list(m) for m in (a.get("market") or [])],
    })
print("steps captured:", len(actions), "max hands:", max(len(x["hands"]) for x in actions))

blob = base64.b64encode(zlib.compress(json.dumps(actions, separators=(",", ":")).encode(), 9)).decode()
lines = textwrap.wrap(blob, 100)
literal = "\n".join("    '%s'" % ln for ln in lines)

src = open("v13.py", encoding="utf-8").read()
tail = src[src.index("def _get("):]

header = '''"""Route agent distilled from episode 90503598 (Seb, $148,637 in contested play).

That route buys all four quadrants and 19 animals and skips the wheat
round-trip the previous clone spent $31,968 on.  Runtime hand alignment keeps
it legal when stochastic state changes alter accepted hires; the idle-unit
layer and terminal liquidation are carried over unchanged.
"""

import base64
import copy
import json
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
%s
    )
)))


''' % literal

open("v16.py", "w", encoding="utf-8").write(header + tail)
print("v16.py written")
