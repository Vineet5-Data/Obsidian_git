import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vI9mR/C868zCkSH3sTdNNbzesGTXUagvegTAYYG0YWHgPY98W+9+3LfGjqjIyMjLfK0q96BtBUVXv+2VGRkb+8j9n'
    'f/3t97//5fezf/vl7McvH2/f//rp5vPDl/vt2dPi7G+//fd//uPrX75+/Ptvv//XX/759fMvZx8+Pv9V+/Djlz//evPzx59u'
    'bs8WZ+/uHs8WK/P15w/b7afBHz5vt++/fv34YXvzcLa4nHz90/b27uezxfLw80/3d++/vHs4/sfF09P/LoYd+/Tx3R+/fDq+'
    'aTno2y9nj9vPD89t/fnu/uHD86fDV5MP44H4vL29Pb71fPrW/eMGrwINGb72+Gk6FagBk9e5swd7eGjJ85wsR33d/Yq869Pt'
    'zbutN56oP/t/AG+btJu8dfcvw/E07Xj+7ufjYhj1dTdTzs/CEd7eTN9/XB43D9v76SKafjdePXDprqaL6PPdl+kisovzD//a'
    'GaNvJr1jU2kHZzzAk1E69u/dzW5p7n/0sjMHXU/N5XG47Ev3ozD8VThdYP+hyQE7waxg8pbd2IMxGwyHmTH7G33GduNOh270'
    '3OnOOw6hnSZnXS6Fww1sBvdo5WfLqAvayKJDJ568fUv1sZS/iecRDOHuhAFzFM2bPoiHdxw+fD17P6MPuYE7jnvLg3e/pJPe'
    '9/l0wrt0YP+/gzd1fW744RUeO7lVzh1rMjhMExdIn6dOz9bM9j15C6b2CPmpMSP6tODd3e3t9t3Dr3/Y3j98vP34H+MzodPg'
    'lV+SWCLld8w0B/tbe9Aedw8dHJHJj52rfPOUsADf9PpPzO+0j+u6dxvaf402CTDvjPk4MMLBwq34GcAYgXsC92q3tFNmMu/D'
    'sLdRH8MBBI59wiBlrgr8FD2QjQX6FD6QeQSi/djgj/pNLjpQ/qBKtq+ygahvHs8/8XTaXF8FeAofB73lhPMAjPvjI60xGG9+'
    'C5wQ2zJuX+pxoalKcLMTG9bfn9b/afK9D2yotQpy1w0D31awh/MYRl9OYPGvp979HUJqpOOQXbXSIVmxHw5vHRxY+btTbHtL'
    '51JDiJD1pjuB3q9Nxga9aCvDwu0YF4rMOE1R+xNmE7U8iMlQsMfooj+ifiE2StCrYDBiyDBz8E6hrP8/wNX3x35/7Df4WB3A'
    '6mHq+JF3GMIPIadNGkBxQvL23caDZe6chq8UvcYEntIWgIwsogoIkkOlMu0nUfVWR5Zd8M7YfLi5/5PXsX43fgItEKPYaKgO'
    'fSkO0XAsWigGdnBsDPJAJmgCUvigHzr28tbcoCOj6jAow5GK4RCAr4yW3XGN7gflGPGUB/34RHTVDN83MNB1DGbK0aD3GXhD'
    'JcJsH2xpUt/NBv7YKWvNwAXfranAPqGj+UxWBPbVBnMhlxlra2fXfH64v3n8cXt//2dg3JRAJ9eEGr8K0jBX3eEmtzV74ufT'
    'DNDTCRGn1EWZsBmnuFP14vRhhCrKNJc9NTRFhsBSDk7iCErT+jh8ONzf8eM0UG1//Q52KGa6doxrNrki0xEorgKv36mvX5pZ'
    'Nf/Qp5eGVuKp9gIj7DaBmJ15XAUTnI179z2K9VoxsYsMULRptFjOnwrHpxAcC2wEYpWg41XxnKljHiEvlWuFQRODS/Dx7u72'
    'OQcG2qm7P+4m6Ov5+P6sbNgdnXfc28TX0tG5kKaa8SE6EVSmQ+3dCmFH8ayk1/JhIkQEDgaOLwWqD0hL6m0olKaIOR1aMEy9'
    'ryXMqYkLpvsubVQoG+oMYTEJqjWfyuDm1kuGyDURYKTT2GuuiQhSHBCkxlkEzbsg0Xk73ejom54WlW3Ahhl90gcFnDoWLZ7m'
    'ydToXcAnmZi3c1lRF8nU2GUpPDcOhK1jywump6bNMZEfpTm6cixrQqLIASIoVRekljptANcvu850tELxp6MBcr62N7nzQw4p'
    'OOfFeWayYXpunIudsxCke5um3/m8LgVSYADZIYyUQPvA/N8E6dOMJX6INJH05SCZtMV6YDuIZpPqyeMsYTW9AuE/NBrALpV8'
    'EQQfLSoY37LEh2D7za6XXraZjS9PVxb8EI80sycOvQAGgGtrpMbZdpk91+1fzuShIDfpoIkyg5TbytJWXslGA8G4xXNOaQEY'
    '88LZlhlnB7YGw185ZMGA6sTO/PCz/P39I5WWVPBqShqQs7tfIfG7D5K7TPsg7ZS/a+xtpNRwhuxBaxPAn6U8j0KuBrhd2wy2'
    'Tol9hytriAZ7pj8w6ogzR7WONFUQzkLl9iumJFWTOhKuAbguDxO8N3h/+nj7x93K8/wk+8s4ra8FJN9t6Zf3LUXoQELWh/Ga'
    'dXaKwaJLwwocvG1x+sDLDisRbHlBySaVjJMMQwl5pnNqT4Ej+2imD41hA5RYa55DI5XsHeLCDI+SmGEqJkKlxvI8Bkyt24b0'
    'rsS1iA/PNucMzLVFjew5jnSArNaaNUqLMVfLkWWXDN8rvoUe821zODN4p/aV+7eacyI5voUP1ezyyDVyfbNerSPbgM5ezqPV'
    '28NWPLiwrGPVd3jgtFBoJZxI4hR2Xmb2BRbSmbriOU9Z511fJYhgFIrKO5RtMmzHM5wc7y2tamWSQey+d3ukTLOmEOE1CRGW'
    '/VzBCV97Bwr53fxeOLAuIiecsHBzAUzdJw+9UmasiFmPcf5jbNjD3CBsTMoOayodsCWxkrnrdrUeI1X2R3p6pM7J0bWTX0hf'
    'a7ySQKqghOZQJ6EVaji0uE6WGt4Z41FQMB3q8qaDt0TRe9eojD8s54Sgra9pfSRCQIBWZtxf0BDkdwZyIda4rdD1ghdLAXoS'
    'wSQKG3XGEzh1THgcDS3Ymb6+NXtqq6OsDSvUzLZGcIFVJnDBWS4pzItJhVwy8iggF4W4BJA8UYh1KcZwQQ7tFC6EMpkzfWic'
    'xhO0qn7qvIVBBCbYW2jW98H6vj3ngRtkR77s+4LaJm8mOm7bRqPjQmQ65+uibuj2rhIol1vJwh2VONHlU5t4cTEFC5j+KpWh'
    'hp2XnNAcEZz6UBXaGuA40tASj8qhh8ie9xgY1IPKuAFJti3yDnzfedjUZcmDZnA37QRDsGozz73g4VvEAGyQvjWNEqxTx4Pk'
    'E0cd8RZ2qvQZOQmCLFZG/0WKmXqmHbDDiEuMtmuwm/B4VrAasAMI0md/BLCG41dKnN0uMxoFhecNgxm2ihiERzpbxquNTWyo'
    'v4oHkIFvRgZIaCIiBfi4Fchu2vPNhuUQ1ek+sscO/x0uylGGI3k1TQklRDgS2gXN9TDo5eZJX8vSrcd7y7X41K6kj1NAZtoK'
    'i9hGaiPTF/YeJPZWVpSOmdNEIYiYulUL0ZTYWG5NRd3XD1pwGR9EjKLVVaQ2gyj5NjyBvTk3PHrUZj/dWNvO6Q7VHH4J+yyP'
    'ejbqj06CAYuYpAkf5DuqqcEjgbcyZZ8jFa9L37eMRd2lDJ1W15HqxCcAUUuhbm/Kv88GwwUD7SqjmWGDW5DF232GWiVgjhkC'
    'sLgw+rJS5mp0purXpLvqa7kmjIYTDTzLrytVnZASOm1sNs9B4bbFhChYcfOAT3XoQDSsGluY3dUtyUfeIGwFMnj7gnDPHc2K'
    '0ApmcQo+6Bd6SCjY2LRsCEOAJoy8xRXDbGK6h10oSK4QkHHWmeAPN4gTiyKW+fSzEqQOMgqd7RdeshEUBGkjbHF5mlwByZag'
    't2EHFGkR5yH8yKj6Djm9LkV8KwY3SO+albu09estKta9OKWoqgUSLhqtqbQAQXqlrDL5ZFzxTIPl2Jin7zAW9gkfT9srd5AJ'
    'Ojvp8R0PGnH0cx0sEiwbWjXFRhLTN5OG/4y0ujyO84zZbOZO0PAhl8OXw3V8FSA080MwgASgBgFdBLhmhOqJGnXSiAi9hOcP'
    'CXH8kMznoGZz3n8Hoe5UDr5dGEVaTrvscKuyEVtZOkQCIpGc5FLLilfy7Rd6Rcm2TJ1ULVzHHddTiOAOO0/c8HFGCiMOhH5e'
    'GxFd0bdOJHIwQ9o5qvQ9L44Y2xuWZNB1qln2CPH+dS+5KMtHVHUHThBpMyzn1pIQj9kefgATpxNOUt56gBnGMOfxVTa0k2mt'
    'KBCzCgeMMoRpHEorJ6dsTxiCeeB5r8DRlIxwRlbCk/vp+kz7Hlh6OBngnPfQBfihqr5RhwsULaRQAoFMqzgkVLMQO7CV/I28'
    'M82oB9Me5WYPhag8LoNUk3F28fOv/gskOnwTTvPJiAvWUob3rsRI9z39gu9sb+5qcD6rJNAq761S9ZHhIrMSaqE8YB8XvePQ'
    'U6lMRiPcwjQMqPNSqRgJq5vrET5NXUH3B32dsSJgHr7ach8eJSudUfZ09wnhXzaRJuwE5016JE6gTtsoPUA5VVJ98vw5oUgN'
    'BJn6kh7IbBPOo945tYHGuuL0LBeDep02LoURKMeB5sKUwm929oLIMZtHN5Uhaclq+VN0HvlizPuV3NK3FrfqdGaCeUjO37yY'
    'Oh32g5XCy7SIOpFEXE8SiGvzkAjnvcgDZ0OlCcMJPHY2aYpYfjzp3eqySutLn/FegWFpLrOajbPQ/Z893munUPwresKcsY9M'
    'ro5eLkY6gYa4cdObykQCXyWyUSHqnfEK4bynSPMtynot0nvKRFbz+yvB3l5uKSUgZ6KMYryeUdjTlQ0UIKWFZaw5xHsKsgX6'
    'Dt+kgrMXTy3pCTm3o2gRohpYCbGF2mxIeuvOehjPRMW/skN+HI7x0wVyP5FeXGYQG78WWcXH1CLcErVB0ghJi2qs2mkLKpTR'
    'UmiYSSrAhRgErSuJZ7QQWqTYQbGyEAjQjngpPSaRgEHjQ7pESY10qtR3DJRGNNJEGEhkHjP1Sn0+RQUMYhgHp1slmO9p5rgU'
    'PAeQDvOmTpcr/SbDhZddvKaTRgtzZYwacphniBsWi5jlSLMKxyEaWuzU0ku5kUkLokB1KnOgd8QTkxt5tHa1jAusvaglJNxf'
    'Pc2aCVbs362bP/IaToieSyV6W5h9yDygmo+RSJZWvb0Yw4gT560cFHULKF+xda2D+IVOAA/Bp3QxOF0tiRrJmlZPEE4pFClj'
    'gSw629JA5TaUJOSWG7qAYptgoZKJzQjsBXE/SmOtTayUGZ7yJfijKqAQteZ5Bg2TofNjjl2tfs0ppJFi5jkl3NdcI6k9Rh15'
    'zeYtUXtzLSZxMsRLGXbw/cd/P82oYnrtS83PgX7UhXfUe2sDWljmiWNX31UKW0wQxAspR05SjDv6u3b6zJ8O3+C1WFxm0+YF'
    'hc+G7waEXxSr30ZBbhbyiDYJq8re6QPssqgpsexauG21xPTm8UIexn9HKmxvNf5bIz43RYK5ZrBrZ/YLAEfZf9u0UlkrhTms'
    '+JuU1Jwn2JuvFVcsTdaU+k0dm1nk8K2FF9UJTJE7i7xEFoSIXMtOCvvRggK2p5TNWkyj1bitvKTbtkehYeZqYYwmiLXrU0L7'
    'OVGIvYgNbhLFOTykLRmWZcJoIgc17PVRCiKiBZSOx6Ne0BRmtrW5g9wUd0VgXQLdpBHJaCr1iu1BAEAqjc6SYNPaZhmznzHd'
    '1eDuI8uir9n14Jzygv1xfZF6y5DAl4Sjs0nPFO64ynhwkhPOQsIAT6qGpaWx4cnobjw9nsapF69E9oF7DupU0oh60l9c9ZL8'
    'vnBIwMvAhTzWzH0dTxHQcl816A1sejnqTUvDtke9QRZcRaZb0MZqdS2hkx3Hm7Z6wIoLt/RzP6O/KwXqxGpdJ3VdLeMxH2WO'
    'OYmpelRaXZukGPFjfcUVXeBAJCcSZwkcsAbOh6JThBjJCWSKWv/RGqt4B1ScMhWZUAuXB2WmJsWbEsXM+GKgginphOFeabrI'
    'd3drv1zMON5upSDi+AP7nIRyOUwRRU40Duru2RtXrvGqtJ6ShAGhYJlcC8wGKy5EZX0SxRcznXnaANtZws6+EBxYEcShaSXg'
    '94wqkYUotFi7VrNUW/hV+ndYKfPQIu/ehD9mqCiTdz6UV6uuZlq4i0AI495FF25t+FGQNazlEJEi2CJyOQDUo/LC/I56x6Iq'
    'AUgDJ8ymUOt+BJjLdNFd1rvCSdupdAZGc5BKcZgbNYXo24RupyieubVFKp/lBWhEPgjM2Nlad8pfWK2d6P/VEPd5acrqjeU6'
    'vCE9cQ5dQL4L6tF5iDjHM9KUD9EVpWir6K7asLLieMeiZsI4iYFpO6OVVAuV5KBx3wU0p2PePlmOmamxJm+iDl/npFIJOpDn'
    'IsGtIP4cQKgrgbHUyq9wQRgLSsylV2tzFaQIfG9vnPCGh1OmjJjbpMamZ1LnmkPYLB9I/HAQheBZD6o8XkKDmORJ8BZomeIq'
    'maA2vWq+EGiqlkhInYnnyF+mPvgYz8Y7RNY7rbK7E7yBnKS9/ZsqyVjNWLZDrWnMqw1kceoBnvCvxdhDKR811RHy0KgBbEZe'
    'FmVXmgk/p6jsNatvVVjUQKxMye2gXixXZOiZh68owEnCb6Ym6dC93dSl4aC7vOlYN17Tj1PSJJoV5U5Z5X5GzXdLXDGJDtPI'
    '26tBHcf7R859QLydNk5OB6oLZwOaBI+JAl1n7ssIwWhhvyj5H0X6C380Nn4y/BfRB00FpJWS0JDH0L3YXQGbadQbixImIp+Z'
    'Qugh9KFPHU5ClFTMiA+YyFRJQh5qfXXuiGiFXq1GjZRagqwLKzdYqA52ba+iq0zBsLC0giQ/wePcgWZdR+YNFwK33iwOXVI9'
    '1xRzmtElJG9J9LNKMm/SskCt8wLeYiGrmZZDgxo8jbv0Ww3iCcOYIvjK1+CmhpAJcGPFtRKQdVmmebOUHq3zHmUEwJHmJ4jL'
    'VumhekjD3yFZhWFencoNED0Cngnq/1+UwTnd8h2URTi0rElNMKQ/XZFPUUNBZVsl0OhRy48N6DICSyaRCsN4ECwnRqqCJFR0'
    '95Odck3UpHuE/I4kcaoGqsDWxmUtTpBu9IzEnP8gsE6Gtv63XoZgLjmKSlWC0IjoQCixwhVhTo/KEZmzGl8dfpi38GC3Sn6P'
    'UmHBN6iVwRz1sQPTWHMiZzcpwhpgM2iGB3Ab4642K28w0USPPaxqaRdWMyitYAdoEk6W04wSyFyehsGSocKpBWe9AtlUk87I'
    '4rPzKdad2DY4TdQdDY8AD9GgSzMcQC7bBvFQIt6iVn9P5ROs9NQfZhi71FQxO8bZjpzmkeroOhOZF8UkHfpWROaBQFoPmQhK'
    'bhS1U8AYyLqoNlklx7xVeWXOatHqZgrZKJKwiro22UHjsijRxkgfNGzpxjiRSJik6ZIFSRgmKRvW6/GOcQGRSq1jcHboDD5e'
    'EDXiu8VobuCAs1Q31iBS0pFUqSxIG7USXsYjlyObnEx0k/NLAKix+ZZAjenVu3jVwiGUVwJNFzUlqBevhLZQywGkx9hzwHuT'
    'vI2VHB5ZfwXfMSTG0qhn9zg/f6S5lmbBk4WrJ1sdpEoWUeaGFRPxSSIZgCX0GQQCxa5Q31NF1hKSk4rZT6l6Iw4bvpgsg3lg'
    'Fm5iOiA8t6VPskxQRCJaQoO7AttTrSwvfuMEVRMoLkKYU6nDkWFJct4cM8trxVrA4uSVQwB7VNctyBbQfDkhVikehD+8gWNL'
    'S/jmFqidfjioQg0EBtA5Ry9wGblqC40RswWiDygnmoTiWAUkkuIZGvuCbVAiMJaja1Cvz7llY06x//tsGZicvARzXRm4AO6U'
    'fXGS1AC//FOQUC6gWVHKmmHLfD1/7u8ewjJwDhRz+G8HykAHxZWwsQzZdRfGFzhsrWST5doIkE5Vc3a9ltK1RNJ14NQwBMon'
    'y7lbxO0A2CM8SwA1gx4ISrnh+fGTUTbO2pOiXZmVADJ3Vsu3Cq3Uypb0IYy4JE2BEzk/R6RGjcggGlJE1wmdLX/I8AwpvlOl'
    'g+jyEXQgUnTbHLGkOIch5YTGKLLpS6smcRy2mLLV/3rWkWfGT6SBkvglL3HXdX3FysCxNK9QrSaZaLSruHuVWERilg1lvUpZ'
    'D6mRt8dXAjBQy4AyX6E2F8t1aQkxOhWnG2vyrDRfcp1YLLRZwSKPAfmEN0FIbVFwGfVBxfwycBM4BhmZidWXVSzgXFFWRSkb'
    '4OiyBjARJhFTDndHWbw4I7dXq9cb4TKk+FE7eQaACnapMLwhSsyJY3XrVIOZc8lEjMmyoOwPBQ8BDQ4q3MpMt5idni/fsipV'
    'LQ3URuPBTSu3Vh1sVjeHSu1SlIL0cQ+iSVktqAvnmbwn6jlpmXP2tBwga0LeTj6Pi+TuEEYNwthYaeOrWKlHA+ivXBBtMWfm'
    'j8eRWZ5/45k/ALDanI4pIxdjBaes7EUP+7buozwbKaay8CRNPlVkZTy0Z6otcflUVHFJFiIKqTYRWpIqLrJJLLhm/KkPLwf7'
    'FFkUaPNUEHuJAjmtQJfMg3fU6RMwEUC29FrDjxopIkUsv25VFSrAiRQfyiCM+BBZJtYYO8eyVXfdcohIooYiF0snCnPZAU0K'
    '5GU59kXAQX3DLG2Bx5K2lag+LBQaYYHXYKIqS43h1BmF6Ey0087CeUKVSitqE6uR4FlJ1tCwLWeIlCJDHe1xNnWZCsnLZUlP'
    'Ki6xEo9raNZoKWCmCfkN8agTmY/dMkSS/ReBFZ44lTY1kkxQF5eXJYs1jhPFhm0PGFQhEaPS8BFDuptlZNDWDEIdLD7nuvhw'
    'r+hOvbDtpcISROqEYUNhNnAE6UVbmjE3qa48Q9HF8xdcK+klhqqC5zxcfl2T6fL63aWy+VYI3EIBae96EUu3sqMJFviaB91y'
    'qyktrxxzGlxgl0DccmYgbIOgro0LpKzdn7cVXlrIDBxrs/iFwM8poCf8lYWvfRGgSpkOmvimybnIBCAlfcyeqZGuaPR3Vdi4'
    'ktdNmPqB/B+FBTKNaigVLue+aBV8a6Vj7IQD2Q2u/xGLA1YALZDnHFCvBxgezC5viNHVws+8YpDd20otnMalKCknOcMqSSb2'
    'WoXEZUhAfSrGMm0gesOwuQF1Thplum/CKIHgmq0zwJ2U9ATDkCT6XKnPY6+kVPQgLCBDu6UVDXNFePIRY651HILzEeBFXB4x'
    '758jpvJsUZYNTaGibK1qzRmWm+bcLlqDaLZJueo2RyMS0x0aRk2JR875l1NXirlAHfhjNE+IauhE+ICcpyjkBmkFhhivhvFK'
    'VblmQKdxyXON4kFxRTApvTpI5+o38lLy6AE05pRpUmF+gredODvL0iM2g2/2Y7YGiVnfVEmlE1VOCkKEzGWQKC5sCia8rJOw'
    'dzIB4aTgSrq0kndO16orJc4+iWjThzEzU2rdPJWTsmiWXBt0NgaNGP5n8RCEfK+04qtLvZ7ddYnsFS91OWchQ4srFYBalWgQ'
    'YV/t9UvT+HmKX0NeVrR3RDckyg3qzSQ4NpuNPQViYzGYvhwZMWePtp4JmpRGlvBiJAlvvcB7+9gyJgwVRopOkyCRLDXCqwQL'
    'Rptq5qAKgU5F6CxivqwSZbW46kWEmVbU2px7d9FeMBraLYFDy6quZdPpvEuWhagkxPTYuL3Tx9aWX3ruVBMhmzxChpIDvAnM'
    '9msRgOWC7gRm0rpJoWVM/Gkg+FyX8SHUGzpFU+IPgISCwmvxtVLvjmHlYRkjjx4jcZcSccxFE6bEl6hYRJJ0hJjyPWYnDTXt'
    'x+fccW2ugd3fKq68UF3C18ko2+Vq/+Dy8RfILUx1f/ymdT+poRnLU82hONS/RlUFeSirC72BilXs0LicRWGIcSTbcKYTKAmF'
    'vUPBp5jwUPeCGOqVqPgdSX6EyTzU41y1ZS6manjLysUhS0gBRnHNEKmmcJey9zSXyyxjKF/OCPAksasGl1ORLbHkjVbRszax'
    '6WLKAOxi+po9RFfp/uZQrxJFTtRq1FKoaGW0rSJHo2lGG8JzbXgpRZL+0SdK+H0SepJYEUGaFE3WUbg7OSXmGAoUk8sisW4W'
    'eRmXRAtRWkVIRhV5kiR/ipJfcskp+8Y4M1SsOCWqajiu8zqeDIrjBidvqphc+liGw08AKI6N6Zq/hXpOtMK9r3UpwPsxyaea'
    'bWVrUKEa5CQoAnR7YgyGsZ9aKDhjqZxjgtDIi1/r+UbL829cZ2d1Op2dfEUq6tjABj0KaThq3SlZfz62zljKVbW4VIrRHH7O'
    '3m8NdaZSXS+VZ8rUMbFXnVhrKlEUm9vRebID41zntJdFMn8W4lkCtXn96AgqTIUIyuNWjzXVfFNeMooJYtJM3KJizlW8poNy'
    'UlrzFFu0l4w1vCOktPOU+EERmpDwuUSyUkpNhUivlYJ+3GZ/ZL5rUPEkA0yaNOUoc0wSFBpbw345m4wEV7G0XKrQlOTBUrgu'
    'X2VKcvrSdVBipnCxBhLNHBXlKJh2SlAApJ54pM0fWq6PW4EBE69Ykg9M51nh0dR5ZqVofi5RL0iwfN6ee9XpECGS0v+OHqYS'
    '8SdCy3EVqhz/JEtcEZl1V7irStlwxithV7qV0BGYhvNILtttZAk1Unl5FQoLs0p7aLHseSUbT5/lgmIqI/xxCSCUTQV5sPOh'
    'Aye+3MnF62QyRWCpxpCHDRGlSaJsJD2rhJe+grbr+qkgT1Jhc9Cbt7lGtaxWkkAO9Mh0rSQ1I1pouRB+7r8w8+dZo5/icFE+'
    'dMyMT64BYIIyefHQJibKEXEpeKLqhquZWmoEz+JLVHGBp04wY4zRoagT9VDCoGMBD0twpEwP+BQXipfdFEtP8nmcBs7rnkyc'
    'oc/aRAQVckMmcf4iuEsb2so25JHbMKVWVEdODRmcV7kOd5QS178KOgctxfw9XRY05YOqisoUfffKnbA4qAnMBlsQunz7946Q'
    'qv2X00hvqjXwiSiHx8SHWaWXQkPix/EPXiS7sRGpDyDmfvpGvL+/+xS1wUcFuKM6xaTkDAdbGmfvy13Jbum149muK65f4s6c'
    'nG9J3zMB30olQCUXLnuRxOIQTe8nub1BGXIqSNQB5eUGhSKRlGN7Rrwg+XaPTRw64ZS7GDUn1szyz7QA6ae03Jb30qiorJHf'
    '2me4xkkRtdj2J68F9ye4oAZ8TGNl1N4LTQpkRHn3e+21oG/WJiATwGzM85hvB44sNsZgYeaHXCgNcNp38hwAWvwikadxsHBY'
    'QMzVaBJL93mopx0REXhrHRH74li1WyngnnrlXH2NDM/dlPPOH9aF/oHlo26oZeqKg9hBO7zT9Q+UD6Sp544W3fQQ418dRv7p'
    '/wD9LtHr'
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
