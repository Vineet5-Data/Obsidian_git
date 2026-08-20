import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXctuZFdy/Beuuegqvr2jumtGjaHEBps9hbFACAJmBgaM8UL2zvC/u4esx617IiMj8pwiJbt3hWLx3vM+mZGRkT/998nf'
    'f/n1H3/79eRffjr57svHuw8/f7r9/PjlYXXydHryb7/8x1//8+tfvn78xy+//vvf/uvr559Ovv/4/Fftw3df/vLz7Y8ff7i9'
    'Ozk9eX+/PjldNl9//n61+jT5w+fV6sPXr9ffr24fT06vZl//sLq7//HkdLH7+aeH+w9f3j/u/+Py6el/Tqcd+/Tx/Z++fNq/'
    'aTHp208n69Xnx+e2/nj/8Pj986fdV7MPhwPxeXV3t3/rcv7W7eMmrwINmb52/2k+FagBs9eFswd7uGvJ85wsDvq6+RV516e7'
    '2/eraDxRf7b/AN42azd56+ZfpuPZtOP5ux/3i+Ggr5uZCn6WjvDqdv7+/fK4fVw9zBfR/LvD1QOX7mK+iD7ff5kvonZx/uGf'
    'O+Pgm1nv2FS2g3M4wLNR2vfv/e1maW5/9LIzJ1235nI/XO1Lt6Mw/VU6XWD/ockBO6FZweQtm7EHYzYZjmbG2t/oM7YZdzp0'
    'B8+d77z9ELbTpK5LMLhgM4RHKz9bDrqgjSw6dPLJ27ZUH0v5m3wewRBuThgwR9m86YO4e8fuw9ez9zP64A3cftx7Hrz5JZ30'
    'sc+nEz6kA9v/nbxp6HPTD2/w2NmtchZYk8lhalwgY546P1ud7fvqLZjbI+SnjRkxpgXv7+/uVu8ff/7D6uHx493Hfz08EwYN'
    'XvklxhIpv+NIc7C9tSftCffQzhGZ/Ti4yi+eDAvwN73+jfmd9/G87t2m9l+nTQLMu8Z8nBjhYOEK9pzirMI9gXu1WdqWmcz7'
    'MO1t1sd0AIFjbxikzFWBn7IHsrFAn9IHMo9AtB/VdQL80bjJRQcqHlTJ9lU2EPXN8/knnk6f66sAT+njoLdsOA/AuN8/sjUG'
    '883fAifEtszbZz0uNVUJbvbKhvW3p41/mnzvAxvqHAPYiy6jAAHJoqnBLra+K46hOcHtnFoHhWswMwQ6oTrpYhhiICCcMbw0'
    'incjA9f3x3XfqICXOY+mxgJ4SzT/6Y2g2RAl84QMD7fa8kdTgBrAaRYASHAuOiJDDmi4Soee/HMs7f8Ocvbtsd8ea2JSsfVi'
    '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'
    '7duEgLB8l/cgPTj8w+XpfwF31j6K'
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
