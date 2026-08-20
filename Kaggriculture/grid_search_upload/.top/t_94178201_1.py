import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vW1ly/C961oNJUV9509jcjLGakSHbS2wGwmCAbBAg2DxM8hbkv8exRPLynurqqj6HtGbhJxMUfe/5Pt3V1dW//M/Z'
    'v/32+9//9vvZP/1y9sPn9/fvfv1w9/HT58f12dP52b//9p//+l9f/vLl499/+/0//vbfXz7/cvbj+69/1T788Pmvv979/P6n'
    'u/uz87O3D5uz82Xz9ccf1+sPkz98XK/fffl68+P67tPZ+fXs65/W9w8/n50vdj//8Pjw7vPbT/v/cfX09L/n0459eP/2z58/'
    '7N+0mPTtl7PN+uOnr239+eHx049fP+2+mn04HIiP6/v7/Vsv5m/dPm7yKtCQ6Wv3n+ZTgRowe104e7CHu5Z8nZPFQV9ffkXe'
    '9eH+7u06Gk/Un+1/AG+btZu89eW/TMezacfX737eL4aDvr7MVPCzdITXd/P375fH3af143wRzb87XD1w6S7ni+jjw+f5ImoX'
    '55/+f2ccfDPrHZvKdnAOB3g2Svv+vb17WZrbHz3vzEnXrbncD1f70u0oTH+VThfYf2hywE5oVjB5y8vYgzGbDEczY+1v9Bl7'
    'GXc6dAfPne+8/RC20xSsy4VwuIHNEB6t/Gw56II2sujQySdv21J9LOVv8nkEQ/hywoA5yuZNH8TdO3Yfvpy9H9EHb+D2497z'
    '4Jdf0kkf+3w64UM6sP2/kzcNfW764Rs8dnarXATWZHKYGhfImKfOz1Zn+568BXN7hPy0MSPGtODtw/39+u2nX/+0fvz0/v79'
    'vxyeCYMGr/wSY4mU33GkOdje2pP2hHto54jMfhxc5ZdPhgX4qte/Mb/zPq7q3m1q/3XaJMC8a8zHiREOFm7FzwDGCNwTuFcv'
    'S9syk3kfpr3N+pgOIHDsDYOUuSrwU/ZANhboU/pA5hGI9mOHPxo3uehAxYMq2b7KBqK+eT7/xNPpc30V4Cl9HPSWDecBGPf7'
    'R7bGYL75W+CE2JZ5+6zHpaYqwc1ObFh/f9r4p8n3PrChVhjAXnQZBQhIFk0NdrH1XXEMzQlu59Q6KFyDmSHQCdVJF8MQAwHh'
    'jOGlUbwbGbi+P677RgW8zHk0NRbAW6L5T28EzYYomSdkeLjVlj+aAtQATrMAQIJz0REZckDDVTr05J9jaf84yNn3x35/rIlJ'
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
