import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vXEly/C8890H9SdI3jtRrCcsZCpS0jfWAGAzgNQwY68PYN8P/3bLYH++9ioqMyKpuUgud1Gi23qvvyoyMjPz1f67+'
    '7fc//v63P67+6dern758uH/328e7T5+/PG6vnmZX//77f/7rf339y9ePf//9j//4239//fzr1fsP3/6qffjpy19/u/vlw893'
    '91ezq7cPu6vZovj60/vt9uPgD5+223dfv9693959vppdT77+eXv/8MvVbH78+cfHh3df3n4+/Y/N09P/zoYd+/jh7Z+/fDy9'
    'aT7o269Xu+2nz9/a+svD4+f33z4dv5p8GA/Ep+39/emty+lbD48bvAo0ZPja06fpVKAGTF5XnT3Yw2NLvs3JfNTX/a/Iuz7e'
    '373d1sYT9efwH8DbJu0mb93/l+F4Fu349t0vp8Uw6ut+pio/C0d4ezd9/2l53H3ePk4X0fS78eqBS3cxXUSfHr5MF1G5OP/0'
    '/ztj9M2kd2wqy8EZD/BklE79e3u3X5qHHz3vzEHXrbk8DVf50sMoDH8VThfYf2hywE4oVjB5y37swZgNhqOYsfI3+oztx50O'
    '3ei50513GsJymirrci4cbmAzVI9WfraMuqCNLDp04sk7tFQfS/mbeB7BEO5PGDBH0bzpg3h8x/HD17P3E/rgDdxp3FsevP8l'
    'nfS+z6cT3qUDh/87eFPX54YfXuCxk1tlWbEmg8PUuED6PHV6tjrb9+ItmNoj5KeFGdGnBW8f7u+3bz//9qft4+cP9x/+ZXwm'
    'dBq89EuMJZJ+x5nm4HBrD9pT3UNHR2Ty48pVvn4yLMBXvf6N+Z32cZX3bkP7r9EmAeZdYT4OjHCwcDN+BjBG4J7AvdovbctM'
    '5n0Y9jbqYziAwLE3DFLmqsBP0QPZWKBP4QOZRyDajw3+aL3JSQeqPqiS7atsIOqbx/NPPJ0211cBnsLHQW/ZcB6AcX96ZGkM'
    'xpu/BE6IbRm3z3pcaKoS3OzChvWPp/V/mnzvAxtqhQHseZNRgIBk0dRgF1vbFcfQnMrtHFoHiWswMgQaoTrpYuhiICCcsXpp'
    'JO9GBq6fjuu2UQEvcx5NjQXwltr8hzeCZkOkzBMyPNxqix9NAWoAp1kAIMG56Ih0OaDhKu168k+xtH8c5OzHY3881sSk6taL'
    'HasHwfRKVD6wtNaZMzPji5vgSNLlM8CQtuhhZHdlDBQPUnLaT0LirV4ou9MrY/P+7vEvtY61AkaD7uiuvhiCRkN17EtyiIZj'
    '0cIPKAenDCAemQBNKAgf9GPHnt9qOjPAHjkOynCkYiwDgCOjZXdao4dBOYUr5UE/PRFdKsP3Te0rKzp8IFjQmwu8IRMeLh9c'
    'cpx+GAg/HtuK8KwjG2n/u5tv2700m9Y66FM1ovam0qfPj3e7n7aPj38F7EApbsQuMdihytvnTy1QSBxjGrekS3Bppx/JvhGl'
    'x8/CcTMMwyl81Q4pGVEMFnTanctoGtobQ4jKw4x4MKtpfRw/HC/p+HEaDHu4YwfbEHNRO0Yem/yN6QgkV0Gt39bXz83M2njo'
    '03NDMxHP8t4i/DOBOu08LoPznY0d9yPO9FJRq42D+6wvaKnU0YNyp+1f9XUjPj6gdAkTaFf8Y+p+R/hK5l5hAMTgFtw9PNx/'
    'S1OBRtT+j/sZ+npAvhMigSdf3ArXpelDMzipBbeMkRM6sUWmg1q7AGQj9jA58pDnoDNg6ICsn963fO8YGEl8yVy2EirUFEDV'
    'HY82plEZ9w2BKwlMLT6l4cdtIqwImghQzNOnDFiHQL8B/whYjM1bwRiBcs7RiTY9GzJ7gY01+mSODDh/SmR3GnvO8aiAazGx'
    'Us9lDG0yOah20AwiLjBstoqNK5gjaltc56EURTbTabkUlJ1jb7zDAGV4upGxHK+ynBkQAgrNycrXkbnGYQL1BAHeeZz2O0tn'
    'RMvpuiQXMaKnTHJePUsR5QHT9c7TemVMQYBfj9Eo2J7SmFBhR+suP8XxLPaUaZ2W7y2PDXEu2kLtlrmNW8fued1YrF63lYYY'
    'tzLYhOURQO590KLJ35IZrswmCD+kHETQ32qnkh0mc5zppm/UkekeHnrIVKccuwp6G9luzMY8viYELD26XzkEx7N1mrIw6xSD'
    'BN08iSPI4e7cu8F6lx+bTOcAZsW5X9kSPM6+UkyLrPsd7eS7W+xFWFIzQx5feePAn1keRSIZgho7xz+2UO5yrLjjph3iuDXD'
    '/vBbIYwaCQmJRiPlg2L74PBWTBlKRcc96BAcjafjeH8x//zh/s/7lVdzh8pfxjlzLaj3fks/v2++iHfqgmEB9lSCxWXDAtyJ'
    '0WeQUG7BigNbW5CDsfxKM1AkJGueU8AJHM0nOubQwCpgjpK16blgubE8zuTwyIiZnrMgbVcIEBZjuYwR0ZJvMZD9wkYr8rHK'
    'VuIDsw0qB/MOnAy2u4BoWfmAZGS05KsCl0VERup+TMx99XDk0qpmDpzj7+UQDDBmYB4TH7L52tSTvETr2AFY53cnwQilQXAg'
    '0EYAd1l0ppx9YsuTuNIkaUDfffjnbNvIHjCmaeSbWRSxLELy3GVNDw2Qn9iPMohRtBg975bBNNaYdyH4G3hOc46nGyQMWOCb'
    'TgFC309f1a5+8jtNDeocDjwwViL/nXBvvZim7s7HUbrC9tG8+hb/vvAUYNIPtkhlT1f+YWsiI/PzyzXM3Zx+fUkngI5JZSu8'
    'rICRBfyjbRwSD6x+k7q2IiBF6NsPr9XxCKQ5hjxwp4TcaGcNc7NkYmIdbupdS0dEJr0VHFfsXQH6KTjjfSgFlP7ElLc4+tGk'
    'yCL53qUzDSxYsi07oRxSttSd4NyCv4lyIjp7u4ZNs+wiyRHWzOn6rxozmJW1UBqoSuSyNF3z/D++0c/dYnsJiCSGVjchFtIQ'
    '4pWQatoWYgzblZHFu0CzgCnX5ZWXHK2LteqVDlZ3VkAfRZvexIFcq+TMPxlUSLvWMV/n5eL2hEiTidvnZdNkWCIVv6cmnqmO'
    'U1lZ109tEsVKd+RBPwtzFKyMNt3IrDuZ4YEC2qtEIYehUvSMZpEByOMI/Oo6J7/qwSSjOORVaiZelOSZzPUqPWowQMOXiGHf'
    '1jQx9dGsKTA+r9QrGwLDty4zBaomaS4xjSuTlVgB6HU2O3hxNM+0ieA/h+0tOUDJABpuBtQSq6poxa0dxkVqdSPILcDIznzd'
    'lt+ASUu1f1OFRedzw7Rgq5gRJsC88CRBuVsGQmfG2wv5llHtRXN9jf5vtnOUUC42Eg6HcMuXsdy4H6jTU8ZguR7X8XpkyPBk'
    'IDbB5O7YIQJ40nKvN8IhouHJ4DYxZxEvjpblOm/0l4BPh9oYWku1QpZ8xZ7eEUufgqwwNh87zYCq9kByqGYSJknSBvC+KSmE'
    '5EhhxTGrpnC82Nr65SGHSYAVNbIBPqkfGwPCNy0Z/KyS0il3e5HOr+DgzWvJtagVF7a887OTNk5pAj3i5UIqtkTmMPRKgPcp'
    'ADkMeZCzxocjldExkjkZzRkk3nNHMiBFyFivJK0sOzvQDhZS2I1EJLvkmvBmWXvXo2EKN/XNUwZICqE/4A6TEC4nqzdxNRCV'
    'WUnr1vgENTJZYB4woxqwl6SsArriC5PIXDw6slAYy6NL4VLrIxkQB2NvLhvuyvdfN2VeF1s2HoObuwdR3kK72tEpYCVT6V2R'
    'ErazssuKOGh8QSutY3QtIoxYPfxnyS7t6qULKNQJoLh6v1M3XNAVqmcWLTTQeoqGKLU2snlDFCoEL1YWU/kbR82OrBLxWOTK'
    'cuivHZeKUkqVy9zVv6b3Cf2q28qhIT/AqRKB2ZzwIR1aCtzHkhGVn3e5pbrLXEiwkKAybUM5J9ymXR2jJxhz/HLYnpsAuzk/'
    'OANQGjf9e5sXKTreSyhjxuHUyAiLyYgIUmNylBkSEiljlDnBIT8Xql2+2ckc0T0WsDIyQi0RgpWRUWOsE6ZXYOCBsqDx7VOG'
    'KkXxGEafn34liMMbyQY6qYv7G500rIEdLacWKZQta9GVgITofHnZwnASFxnuC9UYlDIbM3OG/LGw3K+aM4Rd69w00vBlRL9S'
    'RGyy3iOLvjIvnflaLkts8ZRxxbQgsaAO1GMYqbsBKgAGfq9Tfog5S6E/J2Gziocn5IgLlZgoCCN+J7p0lZWoIUq07XnPs7rK'
    '/S3EWuh4+Rrx7yztTU9zryUr1GoSap1X8AkGHyFGhNS+dj/6Oe35uuJZrxDl6ntxti9GhShda0hr1vKZqwhBwu0+uYHHPyUD'
    '7LJtlcFdpeyISEsNwHCNdH8wv8dNHDmrWUmDFH+hEZwpVwkaVf6dREt7PmvmVaLqjcFp1wRVYlJM6D24mQSWYmP4UqTxF9YE'
    'UiUvaLM9znr5twgOMRJ4ErKTcI0ytoSdV9Ii2KgJ9PNP0lQn5tRZVR7Vr4uyAs1Iox5D/WeNk8i1S5mLI7F6M4RqhDXQMQmp'
    'Co11wpS9JF4t1VSl9toGB2N9+Hwh0lVj3ytysV3uE+bfs1hknXCF8IHJf/MRAC3MG9evxYui1r0egfTdVtU5cWVSMqKdja0B'
    'RCu/WaVr3Cp0QnMHopSOngkOyocBv1Wpsqw1MufN31Z893Xpu89fznfnWQtop3b0y09LE2m3VVGFppKmwM8qw4gweTWKNbf6'
    '1sn8gXSIVZmhZr2JXXLEPPYCc8fS46MUMNOrhoRIjRx8vslpIVLn6kCzHqU+vnke2v03kYkxKMzc6MdGqw+xvuuHha73LvHp'
    'WUaSxinoqLJCwr7RvLWpaoic+sSQi643FeDPeGtg0OEtoHB2WYfVkjBqDknV6THLQuAFhj06qShPnFRHLGijtmsXVI2FkhUK'
    'QLJuOfW8tnAnkxfb0b+lEfA35rzfGFDcgVDRq4530kYbGqrDyeDZOW4OiOLxJtRgctzqzlzgZen13Hw3EUvHDbpowBLtisBt'
    '6pS2fYZYplTlLDbbVRIx+RANtnBZGtVfBF4xCDzledrwPstk1TdSjMuVM67/9yyTYYz/wFrXOL9hMUAkCPPGSKds5YMP5x0b'
    'AXFUKONRSj4JWJQsgIbZd6KLF5oy1w7HMj6hJN8nU7ldxOhvngyeNA20UYcwtG597TJhewSullaWQSwYL0vhvWlTGvQsQa2X'
    'caMXBWNs85Qha3tx2apfKF6AmtKjxuJmKx42x8qvTSwbEgcOCJJaImsgYiAKJwqen6IwGf0Rn/nkyOncco3lHRw+lBeQF6qc'
    'p5xvLa0jEBJuIAyjniylEle2RCMxbUKZwz79KK8AcWtKWBXj9dPAarY7Wpyf0WEJ5ELO/m7atIt2oQm5iJKSasMzXvILcZ1P'
    'fziU+jz8ywLilA5f1AylOoGdO2aDTyNw9wYrC+6/GUoAgibevtZYfI423ycqn3cS+sTjIz9aD5ifJ0ivlzVoYoX68fmwFZ1x'
    'H2V+S7GpTpKOjbF84P6HoRcj01mL0ushb3Rj02s2EYBnke1sbopSt16KxKuCjagWmRwVUojG4AXjhSOZGucRnjPFCZnSQDPs'
    'KcgmK/9ZWUCsMiRxqoJiG450kgIDUE1I4v5kAvySGWvHRBLKuRoqBi0OyoJupKJqyeSK2BmFhbOhYC1KrmkqdNMxYIxsSa5f'
    'I8iHiwy0g0/CVpANrUfXe4wTkSl1gbdYsTExjZRy1UXL7Zzc65q/t3o55w4Qm1+UYgDIszLHgFxEPSgFNA6ny283kiMy3iG8'
    'tfQveVAuweGUHcbo74KDjVH/9jzs/hJ3kZ0KDmA5kK9G7urZ1rdPCd81NJ9rDknUMbgkpxasggWmvGEaahcZ9ZI3Fi08A3Sf'
    'RmTLEKHieY+brDtUPK+0dRKnfVukJOl5CFMtJ9QSN3cILyTWxP1GTSku3WQvaVysZIH+A+WA9wl9EixBVQyo0FsYEtIl+Gkc'
    '5OzME/kjavgKPa6l/OB1eawZfBmarFHBzCjDoNyKg/8cd/C6ac6C0K9UkSU6kvvM2iYbmJekB5GstuLVWlMlxbU1BoiWz1Fd'
    'hXRv9ThA8kFt7kwwwBNTD54rrgz85k3o9UWdLZ4WkWFY0YKd0tmteqyQYYz7uGqdJok0QrpXo2TETd9YYy5l21hdaOGvNewj'
    'ojkApA5KTYfyG8CxqN8CYt/Oh40tVvVSp2S/vqJEncXr0fEnBWxEYTYB+OuSlWMhOEaUl9aFTKbmyJILM/2/t0vSX6IAwE4t'
    'ZtBZbsHK10nk58vyc7RfjfUCIrEG6m+FKG5QILVjHQH0qQZxpXaypBo5PJFvU/UGmJeBR9aYBPG2tRJtROqJWJ6zK39fKV2A'
    'U7cC6zieiOFny7dLFTjgxRakHCJaVF2Fta6NRBtxQYzk7YqWCTvCXkZqgXU7hwv1GJlBBFNN5HDV8PjGkgx8Z+O8FnX+6mys'
    'c2EjKnAoFLU0lREa+rXKTyNFPWiCEE1KgbZlLm1DAX9K11yrH8tQ784y/S1OeXny0zyZhhIJ3TvokGloV4qMiwvPVNwRGmUU'
    'qn5GsH5LyZBsn7oWNnkNW4kVx6BFLnlfESz8rBBHH0rO/PJJ2Wm1kbDRq1c0XWjs5rwYEHa6Yl5HSQ1kE3H2tErHWnYHwyJe'
    'm4wUQPdTRiwqGICSQm54wIbjLHN/UuyYhbGsLOnTPEUt6nA1wBwf2LfGwsxU1JTnChnpxhJFE/kG8QEMa4EBbIIqCStHHoBu'
    'rneBNmdBfHAWNqtdL8paaqgkkWRdLIy79do5YBMFYTk/TcOf4jmuz+ciRx6QWJUqHYSbXHInN23rkPLAVKvQyfETe0EWHK23'
    'om4n+gwZN9M5uuiwCpn2msfoqzMp57aUKVc7wWt4EB12Y7ko7oCUGLlT+JpqLRSfSyucszyHi+jZ0Gq8tMhtYrsCr4bmjmgJ'
    'jnE5pTY80Ur/S2ZMkolh91wX9nKQcby16UTnm4oGhF7haEsLT1in/bBccjyxlRawxyR+ki1OkzumQCWbem0bhWGFatB0UEjK'
    'Uy+16lNaDZ2w2+mlt+xEGVu+qTDDqiqp69eqonPxPEscHsyUuQkNvg60sQgyCOEnwyc0NJ0ZIkaZFV3KwDZX4Y3V1r0qt2E7'
    'DVdNp0n1z80E1vjYazCz4EJeI7fTNYqWFhezC9g6+uPNtV2QmjOhztRcOY2GkhOTAXQxDg4FmR5RWxVVGYYVMZCzluKkEVZ9'
    'jHNtXFSST6LuUOpC6x7OJgOmO+mBtHmBIqzfegIO0ZxY2AqaS8c4O6qL9iYHETGVWWnJ4G2pQt2lLHabJ0ZRdw4B8fyyRMRi'
    '+ZQgO3Mtidp2oKglOsYSGVLAulcPQEquqByu1X2tOldrC/KKNNJFBWHGq0mmFE2lWOPEtSBJFX2q3QeGMNWlUSSCfbFZOBBi'
    'noNsK2dK62GJpCzy1M2fNFYHBsPDG2pCF8Sgm5BAupVoQTcWK2iWVlJzSWmKJkRLCuAbsS+iABtjRlZpuyW5tQp1JYyKNsoW'
    'V3ge1heDxJQf2JRSZoxqvkLYanU+TbARxkSSQkRcqF89MSWvUlYCM+pltNQVQ0nyzfpfTlG0hlLaingSXCx+JqsCn+nZpFr6'
    'GVPVLX2TbSA3LIvEJKKQcyN3Ed47KqwZ6PTK6y6RkMaygmr7FqgwbXlxZjA6ELhQXBVZ2IblOSqW6kwmKOilhTMSZPMUhw0e'
    'FUG9Z7kGN4uYNwTKF9XJvTESKXeeTllUAJrIc2Vmcy3MJkm05DpsjF6iz3fmYLFmE3BOb4wVLZf0BBvZET9qdF2/9WspTDdR'
    'UufTrSZkR+DG2ZjFBjTBdNPwFmXnNauVl5SHM+TKh9mSWGlqvAwVSlIQEWpT+gu0q65T5aeEYiJx7fk8g7Wm8dcmRGbSr6Sq'
    'B11UGq+dzeYVi1Y+VFf6RZYj2YtV8M7TSZt5leS64n5Lp46iIll2yMOVN6a9+daeAr827jQ2oigEJsi/PSTISmDvH6f6Wn/i'
    '2EhjIqaOVdMwL84cC7XWHSDtsiSyTHW3180UO4Pw/UuwxsIq5+gGoiJ3Mi1MoklQXpgqIxzwvm1oIZeXq698SlChukx90ow7'
    'UMky2FWS+GZSyrbKiAplaS2Pb9WJTka/CofUJTKte5HIKugIJhcGLEQHzV218cgC3kuoUSWVnPcDHIxN5srK+KX8fFn1TTuX'
    'LJJ4pyJUOvXGSALNqr5xvGUnoGhWYZLOeaGaFhqlnVUrySgV7VKp7FIxBoUYwsHSiXbdlNnkUISEonrnFUBS2E9HJ580lkUQ'
    'pDutZZJVQhtAd7gOIbWEy58fBgqYdWWN+TYWm8Z5ouxLTQKPrtCqqN/X4/DxoVV0X59ppePBJVcucqoVmChTnOzifihlzh7Q'
    'NAMHbpnvWnLXhvmjFdpiPUOTybdl4ct1HOzrXARzvq6crd8LJw70adnU/nauHCegnbleZkB3cllyZyqSeTai3PmqZr4UT65v'
    '0UxNsV3xjjnNKQQV9frwtp7KbcpXlmA1h9fI5IGNtKWY4COWkiuWrVw/glMm+Oj0idCKDjVck5WcBZ1gOLIQCzthkSrnE3Py'
    'WPVMkZOnEkVatItqwehF6Zcq7DzCG61OtM7gdUpk9OH8GNtYSUCkPqf9qR2D2NuoGdYlB+doyiGfWqMOS3NZz7mAKxEyXqiB'
    'iWatktrY2lWZcqnyoOlcglml+eLVk7cNFlyktPUjRmw9NhA8YqL/nmQZhiuy7FHASRLVwarcBALbd71ndA4eTeQWa58ytK9f'
    'BzcyOW+RIeepFUuoGC11z1pLvOYolVzUvgTD6ut7APXZkmnWqk1jvDGDLyB/EeRTrct1gRE5AYWh0chXpIbcG6S6fLfX+YWg'
    '9FoVxxFLVoCnNAetRmjk2cua3gLr7tXinRevYOrrluwEjA1P9fULiNPpQEdrIYebJy9zmFUuzQrUBdJXJhtPqXgqVhlQMqsM'
    '9C3DkyQVTaPVEob9udZXY91S2XKVNLal0SOYTOnbmuL4rDQMDSUbTimSjNduSo2CaS085luE/FqG7IlJCHruICNICvJKZ1h2'
    'VDSSipqrShDhOjMLe0Yoa4aLF4+cVKGT87K46HrV8w2twWU6rwwEM0Uqg1o/Ri2BI2Tkoo087IuuTconJ6on4WqyW/psaPOF'
    'aL14kfUL9dUaAmNFhCGFpkRxphOSfmzQpRay+1XRYy+elFSV6yHCpckRqqWEqgiJBdMhdfVZhYtilGcIU1gkrhqV7fKF8o32'
    'M37hVilQe4DliuqnRiVubc3xcyIWjdUg9Bs2+MmaPZX+zSrks1ZARRI1CPz776A+ZkmWu1DFTF9tTQGhy3KqFySUCYgMM7pa'
    'C2DuEtUv1QpzCbrYOBRyLsaYmJzXqLpea5NK/wp4KK3+YcnqYvgJy0hUaybgSouR3IvF4PLWAThhVFH3DLi/URJSVgbTBTQb'
    '/A2elXJ2stq5JYnNtPG3oqYamGhdWbY2vYpD0kTUimuDhRlv5JAWqZP6vLUsV3nxBQJNilJ7hs+zaqNmSWppsVlLE+lEIUN1'
    'Pm8yC7WavKRm0CQ3miiClo0Hl8uUyXBXSlIJSVG2dox1spbqCs8TgRZsOUXgDCp/hBIeB65AqzDa86PWeSIPyWJkFQFIFpi0'
    'afPiQKumLUsBoXKvaiVPCOUnVVeknOC5PMGNiB87rthgAGQIoRbPDqMMSSzMzZynOWE8L6grgOAkRO1qrMI6q6eidSfvUb5h'
    'fYezDFCFBj7s2HWNYLPwdr6VCjpPjZESX2N/49F1Y5G8OYvMIhPy9AWG7AjMqsfuX/SFKYe77rCkauvyO8tz3d80ZtMbclBY'
    'TugwPQJ+GZSImMePVaTqEpSG8kOYRApIcqyWix7PZh+yynIyTS7BYEny0lKEvDbCXo4ioXPUIhF4tfZCDDQDCRcwxzwwqit/'
    '12sQMLxz3nLMhMWIklOgEejU8OIiBaegZFxBeNAC+zWdmTAp8dbg4YR5aGHKmpJLw/pxXS3qpB9iBpdGFeGNbEMR5VCOKLUK'
    'gxYNsNkBq1S2DuNjDogPRIVPGIh06CJljasnPSKxbeuyfQr0XU370xxoniBDOX/QpwgbujSZ8Qx6VlIuVchTOm8c+alI6c90'
    'TEsxuQF6odfzTS96OE1aiQnlvmoVmlo6+WPN2nF2+qQ3s5T464ROkiUBVOFMTlil1L3mzDk9hXJlKezzOaB0UCrLUd+/neFF'
    'fRWLU8XhJDIyKfLoOB8wgbHbIGK5/oGOHF/qNflLug6aMyhR5/BA3nZKrFwDZG1Zg4LBZbNYfoeY22hFLvGSvIzcnJTto5MF'
    'YYMUpCpUX6NZNiGuAl1Y0WtiCKalGmTJzhE9XbeaLNPbN0tdttWd4JsCHDj7GoybJwO8wnJyAaiTItu0CuZ1qUlYZpu6MVye'
    'wMWulDg6MzcgCD1X0UEgAw1wc7K61jUrpw4TZkRTSiQcGzUE5ymUldqANOVm2PIJI4HMSSOEil8f5W4EMJ4nTR7vo4VTglXL'
    'b5KpgmJg2twOWj0bmokmHVwe5nVtGFMwKZ9AjMGgloKaVkMJ2R7oPxDQkOrkTavHWE3UCiToAnzOHo3tjuuQE1i5TgOZM6p1'
    'EyjJK/C5W69RwaCIZqWfVs4RuR5niYo3US4nwx3rB2mi+QIvC6wJQq8sKkrCM6V+8lu7giyfSOfCwzARTaRKLcxlsPWTS2My'
    'IHEBL7XCyy57+zpFTEve3y4n2+QtMxFA76DeVVryVbphFafpUtegnISzJqS2k7sWbYmpNftaLByQAz9kChRY08wgpYiCgDMt'
    'DVHVZpGxJMGqS5UDFZvTxdKYI5xLR+XVBEXhGs6X0TaUpuUQgocR/hFEqY2aert62ee4wrBYZk5PngvXGjuedoSXGQ9Subqo'
    'q02lxEpyB88gSOa366LnkehUpjqyyiQXhbagrInVoNg/14uI0g3oic7x+jNWHIH5BRySd0xg7tS7VXsFN1EjluSK/rCSK0ae'
    'V62lYL41IzvIsaxvGqt57DraGXtFLPraZ/wCvTapaHEdi/fbiGlOmJOMuB2T8nCwdNykEl3jJJ8c7uJFI05SyWQo/8P0b1bT'
    'OK2mXkkv8aF9Svu2R2xYHCudTi91w68BG2NT8BM2VBVg6E23JUQFPE5+ISJPLE8KoUCHELNXEmOCCpzhBVatCKi8PBhrSjcN'
    'lPCjV7NbJghJRdzYWPOHmjKRQiMnwYc2aGyniPKdumpEOPTwpBcTVoNipvq7wZ1XocUqRVQFyhe5tti127m3eMjJazNHCnkc'
    'H1mjszvncgSakhX7xsMolDeRV2Z82vJNUh241p4STUxSWqeppyBCFUin+qVTQU/p4aeUEbpsX3XiXntf660kr333+PBx/Nb9'
    'N4MPvK/gZ89fsWRzg4EvqC+Vu67sxPHD8ceTb8RK16W5G7R/HGk8ins//R8/l5Ls'
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
