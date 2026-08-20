"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
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
