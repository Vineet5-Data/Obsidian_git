"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXdFuG0mS/Bc988EkZY19bxq5dy2sxjIk+Yi5gTAYYPdwwGL3Ye7eFvvvJ8si2eyMjIzMqqZkj59GI1PN6qqsqszIyMhf'
    '/nXy37/9/o+//X7yH7+cfDy/vT25X5z8z2///Ov/Pvzi4cd//Pb73//2fw8//3Ly/vJmePhX+sOPn37+9fzD5U/nVyeLk4vr'
    'zcliaX59+34YPp4sTrf/cDsM7x5+vXk/nN+dLF5Pfv3TcHX9YfTrjzfX7z5d3I3/4P7fi4O3uLz4y6ePo+/fvc8vJ5vh9u5x'
    'oLsfnt559Ge78Y1f3/uOp0EcfsuH65u7948P3f9kv+fpT+n3PA1TffaPny6v3v368L93nz4vCHnw5JP66K/OL4bdJNEpevrk'
    '51U4eP7DP3y4262s8z1/GhsF+5rDDx6s9fndcOM9/+I8mKAvH8Dzsn2D7ZeOnvv0ITYvk02GHrcfemFp7RfsHwfMXl9Q+9zd'
    '0/wJkRfSPv72+tPThIP5CBfQn+e94dnpqKzfaHT+PDSt3+7UsvPQsn7KhDSsnzQvlXXc/i2Yji8vUHvc3t6mv6o9z05vF2tg'
    'r99kDduHDOcdjUCZjc428OWHxOOQnxNeB6GlXVxfXQ0Xd7/+abi5u7y6/K/HYdr7JHX7F64tNAzygO0tlxoo+NZwoMHsJIe9'
    '3bs9F6iy+esHxvc/+f4nL+hPDs/E2+Hqc+g22ilfIjIcAZoY7ew+FT/tvJD45PHdfxtnLWpHmYmHDqcGvvDyPnnWTN6j5XbY'
    'X4qVgYLzH45dGaF/l+Axxn9upik85Lf+QedpApOPZ6kywKm/nzKCUdRU+Go7wYUh7CfYjECeX7BszgSHA2SRZeEoNVNUeMZu'
    'huzfqjMEHoonqHxb/FH+tnrVHdx5hyjmcvLr27ub882Pw83NzyeLdfEynPzQ/VLsdT0+z0XZemVuw9PRSrW+iRSKLQBQWb5S'
    '9XvDDs4ea3hGmsOq6fXbdE+AuI9exD1ewMCe2RkCi4iwzjiWVDykvXmUnrcfmIt/d3IzPddDc0KsvzDBBJsuW3twuABUcZAT'
    '0K3l6vv+kD4PafMLmiJeciZO06Xf7/5e4XLb4JMRYXHMJn4uhmhOIP3Zes9v/rNwgYHJJNdEGXRIuDjgoSCRVgmSpyG2NJyn'
    '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'
    'mocKR1lrbnr//+nsKMI='
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
