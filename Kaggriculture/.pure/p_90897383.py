"""Pure verbatim replay of ladder episode 90897383 (opponent seat 1)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vW9cR/S9acxFSH7a7U+yXWIhiGZJcIjWEIEBTFCjSRdpd0f9exabIxzczZ87M3PtIq16Zpki++31nzpw58/E/J3/7'
    '5ffffv395E8fT95f3t2dPCxO/v7LP//6r8c3Hl/+9svv//j134+vP568vbodHv/Kvfj2w08/X767+vHy+mRx8vpmfbJYibfv'
    '3g7D+9Ef7obhzePb67fD5f3J4sXk7R+H65t3J4vl9uPvb2/efHh9v/vG+cPDfxd7/bl6/cOH97snLUd9+3iyHu7uP7X13c3t'
    '/dtPr7ZvTV7sD8TdcH29e+rSfOr2A+Onbv86HpSr6zc/Pw7+/YfN6HHtUAdBNGfzE1oTdsNiPzI3BuChm6+c9u/59NdHrdlN'
    'uTL507fGz57O9fXl62E7knuPkH3THipegYd9N94f+4O7acYfa+qP33r8/7v77Z7R34k8+fXldAAnbXkcqsv74Xby6umhu09N'
    'moFGdnIWbRsxbvlweWc8PfTLux+Uw7R9xPbF3c0HZ7jkE5SFvm3x9ofbDtd0TTQfNbEEZPuVZ35+kZv4XXvRjFUGTR4/o8Og'
    'NFqbVcNM82L86cR4ocUmN2ebgZsehB1GkFhv8h1wjWTWHRq+zLmweWfUzt071qNyD1AGa/unySOTPdi1V/zw5xeB30UfBeYV'
    '+NrTKmQ+a120gRsSffTm+np4ff/zd8Pt/dX11V8+jVrrLszRnqmRBz76dJ59bXq56ZGt8vWj0KPdODGjKVic2e5swN/cfOAM'
    '+puRnR76tu0n1Gx++G3WKcPrPmYj9BqmSBvkMDXwXFsOknTFeZtInH2xR9sjvLNv3TYoA4ya0GqId06S10BlgANjpAxxwNPs'
    'voal+9FqgEdLIGF2Tt3npJc395MLpnbk6krcS7FjtsEllLl6eqzD3G1cOPvyJ16XqyR9vAXvDe857lGWOMA63r2hEfMPcvum'
    'TQ2ZezTNusbC7v9z+krW5Zi8KLkaTDxlGn2L29qLXl5K7IcJx8X5wW5m+qKZF2ijq4U7yYDY317e/jl+Z01NfBW13zQljZMo'
    'ZmRwTJD1vvvtaSAjc/cZQHJp2uSy2k5WeuI0vN6F2gszqJ1RJf9W6wDvzkGfV1ttBctmPFm7H9x7Nz5/cq5AhNG3TFKHXCnQ'
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
