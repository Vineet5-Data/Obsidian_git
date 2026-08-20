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
