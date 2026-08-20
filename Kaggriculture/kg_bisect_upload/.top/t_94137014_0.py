import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrdXctuXEly/ReuuVAViy/v2FKNJQy7KVDSFMYNotGAxzBgjBdt7wz/uzViPW7djDiPyCyK8kqFYunefGfEiRMnfv2fs3/7'
    '/Y+//+2Ps3/69eynLx/u3/328e7T5y+P67On87N///0///W/vv7l68e///7Hf/ztv79+/vXs/Ydvf9U+/PTlr7/d/fLh57v7'
    's/Oztw+bs/Nl8/Wn9+v1x8kfPq3X775+vXm/vvt8dn49+/rn9f3DL2fni/3PPz4+vPvy9vPhf1w9Pf3v+bRjHz+8/fOXj4c3'
    'LSZ9+/Vss/70+Vtbf3l4/Pz+26f9V7MPxwPxaX1/f3jrxfytu8dNXhU0ZPraw6f5VEQNmL0unb2wh/uWfJuTxVFft78C7/p4'
    'f/d2nY1n1J/dfwjeNms3eOv2v0zHs2nHt+9+OSyGo75uZyr5GR3h9d38/Yflcfd5/ThfRPPvjldPuHSX80X06eHLfBG1i/NP'
    '/9gZR9/Meoemsh2c4wGejdKhf2/vtktz96PnnTnpujWXh+FqX7obhemv6HQF+y+anGAnNCsYvGU79sGYTYajmbH2N/qMbccd'
    'Dt3Rc+c77zCE7TQl63IhHG7BZkiPVny2HHVBG9no0OGTt2upPpbyN3wegyHcnjDBHLF50wdx/479h69n76fogzdwh3HvefD2'
    'l3DSxz4fTviQDuz+7+RNQ59LP3yHx85ulYvEmiSHqXGBjHnq/Gx1tu+Lt2Buj4CfNmbEmBa8fbi/X7/9/Nuf1o+fP9x/+Jfj'
    'M2HQ4JVfYiyR8jtONAe7W3vSnnQP7R2R2Y+Tq/zyybAAX/X6N+Z33sdV3bul9l+nTRKYd435ODHCg4Vb8TMCYyTcE3Gvtkvb'
    'MpNxH6a9ZX2kAxg49oZBilyV8BN7IBqL6BN9IPIIRPuxwx/Nm1x0oPJBlWxfZQNB35zPP/B0+lxfBXiijwu9ZcN5CIz7wyNb'
    '45tv/hY4AU4Ib5/1uOdvarhZz2Nbw/owhodPr+l57x4fPmaP43MMHIn9g2ffjHVLhtz+gSW1imHsRZdpEMHJosGBrre+iw5h'
    'OskdTW2EwmXIzIFOwE66HoaYCRHamF4dxRsSQeyHfdw3KsHLnEdDkyF4Szb/9F7QLImSkQKGB9tu/NEQpg5ANQsGBGgXHJEC'
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
