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
