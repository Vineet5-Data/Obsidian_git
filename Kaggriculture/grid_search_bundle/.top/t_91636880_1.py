"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    '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'
    '+cFalDLuoEBXSeiM7c0ZxV73/w9gbCEh'
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
