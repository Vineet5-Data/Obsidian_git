import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vW1ly/C961sOQkigqb1qbmzFWMzJkO8RmIAwGyAYBgs3DJG/B/vc4+iAv76murupzaMkDvdE0de/5Pt3V1dW//O/J'
    'v//2+9//9vvJP/1y8qcvH27e//rx+tPnL3ebk/vTk//47b/+7b+//s/Xj3//7ff//Nv/fP38y8mPHx7+V/vwpy9//fX65w8/'
    'Xd+cnJ68u92enC6brz/9uNl8nPzHp83m/devtz9urj+fnF7Ovv5pc3P788npYvfzj3e377+8+7z/i9X9/T9Opx37+OHdX758'
    '3L9pMenbLyfbzafPD239+fbu848Pn3ZfzT4cDsSnzc3N/q1n87c+P27yKtCQ6Wv3n+ZTgRowe104e7CHu5Y8zMnioK9PvyLv'
    '+nhz/W4TjSfqz/MfgLfN2k3e+vQn0/Fs2vHw3c/7xXDQ16eZCn6WjvDmev7+/fK4/ry5my+i+XeHqwcu3eV8EX26/TJfRO3i'
    '/PP/74yDb2a9Y1PZDs7hAM9Gad+/d9dPS/P5R487c9J1ay73w9W+9HkUpr9KpwvsPzQ5YCc0K5i85WnswZhNhqOZsfY3+ow9'
    'jTsduoPnznfefgjbaQrW5UI43MBmCI9WfrYcdEEbWXTo5JP33FJ9LOVv8nkEQ/h0woA5yuZNH8TdO3Yfvp69n9AHb+D2497z'
    '4Kdf0kkf+3w64UM68Py3kzcNfW764QUeO7tVzgJrMjlMjQtkzFPnZ6uzfb95C+b2CPlpY0aMacG725ubzbvPv/55c/f5w82H'
    'fz08EwYNXvklxhIpv+NIc/B8a0/aE+6hnSMy+3FwlV/cGxbgq17/xvzO+3he925T+6/TJgHmXWM+ToxwsHArfgYwRuCewL16'
    'WtqWmcz7MO1t1sd0AIFjbxikzFWBn7IHsrFAn9IHMo9AtB87/NG4yUUHKh5UyfZVNhD1zfP5J55On+urAE/p46C3bDgPwLjf'
    'P7I1BvPN3wInxLbM22c9LjVVCW72jQ3rt6eNf5p87wMb6lwFueuGQWwrtIfzIYy+mMHiX0+9u1uE1EjHIbtqpUOyYj/s3jo5'
    'sPy7U2x7T+esIUTIetedQO/XLmODXrSVYeF2TAhFOk5T1n7DbKKWBzEZCvYYXfR71C/FRgl6lQxGDhk6B+8cyvrjAFdvj317'
    '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'
    'bkT5'
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
