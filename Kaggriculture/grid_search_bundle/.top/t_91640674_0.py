"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXctuXFly/Beua6F6SC15x5ZqpoVhS4JEmRg3iEYDM4YBY7xoe2f43y1RrNfNyMjIPHmLFKd3Jarq3vM+mZGRkb/878W/'
    '//b7P/7++8W//HLx4fLTp4vbxcV//PZff/vvL3/48vEfv/3+n3//ny+ff7n46e3H7Zf/pR9+/PzXXy/fvf358upicfH6/c3F'
    'Ymn+/Omn7fbDxWKz+49P2+2bL3+++Wl7eX2xeD7588/bq/fvjv784eP7N59fXx//4Pb/Fie9ePv6L58/HL1/359fLm62n67v'
    'Grr/cN/no5/t23fcfe8d9404fcu79x+vf7p76OGTfc/9T+l77pupPvvHz2+v3vz65Z/Xn79OCHnw5Jt6668uX2/3g0SH6P6b'
    'X2fh5Plf/uPd9X5mnff86XhRsNecfvFkri+vtx+957++DAbo2xfwuOx6sHvp0XPvv8TGZbLJ0OMOTS9MrX3B4XFg2esTap+7'
    'f5o/IPJE2sd/ev/5fsDBeIQT6I/zYeHZ4ajM31Hr/HEYmr/9qWXHYWT+lAEZmD9pXCrzuPstGI5vHag97rDepn+qPc8Ob8tq'
    'YN0fWg27h2wvGxeBMhrNa+Dbh8TjkJ0TXgfhSnv9/upq+/r61z9tP16/vXr7b3fNtPdJ6vYvXFuoGeQBu1su1VDw1rChwegk'
    'm73bu50TVNn89QPjj5/88ZNH9JPTM/HT9uqr63a0U755ZNgDND7ai9uU/7S3QuKTxzf/rZ+1qB1lxh86HRrY4eVt8qyZ9GPk'
    'djhcipWGgvMftl1poX+X4DbGPzfDFB7yO/ugeZjA4ONRqjRwau+nFsGR11R4tR3gQhMOA2xaII8vmDZngMMGMs+ycJSaISo8'
    'Yz9C9rfqCIGH4gEq3xb/LL+tXnUnd94pirmc/PnT9cfLmx+3Hz/+9WKxLl6Gkw/tl2LX9fgwF+XolblzT49marQnkiu2AEBl'
    '+UrV7w3bOHus4REZdqum1+/QPQH8PnoRd3TAwJ7ZEQKTiLDO2JdULKTD8ig979AwF/9uMjM900MzQqy9MMEEhy5be3C4AFSx'
    'kRPQbeTq++MhPQ8ZswuGPF5yJk7DpX/c/V3u8ljjkx5hsc3Gfy66aI4j/XX1Xn7818IFBgaTXBNl0CFh4oCHgkBaxUmeuthS'
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
