import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXctuHEmS/BeeeVC9+NgbW6pZCcNuChQ1xGyj0GhgZ7HAYvbQu7fF/PtqxHpkZliYm3lEkuwGb6ViKTPe4W5ubv7z/539'
    'x6+//f1vv539y89nP3z9dPvhl883Xx6+3m/Pdudn//nrf//7/3z7y7ePf//1t//62/9++/zz2cdP3/+qffjh619/ufnp0483'
    't2fnZ+/vHs/Ol8XXXz5ut58Hf/iy3X749vXjx+3Nw9n55eTrH7e3dz+dnS+OP/98f/fh6/uH0/+42O3+cT7s2OdP7//89fPp'
    'TYtB334+e9x+efje1p/u7h8+fv90/GryYTwQX7a3t6e3rqZvPTxu8CrQkOFrT5+mU4EaMHlddfZgD48t+T4ni1Ff978i7/p8'
    'e/N+WxtP1J/DfwBvm7SbvHX/X4bjWbTj+3c/nRbDqK/7mar8LBzh7c30/aflcfOwvZ8uoul349UDl+5yuoi+3H2dLqJycf7p'
    'nztj9M2kd2wqy8EZD/BklE79e3+zX5qHHz3tzEHXrbk8DVf50sMoDH8VThfYf2hywE4oVjB5y37swZgNhqOYsfI3+oztx50O'
    '3ei50513GsJymirrciEcbmAzVI9WfraMuqCNLDp04sk7tFQfS/mbeB7BEO5PGDBH0bzpg3h8x/HDt7P3C/rgDdxp3FsevP8l'
    'nfS+z6cT3qUDh/87eFPX54YfXuCxk1tlVbEmg8PUuED6PHV6tjrb99lbMLVHyE8LM6JPC97f3d5u3z/88qft/cOn20//Nj4T'
    'Og1e+iXGEkm/Y6Y5ONzag/ZU99DREZn8uHKVb3aGBfiq178xv9M+rvPebWj/NdokwLwrzMeBEQ4WbsbPAMYI3BO4V/ulbZnJ'
    'vA/D3kZ9DAcQOPaGQcpcFfgpeiAbC/QpfCDzCET7scEfrTc56UDVB1WyfZUNRH3zeP6Jp9Pm+irAU/g46C0bzgMw7k+PLI3B'
    'ePOXwAmxLeP2WY8LTVWCmz2zYf32tP5Pk+99YEOtVZA7bxjUbYXycB7D6IsJLP7t1Lu/Q0iNdByyq1Y6JDP2w/GtgwPLvzvF'
    'trd0zhpChKw33Qn0fm0yNuhFmxkWbsdUoUjHaYrab5hN1PIgJkPCHqOL/oT6hdgoQa+CwYghQ+fgnUJZfxzg6u2xb4/9HT5W'
    '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'
    'IVA+kKaukILl7h+7/wd7otNk'
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
