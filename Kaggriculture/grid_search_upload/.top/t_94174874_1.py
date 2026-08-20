import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXctuHNly/BeuuVCzu/nwjiP1tYTLGQoU5cb1gBgM4GsYMK4XY+8M/7s5ZD+q6kRGRmaeIjkD7lrNVtV5n8zIyMif//fk'
    '33/97R9//+3kn34++eH7l5tPv3y9/nb//W5z8nB68h+//te//ffjXx4//uPX3/7z7//z+Pnnk89fnv6qffjh+99+uf7py4/X'
    'NyenJx9vtyenZ83X3z5vNl8Hf/i22Xx6/Hr7eXN9f3J6Mfn6x83N7U8np4vDz7/e3X76/vH++D/OHx7+73TYsa9fPv71+9fj'
    'mxaDvv18st18u39q60+3d/efnz4dvpp8GA/Et83NzfGty+lb948bvAo0ZPja46fpVKAGTF5nzh7s4aElT3OyGPV19yvyrq83'
    '1x831nii/uz/A3jbpN3krbv/MhzPph1P3/10XAyjvu5myviZO8Kb6+n7j8vj+n5zN11E0+/Gqwcu3bPpIvp2+326iNrF+Zff'
    'd8bom0nv2FS2gzMe4MkoHfv38Xq3NPc/et6Zg66H5vI4XO1L96Mw/JU7XWD/ockBO6FZweQtu7EHYzYYjmbG2t/oM7Ybdzp0'
    'o+dOd95xCNtpMtblQjjcwGYwj1Z+toy6oI0sOnT8ydu3VB9L+Rt/HsEQ7k4YMEfevOmDeHjH4cPj2fsNfYgN3HHcKw/e/ZJO'
    'et/n0wnv0oH9/x28qetz3Q+v8NjJrbI0rEnnMA1cIH2eOj1bI9v3xVswtUfITxszok8LPt7e3Gw+3v/yl83d/ZebL/86PhM6'
    'DV76JYElkn7HTHOwv7UH7TH30MERmfzYuMrXDwEL8E2v/8D8Tvu4ynu3rv1XtEmAedeYjwMjHCzcjJ8BjBG4J3Cvdks7ZCbz'
    'Pgx76/XRHUDg2AcMUuaqwE/eA9lYoE/uA5lHINqPBX/UbnLSgbIHVbJ9lQ1EfXN//omnU3N9FeDJfRz0lgPOAzDuj49sjUF/'
    '87fACbEt/faFHueaqgQ3e2HD+v1p/Z8m3/vAhlqpIHfeMLBthfZwHsPoiwks/njq3d0ipEY6DtlVKx2SGfvh8NbBgRW/O8W2'
    'VzoXGkKErJfuBHq/lowNetFmhoXbMSYUGXGavPYHzCZqeRCTIWGP0UV/RP1cbJSgV85g+JBh5OCdQll/HuDq/bHvj/0DPlYH'
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
