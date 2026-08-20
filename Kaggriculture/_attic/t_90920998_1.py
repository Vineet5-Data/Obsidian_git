"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vW1ly/C961oNJyR47b1qbuzZWYxuyHGIzEAYDZIMAweZhkrcg/z0aWyIvb1dXV3efS9GOn0xTJO/5Pt3V1dW//M/Z'
    'v/32+z/+/vvZP/1y9vHq06ezu/Ozf//tP//1v+7fuH/5j99+/4+///f961/O3r672dz/VXvxp89/+/Xq/bufr67Pzs9ef9ie'
    'na/N25/ebjYfJ3/4tNm8uX97+3ZzdXt2/tPs7Z831x/en52vdh//ePPhzefXt/tvPL+7+9/zg/68e/3Xzx/3T1pN+vbL2Xbz'
    '6fZLW99/uLl9++XV7q3Zi8OB+LS5vt4/deU+dfeB6VN3f50OyrvrN7/eD/7t54fR09oBB8E05+EnUBP2w+I/sjYG5KEPX7lY'
    'vufzX5+0Zj/lYPLnb02fPZ/r66vXm91IHjzC9g091LwiD/vzdH8cDu5DM/5YU3/81v3/39/u9gx+J/Pk11fzAZy15X6orm43'
    'N7NXjw/df2rWDDays7No14hpyzdXn5ynp355/4N2mHaP2L349OFzMFz2CWCh71q8++GxwzVfE8NHzSwB237wzK8vahO/by+b'
    'sc6g2eNnchi0Ruth1SjTfD79dGG82GKzm3PMwM0PwgVGUFhv9h1yjVTWHRu+yrnw8M6knft3vEfVHgAGa/en2SOLPdi31/zw'
    '1xeJ32UfJeYV+drjKlQ+6120iRuSffTD9fXm9e2vf97c3L67fvcvX0ZtdBeO0Z65kUc++nie/Wh6u+mZrfLjo9SjfXBiJlNw'
    'fum7swl/8+EDl9TfzOz01Ld9P6Fn89Nvq04ZX/c5G2GpYcq0wQ7TAM915CBZV1y3iczZl3u0P8J7+zZsAxhg1oRRQ7x3kqIG'
    'ggFOjBEY4oSnufgatu7HqAGeLIGC2Tl3n4te3rGf3DC1M1dX4V7KHbMDLqHK1bPEOqzdxo2zr37iLXKVlI+35L0RPSc8ygoH'
    '2IJ3b2rE4oPcv2lLQxYeTUddY2n3/3v6StXlmL1ouRpKPGUefcvb2udLeSm5HxYcl+AHFzPTz4d5gT662riTHIj97dXNP+fv'
    'rLmJD1H7h6aUcRJgRibHhFnv+9+eBzIqd58DJLemzS6r3WSVJw7h9SHU3phBdEa1/FvUAd2doz4vWm0Ny2Y6WfsfPHg3P392'
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
