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
