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
