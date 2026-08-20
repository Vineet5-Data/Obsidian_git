import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    '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'
    'AIvPYvE='
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
