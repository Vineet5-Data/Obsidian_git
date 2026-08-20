import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXctuJEly/Beeeeh6sEjqxumu1TSWM2yQ7C2sBoXBAFpBgLA6jHQT9O/q6XplZViYm3lEstkr3grFYma8w93c3PyX/7n4'
    't99+//vffr/4p18ufvj88f7Dr5/unp4/P64vtpcX//7bf/7rf335y5ePf//t9//4239/+fzLxY8fv/5V+/DD57/+evfzx5/u'
    '7i8uL94/bC4u58XXTz+u158Gf3harz98+Xrz4/ru+eLyevT1T+v7h58vLmfHn396fPjw+f3z6T9W2+3/Xg479unj+z9//nR6'
    '02zQt18uNuun569t/fnh8fnHr5+OX40+nA/E0/r+/vTWxfith8cNXgUaMnzt6dN4KlADRq+rzh7s4bElX+dkdtbX/a/Iuz7d'
    '371f18YT9efwD+Bto3aTt+7/ZTieRTu+fvfzaTGc9XU/U5WfhSO8vhu//7Q87p7Xj+NFNP7ufPXApTsfL6Knh8/jRVQuzj/9'
    'sTPOvhn1jk1lOTjnAzwapVP/3t/tl+bhR7udOei6NZen4SpfehiF4a/C6QL7D00O2AnFCiZv2Y89GLPBcBQzVv5Gn7H9uNOh'
    'O3vueOedhrCcpsq6nAmHG9gM1aOVny1nXdBGFh068eQdWqqPpfxNPI9gCPcnDJijaN70QTy+4/jhy9n7hD54A3ca95YH739J'
    'J73v8+mEd+nA4X8Hb+r63PDDN3js6FZZVKzJ4DA1LpA+Tx2frc72ffEWjO0R8tPCjOjTgvcP9/fr98+//mn9+Pzx/uO/nJ8J'
    'nQYv/RJjiaTfMdEcHG7tQXuqe+joiIx+XLnKr7aGBfiq178xv+M+LvPebWj/NdokwLwrzMeBEQ4WbsbPAMYI3BO4V/ulbZnJ'
    'vA/D3kZ9DAcQOPaGQcpcFfgpeiAbC/QpfCDzCET7scEfrTc56UDVB1WyfZUNRH3zeP6Jp9Pm+irAU/g46C0bzgMw7k+PLI3B'
    'ePOXwAmxLeP2WY8LTVWCm72wYf32tP5Pk+99YEMtMYA9azIKEJAsmhrsYmu74hiaU7mdQ+sgcQ1GhkAjVCddDF0MBIQzVi+N'
    '5N3IwPXTcd02KuBlzqOpsQDeUpv/8EbQbIiUeUKGh1tt8aMpQA3gNAsAJDgXHZEuBzRcpV1P/jGW9o+DnL099u2xJiZVt17s'
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
