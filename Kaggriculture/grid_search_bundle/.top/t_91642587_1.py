"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vG9kR/C8682CSktbOTWtzY2G1liFLITaGYCyQDQIEm8MmtyD/PbIkcsjp6urqfm8o2esbLZMz7/t1V1dXf/zv0d9/'
    '+f23X38/+tPHo/dnHz4c3c6O/vHLv/7277s/3H387Zff//nrf+4+fzx6e361uvtf+uH7m58/nb07/+ns4mh29PpyfTSbmz9/'
    'eLtavT+aHW/+48Nq9ebuz+u3q7Pro9nJ6M8/rS4u3+38+f3V5Zub19e7P7j932yvF+evf7x5v/P+bX8+Hq1XH67vG7r98Njn'
    'nZ9t27fbfe8dj43Yf8u7y6vrt/cPHT7Z9zz+lL7nsZnqs7+/Ob948+nun9c3nyeEPHj0Tb31F2evV9tBokP0+M3Ps7D3/Lv/'
    'eHe9nVnnPT/sLgr2mv0v7s312fXqynv+67NggB6+gMdl04PNS3ee+/glNi6jTYYeNzS9MLX2BcPjwLLXJ9Q+d/s0f0DkibSP'
    '/3B58zjgYDzCCfTHeVh4djgq87fTOn8cmuZve2rZcWiZP2VAGuZPGpfKPG5+C4bjoQO1xw3rbfyn2vPs8HZZDaz7Tath85DV'
    'WcdFoIxG5zXw8CHxOGTnhNdBuNJeX15crF5ff/phdXV9fnH+1/tm2vskdfsXri3UDPKAzS2Xaih4a9jQYHSSzd7s3Z4TVNn8'
    '9QPj20++/eQZ/WT/TPywuvjsuu3slAePDHuAxkc7vU35T1srJD55fPPf+lmz2lFm/KH9oYEdnt8mz5pRP1puh+FSrDQUnP+w'
    '7UoL/bsEtzH+uRmm8JDf2AedhwkMPh6lSgPH9n5qEex4TYVX2wEuNGEYYNMCeXzBtDkDHDaQeZaFo9QMUeEZ2xGyv1VHCDwU'
    'D1D5tvij/LZ61e3defso5nz05w/XV2fr71dXVz8fzZbFy3D0oful2Ot6fJqLsvXK3LinOzPV2hPJFZsBoLJ8per3hm2cPdbw'
    'iDS7VePrt+meAH4fvYh7dMDAntkRApOIsM7Yl1QspGF5lJ43NMzFvzuZmZ7poRkh1l4YYYJNl609OFwAqtjIEejWcvV9e0if'
    'h7TZBU0eLzkTx+HSb3d/L3e5rfFJj7DYZuM/F100x5H+vHrPrv5SuMDAYJJrogw6JEwc8FAQSKs4yWMXW2rO4wGvLeenmATd'
    '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'
    'v7tr1e3/AXXJ4KE='
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
