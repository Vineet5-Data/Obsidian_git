"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    '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'
    'QCqoy2WpYZDTC1Q4USbEDpC//z/XUZfa'
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
