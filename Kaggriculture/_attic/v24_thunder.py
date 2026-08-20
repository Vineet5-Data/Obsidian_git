"""v24: family-A route THUNDER 144167 (5COW/10SHEEP), fresh pool 90630506_p0, plus weed repair + price-impact SELL ordering."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vW8mR/S961oNJfYxn3xSbiY1oLEOSQyQDYTDAZhEgyD7M7tsi/30VSyIvb1WdOvXRJOX4yTRF8lZ3V3fXx6lTP//fyX/9'
    '+ts//vrbyX/8fPL56u7u5OH05G+//vd//s/jG48v//Hrb3//6/8+vv755MPH29XjX7kXv/vy51+uPn386er65PTk3c365HQp3r77'
    'sFp9nvzhbrV6//j2+sPq6v7k9IfZ2z+trm8+nZwuNh//fHvz/su7++03Lh4e/nm6M56P7/745fP2SYvJ2H4+Wa/u7r/K+unm9v7D'
    '11ebt2YvdifibnV9vX3qwnzq5gPTp27+Op2Uj9fvf3mc/Psvz7PHyaFOghDn+Sc0EbbTYj8yNwfgoc9fORs/8vmvT6TZLrmy+PO3'
    'ps+er/X11bvVZiZ3HiHHpj1UvAIP+/10f+xO7rMY/9Kpf/3W4/8/3W/2jP5O5MnvruYTOJPlcaqu7le3s1cvD91+aiYGmtnZWbQR'
    'Yir56urOeHrol7c/KKdp84jNi7ubL850yScoir6RePPDvdM114n2WRMqIOVXnvn0IrfwW3nRilUmTR4/k8OgNFvPWsMs8+n004n5'
    'QsomN2fPxM0PwgEzSOibfAdcIxm9Q9OXORee35nIuX3HelTuAcpkbf40e2RyBFt5xQ8/vQj8LvooMK/A1160kPmsddEGbkj00Zvr'
    '69W7+19+v7q9/3j98S9fZ617CPuQZ27kgY++nGffRS+LHtkq3z8KPdpnJ2ayBKfntjsb8DefP3AO/c3ITg992/YTajY//DbrlGG9'
    'j9kIo6YpIoOcpgbPtXOSpCvO20Ti7Is92p7hrX3ryqBMMBKha4q3TpInoDLBgTlSpjjgaQ7XYel+dE3wRAUSZufcfU56eft+csHU'
    'jlxdiXspdsw2XEKZq2eEHuZu48LZlz/xhlwl6eMteG94z3GPssQBNvDuDc2Yf5DbN21qytyjaa86Fnb/v6WvZF2O2YuSq8HkU+bZ'
    't7itfTrKS4n9MOG4OD84zEw/bfMC7ehq4U4yQuwfrm7/FL+z5ia+GrV/FiUdJ1HMyOCcIOt9+9vzREbm7jMCyaVlk2q1Waz0wmnx'
    'ejfUXlhB7Ywq+bfaAHh3Dvq8mrYVLJvpYm1/cOfd+PrJtQIZRt8ySR1ypUTPxkmSuVdGo6kchanayezKywtlRYu/aCVuqibI86W2'
    'vPiqBp5ZIi2ExXgvs+IzpM+9o/Ex9+1jv//4h0HmP73DmnzNStyMOBAtU2dglCw0Z08CxqZMkyMHRepwqdjZ+5b9xn25mq8th1Xy'
    'BPfh9UW8D/vYP2gKC1jLx5HCCqRIijmsrUGXyqBRKbBMfBO4H72h4bIX7asx4TKHV6jDPetaooH2wRzLmUxl1bBrg3JZL47Kzc3j'
    'P4s3L27IozX5vlB+8OzF3N3fXq1/t7q9/fPjb/9oYjyWDxmXTTFoZl4XW0eRuKOVCgMZNpSutXxBnyxLIlg8l9mQS2JXpVwBfD5v'
    'RuhxSgXAHHi6b3/goQef3uivGchxboZe/L3JFkubjAL0qz2ZK7WI3Ei23ihVCOEpUBY0tY7AblNi4ThSji6SUYqlSQRKgoxJTaub'
    'NFpAVctWVonknz05FwfVnPKr+RkI5ymYt2BXNZQ1sm6R8PI1oJac+Qqs3kADTiky0A57M3+YNM9VsdQVNabJ3QXG26X8mZJTdAXV'
    '1tMVIuBYG/tN+ys69ANFatJqgnPdsfXyATlQ/TNs9ZCnIwttYLqwhlK0XAOwJN7f0de6ZFNKedQlOxAUBjt6i4AvJ30S4LGcJ8qF'
    'tcTZ5QOP0N715RbZMmX7OJNFdbK8KluvLC9oadCQ5jm7ou5tq197RcQRgiDg86/iiUxTzXPLWimjT9hTQjmkfQzQC0Otpc0LZJf7'
    'CcdnPQwYRioCpBbn1+pMV2y5tFy1qV7wZh6hH87aMMqxjkCT3MqVUwqshJ7w/B015qvt4Yg5QLiXzjHhTpAUH0LNeBAUBT3cOYDo'
    'Ul+4FYRFa5Yrx6YFn8L8T6u5BgUpmauC1sKmwIKsTEjL70ZwRosfDJzR5eT9nz5e//GF4idkBsbi5Qs/Mm0yV8QsP5LryLZZxQ0p'
    'byxpLOoGa43pBp0I1LlmC1KMCMOILGm51mNhW8vEuHIZmGR3PNg1d828wr4Q8qYKQex8xICWG2bHQLoy00w2gD0zE5Qm86qTM0OV'
    'iwCxKilh1O1zS3Y+bXdn9aJkA27GrXgZGnkS72PJcW+fxS++KUNymCA9TBUQ8YMEajvCmJe4cd2Vyxn4qHQb6C0ReMzCmeRptnnY'
    'V3TvaRU5tfk5Q1vlcxVKpp61lfbqJAAgw5YloAxvLdcCpMEn5S31vT0IuQRnAuTztmr4sx7AEhJiLjlW0BBd5dwTOK/Tm5Ikm3G3'
    'gBlVopoz6CYkpEDFbKSbYENcRsSjWROQiiLXk8JoitTCwkjFaIOPpU+OLg3DgUp9M1n1SoVDgbROJVk3JmdL3IgQCWtmnteNbgHt'
    'I62Aq5IiPFUcNmV/rPGWaN8cAPOl2rhYr8L67xI/yxWUCibWFOVwgtt3mGt+BVBW3IbOI7CQKhr7QZtS5Ndrws2Xmo5RwryE1Lf3'
    'tzefOVCyKt+O5ZSX2U42KX6F4nOEZG6VT+bwhZibKd68EAqC5nZ5PmpuDfVlfJHtCJ4G1accywhCI+I+zTXJLRHg5ldx1CdUGxEB'
    'N+oB5OuZUqdqp8s9Lcyq9JmZ9F5VwEW+FIVerac026Vcv2WkxoZ1vTtCD4VOJCx4zMjQTeuElmcNCDK1+8Zku2qxCL8G5tRByRoR'
    'XsIaucjA1dCAl9onE8O0EKMAI1LA/YpLdhvq1IZig37daIfMKwBMSg5+t0PENLPOUWEBHgLSO3IIe8P5ac0EZhPBYBQZILxmikfW'
    'EaELbT8FJCDoVfTA2SxmuzcKZI9Z5u1Y9DksLKBgebTm2rvSy6nEym0Cemk+4SBbkzmSmGY2jIIGFZuHBMs4CNi0xGGEw1ooFkuh'
    'B7ogOPbxw+5E+npXcsr73JUQvouiAs06qYRf9753YdlpUBNPObrEJJwS2charQsoKPQUVbv2Z8+KyQ5SCxsVVLLRcnirfWliZpRs'
    'wD+Zkm/QskIUFEEVmBf0aaJU3yKHusa2pV5YufiIss8yhXBFSAQRUA0NxskUdIgMToCQqJ4+mYrbrVDFF81H24GANumizDpUZ//g'
    'm2n4xMHkq3GmdEHm2UMA2IdjXXbSv4fWDZjVIGVZgbQsAqYy8AucrH1GsrMm65W39Jvx+oDWzhVFTfa38CvaKuz7rblWn0CjVKg+'
    'BcMgFuS8SYFYkzWgXyXK3NUdURjTFgzwUrlidnwASk95on0sAYb0Ws2lMxWwoWypk5sSD+OjiT1lpoqXS8UVA9FuG10Pg2IJxn9t'
    'PrUzKVkZjApUvQWkOKpKFCmex63OxNy17beRCxXBuSc2u2jfMqJ/WtC7OGOgBj+0gf+PCW9wGM8nVsiFem9q7tH5Q4Chy8yKn9NF'
    'lgT9WY3xU06XndyHXYwyxXEEywrl06F718m1pGldaXaWsCNIZhAC7cwyoL5GBxFTwjVzDBI6HwdEsKgH+4Sp7QLb2EN8OWyZPT/b'
    'e9wFkO8RpPoLGT+yFUhVeHZZ8hh5dCl1K39sKXKcQyGtZ8+Y/PSaPU1P1frjMO+UfqRAp6pSjaAsKn8z6RU3UVaPjHOP0tegyZtL'
    '/55VV23x7PghpE5YEWiOgA9r5/JkWFxuZ88DXve2eJPJO1wr6BYYVOVhh6+2vfM96n5PfeXTDuzf2VZqMAIFDvsLZ+w9QKBUE10e'
    'puB/LznHNveZyS62OsihnOK6sagVGGRDc4qdxn6AanZMNtEz5I1sou2B79c39dONdtSgyfWUKUeukXdbxjqqXQHfLN3us6JoOFQC'
    'sp7jSk1hfrKLOSCSnTSt4/07P/K47+g7h3APspSDTWP6pq+yLt5jFD9rUnb8TKmV8vklUxZIam4dhHozaGjsxSkJjwX9d1wSfH/Q'
    'v0Ge81zPcw7hLxsDK+XSnK89qdmG7tQtA4o8syOBGUkUAluZKMktZjRJ+B7OKzUlMY8E5AdVtjb/jDlFeZ1D0melwt6sY4jdjPbc'
    'pTSTKcexf7K7lJ1oITI+hRlB6QU7a8QVvomXN6K6ylnQkgNmfETPL4L6HX6Vr9tdu42/wxoMYELRDGUE9ukjWDN1jDV2CWXgWu4P'
    'aWVLwpFKM6opKCW1JyndA7tcodyV2R722kIs1SDH1bvTUbZK5iWVAlRAclawEoDDownqJSxjWdRSmjLJvDbIRz4uaXr43fbu1u9S'
    '3fUwle8xGPZ6cqfKN0R7UPUvl/gvfXWgUaCzMkhVzDPDHeELk3qAz6iiCInXkndLFrMiAQ+dBE6AJtV6p+dv7WpN2wCHQqEnymaO'
    'gsF/HwoZrZfakjT8/so1paqnUjIpRWWvAFlbKN3y28jeVxiLCFt7R0qFlwwlN+squzk1akmY3QQ+w1cY4961yegQpG3bvsqqJJGR'
    'RyhqVJYcY+TLhgN0WezreuoYj1KZTPGu9LuZ/o0NSkE1GEbYZj13UWqoqLj5/Z2qy3kJRd7hioNajWH4uxbTDQ0gkJqT97EiJBmi'
    'IkN5gbwm5XcDaiu7bGACD6npQWEIQXY3DdriyDVOwNgg0KV9OPqpUaEXM8Ki9Re4/JaiLscSfmFeWCF+L6SyHBlSQdVQxI0cbfMO'
    'zL/pwY6ppHvks91anZwE2pCqu+SS6McEJjxZKKPi71FURq8pFgTXQdEqi0fpaONAsOYT5lYLESC8leOVwfCs0fQvsEwNzSiosmGO'
    'gNus22xmDYw4WlQBrByBugaZgo183/LiRuF4tnh38rnRE0kbx9T0rghqF7dh39wCDFSh0wtRQKzE0QzedaFMEr0H7INS3ynO7Luq'
    'zkNryOgeeyMwsRzFsJw3iHOgPCihBKXyKpccpYbIMSquoEw3jovbNmqyBzuTuUOhJgkn0S/QBCeABtCJsxFxuJEWWgACfBlDDskX'
    'MqU1EF0SA30E6rnIOWyL0ORXVz0PdjrLnUPOvClS4EcRKVHY9c4OFhZ5pcx5mpfIUIlmgx5ZPvGywGOpxjnxxnAGNLDPkVIfM0c5'
    'C3xvgVe0MZiTaIoIsHkMwznCZDfBosLVU4oRQBJMH3fNFJprFZTD+AnSrYlWS+nerN12L5PbdcmYragS8MdzpONgvuygE8WnitfS'
    'tfTRpAECD1oAGH2MQGTW1UoqrTQktZZQTGRG0D3cIjsRgnKU9dKiHDQVX6ChAoLlZDhEYm07uwIzwiJDPbbMt0LelzpoN9nhePwg'
    'fJFzDZUnz7reO46tU5hJOXFnwok7fyiVUaAuhn5nsi5EQbLa5Ov2afWnd4o4dqo7FsLRPjPc59nyvDaH+uhwBoG29KEQe967RjjO'
    'YAZ8UFOvNZG1X7t9oLIik76J6qfAxq5H62cTyHOaKApaTxDpW0TYKn4MDZMfCC6oEz8QvhDLKQLhBsxCMCwQHIwA90J2cQSFptfD'
    '9ghHekHcApFkfYwSnq7KWDHWspPrzq9Rgta+xs8Pz228LplOaQzGQJl5dNyG8oUIUcA03GZ3b3gyCyX92ggSao4CAnoWfHh7gThF'
    'P4yYbPw+5+hXXYzzENWmT3Svv0VpfMaLw5ciDiliVWe7cqZETJECMyH6YhmASqoq7hhE76FI6+3VUgVjLK2/JrLpFCdIM9zA7EfO'
    'hkI2ZwC/8xdvarEaGW5K9mpX4gNUrOntQzm+8taKr7zpJ8U8yqKNowuv2IwZNVYNYKarX7rggRKLswB9N1kdopzwtpj+JdDeXhvx'
    'fOnFG1ZIjCOOjMktvVpdpgiPHUEbUhhAF/kATOGg0AoaXoS3g+/JXajmaOonoBja1FDJ+Bf+uZK7ZG/MTBMDfXNQpZw4paoU4zKp'
    'zDx4ygsqwOosKS0kemDW1idh8BOl3pZXnRzG1af4OXTxFQJ/MHmVWmrU7SBVcsNRuzoeYQ2tsLGcK+U1xSJ25uvIrsB+hmGgK7yT'
    'MytoQVCZ6CoZ4VipcHM0nFtUZ5XgUeWAy9Q9QxxTmXIKIa2t71oIJqSZ/ELh3pK4mzjWaqWaTvZ/URKKIR3GwarY9ZQB53hBS+Pv'
    '25IlFK0PLbnDrW8vn4KT0DErcvRKNMzMyS9Ytrig8isBX1sB9AlYXd980mq34IADZd6xk1RRWoChpOYyptJiKYH7h3qaMmNkeGmK'
    '5y7P4SwZkcMWIKWoyvSFcm8gRiaH4BWZUZFVE/dsBGJpPCYaiiN4qCZOi1XL2C06LlL0N08ny/mU7GYaaL2EdWG5aq+hgdVXSoIT'
    '4xOwEp274c3zhyGdh2DSHgg9CKKWqZlpkjdfO9M3hUdeQgPhCapWRQCC2dZDHmILmqyD4n993YfCPqYeRtxDJyKKVCQ380fViohk'
    'UZorYLKJN9XTh2lv5pj62WZJAZ5lCq1XRiYyyD0vTCn1nGfbXJmuRhXn5tLTWCasG2fx8DgJ5FugzZQb6MUhtORsQjoWkp7PvvpD'
    'c7XRMjtEhzYTikThiGMtQMMseh58bZJ4MDyzyYbayCFhHFEJxqFCYrtIQHfeYeUl8FcVDxTVWPHdQlRaPOWnSSIVrl6uhKsrevWm'
    'n1+sfWtkmnlSRR97tXxoLY+Th8dLuNMCeZ3LEMS3UB93LLEIiI4JdQ8K9kq6OCyfL4cKwrCu8yDatLlrUnAIpmOyxz5KRLfqsMiH'
    'J9Mli+8gCD+EvjggxS4fYcFTMLi9c7LjEiYEAuErxTXIhFSSLZfociCH6jGSuDtkIybUYClDm8wPr2OLJeisGzoYeanupoLBercm'
    'vFQc1Wy5txAqr8qAM+PxoVJ0xUnah3q2QUagLo3LkQcR3IDsgdihRBVkmVaRRfdwc2rpqCbf+QAqAn/S5M36/GvmMIFoGKSVqHc9'
    'TAAAkBtVqzsSMgYLzKmwogFtZjsgxc46REi1y/GDzwUqDhaxjXIq5VlHMhDBmw8osIdGXVKwalctHOty21XR3FktYpPxOIqUOqE8'
    'tUrKp1Dcj0bjqwoh1VFifl5BTyzEhQgK84JtshYXA+JqKDUGuRRDwxnbOQsKzHUAP3wzLcQwVKHKHt9jy8vsvv/4ByIWlQOQHLjz'
    'lq6YqFjL8zz3G9HI9Jt/WU7dyLVgHtq3Shit7pZdbCWepgYvg3v5V37r5S8JMznTxgu2ubWWiKk6RDNTWk7ZagqjNL0okrykX5Yg'
    '1lMXViqd0jQqsojF36aeMm9ACTDmjVdYiRHxoJw4jgQZSqopph+SKFoUOYAKt/5k85vYHpIhXtol/HmSqhMFiFC12qrU2Fy/8Kpn'
    'TeGa9CwEuRzusJWKMf874DiimLZVR/FtYA8SKWvleNDQPHaUDLbudC9D9Y63rz+FyE49zLSm8e750Y9flV61t9EqBe2AWGp+3Igr'
    'k1S+p2bc2cErETMn9LwZiRIUk9Ed5sSxjye1qEOZg7PeKTC50WiCd58cgyriCAkLdqZG6b/yV88k33cX5PKhPWKoTLwyLOUtqac8'
    'mi+tVr7KLr7TtB1ZozmGXwyZ0ALs5henzWKNi4Ht6UKjwzxyCwwb2V9Pu9hCweqMDh6zxr531IAgMZtNJn+UzfFgLwqOypbrD7Xv'
    'BnqY7D7OquVR0O2n1x5sVcBYfU52IVZTl642xovD0b955bs8n8KhC5FZMuYoXVyAmQFUQcGyZQ+h6gFmICEaUYUGSuOCbQIdtCbe'
    'STGodM+6hBrhIO4YsMcQACh2VFCtD2C+jVQatVMQAYsJtMOz18TFlUov3kmFrtN4TdiDLbI6GqGNZu9DjBbeP7izIx3BRmY7l+hf'
    '46MBJTsxDjqxP5SpULIgKjcPtZExNI5isZOFcrv+ipvv02KuWlSe8UXIumE5mdgJUYIIF8aAlwToFHW0oJ0SGHJGR/w6w8sIRwF7'
    'ZsFzXC1Zx0ws/FEAsfEMiaQkBZOKoyLrqLPEbVGwLLXDlDhM1lgNNbNQ1wiEqYb1WNAYwN58kwDBY4nVRcI7Xvzt4qG/f2VM4qY8'
    'eaptpfKZQO+FQb0qcR2RQxrE56sP3qQSmtfM1dbfmBK/IoF5r6AbJSbdynYDLTahdOh6vNkv9ALdZ+tJZCE60VBmDUD5Dl1fCluy'
    'x2EKAQmTBaGIGIqFpeUmV5khoOHB1oDFaY3VQ3o4R1TtWZ07WjOpgjkkqX9zwMJST1M5hrLqVMLqUESNgS81PT0RgPwHydJUD47L'
    '72Xa5BEwdhdVZ+ePYG2gGfeuGDQ0jEnBh2CaNIBXco+hkIOmtB60SdJMBi8neISbD8ruidKKCfnlbKEiTNhWJhWRn1G4r7g87uZb'
    'Lq0w5YJhFH9CJX2PHiSiByqYZYmpu4gmjl6vxQAAqL/pYgwQg0d7ObavIiWqSba6l9aJWREHMgIFuyNCS4jKGo8qm+tqgIisTVw/'
    'OYRbK9O8EGc1Uu2WjqAXIUffFqOTwD2CenZYsBkh5GEKdnQraKQSuyaPCs9yptmZXHqTFC5POlbho4NhouO7njqIhyzckD84SDmp'
    'IWB0S7rSFMIKMocJVDyKTid0ZLqrpSgSwasT30oVFeNo2uiIKCQOJHF0He0laYEpuiUG3Lg/xix3k8DGPU4w3TYkQv63Z0kKo5oC'
    'jYKgJsNrVCI0nypBIGwd7CTXSWakY/+UjIuMIDGUTD2T6e3Pw3FB1QmpQqGSagjJIab6GsxbvlFiR9+ZqfqjSojriOMHJSAVKuP7'
    'oC522QERoZD9d7gjiJtGjCbf/w4lUWHaDIcPeNvrSPrjqV53tfQjluLO9tDjqKi0Vxpfivlez2ZK4zmcqjyqdop5x+BjaW++5zL0'
    'r1inzce39BeB5ZvxUexS3rBQciFQR4XIkSmmn0q5BFE5tqohE+Tx0dSyksWUZs4SuZs0DAi4yDRsklP9MeZc0Nnr5J0a2z9wUGqk'
    'J3pKslh9os5lZ+FFDZhX/8DuLoTrYNu4ScKBYEM9xNOqCGVgcQhFDEMEY1aIJOkjSi+3aBJUhAOQd8Di32EuctfuIrN2CTgSZlPj'
    '+rfiInBQuwrOoHSBlgJi8WKADnEOGABshRUo0aIZ2sn2iaRFgi1Q230Yxr2kjRMAbn3KJQm0itPScUoWY6DnaJmUetE0t54MkjdH'
    '6lxMYAiLXOsAOT003irFZa+JGsq6HI6daL5S+9TZhDEnkDrvPz6MbbYYYS3aY0NFWOIGL4fjbJtIOBRHx2mOr+pcEdPwVoeRdwN0'
    'aG0tDW0YOIR0VMJQiUaETlFbsthnZE9Bh6l7/udkLDlZ6eUQZ9iWcLbiZ40V38khwUBbrkaO7PyhEFxoyZi22kI2H4JCZV6wKXCL'
    'Uh3n+HMRlfkEiGaYID3EtDjFJQF4eLirGMN0FahKGeaFUv7QKGn2BJb4LsPxyOAHcs+ZlmoX3wJlil/yi+9NI2GwyjcAQ6xXuCBn'
    '/PNx/5M2EdQMUHwWCOq26jowidS25/Mtfvn+776LoUTyfHPSyaOkhWE1w8E6BD3yXKtjwgd1vpVkyvSXx8l8qvsq15FkHfIfHXaJ'
    'hPvm1bbD3oFtrq63H3Gjm14/FqQMwTulun/YyTFFFhaL5XLPh6DC9W46Xm8pZSDzZGqYrSbcvtqkZux2IUimtxl+QKWJExZS0dRZ'
    'psxrGTeX2pVRsnKSsprtm4CIO6X/L0HNNwHrdW2zikKxGRERFUFCQg5+a7UZQrq4jHRlefjnw/8DviPEqg=='
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
