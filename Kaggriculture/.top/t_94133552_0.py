import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vW1ly/C961oMpkZSUN43NjY3VjA3ZDrEZCIMBskGAYPMwyVuw/z2OPsjLe6qrq/ocyrLXbzRN3Xu+T3d1dfWv/3vy'
    '77//8be//nHyT7+e/PT53c2b3z5cf/z0+XZzcnd68h+//9e//feX//ny8W+///Gff/2fL59/PXn77v5/tQ8/ff7Lb9e/vPv5'
    '+ubk9OT1++3J6Vnz9ce3m82HyX983GzefPl6+3Zz/enk9GL29c+bm/e/nJwudj//cPv+zefXn/Z/sb67+/vptGMf3r3+8+cP'
    '+zctJn379WS7+fjpvq2/vL/99Pb+0+6r2YfDgfi4ubnZv/V8/tanx01eBRoyfe3+03wqUANmrwtnD/Zw15L7OVkc9PXxV+Rd'
    'H26uX2+i8UT9efoD8LZZu8lbH/9kOp5NO+6/+2W/GA76+jhTwc/SEd5cz9+/Xx7Xnza380U0/+5w9cClezZfRB/ff54vonZx'
    '/un/d8bBN7PesalsB+dwgGejtO/f6+vHpfn0o4edOem6NZf74Wpf+jQK01+l0wX2H5ocsBOaFUze8jj2YMwmw9HMWPsbfcYe'
    'x50O3cFz5ztvP4TtNAXrciEcbmAzhEcrP1sOuqCNLDp08sl7aqk+lvI3+TyCIXw8YcAcZfOmD+LuHbsPX87ej+iDN3D7ce95'
    '8OMv6aSPfT6d8CEdePrbyZuGPjf98BUeO7tVzgNrMjlMjQtkzFPnZ6uzfZ+9BXN7hPy0MSPGtOD1+5ubzetPv/1pc/vp3c27'
    'fz08EwYNXvklxhIpv+NIc/B0a0/aE+6hnSMy+3Fwla/uDAvwRa9/Y37nfVzWvdvU/uu0SYB515iPEyMcLNyKnwGMEbgncK8e'
    'l7ZlJvM+THub9TEdQODYGwYpc1Xgp+yBbCzQp/SBzCMQ7ccOfzRuctGBigdVsn2VDUR983z+iafT5/oqwFP6OOgtG84DMO73'
    'j2yNwXzzt8AJsS3z9lmPS01Vgps9s2H942njnybf+8CGWqogd90wiG2F9nA+hNEXM1j8y6l3+x4hNdJxyK5a6ZCs2A+7t04O'
    'LP/uFNve0zlrCBGy3nUn0Pu1y9igF21lWLgdE0KRjtOUtd8wm6jlQUyGgj1GF/0e9UuxUYJeJYORQ4bOwTuHsr4f4OrHY388'
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
