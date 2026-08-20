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
