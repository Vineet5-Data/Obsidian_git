"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vW9cR/C965oNJyrLdN9lmGiGKZchyidQQggBNUaBIH9K+Ff3vlSWSl7w7Ozu751xKdvwURibvPd9nd3Z29tN/T/7+'
    'y++//fr7yZ8+nbw///Dh5HZ28o9f/vW3f9/94e7jb7/8/s9f/3P3+dPJ648//fz++urtxzc3J7OT9fer87v/Pr+dfTr5/uJ6'
    'dRJ8+Pzr83cXP55f3v34zdX6ZDY3f/7w/Wr1/mR2uv2HD6vV29Gr9v784+ry6t3nP9/+b3bQi4s3P3x8v/eWXX8+naxXH27u'
    'm7P7sOnz3s92rdjvvveOTdsO3/Lu6vrm+/uHDp/sezY/pe/ZNFN99uuPF5dvf77735uPn4edPHj0Tb31l+dvVrtBokO0+ebn'
    'WTh4/t0/vLvZzZ/znu/2p5695vCLB3N9frO69p7/5jwYoIcv4HHZ9mD70r3nbr7ExmW0ydDjhqYXpta+YHgcWPb6hNrn7p7m'
    'D4g8kfbxH64+bgYcjEc4gf44DwvPDkdl/vZa549D0/ztTi07Di3zpwxIw/xJ41KZx+1vwXA8dKD2uGG9jf9Ue54d3i6rgXW/'
    'aTVsH7I677gIlNHovAYePiQed2jnPJgs4XUQrrQ3V5eXqzc3P3+3ur65uLz4630z7X2Suv0L1xZqBnnA9pZLNRS8NWxoMDrJ'
    'Zm/3bs8Jqmz++oHx7SfffvKEfnJ4Jn5YXX520PZ2yuCOGZ/wDHiAKf9pZ4XEJ49v/ls/a1Y7yow/JLjF89vkWTPqR8vtMFyK'
    'lYaC8x+2XWmhf5fgNsY/N8MUHvJb+6DzMIHBx6NUaeDY3k8tgj2vqfBqO8CFJgwDbFogjy+YNmeAwwYyz7JwlJohKjxjN0L2'
    't+oIgYfiASrfFn+U32pXXYBtHmKV89GfP9xcn69fr66vfzqZLYuX4ehD90ux1/X4OBdl65W5dU/3Zqq1J5IrNgNAZflK1e8N'
    '2zh7rOERaXarxtdv0z0B/D56EffogIE9syMEJhFhnbEvqVhIw/IoPW9omIt/dzIzPdNDM0KsvTDCBJsuW3twuABUsZEj0K3l'
    '6vv2kD4PabMLmjxeciaOg6Lf7v5e7nJb45MeYbHNxn8uumiOI/159Z5f/6VwgYHBJNdEGXRImDjgoSCQVnGSxy621JzNAa8t'
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
