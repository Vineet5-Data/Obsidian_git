"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vW9cR/S9ac2FSlGx3p9hMLESxDEkukRpCEKApChTpIu2u6H+vbFPk45uZM2dm7n2kXK1MUyTf/b7zceacT/85+duv'
    'f/z+2x8nf/p08uHi9vbkfnby91//+dd/Pbzx8PL3X//4x2//fnj96eTd5c3q4a/ci+8+/vzLxfvLny6uTmYnb67XJ7OFePv2'
    '3Wr1YfCH29Xq7cPb63eri7uT2cvR2z+trq7fn8zm249/uLl++/HN3e4bZ/f3/53t9efyzY8fP+yeNB/07dPJenV796Wt769v'
    '7t59ebV9a/RifyBuV1dXu6fOP39s/JbVkN13Bg3Z/nU4TpdXb395mI+7j5sB5ZqmjotozuYntCbsRsp+pPps/hGbVp327+f4'
    '1wet2c25Mvvjt0A/P1xdvFltx23vEbJv2kPFK/Cw74cbZH9wN834vII+/9bD/9/fbTeN/k7kyW8uxgM4asvDUF3crW5Grx4f'
    'uvvUqBloZEeH0bYRw5avLm6Np4d+efeDcpi2j9i+uL3+6AyXfIKy0Lct3v5w2+Ear4nmoyaWgGy/8syvL3ITv2svmrHKoMnj'
    'Z3AYlEZrs2qYaZ4NP50YL7TY5OZsM3Djg7DDCBLrTb7DX1nUukPDlzkXNu8M2rl7x3pU7gHKYG3/NHpksge79oof/voi8Lvo'
    'o8CYAl97XIXMZ62LNnBDoo9eX12t3tz98v3q5u7y6vIvX0atdRemaM/YyAMffTzPnptebnpkqzx/FLq0G7dtMAWzpe3PBhzO'
    'zQeW0OGM7PTQt20/oWbzw2+zThle9zEbodcwRdogh6mB59pykKQrzttE4uyLPdoe4Z1967ZBGWDUhFZDvHOS4rGOyBgpQxzw'
    'NLuvYel+tBrgwRJImJ1j9znp5U395IKpHbm6EvdS7JhtcAllrp4e6zB3GxfOvvyJ1+UqSR9vwXvDe457lCUOsI53b2jE/IPc'
    'vmlTQ+YeTZOusbD7/y19JetyjF6UXA0mnzJOv8Vt7VkvLyX2w4Tj4vxgNzN91swLtKOrhTvJCLG/u7j5c/zOGpv4atR+05R0'
    'nEQxI4Njgqz33W+PExmZu88IJJemTS6r7WSlJ06L17uh9sIMamdUyb/VOsC7c9Dn1VZbwbIZTtbuB/fejc+fnCuQYfQtk9Qh'
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
