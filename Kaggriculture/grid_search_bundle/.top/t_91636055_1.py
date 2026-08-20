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
