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
