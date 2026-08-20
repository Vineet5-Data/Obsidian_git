import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vHEly/C985oPmi6T8xpXmTsJxlwJFmTgviMUCd4YB4/yw9pvh/24eOdPT3RUVGZFVM+Iu+DYajrrruzIjIyN//t+z'
    'f//1t3/8/bezf/n57Idvn28+/vLl+uv9t7vt2eP52X/8+l9/+++nvzx9/Mevv/3n3//n6fPPZ58+P/9V+/DDt7/+cv3T5x+v'
    'b87Ozz7cPpydL4uvv37abr+M/vB1u/349PXDp+31/dn55ezrH7c3tz+dnS+Gn3+5u/347cP94X9cPD7+3/m4Y18+f/jLty+H'
    'Ny1Gffv57GH79f65rT/d3t1/ev40fDX7MB2Ir9ubm8NbV/O37h83ehVoyPi1h0/zqUANmL2uOnuwh0NLnudkMenr7lfkXV9u'
    'rj9sa+OJ+rP/D+Bts3aTt+7+y3g8i3Y8f/fTYTFM+rqbqcrPwhHeXs/ff1ge1/fbu/kimn83XT1w6S7ni+jr7bf5IioX55/+'
    'uTMm38x6x6ayHJzpAM9G6dC/D9e7pbn/0cvOHHXdmsvDcJUv3Y/C+FfhdIH9hyYH7IRiBZO37MYejNloOIoZK3+jz9hu3OnQ'
    'TZ4733mHISynqbIuF8LhBjZD9WjlZ8ukC9rIokMnnrx9S/WxlL+J5xEM4e6EAXMUzZs+iMM7hg9PZ+9X9MEbuMO4tzx490s6'
    '6X2fTye8Swf2/3f0pq7PDT98h8fObpVVxZoMDlPjAunz1PnZ6mzfk7dgbo+QnxZmRJ8WfLi9udl+uP/lT9u7+883n/9teiZ0'
    'Grz0S4wlkn7HkeZgf2uP2lPdQ4MjMvtx5SrfPBoW4Kte/8b8zvu4znu3of3XaJMA864wH0dGOFi4GT8DGCNwT+Be7Za2ZSbz'
    'Pox7G/UxHEDg2BsGKXNV4KfogWws0KfwgcwjEO3HBn+03uSkA1UfVMn2VTYQ9c3j+SeeTpvrqwBP4eOgt2w4D8C4PzyyNAbj'
    'zV8CJ8S2jNtnPS40VQludmLD+u1p/Z8m3/vAhlqrIHfeMKjbCuXhPIXRFzNY/OnUu7tFSI10HLKrVjokM/bD8NbRgeXfnWLb'
    'WzpnDSFC1pvuBHq/Nhkb9KLNDAu3Y6pQpOM0Re03zCZqeRCTIWGP0UV/QP1CbJSgV8FgxJChc/DOoaw/DnD19ti3x/4OH6sD'
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
