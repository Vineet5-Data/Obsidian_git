import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vHNmR/C8890H9SdI3jtS2BHOGAiVtwzsgBgPYhgHDe5jd22L/+8r86K6qjIyMzPeKlAa8tVrNqvf9MiMjI3/+37O/'
    '//rbv/7229kffj774cuH63e/fLz69PnL7f7sbnH2j1//66///fV/vn7816+//fNv//P1889n7z/c/6/24Ycvf/nl6qcPP15d'
    'ny3O3t4czhYr8/Wn9/v9x8F/fNrv3339+vB+f/X5bHE++frH/fXNT2eL5fHnH29v3n15+/n0F7u7u/9bDDv28cPbP3/5eHrT'
    'ctC3n88O+0+f79v6083t5/f3n45fTT6MB+LT/vr69Nb19K1Pjxu8CjRk+NrTp+lUoAZMXufOHuzhsSX3c7Ic9fXxV+RdH6+v'
    '3u698UT9efoD8LZJu8lbH/9kOJ6mHfff/XRaDKO+Ps6U87NwhPdX0/eflsfV5/3tdBFNvxuvHrh0V9NF9Onmy3QR2cX5x3/v'
    'jNE3k96xqbSDMx7gySid+vf26nFpPv3oYWcOup6ay9Nw2Zc+jcLwV+F0gf2HJgfsBLOCyVsexx6M2WA4zIzZ3+gz9jjudOhG'
    'z53uvNMQ2mly1uVSONzAZnCPVn62jLqgjSw6dOLJe2qpPpbyN/E8giF8PGHAHEXzpg/i8R3HD1/P3k/oQ27gTuPe8uDHX9JJ'
    '7/t8OuFdOvD0t4M3dX1u+OEFHju5VdaONRkcpokLpM9Tp2drZvs+ewum9gj5qTEj+rTg7c319f7t51/+uL/9/OH6w3+Oz4RO'
    'g1d+SWKJlN8x0xw83dqD9rh76OiITH7sXOXbu4QF+E2v/8T8Tvu4qXu3of3XaJMA886YjwMjHCzcip8BjBG4J3CvHpd2ykzm'
    'fRj2NupjOIDAsU8YpMxVgZ+iB7KxQJ/CBzKPQLQfG/xRv8lFB8ofVMn2VTYQ9c3j+SeeTpvrqwBP4eOgt5xwHoBxf3qkNQbj'
    'zW+BE2Jbxu1LPS40Vd99+FO/hxXM6den9X+afNsDy2mjQtt1c8C3EOyRPAbPlxMw/OtZd3uD8BnpEGQXrHQ0VqyG41sHx1T+'
    'xhTb3tK51BAiPL3pJqC3apOJQa/XyrBw6yVxsFPjAjU7YSNRM4PYBwXji671E8QXAqEEqgoGI8YHM+ftFLf6/aBUr499fex3'
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
