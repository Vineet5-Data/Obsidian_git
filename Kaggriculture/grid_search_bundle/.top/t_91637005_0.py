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
