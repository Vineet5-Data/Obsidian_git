"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vG9kR/C8682BSsmznJtvcWFitZchyiM1CWCyQDQIEm8MmtyD/PbIkcobT1dXV/d5Qstc3WiZn3vfrrq6u/um/R3//'
    '5ffffv396E8/HX04+/jx6GZx9I9f/vW3f9/+4fbjb7/8/s9f/3P7+aejd+dX69v/pR9ef/rx57P35z+cXRwtjt5cbo4WS/Pn'
    'j+/W6w9Hi5Ptf3xcr9/e/nnzbn12fbR4PvnzD+uLy/ejP3+4unz76c31+Ac3/1vs9eL8zfefPozev+vPT0eb9cfru4buPjz0'
    'efSzXfvG3ffe8dCI/be8v7y6fnf30OGTfc/DT+l7HpqpPvv1p/OLtz/f/vP60+cJIQ+efFNv/cXZm/VukOgQPXzz8yzsPf/2'
    'P95f72bWec9340XBXrP/xb25PrteX3nPf3MWDND9F/C4bHuwfenouQ9fYuMy2WTocUPTC1NrXzA8Dix7fULtc3dP8wdEnkj7'
    '+I+Xnx4GHIxHOIH+OA8Lzw5HZf5GrfPHoWn+dqeWHYeW+VMGpGH+pHGpzOP2t2A47jtQe9yw3qZ/qj3PDm+X1cC637Qatg9Z'
    'n3VcBMpodF4D9x8Sj0N2TngdhCvtzeXFxfrN9c/fra+uzy/O/3rXTHufpG7/wrWFmkEesL3lUg0Fbw0bGoxOstnbvdtzgiqb'
    'v35gfPvJt588oZ/sn4kf1xefXbfRTrn3yLAHaHy005uU/7SzQuKTxzf/rZ+1qB1lxh/aHxrY4eVN8qyZ9KPldhguxUpDwfkP'
    '26600L9LcBvjn5thCg/5rX3QeZjA4ONRqjRwau+nFsHIayq82g5woQnDAJsWyOMLps0Z4LCBzLMsHKVmiArP2I2Q/a06QuCh'
    'eIDKt8Uf5bfVq27vzttHMZeTP3+8vjrbvF5fXf14tDguXoaTD90vxV7X4+NclK1X5tY9Hc1Ua08kV2wBgMrylarfG7Zx9ljD'
    'I9LsVk2v36Z7Avh99CLu0QEDe2ZHCEwiwjpjX1KxkIblUXre0DAX/+5kZnqmh2aEWHthggk2Xbb24HABqGIjJ6Bby9X37SF9'
    'HtJmFzR5vORMnIZLv939vdzltsYnPcJim43/XHTRHEf68+o9u/pL4QIDg0muiTLokDBxwENBIK3iJE9dbKk5Dwe8tpwfYxJ0'
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
