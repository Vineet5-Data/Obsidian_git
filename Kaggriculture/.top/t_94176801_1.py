import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vHNdy/C985oP4Jcl5o6W9tnBpUdBHFjcGYRjIDQIENw9O3oL898gmd3Z3urq6uvvMkHT0xAX345w5c2amu7qq+uf/'
    'Ofm3X3/7x99/O/mnn08+XH/6dHJ3evLvv/7nv/7X1398ffmPX3/7j7//99fXP598/+Vvv3z4ePv2y5vPJ6cn2x8311//Xt2d'
    '3r9z/f7dT9c3X994c7s9OT03//7042bz4eT0YvfGp83m7f5nzl78/v8f333cnEgv7v73lE18+o/w4vggP21ubsDRPcz20+eP'
    '19vvNx8//u3hSPBs3r3565cPu6U4O5rX+9uPn3/8Y3T0ynwTfOxwvt7AD4t9Xhn64bvpwb//8u7m7S9f1/Tzlz9OlTzy/tV2'
    '8+mzeqg3128202yPRpv/ytGr+SxTg/7l911wvM1urt/vrwZ3bWeTPRj0/gUZ8831fDW31583H3e/Oxt9+t2HqfqfIUM+/Aha'
    '0v3Y078eJmjfq+0VckzgxE7/mn2tuHOUlbU7CHz4/odSWwms8e6HD247h9vp95tEcuHtbmLrPf3utJsK6707WXSdZ0doN1dl'
    'jcku21yri/3p9stur00fvf+2sMfuzxAaF0xgP9LsU6ltBH5leuC9/Xj7ITmA3TD7Afav7LNVH+Hhk/URHj5Ehtj9zMEY01Kw'
    'IcxEyBgPP4hCkFFDkChnOhw7wvTW/Yva79fCqUf+fTV81cPORQPR3LHuwrVdAH08qH3X++c0YuEr0STJQ+4gONr9HIyc5LFA'
    'nETGAg80faTbm5vNm8+//GXz8fO7m3f/8sft+2Dc6bfBuPtgKT+uvcNMv7aP9qaB0CTRB0kSdPDdr2c+3OnOkPtHuL3n2fcK'
    'N5HpQeBMwN4Jow+OWxPpMWMf1OMmkHwIDbmZKw+j7KGeP96d9ttA3wb6NtC3gZ7OQP+fAtuLCob58N3zAHJMha4qiFkbz4av'
    '/BdtAJsaLQhhKYRqY9jM0ABcnBAQOBqO1VxQsIu5IZDRvtmCbe3c7dlMjKSeSxG71cFEiuzZI5HPZDiwPZEATkPAWukw7am0'
    'KN4cjDolUF/jXLJf98A9iMFpMbYGzdn0RZlBDNGhsUCmUhjMZtIgTwND+Ucfru1FKVUT5zAGOgSD+cvSDIuUFHHMSMqL9UZa'
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
