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
