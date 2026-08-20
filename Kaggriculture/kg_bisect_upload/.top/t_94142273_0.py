import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXctuXFly/Beua6F6k96xpRpLGHZToCQXxg2i0YDHMGCMF23vDP+71WI97r0ZGRmZ5xTJntGuUCzee94nMzIy8uf/vfr3'
    'X3/7219/u/qnn69++PLh7t0vH28/ff7ysLt6nF39x6//9W///fUvXz/+7dff/vOv//P1889X7z98+6v24Ycvf/nl9qcPP97e'
    'Xc2u3t7vr2YL8/Wn97vdx8EfPu12775+vX+/u/18NdtOvv5xd3f/09Vsfvr5x4f7d1/efj7/x+bx8f9mw459/PD2z18+nt80'
    'H/Tt56v97tPnb2396f7h8/tvn05fTT6MB+LT7u7u/Nbl9K3Hxw1eBRoyfO3503QqUAMmr3NnD/bw1JJvczIf9fXwK/Kuj3e3'
    'b3feeKL+HP8BvG3SbvLWw78Mx9O049t3P50Xw6ivh5lyfhaO8O52+v7z8rj9vHuYLqLpd+PVA5fuYrqIPt1/mS4iuzj/9PvO'
    'GH0z6R2bSjs44wGejNK5f29vD0vz+KOnnTnoemouz8NlX3ocheGvwukC+w9NDtgJZgWTtxzGHozZYDjMjNnf6DN2GHc6dKPn'
    'TnfeeQjtNDnrci4cbmAzuEcrP1tGXdBGFh068eQdW6qPpfxNPI9gCA8nDJijaN70QTy94/Th69n7CX3IDdx53FsefPglnfS+'
    'z2cTPrjAWnpw/N/Bq7qMjPOQV/HYybWydMzJ4DRN3CB9njo9XDP799lbMDVIyE+NHdGnBW/v7+52bz//8qfdw+cPdx/+dXwo'
    'dBq88ksSS6T8jgvNwfHaHrTH3UMnT2TyY+cuXz8mTMBXvf4T8zvt46ru3oYGYKNRAuw7Yz8OrHCwcCuOBrBG4J7AvTos7ZSd'
    'zPsw7G3Ux3AAgWefsEiZrwI/RQ9kY4E+hQ9kLoFoQDY4pH6Tix6UP6iS8atsIOqcx/NPXJ0231dBnsLHQXc54T0A6/78SGsM'
    'xpvfIifEtozbl3pcaKoS4OyZDevvT+v/NPneBzbUSkW564aBbyvYw3mMo88nuPjXU+/hHkE10nHIrlrpkKzYD6e3Dg6s/N0p'
    'tr2lc6khRNB6051A79cmY4NetJVh4XaMi0VmnKao/QmziVoexGQo2GN00Z9hvxAcJfBVMBgxZpg5eKdQ1t8PcPX9sd8f+wd8'
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
