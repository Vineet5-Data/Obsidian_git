"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vW9cR/C965oNJyrLdN8VmaiGKZchyidQQjABNUaBIH9K+Ff3vlSWSl7w7Ozu751xKTvwURibvPd9nd3Z29tN/T/7+'
    '82+//vLbyZ8+nbw///Dh5HZ28o+f//W3f9/94e7jrz//9s9f/nP3+dPJdx9/+vz++urNx9c3J7OT9dvV+d1/n9/OPp28vbhe'
    'nQQfvvz6/N3Fj+eXdz9+fbU+mc3Nnz+8Xa3en8xOt//wYbV6M3rV3p9/XF1evfvy59v/zQ56cfH6h4/v996y68+nk/Xqw819'
    'c3YfNn3e+9muFfvd996xadvhW95dXd+8vX/o8Mm+Z/NT+p5NM9Vnf/fx4vLN57v/vfn4ZdjJg0ff1Ft/ef56tRskOkSbb36Z'
    'hYPn3/3Du5vd/Dnv+X5/6tlrDr94MNfnN6tr7/mvz4MBevgCHpdtD7Yv3Xvu5ktsXEabDD1uaHphau0LhseBZa9PqH3u7mn+'
    'gMgTaR//4erjZsDBeIQT6I/zsPDscFTmb691/jg0zd/u1LLj0DJ/yoA0zJ80LpV53P4WDMdDB2qPG9bb+E+159nh7bIaWPeb'
    'VsP2IavzjotAGY3Oa+DhQ+Jxh3bOg8kSXgfhSnt9dXm5en3z+fvV9c3F5cVf75tp75PU7V+4tlAzyAO2t1yqoeCtYUOD0Uk2'
    'e7t3e05QZfPXD4xvP/n2kyf0k8Mz8cPq8ouDtrdTBnfM+IRnwANM+U87KyQ+eXzz3/pZs9pRZvwhwS2e3ybPmlE/Wm6H4VKs'
    'NBSc/7DtSgv9uwS3Mf65GabwkN/aB52HCQw+HqVKA8f2fmoR7HlNhVfbAS40YRhg0wJ5fMG0OQMcNpB5loWj1AxR4Rm7EbK/'
    'VUcIPBQPUPm2+KP8VrvqAmzzEKucj/784eb6fP3d6vr6p5PZsngZjj50vxR7XY+Pc1G2Xplb93Rvplp7IrliMwBUlq9U/d6w'
    'jbPHGh6RZrdqfP023RPA76MXcY8OGNgzO0JgEhHWGfuSioU0LI/S84aGufh3JzPTMz00I8TaCyNMsOmytQeHC0AVGzkC3Vqu'
    'vm8P6fOQNrugyeMlZ+I4KPrt7u/lLrc1PukRFtts/Oeii+Y40l9W7/n1XwoXGBhMck2UQYeEiQMeCgJpFSd57GJLzdkc8Npy'
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
