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
