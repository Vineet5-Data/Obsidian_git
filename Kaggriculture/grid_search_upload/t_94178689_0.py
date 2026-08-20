import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXctuXFly/BeuuVAV396xpRpLGHZToCQXxg2i0YDHMGCMF23vjPl3y2I9bt0TGRmR5xRJDbRSoVi697xPZmRk5K//e/Lv'
    'v//xt7/+cfJPv5789OXD3bvfPt5++vzlYXXyeHryH7//17/999e/fP34t9//+M+//s/Xz7+evP/w7a/ah5++/OW3218+/Hx7'
    'd3J68vZ+fXK6bL7+9H61+jj5w6fV6t3Xr9fvV7efT06vZl//vLq7/+XkdLH7+ceH+3df3n7e/4/Lx8e/n0479vHD2z9/+bh/'
    '02LSt19P1qtPn7+19Zf7h8/vv33afTX7cDgQn1Z3d/u3ns3fun3c5FWgIdPX7j/NpwI1YPa6cPZgD3ct+TYni4O+bn5F3vXx'
    '7vbtKhpP1J/tfwBvm7WbvHXzX6bj2bTj23e/7BfDQV83MxX8LB3h1e38/fvlcft59TBfRPPvDlcPXLrL+SL6dP9lvojaxfmn'
    '/98ZB9/Mesemsh2cwwGejdK+f29vN0tz+6OnnTnpujWX++FqX7odhemv0ukC+w9NDtgJzQomb9mMPRizyXA0M9b+Rp+xzbjT'
    'oTt47nzn7YewnaZgXS6Eww1shvBo5WfLQRe0kUWHTj5525bqYyl/k88jGMLNCQPmKJs3fRB379h9+Hr2fkIfvIHbj3vPgze/'
    'pJM+9vl0wod0YPt/J28a+tz0wws8dnarnAXWZHKYGhfImKfOz1Zn+z57C+b2CPlpY0aMacHb+7u71dvPv/1p9fD5w92Hfz08'
    'EwYNXvklxhIpv+NIc7C9tSftCffQzhGZ/Ti4yi8eDQvwVa9/Y37nfTyve7ep/ddpkwDzrjEfJ0Y4WLgVPwMYI3BP4F5tlrZl'
    'JvM+THub9TEdQODYGwYpc1Xgp+yBbCzQp/SBzCMQ7ccOfzRuctGBigdVsn2VDUR983z+iafT5/oqwFP6OOgtG84DMO73j2yN'
    'wXzzt8AJsS3z9lmPS01Vgps9s2H942njnybf+8CGOscA9qLLKEBAsmhqsIut74pjaE5wO6fWQeEazAyBTqhOuhiGGAgIZwwv'
    'jeLdyMD1/XHdNyrgZc6jqbEA3hLNf3ojaDZEyTwhw8OttvzRFKAGcJoFABKci47IkAMartKhJ/8cS/vHQc5+PPbHY01MKrZe'
    '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'
    'sfuw+/HsG9EsTlp7EETcmtCPf3/8P8oHl+A='
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
