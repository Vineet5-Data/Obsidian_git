import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vI9mR/C866zAUSUm9N003vd2wZtRQq03YA2EwgL0wYHgPs3tb+L9vWyKLVZWRkZH5HinNQDc2xa563y8zMjLyp/87'
    '+69ffv3n3349+4+fzr7/+un2w8+fb748fL3fnD2en/39l//+6/98+8u3j//85dd//O1/v33+6ezjp6e/ah++//rnn29+/PTD'
    'ze3Z+dn7u+3Z+YX5+svHzebz6A9fNpsP377eftzcPJydX82+/mFze/fj2fli+Pnn+7sPX98/HP7H5ePjv87HHfv86f0fv34+'
    'vGkx6ttPZ9vNl4entv54d//w8enT8NXsw3Qgvmxubw9vXc7fun/c6FWgIePXHj7NpwI1YPY6d/ZgD4eWPM3JYtLX3a/Iuz7f'
    '3rzfeOOJ+rP/D+Bts3aTt+7+y3g8TTuevvvxsBgmfd3NlPOzcIQ3N/P3H5bHzcPmfr6I5t9NVw9cuhfzRfTl7ut8EdnF+Yd/'
    '74zJN7Pesam0gzMd4NkoHfr3/ma3NPc/et6Zo66n5vIwXPal+1EY/yqcLrD/0OSAnWBWMHnLbuzBmI2Gw8yY/Y0+Y7txp0M3'
    'ee585x2G0E6Tsy4XwuEGNoN7tPKzZdIFbWTRoRNP3r6l+ljK38TzCIZwd8KAOYrmTR/E4R3Dh29n7xf0ITdwh3FvefDul3TS'
    '+z6fTniXDuz/7+hNXZ8bfniBx85ulaVjTQaHaeIC6fPU+dma2b4nb8HcHiE/NWZEnxa8v7u93bx/+PkPm/uHT7ef/jI9EzoN'
    'XvkliSVSfseR5mB/a4/a4+6hwRGZ/di5ytePCQvwVa//xPzO+7iqe7eh/ddokwDzzpiPIyMcLNyKnwGMEbgncK92SztlJvM+'
    'jHsb9TEcQODYJwxS5qrAT9ED2VigT+EDmUcg2o8N/qjf5KID5Q+qZPsqG4j65vH8E0+nzfVVgKfwcdBbTjgPwLg/PNIag/Hm'
    't8AJsS3j9qUeF5qqBDc7sWH99rT+T5PvfWBDrVSQu24Y+LaCPZynMPpiBot/O/Xu7xBSIx2H7KqVDsmK/TC8dXRg5e9Ose0t'
    'nUsNIULWm+4Eer82GRv0oq0MC7djXCgy4zRF7U+YTdTyICZDwR6ji/6A+oXYKEGvgsGIIcPMwTuHsn4/wNXbY98e+xt8rA5g'
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
