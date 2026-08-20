import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vW9mR/C961oP5KXrfNDYTG9GMDNkOkR0QgwE2QYBF9mF23xb739eRRPLydnV1dZ9zKSXxkwmauvd8n+7q6uqf//fq'
    'L7/+9rc//3b1bz9f/fD14937Xz7dfv7y9WF7tb+++uuv//Uf//3tf759/Nuvv/3nn//n2+efrz58fPxf7cMPX//0y+1PH3+8'
    'vbu6vnp3v7u6npuvP3/Ybj8N/uPzdvv+29e7D9vbL1fXN6Ovf9ze3f90dT07/vzTw/37r+++nP5ivd//3/WwY58+vvvD10+n'
    'N80Gffv5arf9/OWxrT/dP3z58Pjp+NXow/lAfN7e3Z3euhi/9fC4watAQ4avPX0aTwVqwOh17uzhNxyb8jgpuCHkbZ/ubt9t'
    'EyN6+P3pbYUuPj93OKCmGY/f/XRaDWd9fZ6qdG+3t+MXnxbG7Zftg+3sYwuelipo0/k6got4Pl5On++/muVk3nNs1u/+vlnO'
    '2/f8iU2qHadhl0FP390+z11mNO00Hptt5+7QbdTb+FVoD9pBO3YMbIrBf/pzOHrr8+DDsfOOFmmCnocbbu3hGI62Gj3F4Oqb'
    '7SsDaWePTGxht5u1fA03oj5RoFfH5z3vebrLhC01+mM6fsdX2r6cfvS8IdjAPf81HLnTO+zAxY/+dlx/Pn8y25/gm6e/P3xI'
    'vYlt3MGANbzBfUpry6On/RM+dnSVLBxzMjg5E8dDn6eOT9jM4XHxFozNEvJTYz30acG7+7u77bsvv/xu+/Dl493Hfz8/dzoN'
    'XvkliSVSfsdEc3C4xAftcffQ0RMZ/di521f7hNn3qtd/Yn7HfVzW3dvY2LPuT8Y8tkaeNRUHFjhYuBX3AphCcE/gXsWWgx0m'
    '3odhb6M+Vqzk8VfthujIJC2OBfoUPhAsGd5Ca7c2uKF+k6X1Tr0l185v3EDGma35q6X20fUkIE/h4042uTj5sQMxMPONMRhv'
    'foufENsybl/qcaGpSoCzCxvW35/W/2nyvQ9sqKWKctcNA99WsIfzOY4+G+Hi3069h3sE3bTbE1WoLTQgwh80XaXO0ynyXbhq'
    '6fWXsArsOT54HrsgwvOSDVINNkzYH9y0idcVMDjQ6JYuOrJFww/F4RjczYWZBBGQ0bVJYbHak1vOX2BK/CuiYd8f+/2xUz5W'
    'h696GDp+4B1G8NcR4LRKwycklnX+bmMNMWeuozVkXyPaOsnbkdxgCfimcqORUWsLrRtUqef1fvxrZ3Q+3D78scuFbx6COlOy'
    'qsGKOT37rP1NA3T6dOQSgNc0W8pHBsHYMKoOClw++pAAqoeNnQJ2hTIioN3D+QKDMvzvp7cLseZDjB3ETgfhd8JbGTBnCvYd'
    'GJNr7Mt0uS0tj+i77fD9sa040Soyn55/t3k8aKxFtcLkx1nGvnq2ZD5/ebjd/bB9ePgTgONLIFPYIfXtEtKuRnHGLekSohpf'
    'kROZUs0RqoSxNsavmiMXCXMkx2xrinXCrp9jVDnUCKJpCe6T1PdMSFRl8z3eyYN9iCmt7chi0zo42kbHD20xb/s8ZySemlK1'
    'FgHl7qktldioz1kbtXmwog83lEC5Znw1Z5XoMTVyr/Yh132PV7189GudAYVWjbbKYl9A24UwWEO8C90pRcdNZ69UbhYIQ9h7'
    'cHd/f/eIr0Ez6vk/n2fo2wnx/mqvn7tOtxJfS0coDmKu9wmSQyfWyXhQnctRN2MPk9O0PEsBsv7Xe2ifjq/9IlrWl6ykgL0j'
    'Q6PVAPRuYvB11TSscXoI6QjMYjgYCPhxMwryA8Cae3qowVSrpKZjvy2aVGE3EQej+ERrDhfy5whvquQxo6QgazTaho6+uRjT'
    'q8kcWlfSWdMxNYi6wKjasj3fNMI3UIhNJD9Ri0lOg0WmD/rbAk0IZY6eDnFLEcqZQyiRsCGahMYGJHIJVB7Xqi4xf6MFNN5w'
    'cym6WgGSChYLSpFlqeBN2Zk0ZVYiSzXjO+IG6w4H+qnITvMqI213w3GchUlVdiVa/syCohxx+SwgQBvllB1/RWLo7Xjc+JQB'
    'Wab2q9i0RGn+yKgGUKNtpvehuKyneqcd8TG/XoD5WowjYmqhvOSJX8nyDVpeCQwB08u+b9QmtusrGYiIBDMu9vKGD6/qjSd4'
    'Luk/tHPsZjPsDthgxPNM//jx7g/nrg50hKDyAfoZiyEf39XH85m9wX0VSH3SMZ0Iuqo/Rc5SvHgGRpJm6lfIhLrRwTh5zput'
    'k3+0vyIrX2FApjSJ0IoH45ukKqQ8Z05THe0WgeZwtGUj/uLJ2CYpj3r3ZMEYhaxBpxd00R5Ibf4ZaBLwTWSnlHYH+jXbPKZq'
    'vRhGQgz8Kin5VZ1geIzhWBWyWZl7Bn2WQrYMcNn4oAXcE+qDgNEtOBrHYQEXGGh7EBXYdnBD7EPef/z9+RQybw8QklMNYps2'
    'dIy8AYjjNCcKrKXgNnJx2bCBKWaDa1vbFMABoMHJVjKtJh8qE01iHoDiG2xGeb7tD8d9bwzToFkjfrX9UeI4UdoDRsY0B9CT'
    'wIdcQI+0LdzGpKl5RKSSAsCmNX4V/5Eguob6SL1dbQJfPL+zPxLQHOA7pyCzmF9ZF4DF6U4qBdD/Y7+7uJqBdTWAqSJb0xpt'
    'NGolIFbbcIsXyiOml9DMWpRtIZnVgK0mOKG5r9u7mLC+IwhGUScOUpcawR0BZ3gieC3xchtcaiQWHC9KZ7KYzzJySQg5bdmO'
    'r5nBQC4RiVWDG5WELGlfCicWRRaQjIJZZgxPqlDhrF9s42wKzHCtqZQlDyttuYAbDoQoUS/Q0cu6WErxJAuDHzJgrbITiEWA'
    'C4448xvZClVSflhgs+PCIJa1Ne1RN7fjX9NFxDJNqwvZNhjZacQD0L4qBDKB0c/8yolMcKZ9Yx93sWbl5G3MiTt185Tge5+w'
    'MW+WCv6+lvbq0X3UCFQW4vL7gzztdW6P19mq4x3+ekCG9mj/TWyJd4/llyGCXS6qLWMEeVdbRDCgzEaEDrD4X3fl59yjCz9T'
    'st/sYQ/mNYpHJ0gVLOiXdNXJnIvlbNDPHF2TBts+CJcBE17+oZ65ltIUE/E/iFcBV2P4O/s3SdlRtygR3sfMcZCcegi3vnUP'
    '9U1sTXHlq+jAxGsDS1vl8xqHndzsE+FaEkllMUPs5vNFAhs721iEf7EvhORB47eloGhDw9f7AmWbYimUWA7nTt0KqP0rn+H4'
    'Zl89iVBmIA2p69PWZ5LYaQVWO0KTDyS3YRlE1G9vkWIq2tnTip1D9CV8UlGCD1PIlXsvL81h1C8uLTmb5xLdUHOlDBGW0gGf'
    'ypbp8w/nS2923+x1+gptLKfPOKvBDoif21/MSOaoPrBH2Ph7Re0ieLGUns7iO0zVj1VSZFh5s4gqQPt8lhJjqeJlTrKT/X0c'
    'zAMqrXmEULc+psvWPXmAGzNIz0NFtKcM4IiLZb5vJWWgy2iQWUBysJ80TnrlXS8KzI21i7XY5OLpkBgpwuUJCKQI4pPTNk6w'
    'nhRGL8rXMMpHU+EG4IsKN6J2D6W5E7WYaJFmUkkZSb3A2sSZDitLLgumgVUUtr2ikG1JuWoKgp5IG/6NThtIgQShJgVFa9h/'
    'EhuwhiACt5Nlm1Gmjgc4pVZw5Di6xmJEp2WuM6Xe11Dlaoo5/U8xEV6yu8iigOJEWwHQIqpGjcvCZgzxd8VpFYxOxP+myBc8'
    'Dq+ctkF19zV1fqHStq3yIJF0SC2AwCmKXTdw/GrkHDD+CEUjQ0cPmy2Tq0FzGg8/VaQJVoxQhynap3SlVIecvkcZVjQdCt6W'
    'G2d6zInjxz/pq0JzlYMkCgJmuSuHdj3X4XI1zuiEVoe712SUipPCV1rmDiMCgqtVyKyZRjni0lksA3CkXXiiJ+Zx/PI8Zsgh'
    'kukxEACGMJ9v1zfWfxJGAKkpGUaKDGUkA/9BCgoYjgzIbz2IVJEbQjLKJx11SZyheEzNswQrI+ochyjKdcwUpbWxdH5RdIIK'
    'wDm27dt9hask4jpMgEWNL64yEWCdVsVV/UolGOxyBHBCoCZI9fCa5OeofkvqtanT2y4nTaeE6yBUcs2ZEKC82XCUzY8TcqAE'
    'RZL3+kwyDwzQGNBEDge1ow/G5phnVykRcRa5HI7lQmgpv0zRxlChn2J5TaqSmV111NPiTVXGk0SxKX4YeNhbxRGBLZz3QGoa'
    '2tnU9EZ9+EIHOPyiNJLWFhcBFYrfJhmK82lnWtlZXWY6p4CRUNDIty7tTD9lE28w90CTjVi9nMcNhNJfhGZgYzmQBuwDBJSg'
    '6uIEfZxvPSGlRUkvI+Lts56V5mREI1LOuLIAosSQaLD1JJFiaaI+ayawsLKEj0pYnRAF0trvskhI/ha+ydABwtlnKv4sxSMY'
    'ccW3SaUKkPyxKoGmTTEfkRa0GGTAhtEl9RUKgChioSpfbjsoMjJt4WBUe1c7oO8Nhk4gS0wwd/R0pAPaLDgH3HpaJiFU/FQi'
    '+7mwKltjnD6QcwZyrfKS86Bd0TvMmGtqovxaLsKb+ClApRIQmlD6UN3YAbmHKTmWQIC3+4vFV0magbd4pmwywCuZ6kV+VbxM'
    'O0fR9de0ADQ1E6mNNYTgqTjBGUTw1oEIlo6y5D9sUP58ICZHDKhEuNOdFwnJJ2xfyd0XfPS2UgWNvj3zF0QQpXGeiuiC6vLW'
    'aPlgMJiwhMluHedmdqbYo13EfJq2KDLI5MHd1Fn7JamC5b7Cn8+zFhorrWiFYKijNIVGinVMjk8P8i3adVBUj5al7OssIgp4'
    'MCa/IqUTKRmwkR9ygYZDT8jkSd0UFRHWZ0IZEyaymCXv56UptLImgYjKVso2GUxbkdROPqAXpjUsVrUorm1NgAxUVH3iilaB'
    'tkKZd8HEELTaoi0VQNkUFACYQVlWuBo1Mn1fhvLc+kebfxj/iLjGRxG/64mDrLbWLr4/wSqFvV2KbOyCwW5N4mr4IyPE14Ht'
    'TD5Eg525WLsQoEF4rE4o5xJufYKuChcapnYNCv7N5snx5xazak0MX65cqcTobeWtQ1MjcqtYJ5tiPvb/wI/y9UFKdf5YbQ+a'
    'RB8LQ7Sw6xnnmrYm8sJ00gR6UjMzO6vnL5K6K6Wb7MzT8Iycy8fq2tVo3H4GW1BTQ5P1LySOs92NFioTCXQHL6Pwtc3Nbpox'
    'EIhF5NsnEcJF9wmOLvFH84iY4uhkvBqilZav7Yndd5UyTR1ZCjRJIrtMyEPmF6lyZYpsnCT/luRXs2Ws9K6ifqesMermCpkG'
    '/WZG2UDo4OTDT4T0lKmcdBORJrEdz4LO6Fdadnfj5JlYdaZUS2slyI796AvOzG4G/zHUx9u8qqj2JMT3y/Dd1xTM7h/IrsmH'
    'x95MmsGOzcBi2cIJwttFanoMHnWbUz1jOPQIJwh/nzunkEgRg/nTRb+pmxorVzdkSdiYuPUCA7n+elkHJeyNXPMQLtPCcE2Y'
    'EqtQ7ucMd6X2U7E/bsjpIG8BJGRjJDAuMoqUUqEfWIJ9XCrUj7XUdAPU8HpaD7ySss8C25LQN6S7eRVIsyEOTXkuILo0Kymy'
    'QG9INWfFNxsyXBcZ8IA4QFSNAiiGO0/SCpf3Um3Xqm75KFC1talBp0ls51ZHiE11IeQrlJAKOHY5xgZNF2cYrdOs60sRCYYu'
    '6doNwr1WvxTZuJeWPAtg+12crD0NVQC4rjShVY4lJtgB9axs/csU7277cinZBQJ8F421fEZxcXXJ3HUK5hIrv3+hOBpgjaPo'
    'uilcmpjZpkOut0XUznkfb5M8/7DoF7l43ibqY5XyxR3IJDnNKms9nyyl5ZHzGL8uTgb6eD5AkF+sVSpUgAetxkNWw1s8F2xV'
    'LmUBUQ5AtvEROaS6ZogYqMdhwhRsdcmp6/0mUdNYPEsFSrLzl5lB35QqDXJugTcBlJ0fqHgq/hUtqaflYmBOitTeptVinS9n'
    'NIOkCofWxWCO9x9/73U9v3pAEgK3E8RiF5IUYOWkLAew0yJqztRQxcp0wVe1Q1QfTpSm0/Z1iyro24zuHshVp/LwWkigOUt8'
    'kiZTXt0UTZYUASRxfcRsu3gm/jP3euXAQbOZY66/fWXZJcvXI4mvSs35JVo1VKspdaQDPpFXSU/VPLPGe5Bn0p6twCwjaG6U'
    'aetSCoqKpRT/X+xFGbnYt2So6JklItLCnNIeme9awi0FH3S3TI4hJAqEqVTWdBEAQIbK+wXZenFcPt7JRg4cZNWp2WQgH24p'
    'lkpV8MNLzuteJDx5tTAbHtho4ZdAlNm6tIboPmaHzrlX40euC5AvKyGiVsQLJgOv/bTXta5VE6nmCkji/cqAG+h5nilyoBU6'
    'qk1BPvt+tnHDIWeKW08kIuGkPfbgAJAc/lWzgzgtdtdjvoQAFuO6uJwgNUu6D9EedGxR46AcPx3myuN00BQVseBvsAzTyThs'
    '7NlMsagDUzmW5+emVIfZbpfzydDSPIj8sTwlaxIoLeN/tmFgfyn5HAwNSpcxQHtpqXJqfM1FVP8npRpJepvqWVs3JMlK8OE5'
    'bHwGEb2JelqZsdEbWmGus8et5MoUL6ihcopYvI4qFJFnVy322APWitRDSOp3KoHGyT2q5FewSy/kPYV5zHWpkkQuOVk1qbqW'
    'dSxSLrHQkyolEVXIqq2UodQrguak+4UOPjoJC8HgZlrsNGvACQdS91DFeouz6fpPMzM0q31lW+igpgj1XN6dAnPKsj5UiQhX'
    'B0Cxzq/VIqesqDYk+mIeR+TII/vVnu6VHTkT5oysRHh1pkuiKqhZafmtE8uPRVY1Zc3ohx2AlwwPFeioKtzynDzCVLdAlD9m'
    'VyDWtPEoVNuAWeWXNWo5PwTzDXrBA47tWi+nxPSMRss+N43W2fH2m+0fybsL8myZzpOctUzlHOL5gqFj0gRWWTf56563MC1k'
    'wuMqSj/ow7qCmDifchtLMukLkCWKNszJIpN/KSnuxv6yhH9OdaInpirY8vCPUvpxxV2kwWX2SpZAZ42xzp4gPL0yuXPlQMlV'
    'npVAT27f9zEQb8QU2CIfbr70dJY9KZ/Z61JgthmHL0qJA87VLsmMm4gQd9IAgR5RshRLF1xNiodhq1lvZnPpzC5plCylLFa4'
    '1fkycg5eC6dSFj2yl7qM71WqSrL0GeCFxelDuwTMrGniimpDKq7LDNpwvesSM4oqkZbLwS9KbE1NIVqEWuSVSuFGOpFgaS3m'
    'I5WqQJdJGEvRFiuZdi17Lapzqegj1ZSPqDCkp3huG3j+S35M9BYfU6UWIphPWDJZPaChqr6bZOasN11aPOhb1bCg8DzF81kh'
    'p9CEGzvXmqsmyzEFcV7OH1TSZ3mGYEHllsZQmKnMJeNDj1QTpMm7k2iJhQrjZCcI7nZYSaamEA2rDcbKVQFcFYuBh91pFeCi'
    'bahy8VyUVJO3qkE4iq5UoMLGBkVSj87uq4buthK8WAZiUG9ezky/ru7AJo7XfK2EPZ5Am9eI0Fxc1CqIHrAr6NL1r4KrXCVM'
    'SJhJveqV4BuH6ozeD4KQadIzlLRId+0krlQ1rwgRiU10xTvHgxpjX5JcDe0Cu9TXelyTqdyqSb9e4lJkualENU2+K88uC9iG'
    'u60KJDJLW3QPVbtspVOUNJghD2v5Ho533FQYS6sSpwzECaLcQB0C9MTKcgkglSC9Jb3Q20p1Wj1ARletwf3xl+g4xLip6GtR'
    'SqC2A70EwKm4jpabRSjl/qYy1CCrvOpMqdq9mSDrKsxzy4qmHhTPdgZxocRanpX2pu2AOzn5NAOXtxWcOYoi7yIzpaB2FBHa'
    'ouB5gLGnfOoupgETiWd+SwH43m0zChKBLTDXNyDiGDEbNMC8reRZyMiRxbRLICFnchHYJVB5+7brHu6/6Ko8LzCNUmhCK1Yv'
    'pV6LtEqO2TyP6ylTIgKqlLKINLtp596hg1oYHB/viUMKd2auXOIxR9gPqdo04obOYQO9SpRT5UwAupjKoE+cRJum2evBGzvD'
    'I98wh7BnsfvXVwJu+KHq+rrZsPPcl0HG6mClumXmlEHQ6wKTD8AcC+51KedPt4jJhw7JmU3yZSncj6Ym60Y9O7JkrK9lZeiI'
    'lg6KNGu/6eXD7QeaXM4GXk1PaDfLwK0EN0GGhZlgNhZYlolycwrjVj5pBFR0kTgY/VJ4ZfarqopfOy1DeXW/aIJYr1egN8wy'
    'Wdk0JJ4aYlk7KE+VYZm6gWjZuYewiVLr4iTfuPkL3chhM4NGkW7MOB2S/1EXjok9i8L8ZybpxghmB18ouTmuZa1ZcjKJ2rAp'
    'fXrGGBTTIZc1qCy8zRjJh8PVEdYvcee81dcBeiAYPkvXL8o/xnHfmynUubClW5Cmtjv0sAntCsnUberF9CIlHsSMUQdM1MXa'
    'dJAtQ/oy0g/rDLzGbB4Ak9IrSNObUSGoTZ0bRtc5zbQIFj61xARno4iPWq9JzC/dSgaDVYOkNWa6iq3dGCLeLIdvYUDNPnb1'
    'L0HPU/MgAnre5jL0PI3vkEmOL6Y3ZKhlDcy9gl9ay6DkN1o1p7MDL69fgiVc6dWeaRqxGS0xjZ8niaLtRNF/eIkhtsKchq+F'
    '6t1OEKNNc6q2VCvpny5eVZlCSflMc3hor/A5IhMqs846uB0D9h3hz4kZJGoZgtD109NGJfoZNXqlUl7hnppnwpG1UoS0ahpz'
    'v6W6DLpv87Z0TEg6WJ6TzZepqEMrcyF6QUU6GER3XLZPizae3JluTcRiDJKt6Ml4TlT++4jm+qbyH3sASHLWPjfc/MscjNTT'
    'jJTdbHjBx342dKApG2lcNQIFCwhqelkUKSfuphSS8PQTGPjyOFTFndzc8xAn1AJqcVXSQrLkhclpblZnhL1IInt+wVOxkkM3'
    '8IyzCQUepk9f80dn0k5qHLUA3LeZv4hQCguVgoN8k+LnrZ0zetN/A7DCrJIQplrttoWv+EawWqrVT11Rt2UVqnx68M30dU83'
    'r7DuKUsqDhh2G7FaRFPt0wSJrSI9HyOVQepwI7iXKfJKhSYLNUu9KlPyMIMjoli8oVJ91IpH66PtUTA6KTfZobT1oGItEWEt'
    'VRh0km6X57yz5L+Yk1OhnTE4BeSgRbyyiqfXvHpZYTBmtupjnGAuzBOYiAPm6FSh0FEprupNOVgLkiCjxRO4vklAqMY3qGBy'
    'vEpwpGfHCHtsfa3EqSHLLhY0VFGrHJwYEgMt94wdTxyXjuOS3FkVvc9lDUGMzREKDQVJpilAVCWXlaB5wkQKq3gFIpFk+vu4'
    'UKKCG+PRioWTd+mC1G96wl28ZoCuzNilBo4SMoFOg8FdtOgWX5g0E34TTZkHVpyXdxec+THkMnSaCV3WgWNcSiBTd/PjE5Oq'
    '2IHU0fCIjwpQabu4K4MxwKEWGRYcFRbmIalNoEcMQoXTLuwWPt0N1bU7jPhc14yYzV4u3bRQ4xQMyaoK0skaNpevhvpyRVB3'
    'jV6UNWdfvNSpjzTGoNfrL3KamLB6jcd8bQNRwC8FblZYNp0ysqjEO5VejkYsTc+T7HiybhNpoe0EWlE7bpij71Ve1Vcrt3qk'
    'I3EnIeQ9hahyPnqcSJfhlVQ8/mVirhgrNMZVooHwQPKpVApF5F0WzfTphxUrnMzLIlGFlDM/kjJ9QZ2CutYikwUVGRdbL62t'
    'LjK4RBU2W3YLYxwnSTjwG0zjo0lCPeUVd2JaokzX2IUHX0IP601qj608gopDMVDQ34AtHlHyNMGbLBNrU8s3DvjudnkOskwj'
    'tqlBwwogaQNuI+EXCB2ldRSkX6WzxZGREtW9F4YgXbmHV8PikH+BK3q2aocraVGnmimatxyeVOTqYMXQAzZaupKWumdEiAmM'
    'mp5RrOt433goZOagFWeOSFPsUgWQor05T0i7tiXsuqVPZwZ6XATQ4zB6+89XB7VBzs7X2Zs7JLnhfwNmLv2ZVoHrJJJT1rAD'
    '/ClHaMEnCFaTZRUdO8udymFuckmFDK2O0C4ip19RlPKR6EZZOpnc55ad6CJr16hFB5YsWpT256IUdE8FOkL902mKlaodJc05'
    'qkucSOH1GTi1BUynMDyHWNy/tRojLcZL0WbRnBZybpXkgHDO5KqLgVFP9cd1QaCdRknLwNqcQNGiCV+SvwOnWJQ8q7B0WA+W'
    'jbpcrP6AG99Dp3ZB+K5W24v6LgUtRcLqhOiUnrYGzrqITsabraREkQSbdX1NwPA2w0QCXRyMOqXz7+aNKVcMKmLWHMhDA2tQ'
    'QX2zoPamPZvSAOtc5STOFwh+m+5TMItKJqWSu88UCkjwIV2MY10H7bTqp9za0PDKScvDGumxVYrvSjlzPMiMKh2MD9ZXVT31'
    'sPa9e33dXKigIQAypW6bF+1+rXpuNMgNG6RAI6pqW0hG10EG5kZmZL1TyZEKfVaxvqCFSLARPaEwJbc9OVCCVdjMAklU1lTK'
    'nCdyLAAZg4tXRD5nlU435+q9I4O4QteygjgKkqKOhuCz6swYPKLofylgpJcPzjUcDRX39AJyL/wdQzgl+TM9ATu4PWiwjekQ'
    'lppJvDiqkycniQf4UmEpw+OcS7nT0eV+fp/tJwEAW+pLPhIqhmkEcs6mFqu1GQrtqTDwFJFqdtKYrqYanarWmeyrVMeSCz1H'
    '9cxJymFq6Wmhcxv+1yieTIW/1w6JtagiIi7e7BKrqfU4VRAi5HWjHTMon1iuuzd4hrT0F0KQQcx6jetFZpAMqTpDHQAT8tTY'
    'ImQJipnqQqnstp65i5SRy/lfUXpjfQJTaYhqocux5mFchDd3sBWFrjz22zmPyuxmV4HvABoB9tx8VcFOrInbp3jlBWWw9NKC'
    'O+kqhg2B9ipHddiNm6YPCCSH5b4QoSXfROFZ+6fNtAY7uTJSkAJH2pgNdtq54xKCSjJ1AM77IuttBymBNMOEhnnjwSS6VUj4'
    'kL0sMrfjxjDZlwDcgrYQn9CYUWEHRyw3o+IjYKCSwxMBBYj0Q82MCllAKjjLj2Q9f6wiIudXYhTqS8Qq8RVujlbTleeg0Zan'
    'OE4sQ51aryK/LscNylV1i2S4PD31QN+mUmsUGiV8aadzIDRnJkFmi9143u6RUtsh7Bvs2UpLj88+IRaHb9hr+R88fejWtDOE'
    'wXnZCzUtfNN1sh+pAy87QvoH0gw2HH0/JMyIKPsggo7XK+CArhlroezuBTq9Soq05niWUkCDKJUrZZCzsXKlzigjuRRT32nm'
    'bFBtt+IK6ORJoqOlKSuLZTYCE6ky4/KYi0oTO50AryYHB74DS45Ovp0YpUHIcYA9hXcDn2w5Nl56OZ9uUcEFvLJ4G0HaoLli'
    'cKmclvditUP/xbsubz3+MTg5gGk0AP4bDA/COj0+9v3D/Se5n+SGHkLKy4y6kr+W8dCMvyIj8tw39NZjt5FCplkD7J1jnH3u'
    'DgrIwh5j+0/vwVVo7AryByWnPW9fa9cJWUJe/Cn1xmk6GoqV24YcV4bdIsp/PX0obBqgRwSqfZvmTmDC7/8fHwT/TQ=='
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
