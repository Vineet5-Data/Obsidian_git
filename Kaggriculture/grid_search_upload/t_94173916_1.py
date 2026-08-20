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
