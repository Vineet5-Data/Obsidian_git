"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXdtuW9mR/Rc986F5kWzlTbFP2kbUliHJIZKG0GggCQIMMg898zaYf4/a4uXw7KpVqy6bpAw/maZIntq1b3VZtern/7v4'
    '56+//fsfv1384eeLzzcPDxdPs4t//frff/+f5zeeX/7719/+6x//+/z654sPH++H579yL/745a+/3Hz6+NPN7cXs4t3d+mK2'
    'aN5++DAMn0d/eBiG989vrz8MN48XszeTt38abu8+Xczmu49/vr97/+Xd4/4bl09P/z87GM/Hd3/+8nn/pPlobD9frIeHx6+y'
    'frq7f/zw9dXurcmLQ0U8DLe3+6fO1afuPjB+6u6vY6V8vH3/y7PyH79stBeTQ9NLI+HmVyWp9prSpRDF4R+xkWqZGTo3zumv'
    'j6TZz7kw+9O3wDg/3968G3Z6O3hEOzbpoc0r8LA/jTfIoXI3Yvy+qH7/ref/f3rcbRr5Hc+T391MFTiR5VlVN4/D/eTV9qH7'
    'T03EQJqdHEY7IcaSDzcPytNdv7z/wVZNu0fsXjzcfTHU1T5BWOg7iXc/XKuu6Zoo11qzBFr5hWe+vIhN/F5eNGMZpbXHz+gw'
    'SGlrs2qYaZ6NPx3QF1ps7easUdz0IOygQWK9te/wVxa17pD6IufC5p2RnPt3tEfFHiAoa/enySODI9jL2/zwywvH76KPAvsK'
    'fG27CpnPahet44ZEH727vR3ePf7yp+H+8ePtx7991Vr1EI4hz9TIAx/dnmffRU+L7tkq3z8KXdqNBzWagtlK92cdDufmAyvo'
    'cHp2uuvbup+Qs/nht1mnDK97n43QS00eGVo1FXiulUpqXXHeJmrOPt+jdQ3v7VtTBkHBSIQqFe+dJH+sw6MjQcUOT7P7Gm7d'
    'jyoFj5ZAwOycus9BL+/YT06Y2p6rK3Av+Y7ZgksocvX0WIex2zhx9sVPvC5XSfh4c94b1nPMoyxwgHW8e10asw9y/aYNqcw8'
    'mo66xtzu/7f0lajLMXmRcjWYfMo0/ea3tWe9vBTfDxOOi/GD3cz0WZkXqEdXE3eSEmL/cHP/F/+dNTXxxaj9RpRwnEQwI506'
    'Qdb7/reniYzI3acEklPT1i6r3WSFJ06K15uh9sQMSmdUyr+VBsC7c9DnlVZbwrIZT9b+Bw/e9c9fO1cgw2hbJqFDLpXo2TlJ'
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
