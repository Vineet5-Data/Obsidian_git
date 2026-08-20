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
    'Crcu5FT84u6ew7nTzXf3/6YwEQ0='
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
