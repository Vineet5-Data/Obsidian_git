"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXUtvnEly/C888zDsph7jG0fqhYTlSIIeJtYDYjCA1zBgrA9j3wz/d2tE6uvuLyMjIrOqe7TruRFks+tdlRkZGfnT/1z8'
    '2y+//u2vv178008XP3x6ffvy53c3Hz5+er+7uL+8+Pdf/vNf/+vzXz7/+Ldffv2Pv/73559/unj1+stfuz/88OkvP3/Y7V5e'
    'XF78uLt9++bicrv69d2r3c3Hi8urzdff37x5/ePN7ee/vHh7d3G5ub//38vDfr97/eLPn97t/7zv+E8Xd7sPH780++bt+4+v'
    'vvz0eYAfVr9KP3U88tjH2MUPr3a7d6CTL9+/fXdx1LV9W6Bv67WAvY19zGZm6ZXdATQltzdvPi5j9zpwe/Nit7R/1PrXb3vY'
    'BJ1puPm4e+914+s/HW6M/X+HjrAdQib/YSe8e//25acXHw/28b0/KR/efkpGBycDdL2+Rl/bhN1gO2PfRbYU9qyQU7z87fDY'
    'ZUOddnrArvnTb6c/WR56UIxlcSfqcQDwIK8GB1v2li3Zs78tTjIjoemDhiaeHrAqL25W5wFsCdCFiWuSTg890M4+KawROMjr'
    'g7OVK7X8pJ9CPS2gR2yvLr/Zz1rjPtvdrM+HXHL4p3zpSOOPW9G8Mva/YjfW1LMCLvTlh/2IhxYgXlDLHLA2H9dtzmsS12F/'
    'SYQ+LC2DF/b4w+yGfPgkPPuxSdnS/CblD6WWljmb3FC8sE7nhhz7FWEPPe7aU3oTrSN8bCldffl+aCB97dqLt7e3uxcff/7T'
    '7v3H17ev/+XxdC0ngvWzYHyASdnvx6QPhabJcsT75dHdOviBmh4fdre/7YODzu1du7BGG2ONltbItQNmqTEJx6aHeQWsejXn'
    'ho2Tz3qA98NAf9AXot5Bm2jO6iALDLgHeVurW7XZFPACwg+rNZLHIcx3NLNK7ftPQkROlv8ldoXTUDLQS9vqD69idsCmP7/p'
    '7jxdS40X/xtvyLmnpjR0amPsj4b+3zYUbI95VnLBEoXwQslIZjbnoz+IHEoGJ6C/BTt5uludA9S4Sw8vRROGtNCUgOm0UMe4'
    'CMsbB4A+DQI2nQwwKja7DzM1acARQzTh8fqAAWrE5nbfD3vAm/tJsw4mQ+5pMLkIbvOmF1n+TdSEBz6WFhcL5eGH4cYQNhys'
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
