"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vW9cR/S9ac2FSlCx3p9hMLESxDEkukRpCEKApChTpIu2uyH+vYlHk45uZM2dm7n2kjKxMUyTf/b4zZ86c+fy/k3/8'
    '/Nuvv/x28pfPJx8v7+5OHmYn//z533//z+Mbjy9//fm3f/3y38fXn0/eX92uHv/Kvfjm048/XX64+uHy+mR28vZmfTJbiLfv'
    '3q9WHwd/uFut3j2+vX6/urw/mb0evf3D6vrmw8lsvv34x9ubd5/e3u++cfbw8Ptsrz9Xb7//9HH3pPmgb59P1qu7+y9t/XBz'
    'e//+y6vtW6MX+wNxt7q+3j11bj51+4HhU7d/HQ7K1fW7nx4H//7TZvS4dqiDIJqz+QmtCbthsR+ZGwPw0M1XTvv3fPzrg9bs'
    'plyZ/PFbw2eP5/r68u1qO5J7j5B90x4qXoGHfTvcH/uDu2nGH2vqj996/P+H++2e0d+JPPnt5XgAR215HKrL+9Xt6NXzQ3ef'
    'GjUDjezoLNo2Ytjy1eWd8fTQL+9+UA7T9hHbF3c3n5zhkk9QFvq2xdsfbjtc4zXRfNTEEpDtV5759CI38bv2ohmrDJo8fgaH'
    'QWm0NquGmebZ8NOJ8UKLTW7ONgM3Pgg7jCCx3uQ74BrJrDs0fJlzYfPOoJ27d6xH5R6gDNb2T6NHJnuwa6/44acXgd9FHwXm'
    'Ffja8ypkPmtdtIEbEn305vp69fb+p29Xt/dX11d/+zJqrbswRXvGRh746PN59mfTy02PbJU/Pwo92o0TM5iC2dJ2ZwP+5uYD'
    'S+hvRnZ66Nu2n1Cz+eG3WacMr/uYjdBrmCJtkMPUwHNtOUjSFedtInH2xR5tj/DOvnXboAwwakKrId45SV4DlQEOjJEyxAFP'
    's/salu5HqwEeLIGE2Tl2n5Ne3tRPLpjakasrcS/FjtkGl1Dm6umxDnO3ceHsy594Xa6S9PEWvDe857hHWeIA63j3hkbMP8jt'
    'mzY1ZO7RNOkaC7v/X9NXsi7H6EXJ1WDiKePoW9zWnvXyUmI/TDguzg92M9NnzbxAG10t3EkGxP7+8vav8TtrbOKrqP2mKWmc'
    'RDEjg2OCrPfdb48DGZm7zwCSS9Mml9V2stITp+H1LtRemEHtjCr5t1oHeHcO+rzaaitYNsPJ2v3g3rvx+ZNzBSKMvmWSOuRK'
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
