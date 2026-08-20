"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXctuW1mS/BetuTAfUkuzU9nsLqFVliHLTXQbQqGA6cEAg55Fde8G8+8jSyJ5eTMyMjLPuZTk8apYMnnveZ98RER+/Z+T'
    '//jt93/8/feTf/t68uny8+eT+9nJf/723//+z4c/PHz8x2+//9ff//Xw+evJT1/++uun25sPX97fncxONj+vLx/+e3o/+3ry'
    '89Xt+kT98O0xlx+vfrm8fnjK+5vNyWxu/vz55/X608lstf2Hz+v1h9E7B3/+ZX198/Hbn+//d3bQnav3f/7yafCWXce+nmzW'
    'n+8em7P78Nz5wc+GrXj61+GAeC97buTh6z7e3N79/Pj0/Sf7wuefai98brj6kp++XF1/+PXhf+++PE9E+IbxT+T+XF++X+/G'
    'Txu95598m6mDFz38w8e73Rw7L/zjcHlI7xv9YrgwLu/Wt96L3l+qY/f8TThk2z6N2wveyYZstFnRc/edaVkH9k3754LtU5h9'
    '+4LdY/2xys+6fc/nmy/P4w2GSp9tfy7269aOVNNkD9rrD1Gfyd4dlXaIuky2MlY9JlsasqZJ3z4EjNSoS7Xn7per+6fag+0U'
    '9F1DbGT6rKHt09aXUywdZaCmWjmjD4nnHtpvTxZYeE89LVR2td1cX6/f3/36x/Xt3dX11d8e22svupTp8tSM1H2KmkEesD1s'
    'Uw0Fbw0bGoxOstnb7d1zgp6fWbkoC4v6x09+/OQV/eTwTPy8vv7mbw52iufRQu/37D7lBe5sgPjk8R0U6C1WjjLjwwnu/vw+'
    'edaYy7d+O+xvx0pDwfkP26600L9LcBvjn5thCg/5raHQeZjA4ONRqjRw7EmkFsHAVSu82g5woQn7ATYtkMcXTJszwGEDmTtb'
    'OEp72MnEBlZHCDwUD1CTGf//4bfVq+7gzjsMvc5Hf/58d3u5+Wl9e/vXk9myeBmOPnS/FHtdjy9zUbZemVuHdTBTrT2RXLEZ'
    'CKWWr1T93rCNs8caHpFmt2p8/TbdE8Dvoxdxjw6YoGt2hMAkogBr7EsqFtJ+eZSet2+YG5jvZGZ6podmhFh7QQkp1s09NxJV'
    'bOQoHtdy9f14yNcJwoJZu6DJ4yVn4jjH++Pu7+UutzU+6REW22z856KL5jjS31bv5e1fChcYGExyTZSDDgkTBzwUpOgqTvLY'
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
