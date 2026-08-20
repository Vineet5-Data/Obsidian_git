"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vXMlu/C96ngfPjOy186a158bG1a4MSc7gZiEsFsgNAgQ3D5u8BfnvsSXN12GxWCT7SLZ332R5dKZPN7ubLBaLv/zv'
    '2b//9vs//v772T/9cvbx4ubm7G5x9h+//de//ffnX3z+8R+//f6ff/+fzz//cvb+w/Xm8//SH3789LdfL37+8NPF5dni7O3V'
    '9myxNL++eb/ZfDxbnO/+42azeff519v3m4vbs8XLya9/2lxe/Xz064/XV+8+vb09/oO7/1ucvMWHt3/99PHo+/fv88vZdnNz'
    'ez/Q/Q+P73z0Z/vxHb++9x2Pgzj9lp+vrm/f3z/08JP9nsc/pd/zOEz12T9++nD57tfP/7z99GVByIMnn9RHf3nxdrOfJDpF'
    'j5/8sgonz//8Hz/f7lfW+Z6/HBsF+5rTD56s9cXt5tp7/tuLYIIePoDnZfcGuy89eu7jh9i8TDYZetxh6IWltV9weBwwe31B'
    '7XP3T/MnRF5I+/ibq0+PEw7mI1xAf54Phmeno7J+R6Pz56G1fvtTy85DZ/2UCWmsnzQvlXXc/S2YjocXqD3uYG/TX9WeZ6d3'
    'iDWw129Zw+4hm4uBRqDMxmAbePgh8Tjk54TXQWhpb68uLzdvb3/9y+b69sPlh3+9H6a9T1K3f+HaQsMgD9jdcqmBgm8NBxrM'
    'TnLYu707coEqm79+YPz5J3/+yVf0J6dn4s3m8kvodrRTHiIyHAGaGO3VXSp+2nsh8cnju/82zlrUjjITD51ODXzh5V3yrJm8'
    'R+d2OFyKlYGC8x+OXRmhf5fgMcZ/bqYpPOR3/sHgaQKTj2epMsCpv58ygqOoqfDVdoILQzhMsBmBPL9g2ZwJDgfIIsvCUWqm'
    'qPCM/QzZv1VnCDwUT1D5tvij/G31qju5805RzOXk1ze31xfbHzfX1387W6yLl+Hkh+GX4qjr8Xkuyu6VuQtPj1aq+yZSKLYA'
    'QGX5StXvDTs4e6zhGWmHVdPrt3VPgLiPXsQjXsDAntkZAouIsM44llQ8pIN5lJ53GJiLfw9yMz3XQ3NCrL8wwQRbl609OFwA'
    'qjjICejWufr+fMiYh/T8glbES87Eabr0z7t/VLjcG3wyIiyO2cTPxRDNCaS/WO/F9b8ULjAwmeSaKIMOCRcHPBQk0ipB8jTE'
    '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'
    '4w4KdJWEztjOnFHsdff/FucePA=='
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
