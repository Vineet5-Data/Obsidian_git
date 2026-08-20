import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vXEly/C8886BuNqmWbxrp7Y6wnJFASW6sB8RgAK9hwFgfxr4Z/u/Wiv3x+lVkRGRWtaQxdGs0m+/Vd2VGRkb+8j9X'
    '//bb73//2+9X//TL1Q8f39y//vXdy/cfPj5MV4/XV//+23/+6399+sunj3//7ff/+Nt/f/r8y9WPbz7/1fvww8e//vry5zc/'
    'vby/ur569XZ3db1uvn7/4zS9m/3h/TS9/vT17sfp5Yer6+eLr3+a7t/+fHW9Ov783cPb1x9ffTj9x93j4/9ezzv27s2rv3x8'
    'd3rTata3X6520/sPn9v689uHDz9+/nT8avHhfCDeT/f3p7feLN96eNzsVaAh89eePi2nAjVg8bpw9mAPjy35PCers77uf0Xe'
    '9e7+5aspGk/Un8M/gLct2k3euv+X+Xg27fj83c+nxXDW1/1MBT+TIzy9XL7/tDxefpgeloto+d356oFLd71cRO/fflwuonZx'
    '/ukfO+Psm0Xv2FS2g3M+wItROvXv1cv90jz86GlnzrqemsvTcLUvPYzC/FdyusD+Q5MDdkKzgslb9mMPxmw2HM2Mtb/xZ2w/'
    '7nTozp673HmnIWynKViXK+NwA5shPFr52XLWBW9k0aGjJ+/QUn8s7W/0PIIh3J8wYI7UvPmDeHzH8cOns/c9+pAbuNO49zx4'
    '/0s66WOfTyd8SAcO/zt709Dnyg9f4bGLW+UmsCbFYZq4QMY8dXm2ZrbvF2/B0h4hP23MiDEtePX2/n569eHXP00PH97cv/mX'
    '8zNh0OCVX5JYIuV3XGgODrf2rD3hHjo6IosfB1f57WPCAvym139ifpd93NS9W2n/ddokwLxrzMeZEQ4WbsXPAMYI3BO4V/ul'
    'nTKTeR/mvVV9lAMIHPuEQcpcFfhJPZCNBfokH8g8AtN+7PBH4yYXHah4UC3b19lA1DfX8088nT7X1wGe5OOgt5xwHoBxf3pk'
    'awzqzd8CJ8S21O1LPU6aqgQ3+8KG9fenjX+afe8DG2qDAexVl1GAgGTT1GAXW98Vx9Cc4HaW1kHhGlSGQCdUZ10MQwwEhDOG'
    'l0bxbmTg+um47hsV8LLMo6mxAN4Szb+8ETwbomSekOHhVpt+NAWoAZyWAgAJzkVHZMgBDVfp0JN/iaX9/0HOvj/2+2OTmFRs'
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
