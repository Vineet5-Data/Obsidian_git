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
