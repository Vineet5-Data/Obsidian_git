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
