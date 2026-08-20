"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vG1mS/C8682CSsmzvTS1zuoWRLUOWh5htCI0GdgYDLGYPvXtb7H9fWRLJqsrIyMh8ryjZ4xstk1Xv+2VGRkb++r8n'
    'f//9j3/+7Y+Tf/v15NP5588nd4uTf/z+X//x3/d/uP/4z9//+M+//c/9519Pfrm82dz/L/3w05e//nb+8fLD+dXJ4uTienuy'
    'WJo/f/5ls/l0sjjd/cfnzeb9/Z+3v2zOb08Wryd//rC5uv44+POnm+v3Xy5uhz+4+7/FqBeXF3/+8mnw/n1/fj3Zbj7fPjR0'
    '/+Gpz4Of7ds37L73jqdGjN/y8frm9peHhx4+2fc8/ZS+56mZ6rN/+nJ59f63+3/efvk6IeTBk2/qrb86v9jsB4kO0dM3v87C'
    '6Pn3//Hxdj+zznv+NFwU7DXjL47m+vx2c+M9/+I8GKDHL+Bx2fVg99LBc5++xMZlssnQ4w5NL0ytfcHhcWDZ6xNqn7t/mj8g'
    '8kTax3++/vI04GA8wgn0x/mw8OxwVOZv0Dp/HJrmb39q2XFomT9lQBrmTxqXyjzufguG47EDtccd1tv0T7Xn2eHtshpY95tW'
    'w+4hm/OOi0AZjc5r4PFD4nHIzgmvg3ClXVxfXW0ubn/70+bm9vLq8t8fmmnvk9TtX7i2UDPIA3a3XKqh4K1hQ4PRSTZ7t3d7'
    'TlBl89cPjB8/+fGTF/ST8Zn4eXP11XUb7JRHjwx7gMZHO7tL+U97KyQ+eXzz3/pZi9pRZvyh8dDADi/vkmfNpB8tt8PhUqw0'
    'FJz/sO1KC/27BLcx/rkZpvCQ39kHnYcJDD4epUoDp/Z+ahEMvKbCq+0AF5pwGGDTAnl8wbQ5Axw2kHmWhaPUDFHhGfsRsr9V'
    'Rwg8FA9Q+bb4V/lt9aob3XljFHM5+fPn25vz7U+bm5u/nizWxctw8qH7pdjrenyei7L1yty5p4OZau2J5IotAFBZvlL1e8M2'
    'zh5reESa3arp9dt0TwC/j17EPTpgYM/sCIFJRFhn7EsqFtJheZSed2iYi393MjM900MzQqy9MMEEmy5be3C4AFSxkRPQreXq'
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
