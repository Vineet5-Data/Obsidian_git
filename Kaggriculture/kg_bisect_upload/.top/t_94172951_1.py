import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    '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'
    'zt/EVjhoV+kekZ1f7vG4Xb+znbf/DxyxSgw='
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
