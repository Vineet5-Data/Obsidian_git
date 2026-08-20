import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vW1ly/C985sOQlGQ5bxqbuyOsxjJkeYmNIQwG2A0CBJuHSd6C/PfIEj8ub1dXV/c5l5IQPw1HJu8936c/qqq//c/s'
    '337/45//+GP2L99mn6++fJk9zGf//vt//v2/Hv/w+PGfv//xH//478fP32Y/f/3bb5/vbj9+/XA/m882v6yvHv97+TD/Nvvl'
    '+m49Cz58//XVp+tfr24ef/zhdjObL8yfv/yyXn+ezc92//Blvf74+Odf1ze3n2bz89Gfty04f3j43/lRL64//OXr58Fb9v35'
    'Ntusv9w/NWf/Ydvnwc/2rRh233vHthHHb/l0e3f/y9NDD5/se7Y/pe/ZNlN99s9fr28+/vb4v/dfvw87efDom3rrb64+rPeD'
    'RIdo+83vs3D0/Md/+HS/n1bnPX8azjF7zfEXj+b66n595z3/w1UwQM9fwOOy68HupYPnbr/ExmW0ydDjDk0vTK19weFxYNnr'
    'E2qfu3+aPyDyRNrHf7n9uh1wMB7hBPrjfFh4djgq8zdonT8OZP4ee7q+uTk6TND5t3jQJwQMWMtEKyPXMNHSAFYmfPdbMBzP'
    'Hag97rAwx3+qPc8Ob5dtz7rftBp2D1lfdVwEymh0XgPPHxKPO961z7ZNeG+EK+3D7c3N+sP9b39a391f31z/61Mz7cWTMhMK'
    '9xtqBnnA7jpMNRS8NWxoMDrJZu/2bs8Jqmz++oHx4yc/fvKKfgItmcFOefbbsENo3MmLh5SjtbdC4pPH9xOsQzavHWXGcRL8'
    'Z2PURWfNqB8tt8PhUqw0FJz/sO1KC/27BLcx/rkZpvCQ39kHnYcJDD4epUoDx/Z+ahEM3KvCq+0AF5pwGGDTAnl8wbQ5Axw2'
    'kLmghaPUDFHhGfsRsr9VRwg8FA9Q+bb4//Lb6lV3dOcdRy/Hvv6X+7urzc/ru7u/zear4mU4+tD9Uux1Pb7MRdl6Ze7c08FM'
    'tfZEcsXmIKJZvlL1e8M2zh5reESa3arx9dt0TwC/j17EPTpg4qPZEQKTiIKisS+pWEiH5VF63qFhbqC8k5npmR6aEWLthVFM'
    'sOmytQeHG4AqNnIUdGu5+n48pM9D2uyCJo+XnIlBmvTH3V92l9san/QIi202/nPRRXMc6e+r9+rur4ULDAwmuSbKQYeEiQMe'
    'ChJpFSd57GJLzdke8NpyfolJ0F3ufeukjh++jT1wmybP5/CabAfinu9vZWVCdI/cpkPlWZJSYZU+v62re5xcP3+oXOa7s3z5'
    'ZB7XHP8xzGmRjwicucbC4ZnJiIAcRRoZBcuMydAQiECWQ+yYxU5rbD+1myEvbTcgt/MERgTBlvnWRHyWHyMWphtnfy2q4x0f'
    'zh5KIBpptQ/Whjjco/ur6vlD2zYaP7ZHuMeJlpwgAp5w0VmuoMVFV6NrLdcl62Z9TJUwyokf0pS+MYCkE81AbBV3jTd8vLv9'
    'PKvEGHam0e3tDUNhbxfQitoLqxPbC/XQ/NClyVgk2YhFj5g3iWRkAiL5C7HHNcyCSInISDTwwEXtHilpGmKQBKnbBXqqibS9'
    'l3m8qYw7s2wSxoh9DF4I4YPs8WnWATG44Om92nmAj/fOx1ls2tkgBHoRYeIs857o0oVwDV3k0JncvT5zpuj2K/dZ98/Zr0M6'
    'ftqaJ74PpDNg0yKB+iYsm6d/eL6eF+fH4HeyvkcX+yKTODDxmBZfA0R35NR7a8JmpdLaUow3f9OsiuGWp8eu8CLW0jhyAmlF'
    'ToPFT27PFr3zTuqnXuGhwyfpSxPel77xNpfxKakWLushKMC9C7+agbcoDkAEv3AaZO+FyooaXwS0o3N8O7QYesFaOr430PGR'
    'g/lICTLBZI5uRt8c7o9m3r0KTY28droiW1E81r7Sm6gm7was5+B9cEWvVXsA4LXMmgVLwDe+Eza9AncG0b7oCGbuST2wS1K5'
    '2nmHhrEDcMseiSNjEC8MCy/QYIoaRcu5PAXsmuRvkJiwffBodliGSl+6kLt7tGvQY/cW9sfrP4++VHhjjCxERj36eku2G+wL'
    '8HbxGqmkolnUeD5ZBtyluebS5MuHVhfqXSfPaZvZdmIUq655au47jZPtS2pNj+F3tViKbPZKzsnhyraj1ELfdV43PML3Q9vg'
    'flSowGVfrpGuhp0za0VNkqgOQ9FzBjk6SrPXOALUTCezANFTEy8PwfUxlp0AkpPAFNZ2HNtGnVIQh6vPGYUMG1AByAL72HWJ'
    'c+8KZtExuUaLWoHpATcAWK6H95nRd13oePmwNEdoSu6ngxFYEy9Emzg8a8NlBDw8/zygjm6GhErOKh9t6YY89sOhrKfq+QRG'
    'H2FNeiBDx7f0PADgtljKTPWHBYZC2/UigVVhWb9utrkvatT3RUTn59frm798HxnRCxh8vYdfYB839BSeswdjmG5jAqbJLVg6'
    'NhN3C5hPEfkHAnZDsvAxPKVLekLAKEiWds70VhNmMrKBJk9K+JjoXEfhruge7cAALiBUIrexIcBeQbiM1jO5FOSA6rIdESO4'
    'CT0GrLCqBkb+fkGfikkeOhggNVIh6xJIephPiwP/Zsu4sJNwbXZYAswBARYgWY/5jSJcSGjhoTM1dDjDdQBcBe5NB0vQQMaS'
    'sjs2bQGYfmJGtynGS5zP4epsU6c0H4aPZt5TP0YXXN0TYPjJ+0dKPBNR14hP0P1FKBkzzZtGYLSLfFZi8MMeDsnweQekZWeX'
    'IzVCuWRNB2jasbjwO883W3TwpMDhqHtSNjMM8jXsS11oBY6Wl/bGoPE+rr2V9WjPrI1rsBCEQ9ZNKKLyauEx2zXrzfk8fMd6'
    'bOyKtZXsoX5obsoDHCuVB2k2scttbiS4UWgRARvAHgiLa/PC0ol5zxN0QAjm2+4AU9ThCwH4ViV0HawRa7zYLnOXiRVrmCgM'
    'DmoU7LtR2yrIXkadpfMzGomKxDTsEwBuIzvb92cdHFUPVOR49okyJt5FBO9zWFFbCg10nRx61jpm1GwNmwts7ywJHuNS8MOB'
    'SL2D9xHRXjLcls2+zdWAig0xDBFiVBLhABjn9HKSMLSiONGRHy9TLfxFDpoRxrnk8CE4SPc7wY9UeH3lq344lRe6+vYEC59k'
    'LkffBAPFDAFxpBqXcXQkcwvIRXkM/+15EfDZrZzTQgDbR08H/QribdEFLssQLE+wQm2rVauhT2QFmQ90TR7neFcKCnV/0HQL'
    'D8ET6Cj9mzl4RVOiAHptnR0mzZlbZ5WGHWG1oznMXBA634BCp30YNPCbeoXD6oiEHjTPUwYBtbBgz4CdiIiGATsaTtFIp2cN'
    'mFd+ZeViPRkil5JitoGpDGAi17MTQmlD7imIQ7AAA7r28ujUKfEX3WNSCtFMwWjo8b4Oyzicd93dPayDI9e/MMbNcEu2bBl4'
    'scYpYuvWzm1u2aItBdZVUUw2xCNLMzkPNmqTPi0kvZmJ43Y+0QupwKvZ7MbbRQyQxLvENuzw6x0b0LIUKOCfXE8ha+z9gz5w'
    'YYQst0kYtKZNoSgKJHgCNHj5NakcoVSstA9s6GIa4W0WyU7kZNyKr0X+d57WGeJFIgyUei9Xap7OE7kjD6HSRB/t7Qd11rIu'
    'f6gQtE8wEOP5ed+kgv3GnGUKnWmSrVx6uUIkb8mdZfvb4bW4dP9loTvTJq8FBfcJPJ87IHYYXBzM5PSDJEZXgO5Mii2XeBO+'
    'yvW8u+ypij1H0x9iz0UITg/+K1gRCRcJ2mj73x1vRC3dBHdclSztUf/KLmha6BUOEEQHS5Iv8fgR3XSvPEgCOswN/35iNBuC'
    'aKAjZr+eEGoBqU6CTtSHCEM0MhvZX3cb+mCBGERWRaZ+Hll3GOAFHCfuqQdyRxicu3xorUhIawrN82qstTo91k/lQWCi8rUm'
    'oJjMWcizsAbORWf52Ahxr482cTTi8zmT6NtD2oXS1MzhmFjqA70S2cnTR1NNyV7qhLcBhcWde2XThLLKIJ6icMO3ZIilF5pg'
    '9hrDIu2fm2hmwr+dc1hluMOtcnfR3V4n+DooAX08q0MmxvMInjU56/Z5zzP9ppguL8zm3zgaJGlWf5tkk/rpFaWq2zQIukk8'
    'STk9EtV4obxdsdhIZpWlYglFXHlmmZXC/pABo0OCey0zpgnLOtiUPuwITW4Tb0LOD0Of1mIUIhWc5yWt01KxZZkTlIDWdgFn'
    'gOZ5nYSr0n5HzdgqbAke2CqmaXOsI7puCAGBUhIKCnLqEqX2dx8+v6iyQlARnQvHKaR/a45Yl7I75b/IO+siyVYQCOifDFVe'
    'OaVkwEWDoPHhAcee0aqTlJnh1rwSh0pTDOjgWQF3vIHd7+c/wztaKQriPx6YQQH7MBZ5q8jkRzVyc/iwNgdsVS95bBrNwGO9'
    'XK8w5Vgj3W9iBnfNQ+Sy0cl/Le2MIeM9SmzOs+iAaQTaWK1Mm4VWDO+CWNeyfWfE/hrRr8iQHFFxGy8l4GcnQK5SF6zNuHgI'
    'FrjW8ZATGO18SzLllOxQNNQr4oVN/P2API0CXGfuVIFolfSL9gZ3qAp0ESYvFG5Z8E2ypwT1Fc2DxK6cEmop1U9M6hAi0LEn'
    'n9THpWT4aX8ngBxZbvLqDUZ4ZXkLEO+s4gcSrSL7l84icmAcUNUeex2csJxOKKmdFNmuu6Hve/JXJwjfNDurtobqogdiN84F'
    'rkr0Vgehm2a5asDcHrJsdcdVwONynioED/YuqSqrOwMHK4sdBtm6aYWfhVQZT252AM8AQ1S6fEtMxdhSSe6cTD0TaGIFc96y'
    'Z+w843QwBb5i66WHyBxXv5F89IwEtIxsDBCq+4GGhrL9YxFQq4AWAxI9iFhkQj5MhY5kBKmqGDjrGsOxSAhJFdASqnamFjoP'
    'twXidKgx7auaDhTNbJcAm1rRMjwAezkaXrOJYZufjdpneBqCO8e3Ow0PWbYoNQ6pd53j/67DSVEDWi0VxFLiFXFtpApqhYoH'
    '7VcQASZ7fpmIsTRJn6Mk4WUGGWx9UXPFFBW0HNSnXe0SNFaAllUKxF6W3NZhrnRxhtTce7uv4RyfMNeaV2fvU+V26QrWNSBg'
    'oa+7cv8l1HKHvzoXCusWrI7IYU8dg/5dN7kz6x+UCSCaEB94DQllrW4XT5Sy3rRpomeKjdVSz0NHQknSccJc2i9kpuEQEB6F'
    'ywMEX5Ti04IXPapmE8cNWriMUcfzLwlBF6kAt5DpoG4CSh9iV6cSX2hF8EdEblr0gW17gfRWCwY4msFyFh2vSXejMXxDRfpG'
    'YgWiHZqtRZE46lqjMjS0KxKaw9oJbYXuEKzOTICS1c+qGERi1zHehImdNWX4NU48O4kLCwpEuPHggutKRwlQ9FQ3HI1QzDnG'
    'EKC4k3IeaUJSSm1cu1vAYhFB7TnERlwjurbImIgX2f6CLAcTfJTy6G5yKJglSZdMcqieZk+GKIa1VqaoHe6gA1YeesiIw0ld'
    'cxXkaPirS6VyKzseHuBZpfAokLdceKLlIvasqJQ3pWL3mJIwD9nzWXnzER3cYy68PU54AbvSEjVrUUKXWQ6dSL3Zst6ef9Sb'
    '26uoWgXe0uYECAudBaBgCTciVqBeiDkIqIT2dYvKdmVZ6nJTaMWwBFTXRerTbSi4inCKT7VANxTtQH31kr7xurL+JNh8D6Qa'
    'Q0KwE0bEsZWgGJFMVOxC0sBdhc7O/AM/gGg/dFJl0loIoT0UDsH0IWI/Ezw6nCpyN8B+6MIVqaUe6FoyBFDbmBE7I7HM9aGC'
    'uf7QPOUcHxzyt97DwGftEAOIYLPkCLXU7WBfJhojA9d884gNXTEqxFrMXkeE2hXhvuIYAnpDlNmw7ctcQrYxMH5x9McjDv5Z'
    '4KnZx1F0Syc+/pEPe2mKzr1/E3yIKnzkhcXLUczNxX5IytoKmrsFvLapEg76KmxlQ9OTgS98NwgMqaJITmCw3WAwNecIdEhW'
    'Ks/lOdqQJBVstEj0LKUms0UCMElBcaF5TaOypmGqcICjgszIxjnOfINHVCgnkGcfAGM9rjc/xTZmkRUwcaquVpu+CHcSUiqO'
    'yXRjF/lHvLoFd5+fJlqZrHpsjkJEQFJtE9IPuJRru5x/UUy9jO+pwJPY9AkC6wLTZLpYBgq+aDr7aANKlZOo5qEWdwmjHTgC'
    'GFi3bZXF10LFOek4QOhq5uXUF0GgesFq1gWs3USqVmkp0woH2uusLEioNs4V2GV3lpa+U4rr7WpGgt2lhTVSg65433CCw+Lp'
    'NYjC+3ZWzNLEMFaTk2IWy1fOimlP5Pu6fyU6DD32XFKJw3HJ5benqJCuhG1SihIvAS8AgZM0tlfqx0uGMWht1qxKBTCj2C8m'
    'QyvoSnhoznZXDg10pJj9/h6CtGKB86Kzewj9H3mxu843TVJRY1FizziBWMXTYRoXMVWmRY+RwyZYUbG1FImr8chD/5GMZT43'
    '7cvpBSpI4dRQ8cJccTyc3RRYDvhAVOaFV622jdYLRWn0RFufvaQAiqI+7mjlCGSUrkcIc+2jD3R9iHUQCPnkqZYVbdHKdUgO'
    'XnI20Vq9m8wWYNEkbfDWSiRXrJsnsIKqcq/S/OvWCyX5BOim2rwEadAi5AxYydJIFa5xOj1C5DosUUvzbV0zHnx22CWb2u+0'
    'rIkS/g6lPqpbBtwG0NKifBFWRNFiaiqVUiIfkVGNYilWlcbTJFZ6tOUGfKTFogOP5Tl2ltN3Gb5+LPnSDPv5yb4I4IsWb5rh'
    '0qggc3ZxIppMlxogPJR2XpSSmSJ3mi8awjwnlvNuyKQJ7n2merp2x+bLWBSIHQ31SYh3eUCEKtXDI+gL/WYPkRmdkRknoDMu'
    'tFpDXFJnPBzg65vbT4CIu1GAgIFhl8ZJaXZWVwUaQveOdyIUYaQFMirYAz5v8w7oQ4iu8UtpMjEDxXF07PBCYcZeYX4EemrV'
    'jQJ/OqRBzQiCVUMMv+3s20QikWMRdbkkJQqKtmBnWKw6l6hO41/b3i0JYbZx2GQ0JXJJdu9w1Uru+AKdJLUoxjzYISX1aK5m'
    'EFlfAxwJk6QRpXqVgEkby4rEVZsKUO9nP7dUOSJcYdWEqzeiCWjLTTL2qG6tyA4N+zNuCUfteVFsTqcN0sBJcb/Sik1iUOHX'
    'mYFG2ovtxPoCFehpQEuY3LkQfe5nYQLRKO6kZmT4map0ohI5u//kugc22hfHMq2BIpVW50s1G9bPRTULxENWDfxgMYyxiAO0'
    'GTjSZLFOiLcLkOGWsweudy5rxPrMsYB2aEJm5IglGYomkYU5NmCOj5Glo5Gd07SOY7WXGHVorHvTmvM3V/E4L75djpw6BMxt'
    'ISuvhMV0paiWepVHpf4CtLtg83ngrxeysG8ZK+LTRHwx/s0YWdiJHcZAc7y4FVU9Je0nKLTypmoVw6E9hfnHhGI2/vYTMOcV'
    'VNMSJI1jcoxccQQeB9yaSxAY+YNqRaVKNO6gIWtJWZsliWr630EMQ+nQ4ds7ZBlzUdyEVOAINSuAB14SHlpusVUxmhJ9W1Vs'
    '8YG/FuGMV1L53LFO0M9fr28+/vZoV91/9QF0IueO9AzpT8gHDqJcbX2Z7yZWWpHMukagnbu5UEmvvNjr9pXs5CHXLczFBxFn'
    'MhkcI99QYmfUzEVkpnDiNvpXHuwKDi3F1iV5jCBeEJVTEKvIpdSunAJqq4I2AgwBR0kpEHva7RtiSRkuQ9DnIw/2p4RFaW5R'
    'uJD8aomeWpJ7q8Q1HXswGfCq208aoGRGMoRiuXimO4yPhACpSi1xT0qMa7Tp6vPCEScUZwuil1H5Dxudsl3y/pKCEVomrM5a'
    '4jE/BorcXtPDHXymLqnRjxpDX6szL9D1xrGCTai+VX/ObCoo0gjR4/GmmPfhx6amLtxGJJOSAakgBzkZno6VZ4sQchnehgqP'
    '04t967rfPqcm1WJW8jVauIoGR2kXcaNaEfKSQjV9yN8K8MTPnwaFbgi/Tm6xun/QWOvC7UoRpEpy1+WfCWSsRAHatqrVWtA0'
    'WwjHM/9zDalU6IzSzrpibrw+aSklwqYMWkYKo+XGL78A8+RJtgpYbcaGoL6qW8fYqyQMQsb4+UyLJO0SsXpaJK5P7EXCQ+G7'
    'URCuF33gEuNPEpA/CCRJFxXxDBs4IvLZD5ui1+IEiJCcMLlZwCCYEXrI/C+h8UQWZLo6GHC7qdBWGGNelTS9TBONEhBraEoq'
    '6/jJr0v0e/9BOpdeKQNwIs//vOr5w6ddqFXUY3JAfKO0wD7EalrMqpQgg4VIQ6qukRBhEAUXaPxGDUq8mfpdakHWCCo5Tckv'
    'NNz6bUwjGuhrJts8nVw+jCil3QHV0mZAcsmX1rAPinodxQuEgFwJ1F/FOxR3XopEioEcaxcKEbkA4IyiPFQEwp2kwDUI8CaG'
    'iaYs26FRAFshxDI2kmJ+sno3wVl1LR0tBRUK1Aa9OomJPFaCymFKnp4vCj9N3md2XdREv6jgjEWt0aCqwe9Q4p4AZ8qvQTtl'
    'whKUq3+nIGbUlOP3SkNWCe1CXRt/A4hRqQoKGChA4BuVgyeub6VAiphCKyWhIiwN+EHioJHnTMkOKHkbzThjx07xtFkLBU5B'
    'jHZAj04enZGQPWKOKVIaW8zhvHo1omtPCAmTVJpVzIq2JQl86XBQE8YQUGg2QMgOUsICY0rF4y+FoYzzTHSPAdCCCaAabNRZ'
    '8qoUphKPOfk0XbUseBCLrlq0YSCTlw9lesDNVb+ApsuDfdFgZlMhQz9iuSoWNqTU6TJ/bvVQLG+YwTCJ+lsN+BAJhkR9DM0M'
    'ZYJrPQMvWLo2LnXI0Wauw34qvgyGWkWMsWguRVh6gibDFkNkX0gqY1SVOx360coh8igmQUfMtWpnpY0rqqcrn6Oi4qGtJtcy'
    'hMo5ETBSCSaF30kvjWijAjuSaQyFMbwCf9BuREklK1a4VotJMpXjFr4m2kiMyhGZuiLxoQWfiD75KznUsc5qhcvIRNGbDbmY'
    '/fgxmFAee4NhjOnAUdKKpbry4IEySlG6hRxZIOSZgbVptYpJ8QIpAldDgsIg7siZSzFeKLucoQ1A4/i2TDVLluffKAqn5Obz'
    'kIyh8sxZ7DPa4RtQyU3Fw/00WmIhtYeYDKkVGvcd96emvHtIVLcIhH9AuGmFVxUFqwllEhyEEokfBBX/qpUfpa6xKDSV67oo'
    'BVUsZ8wgj9y10RJUOY+Jgi1hlok14r3Vs2wDlJ15eosKfmxVrj/VOcihKhjRYzrX2K4lEUXUl9h818o4JZyLMc40jXoV0CXa'
    'oItEnV1BKEcHdMWlNqMwTje+ZQK1JWF6pLRsh3BghaiDZNcis0sVpekfJmSIHI65EmsC9oPJ5bmdAkTQnTzKrSlxU7OMNFYO'
    'jTeFzVfOlRM2QBgGklTkFRelvrNhfJau/VxtQ/XMa93OhGIil5FkQQEGf/L1bHvg7Ti/OJGX8MmiuA+VPIUUvwukPgKpbbLB'
    'c3EiuspJjFEEwLH6hPncZwICRsOecgHJAFnTul/huRPgcbPluhXUCQumnfIQYvgoSQ+O6hPmAkDUmWWlFKhMHau6F0B+db0e'
    'qBqPIU1w5okOkoz2oYJJCkRJgfcY/uFz/GTVoV4hCzMdXnIcynnXLqltNcvPgZj3qitFcfU6dbVfmxQRxfdQyK122y0fKj60'
    'CveRygUyTNBr0jDSpsLAR/WeTC1pJBlyUmHu1yF2RLlxLOFZ6QW7YHVqAjVW++hBU9iFFFuAgHxunEpp/BrkwA+U5kDOJoYn'
    'hrROKpNUJZ7p5AhduYbl52UHaMPgeBLyMBGw4tAarvVFmcYZVJsiraRUIxPFllTBbeZhZZSWSCQQNSu+S6x6WVdNPXBIq3FX'
    'CZ3JVnMOaCgptKPzmtX6C/z6Y2sleWykOG0CGYc5syxeK0bzgfV7qeqnVGiAfjaGARF4Ya5EZJ+hiUgAlqYjueNeo29L7Qyv'
    'UGN/23NRqbFVhUFJUd0UFcu29pjtlffsCAQK07DG+k8B15jRn5x+pmBCjmYUmxckuBWKRqU+jN8lyEiBMmld6Vi2NJ0NwL35'
    'KmjRyDqQphRb6wxfShI5a5VQryExmxqlQ5JuEhvXRQaJMD1k36NSv+zEak5UXpTyzHS16S4d4TqfQnBME2ii6hvty1zXrxHg'
    '3PQyr4lsrpq3gaQsF4Vegc8SFp9ddVj6URksHa2eSDYLefFo5JSscyQ3sCmQJ3LQD5pNVih6NWJedFzXC7jjuY/CqK3cIV6/'
    'iew/5JORlEYvKIcUN45hQPpaqMQLhTrvOg6lTV49eBEH37JIv1owIBYvNlxXAHbckGOdSHZWpW1liWW44sOadUx00lPT8XvC'
    '/Z2lwLbDQIPQ8F/o3DWpI9vHXmRaHGvtY3GzUGuEa0oPcA+X2A4gNcgNuUoIkNkO8+CNqeoV04pyLq3Hn7Ijy/hTyk49LiKl'
    'oilw+6r+ukQGyx47AMxSZFHtAinv7TRf0HLxXnOGY37xYoESAb/U0rTINoI1O1E6Ep2LQcFPylktJCNi+QfmXisy0ZPU1Kng'
    'SPlF6XtVdOfEFgANEKgpNRWdruAJbBOTZcd0pgZfXT3qFCWCGTTK5FIhUo0khXxzsPCs984w+BR/xdzDvhOogMlyni/30Jqo'
    'MglCIosaE1zHpkGjktJNFQ5byaO1DQJGMJTPlCsIk1rQBRa4IhiySRU2qtV1bgiz0LCJxoDldbML5WQ3hGOhYxajYsCF5cga'
    'xoEdbdXpmJoESaeTWvR+MSWyDS4n8HGQ7LCpJhxFn0nVJXEnn8mqFxl4PD+1YHCDFUaKDYaUTwNaUvOAfjRC1x4Zb2Wa63k3'
    'oZYrdDwVOXGmpOGZpxRPUIwVayJtxECKj12F1hWE0RPDls27UluRu9DMnC3cRrHJktEs7zU+olkqalNm0uSUu6++j1s0ueQG'
    'hRU4K1jUJ4us2GpJjoiLS4G3/tlQX0QJInDU9kSjrJsruKKCCK9Kgkg1TcgZ8pNcOlWLG68CXlVhtcmRYyqIwWBI2oKpQApc'
    '9pHjGflj9Df0x6kFh04eQb5BycUxw+yd4PdTkQdWm2Xv/qgRby2B877YZo5QDGMwiIj51MFKHxSILu0WGFvgd5IP428z+YBL'
    '0NozF/wbdyPRLOhFu8V3s51YMgTzyAGKob/bhlJPTelVsZ87X+viZSr2wl7Gzf1+Aj38H7hqWbQ='
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
