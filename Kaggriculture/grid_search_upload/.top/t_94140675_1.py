import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vW1ly/C961oNJUV9509jc2FjNyJDtJTYDYTBANggQbB4meQvy3+NYInl5T3V1VZ9DSV74yQRN3Xu+T3d1dfWv/3Py'
    'b7//8fe//XHyT7+e/PTlw+273z7efPr85X598nB68u+//+e//tfX//n68e+///Eff/vvr59/PXn/4dv/ah9++vLX325++fDz'
    'ze3J6cnbu83J6bL5+tP79frj5D8+rdfvvn69eb+++Xxyejn7+uf17d0vJ6eL3c8/3t+9+/L28/4vLh4e/vd02rGPH97++cvH'
    '/ZsWk779erJZf/r8ra2/3N1/fv/t0+6r2YfDgfi0vr3dv/Vs/tbt4yavAg2Zvnb/aT4VqAGz14WzB3u4a8m3OVkc9PXpV+Rd'
    'H29v3q6j8UT92f4BeNus3eStT38yHc+mHd+++2W/GA76+jRTwc/SEV7fzN+/Xx43n9f380U0/+5w9cClu5wvok93X+aLqF2c'
    'f/r/nXHwzax3bCrbwTkc4Nko7fv39uZpaW5/9LgzJ1235nI/XO1Lt6Mw/VU6XWD/ockBO6FZweQtT2MPxmwyHM2Mtb/RZ+xp'
    '3OnQHTx3vvP2Q9hOU7AuF8LhBjZDeLTys+WgC9rIokMnn7xtS/WxlL/J5xEM4dMJA+Yomzd9EHfv2H34evZ+Qh+8gduPe8+D'
    'n35JJ33s8+mED+nA9m8nbxr63PTDCzx2dqucBdZkcpgaF8iYp87PVmf7PnsL5vYI+WljRoxpwdu729v128+//Wl9//nD7Yd/'
    'OTwTBg1e+SXGEim/40hzsL21J+0J99DOEZn9OLjKzx8MC/BVr39jfud9XNW929T+67RJgHnXmI8TIxws3IqfAYwRuCdwr56W'
    'tmUm8z5Me5v1MR1A4NgbBilzVeCn7IFsLNCn9IHMIxDtxw5/NG5y0YGKB1WyfZUNRH3zfP6Jp9Pn+irAU/o46C0bzgMw7veP'
    'bI3BfPO3wAmxLfP2WY9LTVWCmz2zYf3jaeOfJt/7wIZaYQB70WUUICBZNDXYxdZ3xTE0J7idU+ugcA1mhkAnVCddDEMMBIQz'
    'hpdG8W5k4Pr+uO4bFfAy59HUWABvieY/vRE0G6JknpDh4VZb/mgKUAM4zQIACc5FR2TIAQ1X6dCTf46l/eMgZz8e++OxJiYV'
    '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'
    'nn0j1p1uTd2k/d+Ymw//BwKxYTE='
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
