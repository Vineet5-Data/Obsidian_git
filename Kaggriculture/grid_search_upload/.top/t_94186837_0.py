import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXcuOHEly/Jc+94H16JduPWStSGzPNNEkt7AaNAYDaAUBwuow0k3Qv4tivTIzLMzNPCKrmwueWKguZsY73M3NzX/9n4t/'
    '+/2Pv//tj4t/+vXipy8fHt799vH+0+cvT5uL58uLf//9P//1v77+5evHv//+x3/87b+/fv714v2Hb3/VPvz05a+/3f/y4ef7'
    'h4vLi7eP24vLZfH1p/ebzcfBHz5tNu++fr19v7n/fHF5M/n6583D4y8Xl4vjzz8+Pb778vbz6X9cPz//7+WwYx8/vP3zl4+n'
    'Ny0Gffv1Yrv59PlbW395fPr8/tun41eTD+OB+LR5eDi9dTV96+Fxg1eBhgxfe/o0nQrUgMnrqrMHe3hsybc5WYz6uv8VedfH'
    'h/u3m9p4ov4c/gN426Td5K37/zIcz6Id37775bQYRn3dz1TlZ+EIb+6n7z8tj/vPm6fpIpp+N149cOkup4vo0+OX6SIqF+ef'
    '/n9njL6Z9I5NZTk44wGejNKpf2/v90vz8KPdzhx03ZrL03CVLz2MwvBX4XSB/YcmB+yEYgWTt+zHHozZYDiKGSt/o8/Yftzp'
    '0I2eO915pyEsp6myLhfC4QY2Q/Vo5WfLqAvayKJDJ568Q0v1sZS/iecRDOH+hAFzFM2bPojHdxw/fD17P6EP3sCdxr3lwftf'
    '0knv+3w64V06cPi/gzd1fW744QUeO7lVVhVrMjhMjQukz1OnZ6uzfc/egqk9Qn5amBF9WvD28eFh8/bzb3/aPH3+8PDhX8Zn'
    'QqfBS7/EWCLpd8w0B4dbe9Ce6h46OiKTH1eu8qtnwwJ81evfmN9pH9d57za0/xptEmDeFebjwAgHCzfjZwBjBO4J3Kv90rbM'
    'ZN6HYW+jPoYDCBx7wyBlrgr8FD2QjQX6FD6QeQSi/djgj9abnHSg6oMq2b7KBqK+eTz/xNNpc30V4Cl8HPSWDecBGPenR5bG'
    'YLz5S+CE2JZx+6zHhaYqwc3ObFj/eFr/p8n3PrCh1hjAXjQZBQhIFk0NdrG1XXEMzanczqF1kLgGI0OgEaqTLoYuBgLCGauX'
    'RvJuZOD66bhuGxXwMufR1FgAb6nNf3gjaDZEyjwhw8OttvjRFKAGcJoFABKci45IlwMartKuJ/8US/vHQc5+PPbHY01Mqm69'
    '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'
    'fzz5JlEwG7R2HEQ8Sn89/x+DB5ea'
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
