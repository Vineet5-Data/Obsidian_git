"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vHEeS/C965oM5/JLuTSvNroWVLYOSltgzCMPA7eGAw96D794O+9+PFjk9M52RkRFZNdT64CcSM2R3VVZ1dWZkZOSP'
    '//vi33/+5e9/++XFv/z44g+f371/+9MPrz9++ny7fXF/9uI/fv6vf/vvh28efv37z7/859/+5+H3H198++7Lt/SXP3z+608/'
    '3H54+/nNpxdnL+6+3b5++Hm9++b19+++e/3+4YuP3263P7w4u9p98XG7ffvw8ZvXt7cfHv5hs/r86Trn9/f/ODsc+A/v3vz5'
    '8w9H11vGDr9tffh098v7Y3PAqa5n9N32/Yfvfx354ETfv36zXcZ3NMu77cdPX0z//YfbT9+ufnv88njcH7fv3+9vdYMHvBkc'
    '8MPfb4/HuR7U4S+rDXg43tV1n/7l4LrrzQstsn29tkPDwPFO+xv88VdzTBt49tX0CSxfNcb/cMfvP+23xtHlwHePO6I5g9ef'
    'trfZhfdflkZ63AbQNuurKDbZLT83yn6TdKwChhyM8fjMmrYg5j54VJfrGVs9PvtxoA+b8GMyh9IkwOwHNtldeP2RuY7L+Ha/'
    'PC2EcLndlB7PxmmX3U2IXg5ssXq8j/9Mr2tYU7ncwTMx43Jri/9zTnr1i/EEmX7Y+mof3r/fvvn00x+3t5/evX/3r+tdtD+1'
    'owWqUyS+FsjVyie7Gul621hDjSfpk5lbQ317+2F1asLBw2uDP7S21scPnw0zLB7fwf32DmnwYC9SJ3v5g8Ox7M+v+GfJh6Vt'
    '46Z6svYEa0pn/ep0HrDm5dqaj29PGKYs/3LmfFi6trvdcnDLp0FoMy4nQJ74x3WbdX7EcxOuxoYEoiOTabwEiKGf+ZXy+9V+'
    'v1pxtdXp8jJ1QI4RhIsCEuLY0IUIKJAnFQEfE12NCFeMeEWLz7H/xHuBRUPES65N470P11YsEKV6oRY3OnGRQpQ5sG7Zau1v'
    'M2wMI8imoWpmDX28ICRc/DGAbNTWjT4ywgJ0ZwHFrCFWW4XAZ4vL0jVs54Isuu5cD3hd5HodJ27lZHnrEtG8/M0RnTjb7dLO'
    'eDZJCTrgzjmH5J8GtbnveKg+/oDmmlzFQyLY+dvBX6StkuB71jDH8BfXeTncIRcdx2WjJU70yEMPoOOHDf9MfiKE3A53xTz/'
    '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'
    'mG3V6eP/LQz2/h/3/wdNWMOj'
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
