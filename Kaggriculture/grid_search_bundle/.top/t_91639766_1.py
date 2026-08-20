"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    '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'
    'ovRxrzPVvPM26Ixir9v/B3SjI+w='
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
