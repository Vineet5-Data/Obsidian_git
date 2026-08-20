"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vW9mR/S9ac2FSsts9O8VmYiFqy5DkEJmG0GhgEgQYZBY9sxvMfx/FksjHV1WnTn1ckjJ6ZZoi+e73rY9T5/z8v2d/'
    '//W3f/7tt7N/+/nsy+Xd3dnD4uwfv/7Xf/z34xuPL//562//+bf/eXz989mnq9v141+5F3/4+tdfLj9f/XR5fbY4+3CzOVus'
    'xNt3n9brL5M/3K3XHx/f3nxaX96fLX6Yvf3T+vrm89liuf34l9ubj18/3O++8fbh4f8We/25+vDnr192T1pO+vbz2WZ9d/+t'
    'rZ9vbu8/fXu1fWv2Yn8g7tbX17unLs2nbj8wfer2r9NBubr++Mvj4N9/fR49rh3qIIjmPP+E1oTdsNiPzI0BeOjzV87H93z+'
    '65PW7KZcmfz5W9Nnz+f6+vLDejuSe4+QfdMeKl6Bh/1xuj/2B/e5Gf9aU//6rcf/f77f7hn9nciTP1zOB3DWlsehurxf385e'
    'vTx096lZM9DIzs6ibSOmLV9f3hlPD/3y7gflMG0fsX1xd/PVGS75BGWhb1u8/eHe4ZqvifZRE0tAtl955tOL3MTv2otmrDJo'
    '8viZHAal0XpeNcw0L6afTowXWmxyc/YM3PwgHDCCxHqT74BrJLPu0PBlzoXndybt3L1jPSr3AGWwtn+aPTLZg117xQ8/vQj8'
    'LvooMK/A115WIfNZ66IN3JDoozfX1+sP97/8cX17f3V99e/fRq27C4doz9zIAx99Oc9+b3q56ZGt8vtHoUf77MRMpmBxYbuz'
    'AX/z+QMX0N+M7PTQt20/oWbzw2+zThle9zEbYdQwRdogh6nBc+0cJOmK8zaROPtij7ZHeGffum1QBhg1oWuId06S10BlgANj'
    'pAxxwNMcvoal+9E1wJMlkDA75+5z0ss79JMLpnbk6krcS7FjtuESylw9I9Zh7jYunH35E2/IVZI+3oL3hvcc9yhLHGAD797Q'
    'iPkHuX3TpobMPZoOusbC7v/39JWsyzF7UXI1mHzKPPsWt7UXo7yU2A8Tjovzg8PM9EWbF2hHVwt3khFi/3R5+5f4nTU38dWo'
    '/XNT0nESxYwMjgmy3ne/PU9kZO4+I5Bcmja5rLaTlZ44LV7vhtoLM6idUSX/VusA785Bn1dbbQXLZjpZux/cezc+f3KuQIbR'
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
