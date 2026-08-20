import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vG1mS/C8682B+U3tT25y1MXLLkOUlZhtCo4GdwQCL2UPP3Bbz39crksWqepGRkfleSbLHN5qmqt73y4yMjPzlf6/+'
    '8tvvf/vz71f/9svVT18+3L779dPN54cv9/urx9nVX3/7n//6+9f/+frxb7/9/t9//sfXz79cvf/w9L/ah5++/OnXm58/fLy5'
    'vZpdvb07XM0Wxdef3+/3n3r/8Xm/f/f168P7/c3D1Ww7+vrj/vbu56vZvPv5p/u7d1/ePlz+YvP4+M9Zv2OfPrz945dPlzfN'
    'e3375eqw//zw1Naf7+4f3j996r4afRgOxOf97e3lrcvxW8+P670KNKT/2sun8VSgBoxeZ84e7GHXkqc5mQ/6evoVeden25u3'
    'e2s8UX/OfwDeNmo3eevpT/rjWbTj6bufL4th0NfTTBk/c0d4fzN+/2V53Dzs78eLaPzdcPXApbsYL6LPd1/Gi6hcnH/4/50x'
    '+GbUOzaV5eAMB3g0Spf+vb05Lc3zj447s9f10Fxehqt86XkU+r9ypwvsPzQ5YCcUK5i85TT2YMx6w1HMWPkbfcZO406HbvDc'
    '8c67DGE5Tca6nAuHG9gM5tHKz5ZBF7SRRYeOP3nnlupjKX/jzyMYwtMJA+bImzd9ELt3dB++nr2f0YfYwF3GvebBp1/SSW/7'
    'fDrhTTpw/tvem5o+1/3wAo8d3SpLw5p0DtPABdLmqeOzNbJ9n70FY3uE/LQwI9q04O3d7e3+7cOvf9jfP3y4/fCfwzOh0eCl'
    'XxJYIul3TDQH51u71x5zD3WOyOjHxlW+fgxYgK96/Qfmd9zHVd67de2/SpsEmHeF+dgzwsHCzfgZwBiBewL36rS0Q2Yy70O/'
    't14f3QEEjn3AIGWuCvzkPZCNBfrkPpB5BKL9WOGP2k1OOlD2oEq2r7KBqG/uzz/xdOpcXwV4ch8HveWA8wCM+8sjS2PQ3/wl'
    'cEJsS799oce5pirBzZ7ZsP7xtPZPk+99YEOtVJA7bxjYtkJ5OA9h9PkIFv966t3fIaRGOg7ZVSsdkhn7oXtr78CK351i22s6'
    'FxpChKxX3Qn0fq0yNuhFmxkWbseYUGTEafLaHzCbqOVBTIaEPUYX/QX1c7FRgl45g+FDhpGDdwxlfT/A1Y/H/njsN/hYHcBq'
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
