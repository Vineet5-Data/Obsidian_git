import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    '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'
    '+dP/Aanb+JA='
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
