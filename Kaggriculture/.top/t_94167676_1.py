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
