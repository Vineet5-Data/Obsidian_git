"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
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
