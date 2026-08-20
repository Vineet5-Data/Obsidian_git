"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vXMlu/C96ngfPjKy186a158bG1VqGZGdwsxAWC+QGAYKbh03egvz3yLbm67BYLJJ9JNvrp9XKozN9utndZLFY/PV/'
    'z/799z/+8fc/zv7p17P3l7e3Z3eLs//4/b/+7b/vf3H/4z9+/+M///4/9z//evbm7c3m/l/pDz9//Ntv72+uX3989eFscbZ9'
    's7m8/+/z3b9cvnv7y+XV/T+8ut6eLZbm17dvNpv3Z4vz3T/cbjavwWMefv3L5ur63adf3/3f4uQt3r7668f3R9+yf59fz7ab'
    '2w+fB7r/4eGdj/5sP4rj1/e+42Fsp9/y7vrmw5vPDz38ZL/n4U/p9zwMU332zx/fXr3+7f5/P3z8tCDkwZNP6qO/uny12U8S'
    'naKHT35ahZPn3//Duw/79XO+5y/HS8++5vSDJ2t9+WFz4z3/1WUwQV8+gOdl9wa7Lz167sOH2LxMNhl63GHohaW1X3B4HDB7'
    'fUHtc/dP8ydEXkj7+Nvrjw8TDuYjXEB/ng+GZ6ejsn5Ho/PnobV++1PLzkNn/ZQJaayfNC+Vddz9LZiOLy9Qe9zB3qa/qj3P'
    'Tu8Qa2Cv37KG3UM2lwONQJmNwTbw5YfE45CfE14HoaW9ur662rz68NtfNjcf3l69/dfPw7T3Ser2L1xbaBjkAbtbLjVQ8K3h'
    'QIPZSQ57t3dHLlBl89cPjB9/8uNPvqI/OT0TbzdXnwK0o53yJRwTI8CLu1T8tPdC4pPHd/9tnLWoHWUmHjqdGvjCy7vkWTN5'
    'j87tcLgUKwMF5z8cuzJC/y7BY4z/3ExTeMjv/IPB0wQmH89SZYBTfz9lBEdRU+Gr7QQXhnCYYDMCeX7BsjkTHA6QRZaFo9RM'
    'UeEZ+xmyf6vOEHgonqDybfFn+dvqVXdy551ilcvJr28/3Fxuf97c3PztbLEuXoaTH4ZfiqOux6e5KLtX5i48PVqp7ptIodgC'
    'AJXlK1W/N+zg7LGGZ6QdVk2v39Y9AeI+ehGPeAEDe2ZnCCwiwjrjWFLxkA7mUXreYWAu/j3IzfRcD80Jsf7CBBNsXbb24HAB'
    'qOIgJ6Bb5+r78ZAxD+n5Ba2Il5yJ06Toj7t/VLjcG3wyIiyO2cTPxRDNCaQ/We/lzb8ULjAwmeSaKIMOCRcHPBQk0ipB8jTE'
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
