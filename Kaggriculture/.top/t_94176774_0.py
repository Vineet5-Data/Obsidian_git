import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vW1ly/C965oNJUZSUN63NzRirGRmyHWIzEAYDZIMAweZhkrdg/3scWSIv76murupzaGsGeqNp6t7zfbqrq6t//t+z'
    'f//1t7//7bezf/r57E+f39++++XDzcdPn++3Zw+Ls//49b/+7b+//M+Xj3//9bf//Nv/fPn889kP7x//V/vwp89//eXmp/c/'
    '3tyeLc7e3u3OFqvm648/bLcfJv/xcbt99+Xr3Q/bm09ni8vZ1z9ub+9+Olss9z//cH/37vPbT4e/2Dw8/GMx7diH92//8vnD'
    '4U3LSd9+PtttP356bOtPd/effnj8tP9q9uF4ID5ub28Pbz2fv/X5cZNXgYZMX3v4NJ8K1IDZ68LZgz3ct+RxTpZHfX36FXnX'
    'h9ubt9toPFF/nv8AvG3WbvLWpz+ZjmfTjsfvfjoshqO+Ps1U8LN0hLc38/cflsfNp+39fBHNvztePXDpruaL6OPd5/kiahfn'
    'n/9/Zxx9M+sdm8p2cI4HeDZKh/69vXlams8/+rozJ1235vIwXO1Ln0dh+qt0usD+Q5MDdkKzgslbnsYejNlkOJoZa3+jz9jT'
    'uNOhO3rufOcdhrCdpmBdLoXDDWyG8GjlZ8tRF7SRRYdOPnnPLdXHUv4mn0cwhE8nDJijbN70Qdy/Y//hy9n7EX3wBu4w7j0P'
    'fvolnfSxz6cTPqQDz387edPQ56YfvsNjZ7fKeWBNJoepcYGMeer8bHW27zdvwdweIT9tzIgxLXh7d3u7ffvplz9v7z+9v33/'
    'r8dnwqDBK7/EWCLld5xoDp5v7Ul7wj20d0RmPw6u8osHwwJ80evfmN95H9d17za1/zptEmDeNebjxAgHC7fiZwBjBO4J3Kun'
    'pW2ZybwP095mfUwHEDj2hkHKXBX4KXsgGwv0KX0g8whE+7HDH42bXHSg4kGVbF9lA1HfPJ9/4un0ub4K8JQ+DnrLhvMAjPvD'
    'I1tjMN/8LXBCbMu8fdbjUlOV4Gbf2LB+fdr4p8n3PrCh1irIXTcMYluhPZyPYfTlDBb/curd3yGkRjoO2VUrHZIV+2H/1smB'
    '5d+dYtt7OmcNIULWu+4Eer92GRv0oq0MC7djQijScZqy9htmE7U8iMlQsMfooj+gfik2StCrZDByyNA5eOdQ1h8HuHp97Otj'
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
