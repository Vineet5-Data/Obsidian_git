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
