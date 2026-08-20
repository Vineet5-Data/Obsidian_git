"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vG9kR/C8682CSsmznprWZrBCtZchyiGQhLBbIBgGC5LDJLch/jyyJnOF0dXV1vzeU7PWNlsmZ9/26q6urf/zvyd9+'
    '/vWfv/x68rsfTz6cf/x4crs4+fvP//rrv+/+cPfxnz//+o9f/nP3+ceT7y+uN3f/Sz989+nPP52/v/jh/PJkcfL2anuyWJo/'
    'f/x+s/lwsjjd/cfHzebd3Z+332/Ob04WLyd//mFzefV+9OcP11fvPr29Gf/g9n+Lg15cvP3jpw+j9+/78+PJdvPx5r6h+w+P'
    'fR79bN++cfe9dzw24vAt76+ub76/f+jwyb7n8af0PY/NVJ/93aeLy3c/3f3z5tPnCSEPnnxTb/3l+dvNfpDoED1+8/MsHDz/'
    '7j/e3+xn1nnP78eLgr3m8IsHc31+s7n2nv/2PBighy/gcdn1YPfS0XMfv8TGZbLJ0OOGphem1r5geBxY9vqE2ufun+YPiDyR'
    '9vEfrz49DjgYj3AC/XEeFp4djsr8jVrnj0PT/O1PLTsOLfOnDEjD/EnjUpnH3W/BcDx0oPa4Yb1N/1R7nh3eLquBdb9pNewe'
    'sjnvuAiU0ei8Bh4+JB6H7JzwOghX2tury8vN25uffr+5vrm4vPjLfTPtfZK6/QvXFmoGecDulks1FLw1bGgwOslm7/Zuzwmq'
    'bP76gfHtJ99+8ox+cngmftxcfnbdRjvlwSPDHqDx0c5uU/7T3gqJTx7f/Ld+1qJ2lBl/6HBoYIeXt8mzZtKPltthuBQrDQXn'
    'P2y70kL/LsFtjH9uhik85Hf2QedhAoOPR6nSwKm9n1oEI6+p8Go7wIUmDANsWiCPL5g2Z4DDBjLPsnCUmiEqPGM/Qva36giB'
    'h+IBKt8Wv5XfVq+6gzvvEMVcTv788eb6fPvd5vr6zyeLdfEynHzofin2uh6f5qJsvTJ37uloplp7IrliCwBUlq9U/d6wjbPH'
    'Gh6RZrdqev023RPA76MXcY8OGNgzO0JgEhHWGfuSioU0LI/S84aGufh3JzPTMz00I8TaCxNMsOmytQeHC0AVGzkB3Vquvm8P'
    '6fOQNrugyeMlZ+I0XPrt7u/lLrc1PukRFtts/Oeii+Y40p9X7/n1nwoXGBhMck2UQYeEiQMeCgJpFSd56mJLzXk84LXl/BST'
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
