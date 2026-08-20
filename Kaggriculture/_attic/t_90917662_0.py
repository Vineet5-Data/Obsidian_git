"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vW9cR/S9acxFSH7a7U+yXWIhiGZJcIjWEIEBTFCjSRdpd0f9exabIxzczZ87M3PtIq16Zpki++33n48w5H/9z8rdf'
    'fv/t199P/vTx5P3l3d3Jw+Lk77/886//enzj8eVvv/z+j1///fj648nbq9vh8a/ci28//PTz5burHy+vTxYnr2/WJ4uVePvu'
    '7TC8H/3hbhjePL69fjtc3p8sXkze/nG4vnl3slhuP/7+9ubNh9f3u2+cPzz8d7HXn6vXP3x4v3vSctS3jyfr4e7+U1vf3dze'
    'v/30avvW5MX+QNwN19e7py7Np24/MH7q9q/jQbm6fvPz4+Dff9iMHtcOdRBEczY/oTVhNyz2I3NjAB66+cpp/55Pf33Umt2U'
    'K5M/fWv87OlcX1++HrYjufcI2TftoeIVeNh34/2xP7ibZvyxpv74rcf/v7vf7hn9nciTX19OB3DSlsehurwfbievnh66+9Sk'
    'GWhkJ2fRthHjlg+Xd8bTQ7+8+0E5TNtHbF/c3Xxwhks+QVno2xZvf7jtcE3XRPNRE0tAtl955ucXuYnftRfNWGXQ5PEzOgxK'
    'o7VZNcw0L8afTowXWmxyc7YZuOlB2GEEifUm3wHXSGbdoeHLnAubd0bt3L1jPSr3AGWwtn+aPDLZg117xQ9/fhH4XfRRYF6B'
    'rz2tQuaz1kUbuCHRR2+ur4fX9z9/N9zeX11f/eXTqLXuwhztmRp54KNP59nXppebHtkqXz8KPdqNEzOagsWZ7c4G/M3NB86g'
    'vxnZ6aFv235CzeaH32adMrzuYzZCr2GKtEEOUwPPteUgSVect4nE2Rd7tD3CO/vWbYMywKgJrYZ45yR5DVQGODBGyhAHPM3u'
    'a1i6H60GeLQEEmbn1H1OenlzP7lgakeursS9FDtmG1xCmaunxzrM3caFsy9/4nW5StLHW/De8J7jHmWJA6zj3RsaMf8gt2/a'
    '1JC5R9Osayzs/j+nr2RdjsmLkqvB5FOm2be4rb3o5aXEfphwXJwf7GamL5p5gXZ0tXAnGSH2t5e3f47fWVMTX43ab5qSjpMo'
    'ZmRwTJD1vvvtaSIjc/cZgeTStMlltZ2s9MRp8Xo31F6YQe2MKvm3Wgd4dw76vNpqK1g248na/eDeu/H5k3MFMoy+ZZI65EqJ'
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
