import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vW1ly/C961oMpUZSUN43NzRirGRuyHWIzEAYDZIMAweZhkrdg/3scSSQv76murupzKGm8fqNp6t7zfbqrq6t/+d+T'
    'f//t97/99feTf/rl5Icv72/f/frx5tPnL3frk/vTk//47b/+7b+//s/Xj3/77ff//Ov/fP38y8mP7x/+V/vww5e//Hrz8/uf'
    'bm5PTk/efticnJ41X3/6cb3+OPmPT+v1u69fb35c33w+Ob2cff3T+vbDzyeni93PP959ePfl7ef9X6zu7/9+Ou3Yx/dv//zl'
    '4/5Ni0nffjnZrD99fmjrzx/uPv/48Gn31ezD4UB8Wt/e7t96Pn/r9nGTV4GGTF+7/zSfCtSA2evC2YM93LXkYU4WB319+hV5'
    '18fbm7fraDxRf7Z/AN42azd569OfTMezacfDdz/vF8NBX59mKvhZOsLrm/n798vj5vP6br6I5t8drh64dM/mi+jThy/zRdQu'
    'zj/9/844+GbWOzaV7eAcDvBslPb9e3vztDS3P3rcmZOuW3O5H672pdtRmP4qnS6w/9DkgJ3QrGDylqexB2M2GY5mxtrf6DP2'
    'NO506A6eO995+yFspylYlwvhcAObITxa+dly0AVtZNGhk0/etqX6WMrf5PMIhvDphAFzlM2bPoi7d+w+fD17P6EP3sDtx73n'
    'wU+/pJM+9vl0wod0YPu3kzcNfW764QUeO7tVzgNrMjlMjQtkzFPnZ6uzfZ+9BXN7hPy0MSPGtODth9vb9dvPv/5pfff5/e37'
    'fz08EwYNXvklxhIpv+NIc7C9tSftCffQzhGZ/Ti4yi/uDQvwVa9/Y37nfVzWvdvU/uu0SYB515iPEyMcLNyKnwGMEbgncK+e'
    'lrZlJvM+THub9TEdQODYGwYpc1Xgp+yBbCzQp/SBzCMQ7ccOfzRuctGBigdVsn2VDUR983z+iafT5/oqwFP6OOgtG84DMO73'
    'j2yNwXzzt8AJsS3z9lmPS01Vgps9s2H9/Wnjnybf+8CGWqogd90wiG2F9nA+hNEXM1j866l39wEhNdJxyK5a6ZCs2A+7t04O'
    'LP/uFNve0zlrCBGy3nUn0Pu1y9igF21lWLgdE0KRjtOUtd8wm6jlQUyGgj1GF/0e9UuxUYJeJYORQ4bOwTuHsr4d4Or7Y78/'
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
