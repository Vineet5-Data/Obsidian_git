"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vG1mS/C8682CSstvem9quGQujtgxZXmK2ITQamFkssJg99O5tsf99ZUkki5WRkZH5XlGUxzfaIqve98uMjIz89X/P'
    '/v33P/7x9z/O/uXXs88XX76c3S3O/uP3//rbf9//x/3Hf/z+x3/+/X/uP/969vHyZrj/K/3w89e//nbx6fKXi6uzxdn7683Z'
    'Ymn++8vHYfh8tjjf/uHLMHy4/+/Nx+Hi9mzxevLfvwxX159G//355vrD1/e34x/c/d/ioBeX7//y9fPo/bv+/Hq2Gb7cPjR0'
    '9+Gpz6Of7do37r73jqdGHL7l0/XN7ceHh+4/2fc8/ZS+56mZ6rN//np59eG3+3/efv02IeTBk2/qrb+6eD/sBokO0dM3v83C'
    'wfPv//Dpdjezznv+NF4U7DWHXzyY64vb4cZ7/vuLYIAev4DHZduD7UtHz336EhuXySZDj9s3vTC19gX7x4Flr0+ofe7uaf6A'
    'yBNpH//l+uvTgIPxCCfQH+f9wrPDUZm/Uev8cWiav92pZcehZf6UAWmYP2lcKvO4/S0YjscO1B63X2/T/6o9zw5vl9XAut+0'
    'GrYPGS46LgJlNDqvgccPicchOye8DsKV9v766mp4f/vbn4ab28ury397aKa9T1K3f+HaQs0gD9jecqmGgreGDQ1GJ9ns7d7t'
    'OUGVzV8/MH785MdPTugnh2fil+Hqm+s22imPHhn2AI2P9uYu5T/trJD45PHNf+tnLWpHmfGHDocGdnh5lzxrJv1ouR32l2Kl'
    'oeD8h21XWujfJbiN8c/NMIWH/NY+6DxMYPDxKFUaOLX3U4tg5DUVXm0HuNCE/QCbFsjjC6bNGeCwgcyzLBylZogKz9iNkP2t'
    'OkLgoXiAyrfFP8tvq1fdwZ13iGIuJ//95fbmYvPzcHPz17PFungZTj50vxR7XY/Pc1G2Xplb93Q0U609kVyxBQAqy1eqfm/Y'
    'xpmB/XD5Z225ha5cMMb1WwJ4feEYN3ensCHBrI2uIDwqsScp2Ue7fpeet2+li353MjLJvhZMEGstuABRH2tvAjgq1w5r5ARy'
    'a7n4fjykz0ParIImf5ecidNg6Y+bv5ez3Nb4pD9YbLM5E4sOmuNGf1u9Fzf/WrjNwGCSa6IMOSQMHPBQEEaruMhTB1tqztMB'
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
