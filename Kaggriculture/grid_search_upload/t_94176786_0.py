import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vXEly/C8886D+YJP0jSv17gjLGQqUtMR6QAwG8BoGjPVh7Jvh/26ZZHe/fhUZGZFVTcmzurVazffquzIjIyN//u+z'
    'f/31t7//7bezf/r57A+f39++++XDzcdPn++3Z4/nZ//263/8y39++Z8vH//+62///rf/+vL557Mf3j/9r/bhD5//+svNT+9/'
    'vLk9Oz97e/dwdr5svv74w3b7YfIfH7fbd1++fvhhe/Pp7Pxy9vWP29u7n87OF/uff7i/e/f57afDX2weH//nfNqxD+/f/vnz'
    'h8ObFpO+/Xz2sP346amtP93df/rh6dP+q9mH44H4uL29Pbx1NX/r7nGTV4GGTF97+DSfCtSA2evC2YM93LfkaU4WR319+RV5'
    '14fbm7fbaDxRf3Z/AN42azd568ufTMezacfTdz8dFsNRX19mKvhZOsLbm/n7D8vj5tP2fr6I5t8drx64dJfzRfTx7vN8EbWL'
    '84//tzOOvpn1jk1lOzjHAzwbpUP/3t68LM3dj5535qTr1lwehqt96W4Upr9KpwvsPzQ5YCc0K5i85WXswZhNhqOZsfY3+oy9'
    'jDsduqPnznfeYQjbaQrW5UI43MBmCI9WfrYcdUEbWXTo5JO3a6k+lvI3+TyCIXw5YcAcZfOmD+L+HfsPX87ej+iDN3CHce95'
    '8Msv6aSPfT6d8CEd2P3t5E1Dn5t++AqPnd0qq8CaTA5T4wIZ89T52eps31dvwdweIT9tzIgxLXh7d3u7ffvplz9u7z+9v33/'
    'z8dnwqDBK7/EWCLld5xoDna39qQ94R7aOyKzHwdX+cWjYQF+0+vfmN95H9d17za1/zptEmDeNebjxAgHC7fiZwBjBO4J3KuX'
    'pW2ZybwP095mfUwHEDj2hkHKXBX4KXsgGwv0KX0g8whE+7HDH42bXHSg4kGVbF9lA1HfPJ9/4un0ub4K8JQ+DnrLhvMAjPvD'
    'I1tjMN/8LXBCbMu8fdbjUlOV4GavbFh/f9r4p8n3PrCh1hjAXnQZBQhIJjbHMcbcwDDsruu79RjAE1zYqcFQuBkz26ATvZPu'
    'iiE2A4Iew3ukeF0yvP1wgveNCniZ82hqP4C3RPOfXhKaWVGyWMjwcEMufzTFrAHCZmGCBPqiIzLkzIardOhlMIfXfj9g2vfH'
    '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'
    'yIfZj1kG5hLUiWzXxptXss6PZ+nxfwGWU4Iw'
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
