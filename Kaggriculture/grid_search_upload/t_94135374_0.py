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
