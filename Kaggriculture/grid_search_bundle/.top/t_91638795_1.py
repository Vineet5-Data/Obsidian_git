"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXcFuW0mS/BedeTBJSbb3prY5Y2HUliHJS/QaQqOBmcUCg5lD794G8+8rS+Qj+TIyMjKrHqW2fWq1LPLVq8qqyoyMjPzy'
    'r5P//u33f/zt95P/+HLy6eL29uR+dvI/v/3zr//78IuHH//x2+9//9v/Pfz85eSnz7/8+unm+v3nd3cns5P1h9XFw3/P7mdf'
    'Tj5c3qxO1B++fs3Fx8ufL64evuXd9fpkNje/vv2wWn06mZ1u/+F2tXo/euber39eXV1//Prr+3/PDl7n8t1fPn/ae8rwYl9O'
    '1qvbu8fhDD9sXn7vY/ujePrX/QnxHrYZ5OHjPl7f3H14/PbdT/aBm49qD9wMXH3IT58vr97/+vC/d583CxE+YfwR+X2uLt6t'
    'hvnTZm/zka8rdfCgh3/4eDessfPAP+2bh/S80Sf2DePibnXjPejdhTp3m7+EU7Z9p/F4wTPZlI02K/re3cu02IF90u57wfYp'
    'rL59wPC1/lzlV90+5/b682a+wVTpq+2vxc5u7Uw1LfbeeP0p6rPYw1Fpp6jLYitz1WOxpSlrWvTtl4CZGr1S7Xt35ur+qvbF'
    'dgn62hCbmT42tP221cUUpqNM1FSWM/ohcekc+m9PHlh4Tz0ZKnvK9dXV6t3dr39a3dxdXl3+1+N47UWXcl2ehpG6T9EwyBds'
    'D9vUQMFTw4EGs5Mc9nZ7G1tpGELZPn985MdH/lgf4Sfi7erqa7S5t0+8eBbGvuf3qRhw8ADic8cPT2CsWDnITAQnBPvz++RJ'
    'Y67e+t2wuxsrAwWnPxy7MkL/JsFjjD9upim8g7duQudpApOPZ6kywHEckTKCvUCt8Gg7wYUh7CbYjECeX7BszgSHA2TBbOEo'
    '7eElEw9YnSHwpXiCmpz4b/Gzva66gzvvEHidj359e3dzsf5pdXPzy8lsWbwMRz90vxR7XY/Pc1G2XpnbcHVvpVrfRArEZgBI'
    'LV+p+r1hB2ePNTwjzVHv+PptuidA1Ecv4h4vYCDX7AyBRUTw6uZ3jR7SzjxK37cbmAvLd3IzPddDc0Ksv6AAinV3z8WhioPs'
    'ePX9+JIvE4CCWb+gKeIlZ+I4w/vj7u8VLrcNPhkRFsds4udiiOYE0l+t9+LmPwsXGJhMck2UQYeEiwO+FCToKkHyOMSWhrNJ'
    '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'
    'CqbPacExzcRMHbsdbr77/wfEsFR4'
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
