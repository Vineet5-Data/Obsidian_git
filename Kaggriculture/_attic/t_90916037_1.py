"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vW8cR/S965oNJfdjum2IzsRDFMiS5RGoIQYCmKFCkD2nfiv73KhY/Lu/MnDkzs3tJqXkyTZG8s7uzu/Nx5syX/5z8'
    '7efffv3lt5M/fTn5dHl3d/IwO/n7z//8678e33h8+evPv/3jl38/vv5y8uHqdvn4V+7FN59//Ony49UPl9cns5N3N6uT2UK8'
    'ffdhufw0+MPdcvn+8e3Vh+Xl/cns9ejtH5bXNx9PZvPtxz/d3rz//O5+943zh4f/zvbGc/Xu+8+fdk+aD8b25WS1vLv/KuvH'
    'm9v7D19fbd8avdifiLvl9fXuqXPzqdsPDJ+6/etwUq6u3//0OPn3n9ezx8mhToIQZ/0Tmgi7abEfmZsD8ND1V077j3z86wNp'
    'dkuuLP74reGzx2t9ffluuZ3JvUfIsWkPFa/Aw74d7o/9yV2L8btO/f5bj///eL/dM/o7kSe/uxxP4EiWx6m6vF/ejl5tHrr7'
    '1EgMNLOjs2grxFDy5eWd8fTQL+9+UE7T9hHbF3c3n53pkk9QFH0r8faH207XWCeaz5pQASm/8synF7mF38mLVqwyafL4GRwG'
    'pdlaaw2zzLPhpxPzhZRNbs42Ezc+CDvMIKFv8h1wjWT0Dk1f5lxYvzOQc/eO9ajcA5TJ2v5p9MjkCHbyih9+ehH4XfRRYF6B'
    'r220kPmsddEGbkj00Zvr6+W7+5++Xd7eX11f/eXrrLUewhTyjI088NHNefaH6GXRI1vlj49Cj3btxAyWYHZmu7MBf3P9gTPo'
    'b0Z2eujbtp9Qs/nht1mnDOt9zEboNU0RGeQ0NfBcW06SdMV5m0icfbFH2zO8s29dGZQJRiK0muKdk+QJqExwYI6UKQ54mt11'
    'WLofrSZ4oAIJs3PsPie9vKmfXDC1I1dX4l6KHbMNLqHM1dNDD3O3ceHsy594Xa6S9PEWvDe857hHWeIA63j3hmbMP8jtmzY1'
    'Ze7RNKmOhd3/l/SVrMsxelFyNZh8yjj7Fre1Z728lNgPE46L84PdzPRZMy/Qjq4W7iQjxP7h8vbP8TtrbOKrUfu1KOk4iWJG'
    'BucEWe+73x4nMjJ3nxFILi2bVKvtYqUXTovXu6H2wgpqZ1TJv9UGwLtz0OfVtK1g2QwXa/eDe+/G10+uFcgw+pZJ6pArJXq2'
    'TpLMvTIaTeUoTNVOZlc2L5QVLf6ilbipmiDrS21x/lUNPLNEWgjz/l5mxWdIn3tH42NO7WO/v/quk/lP77BGvmYlbkYciJap'
    '0zFKFpqzJwFjU6bJkYMitXCp2Nl7yX7jVK7mc8thlTzBKby+iPdhH/sHTWEBa/k4UliBFEkxh7Uz6FIZNCoFlolvAvejbWi4'
    '7EX7aky4zOEVauGetVqijvbBGMuZTGXVsGttclmrm5vHf+avkD/y+6Q9WpPvC+UHay/m7v72cvXN8vb2x8dnvjUxHouHjMum'
    'GDQjr4uto0jc0UqFgQwbStdavqBPlgURLB7LbMglsatSrgA+nzcj9DilAmAOPN23P/DQg09v6K8ZyHFuhjb+3mCLpU1GAfrV'
    'nsyVWkRuJFtvlCqE8BQoC5paR2C3KbFwHClHF0kvxdIkAiVBxqSm1U0aLaCqZSerRPKPnpyLg2pO+eX4DITzFMxbsKsayhpZ'
    't0h4+Rqglpz5CqxeRwNOKTLQDnszf5g0z1Wx1BU1psndBcbbpfyZklN0BdXW0xUi4Fgb+037Kzr0A0Vq0mqCc91i6+UDcqD6'
    'p9vqIU9HFtrAdGENpWi5BmBJvL+jr7WSTSnlUZfsQFAY7OjNA76c9EmAx3KWKBfWEmcXDzxCe9+Xm2fLlO3jTBbVyfKqbL2y'
    'vKClQUOa5+yKuretfu0VEUcIgoDPv4onMkw1jy1rpYw+YU8J5ZD2MUAvdLWWti+QXe4nHNd6GDCMVARILc6v1Zku2XJpuWpD'
    'veDNPEI/nLVhlGMVgSa5lSszCqyEnrD+jhrz1fZwxBwg3EvnmHAnSIoPoWY8CIqCHu4dQHSpL9wKwqI1y5Vj04JPYf6n1VyD'
    'gpTMVUFrYVNgQVYmpMnvUvbdD1fX36/ZfEakMa+NSP9F2AqMhcvnfmDaJK7gDb+94c8dW3UMrZqxF6a8wKTtqNuvNeIbdEBQ'
    'x5wtSDFADAO0pCFbD43tDBXjBmZQk63Dw671a6YZpgLMmyoEofQRe1pumD176dLMOtl49sxMUJrMq07OKlXuBUSypERVd88t'
    'mf20GZ7Vi5JJuB234nRoXEq8yyXHvXsWv/imDMlhgmwxVU/EDxKobQ/bXsLIdc8uZ++jSm6gt0QcMotukqfZ9mFfwb6zKpBq'
    '+3OGtsrnKgxNbdZWmq+DeICMYpZwM7zxXIuXBp+UN9wnexAA/ryRHsJp1RFgPYIFANDMOYrQKHPmk19wVuRKTZCi+tSci5z3'
    'wAw/UQMa9CYSUqASONKbsIExPaLYrKVIxZ7rqWQ0RWo5YqTOtIErpk+OLg3DnEp9M1krSwVRgbRO/VkvJA9CMayYWWY4hgtB'
    'Edq3WgIXh+NNLXiAyk5a4c0T2Ebp2QQ4G9WOxkoZ3jxN9QBcKyiRFDwNGomvaYiutsr2w66VxXOck3zxkEkfaBOOYg2+hAt+'
    'bmHmR5u797c3nzjktG7uDQ219LzSOC6h3dITQ5PedqoBvMF2LbbzvX0h1gdN9OIsMtGnbWRGPujTMKK6cVqZ5gHdRk5mv44h'
    'MKUwUhEScKsRQL42c6qm+5gkX9RtLsxrW1+eki4wg1yKkDgcmaof1vtvMWOF3igsnM3w+YeVS4vTBpg2GO9Q/uhX5MwczK4R'
    'YHbxgfMzU/NSqLphA5Txmwvzk7HxW8BWAGUpwJNdPN+Z9ubCfFMZIo66yDQIQNQUwYOy6QCucXEQPVRG4JDgRLG4oFoOACsZ'
    '9L5mDEeWj4NEbpdUaR8RXz8PS85CzNuGn3wQpZ0lYsHzsC6iDapQIi9lWpQqAwqonhlCIlborNHuM96m+p3YASNGG4NazMOV'
    'UVgkdNjgIBkK9VIYhiIQyEYGgQJXDMth73QlwV0g0ib2Ilg2uEhehVBWG5UAL71zF313rpIeD+rljGN0LNVoowiaUloJKncQ'
    'QiVw+Y+eFdub2g8q6XmURV9OpaiZ8WmtqUbXw+7wCWEGwipXAgPLcUQcY/pUAQrcngssOvdgXGkl6zq62EYCw3NSBk3QJeNG'
    'lTWJPf0ypyYnfW17eKWdHbRrsi0SqhhtuhHaxeFKgTQ7gqKE0oahmFg1wTAY9kYvHmAC78oBrMlmgxHakNQBf9c23ktQm4hx'
    'bYvggQcykp22snodIcP1qPn8k4dl1lFCVMFBXsXsEoNI9CUXOlErDSjQx4QBDxYqE9CvEgGwmDBcNFmMIqycylkxOz62pU2x'
    'pX0sAb73WgWpMxWwPW6pL50SQfMA5jzakyuaVRxfKhoZCIPbYV8YTUv0L9DmUzuTknXOqNzWW8BAuCpJ+GIFcIXlq+b1S8SY'
    'hA+QqW/OPbG1J/d/VZAgk9D7MIXXLwCZcBj/J1Z1hvqGas7Q2UOAXWwXVoCCoopQgrqtxlYqp8tOJ8IOTJlKPoIhhvLg0C3r'
    '5GLSlLQ0s0zY7YOkm8EJbw4EzbiDmM6uMT8iofNxXAQLfrBPmNousE07xPXDcgLwsz3hLoBclQAOUMgLkm1MqsKzy5LP8KJL'
    'qbXyx5Yix5cU0nr2jMlPr9mPVc8Ghzmz9CMFulCFMgVtUfmbSS+Bj1KQZFx5BAgFDepc6vqsumqLZ0cLIc/DkkB7BDxWO98k'
    'g+ByO3v+7qptezqZOMIVi27dQVUedvhqyz7ff27vly99joTpXWuldiRQrTFd8GKKcIDn/F8chp1g2szjmsds0c6hZrKLTV3m'
    'UE6x0F4j4iV3zSm2NP8DxLl9someaW9kE22ffFpvNQADj5heEWdUphy5tuTNMtZR7Qp4a+nmpRVFw8ETkPVsUDqbyU9yBAZt'
    's5OmvTy9OySP+xZIXYR7kKUSbBrTN4aVdfEeo3hegwLlNSNYKgogy8tBUnOIw6+2tobmX5xRsQtAs5zDObQEfzzoZeY5n2z6'
    'CyPP+bYb+9qEFesD+uWXmvdsBvfUTQWKDLRFjjOSSwTGM1G8W0x6kng+nHpqlOc8EtQfVNna/DP2FeWGdsmwVQqB054i9jua'
    'pzel3Ux5ku0nu5WyEx1S+mc5I7C9YOOQuMI34hmOqK5yFjRJEzNOo+coQf0Ov6IzlwTMQ1G7YPnrkqjMT7W/gzhQH9KaKXus'
    '8VBAJjqKy6BNTpLKRKpZKiX7JynqA7tc4QaWCSH22kKs2yAN1nano4SWTF0qFayAHq1gJQAXSBPUy2nGEq2lTGaSVK6T03xc'
    '0pSylJPimddu8fyoPfusQ398eVXlG6LtqfqXC/wXDgR9Om3OVhX31PBH+FKlbpleROeGOjYfSz4Yyf+Ms8b767n+/r5WNUvr'
    'ts82D+D5pugMcPzYktQrjoN86Lp6SzdldlvZIkDADDPcwbLiGNkIm5yXGi8kWMrZ/Q+WhtlW4DN8RTLu3OvHl7j8+96rrEYS'
    'iXvtfHK3PNhGynFQcoUhSaS8xIf+ci9VyRT5KodSPcyY1RSq1TJCStOgBbKRpBIOqDTslqcKJi9VBOmuItIxitd1gI2ZHVwg'
    'b0e5vTJsYrT7AFjxQKqTcTepFnRLiV6pKUQLyXOcSoxgrSSsckWhC3paJMV0aIv5q3bV40eFtDBR8s8oYsO8sNIBXhRm0aEU'
    'nWLbJ27laMd7YAgOD3xMS91GPtvZ1ZlNhu8CjCLRADspMOHTBqiMsYcXpMPvGhxSXniOLFc8aHlbBSQ7Hw/qYtZDLIeYnkYx'
    'U6o12oqgCootSXx3wB0cT9jbB3xPyuo6ySDHUAU3yREW3UfbHCRcyLbV9mDyERGL0zUwVMjccDO4oKaQa66d5LR+2weevgvK'
    'M8pTAZBxPO2V0s0O9+scdnti2IyMCQEYH5RJQt1xSu3aXX42AIVRpp+5J8t4PBlTsEVDATBUbc23aEFgFxWYjHpronACyYeR'
    'jB1x5fgAj4MQOqWoFiFEDPAx3vvufp+/qtHA1zsVIlsoj0TZa87pxA3OB+/sn4V6Y8eDxEpAvGdhyL94DhQBEFHAcJNmAyFZ'
    'gvKywH25yznx+pAQtKD2IsU+ZtZznHsuDaYfJbpyT+vRrQg0OkOaDn1vlBDkIFW50qus30Pyu3dW3fB25LzJLI28UGLULa4N'
    'KaAeMq7khF3vgm09wNQhJDvtqcOn6LCd1XY9BwgMYa4xWCWhr6a/2SEZPxs7znZtywKAiEoyRCGX2bcR31pxhrkKFyNtX4mx'
    'QfIJ5FopcgZ8T3mHuMAWJUYjHSIH1wUaWj/5BW8NFyh8rSg+ychUnu8NCsE2AIQGDOXU8uYeKngN6X9rtwnClxTRAyp8n/H8'
    'R8pcFKPWdKwwJ354QvHB997alZ0cJTW+qcTDQZ42En9iJAMK3AIoQ6oOmAMt6IYWyMNFXcyW9SJMCrS5xPKq0p08aQ1BY+fw'
    'TjtM4aZR7mD6MdqBMquWJs6Uqmmn0fjtUAziulWhO14AJQc71YYGczIllzRf4MJtHdwIFaP7U2iBSJlLstk1deQC3zwVhEyj'
    'IDBljOIQIIxAapHmDYAPqdoK0oVts0IJLAQox4COJ8akFDgyKGxEdtvgo0DJ63vropiY5w8BJAUD9oG1lNF1iASPFM8Zxhvi'
    'MDg8qxtCu0BoKWADKkqNEBN6wM4nYFpPorr6oNoRNXsgwVTc5M7YnYl6HPhkrXTDR6TsCA2T88vVnLryZA2NwCGuGPM05A2r'
    'LVmZQhlZpdNJriTzf78pqzJ5jCOHLcMupwZI4uXyeBxdmMWmuLD5PSSSIUz0ocPwtC+d83CM+WnPHokUyhB1C+LPnkqlSohD'
    'o5nEnbhQmTBPABOxWrZI2IM09+4jftFljmLCzPjCBGVnFspkbThM20SoA1BqL0zc0a+jAQuVQvlCokl7ICMc2LauBFrgTI/6'
    '8mwWTE94xtXLwm+UN4gNGtJAhnCzWrPfHs+DmKHJfDeKdTeG+Sjoi5yrxtSjB5bMi6Q36LsCMU/8MRVgXgiTecQpczrAlRz8'
    'CtRp9QdzSEYI0clZTq10FhVdRMh1MZmPUrmEIJAUbQ4M5u6f/+ZvlCoN5fUjHf8k9zEKmcK0lcIdkkBHqZ6KFW2Z6d11IusG'
    'Pj3o/7OJ3drxQ92RX17ffNQ6A2aYs7ToqRKUIdVvO4G7sYm5dfduedBMY1cJdrKuM5raZ8kwMOUKJYWwSjY1qapy/EqUEOdY'
    'Mp12PSQgivC5LDZ4NbWYI7Jg9sBVMhR4UYrloSAwKhZcAY6n1jVkT+O0+rDub9CFxKPNF8cOSNvDUL4SK7x4eYg0UDtvJYbj'
    'FMeJLkgEPRlX99KQwCbC0RriiqhB1TDGS5ilmK3GKc+YptKsES8ry8bj+EMl575Nk1PP99TtMzSuZqg2Dx7lbxrACmh43zic'
    'x5gmmQq8qIcHxgVqGdr4a3qjtKLLBlFRWPG6MPmQCkci2jCnZwqxAzFePFSNQ95KHFQCEHVmYkwYABvfBzhPFtV462jYQulS'
    'xXaOQ8SnHmUgSRpzEePNp5Cbi9JUiupBPgJF3S4CddtagAJD3OQeV4CTfDdEOddWQDbXR5BvMGZalzFnnCAo0eqvgMPJtWpq'
    'Ihnk6MX0K2E2mDe+B6rsc/lgB8EGIhTSpc/Mq7wilAm2hQii2WLli/sMLbzHT8VNYsC37U8+zVdbsqAQnxJJI8QXkQXCPG9F'
    '/OaMIARSoz+DINEEsZ79MTUhdz5mMiAbEYeYRoNQuPODkCzDcaNkjQkFDFyYkSrGlc/MEhxC5ooPtbuywRIYnQYZaSmpj4DJ'
    'Nep0aMMPNSHIt50t0y7pQS0IqKSKKactH/RoY0i6IajHmQ7dHO4s19kHR2r91PK0hYME9xq77wwHOqGBLTZYnBQKlSutItlz'
    '6zONIh2rhq3YOVhgrpVSloTHC6VjShmOk7fS4tmTDxwbXNAmOt0RvYtgToZP980OBFnTdlQbTYIDoNuK4ZxTDJGRUTKSYcwD'
    'jtKppWDXq4KCOfE35UaF+YosEq+RtknAp+r0Ay5uDhqnxEAcAyrBNk9QJ6kJKUe3Yogf/0MFxLnCze0cBCBMwcCWYj27SkTg'
    '1V5i1Icy4crebcWYNenQemwYOnsrw2SL51dRahKJm1HCEpzq+HBVVENO8IKsF73o2ciMbOSQG07DgtGowFy79mm7nUWpmiq8'
    '5VO2edKH//7qu1ABbF/USL3/k19RiJLlXmRu2uBGhrR9s56+KadpQbYfFgdHq/ST0tPHYim1Q2YzuM2/8lubvyTMazvGCHbn'
    'kvTk8FgDVTfV5ZTkOzqIjXbAUZ5lsxq4Lx0OODrlAKcBuh5JG5ypdk01YPDauel3FI/2C1Shy0gQuDgl5shh+fbOIlBztA9Z'
    'mvXPdjC3LmnrVE6mfMsTDcvEtnaDGcaWx1UBcOsYGdKC5fvZqVtL3jRkmD3H/i9p5RSrWwHVKFsY8CHAZqsqTt1ED20OYX9s'
    'kAzfZvx2Q6dKEad1+pinEgk3evMQoi9m+vmNIE9kQ+6tLupv+Hxa/FmqrCS9ySA7HTNOgOS3/pSqFcERbnzge/2JaLZdK6Ae'
    'O0JAWakKaoNQC9RpT+mukMUey+mP9R3U/SFKZjPm7e8ht9dDon+Egf075tLNfbyuaoy/BARglI7uzIX4BHsIvunYQ5A5i8lx'
    'z+lB9u07COTWzJ8Iz92hmxNy+D+mGfCzaWEIbylcZLpawiLTI+h1GLYQfAaoQ/dF9CBlHiOdNvxYt/N6I8VlJC7jlMaCHyMq'
    'zyfqshhv7V4msPMHz8StMseHC0fz8JGBhmwVBkjPEWGOdCdFEkC6g5FYTFl2TW2dpos6OpJMP9r9ouXgSGI4WGDAY4BQ4ln5'
    'ZR86C9BvBXa+ULU2bGehsHV5l4MGeiWZC9D+iLRfkLkkjVlN80e0BpFMJC/ElerMVgYzpBT4KTkD1IkR3/4ogsQskO5vnz9k'
    '+CBtn3EeOrIZEkWqL0topZRDzLby7Mi2VwosI5vjmdSzejy7kQcA1ILioNBaDY9h7C2IjyTiLwSrAZJfKXC1Dw5zSopjkIFt'
    'UAaOonywFSkZjlosUiG6zXFsHRoKwdqr5xSlO3ueETgmFMfQS2jBtfOHLk0/mS7DUfG79vzErkMbifM9P3EbRrJPJhvCO2TL'
    'Txju4vjhKDOu2vITF6Q5cbkWda0T9vvUDQUfg3o0bT+9lCWHomTQHAfo9amctAnuvkoQLrRxHPjJinFl/e0tnZn61kBYbn8z'
    'xDoSAy+a1np2ppGGBzLyQOSkjtsQHaKRgHsQueIDdjsYyZLf06ivQ7GWEfWPTDXz/T1wx00UFEPdDWInSrMWDhyjv0PkkClw'
    'dYPX6BLyqi24kuskWZ9GUedEEyAfskbXlguG5kjZMCYGkm/F7/NWhW2Eix8LjrcSTGIDqYHEkU+tBFawGSFp80Cm17KOcn5u'
    'FCLO3xx7lCRVHnlE/TjPcHdMiEKyf9CESPQnItPQz5qcC6/uxCBrm65U8qjbZ8KOBYjCIcPcFOmPGSLtYeBQx9/sksQGR5jR'
    'Dte1kooYNmrl1rJHJUX+wMa3EhHRZNdJjCTz8uYtSa/6dZKkFgT6cmKN2pT8VptHRnUuQQDUqDjCdZpI5n8S5ZekLQKsX25F'
    'eYVKyQmlxmCMJM1aJKRd7zG7alFsKl/QuB6myx+BLESwo3zuJtRGU4WHhIIbipHtAQpQdJmBpCj5uIBqyFlXAgKwQlF5LAGd'
    'iPbs5J1OBkfDUE8xAI4x5CYnsRJv0TZfiDjLLNCqTiqo3oqRYgHHf/LWgrlARSZOY9VnbZEPAsxy9CVnJu3Vy6g509KES4Ib'
    '1QXI+FmVTV3wKLJz1qfXYHagQd7z7t0HDzOOckNCjHKAxdv4puZjLQdrUegxfPHNAAO98KbtXcixk7I8U+Z70RBqvW8hnclH'
    'KUTmHYO6pXt7Q7SGXpY/WrDVrJIuG+zw6qwABwQTXJigro5mO+c6v0V7cIb8cM2HjvcJxY0FMAQoc5CgWI7CEM4xJcLShj7H'
    'gxIXkYCZ2EZyeuh67CTpQwIU2Ehnap8ggOBBsoFwqp/KAEQcRfa5y7MIE1RQqJ/cAB+FoEn5rrwAKWUbXDt3HFWUQlwwosOD'
    '5wNJp3L6EIn5eUaWWuwFA6X6YGQdoyCNA0eKXunymthVEpJHdyB2CgaRBlAFjf4BYy3x4iGwF2GRInU7s1W+qapKuQ2V0mOb'
    '6j/aFdtpfIDSJTGcoMLE5MWola/A3gorsbusaCFRHhWjBwMxLDRwsukkYO9qg+CyNpYSKzw93sjgsVPWMy/8A6IBosqHH3Ur'
    'P1sRtOxct8bj6MgIXh1r20W2dKswjAN0UjRcmwNUXSW6JQJ2yUkaIi7JwqnA5uvQytAr5oJ/b1LVQPclpIq3SnUXyUoi1tsC'
    'sbmQRqLmLH4rB6KBb8iUDvf8gyEHcHwmpQoj4mTgi+mmmIsCJBtWykw4jtJ7Zq3Cd27bLjL7DhKkow/HCnQIhPTMgbmkpkOK'
    'QgTkiXgvEtSIrLXgDok1PQMuWD85SL+vtxhd0CPHIAPbys1EgGx8njetoR/9m7lFio/4kxtd+uhv7lmZjGMxfPyHkAtcCUlx'
    'fONTzY9npwr2jFtRxLeB6cJ8ydC5IWyBmJFC5kkJLyLRHi3YLJcr5MmgU1ztd7QtACfg0ogRwxj2Qkkua7IfSKfF9UuO/Ah8'
    'ulrR85NRS0mGzieZ8lYE8OCBAd7RjGy+Wwq7pTtkuKjHTgK5wbgz4E/F9mGovWew7DXRyFSJhHMCYQ7lpTcSIJLso4cvZ5Lj'
    'FjYqjfXHszpJeAE7TWYoqbIPZF6OG8XG+H+lEA1c+I2opN5KQVYgM4/z2DLPx/LXLM4FbF2jUnijUU22gbHJDKNkbOVGP/64'
    '592Mxkg0pLR6DXkwZcA0OpIeEYHuK98YX/LwP4xoEDM='
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
