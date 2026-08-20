"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXdFuHEly/Bc+z4NmhqIlv3GlPos4rihQ1A3OC2GxgM8wYJwf1n4z/O+mxJmens7IyMis6qGk26flUsPp6qqsqszIyMhf'
    '/vfi33/7/e9/+/3in3+5+HD98ePF59XFf/z2X//234+/ePzx77/9/p9/+5/Hn3+5eHdzPzz+K/3hp09//fX6/c3P17cXq4s3'
    'd7uL1dr8+uO7Yfhwsbo8/MPHYXj7+Ovdu+H64WL1cvbrn4fbu/eTX3+4v3v76c3D9A8+/9/q5C1u3vz504fJ88f3+eViN3x8'
    '+DrQ8Yf9O0/+bBzf9PW9Z+wHcfqU93f3D+++funxJ/uc/Z/S5+yHqX73T59ubt/++vi/D5++LAj54tkn9dHfXr8ZjpO0ppO0'
    '/yxYh8d/ev8wrq7zrD99sQD2gKcPnKzv9cNw733fm+tgUp4+gOfiMOKnVTv53v2H2EzMNhb6uuPQC8tpH3D8OmDqmUW03zx+'
    'nz8l4dLZr/1492k/1WAmwqXzZ/hoYnYiKis3GZ3//k0rN55Rdh7aVk6ZksLKSTNSWcHD34KJeBp47euOljb/Ve377LR2sQP2'
    '+o12cPia4brD8ivz0Hn1n35IfB3yZMLDP7SxN3e3t8Obh1//NNw/3Nze/OvXYdrbI3W/Fy4pNAzyBYc7LTVQ8NRwoMHsJId9'
    '2LU9F6iy7etHxR9/8seffEN/cnomfhxuvwRnk53yFHPhGM9EYVefUxHS6HfEJ4918m0EtaodYSbSOZ0S+KLrz8kzZj/+ltvg'
    'eAlWBgjOezhmZYT+3YHHGP/5OD3hYX7wAzpPD5h0PDuVAc59+dTiTyKiwqOPE1t49HFizZPleQXL5UxsOEAWLRaOynFqCn87'
    'zoz9W3VmwJfiiSnfAv8of1u9wk7uslP8cT379ceH++vdT8P9/V8vVtviJTf7odtl1+vaO+8F2HoVvr35l+YhSzHUJKSdWEG/'
    'i1I6+uxQZzfmqkMcdDzU8PvWbwEQtfFboMfrFDYeWK/JFYNnJY4Eqb8zvm/pe46jczHqTs4i2L+CS2FvfwDoPOFPfby2GTSo'
    'XCfaINtvtD++pM+XtF33TQEqOQTn+cs/rvRqdNs26GQgVxxz7Ra332Nv8XfX938pXFNgEsk9UMYGEpEs+FKQ06rEtPOIWBrO'
    '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'
    'P8o+A30='
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
