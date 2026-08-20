import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vHFly/C8886D+IkXfOFLvSljOUKAoN9aDxmCAXcOAsT6MfTP8361Rf1XVi4yMzHxN9ix0azVbVe8j61VmZGTkz/97'
    '9e+//vaPv/929S8/X/3w5ePD+18+3X9+/vK0vtpeX/3Hr//1t//++pevH//x62//+ff/+fr556sPH7/9Vfvww5e//nL/08cf'
    '7x+urq/ePW6urufN158/rNefBn/4vF6///r15sP6/vnq+nby9Y/rh8efrq5nx59/enp8/+Xd8+l/3Gy3/3c9nNinj+/+8uXT'
    '6U6zwdx+vtqsPz9/G+tPj0/PH759On41+TBeiM/rh4fTXRfTux4uN7gVGMjwtqdP061AA5jcztw9OMPjSL7tyWw01/2vyL0+'
    'Pdy/W1vrieZz+A/gbpNxk7vu/8twPZtxfPvup5MxjOa63ynjZ+4Kr++n9z+Zx/3z+mlqRNPvxtYDTXc+NaLPj1+mRtQa559+'
    'fzJG30xmx7ayXZzxAk9W6TS/d/d70zz8aPdkDqYe2svTcrU3PazC8FfudoHnD20OeBIaCyZ32a89WLPBcjQ71v5G37H9utOl'
    'G113+uSdlrDdJsMuZ8LhBh4G82jlZ8toCtrKokPH37zDSPW1lL/x9xEs4f6EAXvk7Zu+iMd7HD98PXs/ow+xhTute+XC+1/S'
    'Te97fbrhXSZw+L+DO3W9rvvhFS47eassDG/SOUwDL5A+V52erZHH98VHMPVHyE8bN6LPCN49Pjys3z3/8qf10/PHh4//Nj4T'
    'Oi1e+iYBE0nf40x7cHhrD8ZjPkPHQGTyY+NVvtoGPMCLtv/A/k7nuMxHt67/V/RJgHvXuI8DJxwYbibOAM4IfCbwrPamHXKT'
    '+RyGs/Xm6C4gCOwDDikLVeAn74JsLdAn94IsIhD9x0I8ag85GUDZiyr5vsoDRGNzf/9JpFMLfRXgyb0cjJYDwQNw7k+XbJ1B'
    '/+FvgRPiW/rjC13OdVUJbvbCjvX3q/W/mvzeBz7UEgPYs5JTgIBk0dVgL7baK46hOcbb2fUOEq9BzxEoQnXSi6GLg4BwRvOl'
    'kXw3MnD9dFzXVgXcLHJp6iyAu1j7774RNB8i5Z6Q5eFem39pClADOC0EABKci65IlwMaWmnXk3+Kpf3zIGffL/v9skFMyvZe'
    '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'
    '/wEyGl/D'
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
