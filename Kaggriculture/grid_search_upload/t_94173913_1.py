import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vW1ly/C961sOQoj6cN63NzRirGRuyvcRmIAwGyAYBgs3DJG9B/nscSyQv76murupzruQx/EZQ1L3n+3RXV1f/8j9n'
    '//bb7//4++9n//TL2Z8+vb178+v72w8fP91vzx7Oz/79t//81//6/JfPH//x2+//8ff//vz5l7Mf3375q/bhT5/+9uvtz29/'
    'ur07Oz97/W53dr5uvv7w43b7fvKHD9vtm89f737c3n48O7+eff3T9u7dz2fnq8PP39+/e/Pp9cfjf1w9PPzv+bRj79++/sun'
    '98c3rSZ9++Vst/3w8Utbf353//HHL58OX80+nA7Eh+3d3fGtF/O37h83eRVoyPS1x0/zqUANmL0unD3Yw0NLvszJ6qSvT78i'
    '73p/d/t6G40n6s/+H8DbZu0mb336l+l4Nu348t3Px8Vw0tenmQp+lo7w9nb+/uPyuP24vZ8vovl3p6sHLt31fBF9ePdpvoja'
    'xfnn/98ZJ9/Mesemsh2c0wGejdKxf69vn5bm/kePO3PSdWsuj8PVvnQ/CtNfpdMF9h+aHLATmhVM3vI09mDMJsPRzFj7G33G'
    'nsadDt3Jc+c77ziE7TQF63IlHG5gM4RHKz9bTrqgjSw6dPLJ27dUH0v5m3wewRA+nTBgjrJ50wfx8I7Dh89n7wf0wRu447j3'
    'PPjpl3TSxz6fTviQDuz/d/Kmoc9NP7zAY2e3ykVgTSaHqXGBjHnq/Gx1tu+zt2Buj5CfNmbEmBa8fnd3t3398dc/b+8/vr17'
    '+y+nZ8KgwSu/xFgi5XcsNAf7W3vSnnAPHRyR2Y+Dq/zywbAAv+r1b8zvvI+buneb2n+dNgkw7xrzcWKEg4Vb8TOAMQL3BO7V'
    '09K2zGTeh2lvsz6mAwgce8MgZa4K/JQ9kI0F+pQ+kHkEov3Y4Y/GTS46UPGgSravsoGob57PP/F0+lxfBXhKHwe9ZcN5AMb9'
    '8ZGtMZhv/hY4IbZl3j7rcampSnCzZzasvz9t/NPkex/YUBsMYK+6jAIEJIumBrvY+q44huYEt3NqHRSuwcwQ6ITqpIthiIGA'
    'cMbw0ijejQxcPx7XfaMCXuY8mhoL4C3R/Kc3gmZDlMwTMjzcassfTQFqAKdZACDBueiIDDmg4SodevLPsbRvBzn7/tjvjzUx'
    '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'
    'p2/6PnhBEFQmab1+eImt/fB/ylV0Tg=='
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
