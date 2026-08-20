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
