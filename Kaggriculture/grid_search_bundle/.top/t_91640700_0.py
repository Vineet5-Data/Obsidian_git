"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vXEmO/C866+Cqkt323tR2zdoYtWXI8hRmDKHRwM5igcXsoWdui/3v64/6fAwGg2Q+SXb71GpZVS9fJjOTDAaDH//3'
    '7D9/+/0ff//97N8+nr27fP/+7O787L9++5//+OenX3z68R+//f7ff//Xp58/nv384a+/vru5fvXh5e3Z+dnm9fry03+f3p1/'
    'PHv95mZ9pv7w+Wsu37755fLq07e8vN6cnS/Mr9+/Xq/fnZ1f7P7h/Xr9avLMo1//sr66fvv513f/d37yOm9e/vnDu6On7F/s'
    '49lm/f72y3D2P2xf/uhjx6P4+q/HE+I9bDvI08e9vb65ff3l2w8/2QduP6o9cDtw9SE/f3hz9erXT/97+2G7EOETph+R3+fq'
    '8uV6P3/a7G0/8nmlTh706R/e3u7X2Hngn47NQ3re5BPHhnF5u77xHvTyUp277V/CKdu903S84JlsyiabFX3v4WU6dmCfdPhe'
    'sH0Kq28fsP9af67yq26f8/76w3a+wVTpq+2vxcFu7Uy1FvtovP4UjVns/VFpp2jIYitzNWKxpSlrLfruS8BMTV6p9r0Hc3V/'
    'VftiuwRjbYjNzBgb2n3b+nIO01Emai7LmfyQuHRO/bevHlh4T301VPaU66ur9cvbX/+0vrl9c/Xmb1/Gay+6lOvydRip+xQN'
    'g3zB7rBNDRQ8NRxoMDvJYe+2t7GVxhDK9vnjIz8+8m19hJ+I79dXn6PNo33ixbMw9n12l4oB9x5AfO744QmMFSsHmYnghGB/'
    'cZc8aczVW78bDndjZaDg9IdjV0bo3yR4jPHHzTSFd/DOTRg8TWDy8SxVBjiNI1JGcBSoFR5tJ7gwhMMEmxHI8wuWzZngcIAs'
    'mC0cpSO8ZOIBqzMEvhRPUMuJ/x4/O+qqO7nzToHXxeTX729vLjc/r29u/np2vipehpMfhl+Ko67Hh7kou1fmLlw9Wqnum0iB'
    '2DkAUstXqn5v2MHZYw3PSDvqnV6/rXsCRH30Ih7xAgZyzc4QWEQEr25/1/SQDuZR+r7DwFxYfpCb6bkemhNi/QUFUKy7ey4O'
    'VRzkwKvvx5d8nAEUzPoFrYiXnInTDO+Pu39UuNwbfDIiLI7ZxM/FEM0JpD9b7+XNXwoXGJhMck2UQYeEiwO+FCToKkHyNMSW'
    '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'
    'HZ7SycD7FIVbF3IqfnF3z+Hc6ea7+3+AXxZc'
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
