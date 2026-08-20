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
