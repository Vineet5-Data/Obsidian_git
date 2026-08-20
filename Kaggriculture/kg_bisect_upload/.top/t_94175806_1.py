import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vW1ly/C985sOQlGQ5bxqbmxFWYxmyHGJjCIMBskGAYPMwyVuQ/x5Z4sfl7erq6j7nUtKun4Yjk/ee79MfVdXf/nf2'
    '77//8be//jH7p2+zz1dfvswe5rP/+P2//u2/H//w+PFvv//xn3/9n8fP32Y/f/3Lb5/vbj9+/XA/m882v6yvHv97+TD/Nvvl'
    '+m49Cz58//XVp+tfr24ef/zhdjObL8yfv/yyXn+ezc92//Blvf74+Odf1ze3n2bz89Gfty04f3j4v/lRL64//Pnr58Fb9v35'
    'Ntusv9w/NWf/Ydvnwc/2rRh233vHthHHb/l0e3f/y9NDD5/se7Y/pe/ZNlN99s9fr28+/vb4v/dfvw87efDom3rrb64+rPeD'
    'RIdo+83vs3D0/Md/+HS/n1bnPX8azjF7zfEXj+b66n595z3/w1UwQM9fwOOy68HupYPnbr/ExmW0ydDjDk0vTK19weFxYNnr'
    'E2qfu3+aPyDyRNrHf7n9uh1wMB7hBPrjfFh4djgq8zdonT8OZP4ee7q+uTk6TND5t3jQJwQMWMtEKyPXMNHSAFYmfPdbMBzP'
    'Hag97rAwx3+qPc8Ob5dtz7rftBp2D1lfdVwEymh0XgPPHxKPO961z7ZNeG+EK+3D7c3N+sP9b39a391f31z/61Mz7cWTMhMK'
    '9xtqBnnA7jpMNRS8NWxoMDrJZu/2bs8Jqmz++oHx4yc/fvKKfgItmcFOefbbsENo3MmLh5SjtbdC4pPH9xOsQzavHWXGcRL8'
    'Z2PURWfNqB8tt8PhUqw0FJz/sO1KC/27BLcx/rkZpvCQ39kHnYcJDD4epUoDx/Z+ahEM3KvCq+0AF5pwGGDTAnl8wbQ5Axw2'
    'kLmghaPUDFHhGfsRsr9VRwg8FA9Q+bb4R/lt9ao7uvOOo5djX//L/d3V5uf13d1fZvNV8TIcfeh+Kfa6Hl/momy9Mnfu6WCm'
    'WnsiuWJzENEsX6n6vWEbZ481PCLNbtX4+m26J4DfRy/iHh0w8dHsCIFJREHR2JdULKTD8ig979AwN1Deycz0TA/NCLH2wigm'
    '2HTZ2oPDDUAVGzkKurVcfT8e0uchbXZBk8dLzsQgTfrj7i+7y22NT3qExTYb/7noojmO9PfVe3X3L4ULDAwmuSbKQYeEiQMe'
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
