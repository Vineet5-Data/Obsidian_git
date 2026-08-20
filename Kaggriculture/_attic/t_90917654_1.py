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
