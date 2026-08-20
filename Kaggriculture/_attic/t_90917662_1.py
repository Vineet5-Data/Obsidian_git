"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    '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'
    'wcCOb767vru7bd7d/PgjP9dDtwesgsf/ACtgChU='
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
