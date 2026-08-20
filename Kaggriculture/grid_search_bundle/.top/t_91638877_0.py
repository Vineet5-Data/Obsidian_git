"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    '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'
    'rbr9P4GPKHY='
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
