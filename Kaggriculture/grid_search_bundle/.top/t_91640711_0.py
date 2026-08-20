"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vG1mS/C8682CSsmzvTW1zpoVRW4YsLzHbEBoNzCwWWMweeve22P++skSyipWRkZH5XlGyxzdaJqve98uPiMhf//fs'
    '33//4x9//+PsX349+3T5+fPZ/eLsP37/r7/998MfHj7+4/c//vPv//Pw+dezn69uNw//Sz/89OWvv11+vPrl8vpscfb+Znu2'
    'WJo/f/55s/l0tjjf/8fnzebDw5+3P28u784Wryd//mVzffNx9OdPtzcfvry/G//g/v8WR724ev+XL59G7z/059ez7ebz3WND'
    'Dx92fR797NC+cfe9d+wacfyWjze3dz8/PnT4ZN+z+yl9z66Z6rN/+nJ1/eG3h3/effk6IeTBk2/qrb++fL85DBIdot03v87C'
    '0fMf/uPj3WFmnff8abwo2GuOv3g015d3m1vv+e8vgwF6+gIel30P9i8dPXf3JTYuk02GHjc0vTC19gXD48Cy1yfUPvfwNH9A'
    '5Im0j/9882U34GA8wgn0x3lYeHY4KvM3ap0/Dk3zdzi17Di0zJ8yIA3zJ41LZR73vwXD8dSB2uOG9Tb9U+15dni7rAbW/abV'
    'sH/I5rLjIlBGo/MaePqQeByyc8LrIFxp72+urzfv73770+b27ur66t8em2nvk9TtX7i2UDPIA/a3XKqh4K1hQ4PRSTZ7v3d7'
    'TlBl89cPjB8/+fGTF/ST4zPx8+b6q+s22ilPHhn2AI2PdnGf8p8OVkh88vjmv/WzFrWjzPhDx0MDO7y8T541k3603A7DpVhp'
    'KDj/YduVFvp3CW5j/HMzTOEhv7cPOg8TGHw8SpUGTu391CIYeU2FV9sBLjRhGGDTAnl8wbQ5Axw2kHmWhaPUDFHhGYcRsr9V'
    'Rwg8FA9Q+bb4Z/lt9ao7uvOOo5jLyZ8/391ebn/a3N7+9WyxLl6Gkw/dL8Ve1+PzXJStV+bePR3NVGtPJFdsAQKV5StVvzds'
    '4+yxhkek2a2aXr9N9wTw++hF3KMDJuyZHSEwiSjWGfuSioU0LI/S84aGufHvTmamZ3poRoi1FyYxwabL1h4cbgCq2MhJ0K3l'
    '6vvxkD4PabMLmjxeciZO06U/7v5e7nJb45MeYbHNxn8uumiOI/119V7e/mvhAgODSa6JctAhYeKAh4JEWsVJnrrYUnN2B7y2'
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
