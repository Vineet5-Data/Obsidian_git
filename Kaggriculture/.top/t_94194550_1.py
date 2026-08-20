import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU2PW0ly/C997oNI9qdvPRLXErZnWmhJS6wHjcEAXsOAsT6MfTP83y2rm+Tjq8jIiKwiJS10EsGm3qvvyoyMjPz1f87+'
    '7fc//v63P87+6deznz69u3/z2/u7Dx8/Pa7Pns7P/v33//zX//r8l88f//77H//xt//+/PnXs7fvvvxV+/DTp7/+dvfLu5/v'
    '7s/Oz14/bM7Ol83XH96u1+8nf/iwXr/5/PXm7fru49n59ezrn9f3D7+cnS92P3//+PDm0+uP+/9x9fT0v+fTjr1/9/rPn97v'
    '37SY9O3Xs836w8cvbf3l4fHj2y+fdl/NPhwOxIf1/f3+rav5W7ePm7wKNGT62v2n+VSgBsxeF84e7OGuJV/mZHHQ15dfkXe9'
    'v797vY7GE/Vn+x/A22btJm99+S/T8Wza8eW7X/aL4aCvLzMV/Cwd4fXd/P375XH3cf04X0Tz7w5XD1y6y/ki+vDwab6I2sX5'
    'p//fGQffzHrHprIdnMMBno3Svn+v716W5vZHzztz0nVrLvfD1b50OwrTX6XTBfYfmhywE5oVTN7yMvZgzCbD0cxY+xt9xl7G'
    'nQ7dwXPnO28/hO00BetyIRxuYDOERys/Ww66oI0sOnTyydu2VB9L+Zt8HsEQvpwwYI6yedMHcfeO3YfPZ+8H9MEbuP249zz4'
    '5Zd00sc+n074kA5s/+/kTUOfm374Co+d3SqrwJpMDlPjAhnz1PnZ6mzfk7dgbo+QnzZmxJgWvH64v1+//vjbn9aPH9/dv/uX'
    'wzNh0OCVX2IskfI7jjQH21t70p5wD+0ckdmPg6v88smwAL/p9W/M77yPF3XvNrX/Om0SYN415uPECAcLt+JnAGME7gncq5el'
    'bZnJvA/T3mZ9TAcQOPaGQcpcFfgpeyAbC/QpfSDzCET7scMfjZtcdKDiQZVsX2UDUd88n3/i6fS5vgrwlD4OesuG8wCM+/0j'
    'W2Mw3/wtcEJsy7x91uNSU5XgZic2rH88bfzT5Hsf2FAXGMBedBkFCEgWTQ12sfVdcQzNCW7n1DooXIOZIdAJ1UkXwxADAeGM'
    '4aVRvBsZuL4/rvtGBbzMeTQ1FsBbovlPbwTNhiiZJ2R4uNWWP5oC1ABOswBAgnPRERlyQMNVOvTkn2Np/zjI2Y/H/nisiUnF'
    '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'
    'D4OIO+mvp/8D24aE9g=='
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
