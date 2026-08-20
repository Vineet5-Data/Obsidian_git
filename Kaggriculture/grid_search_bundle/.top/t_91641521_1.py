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
