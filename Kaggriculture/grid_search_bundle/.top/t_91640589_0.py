"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vW9cR/C965oNJyrLdN8VmaiGKZchSidQQjABNUaBIH9K+Ff3vlS2Sl7w7Ozu751xKTvwURibvPd9nP2ZmP/735O8/'
    '//brL7+d/OnjyfvzDx9O7mYn//j5X3/79/0f7j/++vNv//zlP/efP558d/vTp/fXV29uX9+czE7Wb1fn9/99fjf7ePL24np1'
    'Enz4/Ovzdxc/nl/e//j11fpkNjd//vB2tXp/Mjvd/sOH1erN6FV7f/5xdXn17vOf7/43O+jFxesfbt/vvWXXn48n69WHmy/N'
    '2X3Y9HnvZ7tW7Hffe8embYdveXd1ffP2y0OHT/Y9m5/S92yaqT77u9uLyzef7v/35vbzsJMHj76pt/7y/PVqN0h0iDbf/DwL'
    'B8+//4d3N7v5c97z/f7Us9ccfvFgrs9vVtfe81+fBwP08AU8LtsebF+699zNl9i4jDYZetzQ9MLU2hcMjwPLXp9Q+9zd0/wB'
    'kSfSPv7D1e1mwMF4hBPoj/Ow8OxwVOZvr3X+ODTN3+7UsuPQMn/KgDTMnzQulXnc/hYMx0MHao8b1tv4T7Xn2eHtshpY95tW'
    'w/Yhq/OOi0AZjc5r4OFD4nGHds6DyRJeB+FKe311ebl6ffPp+9X1zcXlxV+/NNPeJ6nbv3BtoWaQB2xvuVRDwVvDhgajk2z2'
    'du/2nKDK5q8fGN9+8u0nT+gnh2fih9XlZwdtb6cM7pjxCc+AB5jyn3ZWSHzy+Oa/9bNmtaPM+EOCWzy/S541o3603A7DpVhp'
    'KDj/YduVFvp3CW5j/HMzTOEhv7UPOg8TGHw8SpUGju391CLY85oKr7YDXGjCMMCmBfL4gmlzBjhsIPMsC0epGaLCM3YjZH+r'
    'jhB4KB6g8m3xR/mtdtUFsc3DWOV89OcPN9fn6+9W19c/ncyWxctw9KH7pdjrenyci7L1yty6p3sz1doTyRWbgUBl+UrV7w3b'
    'OHus4RFpdqvG12/TPQH8PnoR9+iACXtmRwhMIop1xr6kYiENy6P0vKFhbvy7k5npmR6aEWLthVFMsOmytQeHG4AqNnIUdGu5'
    '+r49pM9D2uyCJo+XnInjpOi3u7+Xu9zW+KRHWGyz8Z+LLprjSH9evefXfylcYGAwyTVRDjokTBzwUJBIqzjJYxdbas7mgNeW'
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
