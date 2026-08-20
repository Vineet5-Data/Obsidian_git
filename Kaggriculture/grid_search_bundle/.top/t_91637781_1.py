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
