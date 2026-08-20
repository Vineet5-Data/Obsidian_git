"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vW9cR/C965oNJyrLdN8VmGiGKZchyidQQggBNUaBIH9K+Ff3vlSXykrw7Ozu751xKSvwURibvPd9nd3Z29vN/T/7+'
    '82+//vLbyZ8+n3w4//jx5HZ28o+f//W3f9/94e7jrz//9s9f/nP3+fPJN59+/OnD9dW7T29vTmYn6+9W53f/fXk7+3zy3cX1'
    '6iT48OXX5+8vfji/vPvx26v1yWxu/vzxu9Xqw8nsdPsPH1erd6NX7f35h9Xl1fsvf7793+ygFxdvv//0Ye8tQ38+n6xXH2/u'
    'mzN82PR572dDK/a7771j07bDt7y/ur757v6hu0/2PZuf0vdsmqk++5tPF5fvfrr735tPX4adPHj0Tb31l+dvV8Mg0SHafPPL'
    'LBw8/+4f3t8M8+e859v9qWevOfziwVyf36yuvee/PQ8G6OELeFy2Pdi+dO+5my+xcRltMvS4XdMLU2tfsHscWPb6hNrnDk/z'
    'B0SeSPv4j1efNgMOxiOcQH+cdwvPDkdl/vZa549D0/wNp5Ydh5b5UwakYf6kcanM4/a3YDgeOlB73G69jf9Ue54d3i6rgXW/'
    'aTVsH7I677gIlNHovAYePiQed2jnPJgs4XUQrrS3V5eXq7c3P327ur65uLz4630z7X2Suv0L1xZqBnnA9pZLNRS8NWxoMDrJ'
    'Zm/3bs8Jqmz++oHx9Sdff/KEfnJ4Jn5cXX5x0PZ2ys4dMz7hGfAAU/7TYIXEJ49v/ls/a1Y7yow/JLjF89vkWTPqR8vtsLsU'
    'Kw0F5z9su9JC/y7BbYx/boYpPOS39kHnYQKDj0ep0sCxvZ9aBHteU+HVdoALTdgNsGmBPL5g2pwBDhvIPMvCUWqGqPCMYYTs'
    'b9URAg/FA1S+Lf4ov9WuugDbPMQq56M/f7y5Pl9/s7q+/vFktixehqMP3S/FXtfj41yUrVfm1j3dm6nWnkiu2AwAleUrVb83'
    'bOPssYZHpNmtGl+/TfcE8PvoRdyjAwb2zI4QmESEdca+pGIh7ZZH6Xm7hu0e9O7iz92MS8/gsKhhzpAZIYK9rT0Xfyq2coS5'
    'tdx8Xx/S5yFtZkGTw0uOxHFM9OvV38tbbmt80iEsttm4z0UPzfGjv6ze8+u/FO4vMJj68a1jDgkLBzwUxNEqPvLYw5aaszng'
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
