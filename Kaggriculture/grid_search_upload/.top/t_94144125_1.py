import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXctuXFly/Beua9HFlyjv2OoatzDspkBJUxg3iEYDHsOAMV60vTP875ZFsu7jREZG5DlFsm2tVCiW7j3vkxkZGfnLf538'
    'y2+///1vv5/8wy8n339+f/PDrx+uP376fLc7ud+c/Otv//7P//HlL18+/v233//tb//55fMvJz++//pX7cP3n//66/XP73+6'
    'vjnZnLy73Z9sTpuvP/64232Y/eHjbvfDl6/3P+6uP51s3qy+/ml3c/vzyWZ7+PmHu9sfPr/7NP2Py/v7/97MO/bh/bs/f/4w'
    'vWk769svJ/vdx09f2/rz7d2nH79+Ony1+rAciI+7m5vprWfrtz49bvYq0JD5a6dP66lADVi9Lpw92MNDS77OyXbR18dfkXd9'
    'uLl+t4vGE/Xn6T+At63aTd76+F/m49m04+t3P0+LYdHXx5kKfpaO8O56/f5peVx/2t2tF9H6u+XqgUv3dL2IPt5+Xi+idnH+'
    '6X93xuKbVe/YVLaDsxzg1ShN/Xt3/bg0n370sDNnXbfmchqu9qVPozD/VTpdYP+hyQE7oVnB5C2PYw/GbDYczYy1v9Fn7HHc'
    '6dAtnrveedMQttMUrMutcLiBzRAerfxsWXRBG1l06OST99RSfSzlb/J5BEP4eMKAOcrmTR/EwzsOH76cvR/RB2/gpnHvefDj'
    'L+mkj30+nfAhHXj6v7M3DX1u+uEFHru6Vc4CazI5TI0LZMxT12ers32fvQVre4T8tDEjxrTg3e3Nze7dp1//tLv79P7m/T8t'
    'z4RBg1d+ibFEyu840hw83dqz9oR76OCIrH4cXOUX94YF+KrXvzG/6z6e173b1P7rtEmAedeYjzMjHCzcip8BjBG4J3CvHpe2'
    'ZSbzPsx7m/UxHUDg2BsGKXNV4KfsgWws0Kf0gcwjEO3HDn80bnLRgYoHVbJ9lQ1EffN8/omn0+f6KsBT+jjoLRvOAzDup0e2'
    'xmC++VvghNiWefusx6WmKsHNntmw/va08U+T731gQ51jAHvbZRQgIFk0NdjF1nfFMTQnuJ1T66BwDWaGQCdUJ10MQwwEhDOG'
    'l0bxbmTg+nRc940KeJnzaGosgLdE85/eCJoNUTJPyPBwqy1/NAWoAZxmAYAE56IjMuSAhqt06Mm/xtL+7yBn3x777bEmJhVb'
    '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'
    'ojl94A9vhT5N9Qfu/wc20dTF'
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
