import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    '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'
    'GBSxf/7KjUm3dL4bECP6V4uf/g8Z16Sh'
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
