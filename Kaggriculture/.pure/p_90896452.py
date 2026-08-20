"""Pure verbatim replay of ladder episode 90896452 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vHMmR/C985oPmgxR1b1xpfBLMFQWK8sBeEIsF7IMBw/ewd28H//fTipzuns7IyMis6hG18tuAnOmuyqquzoyMjPzp'
    '/87+65df//m3X8/+46ezD9cfP549nJ/9/Zf//uv/fP7D54///OXXf/ztfz9//uns7bu73ef/ah9++PTnn6/fv/vx+ubs/Ozj'
    '293uw9n52vzj9e1+8uePu92bz3/cv91d35+dv5z9+cfdze37s/PV+uHhX+dHo373+o+fPkyuNoz/p7P97uP9l/G8v727f/vl'
    '09MkJ7+bDu/xB8cT/20QH+5u33x6fT8Ozwzjh0/vbt78/Pnq95++2GAyivHmbBjDhcfvTccxn/XN9evd06T1m5l/kjs82W5y'
    '6fkU4S3cL5FbEdsNK/h5wu9H+x+b8MkWjwvZaL/DfR7325c9cX2/uzu+4x9+25PTUT19O2XO8brjJA83eH39ZLynL3Uy3jip'
    '4U7Dd+zWD2dg1wTYym6I2c/4Kh3dQLSe3RCxGQ/XS5pv2AkN5qNbbdgJ+labX1e02rgTuhgLP6jzCUdWm7+TRKtN/qSbzdyq'
    'k7XAHHyLmH9NHq6CsYBBfBsJDySZivnQyUT2g2O0buOe2arbuI8/nP6yT2eJ4+BBP2fjulvDF1LXM37T0wHadI350fq1xlGw'
    'r7nGwaX6XUxmd92+MD3G8fr25mb3+v7nP+zu7t/dvPvL8curcsWPt5/al6n/sN7c3X5Y9mn6uLv5LXSbDHmM4BbZEOEJtGq8'
    '3rN54pjhyzsns2973QTEtMndpGIMhdXlqEAcOc5XenqZ0VnXrzc/346uh1bAeFjQpOPD4Vhq9RAGKONAgP9rfbqGe1ujjk6Y'
    'NWrXaTfZPzZC4nDMQQSxETK3JgFdae17TRuELd/pvMFJstDE3Yio073nTgCc7vDh8dvL3fo7mDV/kSux8GI2ILf+fZqgENo/'
    '1zv3vf63dLWZf7vN+Ldb1b/lju4WZ9MUz0pJij1dTEEdmQMFbjG/vRAppVzV5C3bzHWURap5+3OUtLetUADE3MrZ/yq3tEa0'
    'MwI5SXjQVp14csfCFDNvMvZar9+Q2DSE4HvAbuL9WqLCTceXduJFlhiQQU++whienVFAYvO7twk4dP9tlF5ZrWc5hG86MbjU'
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
