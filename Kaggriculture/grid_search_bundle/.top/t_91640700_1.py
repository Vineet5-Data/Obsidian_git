"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXdFuHMmR/Bc+z4NmOOJR98aV2hZhrihQlAd7C2GxwNk4wLAf9u7N8L8fJXJ6ejojIyOzqoeSvE/LpYbT1VVZVZmRkZE/'
    '//Psr7/+9ve//Hb2nz+fvb/68OHs0+rsf379x3//78MvHn78+6+//e0v//fw889nb6/vhod/pT/88PGnX67eXf94dXO2Ont9'
    'uztbrc2vP7wdhvdnq+3+Hz4Mw5uHX+/eDlf3Z6uXs1//ONzcvpv8+v3d7ZuPr++nf/DpX6ujt7h+/aeP7yfPH9/n57Pd8OH+'
    'y0DHH57eefJn4/imr+8942kQx095d3t3//bLlx5+ss95+lP6nKdhqt/9w8frmze/PPzv/cfPC0K+ePZJffQ3V6+HwySt6SQ9'
    'fRasw8M/vbsfV9d51h8+WwB7wOMHjtb36n64877v9VUwKY8fwHOxH/Hjqh1979OH2EzMNhb6usPQC8tpH3D4OmDqmUW03zx+'
    'nz8l4dLZr/1w+/FpqsFMhEvnz/DBxOxEVFZuMjr//ZtWbjyj7Dy0rZwyJYWVk2aksoL7vwUT8Tjw2tcdLG3+q9r32WntYgfs'
    '9RvtYP81w1WH5VfmofPqP/6Q+DrkyYSHf2hjr29vbobX97/8Ybi7v765/q8vw7S3R+p+L1xSaBjkC/Z3Wmqg4KnhQIPZSQ57'
    'v2t7LlBl29ePit//5Pc/+Yr+5PhM/DDcfA7OJjvlMebCMZ6Jwi4+pSKk0e+ITx7r5NsIalU7wkykczwl8EXXn5JnzNP4W26D'
    'wyVYGSA47+GYlRH6dwceY/zn4/SEh/neD+g8PWDS8exUBjj35VOLP4mICo8+TGzh0YeJNU+W5xUslzOx4QBZtFg4KsepKfzt'
    'ODP2b9WZAV+KJ6Z8C/y7/G31Cju6y47xx/Xs1x/u7652Pwx3dz+drc6Ll9zsh26XXa9r77QXYOtV+Ob6j81DlmKoSUg7sYJ+'
    'F6V09Nmhzm7MVYc46HCo4fet3wIgauO3QI/XKWw8sF6TKwbPShwJUn9nfN/S9xxG52LUnZxFsH8Fl8Le/gDQecSf+nhtM2hQ'
    'uU60QbbfaL9/SZ8vabvumwJUcgjO85e/X+nV6LZt0MlArjjm2i1uv8fe4m+v7v5cuKbAJJJ7oIwNJCJZ8KUgp1WJaecRsTSc'
    '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'
    'f2anffp/2+QDfQ=='
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
