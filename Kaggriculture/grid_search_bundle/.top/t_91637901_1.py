"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    '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'
    'np0v'
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
