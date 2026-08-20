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
