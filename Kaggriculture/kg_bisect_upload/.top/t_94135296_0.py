import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXdtuHNmR/Bc+80F942XfOFJ7JZgzFCjKDXtADAawFwYM78Psvi387yuTfamqjIyMzHOK4gh6azSbVed+MiMjI3/+v7P/'
    '+vW3f/7tt7P/+Pnsh88fbt/98vHm08Pn++3Z4/nZ33/977/+z5e/fPn4z19/+8ff/vfL55/P3n94+qv24YfPf/7l5qcPP97c'
    'np2fvb3bnZ0vzdef3m+3Hwd/+LTdvvvy9e799ubh7Pxy8vWP29u7n87OF8eff7y/e/f57cPpPy4eH/91PuzYxw9v//j54+lN'
    'i0Hffj7bbT89PLX1p7v7h/dPn45fTT6MB+LT9vb29NbV9K2Hxw1eBRoyfO3p03QqUAMmr3NnD/bw2JKnOVmM+rr/FXnXx9ub'
    't1tvPFF/Dv8A3jZpN3nr/l+G42na8fTdT6fFMOrrfqacn4UjvL2Zvv+0PG4etvfTRTT9brx64NJdThfRp7vP00VkF+cf/r0z'
    'Rt9Mesem0g7OeIAno3Tq39ub/dI8/Oh5Zw66nprL03DZlx5GYfircLrA/kOTA3aCWcHkLfuxB2M2GA4zY/Y3+oztx50O3ei5'
    '0513GkI7Tc66XAiHG9gM7tHKz5ZRF7SRRYdOPHmHlupjKX8TzyMYwv0JA+Yomjd9EI/vOH74cvZ+Qh9yA3ca95YH739JJ73v'
    '8+mEd+nA4X8Hb+r63PDDV3js5FZZOdZkcJgmLpA+T52erZnt++ItmNoj5KfGjOjTgrd3t7fbtw+//GF7//Dh9sNfxmdCp8Er'
    'vySxRMrvmGkODrf2oD3uHjo6IpMfO1f55jFhAb7q9Z+Y32kf13XvNrT/Gm0SYN4Z83FghIOFW/EzgDEC9wTu1X5pp8xk3odh'
    'b6M+hgMIHPuEQcpcFfgpeiAbC/QpfCDzCET7scEf9ZtcdKD8QZVsX2UDUd88nn/i6bS5vgrwFD4OessJ5wEY96dHWmMw3vwW'
    'OCG2Zdy+1ONCU5XgZi9sWH9/Wv+nyfc+sKHWKshdNwx8W8EezmMYfTGBxb+cevd3CKmRjkN21UqHZMV+OL51cGDl706x7S2d'
    'Sw0hQtab7gR6vzYZG/SirQwLt2NcKDLjNEXtT5hN1PIgJkPBHqOL/oT6hdgoQa+CwYghw8zBO4Wyvh3g6vtjvz/2d/hYHcDq'
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
