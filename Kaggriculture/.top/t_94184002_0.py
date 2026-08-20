import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    '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'
    '1PSs6MGVRjho13G/lSfxtnIIspbiZu3+D8HyZps='
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
