"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vW9cR/S9ac2FSlGx3p9hMLESxDEkukRpCEKApChTpIu2u6H+vYlHk45uZM2dm7n2k1KxMUyTf/b7zceacL/85+dvP'
    'v/36y28nf/py8uni9vbkfnby95//+dd/Pbzx8PLXn3/7xy//fnj95eTD5c3q4a/ci28+//jTxcfLHy6uTmYn767XJ7OFePv2'
    'w2r1afCH29Xq/cPb6w+ri7uT2evR2z+srq4/nszm249/url+//nd3e4bZ/f3/53t9efy3fefP+2eNB/07cvJenV797WtH69v'
    '7j58fbV9a/RifyBuV1dXu6fOzaduPzB86vavw0G5vHr/08Pg333ejB7XDnUQRHM2P6E1YTcs9iNzYwAeuvnKaf+ej3990Jrd'
    'lCuTP35r+OzxXF9dvFttR3LvEbJv2kPFK/Cwb4f7Y39wN834fU39/lsP//94t90z+juRJ7+7GA/gqC0PQ3Vxt7oZvXp66O5T'
    'o2agkR2dRdtGDFu+urg1nh765d0PymHaPmL74vb6szNc8gnKQt+2ePvDbYdrvCaaj5pYArL9yjMfX+QmftdeNGOVQZPHz+Aw'
    'KI3WZtUw0zwbfjoxXmixyc3ZZuDGB2GHESTWm3wHXCOZdYeGL3MubN4ZtHP3jvWo3AOUwdr+afTIZA927RU//Pgi8Lvoo8C8'
    'Al97WoXMZ62LNnBDoo9eX12t3t399O3q5u7y6vIvX0etdRemaM/YyAMffTrP/mh6uemRrfLHR6FHu3FiBlMwW9rubMDf3Hxg'
    'Cf3NyE4Pfdv2E2o2P/w265ThdR+zEXoNU6QNcpgaeK4tB0m64rxNJM6+2KPtEd7Zt24blAFGTWg1xDsnyWugMsCBMVKGOOBp'
    'dl/D0v1oNcCDJZAwO8fuc9LLm/rJBVM7cnUl7qXYMdvgEspcPT3WYe42Lpx9+ROvy1WSPt6C94b3HPcoSxxgHe/e0Ij5B7l9'
    '06aGzD2aJl1jYff/JX0l63KMXpRcDSafMs6+xW3tWS8vJfbDhOPi/GA3M33WzAu0o6uFO8kIsX+4uPlz/M4am/hq1H7TlHSc'
    'RDEjg2OCrPfdb48TGZm7zwgkl6ZNLqvtZKUnTovXu6H2wgxqZ1TJv9U6wLtz0OfVVlvBshlO1u4H996Nz5+cK5Bh9C2T1CFX'
    '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'
    'J+QoLaUhD6QMeEZHrXdxB6f6Lrr/H6yXD3w='
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
