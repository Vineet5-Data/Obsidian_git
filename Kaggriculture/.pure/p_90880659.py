"""Pure verbatim replay of ladder episode 90880659 (opponent seat 1)."""
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
