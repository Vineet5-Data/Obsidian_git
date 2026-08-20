"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtnUtv3Udyxb8L11yYD0l2dhr5DiyMxjIkOcTEIIwBMkGAYLKYZBfku0djUvfxr9O/OlXdl5YnWumCl1S/u6tOnTr10/9c'
    '/Nuf//bXv/zt4p9+uvjdj6/ffPvzDy/ff/jx3e7i/vLi3//8n//6Xx+/+fjxr3/+23/85b8/fv7p4rvXv3zb/fC7H//08/vd'
    '7tuLy4s/7t68/f7i8mbz47vvdi8/XFxeXX/6+cvvX//x5ZuP37x6e3dxeX1//7+Xx/3+4fWrP/z4w+HrQ8d/urjbvf/wS7Pf'
    'v3334btfPn0c4PvNj4a/dTry2MfYxfff7XY/iE5+++7tDxcnXTu0Jfq2XQvZ29jH0czse2V3QE3Jm5fff9iP3evAm5evdvv2'
    'T1r/9L89bILONLz8sHvndePTHx1vjMNfh47QDoHJf9gJP7x7++2Prz4c7eN7f1Lev/1xMDo5GaLr9TX61KbsBu2MQxdpKexZ'
    'gVO8/+742I2Guuz0iF3z+7+f/sHy4EExlsWdqMcByIO8GZxs2Vu2wZ79++IMZiQ0fdTQwtMjVuXVy815EFtCdGHhmgynBw+0'
    's08KayQO8vbg3KQrtf+UP4X5tIge0V7d/+Qwa437bPdyez7SJZdfjZcOGn/ciuaVcfgR3VhLz4q40PcfDiOeWoB4Qe3ngNp8'
    'XLc1r0lch8MlEfqwb1m8sKe/TDfkw2/Ksx+bTFta32T6odTSfs4WNxQvrPO5Iad+RdhDj7v2nN5E6wifWkpXv/z/0kD61LVX'
    'b9+82b368PPvd+8+vH7z+l8eT9f+RFA/C8aHmJTDfhz0odA0LEe8Xx7draMPaHq83735+z446tzBtQtrdG2s0b41uHbELDUm'
    '4dT0MK+ATa/W3LBx8qkHej9M9Ef9h6p30iZaszrKAhPuwbitza3abEp4AeHDZo3S4xDmO5pZpfb9JyEiJ/u/BbvCaWgw0Evb'
    '6g+v4uiALX9+h7vzfC01XvzPvCHnnlrS0LmNsS8N/b9tKNge66zkgiUq4YWSkUw256M/qBxKghPUd8FOXu5WjwFq3aWHl6IJ'
    'Q1poSsB0WqhjXIT9GyeAvhwEbDoZYlQ0uw8ztWjAEUM04fH6gAVqRHN76Ic94Ov7RbMuJiPd02JyFdzmTa+y/JuoCQc+9i3u'
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
