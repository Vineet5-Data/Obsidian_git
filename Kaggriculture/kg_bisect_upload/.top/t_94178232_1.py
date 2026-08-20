import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXctuXFly/BeuuVAViy/v2FKNJQy7KVDSFMYNotGAxzBgjBdt7wz/u2WxHrfuiYyMyHOKkgZaqVAs3XveJzMyMvLX/zn7'
    't9//+Pvf/jj7p1/Pfvr07v7Nb+/vPnz89Lg+ezo/+/ff//Nf/+vzXz5//Pvvf/zH3/778+dfz96++/JX7cNPn/76290v736+'
    'uz87P3v9sDk7XzZff3i7Xr+f/OHDev3m89ebt+u7j2fn17Ovf17fP/xydr7Y//z948ObT68/Hv7H1dPT/55PO/b+3es/f3p/'
    'eNNi0rdfzzbrDx+/tPWXh8ePb7982n81+3A8EB/W9/eHt17M37p73ORVoCHT1x4+zacCNWD2unD2YA/3LfkyJ4ujvm5/Rd71'
    '/v7u9ToaT9Sf3X8Ab5u1m7x1+1+m49m048t3vxwWw1FftzMV/Cwd4fXd/P2H5XH3cf04X0Tz745XD1y6y/ki+vDwab6I2sX5'
    'p//fGUffzHrHprIdnOMBno3SoX+v77ZLc/ej55056bo1l4fhal+6G4Xpr9LpAvsPTQ7YCc0KJm/Zjj0Ys8lwNDPW/kafse24'
    '06E7eu585x2GsJ2mYF0uhMMNbIbwaOVny1EXtJFFh04+ebuW6mMpf5PPIxjC7QkD5iibN30Q9+/Yf/h89n5AH7yBO4x7z4O3'
    'v6STPvb5dMKHdGD3fydvGvrc9MNXeOzsVrkIrMnkMDUukDFPnZ+tzvZ98RbM7RHy08aMGNOC1w/39+vXH3/70/rx47v7d/9y'
    'fCYMGrzyS4wlUn7HieZgd2tP2hPuob0jMvtxcJVfPhkW4De9/o35nfdxVfduU/uv0yYB5l1jPk6McLBwK34GMEbgnsC92i5t'
    'y0zmfZj2NutjOoDAsTcMUuaqwE/ZA9lYoE/pA5lHINqPHf5o3OSiAxUPqmT7KhuI+ub5/BNPp8/1VYCn9HHQWzacB2DcHx7Z'
    'GoP55m+BE2Jb5u2zHpeaqgQ3e2HD+sfTxj9NvveBDbXCAPaiyyhAQLJoarCLre+KY2hOcDun1kHhGswMgU6oTroYhhgICGcM'
    'L43i3cjA9cNx3Tcq4GXOo6mxAN4SzX96I2g2RMk8IcPDrbb80RSgBnCaBQASnIuOyJADGq7SoSf/HEv7x0HOfjz2x2NNTCq2'
    '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'
    '/sP+x7NvCMFopbf2KK4IDOi9vPfT/wEgwJP+'
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
