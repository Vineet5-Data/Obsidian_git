import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXctuXFly/BeuuVAV396xpRq3MOymQElTGDeIRgMew4AxXrS9M/zvlsV63LonMjIiz6kSe6CVCsXSved9MiMjI3/5n7N/'
    '++33v//t97N/+uXsh8/vH979+uH+46fPT6uz5/Ozf//tP//1v7785cvHv//2+3/87b+/fP7l7Mf3X/+qffjh819/vf/5/U/3'
    'D2fnZ28f12fny+brjz+uVh8mf/i4Wr378vX6x9X9p7Pzm9nXP60eHn8+O1/sfv7h6fHd57ef9v/j+vn5f8+nHfvw/u2fP3/Y'
    'v2kx6dsvZ+vVx09f2/rz49OnH79+2n01+3A4EB9XDw/7t17M37p93ORVoCHT1+4/zacCNWD2unD2YA93Lfk6J4uDvm5+Rd71'
    '4eH+7SoaT9Sf7X8Ab5u1m7x181+m49m04+t3P+8Xw0FfNzMV/Cwd4dX9/P375XH/afU0X0Tz7w5XD1y6y/ki+vj4eb6I2sX5'
    'p//fGQffzHrHprIdnMMBno3Svn9v7zdLc/ujl5056bo1l/vhal+6HYXpr9LpAvsPTQ7YCc0KJm/ZjD0Ys8lwNDPW/kafsc24'
    '06E7eO585+2HsJ2mYF0uhMMNbIbwaOVny0EXtJFFh04+eduW6mMpf5PPIxjCzQkD5iibN30Qd+/Yffhy9n5EH7yB2497z4M3'
    'v6STPvb5dMKHdGD7fydvGvrc9MM3eOzsVrkIrMnkMDUukDFPnZ+tzvY9eQvm9gj5aWNGjGnB28eHh9XbT7/+afX06f3D+385'
    'PBMGDV75JcYSKb/jSHOwvbUn7Qn30M4Rmf04uMqvng0L8FWvf2N+5328rHu3qf3XaZMA864xHydGOFi4FT8DGCNwT+BebZa2'
    'ZSbzPkx7m/UxHUDg2BsGKXNV4KfsgWws0Kf0gcwjEO3HDn80bnLRgYoHVbJ9lQ1EffN8/omn0+f6KsBT+jjoLRvOAzDu949s'
    'jcF887fACbEt8/ZZj0tNVYKbndiw/v608U+T731gQ11iAHvRZRQgIFk0NdjF1nfFMTQnuJ1T66BwDWaGQCdUJ10MQwwEhDOG'
    'l0bxbmTg+v647hsV8DLn0dRYAG+J5j+9ETQbomSekOHhVlv+aApQAzjNAgAJzkVHZMgBDVfp0JN/jqX94yBn3x/7/bEmJhVb'
    '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'
    '49k3pLnXemsPg4g7RbDn/wPxGp2T'
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
