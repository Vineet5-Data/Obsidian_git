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
    'Gh6RZrdqev023RPA76MXcY8O7J/07uIP2hPBrI2uIDzOsScp2Uf7MS49b2ili353MjLJvhZMEGstuABRH2tvAjgq1061kWXg'
    'ruX6/PaQRrOgyeElR+I0Wvrt6u/lLbc1PukQFttsDsWih+b40Z9X7/n1nwrXGRhMck+UMYeEhQMeCuJoFR956mFLzXk8m7Xl'
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
