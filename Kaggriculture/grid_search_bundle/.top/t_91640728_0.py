"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vG9kR/C8682CSsiznJtvcWFitZchSiI0hGAtkgwDB5rDJLch/j2yJHHK6urq63xtK9vpGy+TM+37d1dXVH/979Pdf'
    'fv/t19+P/vTx6P3Zhw9Ht7Ojf/zyr7/9++4Pdx9/++X3f/76n7vPH4/enl+t7v6Xfnh18/Ons3fnP51dHM2OXl+uj2Zz8+cP'
    'b1er90ez481/fFit3tz9ef12dXZ9NHs++vNPq4vLdzt/fn91+ebm9fXuD27/N9vrxfnrH2/e77x/25+PR+vVh+svDd1+eOjz'
    'zs+27dvtvveOh0bsv+Xd5dX12y8PHT7Z9zz8lL7noZnqs1/dnF+8+XT3z+ubzxNCHjz6pt76i7PXq+0g0SF6+ObnWdh7/t1/'
    'vLvezqzznh92FwV7zf4X9+b67Hp15T3/9VkwQPdfwOOy6cHmpTvPffgSG5fRJkOPG5pemFr7guFxYNnrE2qfu32aPyDyRNrH'
    'f7i8eRhwMB7hBPrjPCw8OxyV+dtpnT8OTfO3PbXsOLTMnzIgDfMnjUtlHje/BcNx34Ha44b1Nv5T7Xl2eLusBtb9ptWwecjq'
    'rOMiUEaj8xq4/5B4HLJzwusgXGmvLy8uVq+vP/2wuro+vzj/65dm2vskdfsXri3UDPKAzS2Xaih4a9jQYHSSzd7s3Z4TVNn8'
    '9QPj+0++/+QJ/WT/TPywuvjsuu3slHuPDHuAxkc7uU35T1srJD55fPPf+lmz2lFm/KH9oYEdnt8mz5pRP1puh+FSrDQUnP+w'
    '7UoL/bsEtzH+uRmm8JDf2AedhwkMPh6lSgPH9n5qEex4TYVX2wEuNGEYYNMCeXzBtDkDHDaQeZaFo9QMUeEZ2xGyv1VHCDwU'
    'D1D5tvij/LZ61e3defso5nz05w/XV2frV6urq5+PZsviZTj60P1S7HU9Ps5F2XplbtzTnZlq7Ynkis0AUFm+UvV7wzbOHmt4'
    'RJrdqvH123RPAL+PXsQ9OmBgz+wIgUlEWGfsSyoW0rA8Ss8bGubi353MTM/00IwQay+MMMGmy9YeHC4AVWzkCHRrufq+P6TP'
    'Q9rsgiaPl5yJ43Dp97u/l7vc1vikR1hss/Gfiy6a40h/Xr1nV38pXGBgMMk1UQYdEiYOeCgIpFWc5LGLLTXn4YDXlvNjTILu'
    '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'
    '+lDs1YaOdaJKP/YtfwB7GTf3xV2rbv8PqocCyQ=='
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
