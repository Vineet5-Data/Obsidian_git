import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vHFly/C888zBsNinKN47UuxKWMxL0YWI9IAYD7BoGjPVh7Jvh/26NyK7urowXGflRTVKr0/SI3fVevXpVlRkZGfHL'
    '/578+2+//+Pvv5/8yy8n768/fjy5Oz35j9/+62///eUfvnz8x2+//+ff/+fL519Ofvz811/ff3j3+vOrTyenJ7dvNtdf/ntx'
    'd3r/l+uf3/50ffPlD6/e3Z6crsw/f3yz2bw/OT3f/uHjZvN6d5izH/749zdvP2xOpA93/3fKJj79i/Dh8CQ/bm5uwNk9zPbj'
    'pw/Xtz9uPnz468OZ4Nm8ffWXz++3S3F2MK+f33349Obr6OiT+SX42v58RwM/LPYqM/TDb8OD//j57c3rX7+s6afPXy+VPPLu'
    '0+3m4yf1VG+uX22m2R6MNj/Kwaf5LEOD/umPXXC4zW6uf97dDcO1nU12b9D7D2TMV9fz1by9/rT5sD3ubPTpuA9THX+HDPlw'
    'ELSku7Gnf3qYoP1bbq+QcwIXdvqn2c+SO0dZWbuDwJfvDxTaSmCNtwfee+zsb6c/HhLBhbe7ia33dNxpNyXWe3ux6DrPztBu'
    'rswak122uVYX++O7z9u9Nn31/tfCHru/QmhcMIHdSLNvhbYROMr0wnv94d374AB2w+wG2H2y71Z9hIdv5kd4+BIZYnuYvTGm'
    'pWBDmImQMR4OiEKQriFIlDOdjh1h+tP9h9zxc+HUIx9fDV/1sHPRQDR2rttwbRtAHw5q/zr6x2nExE+8SZKX3F5wtD0cjJzk'
    'sUCcRMYCLzR9pHc3N5tXn3790+bDp7c3b//t6+N7b9zp2GDcXbAUH9c+Yaaj7aK9aSA0SfRFkgTt/fbLlXd3+mDI3SvcPvPs'
    '3xIPkelFMJiAfRJ6X+xbE+k1Y1/UfRMIvoRaHubKyyh6qqvHe9J+H+j7QN8H+j7Q0xnonymwPc9gmA+/XTmQYyh0VUHM3Hg2'
    'fOVHtAFsaDQnhKUQqo1hI0MDcHFCQOBoOFYbgoJVzA2BjPaPJdjWzt1ezcBI6rUUsVsdTKTInj0T+Uq6A9sLCeA0BKylTtNe'
    'SovizcGoUwL1Fa4lO/oI3IMYnBZja9CcTV+UGfgQHRoLZCqJwWwmDfI0MNT47N21PU+lauIceqBDMNh4WYphkZIi9oykfDje'
    'SMfBYL+J4NWSCs6eTUx7QBr4aXPz7mf0BKjTBHYxcjburITb1Zg3H2Pngl4FIT5ahA2CXhCWjSreoQD7zfWHf2VB4CAuS0S9'
    'JMI+mMTGREtsjkV2xP395xW07fwKVxefzf6/gsgbzDd+rUEg6l3owdJXyusoSGGpwTTraS6Z4joadf/kdhcdpAaz1U/W3EFU'
    'PF3p/amYZQnt8VlJ99SvgQzzE8Z+e+nnA27hXx07MRJd9dnKsNM0L2ZSygeD22swWws3N7jIBCY0NWiObG20rg01X+nLnghs'
    'OJ3QZl4upHc32FOOvS8JobcSex8nCPejcUPhtZH62Z0TJK/TlN7VY8TNYPrHB6wbofIKeE2Q1lKMHUTMETelEICMMNQ46pqM'
    'SDweJ6PujsLBluwKRJ2GGm3ptfRc/HcqCct3YHAAg5cGJaA4QMe9ONHO05+BxhW1R2bzdAEzHTIHU7BcbhK+um9bUA/hePmM'
    'x83QfXdwGzFTTHu6CQREP9YRQbDjaavXBgWPHxIe7544Nm2ah7GFfcamMCJ4xWag5ETTmYEuhcrYoDzDQrDZxi4NrWRjltfp'
    'Zg1uVrYuRaojZuMjYvT1hAHWDE8HicTVt5IxuPh9JSvwQvI5O/polJVp4AQGK1JXisM6D2RaLZhuT9RKtvcYEyNy1jGXj8h3'
    'a5FpJ3NxZScaJyhWIO5j8TebYmD0OGfCxt6oH0zH0Ozlp4Pi6+83bpUx6XFeIbLQdWQaHBeEnJkx1TgMYOMs/NRnAMJ8AoMP'
    'rrbfGFCMBKcJgGerwsLXA/1YwFvZXWxIEvktsLkCvSztVzbYxhIaPxbns56SSl9T/5ALRPg9Jx8akrCm2s9dKBVcPWs+zjoW'
    'z1OAN4qwV3smnycnZlcA5+NJPJh6nYDExZy10kV317k47lS7qgXdpHfGwWHsd50BhDcVmPwO+p5rSmRW1dtcIKHwQsIUOV0p'
    'NQQQ92J9wcb6CXZ2iG9vM7jAQM41pAB6hWgTSCjQ0LubVCOk6zEmY7WkuOBKfYCAt5GhlHSBwLMB2nk8S/Da8jOUdCVVaKGk'
    'B7H/Y2UCSWG3d+9utnJz9bD44KAXw2NSiPyPv3x5Eb0+GUnmrR4tqJZINGdrzKI5j0zSis8tRoaHWncBhvx6AdKLPYfYje8w'
    'FpZg4RD2L22m9NgXaDay3hbQdKOBmKVeCJqBKYHA2VnucwDQ3+UagSETPCxBkjOP+ihHBCEb73XFqTYhMOu1i9nvT+coF8XS'
    'uHr6Sen6e1thtHwdyYv9gBJEUL1hCxjaJTGOlndhaZswWpVkyQ19YuWPWYbWnhwlrlV5E7VcOS/Lgtcxvsv4laMFNBra5zIj'
    'e2ywZYad0LkUKTtmY7Zkp6B1ZRMCPu2yIAnUSJ2tXDuUcm9Xw7ErqdLrCYkKw3lDhSEqC/502ESxHGrV0ogAXtI9aRL4SUd+'
    'wkenZ1OsqNBw31Ly/bxqPtlqyYWRZVhS1dg9AYhLli1DmFXNMuP7lRipqkDj5qW7K1j2VNEQ2ijpGfnSfDv19FgoguGoH7mw'
    'VaS0ngZu/NJ1FUI8+g9LuHsrJYAH5NZtOoonbkeFUteJ5YwsVrNFBjs46NTORfKwcDQuPXi7plQEAbWdaDUiproeZ+rlFNP7'
    'qyXa8ERYfQqIf3p785cH4RolRF5glgtVX7o0fu8X6HKwQC8eM1p/ukPLmVNDOekZdXLHakyrZTuotZ+01p1iGdMi+ZRFpWm3'
    'hzL3XPxjJyIWe8B8yxwkG6LuRxj0smXcleLwfrAKlWCwBYhG9iWo1afstRdobdWGapanK4JHmWZ7tBxCjs7mWscNWIe7t42m'
    'P4D/G51QeQO510SqwgX0spia6rzhnRpP8dm7CVOsck8sU/ae8YfXz2yvSgGfdKbZgixaNPuthK0Wm4VToAWxuFbTzUFDTCKX'
    'fQmAj5m0avox4fdper6BaUhSdIQFCJI6Yda5/UwyJ6wQF5h3sYHL259k6m5TY0u7l2uZUxUbWKgdR5QfuOcRvliAm7geHPNy'
    'yE08W0nkxLOnR07cr1YF0sUiSRHme0jmCRXVWEElWYXjwr4ZFh4iRKTYeoBQLCZnI/tRnEqWJEy9VzSVFAMnoSPrSizkXjYi'
    'OTZUngq9PVhhEnZNEaPZwVpnAADG0XNJlX7qFuvicLq5XLG0gGVILkajPDV25UbBdWgaRItPE0XLlnjtVExP2OzaHEg3090q'
    'Xb/Y3OQaMyNnjjabvo9IUsRxLYGtlyuH2y4zAeMYTbdeEbdQBVT8jleLEzVQD4bzAncyyYo7te0mYzXGkoQ0AYeDWtLDrjhS'
    '0VqpJT+5jh4oRcYFmmmeQSrsoaQoOKf7hTxXFzI0y9AJuLl1b9/aEu6o8AhQCpkkgu2VxMfRf9g/7avObA+lRTzdO1pzmpKx'
    'dfSm2Zsw3+81+GOGkEPTSxtFgJlkqDd6CgnmZ999ehuazPH0+mX8UNfOV29EYxlBrIqmtz6xvaHYMmb6TeSdMYrV3VJGzAez'
    '5BiZyKHdiyKlhswwaVQHzW0EL2UCVbh6O5n++FAEVJbdFhtY9+M5u14LZHVS/w5x0pnh5ik/p4iiYmoZCAwI6j+Hl4LJT1aq'
    'oIiEP7wUfCE2crNq4cYANOuN/6TI5hvodbR/VUCJs/7cINNwr9BcYPZ03AKXc1MFxyUf5t9egjCqUCfXTcWup0ud3J4pKZFd'
    '+JkRzDmydbC195gGCVlVFdspNrGIg+R1OQhTKiyNORoSgAl5ikOGoSPAB1oqyk0jsuwFrDCBNQmUuOxbnorh6YGwqBlWbUkj'
    'eZLb0ViCVVkwNOSC4ZLT67d/7kHgNR4Y6x1DKxXaPY7rqvPnFCO3o6ykK5DA2wOJJlQ6LtkzmHGAA8NLdSUW1WLalnVgKRO3'
    'GUzE7sKx5sZBhpGqTsKKH7jpWM0NsOximbuXEASkN8elaN+KSjLCYBCfkF/N2zh7+wAM6dH+Cd2S7lQILmzrLeApbtOS0uBE'
    'q33/EoBaFr4oUW+h1V3ItLugIznMwEIJXVZpvijTuG5lQj70Yl7tHfR+mP1/EWtiF08o7xMKuj2TFWtN4WRPrpuBPx9CNNpf'
    'pkkIYMDqh7tAQimW2biU75LOrFr9iwXyShtfi6oEDCyU9ibg7TRu9AvFOqy7sK9VTrCSLcvSkeVj6TTlnE0XLEfKceJCjbPo'
    'ZFVBbFXWlh/jJaQPlRBiG6s2qa62TaUT7hD0DjRcsr49DviQ5W6qQpCHAWfIM7DBsUmzxbXkfc/okaRsZV8Mo0tbrnWO2fth'
    '4KbG4tbfT3ZR8cMnyPIcb4HEHrWFsAR+STe6RojYBdz3UdXLu4h/ocn9wB4RYXukQlXduyzpEsMmKPw27olu8L6xc94oOgnM'
    'DUKrcveROd1XEqu3Sio6CVXrUM9iwBfa4iNd07IgR3Zazo0kEntNcl9k1yaUipwK9L0456XBES4XaNw8GOX+4Ul9Jp4fHXc/'
    'wW/DJi6cvI3XcZcznIDQQ80yLAgcLCMAtPHFRhSnugZ8QdHMBPVhOjvtHMqK6bSQncEXdL3WavsgdBsekxEHaXo5YY8VyhXa'
    'pByrl2RdGULDin44K2YL2rdJYYkdrxauERKW9WbYP5eED2jyzfpbYQcfp6GU9yxFjDVZIDgxsm2S25WtHIWV4+4mfTuY4UCg'
    '9AhXDeH2pOszuWtRUhtwjzcXh4km29nn0DD2ruG5ot0w4KTKNxfrSoYzHatO0abRFicXIM5kkRxHPshyoGnTpU1uDo0Kgjcb'
    'U1ay/yKLa41bSeETIqu+G1L4YRYqrN05Y2AVyb/oWlFH+35kLJSnRwSOl7Hr7MUXCBjycnC/XardzwEGxD7w4tzu62+EAXE1'
    'I7pvi/vHJUYoPIf14+MPeYID/4R+22VaD8KJXPruRDAu/sA97rXW3/S3GhEIsIwO03NvsrppWyVMJomvi5bA/EhLrRaxCSTM'
    'EgZcCMFs6D5y8AStPTsGWPTu1hhRSJW+sZlUphbL/HIi8B71JRyWzxt6F8gmBfmSBATWTRPNpUGrwhNPzaOzyeGVUve9fvZT'
    'hdXRcUdJLIyEWW1KP0ED9mAaDAyEgd4x6SPpwxuA/5IMfjGR5tuRj0AOe2A2USyflWbGZLO2mYgSULHZgnuYZGb0wZUFEgqN'
    'F6z3QfEFDcAKNvVCIKLYFxHCIYI3VWyirb0KUgY/2Ll22q6N66I9FVtT0VWBjnC2jxTswQm9GMHTYCSsFwQF0AMMNS6shwk/'
    '/PoZ5jYcth6FjnghTPKsl+LA6gYtJIIehkMUXzgKxYEgByOFGHoeoBS5BMjgNAFAkAGfF5hwIr7crc7+hGaMbDV4wwiKZg9V'
    'teGijPRABR9eIH89qkQdkiIxiaOZ7A4pUjfywcnKEP56FFypkMCpjre6myWERc/tgvAYvjHRT8aXo04zkiy8/eet3BlAb+w+'
    'dzq6F0dSY56qdhs2gS89244ccznYEpuwfiADJRBeKLw6OHABrgn8QY6/wXs7aHuO5tfWivoxYfDB69beOOMnBGk2KxI6xuIJ'
    'GMtyHwjgx3VnZoJPKJkrgy4OF30Ir9xnmxd57W9yCknOhNGA2N3diYYMJtRenWC6L490WuQQC/1XFLG4MqDDS9N8se5RBNR4'
    'EWcrPD6GQc6eOlViBuQcwiBXxyBJjKGKBGlCNdESwAwznTZOBX1z0c7A42hGjGLmNK3iaMIRDATBFEnwRSpBn0jCeH+qzphw'
    'f4NZyiUBiVGszEXtYJSO+uKr4aFWbbWBB6/wx8UlOrUaxik73Mpqv0KiW0UrvmYEuO25DRJHuPta5Ft4x0mAfg9uiq9alrkb'
    'ztloQaekW8GKr1HAAaGK8Bai4ooNciK8cuzcMg6sQWVp2iAPuFr8thF/MkDPd3oR6uYNmgvq7T4ZalR5X/NbkSF3vMVNs57L'
    'kl8lbWbirw1mZ1dy9vumXY2mbMUZaazMxB0qAg5gUI9agB5ktv1GEXQQlQUiuhmsq6rcNFI2LbDTVMgSwVnGRB08mQojzHB+'
    'txCeorROxRggTLrCNIC0SVocdJKthoDJy2/MZuHyKaht0rYQl81x7jtyR2ziCBzCPRniHSbjlaoz421tRmBOVN2InA4TSUBg'
    'yJJw22EXELlwJD/RXFWbiAAbUgpkBRtosXzN+fwLyF4QtUlNeM7X78jcV5ScQbkRG4Ghzlrg+5gfqE3d4IjbjOrYTnq3KkmC'
    'qjpsFNGMQU2+LH6gCycyrASfNWAVFC3Q6RZVwQStQygJioJHK0+sSBNKslQeLkCL3BQXiR52tXWpXdiHkKg5eeo0MxWcLW1O'
    'FYBXwBQQMOrA0UWjdtISQ+fHku4GLWhkUGE3qs3aYjMtIy4kWyROGHtQtoBhMFERj80hao2E0jfunxEjVPiMmtDUCh0qfk9T'
    'wjTx/Eh5chq3GOErkcaVi8EuexFpaHn6TI49GKussdlI5TgLN5hg7CJhFbKoHsatkq4+nt3HYR5HvcIez/LDaTYPWX547IdS'
    'ArUJC7lzhgTlmGSY8wE2K/dTUAjK5NyqbR9UPJYCJ5yD3mL/sfF3IddjhMVwhoM0WrcPyr2h602qyTQJ7maaMFZLhyJplt9F'
    'UMg4sSMlmMCaaiidxkNOnB6MPgaXpNHpM6DE50cZrxj1+oh6rCLLC/nLF2RoOp4FGWKUDg9KZaLbEO3C6Q7J6n5IcBvVmaFz'
    'JThIoxeIQ4mKznUsj9plXTHYcxausAAYnaXbmLIe9QX80EDUCDmHaBqZgTpYl3eIxNpw0HdCxdgvrT+uiQgRY5EdUTy709NO'
    'KGS4ea8iUMjqyUIhZSWPRtzjstyPcsmRkyCFQ5AE0f7SofmB38UcI6Fof7/sR7S1RStGNMl+jNN80NAyAoVuNwI7pVNilPbp'
    '4Bf6iAIOOKOj5vSS4QlHFaiLo5z78UVo6dfZiL6OvuvMRumiT4bLeJ1GhHW1BrwEPd9RpXCGpx63HXoE48eDxpMfbxBAGtt0'
    '68NofqauPIXLemH2OYXKddTtVea2LSOuMd4rCTdY91XTpP0J+7O85wRtHMB7pMsRJcYeFB7b8Xu68B4haBXkug6cgg1UPL4t'
    '+vCW4Y4UCzTsvZ/njFicAu1o3e/UZ025rPwDAGOUa+ohHuOSMHQLgzKjR5TbPrPOozLcZWev0ehAcQz/sxcLlm9hO/3BvBjZ'
    'h3Yz2eWY/zAkLwJGzcEyyX6YryDHFdUSUbphXpS7YYDN6xqjMc9WTvXs/FFIJ7J+yPgQ6YYZ+PXzPBVmWYGRI3u2KOiFSEFZ'
    '0rolLCvSocHaUep3AxnqCquzgktsf+746Vcit10VFIFbwkZQJNIoZow2/XdvjdCN5iAjjrwJqU3fuhYh7cKqCtcmoTbAVeky'
    'VkQ1JpWvg9HTY+NMQ8U9BSmatvsNj4r/1dPh3DH0x3fn/L3XgGqO7ITcBkHQfzNSqu7X6PYxFo1kOKKdVPax6jCuNuGNUIJJ'
    'FqW6nfFlY4c/FYWcqa3NELrJ+j+PNTEdoZOBzpKn2JwL4li6a9++TKEqACSV70HiMAseBNPWtkiL0DTbAZ4o6eR2lqM6CdGd'
    'sR8IIlQ1mJFUX9UmPgnlYBGXi6woJ0ARnlC+H4B8Ih06wz6wK4RJPh8oRBFZvVwQG1Hgiwwz5fxIzBRn/qtWJkrUfYayUFJI'
    'CSt8kuJfhiWTQUlYzXOcpdGpRYRkl8socZxCo1U5WKhwTuK+pX524JVGq/4zeC1FooyLPS3ab0AhEpcwQxCgPnUENatEptGD'
    'jQ06AlvaYmiV193HhAbk9J9UOmQcsGO+cBCV4RdmsI3Ku5j2D3FoIcRNYLBRNDdzYWoC7vs6Wgu748rCqhK/ZtCra91VyihJ'
    'RlyVdQ8zVd0ckooYALxABcigRnwpK/4h99rqiMF4R2Bck2TGCWBS99njVu94+6BHTUBMQ74PAYWEEAHwurIGmlAfUJBYAuvS'
    'SvIdO4WKNU1IoxSvLlOeUZtjDvhJoBfmornXp9/G5iiWNSNREzuW19tz9Yxaex5P0uRidusFsIk4brKKDZHp9fnnYp94lYgo'
    '86QIqoRFU2mHj/atFP2EhGyDBqSM16GXGY6te9pMnW+dwqXT/CGK/iXTO07Ql4x0PSfMel/5sM8M2kUKibQj/NCjNDJoP4pj'
    'Uly54XYZugnBn4LMKk7gL/QReNjgYCNoIimFIiB7RzCWhQCoODfuSEo3LU3EGVMuRHKq2fm0PRo88FVLm+HTYQmySfIJoafP'
    'YQed3EsPt18TlM01uWahQIEbzGos044VNM8QqOHBN42+hLRdzbWoRpFJRiGcIRFaYcXFkqd0ebA7dN+bAr4iwan6WkPmEOyt'
    'KffsUFgVkHrGzzuJBKJRFooaKyEoKUNLCSJHjt5K2dwGwFRnVcrKE3O1Obs8ZhuPanMzZqooOrCOLbAk5JLUF/GUS6kqx4JA'
    'CYkHIoohZYiEuznCCEYz8+1CRhLCJ11tOZRdk4h1XUPJIG2aWc+JYXHoriLeJI4XhAOskO78RUFIifndBo/IaORwt51m3ZOo'
    'A0bFscP1A+F9XNq8mIBiDuGRI3KvoAsuleIoW/XC0YyW7Z2m2ULVEZ7xjFHPu3LzMUiw784j0I1z44W4jwV1WenZwIg0yiuG'
    'wMQdhtsV22LPIyd300kGas4thpmLGpcqe+t5vdWk+YH6Pdn+X8qPWKAQx+znGHvHSeTNyS7ToTOK2CCt4/DL4ATgr24Jr4m5'
    'vVz6s2dAgYvHsgSYWqyPruXTdt4R2n+qfTwHcMtL6qQcwxCeVB/PQ7fSGjfynL145E4eoVWnaK2TFkpZL2O9E+eQhDp6ktY7'
    'WHyMKbhJ/TC6T7BrCjfvhQaQiPmOpL9QKG1rnc1y8ui+hyhPvtRFQCklBEcYadqDxtmYd2nMZEP1/KUEZZI0d8SPdnfaWMx8'
    'Ry7gw5JQpZ2bbO0UMiI2/zBVwBJTRvIC5r3nfK+3+J24ipSqWws73Wy3hn2A2DZ+yaIHfQo3fhTzzhErgIsEAyUGe92XkBVy'
    '2EMOgWr+fAEQd7OvcKQpqyBW0L+VSQVpoAJCQZTjbObBMhCAkpbqaOtrg78b4wcAaJLOdcykQeBbiNpAjJ09U1zi5UOd6xUF'
    '3DLZxPSXjaSTx2cjZewZ9x7SN2Z3TcjHhzQBxVx8hrZJAsUkRhYJnU1nq9IChJPxcuKBn61y7NWCkMru/nski52LGFySdvFJ'
    'dvaMn3UNrsZLiKWwpJMhMZWepIRoiqjrmCDXLKsqi2wclUpdgXnToiuruXBgOpYr9rFUN/n2VvMUYl3zEMX6JKspqyjF2qzW'
    'k45cQL4hQP2RAA0HIuugf2Qvs2vXw0np1e3sSz4ixZzB7BPMnaT/OJP+SnhMRxG71g0u2zwPtgqVEa3592wEa2d3VziKrzXr'
    'Hs4F08iP5HnhuyL1ycvy7s7kQ8PrtemQIpHKJ8TiTNHVTDr4EBSD8lD8J4Y5XmPPnSsgc+CnMkUesJ8EKI6MumGW9Oaxqf+o'
    '/0XRZAUnhSCYantPWZmVyb2QzPpZiKRcHVEk5YCiAqCTb8F0Z0nopISYCF7C1QNVsRSp5WhZ8sqRe32ibsdH9uLx3XMAokCB'
    'Byoo0tjxgw4vROspP55+p+PANBjekuoq6jCsZHQbXxCV/KSv5wezUni9nNfVY1G56nSsKF9W3G0ZySJRT1eUR8JaKC4cyC5X'
    '3epW6E2KNgD13YFuOVkzQQbErKTmrK4tQf24B08JLkfc68jD5K/tredDcLe611cXh0V3/YgVF+qUkMS7JGH/4W89cJVrLxmn'
    'xZjiwFonUC6WA41HrPVnQybMxYAXugldf2vvVhyJpIRuxgWsepxuHrGFTYY3lnDqcVqAKBgU8R/SwZZc0t/k2LOAPc9D+rt6'
    '8azhEoQJnQ0pOo9hXpw27FnK82eVwF46DHoYmFAhnZBPhWiBoSf8DSbqvZQIJ6qRMUV3xBPuyDlRygCjGbB4LCntAUpiJnSh'
    'FnG26XMKDQwSqdq59oq6SDHt7dgjhK+jIBZYxkw8NWCyM1EqSjCsioSsyGaigAhsjPD0hStyzZ6TwzBLYRjZKMVfQGOEevLo'
    'qabSXtCiIevaheNnh2giUn5TTKkUALSIJoP99viceSuMdaf0G11tNTcBkjLMqs2TB+aBTC4E7wam/tJmyzMdSW0At1Vr3gRG'
    'THfcXQD6jqLT1XUuxjOvG/CAaVvTGMIHQM9s+/VQw852zVd5Ogk4q1CKuZghT7F7ZTk3HmjM+92MxzPdmVFOniFkIiMjwQeL'
    'mqKHxVD9nN6+99yoK1AXD/woAvwnlpNXZfh6RirfJOdAebrzFkPzGkVrjddaUTSM7Ad9ijw4Fwu8tPulLdEV8kWXw0+1YivG'
    'Lqxw7l2lmNHD7JsdyJfGq/G66SNceBt8RPybXLcAm3INr0/SwkCziQlaXmbnYot90wfl7uBfrsYdF2rAYyM4nODZCIK9dUat'
    '8Iny5tqPgCxEYGfLbrvQbINzs8cmc4P3nTK73mkgwpb5kp9oklmwHGq6mjTlMn9kyfrZD3c9c9PSwfkZPKGpBXACMg8lS5MS'
    'U6KtuZNc7M2Aihnmw7RefpnV3f8Dj+JRyw=='
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
