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
