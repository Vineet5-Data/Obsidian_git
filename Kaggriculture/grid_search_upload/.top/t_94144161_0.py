import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXctuHNmx/Beue6F+sukdRypfCeYMBYpyYzxoDAawLwwYvou53hn+d8tkP6rqREZG5jnF5hjctVrNqvM+mZGRkT/98+p/'
    'f/n173/59ep3P1199/XT3YefP99+efz60F3tZ1d//eX//vz/3/7n28e///Lr3/7yj2+ff7r6+Onpf7UP33398efbHz59f3t3'
    'Nbt6f7+7mi2Kr7987LrPvf/40nUfvn29+9jdPl7Nrkdff9/d3f9wNZuffv754f7D1/eP57/Y7Pf/mvU79vnT+z98/Xx+07zX'
    't5+udt2Xx6e2/nD/8Pjx6dPpq9GH4UB86e7uzm9djt96fFzvVaAh/deeP42nAjVg9Dpz9mAPTy15mpP5oK+HX5F3fb67fd9Z'
    '44n6c/wD8LZRu8lbD3/SH8+iHU/f/XBeDIO+HmbK+Jk7wt3t+P3n5XH72D2MF9H4u+HqgUt3MV5EX+6/jhdRuTh//5+dMfhm'
    '1Ds2leXgDAd4NErn/r2/PSzN44+ed2av66G5PA9X+dLjKPR/5U4X2H9ocsBOKFYwecth7MGY9YajmLHyN/qMHcadDt3gueOd'
    'dx7CcpqMdTkXDjewGcyjlZ8tgy5oI4sOHX/yji3Vx1L+xp9HMISHEwbMkTdv+iCe3nH68O3s/YI+xAbuPO41Dz78kk562+fT'
    'CW/SgePf9t7U9Lnuhws8dnSrLA1r0jlMAxdIm6eOz9bI9n3xFoztEfLTwoxo04L393d33fvHn3/fPTx+uvv0p+GZ0Gjw0i8J'
    'LJH0Oyaag+Ot3WuPuYdOjsjox8ZVvt4HLMBXvf4D8zvu4yrv3br2X6VNAsy7wnzsGeFg4Wb8DGCMwD2Be3VY2iEzmfeh31uv'
    'j+4AAsc+YJAyVwV+8h7IxgJ9ch/IPALRfqzwR+0mJx0oe1Al21fZQNQ39+efeDp1rq8CPLmPg95ywHkAxv35kaUx6G/+Ejgh'
    'tqXfvtDjXFOV4GYvbFi/Pa390+R7H9hQKxXkzhsGtq1QHs5DGH0+gsW/nXoP9wipkY5DdtVKh2TGfji9tXdgxe9Ose01nQsN'
    'IULWq+4Eer9WGRv0os0MC7djTCgy4jR57Q+YTdTyICZDwh6ji/6M+rnYKEGvnMHwIcPIwTuGsv57gKu3x7499jf4WB3AamHq'
    '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'
    'JCkOxtelVdPvqZ7wqiw7NYODcVDdbsiA1k0o24N63Yx0T82DgOZcLGIkLzfquRFWrUSAiKnUFOuFuTK0IdRVzbFYmVZVyXth'
    'mQSU+w10JZosEQDHIYkSysWYeIFI08DIVdSfYAuH8xwqFw5oMVvpNrVd06WEg91Ns6jKPXzuR1HdXRC9pOcocSvqlxWhLDn5'
    'Ekrz3FpA2KYwAzEzqU8KS8Rf75wfVrugsjsIgzJa7o1ZOKlikQVOKXc/sBbzBCwbcQ2POaHAcRxSUG9zwIrmF114tbK0onAH'
    'I+sGtkvO4lLqnsZnJl4gh1VewAMvYSgvu45iIFDlh9AaCQM/Z5BH0o1rAP40wnc2JkeE5qRNAfUAzAeK5xJduP6ob6vVSE/H'
    'sZ73kWdgMCTXbzzM9CgP5TJJwoVCnHCnJgscvgnLRXGejKbYjBliyPnVXiv1cWfAJ8cZMkQjJQxCjbpSVM/BPdVMs/U+wxrP'
    'Zfwwznskz56pE7A8JTWpPiDRR1IWAKbCAQVZeLIMUOdE7HgGi5KwRBgcQo6jTogQoSc00uXw0ch8JnQi5cX4qSzt2HJgkHqw'
    'hnpBRsaJObiYKoe/5TtkjGg0xd6Y/oLjmFvF6bCWj7g/1gE0RNTB4LoroOOiqsMignfwjasr/Glaj9KyYCgg9zq9VWxTumL8'
    'fLKuNNYEAIhz6vRisSjhOJHbzg7K7HKkgHkQDmmDOXRKEVhB2tn/9cu55vN5n9f2lA68LZlu1xcTb9B99vVl+BnMnOXeO8g/'
    'jSTNx6kZpQler2lQuj0FBEEcolp1c5jG4uk7UIZAMAMhhubUFxxSZiLj/1fCQox9IQmAsL2QTQApV4kqnkCtg0RtHJoNxlAF'
    'nZvCKSuVnBo3YU0d1/IGTFbVmr/b67zgcr2yAWa3s2NEgPt1tW/kr6oSIEegYHDJv3Org2LjIHC5KMqMTuqgnY8Q4oPTlEuO'
    'CVC7MVAeizUKFQtg4AkycF0hqAxCJ+IU6mZPDZzmlkpwjko96tqUIRBvD7rqWg2ZGD9WnGCJ4J+r9yM2ibZNrH2c5OewOmnI'
    'bUbtkhz9XU3yHH+/+p2B5pTgLEWRc6H7OI9DBAf0GhMvoL0YaEzOx78xfPxV4eJvLuK2r3XJ14Z+uQFoeznflR5RJP4G0xnb'
    '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'
    'vwEUGLMT'
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
