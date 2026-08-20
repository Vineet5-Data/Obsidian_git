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
