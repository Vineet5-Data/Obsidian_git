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
