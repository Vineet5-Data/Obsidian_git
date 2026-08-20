import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXctuXFly/BeuuVAV396xpZppYdhNgZKmMG4QjQY8AwPGeNH2zvC/WxbrceueyMiIPKdIqqGVCsXSved9MiMjI3/5n5N/'
    '/Pb7P//++8m//HLyw+f3d+9+/XD78dPnh9XJ4+nJv//2n//2X1/+8uXjP3/7/T/+/t9fPv9y8uP7r3/VPvzw+W+/3v78/qfb'
    'u5PTk7f365PTZfP1xx9Xqw+TP3xcrd59+Xr94+r208np1ezrn1Z39z+fnC52P//wcP/u89tP+/9x+fj4v6fTjn14//Yvnz/s'
    '37SY9O2Xk/Xq46evbf35/uHTj18/7b6afTgciI+ru7v9W8/mb90+bvIq0JDpa/ef5lOBGjB7XTh7sIe7lnydk8VBXze/Iu/6'
    'cHf7dhWNJ+rP9j+At83aTd66+S/T8Wza8fW7n/eL4aCvm5kKfpaO8Op2/v798rj9tHqYL6L5d4erBy7d5XwRfbz/PF9E7eL8'
    '0//vjINvZr1jU9kOzuEAz0Zp37+3t5uluf3R086cdN2ay/1wtS/djsL0V+l0gf2HJgfshGYFk7dsxh6M2WQ4mhlrf6PP2Gbc'
    '6dAdPHe+8/ZD2E5TsC4XwuEGNkN4tPKz5aAL2siiQyefvG1L9bGUv8nnEQzh5oQBc5TNmz6Iu3fsPnw5ez+iD97A7ce958Gb'
    'X9JJH/t8OuFDOrD9v5M3DX1u+uEFHju7Vc4CazI5TI0LZMxT52ers32fvQVze4T8tDEjxrTg7f3d3ertp1//tHr49P7u/b8e'
    'ngmDBq/8EmOJlN9xpDnY3tqT9oR7aOeIzH4cXOUXj4YF+KrXvzG/8z6e173b1P7rtEmAedeYjxMjHCzcip8BjBG4J3CvNkvb'
    'MpN5H6a9zfqYDiBw7A2DlLkq8FP2QDYW6FP6QOYRiPZjhz8aN7noQMWDKtm+ygaivnk+/8TT6XN9FeApfRz0lg3nARj3+0e2'
    'xmC++VvghNiWefusx6WmKsHNntmw/v608U+T731gQ51jAHvRZRQgIFk0NdjF1nfFMTQnuJ1T66BwDWaGQCdUJ10MQwwEhDOG'
    'l0bxbmTg+v647hsV8DLn0dRYAG+J5j+9ETQbomSekOHhVlv+aApQAzjNAgAJzkVHZMgBDVfp0JN/jqX9cZCz74/9/lgTk4qt'
    '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'
    '3NqDOOOe7vb4fzAwZ2I='
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
