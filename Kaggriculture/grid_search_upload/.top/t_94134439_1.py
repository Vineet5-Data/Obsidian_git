import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vW1ly/C965oNJ6jNvGpu7Y6x2ZMh2iM1AGAywuwgQbB4meQvy3+NYInl5T3V1VZ9DyXHmyQRF33u+T3d1dfXP/3X2'
    '919/+8fffjv7p5/Pfvj8/u7dLx9uP376/LA5e1yc/euv//7X//jyly8f//Hrb//2t//88vnnsx/ff/2r9uGHz3/55fan93++'
    'vTtbnL29354tVs3XH3/cbD5M/vBxs3n35evtj5vbT2eLq9nXf97c3f90tljuf/7h4f7d57efDv/j8vHxvxfTjn14//ZPnz8c'
    '3rSc9O3ns+3m46evbf3p/uHTj18/7b+afTgeiI+bu7vDW9dhe9bz9uxeNGkEaOK0QYdP80lCTZu9LpxX2Pd9S77O1vJoFJ5/'
    'Rd714e727SYaadSf3X8Ab5u1m7z1+b9Mx7Npx9fvfjpMy1Ffn2cq+Fk6wpvb+fsPC+f20+Zhvrzm3x2vK7iIVvNF9PH+83wR'
    'tcv2D/+7Z46+mfWOTWU7OMcDPBulQ//e3j4vzd2PnvbspOvWXB6Gq33pbhSmv0qnC+w/NDlgJzQrmLzleezBmE2Go5mx9jf6'
    'jD2POx26o+fOd95hCNtpCtblUjjcwGYID11+thx1QRtZdOjkk7drqT6W8jf5PIIhfD5hwBxl86YP4v4d+w9fzt6P6IM3cIdx'
    '73nw8y/ppI99Pp3wIR3Y/d/Jm4Y+N/3wCo+d3SrrwM5MDlPjAhnz1PnZ6mzfF2/B3B4hP23MiDEteHt/d7d5++mXP2wePr2/'
    'e/8vx2fCoMErv8RYIuV3sDlofYeOWdnd45MWhrtq/+LZj4PL/eLRsAm/6R1hzPi8j+d1Tzi1CDutFGDwNQblxCwHS7nieQDz'
    'BO4S3KvnpW0ZzrwP095mfUwHEIAAhonKnBf4KXsgGwv0KX0g8xFEi7LDQ42bXHSp4kGVrGFlA1FvPZ9/4vv0OcMKSJU+DvrP'
    'hjsBzP3DI1vzMN/8LZRCrM28fdbjUuOVIGkvbGr//rTxT5PvfWBDnWOwe9llFCDQWTQ12MXWd8UxfCe4nVProHANZoZAJ3gn'
    'XQxDDASEPIaXRvFuZHD74bjuGxXwMufR1FgAb4nmP70RNBuiZJ6Q4eFWW/5oClkDgC0x4J5PsOdY2vmjgYXRMRpyZMN1O/Qu'
    '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'
    'w6wHSlcCkuHj/wAZwKaN'
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
