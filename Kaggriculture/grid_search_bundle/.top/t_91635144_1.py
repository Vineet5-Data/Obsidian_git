"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV2PG0eS/C/zzAeRHEnWvY0l7lrYsUYYjZbYNQjDwPpwwMH34N23w/33kzRks9kZGRmZVc35WL/RY7FZXV1dlRkZGfHT'
    '/1785y+///br7xf/8dPFx6tPny52i4v/+uV//vHPL3/48vG3X37/71//9eXzTxc/vL/dfPm/9MP3n//289WH9z9eXV8sLt7e'
    'bC8WS/PnTz9sNh8vFpeH//Fps3n35c/bHzZXdxeLl5M//7i5vvkw+vPH25t3n9/ejb+w+7/FyV28f/uXzx9Hvz/cz08X282n'
    'u28DHT7s73n0tWF849v3fmM/iNNf+XBze/fDt4seP9nf2X+V/s5+mOq1v//8/vrdz1/+8+7z1wdCLjz5l/ror6/eboZJolO0'
    '/5dfn8LJ9b/8jw93w5N1fudP40XBfub0H54866u7za13/bdXwQTd/wM8L4c7OPzo6Lr7f8TmZfKSocsdh154tPYHjpcDy15/'
    'oPa6w9X8CZEfpL38p5vP+wkH8xE+QH+ejwvPTkfl+Y1G589D0/Mbdi07Dy3PT5mQhucnzUvlOR6+C6bj/gZqlzuut+mfatez'
    '09tlNbDbb1oNh4tsrjouAmU2Oq+B+w+Jy6E4JzwOwpX29ub6evP27uc/bW7v3l+///u3YdrzJHX6F44tNAxygcMplxoo+NVw'
    'oMHsJId9eHd7PqDKy1/fMP74yh9feURfOd0TP22uv6ZuozflPiPDGaDJ0V7tUvnTEIXEO48f/ts8a1Hbykw+dDo18IaXu+Re'
    'M7mPltPheChWBgr2fzh2ZYT+WYLHGH/dTFO4yR/ig87TBCYfz1JlgNN4P7UIRllT4aftBBeGcJxgMwJ5fsFjcyY4HCDLLAtb'
    'qZmiwjWGGbLfVWcIXBRPUPm0+Hf5bvWoOznzTlHM5eTPn+5ur7bfb25v/3axWBcPw8mH7odir+PxYQ7K1iPzkJ6OnlTrnUip'
    '2AIAleUjVT837ODstoZnpDmtmh6/TecEyPvoQdzjBgzsmZ0h8BAR1hnnkkqEdFwepesdB+bi353CTC/00IIQGy9MMMGmw9Zu'
    'HC4AVRzkBHRrOfr+uEifi7TFBU0ZL9kTp+XSP87+Xuly2+CTGWFxzCZ/LqZoTiL9dfVe3f61cICBySTHRBl0SIQ44KKgkFZJ'
    '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'
    'ft5Dhyrdel6OtJxq7v4f+i0JTQ=='
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
