"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    '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'
    'ZgN9'
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
