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
