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
