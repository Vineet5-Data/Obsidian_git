import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrdXctuXFly/BeuuVAV396xpRpLGHZToKgpjBtEowGPYcAYL9reGf53a8R63LonMiIyzymS8kqFYune8z6ZkZGRv/7Pyb/9'
    '/sff//bHyT/9evLT1093H377fPvl8evD6uTp9OTff//Pf/2vb3/59vHvv//xH3/772+ffz35+On7X70PP33962+3v3z6+fbu'
    '5PTk/f365HTZfP3l42r1efKHL6vVh29frz+ubh9PTq9mX/+8urv/5eR0sfv554f7D1/fP+7/x+XT0/+eTjv2+dP7P3/9vH/T'
    'YtK3X0/Wqy+P39v6y/3D48fvn3ZfzT4cDsSX1d3d/q1n87duHzd5FWjI9LX7T/OpQA2YvS6cPdjDXUu+z8nioK+bX5F3fb67'
    'fb+KxhP1Z/sfwNtm7SZv3fyX6Xg27fj+3S/7xXDQ181MBT+TI7y6nb9/vzxuH1cP80U0/+5w9cClu5wvoi/3X+eLqF2cf/rH'
    'zjj4ZtY7NpXt4BwO8GyU9v17f7tZmtsfPe/MSddTc7kfrval21GY/kpOF9h/aHLATmhWMHnLZuzBmE2Go5mx9jf+jG3GnQ7d'
    'wXPnO28/hO00BetyYRxuYDOERys/Ww664I0sOnT05G1b6o+l/Y2eRzCEmxMGzJGaN38Qd+/Yffh29n5BH3IDtx/3ngdvfkkn'
    'fezz6YQP6cD2/07eNPS58sMrPHZ2q5wF1qQ4TBMXyJinzs/WzPZ98RbM7RHy08aMGNOC9/d3d6v3j7/9afXw+Onu078cngmD'
    'Bq/8ksQSKb/jSHOwvbUn7Qn30M4Rmf04uMovnhIW4Jte/4n5nffxvO7dSvuv0yYB5l1jPk6McLBwK34GMEbgnsC92iztlJnM'
    '+zDtreqjHEDg2CcMUuaqwE/qgWws0Cf5QOYRmPZjhz8aN7noQMWDatm+zgaivrmef+Lp9Lm+DvAkHwe95YTzAIz7/SNb41tv'
    '/hY4IU6Ibl/qcc/f1HCznse2hvV+DPef3tLzPjzcf44ep+eYOBK7B8++GeuWDLn9gSV1jmHsRZdpgOBk0+Bg11vfRccwneCO'
    'ljZC4TJU5kAnYGddD0PMBIQ2hldH8YZkEPt+H/eNCnhZ5tHUZABvieZf3gueJVEyUsjwcNtNP5rC1ABUS8GABO2iI1LAjdrL'
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
