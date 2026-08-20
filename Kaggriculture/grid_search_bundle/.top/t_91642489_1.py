"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vXEly/C8890HdTWkk3zhU70pYjiiQlBvrATEYYNcwYKwPY98M/3frg/31MjIyMrMeKWl1Gg7VfF2vKqsqMzIy8tf/'
    'Pfv33//4x9//OPuXX8/eX9zent0vzv7j9//6239//MXHH//x+x//+ff/+fjzr2dv3t5sPv4r/eHnD3/97eLd218urs4WZ5fX'
    '27PF0vz69s1m8/5scb77h9vN5vXHX2/fbC7uzhbPJ7/+ZXN1/e7o1+9vrl9/uLw7/oP7/1ucvMXby798eH/0/fv3+fVsu7m9'
    '+zzQ/Q8P73z0Z/vxHb++9x0Pgzj9lnfXN3dvPj/08JP9noc/pd/zMEz12T9/eHv1+reP/3v34dOCkAdPPqmP/uricrOfJDpF'
    'D5/8tAonz//4D+/u9ivrfM+fjo2Cfc3pB0/W+uJuc+M9//IimKAvH8DzsnuD3ZcePffhQ2xeJpsMPe4w9MLS2i84PA6Yvb6g'
    '9rn7p/kTIi+kffzt9YeHCQfzES6gP88Hw7PTUVm/o9H589Bav/2pZeehs37KhDTWT5qXyjru/hZMx5cXqD3uYG/TX9WeZ6d3'
    'iDWw129Zw+4hm4uBRqDMxmAb+PJD4nHIzwmvg9DSLq+vrjaXd7/9aXNz9/bq7b99Hqa9T1K3f+HaQsMgD9jdcqmBgm8NBxrM'
    'TnLYu707coEqm79+YPz4kx9/8hX9yemZeLu5+hS6He2ULxEZjgBNjPbiPhU/7b2Q+OTx3X8bZy1qR5mJh06nBr7w8j551kze'
    'o3M7HC7FykDB+Q/HrozQv0vwGOM/N9MUHvI7/2DwNIHJx7NUGeDU308ZwVHUVPhqO8GFIRwm2IxAnl+wbM4EhwNkkWXhKDVT'
    'VHjGfobs36ozBB6KJ6h8W/yz/G31qju5805RzOXk17d3Nxfbnzc3N389W6yLl+Hkh+GX4qjr8Wkuyu6VuQtPj1aq+yZSKLYA'
    'QGX5StXvDTs4e6zhGWmHVdPrt3VPgLiPXsQjXsDAntkZAouIsM44llQ8pIN5lJ53GJiLfw9yMz3XQ3NCrL8wwQRbl609OFwA'
    'qjjICejWufp+PGTMQ3p+QSviJWfiNF364+4fFS73Bp+MCItjNvFzMURzAulP1ntx86+FCwxMJrkmyqBDwsUBDwWJtEqQPA2x'
    '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'
    'QYGuktAZ25wzir3u/x9eyCHE'
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
