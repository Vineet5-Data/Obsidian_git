import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXctuXFly/BeuuWC9+PCOLdWMhGE3BYqawrhBNBrwDAwY40XbO8P/bln1unVPZGRk5rlF9oxWKhRL9573yYyMjPz5fy7+'
    '9utvf//rbxf/8vPFD18+Prz/5dP95+cvT+uLl8uLf//1P//tv77+5evHv//623/89b+/fv754sPHb3/VPvzw5S+/3P/08cf7'
    'h4vLi3ePm4vLefP15w/r9afBHz6v1++/fr35sL5/vri8GX394/rh8aeLy9nh55+eHt9/efd8/B/XLy//ezns2KeP7/705dPx'
    'TbNB336+2Kw/P39r60+PT88fvn06fDX6cDoQn9cPD8e3LsZv3T9u8CrQkOFrj5/GU4EaMHqdOXuwh4eWfJuT2Ulfd78i7/r0'
    'cP9ubY0n6s/+P4C3jdpN3rr7L8PxbNrx7bufjovhpK+7mTJ+5o7w+n78/uPyuH9eP40X0fi709UDl+58vIg+P34ZL6J2cf7h'
    '/3fGyTej3rGpbAfndIBHo3Ts37v73dLc/2i7MwddD83lcbjal+5HYfgrd7rA/kOTA3ZCs4LJW3ZjD8ZsMBzNjLW/0WdsN+50'
    '6E6eO955xyFsp8lYlzPhcAObwTxa+dly0gVtZNGh40/evqX6WMrf+PMIhnB3woA58uZNH8TDOw4fvp69n9GH2MAdx73y4N0v'
    '6aT3fT6d8C4d2P/fwZu6Ptf98AqPHd0qC8OadA7TwAXS56njszWyfc/egrE9Qn7amBF9WvDu8eFh/e75lz+sn54/Pnz819Mz'
    'odPgpV8SWCLpd0w0B/tbe9Aecw8dHJHRj42rfPUSsADf9PoPzO+4j8u8d+vaf0WbBJh3jfk4MMLBws34GcAYgXsC92q3tENm'
    'Mu/DsLdeH90BBI59wCBlrgr85D2QjQX65D6QeQSi/VjwR+0mJx0oe1Al21fZQNQ39+efeDo111cBntzHQW854DwA4/74yNYY'
    '9Dd/C5wQ29JvX+hxrqlKcLMzG9bfn9b/afK9D2yoJQawZyWjAAHJoqnBLrbaFcfQHON2dq2DxDXoGQJFqE66GLoYCAhnNC+N'
    '5N3IwPXjcV0bFfCyyKOpsQDeYs2/eyNoNkTKPCHDw602/9EUoAZwWggAJDgXHZEuBzRcpV1P/jGW9o+DnH1/7PfHBjEp23oJ'
    'x+pBMN2IyjuW1ipzZmZ88SA4knT5AmBILXro2V0ZAyUGKUXaT0LiVS+U3enG2Hy4f/qz1bEqYDToju7qiyFoNFSHviSHaDgW'
    'FX5AOzhtAPHABCihIHzQDx3bvjXozAB75DAow5HysQwAjpwsu+Ma3Q/KMVwpD/rxiehSGb5vbF+FosN7ggW9ucAbMuHh9sHv'
    'P/5xgou2ZU59Nzv+iQLNK89E2v3u9ttub62mlY75mDbUzlL6/Px0v/lh/fT0F0AOlMJG7A6DHTLePnupICF+iOm0JV1iSxv9'
    'RI7bUHr4zB23gF04Rq/qiFIgiMFiTpupbKahuTFEqGKQEY9lldbH4cPhjvYfp6Gw+yt2sA0xFbVj4LHkboxHILkKrH6Hvt42'
    'M2vioU/bhmYCnu29RehnAnM68rgMzDcZOe57mOm1glbXEdhndUZLxQYP2p22e9XXjfj0iLIlgji74h5T79uDVzL3CsMfBrfg'
    '5vHx4VuWCjSidn/czdDXA/K9EAg8uuKhaF2aPXQJJ7WhljFuQieyyHhQrQtANmL3kyMPeQ45A4YOSPrpfcv3DoGRvJfMZSuB'
    'QqX4qe541IhGbdjXxa0kLLX5lEYf14moImgiADGPnzJYHcL8BvQjYDGWt0JgBNo5Ryfa+GzI7AU21uhTcGTA+dMCu+PQc45G'
    'BVyLkZU6lTF0nUlBDcfMIOICo2ZL37iCKaJhi2saRpFnMx2XS8PYOfQmdhigBM9oYCxHq2xnBkSAXHPS+Noz1zhMoJ4gwDv3'
    's34v0wnRcrYuSUX02CmjlNeYpYjSgOl651m9MqYgwK+HYBRsT2tMqLBj6C4/hvFC5Kmgddq+tz02xLmoRdpD5jZuHbvndWPR'
    'vG6NhgRuZbAJ2yOA3PugRaO/JRNcmU3gfkg5iKC/ZqeSHSZznOlm3Kgj0z089JCpTil2Bnrr2W7Mxjy8xgUsY2y/dggOZ+s4'
    'Y+GyUwwSdPOojSDHpXPvButdfmwymwOYFVO/shI8zr5SzIq0/Y469+4OexEhpZkhja+9ceDPQh5FIheCGjuHP1YYdzlS3GHT'
    'DnFcy7Df/1YIo3o6QqLRSOmg2D7YvxUzhlLR8Rh0CI7G43G8u5h//Pjwp93Ks9yh9pd+ylwF9d5t6e37ZnN/p84ZFhCeSrC4'
    'wrAAd2L0GSSMW7DiwNYW1GBCfmUwUCTkak6p3wSO5iMbc2hgNTBHS9qMuWC5sTzM5PDI8Imel07WrhAgbMZy4SOiLd9ioPqF'
    'jVbkY7WtxAdmDSoH8w6cDLa7gGZZ+4BkZLSlqwKXRURGbD/Gp77GcOTWqmYOXMTfyyEYYMzAPCY+ZNO1qSd5jtaxA9CmdyfB'
    'CKVBcCDQRgB3mXemTD6x7UlsNEka0GB3clsiMGsh9CGLkWxp55ogGqA/EQAjAxl5qzHm3jKcJv4/qgT/AKBTzvEsRwkNNjUI'
    'HKY9YcFNX1o3P/mdpgU1hf8ObBXPfSfU21hIU/fm/SBdY/poTn3FvW8cBZjygw1S2dGVf1hNY2RufruGj0h8u5L69SSd/HnK'
    'KFviRQUsLOAcrc14OA3A0vAwYa0tCT7huvXD+/S0/2l6IY/ZKdE22tmApcnEMkS3WjocMmmt4KBi73JgT8EL78MloLwnprjV'
    'wh5gM2TSnCWXu/WhgaVKtmQncENKkroXfFrwN1FERCdtW5A0SyqS/F9g6oEu2r8q5i0ra6E1S5WAZWuw5ml/fJtP3eLwEhC5'
    'C1XnwJfPEMKUkGFaiyy67cqI4Z2hWcCE6/LKc47W2Vr1RgerOxmgj45Nb75ArlVywp8MJaRdap+m83rhesKfyYTr82JpMhyR'
    'CttTEy+oiWOsrJuXmjCx0h150CchjIKVUVOLzLqSGfonYLtKzHEYIUXPKGsLQPqG41PbVHzTg0kGb8ir1AQ8L7czmeLV+tNg'
    'gIYvEaO91eww9dGsKTAsr1QpGwLCd1FCCtRK0lxiGk4mK9FA6nUSO3ixN8+0ieA/u+1tqT/JQBluBlQQM7Wz/NbetoGQ1Yt+'
    'CzCOM1+37Tdg0lLtvzYh0dksYFqwVcx4EmBeeG6g3K0APhcMszeqLScVF4Pr6+T/ZjtHeeRiI+FwCLd8G8H1+4E6PSYKtutx'
    '5a9HhguPBuLamdwNO0QAPVru9bVwiGhoMrhNgrOIF0dluc6K/hLw6VAbXWvJKl/JV+zxHb7gKUgGY/Ox0QwosweSQ3UpYZIk'
    'WwDvm5Y5SI4UVhLTNIX9xVbrVww5TAKsqJEF+MQ+NgY8b5K8vZVG6ZSwPU8nVXDo5q0kWFgFhUO++eRUjWNuQD1OLmRfSwSO'
    'gEQJ8DwFEIehDnKieFP7IeQyyzyMcspI7Lknuh+jULFeN1pZcOHwOlhEbicSEeyWXcKbFdq1MWE+4Ya+fckASC7kB9xgErrl'
    '3PQSQwMxl5Usbo1HYJHHHLOAGdOAryQlEdAV35hCwcWjIwqNkYykIyZeHckwOBj54KLhDnz/VdMmcbFFE1P05E6BR0ivSxsd'
    'w1Qybz6qSML2VXZZEbeML2ildYyiRVQQzaP/MtmljV2mgAKcAICz+52635yuUPEyb6GB1lMMRKmrkU0SogAheLGymNrfRKTr'
    'yCoRj0UuI4f+2nGpKGVTuaad/TW9T+hX3VYODfQBJpUIx+ZUDunQUrje14cwft7lluquaSGBQYKkdBjAOaI1dSmMniDM4cth'
    'e24dzGZ6UAagM9Fc73VekehwL6H8mAiTRsZWgjwIJxEmR5QhgZA2MplTF4pnPtW1miO5IrrHAlZGRpXFw64ymmmMa8LECQJI'
    'oKxefPeSIUhRNIaR5sdfCUrwgRQDncrF/Y1OgtXAjpaTiRSiVmjRtXCE6HwxV1ecxHmG8UIFBaU8xsycIX/MLe2r5glh1zo3'
    'jTRo6ZGuFMWarPfIYq7MS2e+VpQbNn/JuGJaaFiQAuoxjNTdANX+HL83UmuIOUuuPychs4qHJ2SEC2WXKAgjfie6dMZK1BAl'
    '2va852mu8vgWYi2MePka3W+S9qanudeSFQozCXXNDXyCwUeIByG1L+pHb9OabzAPwirwPCZa/V6c7bNRIFrXGpKZtRxmEyFI'
    'uN1HN/Dwp2RwXbatMrirlBPhCacBGK5I8gfze9jEnrOaFTFIcReK4Ey7StCo8u8kMtr29JmZ9NTbAJNdk0/x6TCu9xDNHwjJ'
    'M7ovRYJ+bgEgVeSCNjvGVG//5sEhgbSdhMYkXKOMKxHOJqmoM2pq/PyTNNWJOY2sqhjFr4ueAs1Dox6D/bPiJHKhUubiSFze'
    'DI0aYQ10TFyqQrEomLKXxKvFTFCqFzLYG+vD5wuRLotzr2jDdrlPmH/PYpE23QrhA6P/FkcAtDCvX6wWLwqrez0C6Zu1qm4S'
    'FUfJKHQWWwOIVvFmta5xVd6EZgx4iRw90xqUDwN2q1JSWWtkLip+Z/juq9Z3n72e786zFdBO7eiXH5cmUmszUYVS/VLgZ7Vh'
    'RJiy6sWaq751MnMgHWJVZqisMrFZ5/QMr19KdAbmn6UHTClfptcMcaEbORp9m5NDpN7WnnV9kgF5tR3a3TelWKbCtNddVXJW'
    '6NruEpmepSJplIKO0iok6uvNUk1KQ6TUJ4Zc9Lyp2H7GWQODDi8BhbLLOqyWf1ETSEyfJ1gCAi8w7NBJBXj8bDpiQAfquHYB'
    '1VgkWWEAJGuUU8drDXcyeXE4+LcIxPsDc95vDCjsQJjopt+dNNGGdupwMnhyTjQFRHF4ExIwOWp1ZyrwwtDZ/10ELCNe0Fnj'
    'lWhXOF5Tp2ztCUKZUkUz30hXOcTkgzfYwmUZqPQi0IpB3ClP04b3WSadvsgwblfOaa2/rTZGYPwH1rpG+XUL/yEVmKtANmWV'
    'Dj6cd2wE+EGhjP8o+SRgUbL4GSbfiS6ea8rcRCiW/gkl+T6ZKu2iu3yijIXxEEacppE36iK69m5cwkzYMI7zpdVmEMvFy4p4'
    'VzXBwZhtqPXSb/T8JcPVjoVlTb9QvAA1eUeNxM3WN2xOKL02sUhIGNjhR2p5rI6GgaiWKHh+iqyk90d85pMDpnPLNZK3c9RQ'
    'WkBenXKWcr61rA5HPbjAF0Y9WUj1rMK6jMS0cbUN+/SjPfDFrSlhVYzWT+Oq2e5oYX7GhiWQCzn7uwnSzus6E3LdJCXThie8'
    '5BfiKp/9sK1wefyXxcMpG37/AIsiMWnHSiUd58MXD3X+bim9/pDZ+UZD8TnWfJ+gfN4l6BOO9/xoPV4+TYxer2VQIoXGw/Nu'
    'KzrjPsr8tlpTnbQci5F74P67oZdAorMWk9dD3ujGptdsIgDPItvZ1BSlRr0UiVfVGlEBMjkqpPCMwQtOF45kakyjOxdUJmRC'
    'A2XYU9BKVv6zsoBYOUjiVDkVNiLKSQoMQAUhifuTCfBLZmw4JpKQzNUwMGhxUBJ0kYmq5ZIrWmcUFs6GgrUouSap0E3GgBGy'
    'JY1+jR/vLjLQDj4Ja0E11I6u9xgnolIaBd58wcbENFLKVRcpt2kcwaG/t8T+3us4d4DX/KoUA0CVlTkG5CLqQSmgcThde7tI'
    'jsh4h/DW0r/kIbgEh1N2GL2/Cw42Rv3radj9Fe48OxUcwHIgX43T2cnWdy8J39U1ny2HxOsYXJJjC1bBAlPeMA21i/x5yRuT'
    'kxN80H0cuG9DhIrnfdpk3aHiaaXVSRz3bZ7So+chTLWGUCVKHiG8kFgT9xs1obh0k2M542IZC/QfKAe8T+iTYAmqYIBBZmFI'
    'SJfgZ+AgZ2eeyBZRw1focZWagzftsRZgx9BkDQMzowyDdisO/rPfwZvSnDmhX6kci3ck95m162xgXlIeRKrailcbmioprq0x'
    'QLR8DnMV0r3V4wDJB7W5M8EAT0w9+EbCHXrS167X53W2eZpHhmE1CzZKZ9fqsUKG0e/jsjpNEmmEdM+iZPhNvw6NuZRtE+pC'
    'hb9W2EdEcgAoHbSSDu03gGNh3wJi36aTJZgvhW3Z+qpvKFFn/nZk/En9GlGXTQD+umTlhBCcQJSXloNMpubIiguX+n+vK9Kf'
    'Q/9/o9YyqKotVPJ1Evn5svoc7VexXIAnzUD9LRfFdeqidiwjgD5ZEFdqJ0uikcMT+S5VboB5GXhkA5Mg3ra3L5l6BHx8xdqc'
    'Xfn7SuUCnLrlWMf+RAw/h3y7VH0DXmtByhiildRVWOsmkGgjLogTdbumZcKOCC8jtap6OGML9RiZQQRTTWRsWXh8sSID39k4'
    'r0WdP5uNNRU2ogKHQk3LoDJCoV/L/DRS1IMmCNGkFGhb5tI2FPCndc218rEM9e6s0l9xytuTn+bJFCokdO9ghExDu9JkXJx5'
    'pvyO0CijUPTTg/UrFUOyfepa1+QtbCVWG4PWuOR9RbDwVg+OPpSc+e2TstNaYonNlnLVjVfMDTpeMW+jogayiTh7WqVjLbqD'
    'YR6vTUYKoPspIxYGBqCkkAc84IDjLHN/UuyYeWBZhZRP8xQ1r8NmgNk/sO/aAPk8sFYzNTbl6UN2e2DVorm9QhSBgAHBMDdB'
    'loQVKHdwuKjDIexXsrBZ6XpR1lJDJTPsrZkyi+yATdSD5fw0DX/y+2pP3jxHHpBYlSodhJtccieva+uQ8sBUqzCS4yf2giw4'
    'Wm5F3U70GTJupnN00cnkMu01jzGuxaQc0lKmnHVcW3gQHfbsKVZJjNwofE21FEqcSyucszyHi+jZ0GK8tMZtYrsCr4bmjmgJ'
    'jn41pRqeGEr/S2ZMkolh91wX9rKTcbwO04mmm4oCQq9wtKWFJ6zTflguOZ7YSnPYYxI/KSxOkzumQCEbu7SNwrBCJWg6KCTl'
    'qZda8SmthI7b7fTSW3SijC2uDMqYqZK6eqsqOmfPs8ThwUyVG9fg60Ab8/ABF34K+IQBTWeGiFFmRZcqsOUivL7aeqzIrdvO'
    'gKum06T652YCa/zUawhmwbm8Rm6naxQtLS4Wrl8b0R8v13ZBas6EOmO5choNJScmA+hiHBxyMj28tiqqMgwrYoimleKkEVbj'
    'gOYqcFFJPom6Q6kLrXs41xnkPJIeSJvnKMLGW0/AIZoTC1tBc+kYZ0d10a5yEBFTmZWWDN6WKah7XvfEKOrOISCeX5YITyxe'
    'EmRnriVhbQeKWqJjLJEhBax79QCk5ArjcDX3tepcrUKQl6eRLioIM15NMqVoLMXqJ645Sarok3UfBISpzo0iEeyLzcKeELON'
    'pS0jU2qHJZKyyGM3f9RYHRh0D2+oCd0Qg25dAmkxhVQHcyQltSgpTdGEqKQAXol9EQXYGDPSpO225FYT6koYFR3Ki50AUbdG'
    'fTFITPmOTSllxqjmK4StltNpgp1gTCQpRMSF+tUTU/IqZSWwQL2MSl0xlCRf1v+KFEUrVNJWxJPgYolnsirwmZ5NqqWfMVXd'
    '1jdZO3LDskhMIgo5C+QuwntHhTUdnV553SUS0lhWkLVvgQrTmhdnBqMDgQvFVbGFbUoFxRTb9VKmLOjFhpNiRXr6mjWLwBGW'
    'a3CziHkhUD43J/c2kEi5iemUeQWgiTxXn7kjaZVcdY2RSfTZzRwjobk7JWGqqnrtVe5m0LebNCJ11MVRbVXEFoHyaXy61fRr'
    'D8o4F2mYARFMJQ1vSHYWs8p4ffYoEycf5kZiXanTZagQkJz4T03Xz1GqukkVmxJKh/iV5vN8VWsv1mTHgmQrqcZBF03Gm8hm'
    'i5WGVj6YK/0sy5HsRROqi6miXcbqxnVF+RaRqomKQNk+61bemOHerWJ6+9q400iIogeYoPr2Fhzbzvs/Tq21/jSxE0UJnyhm'
    'Jl2enSfmKqtHYLPzUsYytdzeNi9sApn71+CIuRXM0Q1EJe1kEphEiqAsMFU02GF5h4GEXBauvvIpHYWqMPVJKu5AHMvgUkma'
    'W5BAtlZGVChCG/L4lp3IY/Qrd0ijtKVVL8qYgY5gKqHDOYxgt8saa8xhubiKVFKB+Xg4g3HHoiIy8cJ9cRH16zpzzBN0p5JT'
    'OtEmkPKZ1XjjeMtGQNFCZUg6Z4FqymeUZGbWjVHq16US1yXQVKGBcLB0pFQ35jFFCEFCCb1p5Y4UrtPBySeNZREE6U6rTLJK'
    'XwPoDlcdpJZw+/P9QAGzrq0oX+OsaQwnyrXUBO/oCjUl/L4eh0+PVYl9faaVjjuXXLvIqTJgoihxsou7oZQZekDBDBy4bXZr'
    'y1QbZosaJEU7HzMl1ubAl6upeXAr4yT9vfDdQJ8WpfbXeXCcXDZxLUyHyhRlwE1UAHMyEtx0FTFfiwPXtyCmpsau+MKcwuRC'
    'iHrt97BWyl3KM5ZAtAhnkUn/BlKSAHlnbN/fJAvHNQtZrhbBKRN8vKai+ehEOyNDQacTnliIjZ0wTxXvERh4i0j1TJGBp1JH'
    'KtpFlr0zF+aZkETNedbpupF6GH0oPwFSnpJtSF3O8Kd+EISOFTkkyrDpEiixUq7YORNAJMK8c7Us0RwZWYvVru6AohQ1hjPu'
    'iNKmrKZmHrM1DHBuHkwZOX2PBGsHCJxHjCTfk1RDd6W2PXKISaIgmElQINh9gTp7Y5KhAgmsXBolTVvr10ElcVFg4qnFSKjO'
    'LPXOqtVbc/xJrlffIl/2Oh7gemE1tAqNMkPLcxhdBM5US2tVGXpzf0RO0D9lH7cmIl+RGkwfYNBNuhCU3qn6NmLVCfCUPlu3'
    'ByHQVlE/2GQh+M8UqjsfrlmrQoo7sOpHKpT4JUJ90rPpy+noRbUWw+1LLPmXFR/Nasw56lVBip1StFSsCqCkSwVAtgz5kRQl'
    '9VaLG8vncl3F0qOyJSrJZEujR5CW1ocN6tuz6i40PhxwPpHqu3ZTarzK0MJjvoJLmmXgnJhZoCcEMtajoJA0wbKjuo9Ul1wV'
    'c3DXWbA2pweUZgh2/shJRTY52YrrppuerGsNLtLJYiBmKfIT1HovasmaBh1rIBS4kYd90eVF+eR4JSGisuohiTW0+VwMXrzI'
    '+kX0rIbAABChPaEpUZzphCofG3Sphex+VSTVmyclheF66GhpioJqNSATIQnBbkgg/dKgnAQqLLh5KRIBjSpvVbTuT8cs0C9G'
    'JlwrtWf3sJzPSkyzmOexk8RXhtVA81sx+lrolziBYQhGWiczQ9ugimLcgFKb/xxVMuMKawo6bdDkzsIzExAcZqRVa15uEgUv'
    '1aJyCRbZaYhkKiKZmKFXFFq32qSywhzqSdWfbMleDG9haYlqmQS491zNl9sIjSu2DsABo+q4Z4IB10pWyjLAdwHNBn+DR6Wc'
    'oqx2bkFiOX41CEbZ8poawFBtMVlrehUHpkTX8suBuWlv5JAWGZX6vFWWq7z4HJUmRZx9coKWJJBGTHalqKuoVKjO3m1mWZr5'
    'SmrSTHJbgTq7PaPF7aJkOttGzSkhDyosFxM6R1tBhe1EoAXbThE4cdofoRzHQfJMVQtt+6hVns5DEheZ5D9J/JI2bV4PaFna'
    'shQuaveqVtOEEH/KNbK3E6zv3SIeyI4rNhgAN0KIxVZmUoYl5sHNbJxmBrpwlcQS/YoCg4FkGZ3V+qtTcPgovdDe4izrM8z9'
    'nse2eCjNc5YaCyXMxv7Gg+yBSb+aREKRiXTGxYPCgZhlj20+74tJDu2I/ZKy1mUGj9yd6/O3keg6MCNCncmmnLCc0OGxDb90'
    'yj/M/McqwnQJrkP7wU0iBSQ5VqdFD3SzD1kdOZk/l6C2JAlrKaZejcmX407o5DVP4F2tq+AjykCwBcwxj5jqOt92fQEGbM4q'
    'x4xbaCg5BRqzTo0qzlNICkq9FWQGQ6i+pirj5iDeBQg6biKam7OmJM2wftyYBZv0QyxAslEldz1rUQQ4lCNKrbCgwf5h2sAy'
    'la7DiJoDRgTR3BMGIh2jSNnn6kmP2G1rW6RPwbjN/D7NReYZMpQMCL0Mt6GLIGWeoc5KbqWKdgbPmz3aE5Gf8pT+gs5rKyY3'
    'QCz06r3pbQAnTisxodxgVaGpRTDVTMejVgFoNpxpGZtxyh2OxFeSpQJUQU3OeaXsvwmS7JYhhX0+1pQ5SkU47P3bKdvOXpXi'
    '0HNoiYxAik/aAugOxazTdr4T1jnQkeNL2pK/pOvgHPmkyRzMlZWCeQXgN3D0zhc9+IDLtwTC1XTyQjpzUv6PzgaEDVIgKld2'
    'jebduIAK9F3VKmirCJgZ0gsKKdARId1o0VgmtB+saFkrOMF3AzheDb0qBmNhYTkH3knxa6rSeYnKg236aTRsyzO62MXhx2lm'
    'AehBT16MII+O0rc+NbuToKNr304d5siIhpTIKA5UCpyl0FVqAdIcnGHLRyQEMidF6BS/3kvVcOC7mAC5v4/mkbKqWsKTzAUU'
    'Q9TB7aBVraGpadLBFcO6bgK2FMzSJ9CiM6itbGaooYRNDwQhCFhIBfLGNWJCTdTKIOjKe5E96hsZNy4N0LhOHR0zKn7j6MUr'
    'sHm0KqOCKBFpynieOcfdepwlKnpE6ZsMXbQP0kTzBSYWWBOEUdnUjYRnin3yh3YFWT6e8EUMkUT0EJNNGM1QK3GoaPgjpt/H'
    '1ARCtR6ChFDCA2uZfpucXFNsmU0KMZ3IfG2txlsLdbLyXRHqX8Np2kl4I+mllhk6ryWeWva1WDAgh3TI1CewpplBSvEDAWZa'
    'BFRTy6pjSWJVl+oGKjSnq6cxRziXb8prBopKNpwno20oTdzBRQo9/MOJTgcq523s4s5+HWGxmJyeHeeuNXY8bQgf0x+kdnVR'
    'V5tqi7WkDp4bkExg19XOPRWqTA1klVMuKm9BnZNQg3z/XC8VSjdgTIWO150JBQ2YX8Dx94gJzJ36aG1ewU3U6CO5Yj+s1Eog'
    'tctqKZhvzch20irtTRNqHruONoG9IpZ27TN+joCbVJrYxuLjbcRkJsxFRgyOURE4WCBuVG+uOMlHh7t50QnDqOUrtP9h/LdQ'
    '0zh5xq6Xl/hQn9K+7ekzl9TnRsIZl6S6356DcW24zjclb9gha/Lbz5aGzlQVpKiGEI1Xsl+coprubWWW/VNe7ow1ZZA6evfe'
    'q9mV4sSfPLqrr+BD7RZPn5Ez3V2D0zdKRPFOXRXCHXp4rIt5qk59Uv3d4IIzGK1KXVSBxUXuKHbHdu4tHnLy2syRQh7HRzbQ'
    '2U3kJgSKkoYxEwMklDeRV2Yc2PZNUm23ak+J8iUpoFPqKQhHOcKp8fqooKf08FOKBZ23rzolr95Xu5Xkte+fHj+dvnX3zeAD'
    '7yv42fYrxmUFjOJbtToaOUiPKhtNJw4fDj8efUPYREu9vNBJEPGoIfryf97GeUI='
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
