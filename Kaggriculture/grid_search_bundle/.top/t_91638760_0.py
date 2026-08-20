"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vXMlu/C96ngfPjOy186a158bG1VqGJGdwszAWC+QGAYKbh03egvz32LLm67BYLJJ9JNnrp9XKozN9utndZLFY/PV/'
    'z/799z/+8fc/zv7p17MPFzc3Z58WZ//x+3/9239//sXnH//x+x//+ff/+fzzr2dv311vPv8r/eHnj3/77eL9u18uLs8WZ6+v'
    'tmeLpfn1zdvN5sPZ4nz3DzebzZvPv96+3Vzcni2eT379y+by6v3Rrz9cX735+Pr2+A8+/d/i5C3evf7rxw9H379/n1/Ptpub'
    '27uB7n+4f+ejP9uP7/j1ve+4H8Tpt7y/ur59e/fQw0/2e+7/lH7P/TDVZ//88d3lm98+/+/txy8LQh48+aQ++suL15v9JNEp'
    'uv/kl1U4ef7nf3h/u19Z53v+cmwU7GtOP3iy1he3m2vv+a8vggn6+gE8L7s32H3p0XPvP8TmZbLJ0OMOQy8srf2Cw+OA2esL'
    'ap+7f5o/IfJC2sffXH28n3AwH+EC+vN8MDw7HZX1OxqdPw+t9dufWnYeOuunTEhj/aR5qazj7m/BdHx9gdrjDvY2/VXteXZ6'
    'h1gDe/2WNewesrkYaATKbAy2ga8/JB6H/JzwOggt7fXV5eXm9e1vf9lc3767fPevd8O090nq9i9cW2gY5AG7Wy41UPCt4UCD'
    '2UkOe7d3Ry5QZfPXD4wff/LjT57Qn5yeiTebyy+h29FO+RqR4QjQxGgvPqXip70XEp88vvtv46xF7Sgz8dDp1MAXXn5KnjWT'
    '9+jcDodLsTJQcP7DsSsj9O8SPMb4z800hYf8zj8YPE1g8vEsVQY49fdTRnAUNRW+2k5wYQiHCTYjkOcXLJszweEAWWRZOErN'
    'FBWesZ8h+7fqDIGH4gkq3xZ/lr+tXnUnd94pirmc/Prm9vpi+/Pm+vpvZ4t18TKc/DD8Uhx1PT7ORdm9Mnfh6dFKdd9ECsUW'
    'AKgsX6n6vWEHZ481PCPtsGp6/bbuCRD30Yt4xAsY2DM7Q2AREdYZx5KKh3Qwj9LzDgNz8e9BbqbnemhOiPUXJphg67K1B4cL'
    'QBUHOQHdOlffj4eMeUjPL2hFvORMnKZLf9z9o8Ll3uCTEWFxzCZ+LoZoTiD9xXovrv+lcIGBySTXRBl0SLg44KEgkVYJkqch'
    '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'
    'SVnrbvrp/wE8tCjq'
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
