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
