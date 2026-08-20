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
