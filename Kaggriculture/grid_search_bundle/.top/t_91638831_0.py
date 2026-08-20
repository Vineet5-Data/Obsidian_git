"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vXFlu/C967gerW9bYedPYvTvCaixDltPYDITBALtBgGDzMMlbkP8e2ZL647JYLJLntmTvvLXl7nvP9yGLxeIv/3vy'
    '77/9/o+//37yL7+cfLz49OnkbnHyH7/919/++/4P9x//8dvv//n3/7n//MvJT5c36/v/pR9+/PzXXy8+XP58cXWyOHl3vTlZ'
    'nJo/f/ppvf54sjh7+o9P6/X7+z9vflpf3J4sXk/+/PP66vrD3p8/3ly///zudv8Hd/+3OOjF5bu/fP649/5tf3452aw/3X5t'
    '6PbDY5/3frZt3373vXc8NuLwLR+ub25/+vrQ3Sf7nsef0vc8NlN99o+fL6/e/3r/z9vPXyaEPHjyTb31Vxfv1ttBokP0+M0v'
    's3Dw/Pv/+HC7nVnnPX/aXxTsNYdfPJjri9v1jff8dxfBAD18AY/LUw+eXrr33McvsXGZbDL0uF3TC1NrX7B7HFj2+oTa526f'
    '5g+IPJH28Z+uPz8OOBiPcAL9cd4tPDsclfnba50/Dq35255adhw686cMSGP+pHGpzOPTb8FwPHSg9rjdepv+qfY8O7xDVgPr'
    'fms1PD1kfTFwESijMXgNPHxIPA7ZOeF1EK60d9dXV+t3t7/+aX1ze3l1+W9fm2nvk9TtX7i2UDPIA55uuVRDwVvDhgajk2z2'
    '094dOUGVzV8/MP74yR8/eUE/OTwTP62vvrhuezvlwSPDHqDx0c7vUv7T1gqJTx7f/Ld+1qJ2lBl/6HBoYIdP75JnzaQfndth'
    'dylWGgrOf9h2pYX+XYLbGP/cDFN4yD/ZB4OHCQw+HqVKA6f2fmoR7HlNhVfbAS40YTfApgXy+IJpcwY4bCDzLAtHqRmiwjO2'
    'I2R/q44QeCgeoPJt8c/y2+pVd3DnHaKYp5M/f7q9udj8uL65+evJYlW8DCcfhl+Ko67H57kou1fmk3u6N1Pdnkiu2AIAleUr'
    'Vb83bOPssYZHpO1WTa/f1j0B/D56EY/ogIE9syMEJhFhnbEvqVhIu+VRet6uYS7+PcjM9EwPzQix9sIEE2xdtvbgcAGoYiMn'
    'oFvn6vvjIWMe0rMLWh4vOROn4dI/7v5R7nKv8UmPsNhm4z8XXTTHkf6yei9u/rVwgYHBJNdEGXRImDjgoSCQVnGSpy621JzH'
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
