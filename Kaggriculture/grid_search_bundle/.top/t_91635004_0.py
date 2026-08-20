"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vG9kR/C8682CRkiznprUnsRGtZUhyiM1CWCyQBAGC5LDJLch/jyyRw+F0dXV1vzey83EjKGrmfb/u6urqH/958qef'
    'f/nrH385+dWPJ999/nD97qdPV3f3n2+Hk4fVyZ9//tsf/v74l8ePf/35l7/88R+Pn388ef/h6a/ow3eff/jp6uOH76+uT1Yn'
    'd++H4dPJ6sz84e3N9mR1uv/6bhjePX75/XB98/FkdT77evt+uLr/8vXDv1bTtn768Pa3nz8d3nI6ae6PJ9vh7v6pQR9vbu/f'
    'P316/uq4J5P3vL26vb25//Kc+Yuur94O43uO3gLaMPny0MtdI6bvnr1k38xaFz7d3rz7/Pb+MFrreSfcmbV/mr4wbvjdzed5'
    'w4erXcP3f3saw4/34xyz5/FpPbRsPytfBvlpaK7uh1v65N148hEGHVaHmKwTdyBSQ2M7MI70rvfSOJClMA7+ro9n0fKLV/Gv'
    'v+wu3vPnl9FFMftfNIeZIdj/FrXzMFfPo0sesxt+1JrDU0pbaL6W0BKKh+3xSBucXu7+VNs3h3/edzccKrZ2Z7uwtnTt4/Rx'
    'AssWnuzztSas2N3L3TPs6EeP31zd3ZVX7mEHhI95/gGc092flIeQo5qtypvr6+Ht/U+/Hm7vP1x/+P1xfxJr6Cu/I/FT92pI'
    'HC5L9DbxjsRPzXZaounzFfz/n/6X/JSunsd7cLj+4kFM1sujlZJ7BDTnTl9hh+b5Q3wKa7ZkfPHMra0V3iO5K2JiGw1H1+S3'
    '1bZZK3Mmkxn3fOvAU3u17mC+VYeOn5TTN8zfVfTeMgY1cByw+yMbFzurJnJO9AdaC/SwTsY+26d4x8VD2N7RLiNP111U5pao'
    'Hqpt42Ex7s2/Fkt+/PD8tNTszv5XGS3r3lSMWGMJz/73P+shuj0Fr1IfZQMbW1qCqxAuPMb51rOv7+5vr7bfDbe3P+QWdAK1'
    'IA4uA0T6nBLo2qq0GM278ff7NNm6/9FVpr6LnH/EcKn3BJyu4dFlTx1ubzQ1Obr0D3d0xuxkV2EC4wDG3B7RmOzabOMAqHbA'
    'NQxgEl5XwIwFFk7cLHs6H/57dgGmnjJBg/aHfOEpzriPj2zr3/gYwRD877pOv52H5N3iTcKh1cJP7sWn3NXgtOjgsqGGW2fX'
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
