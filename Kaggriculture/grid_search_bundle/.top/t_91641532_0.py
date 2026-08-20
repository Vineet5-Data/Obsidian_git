"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXcFuXEeS/Bee+6Dupmhpb7LUMxaGFg2JmsasIRgGdgYLLGYP3r0t5t9XEtndr19GRkZm1iMlWyfTVPN1vaqsqszIyMif'
    '/+/iH7/+9s+//3bxbz9f/PTi3buLD6uL//z1v//jfz7+4uOP//z1t//6+/9+/Pnnix9ev919/Ff6w/fv//bLizevf3xxfbG6'
    'eHmzv1itza/f/bDb/XSxujz8w7vd7tXHX+9/2L24vVg9nf36x931zZvJr396e/Pq/cvb6R98+Nfq7C1ev/zL+58m3398n58v'
    '9rt3t58Hevzh/p0nf3Yc3/T1ve+4H8T5t7y5eXv7w+eHnn6y33P/p/R77oepPvv796+vX/3y8X9v339aEPLg2Sf10V+/eLk7'
    'ThKdovtPflqFs+d//Ic3t8eVdb7nT1OjYF9z/sGztX5xu3vrPf/li2CC7j6A5+XwBocvnTz3/kNsXmabDD3uNPTC0tovOD0O'
    'mL2+oPa5x6f5EyIvpH38u5v39xMO5iNcQH+eT4Znp6OyfpPR+fPQWr/jqWXnobN+yoQ01k+al8o6Hv4WTMfdC9Qed7K3+a9q'
    'z7PTO8Qa2Ou3rOHwkN2LgUagzMZgG7j7IfE45OeE10FoaS9vrq93L29/+dPu7e3r69f//nmY9j5J3f6FawsNgzzgcMulBgq+'
    'NRxoMDvJYR/27sgFqmz++oHx7U++/ckX9CfnZ+K73fWn0G2yU+4iMhwBmhjt6kMqfjp6IfHJ47v/Ns5a1Y4yEw+dTw184fWH'
    '5Fkze4/O7XC6FCsDBec/HLsyQv8uwWOM/9xMU3jIH/yDwdMEJh/PUmWAc38/ZQSTqKnw1XaCC0M4TbAZgTy/YNmcCQ4HyCLL'
    'wlFqpqjwjOMM2b9VZwg8FE9Q+bb4o/xt9ao7u/POUcz17Nfvbt++2H+/e/v2bxerbfEynP0w/FIcdT0+zkXZvTIP4elkpbpv'
    'IoViKwBUlq9U/d6wg7PHGp6Rdlg1v35b9wSI++hFPOIFDOyZnSGwiAjrjGNJxUM6mUfpeaeBufj3IDfTcz00J8T6CzNMsHXZ'
    '2oPDBaCKg5yBbp2r79tDxjyk5xe0Il5yJs7Tpd/u/lHhcm/wyYiwOGYTPxdDNCeQ/mS9L97+tXCBgckk10QZdEi4OOChIJFW'
    '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'
    'OZsu0JaVF6jl5z7868P/A3TFLvk='
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
