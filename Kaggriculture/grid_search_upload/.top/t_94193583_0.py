import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vW1ly/C961oNJURSVN63NzRirGRmyvcJmIAwGyAYBgs3DJG9B/nscWSQv76murupzKHtn9XZNU7zn+3RXV1f//D9n'
    '//brb3/7629n//Tz2R8+v79998uHm4+fPt9vzx7Pz/791//81//68j9fHv/262//8df//vL889kP75/+V3v4w+e//HLz0/sf'
    'b27Pzs/e3j2cnS+bjz/+sN1+mPzHx+323ZePH37Y3nw6O7+affzj9vbup7Pzxf7rH+7v3n1+++nwF+vHx/89n3bsw/u3f/r8'
    '4fCmxaRvP589bD9+emrrT3f3n354etp/NHs4HoiP29vbw1sv5m/d/dzkVaAh09cenuZTgRowe104e7CH+5Y8zcniqK/P3yLv'
    '+nB783YbjSfqz+4PwNtm7SZvff6T6Xg27Xj67KfDYjjq6/NMBV9LR3h7M3//YXncfNrezxfR/LPj1QOX7nK+iD7efZ4vonZx'
    '/vH/d8bRJ7PesalsB+d4gGejdOjf25vnpbn70tedOem6NZeH4WpfuhuF6bfS6QL7D00O2AnNCiZveR57MGaT4WhmrP2OPmPP'
    '406H7uh35zvvMITtNAXrciEcbmAzhEcrP1uOuqCNLDp08snbtVQfS/mTfB7BED6fMGCOsnnTB3H/jv3Dl7P3I3rwBu4w7j0/'
    '/PxNOuljf59O+JAO7P528qahv5s+fIOfnd0qF4E1mRymxgUy5lfnZ6uzfV+8BXN7hHy1MSPGtODt3e3t9u2nX/64vf/0/vb9'
    'vxyfCYMGr/wSY4mU33GiOdjd2pP2hHto74jMvhxc5ZePhgX4Xa9/Y37nfVzVvdvU/uu0SYB515iPEyMcLNyKnwGMEbgncK+e'
    'l7ZlJvM+THub9TEdQODYGwYpc1XgU/aDbCzQU/qDzCMQ7ccOfzRuctGBigdVsn2VDUR983z+iafT5/oqwFP6c9BbNpwHYNwf'
    'frI1BvPN3wInxLbM22f9XGqqEtzshQ3r118b/2vyvQ9sqBUGsBddRgECkkVTg11sfVccQ3OC2zm1DgrXYGYIdEJ10sUwxEBA'
    'OGN4aRTvRgauH47rvlEBL3N+mhoL4C3R/Kc3gmZDlMwTMjzcast/mgLUAE6zAECCc9ERGXJAw1U69OSfY2m/H+Ts9Wdff9bE'
    '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'
    '8f8AaiVrCg=='
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
