import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    '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'
    'hWvQAnnzSib68VQ9/h9QenyF'
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
