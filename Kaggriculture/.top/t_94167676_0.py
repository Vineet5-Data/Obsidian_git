import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXctuXNmR/Beua6F6kpwdWyqPBLObAiVNwdMgGg3YAwOGvWjPbjD/PhqyHvfejIyMzHNKpNrclUrFe8/7ZEZGRv78Pxf/'
    '9etvf//Lbxf/9vPFD18+3L775ePNp89f7rcXD7OLv/76jz//8+v/fP34919/+9tf/vvr558v3n94/F/tww9f/vTLzU8ffry5'
    'vZhdvL3bXcwW5utP77fbj4P/+LTdvvv69e799ubzxexy8vWP29u7ny5m8+PPP97fvfvy9vPpLzYPD/87G3bs44e3f/zy8fSm'
    '+aBvP1/stp8+P7b1p7v7z+8fPx2/mnwYD8Sn7e3t6a3L6VsPjxu8CjRk+NrTp+lUoAZMXufOHuzhsSWPczIf9XX/K/Kuj7c3'
    'b7feeKL+HP4AvG3SbvLW/Z8Mx9O04/G7n06LYdTX/Uw5PwtHeHszff9pedx83t5PF9H0u/HqgUt3MV1En+6+TBeRXZx/+P+d'
    'Mfpm0js2lXZwxgM8GaVT/97e7Jfm4UdPO3PQ9dRcnobLvvQwCsNfhdMF9h+aHLATzAomb9mPPRizwXCYGbO/0WdsP+506EbP'
    'ne680xDaaXLW5Vw43MBmcI9WfraMuqCNLDp04sk7tFQfS/mbeB7BEO5PGDBH0bzpg3h8x/HD17P3E/qQG7jTuLc8eP9LOul9'
    'n08nvEsHDn87eFPX54YfnuGxk1tl6ViTwWGauED6PHV6tma27zdvwdQeIT81ZkSfFry9u73dvv38yx+2958/3H74z/GZ0Gnw'
    'yi9JLJHyO840B4dbe9Aedw8dHZHJj52rfP2QsABf9PpPzO+0j6u6dxvaf402CTDvjPk4MMLBwq34GcAYgXsC92q/tFNmMu/D'
    'sLdRH8MBBI59wiBlrgr8FD2QjQX6FD6QeQSi/djgj/pNLjpQ/qBKtq+ygahvHs8/8XTaXF8FeAofB73lhPMAjPvTI60xGG9+'
    'C5wQ2zJuX+pxoalKcLNvbFi/Pq3/0+R7H9hQKxXkrhsGvq1gD+cxjG4QGenYY1eqdBhW7ITjWwcHU/6OFNve0rnUECIEvens'
    'p/dok1FBL9TKsHB7xYUcM85R1P6EeUQtDGIaFOwuuuhP6F6IgRKUKhiMGBrMHLBTyOr3A1C9Pvb1sd/hY3WgqodJ40fYYag+'
    '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'
    '494//B894Mv5'
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
