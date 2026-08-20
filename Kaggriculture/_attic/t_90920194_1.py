"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vW9kN/S9eaxHJduJ05yZvJkY9cWA7FaaBMRigLQoU7WLaXdH/Xk8sS0+P5OEhee+TnM4qiizp3e9LHh4efvnPyV9/'
    '/uUff/nl5HdfTj5d3t2dPCxO/vbzP//8r8c3Hl/+4+df/v6Xfz++/nLy4ep2ePwr9+L3n3/86fLj1Q+X1yeLk3c365PFSrx9'
    '92EYPo3+cDcM7x/fXn8YLu9PFm8mb/8wXN98PFkstx//dHvz/vO7+903zh8e/rvY68/Vuz98/rR70nLUty8n6+Hu/mtbP97c'
    '3n/4+mr71uTF/kDcDdfXu6cuzaduPzB+6vav40G5un7/0+Pg33/ejB7XDnUQRHM2P6E1YTcs9iNzYwAeuvnKaf+eT3991Jrd'
    'lCuTP31r/OzpXF9fvhu2I7n3CNk37aHiFXjYd+P9sT+4m2b8uqZ+/a3H/3+83+4Z/Z3Ik99dTgdw0pbHobq8H24nr54fuvvU'
    'pBloZCdn0bYR45YPl3fG00O/vPtBOUzbR2xf3N18doZLPkFZ6NsWb3+47XBN10TzURNLQLZfeebTi9zE79qLZqwyaPL4GR0G'
    'pdHarBpmmhfjTyfGCy02uTnbDNz0IOwwgsR6k++AaySz7tDwZc6FzTujdu7esR6Ve4AyWNs/TR6Z7MGuveKHn14Efhd9FJhX'
    '4GvPq5D5rHXRBm5I9NGb6+vh3f1P3w2391fXV3/6OmqtuzBHe6ZGHvjo83n2W9PLTY9sld8+Cj3ajRMzmoLFme3OBvzNzQfO'
    'oL8Z2emhb9t+Qs3mh99mnTK87mM2Qq9hirRBDlMDz7XlIElXnLeJxNkXe7Q9wjv71m2DMsCoCa2GeOckeQ1UBjgwRsoQBzzN'
    '7mtYuh+tBni0BBJm59R9Tnp5cz+5YGpHrq7EvRQ7ZhtcQpmrp8c6zN3GhbMvf+J1uUrSx1vw3vCe4x5liQOs490bGjH/ILdv'
    '2tSQuUfTrGss7P5/S1/JuhyTFyVXg4mnTKNvcVt70ctLif0w4bg4P9jNTF808wJtdLVwJxkQ+4fL2z/G76ypia+i9pumpHES'
    'xYwMjgmy3ne/PQ1kZO4+A0guTZtcVtvJSk+chte7UHthBrUzquTfah3g3Tno82qrrWDZjCdr94N778bnT84ViDD6lknqkCsF'
    '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'
    'iIKUVq0hj6YMlEYnrUdatPuLb8ovefgflb8QMw=='
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
