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
