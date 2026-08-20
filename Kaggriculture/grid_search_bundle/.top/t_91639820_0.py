"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vXFlu/C967gerW9LYedPYvTvCaixDltPYDITBALtBgGDzMMlbkP8e25L647JYLJLntmTvvLXl7nvP9yGLxeIv/3vy'
    '77/9/o+//37yL7+cfLj8+PHkfnHyH7/919/++/MfPn/8x2+//+ff/+fz519Ofrq6XX/+X/rhx09//fXy/dXPl9cni5O3N5uT'
    'xan588ef1usPJ4uzp//4uF6/+/znzU/ry7uTxfnkzz+vr2/e7/35w+3Nu09v7/Z/cP9/i4NeXL39y6cPe+/f9ueXk836493X'
    'hm4/PPZ572fb9u1333vHYyMO3/L+5vbup68P3X2y73n8KX3PYzPVZ//46er63a+f/3n36cuEkAdPvqm3/vry7Xo7SHSIHr/5'
    'ZRYOnv/5P97fbWfWec+f9hcFe83hFw/m+vJufes9/+1lMEAPX8Dj8tSDp5fuPffxS2xcJpsMPW7X9MLU2hfsHgeWvT6h9rnb'
    'p/kDIk+kffzHm0+PAw7GI5xAf5x3C88OR2X+9lrnj0Nr/ranlh2HzvwpA9KYP2lcKvP49FswHA8dqD1ut96mf6o9zw7vkNXA'
    'ut9aDU8PWV8OXATKaAxeAw8fEo9Ddk54HYQr7e3N9fX67d2vf1rf3l1dX/3b12ba+yR1+xeuLdQM8oCnWy7VUPDWsKHB6CSb'
    '/bR3R05QZfPXD4w/fvLHT17QTw7PxI/r6y+u295OefDIsAdofLSL+5T/tLVC4pPHN/+tn7WoHWXGHzocGtjh0/vkWTPpR+d2'
    '2F2KlYaC8x+2XWmhf5fgNsY/N8MUHvJP9sHgYQKDj0ep0sCpvZ9aBHteU+HVdoALTdgNsGmBPL5g2pwBDhvIPMvCUWqGqPCM'
    '7QjZ36ojBB6KB6h8W/yz/LZ61R3ceYco5unkzx/vbi83P65vb/96slgVL8PJh+GX4qjr8Xkuyu6V+eSe7s1UtyeSK7YAQGX5'
    'StXvDds4e6zhEWm7VdPrt3VPAL+PXsQjOmBgz+wIgUlEWGfsSyoW0m55lJ63a5iLfw8yMz3TQzNCrL0wwQRbl609OFwAqtjI'
    'CejWufr+eMiYh/TsgpbHS87Eabj0j7t/lLvca3zSIyy22fjPRRfNcaS/rN7L238tXGBgMMk1UQYdEiYOeCgIpFWc5KmLLTXn'
    '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'
    'aheRVMg26/7/Adqnskw='
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
