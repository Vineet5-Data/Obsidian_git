"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vHMmx/C88z2FnhqRE37jS+IkwVxRIyoO1QCwWeDYMPPgd1r4Z/u+mqPno6YyMjMyqHnIlnZZLcaarq7KqMiMjIz/9'
    '++Rvv/72j7/+dvKHTycfLu/uTh5mJ3//9f//95+Pv3j88R+//vZ/f/3X48+fTn78+PMvH25v3n58c38yO1m/W10+/vfsYfbp'
    '5N3V7epE/eHz11y+v/rp8vrxW97crE9mc/Pru3er1YeT2en2H+5Wq7ejZw5+/dPq+ub9518//Gd28DpXb/708cPgKbsX+3Sy'
    'Xt3dPw1n98Pm5QcfG47iy78OJ8R72GaQh497f3N7/+7p2/c/2QduPqo9cDNw9SE/fry6fvvL4//ef9wsRPiE8Ufk97m+fLPa'
    'zZ82e5uPfF6pgwc9/sP7+90aOw/849A8pOeNPjE0jMv71a33oDeX6txt/hJO2fadxuMFz2RTNtqs6Hv3L9NiB/ZJ++8F26ew'
    '+vYBu6/15yq/6vY5dzcfN/MNpkpfbX8t9nZrZ6ppsQfj9aeoz2Lvjko7RV0WW5mrHostTVnTom+/BMzU6JVq37s3V/dXtS+2'
    'S9DXhtjM9LGh7betLqcwHWWiprKc0Q+JS+fQf/vigYX31BdDZU+5ub5evbn/5Y+r2/ur66u/PI3XXnQp1+XLMFL3KRoG+YLt'
    'YZsaKHhqONBgdpLD3m5vYysNQyjb5/ePfP/I7+sj/ES8W11/jjYH+8SLZ2Hse/6QigF3HkB87vjhCYwVKweZieCEYH/+kDxp'
    'zNVbvxv2d2NloOD0h2NXRujfJHiM8cfNNIV38NZN6DxNYPLxLFUGOI4jUkYwCNQKj7YTXBjCfoLNCOT5BcvmTHA4QBbMFo7S'
    'Hl4y8YDVGQJfiieoyYn/Gj/b66o7uPMOgdf56Nd397eX6x9Xt7c/n8yWxctw9EP3S7HX9fg8F2XrlbkNVwcr1fomUiA2A0Bq'
    '+UrV7w07OHus4RlpjnrH12/TPQGiPnoR93gBA7lmZwgsIoJXN79r9JD25lH6vv3AXFi+k5vpuR6aE2L9BQVQrLt7Lg5VHGTH'
    'q+/7l3yaABTM+gVNES85E8cZ3u93f69wuW3wyYiwOGYTPxdDNCeQ/my9l7d/LlxgYDLJNVEGHRIuDvhSkKCrBMnjEFsazibd'
    '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'
    'sZKJmTp2O9x8D/8FwvBUeA=='
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
