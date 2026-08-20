"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXdFuG0mS/Bc988EkZdm+N43N3RFWYxmSvMTuQBgMsHM4YLH7MHdvh/v3kyWR3eyMjIzMqqZkj99kmWpWV2VVZWRGRv78'
    'vyf/+evv//rt95P/+Pnk0/nNzcnd4uS/fv33P/77/hf3P/7r19//+dv/3P/888mPF9eb+/+lP/zw+W+/nH+8+On88mRx8v5q'
    'e7JYml/f/LjZfDpZnO7+42az+XD/6+2Pm/Pbk8Xrya9/2lxefRz9+tP11YfP72/Hf3D3f4uDt7h4/5fPn0bfv3+fn0+2m5vb'
    'h4Huf3h659Gf7cc3fn3vO54GcfgtH6+ub398eOjwk/2epz+l3/M0TPXZP3y+uPzwy/0/bz9/WRDy4Mkn9dFfnr/f7CeJTtHT'
    'J7+swsHz7//j4+1+ZZ3v+dPYKNjXHH7wYK3PbzfX3vPfnwcT9PgBPC+7N9h96ei5Tx9i8zLZZOhxw9ALS2u/YHgcMHt9Qe1z'
    '90/zJ0ReSPv4m6vPTxMO5iNcQH+eB8Oz01FZv9Ho/HloWr/9qWXnoWX9lAlpWD9pXirruPtbMB2PL1B73GBv01/Vnment4s1'
    'sNdvsobdQzbnHY1AmY3ONvD4Q+JxyM8Jr4PQ0t5fXV5u3t/+8qfN9e3F5cXfH4Zp75PU7V+4ttAwyAN2t1xqoOBbw4EGs5Mc'
    '9m7v9lygyuavHxjf/+T7n7ygPzk8E282l1+g22inPCIyjAANRju7S+GnvRcSnzy++29x1qJ2lBk8dDg18IWXd8mzZvIeLbfD'
    'cClWBgrOfzh2ZYT+XYLHGP+5mabwkN/5B52nCUw+nqXKAKf+fsoIRqip8NV2ggtDGCbYjECeX7BszgSHA2TIsnCUmikqPGM/'
    'Q/Zv1RkCD8UTVL4t/ih/W73qDu68wyjmcvLrm9vr8+0Pm+vrv50s1sXLcPJD90ux1/X4PBdl65W5g6ejlWp9EwmKLUCgsnyl'
    '6veGHZw91vCMNMOq6fXbdE8A3Ecv4h4vYMKe2RkCi4hinTGWVDykwTxKzxsG5sa/O7mZnuuhOSHWX5jEBJsuW3twuAGo4iAn'
    'QbeWq+/7Q/o8pM0vaEK85Eycpku/3/294HLb4JOIsDhmg5+LEM0B0l+s9/z6r4ULDEwmuSbKQYeEiwMeChJpFZA8hdjScJ4O'
    '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'
    'Uw=='
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
