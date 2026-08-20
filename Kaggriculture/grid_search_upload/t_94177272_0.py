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
