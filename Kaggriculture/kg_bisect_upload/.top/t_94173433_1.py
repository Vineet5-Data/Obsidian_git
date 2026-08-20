import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vXEly/C8886BudpOibxypd0dYzlCgJBPrATEYYNcwYKwPY98M/3drxP54/SoyMiKrmqIWurWarffquzIjIyN/+d+z'
    'f//t93/8/fezf/nl7IdP727f/vr+5sPHT/ebs8fzs//47b/+9t+f//L54z9++/0///4/nz//cvbjuy9/1T788Omvv978/O6n'
    'm9uz87M3dw9n58vm6w8/bjbvJ3/4sNm8/fz1w4+bm49n51ezr3/a3N79fHa+2P/8/f3d209vPh7+x+Xj4/+dTzv2/t2bv3x6'
    'f3jTYtK3X84eNh8+fmnrz3f3H3/88mn/1ezD8UB82NzeHt56MX/r7nGTV4GGTF97+DSfCtSA2evC2YM93Lfky5wsjvq6/RV5'
    '1/vbmzebaDxRf3b/Abxt1m7y1u1/mY5n044v3/18WAxHfd3OVPCzdIQ3N/P3H5bHzcfN/XwRzb87Xj1w6S7ni+jD3af5ImoX'
    '55/+2BlH38x6x6ayHZzjAZ6N0qF/b262S3P3o6edOem6NZeH4WpfuhuF6a/S6QL7D00O2AnNCiZv2Y49GLPJcDQz1v5Gn7Ht'
    'uNOhO3rufOcdhrCdpmBdLoTDDWyG8GjlZ8tRF7SRRYdOPnm7lupjKX+TzyMYwu0JA+Yomzd9EPfv2H/4fPZ+QB+8gTuMe8+D'
    't7+kkz72+XTCh3Rg938nbxr63PTDV3js7Fa5CKzJ5DA1LpAxT52frc72ffYWzO0R8tPGjBjTgjd3t7ebNx9//dPm/uO723f/'
    'dnwmDBq88kuMJVJ+x4nmYHdrT9oT7qG9IzL7cXCVrx8NC/BFr39jfud9XNW929T+67RJgHnXmI8TIxws3IqfAYwRuCdwr7ZL'
    '2zKTeR+mvc36mA4gcOwNg5S5KvBT9kA2FuhT+kDmEYj2Y4c/Gje56EDFgyrZvsoGor55Pv/E0+lzfRXgKX0c9JYN5wEY94dH'
    'tsZgvvlb4ITYlnn7rMelpirBzZ7ZsP7+tPFPk+99YEOtVJC7bhjEtkJ7OB/D6IsZLP751Lu/Q0iNdByyq1Y6JCv2w/6tkwPL'
    'vzvFtvd0zhpChKx33Qn0fu0yNuhFWxkWbseEUKTjNGXtN8wmankQk6Fgj9FFf0D9UmyUoFfJYOSQoXPwzqGsfx7g6vtjvz/2'
    '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'
    'Gp7GrRXWw/6doaOgfCBNBQb7H2Tqx/8HcJrSRQ=='
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
