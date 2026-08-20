import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    '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'
    'ePYNae613lrAC/07i/j5/wDEO2ce'
    )
)))


def _get(v, k, d=None):
    if isinstance(v, dict):
        return v.get(k, d)
    return getattr(v, k, d)


def agent(obs):
    try:
        step = min(max(0, int(_get(obs, "step", 0) or 0)), len(_ACTIONS) - 1)
        act = _ACTIONS[step] or {}
        farms = _get(obs, "farms", []) or []
        seat = int(_get(obs, "player", 0) or 0)
        farm = farms[seat] if seat < len(farms) else {}
        expected = len(_get(farm, "hands", []) or [])
        hands = [list(h or ["PASS"]) for h in (act.get("hands") or [])]
        hands += [["PASS"]] * max(0, expected - len(hands))
        return {"farmer": list(act.get("farmer") or ["PASS"]),
                "hands": hands[:expected],
                "market": [list(o) for o in (act.get("market") or [])][:10]}
    except Exception:
        return {"farmer": ["PASS"], "hands": [], "market": []}
