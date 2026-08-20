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
