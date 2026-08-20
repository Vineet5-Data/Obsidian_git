"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vG1mS/C8682CSsmzvTW1zpoVRW4YsLzHbEBoNzCwWWMweeve22P++skSyipWRkZH5XlGyxzdaJqve98uMjIz89X/P'
    '/v33P/7x9z/O/uXXs0+Xnz+f3S/O/uP3//rbfz/84eHjP37/4z///j8Pn389+/nqdvPwv/TDT1/++tvlx6tfLq/PFmfvb7Zn'
    'i6X58+efN5tPZ4vz/X983mw+PPx5+/Pm8u5s8Xry51821zcfR3/+dHvz4cv7u/EP7v9vcdSLq/d/+fJp9P5Df349224+3z02'
    '9PBh1+fRzw7tG3ffe8euEcdv+Xhze/fz40OHT/Y9u5/S9+yaqT77py9X1x9+e/jn3ZevE0IePPmm3vrry/ebwyDRIdp98+ss'
    'HD3/4T8+3h1m1nnPn8aLgr3m+ItHc315t7n1nv/+Mhigpy/gcdn3YP/S0XN3X2LjMtlk6HFD0wtTa18wPA4se31C7XMPT/MH'
    'RJ5I+/jPN192Aw7GI5xAf5yHhWeHozJ/o9b549A0f4dTy45Dy/wpA9Iwf9K4VOZx/1swHE8dqD1uWG/TP9WeZ4e3y2pg3W9a'
    'DfuHbC47LgJlNDqvgacPicchOye8DsKV9v7m+nrz/u63P21u766ur/7tsZn2Pknd/oVrCzWDPGB/y6UaCt4aNjQYnWSz93u3'
    '5wRVNn/9wPjxkx8/eUE/OT4TP2+uv7puo53y5JFhD9D4aBf3Kf/pYIXEJ49v/ls/a1E7yow/dDw0sMPL++RZM+lHy+0wXIqV'
    'hoLzH7ZdaaF/l+A2xj83wxQe8nv7oPMwgcHHo1Rp4NTeTy2CkddUeLUd4EIThgE2LZDHF0ybM8BhA5lnWThKzRAVnnEYIftb'
    'dYTAQ/EAlW+Lf5bfVq+6ozvvGMVcTv78+e72cvvT5vb2r2eLdfEynHzofin2uh6f56JsvTL37uloplp7IrliCwBUlq9U/d6w'
    'jbPHGh6RZrdqev023RPA76MXcY8OGNgzO0JgEhHWGfuSioU0LI/S84aGufh3JzPTMz00I8TaCxNMsOmytQeHC0AVGzkB3Vqu'
    'vh8P6fOQNrugyeMlZ+I0XPrj7u/lLrc1PukRFtts/Oeii+Y40l9X7+XtvxYuMDCY5Joogw4JEwc8FATSKk7y1MWWmrM74LXl'
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
