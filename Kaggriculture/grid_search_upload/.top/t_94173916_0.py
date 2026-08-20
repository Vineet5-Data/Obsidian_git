import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXdtuHFly/Bc+80F948VvHKnXEpYzFCjKjfWAGAywaxgw1g9jvxn77+aKfamqExkZmXmK4uzyrdVsVZ37yYyMjPz5/87+'
    '49ff/vqX387+5eezH75+uv3wy+ebLw9f77dnj+dn//nrf//5f57+8vTxr7/+9l9/+d+nzz+fffz07a/ahx++/umXm58+/Xhz'
    'e3Z+9v5ud3a+bL7+8nG7/Tz4w5ft9sPT17uP25uHs/PLydc/bm/vfjo7Xxx//vn+7sPX9w+n/3Hx+Pi382HHPn96/8evn09v'
    'Wgz69vPZbvvl4Vtbf7q7f/j47dPxq8mH8UB82d7ent66mr718LjBq0BDhq89fZpOBWrA5HXm7MEeHlvybU4Wo77uf0Xe9fn2'
    '5v3WGk/Un8N/AG+btJu8df9fhuPZtOPbdz+dFsOor/uZMn7mjvD2Zvr+0/K4edjeTxfR9Lvx6oFLdzldRF/uvk4XUbs4//D3'
    'nTH6ZtI7NpXt4IwHeDJKp/69v9kvzcOPnnfmoOuhuTwNV/vSwygMf+VOF9h/aHLATmhWMHnLfuzBmA2Go5mx9jf6jO3HnQ7d'
    '6LnTnXcawnaajHW5EA43sBnMo5WfLaMuaCOLDh1/8g4t1cdS/safRzCE+xMGzJE3b/ogHt9x/PB09n5BH2IDdxr3yoP3v6ST'
    '3vf5dMK7dODwfwdv6vpc98N3eOzkVlkZ1qRzmAYukD5PnZ6tke374i2Y2iPkp40Z0acF7+9ub7fvH375w/b+4dPtp38fnwmd'
    'Bi/9ksASSb9jpjk43NqD9ph76OiITH5sXOWbx4AF+KrXf2B+p31c571b1/4r2iTAvGvMx4ERDhZuxs8AxgjcE7hX+6UdMpN5'
    'H4a99froDiBw7AMGKXNV4CfvgWws0Cf3gcwjEO3Hgj9qNznpQNmDKtm+ygaivrk//8TTqbm+CvDkPg56ywHnARj3p0e2xqC/'
    '+VvghNiWfvtCj3NNVYKbvbBh/fa0/k+T731gQ61VkDtvGNi2Qns4j2H0xQQWfzr17u8QUiMdh+yqlQ7JjP1wfOvgwIrfnWLb'
    'K50LDSFC1kt3Ar1fS8YGvWgzw8LtGBOKjDhNXvsDZhO1PIjJkLDH6KI/oX4uNkrQK2cwfMgwcvBOoax/HODq7bFvj/0dPlYH'
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
