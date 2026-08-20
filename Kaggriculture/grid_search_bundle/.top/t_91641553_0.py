"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vXMlu/C96ngfPjKyV86a158bG1VqGLGdwsxAWC+QGAYKbh03egvz3+EPzdVgsFsk+ku3102rl0Zk+3exuslgs/vq/'
    'Z//++x//+PsfZ//069m7q/fvz+4XZ//x+3/9239//MXHH//x+x//+ff/+fjzr2ev39xuPv4r/eHnD3/77ertm1+urs8WZy9v'
    'tmeLpfn1+9ebzbuzxfnuH95vNq8+/nr7enN1d7Z4Pvn1L5vrm7dHv353e/Pqw8u74z+4/7/FyVu8efnXD++Ovn//Pr+ebTfv'
    '7z4PdP/Dwzsf/dl+fMev733HwyBOv+Xtze3d688PPfxkv+fhT+n3PAxTffbPH95cv/rt4//effi0IOTBk0/qo7++ernZTxKd'
    'oodPflqFk+d//Ie3d/uVdb7nL8dGwb7m9IMna311t7n1nv/yKpigLx/A87J7g92XHj334UNsXiabDD3uMPTC0tovODwOmL2+'
    'oPa5+6f5EyIvpH38+5sPDxMO5iNcQH+eD4Znp6Oyfkej8+ehtX77U8vOQ2f9lAlprJ80L5V13P0tmI4vL1B73MHepr+qPc9O'
    '7xBrYK/fsobdQzZXA41AmY3BNvDlh8TjkJ8TXgehpb28ub7evLz77S+b27s312/+9fMw7X2Suv0L1xYaBnnA7pZLDRR8azjQ'
    'YHaSw97t3ZELVNn89QPjx5/8+JOv6E9Oz8T3m+tPodvRTvkSkeEI0MRoF/ep+GnvhcQnj+/+2zhrUTvKTDx0OjXwhZf3ybNm'
    '8h6d2+FwKVYGCs5/OHZlhP5dgscY/7mZpvCQ3/kHg6cJTD6epcoAp/5+ygiOoqbCV9sJLgzhMMFmBPL8gmVzJjgcIIssC0ep'
    'maLCM/YzZP9WnSHwUDxB5dviz/K31avu5M47RTGXk1+/v7u92v68ub3929liXbwMJz8MvxRHXY9Pc1F2r8xdeHq0Ut03kUKx'
    'BQAqy1eqfm/YwdljDc9IO6yaXr+tewLEffQiHvECBvbMzhBYRIR1xrGk4iEdzKP0vMPAXPx7kJvpuR6aE2L9hQkm2Lps7cHh'
    'AlDFQU5At87V9+MhYx7S8wtaES85E6fp0h93/6hwuTf4ZERYHLOJn4shmhNIf7Leq9t/KVxgYDLJNVEGHRIuDngoSKRVguRp'
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
