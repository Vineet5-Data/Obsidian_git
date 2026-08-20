import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vXEly/C8886BuNinSN47UawnLGQqUZGI9IAYDeA0Dxvow9s3wf7eW7I/XryIjI7KqSWqhW6PZfK++KzMyMvLX/z35'
    '99//+Ntf/zj5p19Pfvr68eb9b5+uP3/5erc+eTg9+Y/f/+vf/vvbX759/Nvvf/znX//n2+dfTz58fPyr9uGnr3/57fqXjz9f'
    '35ycnry7vT85XTZff/6wXn+a/OHzev3+29f3H9bXX05O386+/nl9c/vLyeli9/NPd7fvv777sv+Pi4eH/zudduzTx3d//vpp'
    '/6bFpG+/ntyvP395bOsvt3dfPjx+2n01+3A4EJ/XNzf7t57N37p93ORVoCHT1+4/zacCNWD2unD2YA93LXmck8VBXze/Iu/6'
    'dHP9bh2NJ+rP9h/A22btJm/d/Mt0PJt2PH73y34xHPR1M1PBz9IRXl/P379fHtdf1nfzRTT/7nD1wKW7nC+iz7df54uoXZx/'
    '+vvOOPhm1js2le3gHA7wbJT2/Xt3vVma2x897cxJ16253A9X+9LtKEx/lU4X2H9ocsBOaFYwectm7MGYTYajmbH2N/qMbcad'
    'Dt3Bc+c7bz+E7TQF63IhHG5gM4RHKz9bDrqgjSw6dPLJ27ZUH0v5m3wewRBuThgwR9m86YO4e8fuw7ez9zP64A3cftx7Hrz5'
    'JZ30sc+nEz6kA9v/nbxp6HPTDy/w2NmtchZYk8lhalwgY546P1ud7fvsLZjbI+SnjRkxpgXvbm9u1u++/Pan9d2Xjzcf//Xw'
    'TBg0eOWXGEuk/I4jzcH21p60J9xDO0dk9uPgKj9/MCzAV73+jfmd93FV925T+6/TJgHmXWM+ToxwsHArfgYwRuCewL3aLG3L'
    'TOZ9mPY262M6gMCxNwxS5qrAT9kD2VigT+kDmUcg2o8d/mjc5KIDFQ+qZPsqG4j65vn8E0+nz/VVgKf0cdBbNpwHYNzvH9ka'
    'g/nmb4ETYlvm7bMel5qqBDd7ZsP6x9PGP02+94ENtVJB7rphENsK7eF8CKMvZrD4t1Pv7hYhNdJxyK5a6ZCs2A+7t04OLP/u'
    'FNve0zlrCBGy3nUn0Pu1y9igF21lWLgdE0KRjtOUtd8wm6jlQUyGgj1GF/0e9UuxUYJeJYORQ4bOwTuHsv5xgKsfj/3x2O/w'
    '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'
    '3QHlQ3ZAPfw/bCOpjQ=='
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
