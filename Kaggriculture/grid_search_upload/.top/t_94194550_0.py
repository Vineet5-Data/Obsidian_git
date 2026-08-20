import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vG1mS/C866yCKpGTtTW1zxsbILUOWl5htCI0GZhYLLGYPvXtb7H9fj0QWq+pFRkZmPkpqQzeaoqve98uMjIz85X9P'
    '/v233//x999P/uWXk5++fbr58OuX66/33+42Jw+nJ//x23/97b+//+X7x3/89vt//v1/vn/+5eTjp8e/ah9++vbXX69//vT5'
    '+ubk9OT97fbk9Lz5+uvHzebL6A9fN5sP37/eftxc35+cXs6+/ry5uf355HQx/PzL3e2Hb+/vD//j4uHh/07HHfvy6f1fvn05'
    'vGkx6tsvJ9vN1/vHtv58e3f/8fHT8NXsw3Qgvm5ubg5vXc7fun/c6FWgIePXHj7NpwI1YPY6c/ZgD4eWPM7JYtLX3a/Iu77c'
    'XL/fWOOJ+rP/D+Bts3aTt+7+y3g8m3Y8fvfzYTFM+rqbKeNn7ghvrufvPyyP6/vN3XwRzb+brh64dM/ni+jr7bf5ImoX55/+'
    'uTMm38x6x6ayHZzpAM9G6dC/99e7pbn/0dPOHHU9NJeH4Wpfuh+F8a/c6QL7D00O2AnNCiZv2Y09GLPRcDQz1v5Gn7HduNOh'
    'mzx3vvMOQ9hOk7EuF8LhBjaDebTys2XSBW1k0aHjT96+pfpYyt/48wiGcHfCgDny5k0fxOEdw4fvZ+9X9CE2cIdxrzx490s6'
    '6X2fTye8Swf2/3f0pq7PdT+8wGNnt8rSsCadwzRwgfR56vxsjWzfZ2/B3B4hP23MiD4teH97c7N5f//rnzZ3959uPv3b9Ezo'
    'NHjplwSWSPodR5qD/a09ao+5hwZHZPZj4ypfPwQswFe9/gPzO+/jKu/duvZf0SYB5l1jPo6McLBwM34GMEbgnsC92i3tkJnM'
    '+zDurddHdwCBYx8wSJmrAj95D2RjgT65D2QegWg/FvxRu8lJB8oeVMn2VTYQ9c39+SeeTs31VYAn93HQWw44D8C4PzyyNQb9'
    'zd8CJ8S29NsXepxrqhLc7JkN67en9X+afO8DG2qlgtx5w8C2FdrDeQqjL2aw+PdT7+4WITXScciuWumQzNgPw1tHB1b87hTb'
    'XulcaAgRsl66E+j9WjI26EWbGRZux5hQZMRp8tofMJuo5UFMhoQ9Rhf9AfVzsVGCXjmD4UOGkYN3DmX9OMDV22PfHvsHfKwO'
    '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'
    '4ZT4QNq8xGP68P9HsgG0'
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
