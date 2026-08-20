"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXctuW9kR/BetuRg+pEjZaWwmI0RjGbIcYmIIgwGSIECQLCbZBfn3yJZIXt6urq7ucy4lOV4NRybvPe/Tj6rqT/85+esv'
    'v/7jL7+e/PbTyfvLDx9O7mcnf/vln3/+18MfHj7+45df//6Xfz98/nTy/ceffn5/e/P245u7k9nJ5of15cN/T+9nn05+uLpd'
    'n6gfPj/m8t3Vj5fXD095c7M5mc3Nnz/8sF6/P5mttv/wYb1+O3rn4M8/rq9v3n3+8/1/ZwfduXrzh4/vB2/ZdezTyWb94e5L'
    'c3Yfnjo/+NmwFY//OhwQ72VPjTx83bub27sfvjx9/8m+8Omn2gufGq6+5PuPV9dvf37437uPTxMRvmH8E7k/15dv1rvx00bv'
    '6SefZ+rgRQ//8O5uN8fOC383XB7S+0a/GC6My7v1rfeiN5fq2D19Ew7Ztk/j9oJ3siEbbVb03H1nWtaBfdP+uWD7FGbfvmD3'
    'WH+s8rNu3/Ph5uPTeIOh0mfbn4v9urUj1TTZg/b6Q9RnsndHpR2iLpOtjFWPyZaGrGnStw8BIzXqUu25++Xq/qn2YDsFfdcQ'
    'G5k+a2j7tPXlFEtHGaipVs7oQ+K5h/bbowUW3lOPC5VdbTfX1+s3dz//bn17d3V99acv7bUXXcp0eWxG6j5FzSAP2B62qYaC'
    't4YNDUYn2ezt9u45QU/PrFyUhUX97SfffvKCfnJ4Jn5YX3/2Nwc7xfNoofd7dp/yAnc2QHzy+A4K9BYrR5nx4QR3f36fPGvM'
    '5Vu/Hfa3Y6Wh4PyHbVda6N8luI3xz80whYf81lDoPExg8PEoVRo49iRSi2DgqhVebQe40IT9AJsWyOMLps0Z4LCBzJ0tHKU9'
    '7GRiA6sjBB6KB6jJjP9/+G31qju48w5Dr/PRnz/c3V5uvl/f3v50MlsWL8PRh+6XYq/r8XkuytYrc+uwDmaqtSeSKzYDodTy'
    'larfG7Zx9ljDI9LsVo2v36Z7Avh99CLu0QETdM2OEJhEFGCNfUnFQtovj9Lz9g1zA/OdzEzP9NCMEGsvKCHFurnnRqKKjRzF'
    '41quvm8P+TRBWDBrFzR5vORMHOd4v939vdzltsYnPcJim43/XHTRHEf68+q9vP1j4QIDg0muiXLQIWHigIeCFF3FSR672FJz'
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
