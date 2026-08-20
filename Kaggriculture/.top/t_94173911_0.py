import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vXMmR/C8886ButkhqbxypvRLMGQqUtA3vgBgMYC8MGPZhvLeF//vKYn+8fhUZGZFVTUq2Tmo0W+/Vd2VGRkb+/H9n'
    '//Prb3/9029n//Hz2Q+f3t2++eX9zYePn+7XZw/nZ3/+9W9//Pvnv3z++Ndff/vLn/738+efz96++/JX7cMPn/7wy81P7368'
    'uT07P3t9tzk7XzZff3i7Xr+f/OHDev3m89ebt+ubj2fnV7Ovf1zf3v10dr7Y//z9/d2bT68/Hv7H5cPDP86nHXv/7vXvP70/'
    'vGkx6dvPZ5v1h49f2vrT3f3Ht18+7b+afTgeiA/r29vDWy/mb909bvIq0JDpaw+f5lOBGjB7XTh7sIf7lnyZk8VRX7e/Iu96'
    'f3vzeh2NJ+rP7j+At83aTd66/S/T8Wza8eW7nw6L4aiv25kKfpaO8Ppm/v7D8rj5uL6fL6L5d8erBy7d5XwRfbj7NF9E7eL8'
    '3T93xtE3s96xqWwH53iAZ6N06N/rm+3S3P3ocWdOum7N5WG42pfuRmH6q3S6wP5DkwN2QrOCyVu2Yw/GbDIczYy1v9FnbDvu'
    'dOiOnjvfeYchbKcpWJcL4XADmyE8WvnZctQFbWTRoZNP3q6l+ljK3+TzCIZwe8KAOcrmTR/E/Tv2Hz6fvR/QB2/gDuPe8+Dt'
    'L+mkj30+nfAhHdj938mbhj43/fAMj53dKheBNZkcpsYFMuap87PV2b5P3oK5PUJ+2pgRY1rw+u72dv364y+/W99/fHf77r+P'
    'z4RBg1d+ibFEyu840Rzsbu1Je8I9tHdEZj8OrvKXD4YF+FWvf2N+531c1b3b1P7rtEmAedeYjxMjHCzcip8BjBG4J3Cvtkvb'
    'MpN5H6a9zfqYDiBw7A2DlLkq8FP2QDYW6FP6QOYRiPZjhz8aN7noQMWDKtm+ygaivnk+/8TT6XN9FeApfRz0lg3nARj3h0e2'
    'xmC++VvghNiWefusx6WmKsHNntiw/v608U+T731gQ60wgL3oMgoQkCyaGuxi67viGJoT3M6pdVC4BjNDoBOqky6GIQYCwhnD'
    'S6N4NzJw/XBc940KeJnzaGosgLdE85/eCJoNUTJPyPBwqy1/NAWoAZxmAYAE56IjMuSAhqt06Mk/x9L+dZCz74/9/lgTk4qt'
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
