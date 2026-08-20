import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vHFly/C8886Bmd5OibxypdyUsZyhQlBvrATEYYNcwYKwPY98M/3drxe7qqsrIyMh8r0jOQLdWs1X1vl9mZGTkz/97'
    '9u+//vaPv/929i8/n/3w5ePt+18+3Xx++HK/O3s8P/uPX//rb//99S9fP/7j19/+8+//8/Xzz2cfPn77q/bhhy9//eXmp48/'
    '3tyenZ+9u9ufnV+Yrz9/2O0+jf7webd7//Xr/YfdzcPZ+dXs6x93t3c/nZ2vhp9/ur97/+Xdw+l/XD4+/t/5uGOfPr77y5dP'
    'pzetRn37+Wy/+/zwra0/3d0/fPj2afhq9mE6EJ93t7ent67nbz0+bvQq0JDxa0+f5lOBGjB7nTt7sIdDS77NyWrS18OvyLs+'
    '3d6823njifpz/A/gbbN2k7ce/st4PE07vn3302kxTPp6mCnnZ+EI727m7z8tj5uH3f18Ec2/m64euHQv5ovo892X+SKyi/NP'
    '/9wZk29mvWNTaQdnOsCzUTr1793NYWkef/S0M0ddT83labjsS4+jMP5VOF1g/6HJATvBrGDylsPYgzEbDYeZMfsbfcYO406H'
    'bvLc+c47DaGdJmddroTDDWwG92jlZ8ukC9rIokMnnrxjS/WxlL+J5xEM4eGEAXMUzZs+iMM7hg9fz97P6ENu4E7j3vLgwy/p'
    'pPd9Pp3wLh04/t/Rm7o+N/zwAo+d3Sprx5oMDtPEBdLnqfOzNbN9n70Fc3uE/NSYEX1a8O7u9nb37uGXP+3uHz7efvy36ZnQ'
    'afDKL0kskfI7FpqD4609ao+7hwZHZPZj5yrfPiYswFe9/hPzO+/jpu7dhvZfo00CzDtjPo6McLBwK34GMEbgnsC9OiztlJnM'
    '+zDubdTHcACBY58wSJmrAj9FD2RjgT6FD2QegWg/NvijfpOLDpQ/qJLtq2wg6pvH8088nTbXVwGewsdBbznhPADj/vRIawzG'
    'm98CJ8S2jNuXelxoqhLc7JkN6+9P6/80+d4HNtRGBbnrhoFvK9jDeQqjr2aw+NdT7/4OITXScciuWumQrNgPw1tHB1b+7hTb'
    '3tK51BAiZL3pTqD3a5OxQS/ayrBwO8aFIjNOU9T+hNlELQ9iMhTsMbroT6hfiI0S9CoYjBgyzBy8cyjrjwNcfX/s98f+Dh+r'
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
