import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    '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'
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
