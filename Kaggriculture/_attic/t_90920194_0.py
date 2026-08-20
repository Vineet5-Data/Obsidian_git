"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    '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'
    'VRrySMpAZ3TSejfL4FTfRQ//A8IgD3w='
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
