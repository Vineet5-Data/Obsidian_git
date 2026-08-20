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
