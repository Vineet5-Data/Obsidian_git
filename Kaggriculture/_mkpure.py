"""Re-extract the six ladder opponents as PURE replays.

The first extraction wrapped them in v30's code, whose smoothing layer re-times
market orders -- so the "opponent" was not the opponent.  A faithful replay
emits the recorded action verbatim and only pads hands to the live unit count.
"""
import base64, collections, glob, json, os, textwrap, zlib

OURS = {"STRAWBERRY": 292, "WHEAT": 273, "MILK": 213, "FERTILIZER": 210}
TMPL = '''"""Pure verbatim replay of ladder episode {ep} (opponent seat {opp})."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
{body}
    )
)))


def _get(v, k, d=None):
    if isinstance(v, dict):
        return v.get(k, d)
    return getattr(v, k, d)


def agent(obs):
    try:
        step = min(max(0, int(_get(obs, "step", 0) or 0)), len(_ACTIONS) - 1)
        act = _ACTIONS[step] or {{}}
        farms = _get(obs, "farms", []) or []
        seat = int(_get(obs, "player", 0) or 0)
        farm = farms[seat] if seat < len(farms) else {{}}
        expected = len(_get(farm, "hands", []) or [])
        hands = [list(h or ["PASS"]) for h in (act.get("hands") or [])]
        hands += [["PASS"]] * max(0, expected - len(hands))
        return {{"farmer": list(act.get("farmer") or ["PASS"]),
                "hands": hands[:expected],
                "market": [list(o) for o in (act.get("market") or [])][:10]}}
    except Exception:
        return {{"farmer": ["PASS"], "hands": [], "market": []}}
'''

os.makedirs(".pure", exist_ok=True)
for path in sorted(glob.glob("v27_losses/*.json")):
    ep = os.path.basename(path).split(".")[0]
    rep = json.load(open(path, encoding="utf-8"))
    steps = rep["steps"]
    sold = [collections.Counter(), collections.Counter()]
    for i in range(len(steps) - 1):
        for seat in (0, 1):
            for o in ((steps[i+1][seat].get("action") or {}).get("market") or []):
                if o and o[0] == "SELL" and len(o) >= 3:
                    sold[seat][o[1]] += int(o[2])
    us = 0 if all(sold[0].get(k) == v for k, v in OURS.items()) else 1
    opp = 1 - us
    tape = [{"farmer": (steps[i+1][opp].get("action") or {}).get("farmer") or ["PASS"],
             "hands": (steps[i+1][opp].get("action") or {}).get("hands") or [],
             "market": (steps[i+1][opp].get("action") or {}).get("market") or []}
            for i in range(len(steps) - 1)]
    blob = base64.b64encode(zlib.compress(
        json.dumps(tape, separators=(",", ":")).encode(), 9)).decode()
    body = "\n".join(f"    {l!r}" for l in textwrap.wrap(blob, 96))
    open(f".pure/p_{ep}.py", "w", encoding="utf-8").write(
        TMPL.format(ep=ep, opp=opp, body=body))
    print(f".pure/p_{ep}.py  seed={rep['info']['seed']}  ourseat={us}  "
          f"real {steps[-1][us].get('reward',0):,.0f}/{steps[-1][opp].get('reward',0):,.0f}")
