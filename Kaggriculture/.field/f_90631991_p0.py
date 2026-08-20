"""Pool route 90631991_p0."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vW9cR/S9acxFStCx3p9pMLESxDEkukRpCEKApChTpIu2uyH+vYlHk45uZM2dm7n2kVK9MUyTf3Llf83HmzOf/nvz9599+'
    '/eW3kz99Pvl4cXt7cj87+cfP//rbvx/eeHj568+//fOX/zy8/nzy/vJm9fBX7sWfP/3408WHyx8urk5mJ2+v1yezhXj79v1q9XHw'
    'h9vV6t3D2+v3q4u7k9nr0ds/rK6uP5zM5tuPf7y5fvfp7d3uG6/u73+f7Y3n8u33nz7unjQfjO3zyXp1e/dF1g/XN3fvv7zavjV6'
    'sa+I29XV1e6pc/Op2w8Mn7r961Apl1fvfnpQ/t2njfY4OVQlCHE2P6GJsFOL/cicDsBDN1857T/y8a8PpNlNuTL547eGzx7P9dXF'
    '29VWk3uPkGPTHipegYd9O9wf+8rdiPHHmvrjtx7+/+Fuu2f0dyJPfnsxVuBIlgdVXdytbkavnh66+9RIDKTZ0Vm0FWIo+eri1nh6'
    '6Jd3PyjVtH3E9sXt9SdHXfIJykLfSrz94bbqGq+J5loTS0DKrzzz8UVu4nfyohmrKE0eP4PDoKStzaphpnk2/HRCX2ixyc3ZRnHj'
    'g7CDBon1Jt8B10hm3SH1Zc6FzTsDOXfvWI/KPUBR1vZPo0cmR7CTV/zw44vA76KPAvMKfO1pFTKftS7awA2JPnp9dbV6e/fTt6ub'
    'u8ury79+0VrrIUwhz9jIAx99Os++il4WPbJVvn4UerQbJ2YwBbOl7c4G/M3NB5bQ34zs9NC3bT+hZvPDb7NOGV73MRuhl5oiMkg1'
    'NfBcWypJuuK8TSTOvtijbQ3v7FtXBkXBSIRWKt45SZ6AioIDOlJUHPA0u69h6X60UvBgCSTMzrH7nPTypn5ywdSOXF2Jeyl2zDa4'
    'hDJXT491mLuNC2df/sTrcpWkj7fgveE9xz3KEgdYx7s3pDH/ILdv2pTK3KNp0jUWdv9f0leyLsfoRcnVYPIp4+xb3Nae9fJSYj9M'
    'OC7OD3Yz02fNvEA7ulq4k4wQ+/uLm7/E76yxia9G7TeipOMkihkZ1Amy3ne/PU5kZO4+I5Bcmja5rLaTlZ44LV7vhtoLM6idUSX/'
    'VhsA785Bn1dbbQXLZjhZux/cezc+f3KuQIbRt0xSh1wp0bN1kmTulVnRVI7CXNrJ7MrTC2VGi79oJW6qJsjmUlu8+rIMPLNEWgjz'
    '/l5mxWdIn3tH42NO7WO/u/yuk/lP77BGvmYlbkYciJap0zFKFtLZo4AxlWly5KBILVwqVnsv2W+cytV8bjmskic4hdcX8T7sY/+g'
    'KSxgLR9HCiuQIinmsHYGXSqDRqXAMvFN4H60DQ2XvWh/GRMuc3iGWrhnraaoo30wxnImU1k17FqbXNb6+vrhn/k3yB/5Q2kP1uS7'
    'QvnBxou5vbu5WP95dXPz48Mz35gYj8V9xmVTDJqR18XWUSTuaKXCQIYNpWstX9Any4IIFo9lNuSS2FUpVwCfz5sRepxSATAHnu7b'
    'H3jowac39NcM5DinoSd/b7DF0iajAP1qT+ZKLSI3kr1ulCqEsAqUCU3NI7DblFg4jpSji6TXwtIkAiVBhlLTy00aLaCqZSerRPKP'
    'npyLg2pO+cX4DIR6CuYt2FkNZY2sWyQ8fQ1QS46+ArPX0YBTigy0w97MHybNc1UsdUYNNbm7wHi7lD9TcoquoNp8ukIEHGtjv2l/'
    'RYd+oEhNWk1Q1y22Xj4gB6p/us0e8nRkoQ1MF9ZQipZrAKbE+zv6WivZlFIedcoOBIXBjt484MtJnwR4LMtEubCWODu75xHa+77c'
    'PFumbB9nsqhOlldl65XlBS0NGtI8Z2fUvW31a6+IOEIQBHz+VTyRYap5bFkrZfQJe0osDmkfA/RCV2tp+wLZ5X7CcbMOA4aRigCp'
    'xfm1OtMVWy4tZ224Lngzj1gfztwwi2MdgSa5lSszCqyEnrD5jhrz1fZwxBwg3EvnmHAVJMWHUDMeBEVBD/cOILrUF24FYdGa5cox'
    'teBTmP9pNdegICVzVdBa2BRYkBWFNPldyr774fLq+yfanhFrzGsj1H8WNgNj8fK5H5k2mStilp9hmo6RVDP2fpT3lTQVdXO1xnOD'
    'zgPqVLMFKcaDYTyWtFvrkbCdXWJcuAxIsnU02DV2zazCVPh4cwlB5HzEfJYbZs88ujCTTDZ8PaMJaiXzSydnhCrXAOJUUoKou+eW'
    'rHza6s6ui5IFuB234mNo1Em8hyXHvXsWP/mmDMlhguQwVT7EDxIs2x6mvESN645czrxHhdtg3RJhxyyYSZ5m24d9wfbOqrip7c8Z'
    'q1U+VyFkajO30loduP8yaFmCyfC2ci08GnxS3k6f7EEA53Mu/YHTqtnP2v8LgJeZc4ygIarKJBFqgvHU591c5HwFZrCJAs+g75CQ'
    'AtW3kb6DjXrpEaJm7UIqsFzPEyMVqbWGkSLSBo6XrhxdGoYWlfpmshCWipACaZ3isl4wHQRRWDNaZgiECyEQ2pNaAYeGI0Ut+HvK'
    'TlrjzRPYRmltAhCNajXjRRnePE3XAbhWUJYoeBo0El9bIfqyVbYfdqQsEuOc5Iv7TG5AUziKLPgSLnjdwrSOprt3N9cfOVi0HuIe'
    'GmppvdIgLbG6pd+FlN5W1QC7YDsSW31vX4j5QYpeLCOKPm0jM/I4H4cRXRunFTUPuDRyMvtFCgGVwrhESMDtigDytdGpmstjMnhR'
    'J7mg17aeOyVdQINc/k+ZrMec4BnYxUyRD+v9t9BhoRUKi14zogDDQqXFaQMIG4x3KH/0C3BmDkTXCDAThnUKKzdsazJ+c2F+MjZM'
    'C64KACoF0LGL0ltqby7MN5Uh4nCLzHYAnEwREihbCeDKFQenQwX+Dwk5FJMLauAAXJLB5GtWcGT6OKDjdkqVphDx+fMQ4ixwvG3c'
    'yYdG2skgFhIPqx3aYAUlnlJmP6ninsDSM2NHxAwtG+0+422qi4kdKWJWY3AV8yBkFA8JHTY4OoZivBRUoYj3sQFAoGwVo2/YO13J'
    'YxfosYm9CKYNTpJX95NdjUpkl965i747V8mCB9fljONpLFVeo9CZkjwH9TgIiBK4/EeBj9jeVIOqoVz5aqp1mhme1m9qdDskkQHh'
    'FVdC+MpxRKSmDxWl4Be50DWCr71zPxUIUTZQpuSu1+iSO0oOz0kVNMGQjLtP1iT21pepmpz0te3h1Wt2WF2TbZFQGWjTjdAu2lYK'
    'l9kBFCVgNozEpGtDmcC6ctBqMthggzYMc8CttW30EpQmYkPbInjggIxkp62MW0fIcDFpPr/kIZN1FBBVPpBfYnbBQCTIkouQqHUD'
    'FKhjwrgGC4UJrK8Se69QGK54LAYL1k7Zq9COj11pUylpH0uArL1W/umoAva2LTWVUwJlHlycR3NyFa+Kf0sFHQPRbju6C4NmieYD'
    'mj61MylZpIxqZb0JDESlkmwtVpxWWLhq3r7EaknY+pni5NwTW3tsL7i8YFhI7IEOrEqE1y8AeXAYzydWVYbagGru0fI+QBa2CyhA'
    'QVHFJ8HEViMfleqy84iwoVKmUo8gfKF8OnTvOkmYNMMsTRQTdgQhh2ZQ4c2hnxkHEbPTNaY7JNZ8HBDBoh7sE6a2C2xjD1H3sDX/'
    'vLYn3AWQehLgAAoJQbIrSVV4dlryqV10KbVe/LGpyNEfhVY9e8bk1Wu2V9XTwGEKLP1IgU5VoTBBm1T+ZtJL3KMUIxnnHgE+Qb85'
    'l4k+u1y1ybPjh5DHYUXAPAI+rJ1pkmFxuZ09D3jdttucTBnhGkW30qAqDzt8tQOf71G399RXPgfC9M62Ui0SqM+YLpwxeYBAqSQ6'
    'Owz7wCQ5x2buM5NdbOogh3KKhd4YEZ+4a06xpbEfYL3tk030DHkjm2h74NP6pgG0d8TQirieMuXI9RRvlrGOrq6Ab5buPFpZaDhU'
    'ArKeDUpjM/lJjqCgbXbStI6nd37kcd8CkItwD7Iigk1j+qavMi/eYxQ/a1CAvOH3Svn8EnkMkppDuH21LzU09uL8iF2AmOWMzaEl'
    '+Pqg/4M851LPc3YhU5uiJP2lJjWboTt1y4Bi8myRwIwkCoGtTJTkFjOaJHwP55UaJTGPBOQHl2xN/4w5RXmdXdJnlfLetGOI3Yzm'
    'uUtpJlOOY3tlt1rsRDeT/inMCEov2OQjvuAbkQRHlq5yFjTJATM+oucXwfUdfkWnJQkMh7LsgkWtK6LePtWqDsI+fQRrppqxxi4B'
    'ieUohoI2CUcqzaimoJTUnuSXD+xyhepXZnvYawtRZoMcV9udjrJVMi+pFKYCtrOClQAcHk1QL2EZy6KW0pRJjrhOPvJxSVNKQU7b'
    'LslOWO7wy0fr4Afhy0eTO1W+ITqVqn85w39pVwfaMFOrintquCV8gVK3/C7iakNNlo8lC4zkf8a54v353Hx/f1U1S+a2zzEPIPim'
    '6Aw4/NhS02uOWXzowXpTN2VOW9kiQMAM7dvBcuEYvQj7kpfaKSS4x9n9D6aG2VbgM3wdMm6264eZuKz73qvsiiTS9dr55G55sI2U'
    '46DkEUMGSHmJD93mXkslU9qrHEr1aGN2pVDdkREamoYqkM0glahApce2PFUwM6kiSPclIt2geO0G2JjZwQXSd5T3K6MnRhMPgAcP'
    'ZDwZ55JqI7eSmJXagmgheY4xiRGslYRVJih0QU+Lnzhs7+rXLxJecSxhGOaFFer3QiuLDjXkFA0+cdVGO88D6254imMi6Tby2R6s'
    'TlIyfBfADYnO1EmBCUc1QD6M3bYggX3XiI/ywvNOuao/y4UqgNL5IE8XWx3iNIR6GgVCqS5ma4L1JzYl8d0Bd3A8GW8f8D1Jput8'
    'gRzZFNwkR1gtH21MkPAL25bJA+UjBhWnwV+oArnhZnABSyF/WzvJ6fVtH3j6LihrlK/hJ4Nz2iul8RxurTlsw8TQEBkKAfgdlB5C'
    '/WxKfdRdqjUAc1HUz9yTZaydDBTYoqGoFiqT5puqICCLCjpGbTBRjIAkskgGhLg6eoC1QeibUqiKECIG5hjvfXe/z7+pMbfXmwoi'
    'WygT2HhEjiyWkB5vqIIzA4/yxmjBeJD4xzOlytM8QYY7NBvdyBKIlwXuyy3OideHJKAF0RYp9jGzkuMscWkw/SjLlctXD1lFsMwZ'
    'UnPoUKPUHQd+ytVKZZ0Zkn+989INb0fORczSvIea2Leh6NPjwJXsresysK0BmMKBZMM7dfgUXbUz2647ACEczDUGyxr02fQ3OyTL'
    'ZwPC2eZpWagOUfqFCN0y+zbiMCseLleSYiTYK4EzTQTgucPsdKYiTl4mA26KJ3dr+8KrkVA1ZUcbQOr2DWT7Hjoyr6I3juKEjKzo'
    'uZdMx8XjTQjqGIfd2zJNEvvJ6o+R/EUhar2+ChrxQwzn0BVv63IfJV/9sWAPAg3sQ2H5PMxAt6JA5izqP7Ys22CSls0llteP7sFJ'
    'UwdaMof3yGHSNQ02B+rH+ATKZlqZcE+qwpwGxbfDHQi3TAXbeNGRHPpTGxrMopT8zXydCbd1cLdRDLJP5fcj1SbJhtLUkQsc71SE'
    'MY1bwAQuipGPsvqpSZo3gCqkShxI/7TNDCXQC6AqAnqVGEVSYKyg0AzZbYOPAiUT780Lk4hH2AcGngNLGqPzEIkMKXgEGEyIA9ew'
    'VrHLsUg1sg8wgSk3HgyvKHEwoPmNctVVAYoRUb8FEhZVU/qM3cmo/YDPrEp3Z0SbA+Fdcl67mjVXnqzhDThMFWPOhnxitX9qJCbT'
    'qdiDCr4gkfuprMrDMYZbtAzKnC7poMz8m5fEwnF00RmboMJm55DohjBNh4630770iodozE97djGk4ISonw9/BFVKUkIMGM0k7kRo'
    'ykSHAjiJ9apFEh+kvncf8UsmcwQRZhYYJi07U0kmK7thviZS+I/SfWHajX5dCFj4FEodEo3VA1niwLZ1JdDibXqwmOeiYPq4Mx5i'
    'FpKjvEFs0NAKZFgzqxX37TE+iN6ZTH2jEHlj6I+CyMh5bEw1eWDKvAB8g14pEAfFH1MB3oQwFUec8KYDhCkGvMGtGOsgR4jeoeoY'
    'OT3m1iwOcRe5eGSN0jaCh0NDwe2mh1XAjzARp1OBilmasSaGPEpZtBbER/P91gxEEGebFIKQBLCKxO4hXyS2Mpl51JcWLo59mu3V'
    '1fWHL/wVBK5tRXUFUGaGXJhM+N11SLKs5+AwMk3Vld3ENsRChFPbtQo4htfdNJsiK1UGL2G6mgkTSmuXrnmTbNBKPNClqsHXozZZ'
    '/FESCt95eEgqWArvn9BxcX6f4sp5/LZSUyZBmBqjzqsXgGE7Puiay4Pfgok40bNITXMSQlfQa5abzyPYWssaZNngWl1Qmetn0CkU'
    'wvDUm/rgxMI4uqDGv2E8qhl2zbPLc5sA+5T6dvOz9ZnSObQzODBQTvuL+2QHstxOQAg0Xd0FaF2jaFws18HW9GR5ZQIAM6rTTRnS'
    'yADL+Oa4iEgbF+OBvRzTNd03l1/sUjYFLoV7ODHgMeQV++2unLfUwz+Hp16LuAAu/4K7DcRVghGkgDZtqiSnaE95S4+Q5XAqypXO'
    'HnNeASKzqhOgH7ouUnryKBOEXM8mZC5GWXISSFURScFGbfdVFkC1zkRgMyIDKFmUdMY3zCg+afKxTF3i4zT4pXOLSrxir/Bu72d5'
    '8NdSRjOWz44E55kS5djIMGTjByFhAXTXoie4i+jOq/6qXKxWcUGjssC1z2MSHAvBrFwLtDDcDBjBRUWHOPEPz29Ks4KCiAaTDSoM'
    'Ph6pCYw1GmpiKxenrdrTRwG7WOGQorJ8IzwkkXo9krqFozTXRgCWJwQK9C/ii7HDeBAVdoWWAl+JzZigm7GbHdP9U1YtW01lqgDd'
    'M4hryu7QyTTqSAUZcNzAPBkGgRQBZmVkrr2ThVvwo3/kqVlce/7gFJQKQx4v43JkgWHX9YUGwxNBIwQCD7OhFl+mzFNagRlCayWU'
    'k0OmtFmGysmAyJZhU/lkd7T4V7/siliMA/fzAIZJvKEWWHaPO6BFaLCArQHBxKBVdQxtpAJNrSq9/CYbj7PMkAIKRZT9m3iRfdIm'
    '4eTSgEuLr5Wfk/YEo5pYghdkleZZh0AeihBpQJDccLp0DoMl/7Bk7Ci7iTm8BWkK8V5tlHAHsT2w+OV3obrTGtylW/zRYSNCICTP'
    'LYVgpCMLPj7Npn65W+gT7VvtQWWFbk0UBa6xdZ8G9/Svgg7Z/MX11TKFpUx2YM1PFVNKijTUuAZRR6s5S9gDbYyXJe7/hmEoHEZV'
    'Mv54QIlAE0SHgxCtYsxsnK3dCkS/5Bm4BTs4lJlOZMg7fgAkwhiGvDsVoSWjL7Yx/c5qoROm0YzR16hKMQ3TkzDf2vIg4ndrpJUH'
    '39NDqX/xvwMOJJP9y/Ubz2OQbCJprhwgFIwLcqjxIU0wP0BU9SpB8vsHS3u0rc706tx3bGEDRLFJkNn42BH3Jrn+5gu+mpcJNnjB'
    'asngCJq3obJK+09q8lxj7Go7crOVnRPJVWK7yNDx8+YhYbnaDVto5UMmItKdkbM24S0nuKmIrLwl1ycPMUyvqwTz4yOZnLa8T7/G'
    'GqcAGkbZ32yOurlHcEAFI9907OpHsfK7Izhk4z9qBAhjYBMdHLo7YJQagxraMXcQXLM8XZibqDbsfr0G0eiAQUTxeQFczpSNCh3S'
    'KLI/N8S09exqqNlKMPSjJxDUQA8h/kRtDhON6FHdkv+3XIFb4txQt5vL8YIZvjNt4la1XqSKGCjRgaudA92jOXAZmW7LQxQh07sX'
    'JI4QVinbWKmhRYirWIWfesClxiDNn8EQHI8d4sxYtJz0aFO7H5WJovYIkN5N3eTc8EGQ5clry7D4qf4IZBZBKU4KeaSZQxEGPKq4'
    'WwnA0j10vdx7cnoMp5qw051tY7uPc/6ypCgP9ZMTJMKj+A+5F2xzD1a6ylgMc1hGlqFnE8HYtpHriHSexHyOFcCcsmNqHSqVMmVU'
    'aK3uItGCJFqm7OFOa0OkSrJH4Uo962i4uGGY4GJunDivFazgUqfe/Mp7VgnXMXG78aXkhdyW9136d3IQeeDNTNa3k3R6E+G/fLdO'
    'urqN098RdulkC0zjWq/25eS5zWDnhyNvx+mBXzPYwa5dONUcM8n1HbMjp+i1aUZfnGBPJaQW2gVIQB+j6SItFEBeeZn7QGzXz2iD'
    'LXRXB9OBz2CagSs+oXYagJSrSESBR2ZRMwJD7gnyrDDXTkg2BZoVbnOJ3oqi8NKtLSOssQj6gWGgmRJT7a5ClwXUOuDb4yFIoWaz'
    'HmQvQBHgEF0ESGOkS6VgSqgX3B4riRYNbyixHIiSJZEy50Rr0pSYyO+vdM1M6w0JJE63almiJFLfC20qVYl77+1tzbOvAYeWXSjn'
    'mIUMYWhsLJGJVehPNqblHxxOtEibzO6FigzxgY9wmr6JJG7tVBG41iSSYXyCcKTj7/CYo4TCwz9cr0ZM8uSU8TSlZ3ebMTJ7Fes9'
    'ctM2a69I5cqDSynGxTI1iTsXdyLLaKyhtinD1fyfpFMBWxxBrFqb3Z/qgRjkpEL2ie+HQHqwAPwK0dcxKEhmSfGH7TpzFJDg41rj'
    'L63THhM1CwJIU7VVVJc5ZX7rLj+sJ/Yv91AsS2ITEZVHCI3Yrfud13gpbEjHakUTekc979ItbLRqLu7uSrGhKQECuUVRhVmI/iih'
    'ZIrP3d2GST4tJiJwcOqppmxS3zhsUo+d8c5fZme85wQeYVIp2UquxbJPPz2U2wPjgc59c5amQK4SdtuFNE6ZgZT78EGWBVJw8OqY'
    '2/SxI6a5t3KE1BP28cMM6ZiVS7x3RC3+XDfNIxr3+VJ4Zu02XQAZQxVV4OnnWOsKqD5NAxuUc0XpmSZsIQibk7ss+XHYS6BOKgVB'
    'Iz0RvESpUyZSHkUjdfzGn0btEFNFRJweHLZDbjSNatlLErQ8VFCzS+oo4WpdQBwDGoUNzhAnClbp5qnUT+ygRow1H4evkmgjqlOY'
    'XlChUNeJSJPLejb3rRiNU8omkBpzEym2Sw5uBcKwgfA37i/Bmm7Mxo6eQac5fJlGj7Xyp8k6hoOl+NEkPcxdB5oagwPFufgEBdUa'
    '4s6ZdrAAxwhBHbFKsjBbZFOwI4qzwlg6wpGhvzkxCzfOLU9Hmq+sUd2ZnFYvWxIroPPrzZR2k6evjBk/ax2d60gYZd2XR8pDn6jB'
    'aQnP8lmPXO2+ue/S4jEp4iFaNkJqmWNqwuiR0x9/G0VgeNRqGpO6MygHQqVFHbsZ2mDsLrVOBLuaF/1bJ2Im7XoEMpGhbDwnGQ9X'
    '7JscEESuM0ToHSXPDeRJENMJyQ6kRBlMxzwpSRjUxgY8/IgnXb9HU1yx3PGu5azEvmy62v06cWisM89GXdXsogmqOYjJBVsVh+Cr'
    'cLreZwShGncFyDAm7jt2PGCO5/Fo4MPvgUP2grua//fmBRADJ2LWBIUrg+MIneiYFsAxK3uJ4uZuY7L47pkTB8TVOthYy4hT0g2m'
    'LLWxHTHgKII200Y26fv56EQ/YcfztOWEclaQh0smfSbxXswJcLlp8cR5ojNeZmDyKFoBPheertXzDkYqJ1ehtqHseI/YA5IWhsRh'
    '3DBcPAPaKNfaoROXAYg9VnrIwOoa5OBWxIA1FUgOaGAkBJGJDEzXqQiipL/tbyIOvPMMzR8k/oScVcwIQv20FMw0wUMgc4bbd0Ka'
    'DYr/RmcAHFXvnwcMcrQg4UjMNYUWy+tGkqEFLWcEtY97lOsskli7//3+f7zhMcQ='
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
