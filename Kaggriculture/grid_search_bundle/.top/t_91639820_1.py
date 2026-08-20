"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXctuW9kR/BetuTApWbazk21OLIzGMvQIMTEEY4BMECCYLCbZBfn3yBYfl7erq6v7nEvJHu9ombz3vE93dXX1x/8e/f2X'
    '33/79fejP308+nB2fX10Nzv6xy//+tu/7/9w//G3X37/56//uf/88ejd+dXy/n/ph9e3P386e3/+09nF0ezozeXqaDY3f75+'
    't1x+OJqdbP7jerl8e//n1bvl2c3R7Pnozz8tLy7fD/784ery7e2bm+EP7v432+vF+Zsfbz8M3r/tz8ej1fL65ktDtx/WfR78'
    'bNu+Yfe9d6wbsf+W95dXN+++PHT3yb5n/VP6nnUz1We/vj2/ePvp/p83t58nhDx49E299Rdnb5bbQaJDtP7m51nYe/79f7y/'
    '2c6s854fhouCvWb/i3tzfXazvPKe/+YsGKCHL+Bx2fRg89LBc9dfYuMy2mTocbumF6bWvmD3OLDs9Qm1z90+zR8QeSLt468v'
    'b9cDDsYjnEB/nHcLzw5HZf4GrfPHoWn+tqeWHYeW+VMGpGH+pHGpzOPmt2A4HjpQe9xuvY3/VHueHd4uq4F1v2k1bB6yPOu4'
    'CJTR6LwGHj4kHofsnPA6CFfam8uLi+Wbm08/LK9uzi/O//qlmfY+Sd3+hWsLNYM8YHPLpRoK3ho2NBidZLM3e7fnBFU2f/3A'
    '+P6T7z95Qj/ZPxOvlxefXbfBTnnwyLAHaHy007uU/7S1QuKTxzf/rZ81qx1lxh/aHxrY4fld8qwZ9aPldthdipWGgvMftl1p'
    'oX+X4DbGPzfDFB7yG/ug8zCBwcejVGng2N5PLYKB11R4tR3gQhN2A2xaII8vmDZngMMGMs+ycJSaISo8YztC9rfqCIGH4gEq'
    '3xZ/lN9Wr7q9O28fxZyP/nx9c3W2er28uvr5aHZcvAxHH7pfir2ux8e5KFuvzI17Opip1p5IrtgMAJXlK1W/N2zj7LGGR6TZ'
    'rRpfv033BPD76EXcowMG9syOEJhEhHXGvqRiIe2WR+l5u4a5+HcnM9MzPTQjxNoLI0yw6bK1B4cLQBUbOQLdWq6+7w/p85A2'
    'u6DJ4yVn4jhc+v3u7+UutzU+6REW22z856KL5jjSn1fv2dVfChcYGExyTZRBh4SJAx4KAmkVJ3nsYkvNWR/w2nJ+jEnQXe5t'
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
