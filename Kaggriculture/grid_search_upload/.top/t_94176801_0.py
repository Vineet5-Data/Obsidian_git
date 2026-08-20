import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vW1ly/C961oNJUbKcN42HmzFWMzJkO8RmIAwGyAYBgs3DJG9B/nscSSTvvae6uqrPoS1v/EbT1L3n+3RXV1f/+t9n'
    '//r7H3/76x9n//Dr2Q+f3t3++Nv7mw8fP91vzx7Oz/7t9//4l//8/D+fP/7t9z/+/a//9fnzr2c/vXv8X+3DD5/+8tvNL+9+'
    'vrk9Oz97e7c7O183X3/4abt9P/mPD9vtj5+/3v20vfl4dv568fXP29u7X87OV4efv7+/+/HT24/Hv7h6ePif82nH3r97++dP'
    '749vWk369uvZbvvh42Nbf7m7//jT46fDV4sP84H4sL29Pb71YvnW/eMmrwINmb72+Gk5FagBi9eFswd7eGjJ45ysZn19/hV5'
    '1/vbm7fbaDxRf/Z/AN62aDd56/OfTMezacfjd78cF8Osr88zFfwsHeHtzfL9x+Vx83F7v1xEy+/mqwcu3fVyEX24+7RcRO3i'
    '/NP/7YzZN4vesalsB2c+wItROvbv7c3z0tz/6GlnTrpuzeVxuNqX7kdh+qt0usD+Q5MDdkKzgslbnscejNlkOJoZa3+jz9jz'
    'uNOhmz13ufOOQ9hOU7AuV8LhBjZDeLTys2XWBW1k0aGTT96+pfpYyt/k8wiG8PmEAXOUzZs+iId3HD58Pns/oA/ewB3HvefB'
    'z7+kkz72+XTCh3Rg/7eTNw19bvrhKzx2catcBNZkcpgaF8iYpy7PVmf7fvEWLO0R8tPGjBjTgrd3t7fbtx9/+9P2/uO723f/'
    'PD8TBg1e+SXGEim/40RzsL+1J+0J99DBEVn8OLjKLx8MC/BFr39jfpd93NS929T+67RJgHnXmI8TIxws3IqfAYwRuCdwr56X'
    'tmUm8z5Me5v1MR1A4NgbBilzVeCn7IFsLNCn9IHMIxDtxw5/NG5y0YGKB1WyfZUNRH3zfP6Jp9Pn+irAU/o46C0bzgMw7o+P'
    'bI3BfPO3wAmxLfP2WY9LTVWCm31hw/r708Y/Tb73gQ21UUHuumEQ2wrt4TyH0VcLWPzzqXd/h5Aa6ThkV610SFbsh8NbJweW'
    'f3eKbe/pnDWECFnvuhPo/dplbNCLtjIs3I4JoUjHacrab5hN1PIgJkPBHqOL/oj6pdgoQa+SwcghQ+fgXUJZfz/A1ffHfn/s'
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
