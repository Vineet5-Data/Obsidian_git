"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vG9cR/S965oNJyrLdN8VmGiGKZchyiTQQggBNUaBIH9K+Ff3vlS2Ru9w5c+bM3LuU7PiNlsnd+31nzpw589N/T/7+'
    'y++//fr7yZ9+Onl3/v79ye3i5B+//Otv/777w93H3375/Z+//ufu808n311cb+7+l3745sOPP5+/vfjh/PJkcfL6anuyWJo/'
    'v/9us3l3sjjd/cf7zebN3Z+3323Ob04Wzyd//mFzefV29Od311dvPry+Gf/g9n+Lg15cvP7+w7vR+/f9+elku3l/86mh+w8P'
    'fR79bN++cfe9dzw04vAtb6+ub7779NDhk33Pw0/pex6aqT77mw8Xl29+vvvnzYePE0IePPmm3vrL89eb/SDRIXr45sdZOHj+'
    '3X+8vdnPrPOeb8eLgr3m8IsHc31+s7n2nv/6PBig+y/gcdn1YPfS0XMfvsTGZbLJ0OOGphem1r5geBxY9vqE2ufun+YPiDyR'
    '9vHvrz48DDgYj3AC/XEeFp4djsr8jVrnj0PT/O1PLTsOLfOnDEjD/EnjUpnH3W/BcNx3oPa4Yb1N/1R7nh3eLquBdb9pNewe'
    'sjnvuAiU0ei8Bu4/JB6H7JzwOghX2uury8vN65ufv91c31xcXvz1UzPtfZK6/QvXFmoGecDulks1FLw1bGgwOslm7/Zuzwmq'
    'bP76gfH1J19/8oR+cngmvt9cfnTdRjvl3iPDHqDx0c5uU/7T3gqJTx7f/Ld+1qJ2lBl/6HBoYIeXt8mzZtKPltthuBQrDQXn'
    'P2y70kL/LsFtjH9uhik85Hf2QedhAoOPR6nSwKm9n1oEI6+p8Go7wIUmDANsWiCPL5g2Z4DDBjLPsnCUmiEqPGM/Qva36giB'
    'h+IBKt8Wf5TfVq+6gzvvEMVcTv78/ub6fPvN5vr6x5PFungZTj50vxR7XY+Pc1G2Xpk793Q0U609kVyxBQAqy1eqfm/Yxtlj'
    'DY9Is1s1vX6b7gng99GLuEcHDOyZHSEwiQjrjH1JxUIalkfpeUPDXPy7k5npmR6aEWLthQkm2HTZ2oPDBaCKjZyAbi1X39eH'
    '9HlIm13Q5PGSM3EaLv169/dyl9san/QIi202/nPRRXMc6Y+r9/z6L4ULDAwmuSbKoEPCxAEPBYG0ipM8dbGl5jwc8NpyfoxJ'
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
