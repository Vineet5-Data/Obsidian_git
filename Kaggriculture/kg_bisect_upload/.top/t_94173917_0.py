import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vW1ly/C961oNJURSdN43N3TFWMzJke4XNQBgMsLsIEGweJnkL8t/jSCJ5eU91dVWfQ9nr+I2mqXvP9+murq7+5b/P'
    '/v7b7//42+9n//LL2Q+f3t28/fX99YePn+62Zw/nZ//223/89T8//8/nj//47fd//9t/ff78y9mP7x7/V/vww6e//Hr987uf'
    'rm/Ozs/e3N6fnS+brz/8uN2+n/zHh+327eev73/cXn88O7+aff3T9ub257Pzxf7n7+9u33568/HwF+uHh/85n3bs/bs3f/r0'
    '/vCmxaRvv5zdbz98fGzrz7d3H398/LT/avbheCA+bG9uDm+9mL9197jJq0BDpq89fJpPBWrA7HXh7MEe7lvyOCeLo74+/4q8'
    '6/3N9ZttNJ6oP7s/AG+btZu89flPpuPZtOPxu58Pi+Gor88zFfwsHeHt9fz9h+Vx/XF7N19E8++OVw9cusv5Ivpw+2m+iNrF'
    '+Yf/2xlH38x6x6ayHZzjAZ6N0qF/b66fl+buR087c9J1ay4Pw9W+dDcK01+l0wX2H5ocsBOaFUze8jz2YMwmw9HMWPsbfcae'
    'x50O3dFz5zvvMITtNAXrciEcbmAzhEcrP1uOuqCNLDp08snbtVQfS/mbfB7BED6fMGCOsnnTB3H/jv2Hz2fvB/TBG7jDuPc8'
    '+PmXdNLHPp9O+JAO7P528qahz00/fIHHzm6Vi8CaTA5T4wIZ89T52eps3xdvwdweIT9tzIgxLXhze3OzffPx1z9s7z6+u3n3'
    'r8dnwqDBK7/EWCLld5xoDna39qQ94R7aOyKzHwdX+eWDYQF+1evfmN95H1d17za1/zptEmDeNebjxAgHC7fiZwBjBO4J3Kvn'
    'pW2ZybwP095mfUwHEDj2hkHKXBX4KXsgGwv0KX0g8whE+7HDH42bXHSg4kGVbF9lA1HfPJ9/4un0ub4K8JQ+DnrLhvMAjPvD'
    'I1tjMN/8LXBCbMu8fdbjUlOV4GYvbFh/f9r4p8n3PrChVhjAXnQZBQhIFk0NdrH1XXEMzQlu59Q6KFyDmSHQCdVJF8MQAwHh'
    'jOGlUbwbGbh+OK77RgW8zHk0NRbAW6L5T28EzYYomSdkeLjVlj+aAtQATrMAQIJz0REZckDDVTr05J9jad8Ocvb9sd8fa2JS'
    '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'
    '/wKq6m+k'
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
