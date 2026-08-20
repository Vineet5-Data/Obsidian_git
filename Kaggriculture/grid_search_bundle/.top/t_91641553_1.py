"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vXFlu/C967ofplizbedPYvTvGaizDltPYDITBALtBgGDzMMlbkP8e2VJ/XRaLRfLclsbrt7bcfe/5PmSxWPzlf8/+'
    '/bff//H338/+5ZezD1efPp3dLc7+47f/+tt/3//h/uM/fvv9P//+P/effzn76d3H9f3/0g8/fv7rr1fv3/18dX22OHtzszlb'
    'LM2fP/20Xn84W1xs/+PTev32/s+bn9ZXt2eLF5M//7y+vnl/8OcPH2/efn5ze/iDu/9bHPXi3Zu/fP5w8P5df34526w/3X5t'
    '6O7DY58PfrZr32H3vXc8NuL4Le9vPt7+9PWh+0/2PY8/pe95bKb67B8/v7t+++v9P28/f5kQ8uDJN/XWX1+9We8GiQ7R4ze/'
    'zMLR8+//4/3tbmad9/zpcFGw1xx/8Wiur27XH73nv7kKBujhC3hctj3YvvTguY9fYuMy2WTocfumF6bWvmD/OLDs9Qm1z909'
    'zR8QeSLt4z/dfH4ccDAe4QT647xfeHY4KvN30Dp/HFrztzu17Dh05k8ZkMb8SeNSmcftb8FwPHSg9rj9epv+qfY8O7xDVgPr'
    'fms1bB+yvhq4CJTRGLwGHj4kHofsnPA6CFfam5vr6/Wb21//tP54++763b99baa9T1K3f+HaQs0gD9jecqmGgreGDQ1GJ9ns'
    '7d4dOUGVzV8/ML7/5PtPntFPjs/ET+vrL67bwU558MiwB2h8tMu7lP+0s0Lik8c3/62ftagdZcYfOh4a2OHlXfKsmfSjczvs'
    'L8VKQ8H5D9uutNC/S3Ab45+bYQoP+a19MHiYwODjUao0cGrvpxbBgddUeLUd4EIT9gNsWiCPL5g2Z4DDBjLPsnCUmiEqPGM3'
    'Qva36giBh+IBKt8W/yy/rV51R3feMYq5nPz50+3Hq82P648f/3q2OC9ehpMPwy/FUdfj01yU3Stz654ezFS3J5IrtgBAZflK'
    '1e8N2zh7rOERabtV0+u3dU8Av49exCM6YGDP7AiBSURYZ+xLKhbSfnmUnrdvmIt/DzIzPdNDM0KsvTDBBFuXrT04XACq2MgJ'
    '6Na5+r4/ZMxDenZBy+MlZ+I0XPr97h/lLvcan/QIi202/nPRRXMc6S+r9+rjvxYuMDCY5Joogw4JEwc8FATSKk7y1MWWmvN4'
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
