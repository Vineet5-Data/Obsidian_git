import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vW1ly/C961oNJUaKcN43N3TFWMzIkO8JmIAwG2F0ECDYPk7wF+e9xJJG8vKe6uqrPoewx9EZT9L3n+3RXV1f/8j8n'
    '//jt93/+/feTf/nl5IfPH67f//rx6u7T59vNycPpyb//9p9/+68vf/ny8Z+//f4ff//vL59/Ofnxw+NftQ8/fP7rr1c/f/jp'
    '6vrk9OTdzf3J6bL5+u7Hzebj5A93m837L1/f/7i5+nRyup59/dPm+ubnk9PF7ucfb2/ef373af8/Lh4e/vd02rGPH9795fPH'
    '/ZsWk779cnK/ufv02Nafb24//fj4affV7MPhQNxtrq/3bz2bv3X7uMmrQEOmr91/mk8FasDsdeHswR7uWvI4J4uDvj7/irzr'
    '4/XVu000nqg/2/8A3jZrN3nr83+ZjmfTjsfvft4vhoO+Ps9U8LN0hDdX8/fvl8fVp83tfBHNvztcPXDpLueL6O7m83wRtYvz'
    'T/+/Mw6+mfWOTWU7OIcDPBulff/eXT0vze2PnnbmpOvWXO6Hq33pdhSmv0qnC+w/NDlgJzQrmLzleezBmE2Go5mx9jf6jD2P'
    'Ox26g+fOd95+CNtpCtblQjjcwGYIj1Z+thx0QRtZdOjkk7dtqT6W8jf5PIIhfD5hwBxl86YP4u4duw9fzt479MEbuP249zz4'
    '+Zd00sc+n074kA5s/+/kTUOfm374Co+d3SpngTWZHKbGBTLmqfOz1dm+L96CuT1CftqYEWNa8O7m+nrz7tOvf9rcfvpw/eHf'
    'Ds+EQYNXfomxRMrvONIcbG/tSXvCPbRzRGY/Dq7y8wfDAvym178xv/M+rurebWr/ddokwLxrzMeJEQ4WbsXPAMYI3BO4V89L'
    '2zKTeR+mvc36mA4gcOwNg5S5KvBT9kA2FuhT+kDmEYj2Y4c/Gje56EDFgyrZvsoGor55Pv/E0+lzfRXgKX0c9JYN5wEY9/tH'
    'tsZgvvlb4ITYlnn7rMelpirBzV7YsH592vinyfc+sKFWGMBedBkFCEgWTQ12sfVdcQzNCW7n1DooXIOZIdAJ1UkXwxADAeGM'
    '4aVRvBsZuL4/rvtGBbzMeTQ1FsBbovlPbwTNhiiZJ2R4uNWWP5oC1ABOswBAgnPRERlyQMNVOvTkn2Np3w9y9vrY18eamFRs'
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
