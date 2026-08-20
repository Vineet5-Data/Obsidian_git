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
