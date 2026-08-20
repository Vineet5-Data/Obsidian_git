"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vG1mS/C8682CSsmzvTS1zuoWRLUOWh5htCI0GdgYDLGYPvXtb7H9fWRJZxcrIyMh8ryjZ4xstk1Xv+2VGRkb++r8n'
    'f//9j3/+7Y+Tf/v15NP5588nd4uTf/z+X//x3/d/uP/4z9//+M+//c/9519Pfrm82dz/L/3w05e//nb+8fLD+dXJ4uTienuy'
    'WJo/f/5ls/l0sjjd/cfnzeb9/Z+3v2zOb08Wryd//rC5uv44+vOnm+v3Xy5uxz+4+7/FQS8uL/785dPo/fv+/Hqy3Xy+fWjo'
    '/sNTn0c/27dv3H3vHU+NOHzLx+ub218eHjp8su95+il9z1Mz1Wf/9OXy6v1v9/+8/fJ1QsiDJ9/UW391frHZDxIdoqdvfp2F'
    'g+ff/8fH2/3MOu/503hRsNccfvFgrs9vNzfe8y/OgwF6/AIel10Pdi8dPffpS2xcJpsMPW5oemFq7QuGx4Flr0+ofe7+af6A'
    'yBNpH//5+svTgIPxCCfQH+dh4dnhqMzfqHX+ODTN3/7UsuPQMn/KgDTMnzQulXnc/RYMx2MHao8b1tv0T7Xn2eHtshpY95tW'
    'w+4hm/OOi0AZjc5r4PFD4nHIzgmvg3ClXVxfXW0ubn/70+bm9vLq8t8fmmnvk9TtX7i2UDPIA3a3XKqh4K1hQ4PRSTZ7t3d7'
    'TlBl89cPjB8/+fGTF/STwzPx8+bqq+s22imPHhn2AI2PdnaX8p/2Vkh88vjmv/WzFrWjzPhDh0MDO7y8S541k3603A7DpVhp'
    'KDj/YduVFvp3CW5j/HMzTOEhv7MPOg8TGHw8SpUGTu391CIYeU2FV9sBLjRhGGDTAnl8wbQ5Axw2kHmWhaPUDFHhGfsRsr9V'
    'Rwg8FA9Q+bb4V/lt9ao7uPMOUczl5M+fb2/Otz9tbm7+erJYFy/DyYful2Kv6/F5LsrWK3Pnno5mqrUnkiu2AEBl+UrV7w3b'
    'OHus4RFpdqum12/TPQH8PnoR9+iAgT2zIwQmEWGdsS+pWEjD8ig9b2iYi393MjM900MzQqy9MMEEmy5be3C4AFSxkRPQreXq'
    '+/GQPg9pswuaPF5yJk7DpT/u/l7uclvjkx5hsc3Gfy66aI4j/XX1nt/8pXCBgcEk10QZdEiYOOChIJBWcZKnLrbUnKcDXlvO'
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
