"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXdFuHMmR/Bc+z4NmSNHce+NK7ZNgrihQlAe+hbBY4HwwcPA9rP12uH8/SuR093RGRkZmVQ8leZ+WSw2nq6uyqjIjIyN/'
    '/t+z//r1t7//9bezf/v57P31hw9nnzZnf/v1f/7zHw+/ePjx77/+9t9//efDzz+fvXl7Nzz8K/3hx49/+eX63dufrm/ONmev'
    'bvdnm6359Yc3w/D+bHNx+IcPw/D64df7N8P1/dnm5eLXPw03t+9mv35/d/v646v7+R98+r/N0Vu8ffWnj+9nzx/f5+ez/fDh'
    '/stAxx+e3nn2Z+P45q/vPeNpEMdPeXd7d//my5dOP9nnPP0pfc7TMNXv/vHj25vXvzz87/3HzwtCvnjxSX30N9evhmmStnSS'
    'nj4L1uHhn97dj6vrPOuPny2APeDxA0fre30/3Hnf9+o6mJTHD+C5OIz4cdWOvvfpQ2wmFhsLfd009MJy2gdMXwdMPbOI9pvH'
    '7/OnJFw6+7Ufbj8+TTWYiXDp/BmeTMxORGXlZqPz379p5cYzys5D28opU1JYOWlGKit4+FswEY8Dr33dZGnLX9W+z05rFztg'
    'r99oB4evGa47LL8yD51X//GHxNchTyY8/EMbe3V7czO8uv/lj8Pd/dubt//xZZj29kjd74VLCg2DfMHhTksNFDw1HGgwO8lh'
    'H3ZtzwWqbPv6UfH7n/z+J1/RnxyfiR+Gm8/B2WynPMZcOMYzUdjlp1SENPod8cljnXwbQW1qR5iJdI6nBL7o9lPyjHkaf8tt'
    'MF2ClQGC8x6OWRmhf3fgMcZ/Pk5PeJgf/IDO0wMmHc9OZYBLXz61+LOIqPDoaWILj54m1jxZnlewXM7EhgNk0WLhqBynpvC3'
    '48zYv1VnBnwpnpjyLfCv8rfVK+zoLjvGH7eLX3+4v7ve/zjc3f3lbHNevOQWP3S77Hpde6e9AFuvwtdv/715yFIMNQtpZ1bQ'
    '76KUjj471MWNuekQB02HGn7f+i0AojZ+C/R4ncLGA+s1XTEHi4tDP+bgOHNb+tJpbC5C3clVBLtXcCjs3Q/gnEf0qY/PtgAG'
    'lctEG2T7ffb7l/T5krbLvik8JUfgMnv5+4VejW3bBp0M44pjrt3h9nvsHf7m+u7PhUsKTCK5B8rIQCKOBV8KMlqViHYZD0vD'
    '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'
    'Ad2gAs4='
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
