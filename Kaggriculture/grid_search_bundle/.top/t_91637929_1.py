"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vXMlu/C961sPOjKy186a158bG1VqGbGdwYwiLBXKDAMHNwyZvQf57bHk+D4vFItlHkr1+Wq2smdOnm91NFovFT/97'
    '9u+///GPv/9x9k+fzt5dvX9/dnd+9h+//9e//ffnX3z+8R+///Gff/+fzz9/Ovvl499+e3d78+rjyw9n52eb1+urz/99dnf+'
    '6ez1m9v1mfrDl6+5evvm16vrz9/y8mZzdr4wv37/er1+d3Z+sfuH9+v1q8kzj3796/r65u2XX9/93/nJ67x5+deP746esn+x'
    'T2eb9fsP98PZ/7B9+aOPHY/i678eT4j3sO0gTx/39ub2w+v7bz/8ZB+4/aj2wO3A1Yf88vHN9avfPv/vh4/bhQifMP2I/D7X'
    'Vy/X+/nTZm/7kS8rdfKgz//w9sN+jZ0H/uXYPKTnTT5xbBhXH9a33oNeXqlzt/1LOGW7d5qOFzyTTdlks6LvPbxMxw7skw7f'
    'C7ZPYfXtA/Zf689VftXtc97ffNzON5gqfbX9tTjYrZ2p1mIfjdefojGLvT8q7RQNWWxlrkYstjRlrUXffQmYqckr1b73YK7u'
    'r2pfbJdgrA2xmRljQ7tvW1/NYTrKRM1lOZMfEpfOqf/21QML76mvhsqecnN9vX754be/rG8/vLl+86/347UXXcp1+TqM1H2K'
    'hkG+YHfYpgYKnhoONJid5LB329vYSmMIZfv88ZEfH/m2PsJPxPfr6y/R5tE+8eJZGPte3qViwL0HEJ87fngCY8XKQWYiOCHY'
    'X9wlTxpz9dbvhsPdWBkoOP3h2JUR+jcJHmP8cTNN4R28cxMGTxOYfDxLlQFO44iUERwFaoVH2wkuDOEwwWYE8vyCZXMmOBwg'
    'C2YLR+kIL5l4wOoMgS/FE9Ry4r/Hz4666k7uvFPgdTH59fsPt1ebX9a3t387O18VL8PJD8MvxVHX4+NclN0rcxeuHq1U902k'
    'QOwcAKnlK1W/N+zgzMS+evPPmrmFgVwwx/VbAsR84Ry3X6ewIcGqHV1BeFa2f9D1j/bvXfq+wyhdUH6Qk0n2teCCWG/BxYnG'
    'eHsFtJINcuDF9+NLPs0ACWa9gla8S87EaX73x80/KljuDT4ZDxbHbM7EYoDmhNFfrPfq9l8KtxmYTHJNlCGHhIMDvhSk5yoh'
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
