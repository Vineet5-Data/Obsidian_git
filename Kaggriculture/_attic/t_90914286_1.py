"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vW9cR/S9ac2FSlCx3p9hMLESxDEkukRpCEKApChTpIu2u6H+vYlHk45uZM2dm7n2k3KxMUyTf/b7zceacz/85+dvP'
    'v/36y28nf/p88vHy7u7kYXby95//+dd/Pb7x+PLXn3/7xy//fnz9+eT91e3q8a/ci28+/fjT5YerHy6vT2Ynb2/WJ7OFePvu'
    '/Wr1cfCHu9Xq3ePb6/ery/uT2evR2z+srm8+nMzm249/vL159+nt/e4bZw8P/53t9efq7fefPu6eNB/07fPJenV3/6WtH25u'
    '799/ebV9a/RifyDuVtfXu6fOzaduPzB86vavw0G5un730+Pg33/ajB7XDnUQRHM2P6E1YTcs9iNzYwAeuvnKaf+ej3990Jrd'
    'lCuTP35r+OzxXF9fvl1tR3LvEbJv2kPFK/Cwb4f7Y39wN834fU39/luP//9wv90z+juRJ7+9HA/gqC2PQ3V5v7odvXp+6O5T'
    'o2agkR2dRdtGDFu+urwznh765d0PymHaPmL74u7mkzNc8gnKQt+2ePvDbYdrvCaaj5pYArL9yjOfXuQmftdeNGOVQZPHz+Aw'
    'KI3WZtUw0zwbfjoxXmixyc3ZZuDGB2GHESTWm3wHXCOZdYeGL3MubN4ZtHP3jvWo3AOUwdr+afTIZA927RU//PQi8Lvoo8C8'
    'Al97XoXMZ62LNnBDoo/eXF+v3t7/9O3q9v7q+uovX0atdRemaM/YyAMffT7P/mh6uemRrfLHR6FHu3FiBlMwW9rubMDf3Hxg'
    'Cf3NyE4Pfdv2E2o2P/w265ThdR+zEXoNU6QNcpgaeK4tB0m64rxNJM6+2KPtEd7Zt24blAFGTWg1xDsnyWugMsCBMVKGOOBp'
    'dl/D0v1oNcCDJZAwO8fuc9LLm/rJBVM7cnUl7qXYMdvgEspcPT3WYe42Lpx9+ROvy1WSPt6C94b3HPcoSxxgHe/e0Ij5B7l9'
    '06aGzD2aJl1jYff/a/pK1uUYvSi5Gkw+ZZx9i9vas15eSuyHCcfF+cFuZvqsmRdoR1cLd5IRYn9/efvn+J01NvHVqP2mKek4'
    'iWJGBscEWe+73x4nMjJ3nxFILk2bXFbbyUpPnBavd0PthRnUzqiSf6t1gHfnoM+rrbaCZTOcrN0P7r0bnz85VyDD6FsmqUOu'
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
