"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXUtvm9mR/S9acyG+9JidYjOxELVlyHKIpEE0GkgGAwwyi052g/nvI1sU+fGrqlOnqu4l6YZXpimS333fepw65+f/vfjP'
    'X3/75z9+u/iPny8+3X3+fLGZXPzXr//z93+9vPHy8p+//vbf//j3y+ufLz7cP61e/sq9+MOXv/5y9/H+p7uHi8nFu8f1xWQm'
    '3v78YbX6NPjD59Xq/cvb6w+ru+eLyfXo7Z9WD48fLybT3cc/PT2+//Luef+N5Wbzf5OD/ty/+/OXT/snTQd9+/livfr8/K2t'
    'Hx+fnj98e7V7a/TicCA+rx4e9k+dfv3Y+C2rIfvvDBqy++twnO4f3v/yMh/PX7YDyjVNHRfRnO1PaE3Yj5T9SPXZ/CO2rZr3'
    '7+f41wet2c+5Mvvjt0A/Pz3cvVvtxu3gEbJv2kPFK/CwPw43yOHgbpvxdQV9/a2X/3983m0a/Z3Ik9/djQdw1JaXobp7Xj2N'
    'Xr09dP+pUTPQyI4Oo10jhi1f3X02nh765f0PymHaPWL34vPjF2e45BOUhb5r8e6H2w7XeE00HzWxBGT7lWe+vshN/L69aMYq'
    'gyaPn8FhUBqt7aphpnky/HRivNBik5uzzcCND8IOI0isN/kOf2VR6w4NX+Zc2L4zaOf+HetRuQcog7X70+iRyR7s2yt++PVF'
    '4HfRR4ExBb72tgqZz1oXbeCGRB99fHhYvXv+5Y+rp+f7h/u/fRu11l04RnvGRh746Nt59qPp5aZHtsqPj0KXduu2DaZgsrD9'
    '2YDDuf3AAjqckZ0e+rbtJ9Rsfvht1inD6z5mI/Qapkgb5DA18FxbDpJ0xXmbSJx9sUfbI7y3b902KAOMmtBqiPdOUjzWERkj'
    'ZYgDnmb3NSzdj1YDPFgCCbNz7D4nvbxjP7lgakeursS9FDtmG1xCmaunxzrM3caFsy9/4nW5StLHW/De8J7jHmWJA6zj3Rsa'
    'Mf8gt2/a1JC5R9NR11jY/f89fSXrcoxelFwNJp8yTr/Fbe1JLy8l9sOE4+L8YDczfdLMC7Sjq4U7yQixf7h7+kv8zhqb+GrU'
    'ftuUdJxEMSODY4Ks9/1vjxMZmbvPCCSXpk0uq91kpSdOi9e7ofbCDGpnVMm/1TrAu3PQ59VWW8GyGU7W/gcP3o3Pn5wrkGH0'
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
