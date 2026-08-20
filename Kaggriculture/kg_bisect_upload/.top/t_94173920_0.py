import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vW1ly/C961oNJUV9589jcjLGakSHbITYDYTDAbhAg2DxM8hbkv8exKPLynurqqj6HlGbhJxMUfe/5Pt3V1dW//M/Z'
    'v/32+9//9vvZP/1y9sOXD3fvf/349tPnLw/rs8fzs3//7T//+l9f//L1499/+/0//vbfXz//cvbjh29/1T788OUvv779+cNP'
    'b+/Ozs/e3W/OzpfN159+XK8/Tv7wab1+//XrzY/rt5/Pzq9nX/+0vrv/+ex8sfv5x4f791/efd7/j6vHx/89n3bs44d3f/7y'
    'cf+mxaRvv5xt1p8+f2vrz/cPn3/89mn31ezD4UB8Wt/d7d96MX/r8+MmrwINmb52/2k+FagBs9eFswd7uGvJtzlZHPR1+yvy'
    'ro93b9+to/FE/Xn+D+Bts3aTt27/y3Q8m3Z8++7n/WI46Ot2poKfpSO8fjt//355vP28fpgvovl3h6sHLt3lfBF9uv8yX0Tt'
    '4vzT/++Mg29mvWNT2Q7O4QDPRmnfv3dvt0vz+UdPO3PSdWsu98PVvvR5FKa/SqcL7D80OWAnNCuYvGU79mDMJsPRzFj7G33G'
    'tuNOh+7gufOdtx/CdpqCdbkQDjewGcKjlZ8tB13QRhYdOvnkPbdUH0v5m3wewRBuTxgwR9m86YO4e8fuw9ez9xP64A3cftx7'
    'Hrz9JZ30sc+nEz6kA8//d/Kmoc9NP7zAY2e3ykVgTSaHqXGBjHnq/Gx1tu/JWzC3R8hPGzNiTAve3d/drd99/vVP64fPH+4+'
    '/OvhmTBo8MovMZZI+R1HmoPnW3vSnnAP7RyR2Y+Dq/zy0bAAX/X6N+Z33sdV3btN7b9OmwSYd435ODHCwcKt+BnAGIF7Avdq'
    'u7QtM5n3YdrbrI/pAALH3jBImasCP2UPZGOBPqUPZB6BaD92+KNxk4sOVDyoku2rbCDqm+fzTzydPtdXAZ7Sx0Fv2XAegHG/'
    'f2RrDOabvwVOiG2Zt896XGqqEtzsxIb196eNf5p87wMbaoUB7EWXUYCAZNHUYBdb3xXH0Jzgdk6tg8I1mBkCnVCddDEMMRAQ'
    'zhheGsW7kYHr++O6b1TAy5xHU2MBvCWa//RG0GyIknlChodbbfmjKUAN4DQLACQ4Fx2RIQc0XKVDT/45lvaPg5x9f+z3x5qY'
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
