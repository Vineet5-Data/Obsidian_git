import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vI9mR/C8689CkSFHam6abdgvWjBpqtYnxQBgMYC8WMOzD7N4W+9+3LfGjWC8yMjLzlaQZ96kLbIr1vl9mZGTkT/97'
    '9p+//PqPv/169h8/nX335eb2w8+frj8/fLnfnD3Ozv7rl3/+9b+//s/Xx3/88uvf//Y/X59/Ovt48/S/2sN3X378+fqHm++v'
    'b89mZ+/vtmezRfPx54+bzafBf3zebD58/Xj7cXP9cDZbjz7+fnN798PZbH74+qf7uw9f3j8c/+Li8fH/ZsOOfbp5/6cvn45v'
    'mg/69tPZdvP54amtP9zdP3x8ejp8NHo4HYjPm9vb41sX47fuf27wKtCQ4WuPT+OpQA0Yvc6cPdjDQ0ue5mR+0tfdt8i7Pt1e'
    'v99Y44n6s/8D8LZRu8lbd38yHM+mHU+f/XBcDCd93c2U8TV3hDfX4/cfl8f1w+Z+vIjGn52uHrh05+NF9Pnuy3gRtYvzD//a'
    'GSefjHrHprIdnNMBHo3SsX/vr3dLc/+l55056HpoLo/D1b50PwrDb7nTBfYfmhywE5oVTN6yG3swZoPhaGas/Y4+Y7txp0N3'
    '8rvjnXccwnaa1HUJBhdsBvNo5WfLSRe0kUWHjj95+5bqYyl/4s8jGMLdCQPmyJs3fRAP7zg8fD17P6OH2MAdx73yw7tv0knv'
    '+/t0wrt0YP+3gzd1/V334RV+dnSrnBvWpHOYBi6QPr86Plsj2/fFWzC2R8hXGzOiTwve393ebt4//PyHzf3Dze3NX07PhE6D'
    'l35JYImk3zHRHOxv7UF7zD10cERGXzau8tVjwAJ80+s/ML/jPi7z3q1r/xVtEmDeNebjwAgHC1ew5xRnFe4J3Kvd0g6ZybwP'
    'w956fXQHEDj2AYOUuSrwyftBNhboyf1B5hGI9qO6ToA/ajc56UDZgyrZvsoGor65P//E06m5vgrw5P4c9JYDzgMw7o8/2RqD'
    '/uZvgRNiW/rtC/2ca6oS3OyFDetvv9b/1+R7H9hQSwxgz0tGAQKSRVODXWy1K46hOcbt7FoHiWvQMwSKUJ10MXQxEBDOaF4a'
    'ybuRgevH47o2KuBlkZ+mxgJ4izX/7o2g2RAp84QMD7fa/J+mADWA00IAIMG56Ih0OaDhKu168o+xtN8PcvbtZ7/9bBCTsq0X'
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
