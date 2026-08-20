import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vW1ly/C961oNIUV9509jcjLGakSHbK2wGxGCAbBAg2DxM8hbkv8crieTlPdXVVX0OZXviJxMyee/5Pt3V1dW//M/J'
    'v/32+9//9vvJP/1y8sOnd3dvf31/++Hjp4f1yeb05N9/+89//a/P//P5499/+/0//vbfnz//cvLju6f/1T788Omvv97+/O6n'
    '27uT05M3948np8vmzx9+XK/fT/7jw3r99vOfH39c3348Ob2a/fmn9d39zyeni93X3z/cv/305uP+F5ebzf+eTjv2/t2bP396'
    'v3/TYtK3X04e1x8+PrX15/uHjz8+fdr9afbhcCA+rO/u9m89n791+7jJq0BDpq/df5pPBWrA7HXh7MEe7lryNCeLg76+fIu8'
    '6/3d7Zt1NJ6oP9sfgLfN2k3e+vKT6Xg27Xj628/7xXDQ15eZCr6WjvD6dv7+/fK4/bh+mC+i+d8OVw9cusv5Ivpw/2m+iNrF'
    '+ad/7IyDv8x6x6ayHZzDAZ6N0r5/b25flub2S887c9J1ay73w9W+dDsK02+l0wX2H5ocsBOaFUze8jL2YMwmw9HMWPsdfcZe'
    'xp0O3cFz5ztvP4TtNAXrciEcbmAzhEcrP1sOuqCNLDp08snbtlQfS/kv+TyCIXw5YcAcZfOmD+LuHbsPn8/eD+iDN3D7ce95'
    '8Ms36aSPfT6d8CEd2P528qahz00/fIHHzm6V88CaTA5T4wIZ89T52eps31dvwdweIV9tzIgxLXhzf3e3fvPx1z+tHz6+u3v3'
    'L4dnwqDBK7/EWCLldxxpDra39qQ94R7aOSKzLwdX+cXGsAC/6vVvzO+8j6u6d5vaf502CTDvGvNxYoSDhVvxM4AxAvcE7tXL'
    '0rbMZN6HaW+zPqYDCBx7wyBlrgr8lD2QjQX6lD6QeQSi/djhj8ZNLjpQ8aBKtq+ygahvns8/8XT6XF8FeEofB71lw3kAxv3+'
    'ka0xmG/+FjghtmXePutxqalKcLNXNqy/P2380+R7H9hQKxXkdg0DcAvtNxjYTghGbxAZdu31XYAM6wnu7tR2KFySmZnQCeRJ'
    '18YQ8wGhkOGVUrw5GfS+X2t9owJe5jyamhLgLdH8p/eFZmGUjBcyPNymyx9N4WsAtlnwIEHB6IgMOb7hKh16L8yRtj8Orvb9'
    'sd8fayJWI2ybONQexOwTO+yicmZWPHUTOik6hAZU0hdbzOyuioHiAU5O+0nAvNdHZXd6MDY/3j78JepYL5w06Y4OBIgBajRU'
    'u74Uh2g6Fj3sgXZw2vDijifQhZHwQd917PmtpjMD7JHdoExHKkc6AHRysOz2a3Q7KPtgpjzo+yeiS2X6vrl9ZcWOt/QLenOB'
    'N1SCx+2DWwbUdwPh+2N78Z+LzEZ6+d7103ZvzaYLzGlcOEbUi6n04ePD7eMP64eHvwLuoBRVYpcY7FDwdgFKIlBIHoE6bMmQ'
    '0NOjfiT7RpQeXUvHzTAM5/BVP6RkxDhYSOrxWEbT1N6YQlQeZsRDXV3rY/dhd0nnj9Ng2O0dO9mGmKk6MC7Z5W/MR6C4CqJ+'
    'W39+bmbVxkOfnhtaiYe29xZhpwnEaudxFZzvaNy571GoLxXTunRwn4tXtFRi9KDdaS+v+rwRH+7RPjOBdsU/pu53hq9U7hUG'
    'QExuwcf7+7unJBZoRL3858sMfT4g355sdKfcC9eVyUWncFKbvBxGXRjEJZkPanQByEbsdnLkIa9BZ8DQATlBo2/50TEwkhZT'
    'uWwlVKgrgKo7Hn08pDbumwJXEphKaQQW/LguhBVBEwGKuf9UAesQ6DdhJwGLsXsrGCPQzjk60eZnQ2UvsLFGn8yRAedPi+zO'
    'Y881lhVwLWZW6rGMoctKhqodNANW1AqHzVa5cQUzSG2LS6QwmZSizGbaL5eGsrPrjXcYoPxPNzJWY122MwNCQKk5Gfw5M9c4'
    'TKCeIMA7z5OCT8v50nIyL8lUzOgps4xYz1JEWcJ0vfOk3zqm0E7MLhoF29MaEyrsaN3l+ziexZ4yrdP2ve2xIc5FX6jdMrdx'
    '69g9rxuL4XUbNMS4lcEmbI8Acu+DFs3+r5j/ymyC9EPJQQT9DTtV7DCZ40o3faOOTPf00JMawy1LZTgkE5M+vNAwa3R2xy7d'
    'efmi9QZhr6ugREDx+ETRc29ryBFYnNxcCZZY7wStSNUFOuLMxeyX+R5b2i5KP0+Ph3+hM7J09GymdMD24oJfsxyTQrYFtZl2'
    '/9nD3KuR63bbewoHR/7B9rtCNLbT+kb2w/ZxmFJUip738C7JHG9v8Z/e3f35ZX1FvlP7TXCUj+A7PL9hscx35znZnVd4dwqc'
    'jd3iybxIFUqgaY/rfkiLU5q5hS16SINdVmr9A38pcd8qycTgVIaEzgYnEZJiB1CYAdev5YOCWAk8e6SsZmsNNuFMyK0E7Qvs'
    'LigwFSiNnaYRwS4T2mwK2NPg26G76TWSg/iEx5OZ4EazyG2ye1xrRlvuGXAbdLU7cqArrxzsOLewDELrbWfNGDyrccxz68Iz'
    'amPVzhy4wmofTCeXwGvZNArb7ZTKi6UDx+hKcpvk1Qh+O4aphexJZfWZbv54Lzdg4en6Zcdjehvvfj0y1eWEJT53tDtjh77v'
    'vQo2JPueJiN1DKccWDuZT05ouV64U79oc1+WHOxeJnigMax5TtBqBWw42aE9NZMAe9x6YB+21zd0VtvVpAd/daaPLof8TA5b'
    '4bUE7CWQGUecsr6wMmGzrUJgQmBgTa/bw0Eo0w6VoBaW8G39W9ptw5VuaZpYwluJfoo/8Ihr7ZHlHkncpx7BWTLZUXQzKJid'
    'gdMSF4K5z6zVfPEyaKYkDhKm2SYODloAzG51wBUNumxXMyXP5hkRp1ywzPAsCa+XLQvFpGctNPRL2oUbJ/2aMcWJgn48hm0D'
    'i3PeZeEnfWQ6M0V0vTNsWBSvqbNDj9de3dkClt7X0Kzvg2U0q5MmcKRWveb+PAa4UHaxc0rPl4vJE0INzdmy/DgxLCUjFFZ4'
    'Xm4lsw6F7LjmwL/a9IkeFz0zYJcdhWoK1kmf0KTnbPYRR2ncV/JWcMxzoCxB9irmOoa5S0eIW2vUV+ottNhXr1+NHKbpWzBb'
    '5oii1pJTnLU6WpgpRHyz0bdzEu9mawzAZ2y1BXi9Pt9gPMBOhB0CDQTbLG3t4szBTyTUpP0SyFrZ/wlmUeO2XrehkLgExdXG'
    '4DHEtb/SFcy6q0ZAUM8uDQSDzAubPDAvDLaoN50kmyBRu7VAONhR7KaVGu3ldfDrau9IKJ63kubW+gGqNvSd9ykvdLkQ+svO'
    'MeAVaIOCcDbSxcpUXmwqGXdUWb2QsgjHAyq0i1297Ez2IlgjzQjLoWtP8HRe+xFxxNAqsRPqQjl8cKtoPHapQhtqMVwMbGpo'
    'Ict1fjQ0J0CCUo5KboAxNiXzQRt/l3IxoWrTusHPYiiDUrSX59X8Bw7A6LgLWgTHzY+Iqg5bfvbRSRl70j8lsB8D7BjDFQc+'
    'pQA2Meq6nDA+HamKhJHMuKgmhxSf2xqf054OId0y6hIHB3TUbH49FON+ImiBbCSKpRgyfcJ9fb2pQEIpjOdmqKbB8C46BnCm'
    'GGlWpb6sO/QoW/pRq5+DzDnmSQBpj9pacXIHGq/l4B541QUhmWeM6BbLIyXrBP0Qpk2sOzKRU4l4ZXTFFI4xC4d5i2Dd00JM'
    'Efc8rOpOnKEBzANAjkwHXKEVsm0t2voLA39JKkCsBUQsnoEj3VAaTtnTUo0Jmt5I2lHT1YZ1niqb305U/iBL+aiuFuaWd2tG'
    'KKcwbqg+G+nJNO6CsrcYI40J5e5M8W7YGIR/8NOGsfNmtc8C5p50wCTDL9XFOBbdbGSOzASwkVT3BgA5I7EaF9U5voQFwGqS'
    'yGMDN01n4Lpb4XWvLSCnytT5NAy7zhsPc2MixTgBS6GOWdZJ/0yIOVT7fKlE6KGIqbReRxcbhoIShgxLNj9jCoTryWgaDQWh'
    '/JrNqbGjrATjCmcrUJM38hLaHUb9bU74KGAyLe4h+vtMCbAlIBSzCeLAOiOPRdXD9JCzrcKiwUDAr4dovVb8r+hrghQeBqbF'
    'fm+BFuW4wjRyi3YEAryYtse6Q0eEeUsUQEH/mSe72nkjYJIpeWP3n+22jrszALYhzDIlcqy4sUZiE3P1KGWELdCA7yaN4Lnj'
    'jEqxMKIyLaEBRXQRGuYGE+DVcESK+muSS8r+F05KjbfhlsSQKI7oJBXLKRTPK/H0zOve51S14/r0z1nUeqXE1xLCGOHYv5o4'
    'ZWsUqy7+ZA2j8y33Pl3eRWvId0fzQQp/g1OIyf0VrT6Y64PHX8yhNzMzlIWR0k6H/Dk9bugMd2JHjFrB/hTHXgRH+0a4X9ia'
    '4T4j5YE0B396R1536t3Kgns9UFEnryY9TTSBLXAdmruSVFoiS1ZJP9Cuas2fVPQLacmGtF7Qk2E0y0gx4zOKG0RBPlr2XdtQ'
    'BnGKyclS7oWyq4ptAryFpBBFuztEELO7tJeQcGOPZK18F2W0obeBtdQ/agRp1sqLwPwmFXVR5cRuNkPquCkh+8g5JvQt9YC8'
    'MXJhVJRZIfZIgqUa9ApDVTB/RcyxMERPbc92PiZwtQArli5jsqbisRdUDPNIO2NFqp8o/H3YDWFxVLNZJCEd1Hzy9aR8p97+'
    'xaBskJsGiLhE6YCncdu+dggCre1j4A3A1JEukx4/DzreWIrAtN3rfr/JSUCoRI/mOMu65WUGesUgyDyB2Mrooh7M9G0njBVE'
    '0YckSqc9qylCUkRo14bRtU/IbKUYz1FERdobVKr0UB6SLFCNBFdlSs/htFkVL4QyYlTORIyJG4U28kw2tZSLZ7Dq466EQgQa'
    'KLBFyeAfznGS87GusSnYtKDINTHYu2PnII3bLzu1aw6+rqGmQ6lqiZbX7tIyVpLPZRygCoG5dw1TX4O7JPYKXjm+EockqGs6'
    '2XwDFrKaBYXD9BUKAKIn0K57HvCX9q+i0gaty/VH8qOO5FnhQCIkdqlK5uXseeKMUUTeK37s2gw00IYcxNBxXDth9JoZB1y1'
    '3rz4BPH1aOXKqa4QtdsVwvXja13nqfA+7MvUDjN7p4GkJ+fcFNTM7EZVNIpUJ4ixqwo/vOW15+KNHYu4Uvs7y2JoV6MYW2JE'
    'sCpSsKgowLXLLOwqXmA0zZFXP6ztHN2Vw0J8LE4vSmAYHbre9LjimlgvIoSrHHYU1V+WMig80WSlViYLsOe9WHQGWMDYwwVF'
    'cZOCtuP55hUAjbVUe2Nd5gYtrjZD4BC90mpAdg5RjJJS5cqBUrgUD5XXJGU8Ypet2KPTontL130wBzQHgkoGW/Kiff0hMqlS'
    'AgrTsixwrKCKbdobvlkyOWgq4RtvvnHTQzV2VHTJDYcP2VAugYLuCa7fQZlKx+kMmJe37/5Zq8fDaxCBkD8vOlPVbC2CT4tr'
    'SSj2yU9arCZ/mgo4wvb9YVMPenCqFEtRUqqGUQMsl7OjSEceUbNQqlJWezsFXyhZoE92cdTc60n+KJj3j4d4gD1lGiiuOWf+'
    'Pz+rNqOiTjK6l4pFQbsY+9SlEfVVS7iLxdWf4rUYYQHGY4WbAeDgTKOjkAHYk3WhgPiiMIMH82GODFlQ2H6mIKHXonjrSkzO'
    'gHGf7f124WZRoszXJs6FHWFFtg7pNhNB59rv1g2IpXwkJUPU1sNDgCt5SFxctLg4u1GkO/BR6iA6sIkzC9mGjyoUumlNrwTk'
    '4DdiPNEGTivSsWPoTcMxuCO9lrhAEkgI4DQNC+OfopvVXhRXdVkAdVw1hUZ5jVyqa2Ssnt4i4WpMneJV4z+vvlUOB+jwV0Hr'
    'sPRHjk/qMPzSaX+E2jrDXOfHtQ1EOFHILgOecT3qUAXsXD9tYnh6hp4UeUiYeKkbRQ9fFqTbPcUpeqByOxxGviUA6LA9zcwC'
    'JnKlZ8trZfAMppDK1NBT+0XtqULmrcLH4MVgDde9g2bG9P+zWFJ2grPwVGdKg1pqRJTvVGtldelPJqSVw4NC5DpL46mwIxIS'
    'plZhNvYmrOmO4Na00F7sefWPYoIG0OwXpQAFAjrCzcls06UREDc4PGBBRs4XH+yQij/vxmkVO+JkHtEh09La86sBrpt20pWl'
    'S2PGWp0f4r87yogSFKchENklE4qjsk5cqVyR9mjMlzf34xUNBI25t9PLGIBMUOqXIv+JSViRIcV9Z0NT4HAOqIwAEtIQ2Al5'
    'g28iJOS4OTEHRV2nqAriQlx/m0jLFxQ+TOT2Un2t0ViKwC2IfPrsOofVZRFKZIRGl5tqok3iktVhjpRh4vihSkKOTBsYm6tS'
    'GSpBW/+0PfcKWTwVEj7bfuqSZgf4Ki5pvnDyeXS3EvQoSRtTqgsKUbh8EkkCD4N9oiuZIdGPCjga2v3tZK2c7AXg2c6voIUC'
    'bDA295YgqVpxSoIVSe3ha4mjSUyUIbL/invqXLSLWAIQcPhRaCTymYQaPqUEmou+DYYve6aziDym4m3RNaeXdXY3k3dgSi1i'
    '4eMQP1GIAKeisyUQwaivRTcpFY+U4SrbaxHOV6nGSZm4kZqzKtlgKexKtjATJxd7CmmMSlysWh+v60uV1QRgGchcLufwBysr'
    'tStDAA/TRhsKPtu2JQuPFu5ZK0uZVfDxxQxxD0snraZsrGp4S5l2ypScdguveAw71NXs/xXIPVyp+qRxppCWS4jsBQOPrVwj'
    '58aO06qSuGm3bVWV5/PhojuVbdmcORfy8bvc6KLMXKPHzR5Da1iY4Mt4IvupZFPYcjk91aL6Lgdjn7q2PQgn2IpfIcJ52pGa'
    'ALypeROX4R+x0QO/GkGlDkJKD8Y2tpqRooDXCHYWpcAX63GBkp7trQzdv+E5Z4WEDVLtNac+yelncomp7koaDA2iyU/AJMTO'
    'QXXsAZYqL+UJxwRHKGmpx6PWGWCyOUIcnUdgejK3aCZOe8Doi5kmzDGXiF3KSvMdztg6RcwUZRcC1gjA7rk1JXKQhbK+xMKC'
    'woxcbPRqIGD7JbcPM/NDyaDSPgB7l6Z0ieJb3m+omohQXyF3tBglXApZcJaD4O8XgdYzJ8tLRYzlykFgKeg5YOelEGLmkNeV'
    '1dRtV4xGnRvAEpXPVcSxpZkeAywB3WYClGZsYAaGm7rBO7dKP4nZlSylIMq5XQKvTvez25WUUxr8s4D/9rFj01djKBqOBTWb'
    'nmPmE7jh0tg/mnZT8/SE10bEAszmwE731W9Gq3CogBPoq6YIBMsDHtL2NLnq2qocztZbYmoeuGfKWFa70r4+aeseJAtxFmQk'
    'S/0xsLPb7zmYlsK04Wme08+y5nNYBK2YdRXn65lsNiYGAuCC7pTDBG/T9CG6KsXW+IXI+pisHK4iYWGiVaBNUesBct66GC9X'
    'LkzEhwc4VqSmEJ2dOobb+iedNnChbHpOMQKcOinJQ/CJrzaFRUbD7WV1stZXSN3hiFBTtoTXXk3lKE9CywrSJa8r9DdmxDLV'
    'kZr2d7aRxNPBKdSTOFKRkn+7YnO5N5GLoPAUwflH+ZdsquJbiSrLSWfdwpRdBTsGTVCqyZbK+Ehu/7LL8K2G2oT0uQR19uWM'
    'V7U1x6HXTPv7cJKCDVadO4fjAjIJozOZajnQcFlSn1udqesaUynY7b5mczBNHSjUorNHXPVSqTSRkUQFJs7KXlOi6rqIPiPc'
    'BQBr1zk6BhbYVS1Cs7uHdqkWAFZKkqld5NZoKHQsad13rbxKwuA6BowF+FctSasFtr7XYxtYj+3IKaZmDbY0oENO6d4qbGku'
    'J0yBSr/wuB5Qh82kTQyXGJdlyToBPyPDQUvfKYlfWTCIlr0Jk8ug+A6ObhbnRZFG0HkBCrqsy0BnZxTjTOgMgcWi5iNIcBwD'
    'OOrbVKM4pbaoHvtV8j/byyaVkSrURDfm9VKYVyndU9SjSlPHNGV12JmrvvlT0j8zr5YQjiKISK87IddXsVKOWrOHlbqzpNDA'
    'aBVPmp7MR1hkUwNnpep//PwZM4FkbaaXPevELPW6cRmfeUcSViP39ypyS7z0wDNnkdPsnAwBkMiDnkK4TbZLzeoQs2IsvEQH'
    'UswVjGBsPG8XzvWieNj4aynibzO8R5y6eZ4yXWNUMCevSzimW0S6nrhuJXJexlasicWPT3clOp3afuUD55XPK86ylhQpBQnt'
    'DEhgSbSrWeT/jtimub2aVQidp9ib1E6zZxE57WjUuRfM8Sa4ys/bjNEwP/RmdH7ot6GAp1u0il85b+FF+Ee4iPWfJyvVhTqB'
    'gtVazBSFFLvAPwtvIAtQ9Moo6GS6Yq29PN2P5WxkzXOYT1SFUc1MKeRkEIwko1h2j37KE2Q5rZltynRNWiSNjnWl0hlwFDWc'
    'h/IYEFvNr3yYc8OIWn+6KvIa5cVqliyhiNa1bI+LnGXRzvkQJ1ou4yDUce4violamsH7LRwgaT0jxwWABqSxu7t0hjdbR7PO'
    'YatqrqLjxiMYg1nh6bJkArzykhpV40pY8LQBMs1HhoqFVi8dDobYVimVn6+YUZmyvIxfRD/KADzuU2sVL8osrEdScUKUScrJ'
    'Vmshj6xLchD4Ivs2oR1DhZHEUh4ZfDkAlfQrU4COafU/KEjJtPjU4Al3/uEoOHIObj73ow5HsmzRLmWzZHqfGWkpKrtr5JbB'
    'hiZ1JiQM+x0XMBnYS6vILBcQ1JQTBam7Y+7RPkUzntoJNM6+IWDqSNmeZ44iRIgsLcI/arplC0UOfAAHT6EHUoYSYHqshW0y'
    'BIQKeW7Nb+tcthpXraakNqaApqliVnPvDc6czucpO4RWus7VRkewCiJPUK2IeqOOSMelEXBmiBcihhCYs5qfyImvefRnVSIR'
    'MHPNEOnipfxiD6s4f2eV0zqxcPSE5jwU2CnqXpBCjGvrxnIia61GqJtHlnv7104ImYHFvJpGwh0t7rOLekwVAEvyqcmrCOBL'
    'lDrcary8k4JFFm8g/xwW+8h1/JUEA2Oqz4ezz8CytujczIPWCN5dNIn+IgVsX3MaBABG9IJhIkySX6jEpKgWymlvKkXuXRGa'
    'o4blkcmorJoYmt4WUaF1Vny9g7EUJwZvkqpMnwfj4f6QW/uMLJxnd3Nh4lr8wjrQlmcCqQ3la4arGMwxtSVp1SDITV6Y62D2'
    '43SBvMzfaVGSmEGCIhKX0bMvaznXZ8GgXJpXoLafGDtSvA62aymvx1Mop6CmkPQEDWhKN4sCZDk0JJwulVlG9vprALAXDQB7'
    '1Rxg35mBdsaZgMCeh3/s+rGQAd3lxu+EJFOZvSR9OyVuYQGh46nqJcllBUE6KDCPwGGSWcAzvgq6hHtToantbQjiE1i9lAxZ'
    '0DBrVwDnXjDxM5lm01U3DQ0MvY3bJsepC8kS68yOu+Fx7RceumHCAwnFbbMZfsaSI+VIvZ6AAKMjKfURuBSUrilTWw3zQRUj'
    'zhYlVWuEVXumizI7PQ5NrhfsxyJcHOBFAxSNsFEH5l48bGItRC7ZdoxjpYK262mt6Td1EHA1cu7I5ZpQB8XA3qh4SkbqitK7'
    '9TDEui4a2VNmNXdEab10VR2SITl9sZPzeqyB8rYCqQlNFsat8nvVm4PH50FhYOUCBYNDlGCp8XObBUVUCl6Yf0iusQ69fUnt'
    'PZftBGdCCx0mgGjf7gGThSnblMvJ1h9bkRFfsDBpSny59Rbb0cb3GYvW0cPQUpMOJu1cIFiTkDFPJVCpDU8jVdSMPTtuFYtL'
    'KqrxB0fMUuxhBznYYn+CAmcJ6urAk7wIuFEd8rEm9Bdw+mpplW3TrcqEis6jVQ7UmoOSbn2lYtFF3wLrqeIq/L9YXDK1P2qs'
    'C2nNco8z4RXpWN0zUnCmX9fLUnmIR7+SCMcTFBM/l9o+23RVH+mteeFwfzsSFpYuLkJqlYh8SkqWcJHk8y5xNa1QosG8hLPm'
    'B3Jv+ngsAC6mdqOUTNmHBTggd0tnFk11Iq1gUOn6FM4YB1QMXrWa4z3n2MpRLEuFn7S0wViMTyJNVoTebypCtbTco5YOaVYP'
    'mIcgEvYJuXPUFPgWYaKSZlb5muUAsEVJqgecNCVlM1xsFpR+wPwoLTyuBhaUCaGYBPu+l+BeyMNkqTDU93xci+z98gbSivZk'
    'ZLXtltn+a9K1tj+TJuJaGPHmge6yz9hXyjNENvZqKAeNGSRU5eZR3V1it3Rq3Woo1WxxxbXonp2068C6B/fk/4fyGXoyHeOg'
    'jUEFGR/t0oi69Wf+phw0wachLvjwPOBq3mg1q9HUCpLoiyJvjQXbdZkmj5JYzALF52n34OLDr5K70TL1DPJQ1/jT+8vOYpdS'
    'SapF18+cRCgG1emK8oIuRyfHsV3trGCFIGOY1GbJYxJSOiwhZHLNaRSwll23Ra30gFiEAP0gCqE/+vxWlp1KCXd1cbSuybZL'
    'N/Dp5o7SiJRPC+hM+YzCGlCSPvJaUjLXTgN+5DnyQ320bIBTP4jyO3KYgcA9NqYT4zZATarBp4xS0nM4yPKvlXYTGE11roV1'
    'pR3TZQ6dJmIryS5o6Ghd2m5VT8az6WXqhcTIbNlmWVY1ImlsjOm+ApQ3WmQ+n4ynebbAl0mKq0iIDiAabRNkI2n/y28VKIkr'
    'q47rnlWSNFE1tUuSJsB8I8gHe2CBElwFuMinyT1KCWOo64tIBb5LxiWE3dsVkmjB6PacxiEx9bh9DhK1302orXIqKsU2QFAd'
    'hxLjD738sMg0k5TphMhrXkpjDEXooqI5Jxdzy3CUIv/PSu6TfSxKAgJdTq4EY36Egp/tCgbEGL0obVXlTyk5yzQi2toQtAYV'
    's/rHNJbKnLHoXDaqTgKSsGZZdDohTtOyWEy1zVW7zhcxx35ZH9aGvrk11NytEeqQNaNL9GHoYte5Q0rNYLrWidfGKHUCnm6N'
    'fVbbXhZcISANUvCZloWripd1FmdkJ5tIFQx9aW/9a75yXrmE/m8MPdUy9ttdq+WBUd0r9nUBPrI6YC8TsS6juJx6FRNQJq+y'
    'tB/nC0IpJVa46fu0kZLiiVvXZdGQWA5+2RbVLkMV7XLXCwbqfxybBPYSuy5kAmX2jGK4dkoKsShxnxi4gEWsnBJJFuPF5JWw'
    'Uj3dVBMaK6ZahIaIRYVxIhbYo2k7zHcXVsD5piQxxQ2HxPzoIomouJic42lkTQIHv9nYboFMJhRvLSY+OZmtK+VdeDOVKJ8k'
    'b0yQjnSuQIOSJZFYQ8RskCwbJybsF1CQst6t5lGRSzyRKheHjbTVRqY3mjVWrLSuZtzos0yBhegIE0up525ZN5VpxxSk/QD0'
    'hqffWU1TK0zSxiW5vj3taw3P+tBNHMBGNHFI05TepzX8AE10SOPYVEIqNkyk235x3t7OxqEzo21d+yFRNB0+q+3D7fbNPnQd'
    'JATeAqkWVxeAbXBBK7U1KSdlDzKBB5VUVM2XregqJVQ1TXvHs45yO01qlOsmP5q4Xy3BguHVjN1GWXal1zIEPLOwaIHJdJmx'
    'IsH4vBXZkN1WeHsUBRr5zQElFDVoblby2vCsd1c16Ih6y+lvbm+GtrPe7dXzSjZlx3tr7V2dL30U3hhOt8exad9JXh6tbO+V'
    'tOrvkH62eBPDaJR+5qU2tY5qgDBlZnb1NY1T1Pw92vm3D/fvc31Qm5faGH2HbMR50ebnRkxzurfN2k3y7i/6B8J0XfAiwfsw'
    'jH4u9Hw4XEKb/wO0FKcG'
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
