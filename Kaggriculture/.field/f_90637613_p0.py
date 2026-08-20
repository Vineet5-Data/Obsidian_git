"""Pool route 90637613_p0."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vW9cR/S9ac2FSH7a7U+yXWIhiGZJcIjWEIEBTFCjSRdpdkf9exabIxzczZ87M3PtIO16Zpki++33n45wzH/538o+ff/v1'
    'l99O/vLh5N3l3d3Jw+Lknz//++//eXzj8eWvP//2r1/++/j6w8mbq9vh8a/ci2/e//jT5durHy6vTxYnr27WJ4uVePvuzTC8G/3h'
    'bhheP769fjNc3p8snk/e/mG4vnl7slhuP/7u9ub1+1f3u2+cPzz8vtjrz9Wr79+/2z1pOerbh5P1cHf/sa1vb27v33x8tX1r8mJ/'
    'IO6G6+vdU5fmU7cfGD91+9fxoFxdv/7pcfDv329Gj2uHOgiiOZuf0JqwGxb7kbkxAA/dfOW0f8+nvz5qzW7KlcmfvjV+9nSury9f'
    'DduR3HuE7Jv2UPEKPOzb8f7YH9xNM/5YU3/81uP/395v94z+TuTJry6nAzhpy+NQXd4Pt5NXTw/dfWrSDDSyk7No24hxy4fLO+Pp'
    'oV/e/aAcpu0jti/ubt47wyWfoCz0bYu3P9x2uKZrovmoiSUg268889OL3MTv2otmrDJo8vgZHQal0dqsGmaaF+NPJ8YLLTa5OdsM'
    '3PQg7DCCxHqT74BrJLPu0PBlzoXNO6N27t6xHpV7gDJY2z9NHpnswa694oc/vQj8LvooMK/A155WIfNZ66IN3JDoozfX18Or+5++'
    'HW7vr66v/vZx1Fp3YY72TI088NGn8+xr08tNj2yVrx+FHu3GiRlNweLMdmcD/ubmA2fQ34zs9NC3bT+hZvPDb7NOGV73MRuh1zBF'
    '2iCHqYHn2nKQpCvO20Ti7Is92h7hnX3rtkEZYNSEVkO8c5K8BioDHBgjZYgDnmb3NSzdj1YDPFoCCbNz6j4nvby5n1wwtSNXV+Je'
    'ih2zDS6hzNXTYx3mbuPC2Zc/8bpcJenjLXhveM9xj7LEAdbx7g2NmH+Q2zdtasjco2nWNRZ2/7+kr2RdjsmLkqvB5FOm2be4rb3o'
    '5aXEfphwXJwf7GamL5p5gXZ0tXAnGSH2N5e3f43fWVMTX43ab5qSjpMoZmRwTJD1vvvtaSIjc/cZgeTStMlltZ2s9MRp8Xo31F6Y'
    'Qe2MKvm3Wgd4dw76vNpqK1g248na/eDeu/H5k3MFMoy+ZZI65EqJnq2TJHOvzIqmchTm0k5mV55eKDNa/EUrcVM1QTaX2ur84zLw'
    'zBJpISz7e5kVnyF97h2Njzm3j/366rtO5j+9wxr5mpW4GXEgWqZOxyhZaMw+NTA2ZFo7clCkFi4VO3pfst84l6v5ueWwSp7gHF5f'
    'xPuwj/2DprCAtXwcKaxAiqSYw9oZdKkMGpUCy8Q3gfvRNjRc9qL9ZUy4zOEZauGetZqijvbBFMuZTGXVsGudcllPjsrNzeM/y2dP'
    'bsijNfm6QD/YeDF397eX62+G29sfH3/7pYnxWD1kXDbFoJl4XSyPInFHKwwDGTaUrrV8QZ8sKyJYPG2z0S6JXZXtCuDzeTNCj1Mq'
    'AObA0337A3c9+PSG/pqBHOdG6MnfG22xtMkoQL/akzmqReRGsteNwkIID4Eyoal5BHabEgvHkXJ0kfRaWFqLACXIGNT0cpNGC2C1'
    '7NoqkfyTJ+fioJpTfjk9A+E4BfMW7KyGskbWLRKevgaoJWe8ArPX0YBTSAbaYW/mD5PmudosdUaNYXJ3gfF2KX+m5BTdhmrz6TYi'
    '4Fgb+037Kzr0AyQ1aTXBsW6x9fIBOcD+6TZ7yNORRBuYLqyhFC3XAEyJ93f0tVZtU6g86pQdCAqDHb1lwJeTPgnwWM4SdGEtcXbx'
    'wCO09325ZZambB9nklQn6VVZvrK8oKVBQ5rn7Iy6t61+7RURRwiCgM+/iicyTjVPLWuFRp+wp8TikPYxQC90tZa2L5Bd7iccN+sw'
    'YBipCJBanF/jmQ4sXVrO2nhd8GYesT6cuWEWxzoCTXKZKwsKrISesPmOGvPV9nDEHCDcS+eYcAdINh9CzXgQFAU93DuAaKov3ArC'
    'ojXpyrFhwacw/9NqrkFBSuZY0FrYFFiQlQFp8rsRnNHyuYEzuhi9/8PV9fdPEj8hMzAWL1/6kWlTuSJm+Rmm6RRJtWDvR3lfSVNR'
    'N1drOjfoPKBONbshxXgwjMeSdms9ErazS4wLlwFJto4Gu8aumVWYCx9vLiGInI+Yz3LD7JlHl2aSyYavZ0aCWsn80skZoco1gDSV'
    'lCDq7rklK5+2urPromQBbvut+BiadBLvYcl+757FT77ZhmQ3QXKYog/xnQTLtocpL1HjuiOXM+8RcRusWyLsmAUzydNs+7CP2N5F'
    'FTe1/TljtcrnKoJMbeZWWqsj918GLUswGd5WroVHg0/K2+mzPUh3CD7ieV6MET4jSciK2c/a/yuAl1lyiqAhqcqkEGpC8dTX3Vzl'
    'fAWmswmCZ9B3SLQC8dtI38FGvfQIUbN2IRVYrueJ0RCpXMMIibSB46UPjt4aRhaV+maSCEtFSEFrHXJZL5gOgiismVFmBIQLIRDa'
    'kxqAQ8OJohb8PWUnrfHmCWyj9GgCEI1qNeNFGd48TdcBuFZQlih4GjRqvrZC9GWrbD/sSFkixrmWrx4yuQFtwFFkwW/hih9bmNbR'
    'xu717c07DhattnDPUEuPKw3SEqtb+l1o0NsONcAu2I7Edry3L8T8oIFenUUG+rRNm5HH+akb0bVxWhnmkZZGrs0+SSEwpDAuEWrg'
    'dkWA9rUZUzWXx2Twok5yYVzbeu5U6wIjSLn72mR9yvNdgF3MkHxY77/FGBZKobDoNSMKMCYqrU4bQNhgvEP5o0/AWTgQXSPATBjW'
    'KazcuKzJ9M2V+clYNy24KgCoFEDHLkrvTHtzZb6pdBGHW2S2A+BkipBAWUoAM1ccnA4V+D8k5FBMLuDAAbgkg8nXrODI9HFAx+2U'
    'KkUh4vPnIcRZ4HjbuJMPjbSTQSwkHrId2mAFJZ5SZj8pck9g6ZmxI2KGzhrtPuNtqoqJHSliVmNwFfMgZBQPCR02ODqGYrwUVKGI'
    '97EBQIC2itE37J2u5LEL8tjEXgTTBifJ4/1kV6MS2aV37qrvzlWy4MF1ueB0GkvMaxQ6U5LngI+DgCiBy38S+IjtTTWoGsqVD3Ot'
    '00z3tHpTk9shiQwIr7gSwlf2I9Jq+lBRCL/Iha4JfO2d+6lAiLKBMpS7Xr1L7ijZPSdV0ARDMq0+WWuxt77Mocm1vrY9PL5mh9U1'
    '2xYJ0UCbboR20bZSuMwOoCgBs3EkJs0NZQLrykGrtcEGG7RRmANurW2jl6A0ERvaboIHDsi07LSVces0MkwmzeeXPGSyjgKi6AP5'
    'JWYTBiJBllyEROUNUKCOGeMaLBQmsL5K6r1iwDDjsRgsWDu0VzE6PnalDVPSPpaAWHuN/ukMBaxtWyoqpwTKPLg4j+bkGK+Kf0sF'
    'HQPRbju6C4NmieID2nhqZ1KSpIy4st4EBqJSSbUWK04rLFw1b19StSRs/Qw5OffE1h7bn4peMGYbczCE518A8uAwnk+MVYbKgGru'
    '0dlDQCxsF1CADUWMT0KJrSY+KofLziPCgkoZph4h+EL5dOjedZIwaYVZWigm7AhCDc3ggDeHfmYcRKxO11jukFjzcUAEi3qwT5ja'
    'LrCNPSTdw3L++dGecRdA6UmAAygkBMmqJNXGs9OST+2iS6n14o9NRU7+KLTq2TMmP7xmeVU9DRyWwNKPFOhUFYgJ2qTyN5NOcY9K'
    'jGScewT4BPXmXCX67HLVJs+OH0Idh4GAeQR8WDvTJMPicjt7HvC6bbU5mTLCHEWXaVBtD9t9tQKf71G399QHXwNhfmdbYYsE+Bnz'
    'hTPmCBDshQMUJtHFYdQHZsk5NnOfmexiUwc5lFMs1MaI+MRdc4otjf2A6m2fbKJnyBvZRNsDn9c3DaC9I4ZWxPWUKUeupnizjHV0'
    'dQV8s3Tl0cpCw6ESkPVsQI3N5Cc5gYK22UnTOp7f+ZHHfQtALsI9SEYEm8b0TV9lXrzHKH7WiIC80fdK+fwSeQySmmO4fbUuNTT2'
    '4vqIXYCY5YzNoVvw9UFfZp7TdGNGWc0uYmpzUNK/1KRmM3SnbhlQSp4tEpiRRCGwlQlKbjGjScL3cF6pURLzSEB+cMnWxp8xpyiv'
    's0v6rELvTTuG2M1onruUZjLlOLYf7FaLnahm0j+FGUHpBYt8xBd8I5HgyNJVzoImOWDGR/T8Iri+w6/otCSB4VCWXZDUOhB8+1Sp'
    'Ogj79BGsGTZjTV0CCstRCgVtEo5UmlFNQSmpPakvH9jlitSvzPaw1xaSzAY5rrY7HWWrZF5SIaYCtbOClQAcHq2hXsIylkUtpSmT'
    'GnGdfOTjak0pBXk4+PLZDNWSOgbDPp/cqfINUalU/csF/ks7HmjDTK3a3FPDLeEJSt3yu0irDRVZPpYsMGr/Z5wr3p/Pzff3V1Wz'
    'ZG77HPMIgm82nQGHH1tqes0pi489WG/q5sxpK1sENDAj+3awXDhGL8K65KVyCgntcXb/g6lhthX4DM9DxsV2/TATl3Xfe5VdkUS6'
    'Xjuf3C0PtpFyHJQ8YqgAKS/xsdvca6lkqL3KoVSPNmZXClUdGaGhaagCWQxSiQpUamzLUwUrkyoN6b5EpBsU526AjZntXCB9R3m/'
    'MnpiFPEAePBAxpNxLqkycoPErNQWRIuW5xSTmIa1amFVCQpd0PPiJ+YIxowjLG0Y4scNrziWMAzzwgr1e6GVVQcOOSWDT1y10crz'
    'wLobn+JYSLpN+2wPVhcpGb8L4IZEZepkgwlHNSA+jN22oIB914iP8sLzTjnWn+VCFUDpfJCni60OcRpieBoFQqkqZmtC9Sc2JfHd'
    'AXdwPBlvH/A9RabreoGc2BTcJEfIlo8WJkj4hW1p8mDwkYKKU+AvxEBuuBlcwFLI39ZOcnp92weevgvKI8pz+MngnPZKKTyHS2uO'
    'yzAxMkTGgAD8DkoPoXo2pTrqrtQagLkow8/ck2WsnQwU2E1DUS1Ek+aLqiAgiwo6RmUwUYyAFLJIBoQ4Hj3A2iD0TSlURTQiBuaY'
    '7n13vy+f1ZTb60UFkS2UR5ns1dEcd/jCgJ+8ZMTzTg8W//hMpfI0T5DRDs1GN7IC4uUG99UW55rXRySghdAW2exjViXHWeJSZ/pJ'
    'liuXrx6yimCZM6Lm0KFGqTsO/JTjSmWdGVJ/vfPSDW9HzkXMyryHiti3kejT48CV7K3rMrClARjiQLLgndp9Sq7amW3XHYAQDuYa'
    'g7QGfTb9zQ7F8tmAcLZ4WhaqQ1C/kKBbZt9GHGbFw+UoKUaCvRI405oAPHeYnc4w4uRlMtKmeHK3ti88joQ6Una0AaRuXxqOzPnY'
    'bdkg7oM3juKETKzopZdMx+TxJgJ1jMPubZkmif0k+2PS/mIjarW+CiPihxheQNfacsJzLvdR6tUfC/YgUMA+FJbPwwx0KwpkzqL+'
    'Y0vaBpO0bN5ief3oHpw0daAlc3iPHCZd02BzMPwYn0DZTIMJ96QY5jQovh3uQLhlKtjGi47k0J9a12AWpeRv5nkm3NbB1UYxyD6V'
    '34+wTZIFpakjFzjeqQhjGreABVwUIx9l9VOTtGwAVUhRHEj/tM0MJdALgBUBvUqMIikoVlBohuy2wUeBkon35oVJxCPsAwPPgZTG'
    '6DxEIkMKHgEGE+LANTyq2OVYpQrZB5TAlBsPhleUOBgY+c3gqqsCkBFRvQUSFlUb9AW7k1H5AV9Zla7OiDYHwrvkvHY1a648WcMb'
    'cJgqxpwN+cRq/dRITKYT2YMKvqAm9xuyqg7HFG7RMihzembJcDxrr7d5TCocRxedsQUqbHUOiW4Iy3ToeDvtS+c8RGN52rOKIQUn'
    'RPV8+COoQkkJKWA0a3EnQVMmOhTASayHFkl8kPrefcSnTOYEIswsMExadpaSTDK7Yb4mQvxH6b6w7Ea/KgQsfAqlDonC6oEscWDb'
    'ui3Q4m16sJjXomDquDMeYhaSo7xBbNDQCmRUM6uM+/YYHyTvTKa+UYi8MfRHQWTkPDaGTR6YMi8A36BWCsRB8cdUQDchLMURF7zp'
    'AGFyMC1wTas/mEM3QthOznJqtWYRuyICrsBSPApFCcEiKdEbGAPeP//N3yhRCuX1I/3/pIAxirTCbJei/JFATKmeihV0WegVcSLz'
    'Bj6t4KLs8KIeNRyub95+VKVooHulBVcdYBCzU3d9G2SBe2fvljvNlF6VrCLrOqOFeQZGPynHiBSNVZKwyaUq+68EC3FqJlML11iO'
    '23WDAn2uBg2eTS30iCyYPZigVminErlDsWDEClwDhabWZLHN3ttji30ajT1lHJMQdvEVnTYLOg0w360kcVx1OFGfiFAM4wguDeVn'
    'IrKpIaWHGmwN472ErYm1ZhwexjyUskZSqayWjuPklDz2NtVGPYdSN7pQv5oh3DyolL9pgFCf4VLjGB1jb2SodlG3DfQLkBXaOGF6'
    'CbOiHwYRUnjhddHhIRcciW7DMpsp9A7Ee/GwNQ6FKzFRKXDUogBm4wvy5qWeGm8dDWfIFvElZKE9aqid2sxSzYhaW1hDRJxayhLz'
    'xl6Vh+CTTBDY5hcR8/Vz8IawvLbTh8z4p+rAa2XAJACUR7OtiZx7MnGA3EsQy8tFBRAoSS4fj63mOkixsBJqLlNkTINe2TYEtoiS'
    'o8pJe0PsmjJFJVEfWpnQG0qAHpuEHtuK+8AoDSehhHWVwoPq9m8lD7+XIpBjAd3OjGiO2D7zxHPawdiOT/sHKYHa8DfnMxd9GImU'
    'vBo8dUzUnn//ReiJa19PBWLMkPuQKc+bEjaC3gxTmzpU/3BGDVWmmpInN2klA9qUcG0oqVqSWc3X2cwz/jx8lL3KnIq1LaS5owIv'
    '7H4JpOzn5fXZm4ssyMbIlcy0aRI6My3K67TUWs6yahzkL0DtKIclszJzBZzoWnmsBG9AERjV0TYACZGKd2BkK+VhFByC9gD/jne0'
    'noJFgloeXmFIFK2cLl1jHFkLLCel0TzJVVvdTGQkV9psnYgR+pEkfjAxfy5x2NAltBQ4CyHVg2IFmaWSUhDytKwooltuvfgOSCsS'
    'GRYw7rZakow3G/HTq9B6SUbqQIWsRKpI4znK8M/5lwTm+QwKX1F8vmwtrOVFByqicr0Gqx2YPkv3+lhQgweG1m0tv0MWzWIhJF66'
    'oEmsi5MV5rRbXl99F2JXHmX8C0ZQ9u5ckMj1wjQl3EaHiJgXTHqaWT9X9PRJLDhRQkS1KEikZYhQYn7Tq6d/5WdFv0MMIzuUZq9f'
    'NwCozhXDkkRghfxcSsEXHUTFeqooDSDXK3QWs3AFYKCRGjFSndbf1muWNgt7L6dWuV11rd+42qC86hUICrCzlJBM5ABiFH/s2aTt'
    'AwXIoxqenrA5QBTxBxGADcUXNI+HVPWWEYgO2nQtT67QgHCaT+FUgrRMrVCFtm4ge3I7A+jsM9WzQruZlNaANbXsWYU5EV7aV5cL'
    '5VM50Ovw7l7rcMrX/pS+eRJXBjqqUcK2+3oL5ZmcQOLOLdTLpcq509YfVReNOVRcCzFjDjF9hWcjFbIiDaDM+iPisJqBktScl5jD'
    'T+8wIu6JrrCbR+ELV6T0eYTcC/5SikusWYbAC91k+BMorPGDfQR16mxkGsZ6nQa01VZ8QPNlx/J3GkHaaW64rkDTwmIUtozXVWPR'
    '4IWLqmVhPdQzmiNZ6d0hy+/ByCJEEdo15g9ZpM+ZJlb5lYQ+9a7l5we9whY+rfjcvAogIndjn5qKD2Vq1s1VLBCXrwhXJ4+sSSTr'
    'VzovQtJKLpM3pmkYoGQlS3zmCn/i4iSlyXLykWCLUIUdWS1ABD9LzpA2aKS4fUzGDUWB+DNDzhGub6J4YzFhueCngxpRujQNV/EB'
    'R5S1PD8wC3HNFwcX7vUHVkI04QqrkIQ9peVlLbg8NpnAZRCFlQO7z6m1aN9mWbSxqqYLc5PxuK7SahD9YMK6JBhDEs8NxgKx92Ui'
    'w2ZC+jGqZUg2TimP4UBllTATVGNAZFMX/AbbPkpY0NlNTo/LO9z4DuDUAUph7XvGXmzWVjaEcSxcIjXORV3yPNPV+RcQ7ztwxI6K'
    '7pjQqLg4WKKgZVDivyYIlFF0oHBloSoE+WqVmCfJ1x86uuKUGFSUGeRqGUrPJ4QhxCOqOUlZpiB5VttnpWKSGS232epDamsSGeTr'
    'Y6kFyYrmdZO5b7im6RoUPPyX6IC7YsC57QKyQaCnyj7MigKBg8POOITK8QG9M47LGVGso4rvnQXKNeD8AuYw22GIZNmANV8lRCHS'
    'eXDB5Fp0b325ZRS3y4dvZnmgLpsbU+I4HH8sTqJdiCFw0RrXjHAHTLpLitZ4jOam/ED3ZpBkxkQ7MCky9yIOjmpfxHDfDX/xBfD9'
    'DkzqKwNgnEKHZn5+34FfzcP1I0INdm+6E/yoZlYC9Z1KDDr2hIvU6VZDEDcsVq3xOOv/4bSJZjvFOPvzVvKjnP4FzH7OVKkvXWTR'
    'JiDPUXuPUzzOKT60FDvrV22PlOYma0HmqarVenpU5tZRWZn6d402/k5sJ7Dzh5BUdDN5oUhOeM3j3Dx5pObiU6HiIYgBgawnnyKF'
    'XEVFYk3g9GIlrPqdU3yYrUXdgzgEL4HI4BPOSgTTjQzqfjyhFy5XDIz8oGQ4AprldO+BYzg+ZvgNJ/lkBjt90qdcG93IEcUMs1+0'
    '1VHSUDA5MtEBdJPmU0vaFDeTFCRTQGkvlrKX6v6qlNQ0qKLEy0GZDChFtB5CxdFW532qo83To+7l0g7SjXIBNRJDGWz3Z1BPzQO6'
    'e/pCvn3elDWUKbSGRHYwkGbKO3/6N0LQ6FRgDfo3KmGbYJ1jcgFOo+7HqbuUZuO1o1xFGqEyFSAVdSnMhphgpKgSICuaP+pO5XLO'
    'Cm5eSUQOgeD7ShkRZ+USyJRBhKIKtqiUPHn8DGEUz82Vb4O1GqJHCrsKieqICkw+iXNxStbyGmhQn62dMhJCpCCWTYMjB+rmuIsh'
    'fvjAWMua4sDyhT1zR4trEEjUE1E/ckfFAhRZ0iYw1XTWWZDU+UOAROeZcKqaFyfgr2/N6KGkpuaYQ0k5cCdFyEIUFIeIJTvhq4uK'
    'own1FR9Dq5huJja0GQqXZxwoLrcUqrP1e4JHLE6aonKvVNJFCcs5A5EpXOu0CsC1oCTUmqBCURaMPCpJrJXSYhTfVAaZaq64w8u8'
    'qOfGblMAWadnnxEvSnUSjxepharY8dSTBrgqeFia9C7/gHv20KWYHmyu/Vb/0nlsaCsRuptRJ5yNW0GRvaMogucw/1wf8TA179JS'
    'UrPUuMPYKXsrVAR0EmXqOFXsoFPFcw3o6nMUeTY214idk+VJshXTazUc0GAgYxeoag8FmgvTCt7R8uEagZWIODk8GgSFKtZDBl9B'
    '8+8UI5oPqKzjyu1KKE9Y+EQ+JOQV5AApFESCYqWUiqe3ry01XwExho5zDBCSr23oVm9szw9R9D7Onn12eh/8fYWKLbp4idDpjgNU'
    'oMhGs+eawfIWD1ajjWgsHc2xqcfdq89YOCLzcKyqhDJVkecq4FGfrxFWVsxPeKQigj0oTcsRQ1XamOMgH+72zW0dnw1fE3Q7P0eG'
    '4tflcefs5JB6EA4+05lAVIuEzAfzpSsYyJ1/F2UxBcxD7chJXd3tQI9VGqDIg4rP65NvMB0hWUZ5hvJH5TgC6bAnpTeESngKuzE1'
    'Va4vXw27r1xMNQs+/nGUZN5+frcZVK2D8Y+unOSDQm23tlqqfsekOS9k104b9kObiGc103e/GW0GfTvhAe/h4feH/wO8VoOK'
    )
)))


USE_WEED = 1
# Measured OFF: the stationary idle layer lost 0-12-0 (margin -519) to the same
# agent with it disabled.  rayk's +258 on a different host does not transfer to
# this route - the extra output depresses our own premium prices.
USE_IDLE = 0
USE_IMPACT = 1

_WEED_REPLAY_STEPS = 8
_WEED_STATE = {0: {}, 1: {}}

SELLABLE_PRODUCTS = {
    "WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON",
    "EGG", "MILK", "WOOL", "FERTILIZER",
}

# base, equilibrium, scale, below shape/target, above shape/target
_MARKET_PARAMS = {
    "WHEAT": (25, 10000, 400, "sqrt", 0.8, "log", 0.2),
    "CARROT": (35, 10000, 450, "log", 0.2, "sqrt", 0.7),
    "TOMATO": (60, 10000, 200, "linear", 0.4, "sqrt", 0.6),
    "STRAWBERRY": (120, 10000, 100, "sqrt", 0.7, "linear", 1.6),
    "MELON": (250, 10000, 300, "log", 0.2, "sq", 3.6),
    "EGG": (50, 10000, 332, "linear", 0.4, "log", 0.2),
    "MILK": (160, 10000, 122, "sqrt", 0.6, "linear", 1.6),
    "WOOL": (200, 10000, 105, "log", 0.2, "sq", 3.2),
    "FERTILIZER": (100, 10000, 200, "linear", 0.4, "linear", 0.4),
}


def _get(value, key, default=None):
    if isinstance(value, dict):
        return value.get(key, default)
    getter = getattr(value, "get", None)
    if callable(getter):
        return getter(key, default)
    return getattr(value, key, default)


def _seat(obs):
    return 1 if int(_get(obs, "player", 0) or 0) == 1 else 0


def _farm(obs):
    farms = list(_get(obs, "farms", []) or [])
    seat = _seat(obs)
    return farms[seat] if seat < len(farms) else {}


def _aligned(action, obs):
    action = copy.deepcopy(action or {})
    expected = len(_get(_farm(obs), "hands", []) or [])
    hands = [list(order or ["PASS"]) for order in (action.get("hands") or [])]
    if len(hands) < expected:
        hands.extend([["PASS"] for _ in range(expected - len(hands))])
    return {
        "farmer": list(action.get("farmer") or ["PASS"]),
        "hands": hands[:expected],
        "market": [list(order) for order in (action.get("market") or [])][:10],
    }


# --------------------------------------------------------------------------
# weed repair
# --------------------------------------------------------------------------
def _tile_at(farm, position):
    try:
        x, y = int(position[0]), int(position[1])
        return (_get(farm, "tiles", []) or [])[y][x]
    except (IndexError, TypeError, ValueError):
        return "LOCKED"


def _trace_actor_action(step, actor):
    trace = _ACTIONS[min(max(int(step), 0), len(_ACTIONS) - 1)] or {}
    if actor == "farmer":
        return list(trace.get("farmer") or ["PASS"])
    hands = trace.get("hands", []) or []
    return list(hands[actor] if actor < len(hands) else ["PASS"])


def _weed_repair(obs, action, step):
    if not USE_WEED:
        return action
    action = _aligned(action, obs)
    seat = _seat(obs)
    game = _WEED_STATE[seat]
    if step == 0 or step < game.get("last_step", -1):
        game = {"last_step": step, "active": {}}
        _WEED_STATE[seat] = game
    game["last_step"] = step
    farm = _farm(obs)
    positions = [_get(farm, "farmer"), *list(_get(farm, "hands", []) or [])]
    units = [action.get("farmer", ["PASS"]), *list(action.get("hands") or [])]
    active = game["active"]

    for actor, transaction in list(active.items()):
        index = 0 if actor == "farmer" else int(actor) + 1
        if index >= len(units):
            active.pop(actor, None)
            continue
        age = step - transaction["start"]
        if age == 1:
            units[index] = list(transaction["intended"])
        elif 2 <= age <= 1 + _WEED_REPLAY_STEPS:
            units[index] = _trace_actor_action(step - 1, actor)
        else:
            active.pop(actor, None)

    for index, (position, intended) in enumerate(zip(positions, units)):
        actor = "farmer" if index == 0 else index - 1
        if actor in active or not isinstance(intended, list) or not intended:
            continue
        if intended[0] not in ("BUILD_PASTURE", "PLANT"):
            continue
        tile = _tile_at(farm, position)
        if not isinstance(tile, dict) or tile.get("kind") != "WEED":
            continue
        active[actor] = {"start": step, "intended": list(intended)}
        units[index] = ["DIG"]

    action["farmer"] = units[0] if units else ["PASS"]
    action["hands"] = units[1:]
    return _aligned(action, obs)


# --------------------------------------------------------------------------
# stationary idle work -- NOTHING MOVES
# --------------------------------------------------------------------------
def _idle_tile(farm, position):
    try:
        x, y = int(position[0]), int(position[1])
    except (TypeError, ValueError, IndexError):
        return None
    rows = _get(farm, "tiles", []) or []
    if not (0 <= y < len(rows) and 0 <= x < len(rows[y] or [])):
        return None
    tile = rows[y][x]
    return tile if isinstance(tile, dict) else None


def _idle_job(tile, inventory):
    """Best stationary op for this tile, or None. Fertilizer outranks the rest."""
    if tile.get("animal"):
        if tile.get("fertilizer_available"):
            return ["COLLECT_FERTILIZER"]
        if not tile.get("fed_today") and int((inventory or {}).get("WHEAT", 0) or 0) > 0:
            return ["FEED"]
        if int(tile.get("yield_units", 0) or 0) > 0:
            return ["HARVEST"]
        # The engine banks the care bonus only on a day the animal is also fed,
        # so caring an unfed animal spends the op for nothing.
        if tile.get("fed_today") and not tile.get("cared_today"):
            return ["CARE"]
        return None
    if tile.get("kind") == "PLANT" and tile.get("crop") and not tile.get("watered_today"):
        return ["WATER"]
    return None


def _idle_fill(obs, action):
    if not USE_IDLE:
        return action
    farm = _farm(obs)
    private = _get(obs, "private", {}) or {}
    inventories = list(_get(private, "inventories", []) or [])

    def inventory_of(index):
        return inventories[index] if index < len(inventories) else {}

    def job_for(position, inventory):
        tile = _idle_tile(farm, position)
        return _idle_job(tile, inventory) if tile is not None else None

    order = action.get("farmer") or ["PASS"]
    if order and order[0] == "PASS":
        job = job_for(_get(farm, "farmer", [0, 0]), inventory_of(0))
        if job:
            action["farmer"] = job

    hands = list(action.get("hands") or [])
    positions = list(_get(farm, "hands", []) or [])
    for index, order in enumerate(hands):
        if not (order and order[0] == "PASS") or index >= len(positions):
            continue
        job = job_for(positions[index], inventory_of(index + 1))
        if job:
            hands[index] = job
    action["hands"] = hands
    return action


# --------------------------------------------------------------------------
# price-impact SELL slot ranking
# --------------------------------------------------------------------------
def _shape(name, value):
    value = max(0.0, float(value))
    if name == "linear":
        return value
    if name == "sq":
        return value * value
    if name == "sqrt":
        return math.sqrt(value)
    if name == "log":
        return math.log1p(value)
    raise ValueError(name)


def _market_price(item, inventory):
    base, equilibrium, scale, below_f, below_t, above_f, above_t = _MARKET_PARAMS[item]
    if inventory < equilibrium:
        amplitude = below_t * base / _shape(below_f, scale)
        price = base + amplitude * _shape(below_f, equilibrium - inventory)
    else:
        amplitude = above_t * base / _shape(above_f, scale)
        price = base - amplitude * _shape(above_f, inventory - equilibrium)
    return max(1, int(round(price)))


def _is_sell(order):
    return (isinstance(order, (list, tuple)) and len(order) >= 3
            and order[0] == "SELL" and order[1] in _MARKET_PARAMS)


def _impact_score(obs, order):
    if not _is_sell(order):
        return float("-inf")
    item = str(order[1])
    try:
        quantity = max(0, int(order[2]))
    except (TypeError, ValueError):
        return 0.0
    market = _get(obs, "market", {}) or {}
    inventory = _get(market, "inventory", {}) or {}
    prices = _get(market, "prices", {}) or {}
    current_inventory = int(_get(inventory, item, 10000) or 0)
    current_quote = float(_get(prices, item, _market_price(item, current_inventory)) or 0)
    later_quote = float(_market_price(item, current_inventory + quantity))
    return float(quantity) * max(0.0, current_quote - later_quote)


def _impact_slots(obs, action):
    if not USE_IMPACT:
        return action
    market = list(action.get("market") or [])
    rows = [(_impact_score(obs, order), -index, list(order))
            for index, order in enumerate(market) if _is_sell(order)]
    if len(rows) < 2:
        return action
    rows.sort(reverse=True)
    ranked = iter(row[2] for row in rows)
    action["market"] = [next(ranked) if _is_sell(o) else o for o in market]
    return action


# --------------------------------------------------------------------------
def _fix_animal_species(obs, action):
    """Keep a scripted PICKUP/PLACE legal if the two species got swapped."""
    private = _get(obs, "private", {}) or {}
    shed = _get(private, "shed", {}) or {}
    inventories = list(_get(private, "inventories", []) or [])
    units = [action.get("farmer", ["PASS"]), *list(action.get("hands") or [])]
    for index, unit in enumerate(units):
        if not unit or len(unit) < 2 or unit[1] not in ("COW", "SHEEP"):
            continue
        other = "SHEEP" if unit[1] == "COW" else "COW"
        if unit[0] == "PICKUP":
            if int(shed.get(unit[1], 0) or 0) <= 0 and int(shed.get(other, 0) or 0) > 0:
                unit[1] = other
        elif unit[0] == "PLACE":
            inventory = dict(inventories[index] or {}) if index < len(inventories) else {}
            if int(inventory.get(unit[1], 0) or 0) <= 0 and int(inventory.get(other, 0) or 0) > 0:
                unit[1] = other
    action["farmer"] = units[0]
    action["hands"] = units[1:]
    return action


def _terminal_liquidation(obs, action):
    if int(_get(obs, "step", 0) or 0) < len(_ACTIONS) - 1:
        return action
    private = _get(obs, "private", {}) or {}
    shed = _get(private, "shed", {}) or {}
    prices = _get(_get(obs, "market", {}) or {}, "prices", {}) or {}
    stock = [(item, max(0, int(quantity or 0)))
             for item, quantity in shed.items()
             if item in SELLABLE_PRODUCTS and int(quantity or 0) > 0]
    stock.sort(key=lambda pair: (-max(1, int(prices.get(pair[0], 1) or 1)), pair[0]))
    action["market"] = [["SELL", item, quantity] for item, quantity in stock[:10]]
    return _aligned(action, obs)


def agent(obs):
    try:
        step = min(max(0, int(_get(obs, "step", 0) or 0)), len(_ACTIONS) - 1)
        action = _aligned(_ACTIONS[step], obs)
        action = _weed_repair(obs, action, step)
        action = _fix_animal_species(obs, action)
        action = _idle_fill(obs, action)
        action = _impact_slots(obs, action)
        return _terminal_liquidation(obs, _aligned(action, obs))
    except Exception:
        return {
            "farmer": ["PASS"],
            "hands": [["PASS"] for _ in (_get(_farm(obs), "hands", []) or [])],
            "market": [],
        }
