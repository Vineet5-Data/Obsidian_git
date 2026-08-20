"""Family-A pool route 90631991_p1 + sell smoothing + per-item volume cap (v28)."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vW0ly/S965oNJybInb1qbuxZWYxmSvMRmIAwGyAYBgs3DJG/B/vdoJYq8ulV16tTHvaQUP5kmKd7q7uru+jh16pf/Pfn3'
    '337/+99+P/mXX06+XdzentwvTv7jt//6t/9+eOPh5d9/+/0///Y/D69/OflyebN++JR78Yfvf/314uvlzxdXJ4uTT9ebk8VKvH37'
    'Zb3+Nvjgdr3+/PD25sv64u5k8WH09s/rq+uvJ4vl7uvfbq4/f/90t/+L9/f3/1i8GM/lpz9//7Z/0nIwtl9ONuvbu0dZv17f3H15'
    'fLV7a/Ti5UTcrq+u9k9dmk/dfWH41N2nw0m5vPr868Pk333fzh4nhzoJQpztT2gi7KfFfmRuDsBDt39yOv3Ix78+kGa/5Mrij98a'
    'Pnu81lcXn9a7mXzxCDk27aHiFXjYH4f74+XkbsX4p07987ce/v/1brdn9HciT/50MZ7AkSwPU3Vxt74ZvXp+6P5bIzHQzI7Oop0Q'
    'Q8nXF7fG00O/vP9BOU27R+xe3F5/d6ZLPkFR9J3Eux/una6xTrTPmlABKb/yzKcXuYXfy4tWrDJp8vgZHAal2dpqDbPMi+G3E/OF'
    'lE1uzp6JGx+EE8wgoW/yHXCNZPQOTV/mXNi+M5Bz/471qNwDlMnafTR6ZHIEe3nFDz+9CPwu+iowr8CfPWsh813rog3ckOir11dX'
    '6093v/5xfXN3eXX5r4+z1j2EOeQZG3ngq8/n2Q/Ry6JHtsqPr0KPduvEDJZgcWa7swF/c/uFM+hvRnZ66K9tP6Fm88O/Zp0yrPcx'
    'G2GqaYrIIKepwXPtnCTpivM2kTj7Yo+2Z3hv37oyKBOMROia4r2T5AmoTHBgjpQpDniak+uwdD+6JnigAgmzc+w+J728uZ9cMLUj'
    'V1fiXoodsw2XUObqmUIPc7dx4ezLn3iTXCXp4y14b3jPcY+yxAE24d0bmjH/ILdv2tSUuUfTrDoWdv/f0p9kXY7Ri5KrweRTxtm3'
    'uK29mMpLif0w4bg4PziZmb5o8wLt6GrhTjJC7F8ubv4Sv7PGJr4atd+Kko6TKGZkcE6Q9b7/7XEiI3P3GYHk0rJJtdotVnrhtHi9'
    'G2ovrKB2RpX8W20AvDsHfV5N2wqWzXCx9j/44t34+sm1AhlG3zJJHXKlRM/OSZK5V0ajqRyFqdrJ7MrzC2VFi79oJW6qJsj2Ulu9'
    'f1QDzyyRFsJyei+z4jOkz72j8THn9rE/X/5pIvOf3mFNvmYlbkYciJapM2GULDRnTwLGpkyTIwdF6nCp2Nl7y37jXK7ma8thlTzB'
    'Oby+iPdhH/sHTWEBa/k4UliBFEkxh7U36FIZNCoFlolvAvejNzRc9qJ9NSZc5vAKdbhnXUs0oX0wxnImU1k17NpEuaxnR+X6+uGf'
    '5btnN+TBmvxcKD/YejG3dzcXmz+sb27++vDbP5kYj9V9xmVTDJqR18XWUSTuaKXCQIYNpWstX9Any4oIFo9lNuSS2FUpVwCfz5sR'
    'epxSATAHnu7bH3jowac3+msGcpyboWd/b7DF0iajAP1qT+ZKLSI3kq03ShVCeAqUBU2tI7DblFg4jpSji2QqxdIkAiVBxqSm1U0a'
    'LaCqZS+rRPKPnpyLg2pO+cX4DITzFMxbsKsayhpZt0h4+RpQS858BVZvQgNOKTLQDnszf5g0z1Wx1BU1psndBcbbpfyZklN0BdXW'
    '0xUi4Fgb+037FB36gSI1aTXBue7YevmAHKj+mWz1kKcjC21gurCGUrRcA7Ak3ufoz7pkU0p51CU7EBQGO3rLgC8nfRLgsZwlyoW1'
    'xNn5PY/QfunLLbNlyvZxJovqZHlVtl5ZXtDSoCHNc3ZF3dtWv/aKiCMEQcDnX8UTGaaax5a1UkafsKeEckj7GKAXJrWWdi+QXe4n'
    'HLd6GDCMVARILc6v1Zmu2XJpuWpDveDNPEI/nLVhlGMTgSa5lSsLCqyEnrD9GzXmq+3hiDlAuJfOMeFOkBQfQs14EBQFPXxxANGl'
    'vnArCIvWLFeOTQs+hfmfVnMNClIyVwWthU2BBVmZkJbfpey7ny+v/vxM2zNijflgQI/Ow2ZgLF6+9CPTJnNFzPIzTNMxkmrB3o/y'
    'vpKmom6u1nhu0HlAnWq2IMV4MIzHknZrPRK2t0uMC5cBSXZHg11j18wqzIWPN1UIIucj5rPcMC/MowszyWTD1zMzQWkyrzo5I1S5'
    'BhCnkhJE3T+3ZOXTVndWL0oW4G7cio+hUSfxHpYc9/5Z/OKbMiSHCZLDVPkQP0igtlOY8hI1rjtyOfMeFW4DvSXCjlkwkzzNdg97'
    'xPYuqrip3c8Z2iqfqxAy9ayttFYH7r8MWpZgMrytXAuPBp+Ut9Nne5AOgXnE83yU/sBp1exn7f8VwMssOUbQEFVlkgg1wXjq826u'
    'cr4CM9hEgWfQd0hIgerbSN/BRr1MEaJm7UIqsFzPE6MpUmsNI0WkDY6XPjm6NAwtKvWXyUJYKkIKpHWKy6aC6SCIwoaZZYZAuBAC'
    'oT2pNXBoOFLUgr+n7KQN3jyBbZSeTQCiUa1mrJThzdOqB+BaQVmi4GnQJL6mIbraKtsPO1IWiXFO8tV9JjegTTiKLPgSrvi5hWkd'
    'be4+31x/42DReoh7aKil55UGaQntln4XmvTeqQbYBduR2M337oVYHzTRq7PIRJ/2yIw8zqdhRHXjtDLNAy6NnMx+kUJgSmFcIiTg'
    'TiOAfD1zqubymAxe1EkuzGuv505JF5hBLv+nLNZTTvAc7GKmyIf1/jvmsNAKhUWvGVGAYaHS6rQBwgbjHcqHfgHOwoHoGgFmwrBO'
    'YeWGbU3Gb67Mb8aGacFVAUClADp2UXpn2psr801liDjcIrMdACdThATKVgK4csXB6VCB/0NCDsXigho4AJdkMPmaFRxZPg7ouFtS'
    'pSlEfP08hDgLHO+NO/nQSDsZxELiYbVDD1ZQ4ill9pMq7gmonhk7IlborGn3GW9TXUzsSBGjjUEt5kHIKB4SOmxwdAzFeCmoQhHv'
    'YwOAQNkqRt+wd7qSxy7QYxN7ESwbXCSv7ierjUpkl965q2l3rpIFD+rlguNpLFVeo9CZkjwH9TgIiBK4/EeBj9jeVIOqoVz5ei49'
    'zQxP6zc1uh2SyICwxpUQvnIcEanpQ0Up+EUudI3g68W5nwqEKBsoU3I31eiSO0oOz0kVtGBIxt0naxJ7+mVOTU762vbw6jUn0K7Z'
    'tkioDLR1I/RF20rhMjuAogTMhpGYdG0oE1hXDlpNBhts0MMwB9xa20YvQWkiNrQtggcOyEh22mXcOkKGi0nz+SUPmayjgKjygbyK'
    '2QUDkSBLLkKi1g1QoI4Z4xosFCagXyX2XjFhuOKxGCzYOGWvYnZ87EpPpaR9LAGy9lr5pzMVsLdtqamcEijz4OI8mpOreFX8Wyro'
    'GIh229FdGDRLNB/Q5lM7k5JFyqhW1lvAQFQqydZixWmFhavm7UusloStnylOzj2x22P7f1VeMCwt5mAIH94A8uAwnk+sqgy1AdXc'
    'o7P7AFnYPqAABUUVnwQTW418VE6XnUeEDZUylXoE4Qvl06F710nCpBlmaaKYsCMIOTSDE94O/cw4iJidrpnukND5OCCCRT3YJ0xt'
    'F9jGHqLuYWv++dmecRdA6kmAAygkBMmuJFXh2WXJp3bRpdSt/LGlyNEfhbSePWPy02u2V9XTwGEKLP1IgU5VoTBBW1T+ZtJL3KMU'
    'IxnnHgE+Qb85l4k+q67a4tnxQ8jjsCZgHgEf1s40ybC43M6eB7zp7TYnU0a4RtGtNKjKww5f7cDne9T9nvra50CY39lWqkUC9Rnz'
    'hTPmCBC8CAcolUTnh2EfmCXn2OY+M9nFVgc5lFMs9MaI+MST5hQ7jf0A6+002UTPkDeyibYHPq9vGkB7RwytiOspU45cT/G2jHVU'
    'uwK+WbrzaEXRcKgEZD0bSmMz+UmOoKA3O2lax/M7P/K47wDkItyDrIhg05i+6ausi/cYxc8aFCBv+b1SPr9EHoOk5hBuX+1LDY29'
    'OD/iJEDMcsbm0BL8eNDbzHPK5KV0bCYhU5ujJP2tJjXb0J26ZUAxeXYkMCOJQmArEyW5xYwmCd/DeaWmJOaRgPygytbmnzGnKK9z'
    'kvRZpbw37RhiN6M9dynNZMpx7J/sLmUnuplMn8KMoPSCTT7iCt9EEhxRXeUsaMkBMz6i5xdB/Q6/otOSBIZDUbtgUeuaqLdPtaqD'
    'sE8fwZqpZqyxS0BiOYqhoCfhSKUZ1RSUktqT/PKBXa5Q/cpsD3ttIcpskOPq3ekoWyXzkkphKmA7K1gJwOHRBPUSlrEsailNmeSI'
    'm8hHPi5pSinIedsl2QnLPdT5aB38IHz5aHKnyl+ITqXqJ+f4k7460MZMrSruqeGW8AVKk+V3EVcbarJ8LFlgJP8rzhW/XM/t37/U'
    'qrZkbn+OeQDBN0VnwOHHlprecMziQw/WW7o5c9rKFgECZmjfDpYLx+hF2Je81E4hwT3O7n+wNMy2At/h65Bxs10/zMRl3V+8ymok'
    'ka7Xzid3y4NtpBwHJY8YMkDKS3zoNk+lKpnSXuVQqkcbs5pCdUdGaGgaqkA2g1SiApUe2/JUwcykiiCTq4h0g+K1G2BjZgcXSN9R'
    '3q+MnhhNPAAePJDxZJxLqo3cWmJWagrRIXmOMYkRrEvCKhMUuqDnxU8ctnf1hzcJrziWMAzzwgr1e6GV1QQ15BQNPnHVRjvPA+tu'
    'eIpjIuke+WwPVicpGb4L4IZEZ+qkwISjGiAfxm5bkMB+0oiP8sLzTrmqP8uFKoDS+SDPJLY6xGmI6WkKhFJdzDYE609sSeK7A+7g'
    'eDLePuCnJJmu8wVyZFNwkxxhtXy0MUHCL+wtkweTjxhUnAZ/oQrkxs3gApZC/rZ2ktP6bR94+i4ozyhfw08G57RXSuM53Fpz2Ibp'
    '7D5Cju50n0cpLFZzS7FR2NyHKXRjLscYwG67OpgYmw2+o8CWwiWtm6ioaeJjFv484MjtlE8JhJE67eFNNlTX0kfJl6uSDwrTFIyD'
    'KvdHVwyhVvU+IZNgV5fBVCDTPd6WHwXGxCoz+Ylh0zs9WEDkdXHnmRALkks0G+3IEopD/ztBftrMNc6JNw1pQMGvkIcolPqYScr1'
    'yE/TcCbjMMdsfyRVQgPHOfSvcQEBh4bKFU/ZGu3AakhG9om1N88HiS2zdQcwA/VwK7rxOC5cyea6bM3IovY6xgbAE2jyVJ40BJuA'
    'NQ10w0XobTF3mOM76ovpb3XInc/Gh7n9UIS/6LrDc/rhchG8ayOhCuSye9x8RsK9EkjThs049Uz9TKaLxoCp4tn3jfM7kHqmlnpQ'
    '5OApR9gr+MDFQEA/Z8ik4wzV/Al9JZI0vxA7DcXMIorjfH5fdr3f8bz1y/dlV/soieuPBYQQ6GQfis/n8QZ6pyWQQou6Wp31G0z2'
    'sl1iefPonp00cqB50O68hr0ZmH1No87B9GOgAmUvrU3cJ1VqTqPj+wAIwiFTUTdeXCQHA9WGBjMrJU8zX3DCbR3cdhSj7VOJ/kjZ'
    'SbKzNHXkypOxtE55AANmcpGOC0zvpxZp2YBZSNU6kF2+e1YoAWMA5RHKwqDzumfzcLCG7LbBR4GSkvdiaUxGngNBUPwW3NfXLaQS'
    'ypkKaS7COB3m4k5odID0S7nTIGwAcjhEFBkQcKDOCrhqMncdUxhk9baMk5Eq2XDFdB1tPnfDfYzweVDl2ig6QWzGXITAMRnZjuVg'
    'ilsQDSotQbJxd69kTrFQqWd9J6ZhRRFqbAMrb4pR4+gCLDbZBMtMccZQbOAX6l+/d+EUy9WUHQixdOd0gH49b3kJJLGAZaUViSci'
    'J8U5f4avI8iqkMvIgzT2/is8A0esapYFjc9IE5ms2g5SGChGoV/dhPGN03UTYHcjsq2UwlsrQam+k1D6wL5Ws/pG4VuW8cRL00by'
    '21mEjfKGXy5MbX+/sB+c15MU5IRRO7ANbYguALp8Pm9FZjpkmKLKQ8G5ssG7Aap+5jSTAH8eq8dt2/Utv1XwtSY3hHLEALTBWWDR'
    'iRskyy7iPENRl8ThTQ0tYoQ5XDyUHhfBFqhXC6S8ARoE5PYWmyjASQ7GBfLVkIcebG347gAlxBy2z+77+ur6q+akQWAZA7ZXoog5'
    '+iKpCpBtucYYhRU/RDvjQA+IcrZgSHztHxsYWZUk9ttpnm0qx3RPaQ0r58/261AEzyVjcfJeUhkTjW49/JvnsIXIcJjqMR3Cxazd'
    'x/sDMtag+EgPm83LhNlClgEuxjNyLmOjdS6cI6jveuVYs42X8p2sBoy+BnLSFzllAlyoJN+cSZjXR51BgQE4HMNr6gOKMu5eNVYT'
    'uKune2ioj6jv25SwKGoU3/OsQz2MODdUDcz5Wb1MlZzcPlzfHxyhrebz2UZkWT8LRS5AAA85inNH8PAOYusHaV6dCMaFB595iGxE'
    '95lYDAZ8xnfSBa1cnRnmvPvY9CvQp07EmeXrGN5CEnaGPFkqvADRjIghJtGbD7EWQuozUsgRZWwyAAAzI04EE/lUnt+aofxQdFiu'
    'lBq2cE5D8f2UdIFKNWTBOFQ5ANjztNPi4DLgI0oQllm/hUmTsOQu/4+EEZ1mRgHwexTOy0765oBeqtYmOzlNJlsx8qIPLSyZX9x3'
    'LiMsKxmIOTOQalLDfsoWANZDMH2Rl6OLxZBwrFMP2RrsDvX+sMzFwWafNi4vQAYfqS+02RWzQzCDb7XYDkPrAEVGtgMl8xGQo0K0'
    'Df6UahCSH3Q86JPqiEUWkYLSuXmr+ngqJGjyqyPjA0CRKj7oFzidltcloE9tjfK7juGVjXCN2J2DQyNsoSZ2Npsjdjar7WaGm6rp'
    '/JiMtytRiIavtY10mEk2aubhY47vTjcwqFXc6fIQDDmwGrhd+XwWLiIdFgyRT6pDiIKKZ4DWRaSOcD10m1AvCC7y7l1V3SGGczYd'
    'w1TRKAJMxZMpzHUQypuBYNvNwnG1uXN8IQBOQLk8a8GD2dhnAAijMAAcBoQUw0z3Ym9gDSQsMW3uGpcORdWYvI6qDxejXK3Vnu8o'
    '4NLZjzrPecFNVP9Jl4zQLdI8nzJQRnY7yA2nsSozKjDXnXzePmBRJqRoDeqhGiDpw/98+adQRWkNoTJ9ZyS/Kg+ho7yIVCFAMWkM'
    'cMCpsV1P3/3VtCDbKYoDhVU6LalDQIUNckqe/5V/9fxJos2R7bSHIvH+EjGVr1T9WE/pnA4tQ+xs2Pd9XoI2vl0tN75gN+v4Wl7m'
    '6kX17+2wAjDSzeo5duYxm5VRK8g0KrftsBWfFssdTJsJCAgVKan4vrKW0pLhDyCefOyjj/7UAkIsvfoADydXvPNYKtyonjWhEE0F'
    'igl9liZ0ZJnRtBqah6u82/gRZf4qBhhGiNcrVYUiPWQxbf5SlhlBiaY8bn1rnJJeLuJOv/d4tNGRM/4XKOML9FAnOz2iLlOSLfvf'
    'ZY4Y+zwqFGuEYitKW7/dukiaSRgNtNPdxL2w8K53ZePB0JlZHCrHAraj/6VYNi0WqbSwrG4cVNlaHJ70idAtp2d+rNHqjbd8pzfH'
    'e3MBx8OEFxkCNIJqDn935QYbP/QVVzIj4l90U6cRADyuoMAE5TcxoRHOflTQBNquv9seG3ZjcWal4a3q3fdcc1dVGVhrbLd9aq46'
    '9LAt+uduKCaQxCMrDHG/MwXQz6TuMSNShuiwqaYw3XmdLN1z079UWaG3k73EhoPmC6ALMtz1vNuOdCkysoRCcYwyxi52oGoEgAXB'
    'FZPLQWbMtA5a5DKA6AIBCcxR+JD701meQFqPAs4lWoIq/ZBCDHspbnsNMEcHEyEJpBFlG1XWxRuiKf4u4gzhejY6HI6xymQSLMo0'
    'U9wQO8uBu2ZOcMZklxE8ZeI4Pthi1b2mhvwFCXnHlEJQXHOvaPCHELqbbgpJMqdB9yRROhlj6Cd5DJQfnaB20uTvXzpQLxHPf478'
    'nB0s9PJKOyNC8vNQPEILpDSCtvhu7n5EYLb2iFhQqgnUJI0Rw2VeyBo7wnaIKIkIRzdHD0TkTOFASWIV5up+SPJsQ7fwiHoeQmqp'
    'KmnZjI0OcRmZVuDOAZum7WiIYyEuc3bcX2zUf+SZJ7BEAW55ui8hS+6GYFH+TSpFVXyPLA8+x/LunDG+WgCPClQKOv4fhkL4znWA'
    'KstJ1cC0QYJIGNb/8Z0woEfFUaknhVRsJieR7fRVjfS5LkA/FKeEOYaQ/cGm4Vc5ZxoBBUiewECEUE5tUCRFNg16wd9BXVl+iZ8w'
    'x+Ov5btDcmUzRzQVYjA7Ab5AeFDFZMuzI8J0vNIIg4rBWGIkh0O4dOrmxo+RjSmFYGG6Jk5ackaxmJtxgu5kfYQXHFOJANEjVm6t'
    'nR8UMQ+GOM6+fORgg02hCiwvE/Xjw+Y3NsQjnec6m+rlGt+EkGDpoGayn166qVaqB9dx9c2D2SbYS8gfcg+QjE/Mu+5uTne5KFKt'
    'I16GNYqkZ3NCNwyghYAnyPOQZGmn6kNCLbUiuzIGBUh1s4MmBSxYWhfIvZVsOgjv1TeGdkD0Irj0wE627QhMbiv7KZb4QQT3nmjY'
    'yCZ3RYxxKQU/CgB4YSLNg8XqxEydhELDfeBjZMMN82gEXrTNF67uQbEptcDGh4dUpzcUi8qGO5xKzvNSxKWLdLy/pdtKwl6WZ3oJ'
    '0svI1fu3FLg6llCW36sDcwNx/LlqYGqifm/JERUpgft7wHFER5A9aCpyY6cvHEJmwg+h5BFMxcHaxdGs1OTo968eUT+Hax/HeS9s'
    '4zmSsSYa/623kPNFjPNkjfBaMzaWC5XBG51TiJ+wfrQeEsvGT/ArTpezmIspG8/phVRsgRKKY4rjJRPuInAQTN0eB+hvPEzQ4CSP'
    'kUdnH+w9afFZJcMoVRwSAlDguFyMhypZQiT7nns4mmjJH7ARlTuYIRDTkvi5iiPNMPDr4QLFgv7W8/EJRMhYlrqLk8Luje5UIeFb'
    'ziwk0juuw0UUViao2ovtRoVMjt5f7F1mW6AxpBmizVWAAlEsKUynjrnU3ODDe0I5FYI23NwVHB24BB3WK4HKL6yWK18t9+A7fyNq'
    'aDZmNUHfQsltxK7feYSZiC94QxFFjqHdjhwnOYpiNXBp9vbRxRpvJRuP/xlq+1HpEvhBv1CPMgio7sRXQHveQtUzCahs4zouvjHy'
    '/n7aZn5JYafp18cycm/CvKgz8nKzg4A49COj2A7joo6pk57+zVDJR1vDvJgh29G5JkPgxdXWlOo7qjRcQETkGCbJWevUWrgUCBOL'
    'hBQThdX84icqKJ6sMCOpdRQkrk9M7Mec4r5t+OSHnmSx7g0wj3oFSI/jcNKIiRseGfgge0/1U+yq0mGhGaAfVJcodkndJDCGycqC'
    'fsjwKmUAcRib80WhczlbdeNE5uPWzfh8GgSA6HWeq/9xa+tjDdczcNYYwOSQM9AjRbTHLssGEjGaNnAaPA7URjko6juekxVUCIcr'
    '4zgi1yDjZSZTGeC/ULaOY4FPvjiwn2xybbxnupVOuVorxUZ21EFJubqy5az1zM6QkTi+sQjgIMlE+tqfTdBX5R4uu3Shh8OSOLv1'
    'YTpjbhV5SpuHzJU7ELvntBSU+0mmjxGZxj+8cD6UqHNCIqbxikRPQNG01Dol0ROqWzaW+EnhI4j0i1EgGUh+KTXIcj3Ls8zIo5i5'
    'ynKaDB1gFpX9sDIIID5GcnP3/7j/P3KxwzU='
    )
)))


USE_WEED = 1
# Measured OFF: the stationary idle layer lost 0-12-0 (margin -519) to the same
# agent with it disabled.  rayk's +258 on a different host does not transfer to
# this route - the extra output depresses our own premium prices.
USE_IDLE = 1
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
    """Best stationary op for an idle unit, ranked by what the turn is worth.

    CARE banks +1 product on the next production (milk 193 / wool 241); WATER
    adds +1 yield unit in a one-time crop's bonus window.  HARVEST and
    COLLECT_FERTILIZER are deliberately NOT here: they load produce into a unit
    inventory the tape may never DROP, orphaning the goods and desyncing the
    scripted HARVEST that expects to find the tile still loaded.  Measured on
    the four reproduced ladder losses: this ordering +205, the old
    fertilizer-first ordering -3,829.
    """
    if tile.get("animal"):
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


# --------------------------------------------------------------------------
# sell-schedule smoothing
# --------------------------------------------------------------------------
# Settlement is a per-unit lockstep loop: unit k of a SELL is priced against an
# inventory already raised by units 1..k-1, so a bunched sale walks its own
# price down.  Between turns the shops (every 4 steps) and the town centre
# (every 12) drain that inventory back.  Same goods spread over more turns
# therefore realise a higher average price.
#
# So: pull a future sell forward into a spare slot whenever the shed verifiably
# already holds the goods.  Advance, never defer -- this tape spends its cash to
# the bone, so delaying revenue starves the next purchase (measured -35,572),
# while arriving early is free.
#
# CAP is an interior optimum, not a "more is better" knob: cap 5 window 8 gives
# -271 against the mirror where cap 10 window 24 gives -1,920, WORSE than doing
# nothing, because pulling everything forward simply re-bunches it earlier.
#
# The rule reads no price, no base, no amplitude and no opponent -- only the
# pending sell queue and turn occupancy -- so it holds in any regime where price
# decreases in inventory and drain is positive.
# SMOOTH_START is the load-bearing knob, and it is a ROBUSTNESS knob, not a
# performance one.  Smoothing from step 0 scores best at baseline (+3,245 vs
# +3,080) but detonates under a 40% premium haircut: -28,327 against -8,037.
# Advancing a sale moves when cash lands, which changes which Fibonacci-priced
# HIREs clear; with fat revenue that is harmless, with thin revenue it cascades
# through the whole labour schedule.  The cliff is sharp and it is located: step
# 168 is the tape's biggest capital turn (BUY_LAND + 3x HIRE + BUY_ANIMAL COW 2
# + BUY_SEED STRAWBERRY 19).  Smoothing across it can starve BUY_LAND, and the
# farm never gets the plot.  Measured in premium_bear: start 100 -> -28,327,
# start 200 -> -9,778, start 250 -> -7,492.  250 clears the land purchase with
# room, and costs nothing at baseline (+3,252 vs +3,245 ungated) because the
# bisection already showed the value is late anyway -- steps 568-718 carried
# +1,073 of the +1,258, everything earlier carried +154.
USE_SMOOTH = 1
SMOOTH_START = 250
SMOOTH_CAP = 5
SMOOTH_WINDOW = 8
SMOOTH_FLUSH = 8            # last turns: dump everything, unsold goods score 0
_SMOOTH_STATE = {0: {}, 1: {}}


def _tape_sells(step):
    if not 0 <= step < len(_ACTIONS):
        return []
    return [list(o) for o in (_ACTIONS[step].get("market") or [])
            if o and o[0] == "SELL" and len(o) >= 3]


def _smooth_sells(obs, action):
    if not USE_SMOOTH:
        return action
    try:
        seat = _seat(obs)
        step = int(_get(obs, "step", 0) or 0)
        state = _SMOOTH_STATE[seat]
        if step <= 0 or step < state.get("last", -1):
            state.clear()
            state.update({"last": step, "taken": set()})
        state["last"] = step

        orders = [list(o) for o in (action.get("market") or [])]
        sells = [o for o in orders if o and o[0] == "SELL" and len(o) >= 3]
        others = [o for o in orders if not (o and o[0] == "SELL")]

        # a sell already pulled forward must not fire again at its own step
        for key in list(state["taken"]):
            pulled_step, item, quantity = key
            if pulled_step != step:
                continue
            for i, order in enumerate(sells):
                if order[1] == item and int(order[2]) == quantity:
                    sells.pop(i)
                    state["taken"].discard(key)
                    break

        if step < SMOOTH_START:
            return action

        if step >= len(_ACTIONS) - SMOOTH_FLUSH:
            action["market"] = (sells + others)[:10]
            return action

        # the observation's shed predates this turn's DROP, so it is a
        # conservative floor -- we never advance a sale of goods we lack.
        shed = {k: max(0, int(v or 0)) for k, v in
                dict(_get(_get(obs, "private", {}) or {}, "shed", {}) or {}).items()}
        for order in sells:
            shed[order[1]] = shed.get(order[1], 0) - int(order[2])
        free = 10 - len(sells) - len(others)
        slack = SMOOTH_CAP - len(sells)
        for ahead in range(step + 1, step + 1 + SMOOTH_WINDOW):
            if free <= 0 or slack <= 0:
                break
            for order in _tape_sells(ahead):
                key = (ahead, order[1], int(order[2]))
                if key in state["taken"] or shed.get(order[1], 0) < int(order[2]):
                    continue
                sells.append(order)
                shed[order[1]] -= int(order[2])
                state["taken"].add(key)
                free -= 1
                slack -= 1
                if free <= 0 or slack <= 0:
                    break
        action["market"] = (sells + others)[:10]
    except Exception:
        pass
    return action


# --------------------------------------------------------------------------
# per-item sell volume cap
# --------------------------------------------------------------------------
# Realised revenue per unit, measured live against the strongest rival:
#
#     STRAWBERRY   us 292 @ $108.4      him 286 @ $139.5
#     MILK         us 213 @ $176.6      him 287 @ $184.2
#     MELON        us 144 @ $142.7      him 138 @ $158.5
#
# Strawberry is the SAME volume at 22% worse price -- -$9,081 of pure execution
# loss with no production difference at all.
#
# Cause is order SIZE.  Strawberry moves $119 per 100 units (price $120, so a
# hundred units nearly floors it) and settlement is per-unit lockstep, so the
# tape's 22-unit block at step 648 walks its own price down the whole way while
# exogenous drain only clears about one unit per step.
#
# Splitting INSIDE a turn is provably useless -- every unit is priced off the
# same running inventory -- so the split must be across turns, letting drain
# refill between pieces.
#
# Only the illiquid premium goods are capped.  WHEAT moves $4 per 100 units and
# needs no help; capping it measured no different from not capping it.
USE_SPLIT = 1
SPLIT_CAP = 4
SPLIT_ITEMS = ("STRAWBERRY", "MILK", "WOOL", "MELON")
_SPLIT_STATE = {0: {}, 1: {}}


def _split_sells(obs, action):
    if not USE_SPLIT:
        return action
    try:
        seat = _seat(obs)
        step = int(_get(obs, "step", 0) or 0)
        state = _SPLIT_STATE[seat]
        if step <= 0 or step < state.get("last", -1):
            state.clear()
        state["last"] = step
        queue = state.setdefault("queue", [])
        if step < SMOOTH_START:
            return action

        orders = [list(o) for o in (action.get("market") or [])]
        sells = [o for o in orders if o and o[0] == "SELL" and len(o) >= 3]
        others = [o for o in orders if not (o and o[0] == "SELL")]

        # endgame: dump the queue, goods unsold at 719 are worth nothing
        if step >= len(_ACTIONS) - SMOOTH_FLUSH:
            state["queue"] = []
            merged = {}
            for order in queue + sells:
                merged[order[1]] = merged.get(order[1], 0) + int(order[2])
            action["market"] = ([["SELL", k, v] for k, v in merged.items()]
                                + others)[:10]
            return action

        # No shed gate here.  Unlike the ADVANCE path this only re-times orders
        # the tape already scheduled, so the goods exist; and the observation's
        # shed predates this turn's DROP, so gating on it stalls every sale.
        room_slots = max(0, 10 - len(others))
        emit, sent, leftover = [], {}, []
        for order in queue + sells:
            item, want = order[1], int(order[2])
            if item not in SPLIT_ITEMS:
                emit.append(order)
                continue
            take = min(want, max(0, SPLIT_CAP - sent.get(item, 0)))
            if take > 0 and len(emit) < room_slots:
                emit.append(["SELL", item, take])
                sent[item] = sent.get(item, 0) + take
            else:
                take = 0
            if want - take > 0:
                leftover.append(["SELL", item, want - take])
        state["queue"] = leftover[:60]
        action["market"] = (emit + others)[:10]
    except Exception:
        pass
    return action


def agent(obs):
    try:
        step = min(max(0, int(_get(obs, "step", 0) or 0)), len(_ACTIONS) - 1)
        action = _aligned(_ACTIONS[step], obs)
        action = _weed_repair(obs, action, step)
        action = _fix_animal_species(obs, action)
        action = _idle_fill(obs, action)
        action = _impact_slots(obs, action)
        action = _terminal_liquidation(obs, _aligned(action, obs))
        return _split_sells(obs, _smooth_sells(obs, action))
    except Exception:
        return {
            "farmer": ["PASS"],
            "hands": [["PASS"] for _ in (_get(_farm(obs), "hands", []) or [])],
            "market": [],
        }
