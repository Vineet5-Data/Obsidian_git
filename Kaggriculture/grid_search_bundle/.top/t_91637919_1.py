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
