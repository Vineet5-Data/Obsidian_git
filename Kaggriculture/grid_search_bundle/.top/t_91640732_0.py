"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vXEly/C8890HdTWkk3zhS70pYzlAgKTfWA2IwwK5hwFgfxr4Z/u+WSPbXy8jIyMx6pKSd03Co5ut6VVlVmZGRkb/8'
    '79m///b7P/7++9m//HL28eLm5uxucfYfv/3X3/778y8+//iP337/z7//z+effzl7/+F68/lf6Q8/fvrrrxc/f/jp4vJscfb2'
    'anu2WJpf37zfbD6eLc53/3Cz2bz7/Ovt+83F7dni5eTXP20ur34++vXH66t3n97eHv/B3f8tTt7iw9u/fPp49P379/nlbLu5'
    'ub0f6P6Hx3c++rP9+I5f3/uOx0GcfsvPV9e37+8fevjJfs/jn9LveRym+uwfP324fPfr5/+9/fRlQciDJ5/UR3958XaznyQ6'
    'RY+f/LIKJ8///A8/3+5X1vmePx0bBfua0w+erPXF7ebae/7bi2CCHj6A52X3BrsvPXru44fYvEw2GXrcYeiFpbVfcHgcMHt9'
    'Qe1z90/zJ0ReSPv4m6tPjxMO5iNcQH+eD4Znp6Oyfkej8+ehtX77U8vOQ2f9lAlprJ80L5V13P0tmI6HF6g97mBv01/Vnmen'
    'd4g1sNdvWcPuIZuLgUagzMZgG3j4IfE45OeE10FoaW+vLi83b29//dPm+vbD5Yd/ux+mvU9St3/h2kLDIA/Y3XKpgYJvDQca'
    'zE5y2Lu9O3KBKpu/fmD88Sd//MlX9CenZ+LN5vJL6Ha0Ux4iMhwBmhjt1V0qftp7IfHJ47v/Ns5a1I4yEw+dTg184eVd8qyZ'
    'vEfndjhcipWBgvMfjl0ZoX+X4DHGf26mKTzkd/7B4GkCk49nqTLAqb+fMoKjqKnw1XaCC0M4TLAZgTy/YNmcCQ4HyCLLwlFq'
    'pqjwjP0M2b9VZwg8FE9Q+bb4Z/nb6lV3cuedopjLya9vbq8vtj9urq//erZYFy/DyQ/DL8VR1+PzXJTdK3MXnh6tVPdNpFBs'
    'AYDK8pWq3xt2cPZYwzPSDqum12/rngBxH72IR7yAgT2zMwQWEWGdcSypeEgH8yg97zAwF/8e5GZ6rofmhFh/YYIJti5be3C4'
    'AFRxkBPQrXP1/fGQMQ/p+QWtiJecidN06R93/6hwuTf4ZERYHLOJn4shmhNIf7Hei+t/LVxgYDLJNVEGHRIuDngoSKRVguRp'
    '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'
    '4/YKdJWEztjenFHsdff/LDIhhA=='
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
