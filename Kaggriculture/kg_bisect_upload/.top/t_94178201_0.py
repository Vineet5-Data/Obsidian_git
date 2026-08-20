import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vW1ly/C961oNJfZjKm8bmro3VjAzZDrEZCIMBdoMAweZhkrdg/3scSyQv76murupzSHl2/WSCou8936e7urr65/89'
    '+/dff/vbX387+5efz374/P7u7S8fbj9++vywPns8P/uPX//rL//95S9fPv7t19/+86//8+Xzz2fv3n/9q/bhh89//uX2p/c/'
    '3t6dnZ+9ud+cnS+brz++W68/TP7wcb1+++Xrzbv17aez89ezr39c393/dHa+2P38w8P9289vPu3/x/Xj49/Ppx378P7Nnz5/'
    '2L9pMenbz2eb9cdPX9v60/3Dp3dfP+2+mn04HIiP67u7/Vsv5m/dPm7yKtCQ6Wv3n+ZTgRowe104e7CHu5Z8nZPFQV+ff0Xe'
    '9eHu9s06Gk/Un+1/AG+btZu89fm/TMezacfX737aL4aDvj7PVPCzdITXt/P375fH7af1w3wRzb87XD1w6S7ni+jj/ef5ImoX'
    '5x/+f2ccfDPrHZvKdnAOB3g2Svv+vbl9XprbHz3tzEnXrbncD1f70u0oTH+VThfYf2hywE5oVjB5y/PYgzGbDEczY+1v9Bl7'
    'Hnc6dAfPne+8/RC20xSsy4VwuIHNEB6t/Gw56II2sujQySdv21J9LOVv8nkEQ/h8woA5yuZNH8TdO3Yfvpy9H9EHb+D2497z'
    '4Odf0kkf+3w64UM6sP2/kzcNfW764QUeO7tVLgJrMjlMjQtkzFPnZ6uzfU/egrk9Qn7amBFjWvDm/u5u/ebTL39YP3x6f/f+'
    '3w7PhEGDV36JsUTK7zjSHGxv7Ul7wj20c0RmPw6u8qtHwwL8pte/Mb/zPl7WvdvU/uu0SYB515iPEyMcLNyKnwGMEbgncK+e'
    'l7ZlJvM+THub9TEdQODYGwYpc1Xgp+yBbCzQp/SBzCMQ7ccOfzRuctGBigdVsn2VDUR983z+iafT5/oqwFP6OOgtG84DMO73'
    'j2yNwXzzt8AJsS3z9lmPS01Vgpud2LD+/rTxT5PvfWBDXWIAe9FlFCAgWTQ12MXWd8UxNCe4nVProHANZoZAJ1QnXQxDDASE'
    'M4aXRvFuZOD6/rjuGxXwMufR1FgAb4nmP70RNBuiZJ6Q4eFWW/5oClADOM0CAAnORUdkyAENV+nQk3+Opf3jIGffH/v9sSYm'
    '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'
    '7T7sfjz7JiN7aq09kMvf2tiPf3/8P3zKrrM='
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
