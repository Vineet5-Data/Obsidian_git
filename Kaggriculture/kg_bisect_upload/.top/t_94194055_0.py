import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXcuOW1ly/Jda10Jkvb2rljiWMNVdQkkaYtwoNBrwGAaM8aLtneF/t6zi4/KeyMiIPIeUNNBKBIu697xPZmRk5K//c/Zv'
    'v//x97/9cfZPv5799Ondw5vf3t9/+PjpaXX2fH7277//57/+1+e/fP7499//+I+//ffnz7+evX335a/ah58+/fW3+1/e/Xz/'
    'cHZ+9vpxfXa+bL7+8Ha1ej/5w4fV6s3nr9dvV/cfz85vZl//vHp4/OXsfLH7+funxzefXn/c/4/r5+f/PZ927P2713/+9H7/'
    'psWkb7+erVcfPn5p6y+PTx/ffvm0+2r24XAgPqweHvZvvZi/dfu4yatAQ6av3X+aTwVqwOx14ezBHu5a8mVOFgd93fyKvOv9'
    'w/3rVTSeqD/b/wDeNms3eevmv0zHs2nHl+9+2S+Gg75uZir4WTrCq/v5+/fL4/7j6mm+iObfHa4euHSX80X04fHTfBG1i/NP'
    '/78zDr6Z9Y5NZTs4hwM8G6V9/17fb5bm9kcvO3PSdWsu98PVvnQ7CtNfpdMF9h+aHLATmhVM3rIZezBmk+FoZqz9jT5jm3Gn'
    'Q3fw3PnO2w9hO03BulwIhxvYDOHRys+Wgy5oI4sOnXzyti3Vx1L+Jp9HMISbEwbMUTZv+iDu3rH78Pns/YA+eAO3H/eeB29+'
    'SSd97PPphA/pwPb/Tt409Lnph6/w2NmtchFYk8lhalwgY546P1ud7XvyFsztEfLTxowY04LXjw8Pq9cff/vT6unju4d3/3J4'
    'JgwavPJLjCVSfseR5mB7a0/aE+6hnSMy+3FwlV89GxbgN73+jfmd9/Gy7t2m9l+nTQLMu8Z8nBjhYOFW/AxgjMA9gXu1WdqW'
    'mcz7MO1t1sd0AIFjbxikzFWBn7IHsrFAn9IHMo9AtB87/NG4yUUHKh5UyfZVNhD1zfP5J55On+urAE/p46C3bDgPwLjfP7I1'
    'BvPN3wInxLbM22c9LjVVCW52YsP6x9PGP02+94ENdYkB7EWXUYCAZNHUYBdb3xXH0Jzgdk6tg8I1mBkCnVCddDEMMRAQzhhe'
    'GsW7kYHr++O6b1TAy5xHU2MBvCWa//RG0GyIknlChodbbfmjKUAN4DQLACQ4Fx2RIQc0XKVDT/45lvaPg5z9eOyPx5qYVGy9'
    '2LF6EEwPovKJpXVVOTMrvrgJjhRdPgMM6YseZnZXxUDxICWn/SQk3uuFsjs9GJu3909/iTrWCxhNuqO7+mIIGg3Vri/FIZqO'
    'RQ8/oB2cNoC4YwJ0oSB80Hcde3mr6cwAe2Q3KNORyrEMAI4cLLv9Gt0Oyj5cKQ/6/onoUpm+b25fWdHhLcGC3lzgDZXwcPvg'
    'luP0w0D48dhehOcqs5E2v7v9st1bs+lKB31CI2pjKn34+HS//mn19PRXwA6U4kbsEoMdCt6+eO6BQvIY02FLhgSX1vqR7BtR'
    'evwsHTfDMJzDV/2QkhHFYEGn9bGMpqm9MYWoPMyIB7O61sfuw+6Szh+nwbDbO3ayDTEXdWDkscvfmI9AcRVE/ba+fmlm1cZD'
    'n14aWol4tvcW4Z8J1GnncRWc72jsuB9xpq8Vtbp2cJ+rE1oqMXrQ7rTNqz5vxKdHlC5hAu2Kf0zd7wxfqdwrDICY3ILrx8eH'
    'L2kq0Ija/HEzQ58PyDdCJHDvi1vhujJ96BxOasMtY+SEQWyR+aBGF4BsxG4nRx7yGnQGDB2Q9TP6lh8dAyOJL5XLVkKFugKo'
    'uuPRxzRq474pcCWBqc2nMvy4KoQVQRMBirn/VAHrEOg34R8Bi7F7Kxgj0M45OtHmZ0NlL7CxRp/MkQHnT4vszmPPNR4VcC1m'
    'VuqxjKHrSg6qHTSDiAsMm13mxhXMEbUtruNQijKbab9cGsrOrjfeYYAyPN3IWI1X2c4MCAGl5mTwdWaucZhAPUGAd56n/Z6X'
    'M6LldF2Si5jRU2Y5r56liPKA6Xrnab0ypiDAr7toFGxPa0yosKN1l+/jeBZ7yrRO2/e2x4Y4F32hdsvcxq1j97xuLIbXbdAQ'
    '41YGm7A9Asi9D1o0+1sxw5XZBOmHkoMI+ht2qthhMseVbvpGHZnu6aGHTHXKsQvQ28x2Yzbm7jUpYOnR/doh2J2t85SF80Ex'
    'SNDNvTiCHO6uvRusd/mxxXQOYFYc+5U9wePqK8W0yNjv6Cff3WEvwpKamfL42hsH/szyKArJENTY2f2xh3JXY8XtNu0Ux40M'
    '++1vhTBqJiQkGo2UD4rtg+1bMWWoFB33oENwNO6P483F/PO7hz9vVl7kDrW/zHPmelDvzZZ+ed9ime/UJcMC7KkEi8uGBbgT'
    'o88godyCFQe2tiAHY/mVZqBISNY8poATOJr3dMypgdXAHC1r03PBamO5m8npkZEzPc+TtF0hQNiM5UWOiLZ8i4nsFzZakY/V'
    'thIfmH1QOZh34GSw3QVEy9oHFCOjLV8VuCwiMhL7MTn31cORW6uaOXCOv1dDMMCYgXksfKjma1NP8hStYwdgzO8ughFKg+BA'
    'oI0A7rLsTDn6xLYncdAkaUDN7tS2hDFrFvpQxUjevPtnWREN0J8IgFGBjLLV6Lm3DKfx/0cvw98AdLqTPLujhAGbGgQOy56w'
    '4KZfRjc/+Z0mBnUM/x3YKpn7Tqi3XkhT9+bzIF1j+mhOfY973zgKMOcHG6Syoyv/sDePkbn57RreI/HtShrXk3L25yGj7BIv'
    'KmBhAedoFcbDaQCWhocJa+2S4BOpWz+9Tw/7X6YX8pidEm2jnTUsTaaWIbrV0uFQyWsFBxV7VwJ7Cl74GC4B5T0xya0W9gCb'
    'oZLnLLncrQ8NLFWyJQeBG1KS1L3g04K/iSoiOmk7gqRZUpHk/wJTD3Qx/lVn4rKyFlqzVAlYtgZrnfbHt/mxW2wvAZG70Osc'
    '5PoZQpgSMkz7IotpuypqeCdoFjDhhrzylKN1slZ9o4M1nAwwRshmNF+g1io54U+GEsoudU7T+XrhesKfqYTr62ppMhxRCttT'
    'E88UxQlW1s1znzKx0h150I9CGAUro08usupKVuifgO0qMcdhhBQ9o1tbANI3Ep86puKHHkwxeENepSbgZbmdxRSv1p8GAzR9'
    'iRjt7c0OUx/NmgLD8kqZsikgfOcSUqBYkuYS03AyWYkBUq+T2MGLs3mmTQT/OW1vS/0pBspwM6CEWCielbf2tg2EXD3rtwDj'
    'OPN1234DJq3U/usQEl0sDNOCrWLGkwDzwnMD5W4Z+JwZZm9UWw5KLprr6+D/VjtHeeRiI+FwCLd8G8HN+4E6PScKtuvxKl+P'
    'DBeeDcR1MrlrdogAerTc62vhENHQZHCbmLOIF0fPcl10+kvAp0NtTK2lqH4lX7H7d+SKpyAZjM3HWjOgwh5IDtW5hEmSbAG8'
    'b1rmIDlSWE3M0BTOF1tfvzzksAiwokZ2wCfxsTHhedNKwS/iKINStpfltAoO3nwrKRZRTWHLOz86WWOfHUAJ72KsXMjAlkgc'
    'hkwJ8D4FIIchD3Ky+HSkKvJFMhujO3HEe+6B+kfDk9cLSCvLzg6zg4WUdqMQyW5ZJrxZ1t71BPqEm/r2uQIkpdAfcIdJCJdz'
    '1LuYGojBrGRza3yCiESWmAfMqAa8JSmZgK74xiQyF4+OLDTG8sGlcKr1UQyIg7E3lw135cevmzadiy0bT9uTuwcZNb1f5Ggf'
    'sJIZ9K42CdtZ1WVFHDS+oJXWMbIW0UMMD//zYpfWccUCCnUCKC7ud+mGS7pCZcyyhQZaT9EQpcRGNV2IQoXgxcpian/jiNiR'
    'VSIei1xQDv114FJRKqhydbv4a3qf0K+GrRwa8gOcKhGYrekd0qGlwH2uFBH8fMgtNVzdQoKFBHFpG8rZ4zb9ohgjwZjdl9P2'
    '3CbYzfHBGYDSuFnfq7o20e5eQpkyDqdGRlhMRkSSElOjzJCQSBujrOkM+TlQ/arNTtaI7rGAlVHRZ8kQrIp6GmOdMJkCAw+U'
    'dYzvnitUKYrHMPr8/CtBE95INtBJXdzfGCRdDexoOa1IoWxZi64FJETni7m64iQuK9wXKi0oZTRW5gz5Y2mVXzVjCLvWtWmk'
    '4cuMfqVo11S9RxZ9ZV4687VcltjyueKKaUFiQRRoxDBSdwMU/kv8XqfqEHOWUn9OwmYVD0/IDRcKMFEQRvxOdOmClaghSrTt'
    'dc8zXOX+FmItdLx8jfh3lPaWp3nUkhVKNAklzgN8gsFHiBEhtc/1o18SnG8wIyKq9TynXH0vzvbJqBCtaw1pzVo2c4gQFNzu'
    'vRu4+1MxwC7bVhXcVcqOyCTUAAzXSfcH87vbxJmzWpUzKPEXOsGZdpWgUeXfSbS0l9NnERJVbw1OuyakkpNiUu/BzSSwhBrT'
    'lyJpv7QUkCp3QZvtcdbbv2VwiJHAU1CbhGuUsSXsvJIenUZNl59/kqa6MKfOqvKofkOUFWhGGvUY4p91TiKXLGUujsTqrRCq'
    'EdZAxySlKnSWB1P2kni1hKlK/SUNtsb69PlCpCti3ysqsUPuE+bfs1hkTLhC+MDsv/kIgBbmzcvW4kURdW9EIH29UnVOXJmU'
    'ilZnZ2sA0cpvVusa9wqd0NyBLKVjZIKD8mHCb1WKK2uNrEXF7wLf/ar13Rdfz3fnWQtopw70y/dLE+m2hahCVyVT4Ge1YUSY'
    'vJrFmnt962L+QDnEqsxQt97EujhiHnuBuWPl8VHqlunFQlKkRg4+39Z0EKlztaVZH6Q+vnoZ2s03mYkxqcfc6cdmqw+xvuPD'
    'Qpd5l/j0LCNJ4xQMVFkhYd9s3vpUNUROfWHIRdeb6u5XvDUw6PAWUDi7rMNqJRg1hyR0esxqEHiBYY9OqsWTJ9URC9oo6ToE'
    'VWOhZIUCUCxXTj2vFdzJ5MV29O/CCPgbcz5uDCjuQKjooeNdtNGmhup0Mnh2jpsDoni8BTWYGrd6ABd4mh4yXKX+lBFLxw06'
    'acAS7YrEbRqUtn2EWKZU3Cw321USMfmQDbZwWRpFXwReMQg81Xna8D6rZNV3UozblXNY9u9FJsMY/4m1rnF+0xqASBDmlZFO'
    '2csHn847NgLyqFDFo5R8ErAoWQANs+9EFy81ZW4cjmV+Qkm+T6Vgu4jR3z4bPGkaaKMOYWrd+tplwvZIXC2tKINYJ16WwnvV'
    'pzToWYJaLwswy2L5XCFre3HZ0C8UL0BN6VFjcbMVD5tj5dcWlg2JAycESS2RNRExEIUTBc9PUZjM/ojPfHLkDG65xvJODh/K'
    'C6gLVS5KzreW1pEICXcQhlFPLqTSVrZEIzFtUpnDMf1orwBxa0pYFeP108BqtTtanJ/RYQnkQs7+Ydq0y36hCbmEkpJqwzNe'
    '6gvxqp7+8FLscv8vC4hTOvz2ARFH4qgd66ruuLylPPqpBCBo4t23Gouv0ebHROXrTsKYeHzmR+sB8+ME6fWyBl2sUD8+n7Zi'
    'MO6jzG8rNjVI0rEzlg/c/zT0YmQ6a1F6PeSNbmx6zRYC8CyyXc1NUcrVS5F4VbAR1SKTo0IK0Ri84HDhSKbGcYTnTHFCpjTQ'
    'DXsKssnKf1YWEKsMSZyqpNiGI52kwABUE5K4P5UAv2TG2jGRgnKuhopBi4OyoDupqFoyuSJ2RmHhaihYi5JrmgrDdAwYI1uS'
    '69cI8ukiA+3gk7ASZEPj6PqIcSIypS7wlis2FqaRUq6GaLkdk3sd+XuXX8+5A8Tmr0oxAORZmWNALqIRlAIah9PltzvJERXv'
    'EN5a+pc8KFfgcMoOY/Z3wcHGqH9/HvZ4ibvMTgUHsBzIV6sHxdnWd88F3zU1nyOHJOsYXJJzC1bBAkveMA21i4x6yRvLFp4B'
    'up/P8+pfVajvh03WHSqeV9o7ifO+LUuS9DyEqZYTMuPmfDl6SeErqdidphRXbrKXNC5WskD/gXLAx4Q+CZagKgYE9BaGhAwJ'
    'fhoHOTvzRP6IGr5Cj+spP3jTHmsGX4YmawSYGWUYtFtx8p/zDt50zVkS+pUqsmRH8phZu64G5iXpQSSrrXi11lRJcW2NAaLl'
    'c4SrkO6tEQdIPajNnQkGeGLqwUvFlYnffJ16fVlnm6dlZBhWtGCtdHalHitkGPM+XvZOk0QaId2LKBl506+tMZeybawu9PDX'
    'OvYR0RwAUgetpkP7DeBYxLeA2LfjYWPLy7jUKdmv31CizvLb0fEnBWxEYTYB+BuSlWMhOEaUl9aFLKbmyJIL5/p/75ekP0UB'
    'gLVazGCw3IKVr1PIz5fl52i/OusFZGIN1N9KUdykQOrAOgLoUwRxlXaypBo5PZHvSvUGmJeBR9aYBPG2tRJtROqJWJ5zKH9f'
    'KV2AU7cS6zifiOlny7crFTjgxRakHCJaVF2FtW6MRBtxQRzI2zUtE3aEvYzUAut2DhfqMTKDCKZayOGK8PjOkgx8Z+O8FnX+'
    'YjbWsbARFTgUilqayggd/bqsTyNFPWiCEE1KgbZlLW1DAX9a11yrH8tQ78Ey/T1OeXvy0zyZjhIJwzvokGloV5qMixPPVN4R'
    'GmUUqn5msH5PyZBqn4YWNvkWthIrjkGLXPK+Ilj4RSGOPrRy5revSKZ1MEtsESFkXzE3aH/FfBslNZBNxNnTKh3rYjgYlvHa'
    'ZKQAup8yYhFgAEoKueEBG46zzP0psWOWxrKypE/rFLWsw2GAOT+/7oyFWamoKc8VMtKNJYom8hXiAxjWAgPYBFUSVo48Ad1c'
    '7wJtzob44CxsVrtelLXUUMkSe2spTCw7YAsFYTk/TcOf8r7G87mskQckVqVKB+Eml9zJ6751SHlgqlXo5PiJvSALjtZbUbcT'
    'fYaMm+kcXXRYpUx7zWP01ZmUc1vKlItO8AgPosNePcV6EiPXCl9TrYXi+zvCOctzuIieDa3GS4vcFrYr8Gpo7oiW4JiXU+rD'
    'E630v2LGJJkYds8NYS8nGccrm050vKnoQOgVjra08IR1Og7LJccTW2kJe0ziJ9niNLVjClSyiWvbKAwrVINmgEJSnXqpVZ/S'
    'auik3S4vvYtBQNnFqwgpW7IiN997RZvBajrY6NPL3KQG3wDaWAYZpPCT4RMams4MEaPMiiFlYLur8OZq616V27Sdhqum06TG'
    '52YCa/zQazCz4FJeI7fTNYqWFhezC9g6+uPdtV2QmjOhzkSunEZDqYnJALoYB4eSTI+srYqqDMOKGMgZpThphFUf47wyLirJ'
    'J1F3KHWhdQ/nugKmO+mBtHmJIqzfegIO0ZxY2AqaS8c4O6qL9qoGETGVWWnJ4G1ZgrqX/Z4YRd05BMTzywoRi4vnAtmZa0lE'
    '24GilugYK2RIAetePQApuSI4XMN9rTpXVxbklWmkiwrCjFdTTCmaS7HmiWtJkir6FN0HhjDVqVEkgn2xWdgSYl5iaZfOlMZh'
    'iaIs8tzNnzVWBwbTwxtqQjfEoNuUQNqZQqqDOZKSmktKUzQhelIAX4l9EQXYGDMypO225NYQ6ioYFTYSdQA7cYXnpO7Y8gc2'
    'JZUZo5qvELa6PJ4m2AHGRJJCRFxoXD0xJa9SVgIz6mX01BVDSfLd+l9OUbSOUtqKeBJcLH4mqwKf6dmkWvoZU9VtfZNVIjcs'
    'i8QUopALI3cR3jsqrJno9MrrrpCQxrKCon0LVJhWvDgzGB0IXCiuiixsw/IcFUv1XCYo6KWFKyS2RYnDBo+KpN6zXIObRcw7'
    'AuXLcHJvjUTKtadTlhWAJvJcldm8EmaTJFpyHTZGL9Hnu3KwWLMJOKe3xoqWS3qCjeyIHw1xXVtdsQujoBqfbjUhOwM3jsYs'
    'NqAJppuGtyg7r1mtvOI0GnLl02xJrDR1uAwVSlISEepT+ku0q25K5aeEYiJ57fk6gzXai31CZCb9Sqp6MESl8cbZbF6xaOVD'
    'uNJPshzJXgzBO08n7dyrJDcU97tw6igqkmXbPFx5Y9q9u/IU+LVxp7ERRSGwQP4dIUHWAnv/ONXXxhPHDjQmcupYmIZ5cuZY'
    'qrXuAGmnJZFVqrt920yxIwjffw3WWFrlHN1AVOROpoVJNAnKC1NlhBPetw0t1PJy9ZVPCSpUl2lMmvEAKlkFuyoS30xK2UoZ'
    'UaEsreXxXQ6ik9Gv0iF1iUxXo0hkATqCyYUJC9FBcy/7eGQJ7yXVqJJKzvsBDsYmc2Vl/FJ+vqz6dT+XLJN4pyJUOvXGSAKt'
    'qr5xvGUtoGhWYZLBeaGaFhqlnYWVZJSKdqVUdgk0VYghHCydadfNmU0ORUgoqndcASSF/bRz8kljWQRButN6JlkltAF0h+sQ'
    'Uku4/fl2oIBZ19aY72OxaZwnyr7UJPDoCg1F/T4fh0+PvaL7+kwrHU8uuXaRU63AQpniYhc3Qylz9oCmGThw23zXlrs2zR8N'
    'aItxhmZJvi2BL6/GMuOuFGbc4ntiwIFeXnS1v58Zx+lmR66OmZCbXE7ckUpiHo0Wd7wamV+LFTe2RKamz674wpzUlEKIejV4'
    'Wz3lruQZSyCaw2JkYsBGklJO5xELxzXLVq4WwQkSfHTGxGNF9xmuySBDQacTHtiDjVWwLBXvyRl4rFamyMBTaSE9SkWJA9qM'
    '1KFj6rBEw4nW+bpOQYwxDB9jGyvphtTDtD8dD3G4NMCihFdp2y5G1ZXuIp4LAUUi1LtU8RLNWpDIOKarN4BzWWQ907kEs0qz'
    'w8OTtw8EXJaU9DP+axwJSB4xU3svcgrTFdn2KGEgiVpgIROBgPS9CuDLGuOOpm2LlU4Ztjeug9cyFW9ZoeKp9Umo9Cx1z3oL'
    'utYIlFzCvoW+4vU9AfZsgTRr1ZYR3Zyvl1C9CM6pVuE6wYjsYcHUaOQrUsPpDQpdvdtX9YWg9FqVwhELVICnDPUQjl/E9A5Y'
    'd98s3nnyeqW+SslawNjwVN98BSk6HejoLdtw++zlCbM6pVU5ukToyuTeKfVNxZoCSh6Vgb5VWJGkfmm2WtIgP1f26qxSKluu'
    'kqK2NHoEk2l9W1MKnxWCoYFjwylFAvHaTakRLq2Fx3yLlE3LkD0x5UDPFGR0SEFM6QjLjkpEUglzVfchXWdmGc8MZa0w7/KR'
    'k+pxchYWl1gPPd/UGrwoZ5GBYKZIXFCrxagFb4T8W7SRp33RlUj55GTVI1wFdkuNDW2+FK0XL7Jxob6oITBWRPhQaEoUZ7og'
    '4McGXWohu18V9fXmSUUNuRGSW5r4oFo4KERILJgOaamfB1wUoxhDmrAiMdOoSJcvi2+0n7EJV0o52i0sl9MSyzTmpXdi5GKx'
    'Gph+K4ZoO/oVccqGEshuImAlUjf4buphtqy4E1XI9NXVFBi6rZJ6QkqZgMkws6u34OW6UO1SrShXIIwdBkOOxRkTk/E6Vdaj'
    'NqkEsISJ0ushtrwuhqCwDES1RgLcfKm8i8Xh8tYBOGFUEfcKvH9dooMQQA40G/wNnpVyNrLauQsSneljcGVNNVDRWEk2ml7F'
    'JcnDsAQWzGuBpRlu5JAWyZP6vPUsV3nxJYJMijJ7RTLtsiSA56mjEXNdqfEqCheq83lbWahhspKaMVPcaLdA4WxgRLhdpkx2'
    'OyhBJSRB2Vox1snaqim8TARasO0UgTOo/RFKcJy4Ar1CaC+PuqpTeUjWIqsAQLK+pE1bFwO67NqyFBJq96pW4oSQfrpLZr9M'
    '8EKe4E7Mjx1XbDAANoTQiheHUYYkluZmrhOdMKKX1BGYjBfL2uytunoeJ6MNp+9RxmG8w1nGp0IEn3YsRIKW3s63Uj8XpTFS'
    'Imzsbzy+biySV0eRVWTCnb6gkB2DuRyx+5fdMGVoXmyXVLQuv7NM181NYza9IwuFZYVOEyTgl0lJiEX+WEWarkBqaD+kaaSA'
    'Jsdqt+gRbfahqiQnE+UKHJYiM61Eyeuj7NVIEjpLLRN9V2st5EAzkGwBc8xDo7rSd1xzgOGdi55jJi0+VJwCjUKnhhWXJTgF'
    'peMKQoMW2K/pyqRpiXcGEyfNREuT1pRsGtaPm7CIk36IGWwaVXQ3sw1FlEM5otSqC1o0wOYHXJbydRgjc0J9IKp7wkCUQxcl'
    'a1w96RGNbRXL9CnQd5j4pznQPEWGsv6gT5E29MLkxjPoWUm6VCFP6bxx5KYyZT/TMW3F4ybohV6/t7zo4TRpJSWU+6pXWOrC'
    'ySDr1oqzEyi9maXUXyd0UiwBoAplcsoqJe91587pSZSXlqI+nwNKCKXCHPH+HQwv6qtYnCoOJ5GRKdFHWyz9MEdw+DYH6x/o'
    'xvGlHsld0nXQnUOJOoeH7W5QauVVBPuCi2WJYLiL7xBzO1h/F3ipnkZwTsr30cmCsEEKUpXqr9E8mxRXgS6s6DUxBNPSDbKE'
    '54h+rls9lunrm6Ut++pM8E0BDpwgHYZhV1hPLsF0SlybXsW8ISUI23RTN4TLM7jYjZIHZxYGAqEnKzoAZCL5bU7W0DJm7dRh'
    'voxoSYl8Y6Nk4KIEslITkObcTFs+IySQOelEUPHrs5SNBMXzlMjzfbR0Kq5qCU4yU1CMS5vbQStfQ1PRpIPLg7xuDFsKZuUT'
    'hDEZ1FZR02oo4doDAQiCGVKhvHmxGKuJWj0EXYHP2aO52XGTUgKD6zTROaNiN4lwvIKeu+UZFQiKiFb6eeUckBtxlqhwE6Vy'
    'MtgxPkgLzRdoWWBNEHZlU0ASninxyW/tCrJ8MqELD8JELJGQWVhLYBunl8Z0QPJ6XWpBl3X19nVqlra0v3VNt8lbZiJ+PkC+'
    'q7XkQ7ZhCNMMKWzQTsJR81H7uV3LvrzUyL4WKwfUsA+ZAQXWNDNIKaIgwEwXhqpqt8pYkV81pMyBCs3pamnMEa5lo/LigaJy'
    'DafLaBtKE3NIscMM/0iC1EYJvXVc5TkvKCxWldNz59K1xo6nNaFl5oPUri7qalMtsZbbwRMIiuntuup5pjpVKYasEslFpS2o'
    'a2I1KPfP9ZqhdAN6qnO8AI0VRmB+AUfkHROYO/VukV7BTdR4JbWqP6zmipHmFbUUzLdmZCcplvGmsZrHrqO1sVfEGq9jxi8R'
    'bJNqFMdYvN9GzHLClGRE7ZhVg4OV4maF5zonee9wNy86oCS1RIb2P8z/ZjWNs2riwnmFD/1TOrY9YsPSUOl8dkkg5VKp5XcT'
    'MaRvADWjT/UoYXHy+xA5YnVKCMU5hIi9khaT1NtM76+wIqDy8mSsKdk0UcLPXs0umSQilTFjc8UfaslkCo2cAp+aoLmZIsp3'
    '6poR6dDDg15MV01Kl+rvBldeQIpVSqYKhC9ya7Fbd3Bv8ZCT11aOFPI4PrJGZ9fO3Qg0JQPzxoMolDeRV1Zc2vZNUh243p4S'
    'TUxSWqerpyBAlUin+qVTQU/p4aeUETptX3XaXn9f41aS1755enx/+NbNN5MPvK/gZy9fsVRzg38vaC+1u67txO7D7sezb0Sz'
    '+EB0IOkBMKF3Jvrz/wFmuIxz'
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
