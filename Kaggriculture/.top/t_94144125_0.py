import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vW1ly/C961oNJfZjOm8bmro3VjAzZDrEZEIMBsosFFpuHSd6C/Pc4lkhe3lNdXdXnUNJs/GSCou8936e7urr65/8+'
    '++uvv/3jL7+d/cvPZz98+XD77pePN58+f7lfn23Pz/7263/8+39+/cvXj//49be//+W/vn7++ez9h29/1T788OXPv9z89OHH'
    'm9uz87O3d5uz82Xz9af36/XHyR8+rdfvvn69eb+++Xx2/nr29Y/r27ufzs4X+59/vL979+Xt58P/uN5u/+d82rGPH97+6cvH'
    'w5sWk779fLZZf/r8ra0/3d1/fv/t0/6r2Yfjgfi0vr09vPVi/tbd4yavAg2ZvvbwaT4VqAGz14WzB3u4b8m3OVkc9fXxV+Rd'
    'H29v3q6j8UT92f0H8LZZu8lbH//LdDybdnz77qfDYjjq6+NMBT9LR3h9M3//YXncfF7fzxfR/Lvj1QOX7nK+iD7dfZkvonZx'
    '/uH/dsbRN7PesalsB+d4gGejdOjf25vHpbn70cPOnHTdmsvDcLUv3Y3C9FfpdIH9hyYH7IRmBZO3PI49GLPJcDQz1v5Gn7HH'
    'cadDd/Tc+c47DGE7TcG6XAiHG9gM4dHKz5ajLmgjiw6dfPJ2LdXHUv4mn0cwhI8nDJijbN70Qdy/Y//h69n7CX3wBu4w7j0P'
    'fvwlnfSxz6cTPqQDu/87edPQ56YfnuGxs1vlIrAmk8PUuEDGPHV+tjrb98lbMLdHyE8bM2JMC97e3d6u337+5Q/r+88fbj/8'
    '2/GZMGjwyi8xlkj5HSeag92tPWlPuIf2jsjsx8FVfrU1LMAXvf6N+Z338bLu3ab2X6dNAsy7xnycGOFg4Vb8DGCMwD2Be/W4'
    'tC0zmfdh2tusj+kAAsfeMEiZqwI/ZQ9kY4E+pQ9kHoFoP3b4o3GTiw5UPKiS7atsIOqb5/NPPJ0+11cBntLHQW/ZcB6AcX94'
    'ZGsM5pu/BU6IbZm3z3pcaqoS3OyJDevvTxv/NPneBzbUJQawF11GAQKSRVODXWx9VxxDc4LbObUOCtdgZgh0QnXSxTDEQEA4'
    'Y3hpFO9GBq4fjuu+UQEvcx5NjQXwlmj+0xtBsyFK5gkZHm615Y+mADWA0ywAkOBcdESGHNBwlQ49+edY2j8Pcvb9sd8fa2JS'
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
