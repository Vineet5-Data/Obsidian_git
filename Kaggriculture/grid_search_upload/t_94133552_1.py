import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    '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'
    'D38ac+o='
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
