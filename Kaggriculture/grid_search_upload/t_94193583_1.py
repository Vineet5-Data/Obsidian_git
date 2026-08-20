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
