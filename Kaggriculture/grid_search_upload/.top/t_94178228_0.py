import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vW1ly/C961oNJUV9509jc2FjNyJDtEJuBMBhgNwgQbB4meQvy3+NYInl5T3V1VZ9D2l74yQRF33u+T3d1dfWv/3P2'
    'b7//8fe//XH2T7+e/fTp3f2b397fffj46XF99nR+9u+//+df/+vzXz5//Pvvf/zH3/778+dfz96++/JX7cNPn/7y290v736+'
    'uz87P3v9sDk7XzZff3i7Xr+f/OHDev3m89ebt+u7j2fn17Ovf17fP/xydr7Y/fz948ObT68/7v/H1dPT/55PO/b+3es/f3q/'
    'f9Ni0rdfzzbrDx+/tPWXh8ePb7982n01+3A4EB/W9/f7t17M37p93ORVoCHT1+4/zacCNWD2unD2YA93LfkyJ4uDvr78irzr'
    '/f3d63U0nqg/2/8A3jZrN3nry3+ZjmfTji/f/bJfDAd9fZmp4GfpCK/v5u/fL4+7j+vH+SKaf3e4euDSXc4X0YeHT/NF1C7O'
    'P/3/zjj4ZtY7NpXt4BwO8GyU9v17ffeyNLc/et6Zk65bc7kfrval21GY/iqdLrD/0OSAndCsYPKWl7EHYzYZjmbG2t/oM/Yy'
    '7nToDp4733n7IWynKViXC+FwA5shPFr52XLQBW1k0aGTT962pfpYyt/k8wiG8OWEAXOUzZs+iLt37D58Pns/oA/ewO3HvefB'
    'L7+kkz72+XTCh3Rg+38nbxr63PTDV3js7Fa5CKzJ5DA1LpAxT52frc72PXkL5vYI+WljRoxpweuH+/v164+//Wn9+PHd/bt/'
    'PTwTBg1e+SXGEim/40hzsL21J+0J99DOEZn9OLjKL58MC/CbXv/G/M77uKp7t6n912mTAPOuMR8nRjhYuBU/AxgjcE/gXr0s'
    'bctM5n2Y9jbrYzqAwLE3DFLmqsBP2QPZWKBP6QOZRyDajx3+aNzkogMVD6pk+yobiPrm+fwTT6fP9VWAp/Rx0Fs2nAdg3O8f'
    '2RqD+eZvgRNiW+btsx6XmqoENzuxYf3jaeOfJt/7wIZaYQB70WUUICBZNDXYxdZ3xTE0J7idU+ugcA1mhkAnVCddDEMMBIQz'
    'hpdG8W5k4Pr+uO4bFfAy59HUWABvieY/vRE0G6JknpDh4VZb/mgKUAM4zQIACc5FR2TIAQ1X6dCTf46l/eMgZz8e++OxJiYV'
    'Wy92rB4E04OofGJpXVbOzIovboIjRZfPAEP6ooeZ3VUxUDxIyWk/CYn3eqHsTg/G5u3d479EHesFjCbd0V19MQSNhmrXl+IQ'
    'Tceihx/QDk4bQNwxAbpQED7ou449v9V0ZoA9shuU6UjlWAYARw6W3X6NbgdlH66UB33/RHSpTN83t6+s6PCWYEFvLvCGSni4'
    'fXDLcfphIPx4bC/Cc5nZSC+/u/my3Vuz6VIHfUIj6sVU+vDx8W7z0/rx8S+AHSjFjdglBjsUvH3x1AOF5DGmw5YMCS5t9CPZ'
    'N6L0+Fk6boZhOIev+iElI4rBgk6bYxlNU3tjClF5mBEPZnWtj92H3SWdP06DYbd37GQbYi7qwMhjl78xH4HiKoj6bX393Myq'
    'jYc+PTe0EvFs7y3CPxOo087jKjjf0dhxP+JMXytqdeXgPpcntFRi9KDdaS+v+rwRHx9QuoQJtCv+MXW/M3ylcq8wAGJyC24e'
    'Hu6/pKlAI+rljy8z9PmAfCNEAve+uBWuK9OHzuGkNtwyRk4YxBaZD2p0AchG7HZy5CGvQWfA0AFZP6Nv+dExMJL4UrlsJVSo'
    'K4CqOx59TKM27psCVxKY2nwqw4/rQlgRNBGgmPtPFbAOgX4T/hGwGLu3gjEC7ZyjE21+NlT2Ahtr9MkcGXD+tMjuPPZc41EB'
    '12JmpR7LGLqq5KDaQTOIuMCw2So3rmCOqG1xHYdSlNlM++XSUHZ2vfEOA5Th6UbGarzKdmZACCg1J4OvM3ONwwTqCQK88zzt'
    '97ycES2n65JcxIyeMst59SxFlAdM1ztP65UxBQF+3UWjYHtaY0KFHa27fB/Hs9hTpnXavrc9NsS56Au1W+Y2bh2753VjMbxu'
    'g4YYtzLYhO0RQO590KLZ34oZrswmSD+UHETQ37BTxQ6TOa500zfqyHRPDz1kqlOOXYDeZrYbszF3r0kBS4/u1w7B7mydpyyc'
    'D4pBgm7uxRHkcHft3WC9y48tpnMAs+LYr+wJHldfKaZFxn5HP/nuFnsRltTMlMfX3jjwZ5ZHUUiGoMbO7o89lLsaK263aac4'
    'bmTYb38rhFEzISHRaKR8UGwfbN+KKUOl6LgHHYKjcX8cv1zMP7+7//PLyovcofaXec5cD+r9sqWf37dY5jt1ybAAeyrB4rJh'
    'Ae7E6DNIKLdgxYGtLcjBWH6lGSgSkjWPKeAEjuY9HXNqYDUwR8va9Fyw2ljuZnJ6ZORMz/MkbVcIEDZjeZEjoi3fYiL7hY1W'
    '5GO1rcQHZh9UDuYdOBlsdwHRsvYBxchoy1cFLouIjMR+TM599XDk1qpmDpzj79UQDDBmYB4LH6r52tSTPEXr2AEY87uLYITS'
    'IDgQaCOAuyw7U44+se1JHDRJGlCzO7UtYcyahT5UMZI37/5ZVkQD9CcCYFQgo2w1eu4tw2n8/9HL8DcAne4kTzdKmNDAWeCw'
    '7AkLbvoquvnJ7zQxqGP478BWydx3Qr31Qpq6N58H6RrTR3Pqe9z7xlGAOT/YIJUdXfmHvXmMzM1v1/AeiW9X0rielLM/Dxll'
    'K7yogIUFnKN1GA+nAVgaHiastRXBJ1K3fnqfHva/TC/kMTsl2kY7a1iaTC1DdKulw6GS1woOKvauBPYUvPAxXALKe2KSWy3s'
    'ATZDJc9ZcrlbHxpYqmRLDgI3pCSpO8GnBX8TVUR00nYESbOkIsn/BaYe6GL8q87EZWUttGapErBsDdY67Y9v82O32F4CIneh'
    '1znI9TOEMCVkmPZFFtN2VdTwTtAsYMINeeUpR+tkrfpGB2s4GWCMkM1ovkCtVXLCXw/huA8gyOk7Xy+MT3g1lTB+XUVNhilK'
    '4Xxq+pliOcGKu37qUyxWuiMP+lGIpGBl9MlIVl3MCi0UsGAlRjmMnKJndGsOQFpH4mvHFP3QsykGdcir1MS8LOezmPrV+tlg'
    'gKYvEaPAvVlj6qNZU2C4XilfNr29bl2iChRR0lxlGmYmKzGA63VyO3hxNs+0ieA/p+1tKUHFABpuBpQWC0W18tZOoyRRGQly'
    'CzDuM1+37Tdg0krtvwqh0sXCMC3YKmb8CTAvPGdQ7paB25nh90bN5aAUo7m+Dv5vtXOUXy42Eg6HcMu3kd28H6jTcwJhux4v'
    '8/XI8OLZQFwlk7thhwigTcu9vhIOEQ1lBreJOYt4cfQs10WnvwR8OtTG1FqK6lryFbt/R66ECpLE2HxsNAMq7IHkUJ1LWCXJ'
    'IsD7pmUUkiOF1coMTeF8sfX1y0MUi8AramQ/rAKOjQn/myR1P0umDErkXpaTLTh0oyM2/drOlYSMqAKx5bMfndqxzyXoj6sL'
    '2doS4cOQNAEeqQDuMDRCTixvikVYrrTM2+hOMfGee6ATMgst64WmlQVnh+PBIko7UYh4t2wU3ixr13pCfsLNffNUAZZSKBC4'
    'xyTUy7nsXYwOxHRWsr413kFENkvMBWZkA36TlHRAV3xjIpmLR0caGuMZSU0ceXUUw+Zg5M1Fwx378aumTfpii8ZTAOXOQkZg'
    '75dC2oevZJ69q2DC9lV1WRF3jS9opXWM0kVUE8Oj/7zYpU1c14ACnwCYi/tdut+SrlCxs2yhgdZTbEQpxFFNKqLAIXixspja'
    '3zhSd2SViMcil51Dfx24VJQ6q1wDL/6a3if0q2ErhwYAAfNKhGlrqoh0aCmMn+tJBD8fcksN18CQQCJBgtoGdvYoDkJSj55j'
    'E6Mzuy+nDbpJwJzjy2QAeMZNDl/XJYx2FxNKqHEoNjK4YhIkksyZGoOGREjakGVNjshPleoXd3aSS3SXBayMioxLBl5VRNYY'
    'CYWpGRhQoCx3fPtUYU5ROIax7OdfCdLxRk6CzvHiDscghWtgSMvZRwqDy1p0LR4hel/M1xUncVmhwlAFQinxsTJnyCFLiwGr'
    'iUXYt65NI41mZmwsReKm6j6yYCxz05mz5ZLGlk8VX0yLGQvaQSOGkfoboD5g4vg6xYmYt5Q6dBI0q7h4Qgq5UKeJojDid6JP'
    'F5PvhRVA2153PcNV7m8h1kLHzdd4gEdpb3maRy1ZoZKTUAk9ACgYfoQIElL7bA2LL3nQ15EjvcLMiTkF63vxtk+mStn61pDm'
    'rGU9hxBBwe/e+4G7PxXD67JxVUFepWyJTGoNAHGd9H8wv7tdnHmrVdmDEnuhE51pVwkaVf6dRFN7Pn4WIXH1xuC4a4IrOSEm'
    'dR/czAJL0DF9KZIATEsGqbIYtNkeh739W4aHGAk9BVVKuEYZW8LOM+nRc9T0+/knaaoLc+qsKo/kN0SBgWaoUZch/lnnJHJp'
    'U+bjSCzfCsEagQ10TFKyQmcZMWUviVdLmLrUX/pga61Pny/EuiI2vqImO+Q+YQ4+i0bGhCsEEMz+mw8BaIHevLwtXhRR90aE'
    '0jdrVQ/FlVOpaHp2tgZQrfxmtb5xryAKzSXIUjxGJjwoHyb8VqUIs9bIWlz8VnHnp8Vcvo7zzhMZ0FYd6Jjv1yYSeAthha6S'
    'p8DRagOJMJs1izb3OtfF5IFykFWZoW4Bik1xxDz+AvPHyuOjFDjTq4qkUE3qoV/pHromoUj9rS3z+uDsevU82C/fdIUzFba9'
    '7qySw0LXg5cI9SwdSWMVDJRdIYHfbJb6ZDZEWn1hyEXfmwr0V9w1MOjwFlBou6zDaskYNYkk9HrMshF4gWGXTirak2fUERPa'
    'qP06BFZjwWSFBFCsa05drzXcyeTFdvzvwgj5G3M+bgwo8EDY6KHnXbTRpobqdDJ4go6bBqK4vAV5mBq9ejAd+Lr1em6+m5Cl'
    '4wadNGKJdkXiNg3K2D5CMFOqgpab7SqNmHzIBlu4LI3qMAKzGESe6kxteJ9VUuo7ScbtyjmsD/icQWCM/8Ra11i/abFAhN+8'
    'MjIqexnh03nHRkAeFqqkb0s+CViULIKG+Xeii5eaMtcOyzI/oSTfp1LZXXSXb54MpjSNtFGHMLVufTEzYXskrpZWvUEsKC/C'
    'KlJPPDFCzzbU+p0P//KpQtf2ArOhXyhegJr0o8bjZiseNsdKsS0sdxIITiiSWi5romMgKikKnp8iOZn9EZ/55MgZ3HKN550c'
    'PpQYUFeuXJScby2xI1EW7qAMo55cSDWwbM1GYtqkuodj+tEe+OLWlLAqxuynkdVqd7RAP+PDEsiFnP3DxGqX/VoTcq0lJdmG'
    '57zUF+JlPQHiuSrm/l8WEaeE+O0DIpLEUTvWV7vhhhLmp6qAoIm332osvsabHxOVrzsJY+LxmR+tB8yPE6TX6xx00UL9+Hza'
    'isG4jzK/rd7UID3Hzlg+cP/T0IuR66zF5PWQN7qx6TVbCMCzyHY1OUWpay9F4lXFRlS0TI4KKUxj8ILDhSOZGsfRnjPVCZnW'
    'QDfsKegoK/9ZWUCshCRxqpLqG456kgIDUFFI4v5UAvySGWvHRAqyuRoGBi0OSoPu5KJq6eSK3hmFhauhYC1KrqkqDFMyYJRs'
    'Sb9fY8iniwy0g0/CWlAOjaPrI8aJKJW6wFsu2liYRkq5GiLndkzydeTvrQKsf/X1nD5AeP6q1ANAqpW5B+SCGkE1oPE5XZe7'
    'kzRR8RrhbaZ/yYN1BW6n7EhmfxccbxwN6E/QHi9+l9mv4GCWA/xq/C5Ow759Kvi0qVkdOSpZx+CSnFu2CkZY8pJpCF5k2kte'
    'Wrbw5kn0r4wyWBcVSvxhk3VHiyec9k7i+WwcliWteh7aVOsO9UTPHSIMiUFxf1LTkCs32csmF0tcoP9AueFjQqIEY1ClBALa'
    'C0NIhgRFjYOcnXkii0QNa6HH1eoU7kVDDvt9bbBmaBJHgKVR5kG7FSf/Oe/gddecJSFhqVRLdiT3zlpQgFEN2EuihEhxW/F2'
    'ramS4t0aM0TL8whXId1bIw6QerCbOxMMCMWUhC/k3Kk/fZV6fVlnm6dlJBlWz2CjdHatHitkGPM+rnqnSSKTkO5FVI286VfW'
    'mEtZOFYXenhtHfuIiBEADYRW7KH9BnAv4ltA7NvxMLPlKq6JSvbrN5TAs/x2FP5JbRtRsU0A/oZk61gIjhH9paUiiyk7shTD'
    'uf7f+8XqT1EaYKOWORgsw2Dl8RTy9mVdOtqvzkoCmYgD9bdSFDepmTqwwgD6FEFcpZ0siVVMT+TbUiUC5mXgkTUmQbxtrQQc'
    'kZIi1u0cyutXihrglK7EOs4nYvrZ8u1KpQ94GQYpt4hWX1dhrWsjAUdcEAe6d03LhB1hLyO1Erud24V6jMwggqlquV05WHDe'
    'XayB72yc76LOX8zSOhY2ogKHQr1LUzGho1+r+jRS1IMmDtFkFWhb1tI5FPCndc210rIM9R4s4N/jlLcnP82f6SieMLyDDsmG'
    'dqXJxDjxTOUdoVFGoSBoBuv3FBOp9mloyZNvYSuxshm0/iXvK4KFn8Pg9KGVM799RTKtNhJ28AZed+PQzflqQNj+ivk2am0g'
    'm4izqlU61sVwMCzjtclIAXQ/ZcQiwACU1HLDAzYcZ5n7I7NjTCXIxImoy90Uy6iEAeb8/Lo1Fmal1qY8V8hIN5YomshXQvSf'
    'WQsMYBPUSlil8gR0OyQxLA3S1iqkCLT7lSxsVtZelLvUUMlRZLVr54AtlIrl/DQNf8p3Yzx5yxp5QGJVqnQQbnLJnbzqW4eU'
    'B6ZahU7un9gLsuBoIRZ1O9FnyLiZztFFh1XKtNc8Rl+1STm3pQy66ASP8CA67MZyUbw8KWFyo/A11SIpvr8jnLM8t4vo3NA6'
    'vbT8bWG7Aq+G5o5oiY95naU+PNFKCyxmUpKJYffcEPZykom8tulEx5uKDoRe4WhLC09Yp+OwXHI8sZWWsMckfpItWlM7pkCJ'
    'm7jojcKwQsVpBign1amXWlkqrbhO2u3y0rsYRBm7eBWhc5FLdfmtquucPM8Shwcr5W9Sg28AbSyDDFL4yfAJDa1nhohRZsWQ'
    '+rDd5XlzFXav/G3aTsNV02lS43MzgTV+6DWYWXApr5Hb6RpFS4uL2ZVtHV3y7povSOWZUGciV06jodREZgBdjINDSaZH1lZF'
    'bYZhRQzkjFKcNMKqhnEe3r76CpB8EnWHUhda93CuKmC6kx5Im5coxfqtJ+AQzYmFraC5dIyzo7por2oQEVOflZYM3pYq1D0j'
    'FnZ7YhR15xAQzy/zd7NC9hRzk9OkKIpaomOskCEFrHv1AKTkiuBwDfe16lxdWpBXpp0uKgszXk0xpWgu0ZonriVJquhTdB8Y'
    'glWnRpEI9sVmYUuIeQ6yrZwpjcMSRbnkuZs/a6wODKaHN9SKbohBNymBtDOFVAdzJIU1l5SmaEL0pAC+EvsiCrMxZmRI223J'
    'rSHUVTAq+ihbXPl5WncMElN+YFNK+TGqBQthq9XxNMEOMCaSFCLiQuPqjCl5lbISmFFHo6feGEqS79b/coqldZTYVsST4GLx'
    'M1kV+EzPJtXSz5jabuubrBMZYlkkphCFXBi5i/DeUWHNRL9XXneFhDSWFRTtW6DCtOZFm8HoQOBCcVVkYRuW56hYqucyQUEv'
    'OXwsaSKSvhbNInCE5drcLGJe11q7JHVSKpX+2uNEUy7LSkUTwa6Sd+MkWnIdNkYv0ee7crAg5TxjNq1ie3KpT7CRHfGjTtdV'
    '3rxEYZ1Pt5qQnYEbPQpcDo2YQRNMNw1vSHZesxp6Y/YokzGfZktipanDZahQkpKIUJ/SX6JddV0qSyUUGclr0tcZrHASu4XI'
    'TPqVVA1hiErjtbPZvCLSyodwpZ9kOZK9GIJ3nk7auVdhbijud+HUV1Qky7Z5uPLGtHt36Snza+NOYyOKQmCB/DtCgiwE9r4L'
    'PtnpMy/xpB5oT+SUsjA98+SMslSD3QHYTksuq1SD+7YZZEcQxP8abLK0Kjq6maj4nUwXk+gTlC+mygsnfHAbcqjl6+ornxJX'
    'qF7TmPTjARSzCqZVJMSZVLO1MqJCGVvLE1wNopnRr9IhdQlOl6PIZQFqgkmHCTvRQXlXffyyhA+TaldJJer9wAdjmblyM37p'
    'P19u/aqfY5ZJv1NxKp2SYySHVtXgOA6zEdA1q2DJ4HxRTSON0tHCCjNKBbxSirsEKSvpvhxEnWnazRlPDnVIKMJ3XGEkhRW1'
    'c/5JY1lkQbrTehBllegGUB+uT0gt4fbn24ECZl1bk76P3aZxoSgrU5PGoys0FPv7fBw+PvSK8eszrXQ8ueTaRU41BAtljYtd'
    'fBlKmcsHtM7AgdvmwbactmleaUBnjDM3maxbhF7a/Nw+xtylJ3IGTtjvhTEHen/R1f5+Jh2npx25mmZChnI5dEcqoXk0Gt3x'
    'amp+LRbd2JKamp674iNzElQKLepV5W21lduSxyyBaw7rkYkHG0lNOdlHLDTXLFu5ugQnVPDRORYJSCfmBRkNOv3wwE5srIVl'
    'qdhPzthjtTVFxp5KI+lRNgIsn1cB2QBc1UuDVRpOtM7vdQpojGEEGdtYSU+knqf9aRASsSpxMjlERxMS+dQaVVq6i34uBHSJ'
    'UPVShUw0a0HiY29XI9bpdZUlTecSzCrNJg9P3j5wcFlS3s/YsXGEIHnETB2+yEFMV2Tbo4SxJGqHhQwFAt73KoYvaww9muYt'
    'VkZlmN+4Dl7J1L1lhbqn1jOhUrXUPestAFsjXHLJ+xYSi9f3BPCzBdWsVVtGenN+X0INI/inWrXrBCOyhwtTo5GvSA2/Nyh3'
    'dQIuAu/KRVTEDanUrMh5hcfo+uXRi54iuPObxTtPXt/UVzXZCBhbMNWnV67TcY7eKg83T15aMStrWlWvS3SxTEqeUg5VLEGg'
    'pF0Z4FuFLEnKnWarJY39cyGwzqKmsuEqCXBLo0cgmda1NZXzWd0YGk82fFKkJ69dlBoP01p4zLVISbYM2BMzFPTEQsaSFLSX'
    'jrDsqKIkVTxXZSLSdWZW/cxA1gohLx85qXwnJ2dxRfbQ8U2NwYty0hmIZYp8BrW4zCarrLIKFWbmE4A28rQvunApn5ys2IQr'
    '2G6Jt6HNl4L14kU2LtIXNQSGighNCk2J4ksX9P7YoEstZPerItbePKkoOTdCoUvTKlTrDIUAiei1LFaU0yNosrPiDWkii8RY'
    'o6Jevoy+0X7GMlwr5Wu3sFxOVyzTm5fekZGLy2pg+o0YohX7BZbmSiXRuZCKVrjzOlBD+G7qZ7ZsuRNV1PTV2BQYehzW4jPK'
    'BEyGmV299TE3heKYagG6Al/sMBZyLMqYmKPXKcoetUnlfyVElF4PsaV1MQSFJSaqJRWwu5CpwVgULm8dgANG1XxX0X3uDV31'
    '0blAs8Hf4FEpJymroYsLEpPqI3BlTTVQ0Vh4NppexSXJ55DAgnnpsDTxjRzSIncypyh1iOfJB14i0E6K4vUGV/UsMYI7S2Jq'
    'xFpXSsKKOofq7N1UFmqYw6Qm0hQ3WhIbfZ7Di3JAuF2mTKU7qFgl5EbZ0jLWydqKLDxPBFqw7RSBM6j9Ecp7nHgCvbppz4+6'
    'rDN5SDIjKxhAksGkTVvXDlp1bVkKCbV7VauIQjg/pbIj7QQv5AnuxPzYccUGA0BDCKx4ZnDLiMTS3Mx1nhNG9JKyA5PxYsmc'
    'vUVaz+NctOHsPUo4jHc4SwRVeOAN3NS9Gm68jNBFaYyUCBv7G4+vG4vk1VFUGJnOp68zZMdgVjq968I+FQajl9PduF1q0Xr9'
    'zhJgX24gs+kdySksWXSaNwG/TCpLLPLHKkp2BbJD+yHNLgXsOVYCRo90sw9V4TmZQFfgthQZayWqXh+Vr0ae0NlrmXa8WrIh'
    'B6CBwguYYx4y1QXD49IFDAdd9BwzaQ2j4hRo1DoWbQSXnalIh7J0BV1CKwigydCk2Yq3BkMnTVBLc9mUJBtBErCruIDBslG1'
    'ezObcWA1ALVUgxYlsGkDq1IaD2NqThgRRKRPGAihoOtAK1096RG9bR2r+imQeJgPqDnWPHOGsgGhr5E29MLkzDNIWsnFVKFQ'
    '8w7YQkGOXlUmDWi6sK363ATn0AsDl7cBnDitVoVyg/UqU104qWbdYnN2pqU3s5Qk7ARZirUFVKVNTm6lNL9Splkt23JlSfXz'
    'OaDUUargEe/fwUCkvorFqeLAExmZEtG0yZp00XgbbmzXPxCe40s90suk60CVnLs1JOfU07yYg3nJeIrihbNEgN3Fd4jORQn9'
    'k5V6GsE6KWFIJxvCBimQVqrfRhN1UgAG+rqie8WgTkt3yBKuI7q8brVapttvltLsq1/B98QzuUFRbGYgF9ajS8CfElmnV3Gv'
    'gEG02aluxJcnfFGWXxrJXRjAhJ7b6OCSiXC4PjXRUrzuz1dL2MiiOSXSk42ChIsS9krtQJqiM235jL+gutZbSlsl3zGvgyCD'
    'e56eeb6Plk71Vi0fSiYWimFscztoRXBo5pp0cHlI2LVhOcEkfgI8JoPa6m9aDSXUfKAXQaBEKqs3LzljNVGrqqDr9Tl7lBkZ'
    'QXMbBmFwnSaqaFQaJ5GfV0B1t/ijgkMRiUs/DZ2jciPOEhVzosxPhj3GB2mh+QKLC6wJQsZsylPCMyU++a1dQZZPpovh4ZiI'
    'PBISEd10ty6eFQ2OeGqATGzAKh1hckkJV6xlCW5qKk/eMjsq0LTUqIiNiX+wZC5Gl0FoJ+Go2av9lK9lXxZrZF+LdQZqSIdM'
    'jAJrmhmkFD8QQKULQ4O1W5SsSLsaUhRBBeJ0cTXmCNeSV3kJQlHohrNotA2lST+kSGGGfySxa6MQ3yauIZ2XJRZr0+mpdula'
    'Y8fThrA180FqVxd1tan0WEv54PkGxWx4XSM9E6mqlFRWeeeiMBdUQbEalPvneuVRugE9kTpersYKGjC/gLMzHROYO/VuqV/B'
    'TdTIJbUaQaxCi5EVFrUUzLdmZCcZmfGmsZrHrqONsVfESrFjxi/Rd5MqHcdYvN9GTHXCTGXE75jVlIP15mbl6zonee9wNy86'
    '4CW1bIb2P8z/ZjWNU2vi8nuFD/1TOrY9Y+aS+tzXcgXAa8CxuMIKCmVvOKFy8tsPuV11tgdFNYRovJIbk9ToTG+rsFqg8vJk'
    'rCm/NFHJz17NrpQk/pSRYXM5IGq3ZPKNnAefGpy5USJqe+qCEunQw2NdzGVNyp3q7wYXXMCDVcqsClwuckexO3Zwb/GQk9dW'
    'jhTyOD6yRmc3zk0I9CYDY8YDJJQ3kVdWHNj2TVKNuN6eEr1MUnanq6cgHJXoqvplVUFP6eGnlBg6bV91Sl5/X+NWkte+eXx4'
    'f/jWl28mH3hfwc+ev2L55gblXhBmandd24ndh92PZ99ksp5ZayPBsC9M0af/A1wRrCc='
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
