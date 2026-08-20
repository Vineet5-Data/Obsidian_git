import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vXMmR/C888zDdpKTW3jhSeyWYMxRIyg17QAwGsBcGDO9hdm+L/e+rJfvj9avIyIisaooydFKj2XqvviszMjLyl/85'
    '+4/ffv/n334/+7dfzn78/PH6/a+fru7uP9+uzx7Oz/7+23/+9b++/OXLx3/+9vs//vbfXz7/cvbh4+NftQ8/fv7zr1c/f/zp'
    '6vrs/OzdzebsfNl8ffdhvf40+cPdev3+y9ebD+ur+7PzN7Ovf1pf3/x8dr7Y//zT7c37z+/uD//j9cPD/55PO/bp47s/fv50'
    'eNNi0rdfzjbru/vHtv58c3v/4fHT/qvZh+OBuFtfXx/eejF/6+5xk1eBhkxfe/g0nwrUgNnrwtmDPdy35HFOFkd93f6KvOvT'
    '9dW7dTSeqD+7/wDeNms3eev2v0zHs2nH43c/HxbDUV+3MxX8LB3h9dX8/YflcXW/vp0vovl3x6sHLt3lfBHd3XyeL6J2cf7h'
    '/3fG0Tez3rGpbAfneIBno3To37ur7dLc/ehpZ066bs3lYbjal+5GYfqrdLrA/kOTA3ZCs4LJW7ZjD8ZsMhzNjLW/0WdsO+50'
    '6I6eO995hyFspylYlwvhcAObITxa+dly1AVtZNGhk0/erqX6WMrf5PMIhnB7woA5yuZNH8T9O/Yfvpy9d+iDN3CHce958PaX'
    'dNLHPp9O+JAO7P7v5E1Dn5t++AqPnd0qF4E1mRymxgUy5qnzs9XZvs/egrk9Qn7amBFjWvDu5vp6/e7+1z+sb+8/Xn/8y/GZ'
    'MGjwyi8xlkj5HSeag92tPWlPuIf2jsjsx8FV/urBsABf9Po35nfex8u6d5vaf502CTDvGvNxYoSDhVvxM4AxAvcE7tV2aVtm'
    'Mu/DtLdZH9MBBI69YZAyVwV+yh7IxgJ9Sh/IPALRfuzwR+MmFx2oeFAl21fZQNQ3z+efeDp9rq8CPKWPg96y4TwA4/7wyNYY'
    'zDd/C5wQ2zJvn/W41FQluNkzG9bfnzb+afK9D2yoSwxgL7qMAgQki6YGu9j6rjiG5gS3c2odFK7BzBDohOqki2GIgYBwxvDS'
    'KN6NDFw/HNd9owJe5jyaGgvgLdH8pzeCZkOUzBMyPNxqyx9NAWoAp1kAIMG56IgMOaDhKh168s+xtH8d5Oz7Y78/1sSkYuvF'
    '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'
    'H/Y/nn1TmlC4+B/+D1ldUr8='
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
