"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vXFlu/C967gd3t+yx86axe9fGaixDltPYDITBALtBgGDzMMlbkP8eW1J/XRaLRfJcyfb6aXrk7nvP9yGLxeKv/3v2'
    '77//8Y+//3H2L7+efbj4+PHsdnH2H7//19/++/MfPn/8x+9//Off/+fz51/P3r673nz+V/rh509//e3i/btfLi7PFmevr7Zn'
    'i6X588e3m82Hs8X57h8+bjZvPv95+3ZzcXO2eD758y+by6v3R3/+cH315tPrm+Mf3P7f4qQX717/5dOHo/fv+/Pr2Xbz8eau'
    'ofsPD30++tm+fcfd997x0IjTt7y/ur55e/fQwyf7noef0vc8NFN99s+f3l2++e3z/958+jIh5MGTb+qtv7x4vdkPEh2ih29+'
    'mYWT53/+h/c3+5l13vOn40XBXnP6xZO5vrjZXHvPf30RDND9F/C47Hqwe+nRcx++xMZlssnQ4w5NL0ytfcHhcWDZ6xNqn7t/'
    'mj8g8kTax3+8+vQw4GA8wgn0x/mw8OxwVObvqHX+OLTmb39q2XHozJ8yII35k8alMo+734LhuO9A7XGH9Tb9U+15dniHrAbW'
    '/dZq2D1kczFwESijMXgN3H9IPA7ZOeF1EK6011eXl5vXN7/9aXN98+7y3b/dNdPeJ6nbv3BtoWaQB+xuuVRDwVvDhgajk2z2'
    'bu+OnKDK5q8fGD9+8uMnX9FPTs/Ej5vLL67b0U6598iwB2h8tBe3Kf9pb4XEJ49v/ls/a1E7yow/dDo0sMPL2+RZM+lH53Y4'
    'XIqVhoLzH7ZdaaF/l+A2xj83wxQe8jv7YPAwgcHHo1Rp4NTeTy2CI6+p8Go7wIUmHAbYtEAeXzBtzgCHDWSeZeEoNUNUeMZ+'
    'hOxv1RECD8UDVL4t/ll+W73qTu68UxRzOfnzx5vri+3Pm+vrv54t1sXLcPJh+KU46np8mouye2Xu3NOjmer2RHLFFgCoLF+p'
    '+r1hG2ePNTwibbdqev227gng99GLeEQHDOyZHSEwiQjrjH1JxUI6LI/S8w4Nc/HvQWamZ3poRoi1FyaYYOuytQeHC0AVGzkB'
    '3TpX34+HjHlIzy5oebzkTJyGS3/c/aPc5V7jkx5hsc3Gfy66aI4j/WX1Xlz/a+ECA4NJroky6JAwccBDQSCt4iRPXWypOQ8H'
    'vLacn2ISdJd73zqp44dvYw/cRr/zMbyW7UDc8/2trEyI7pHbcKg8S1IorNLn7//q3p3cP90ZwzU33yE36d7/eY+uVPeUptf/'
    'KmMcNCAHZCPELljsnj6KxfHUJgLyMB/BXiDsMN9wiI9tjxE2FBHwV6I62PEh7LEBomFW+2BthcN9ub+S7j/0NtH0sSNgHQcV'
    'eQSkO+GKs5jA2OjAm3d/7l+E8w9pBc9gT9mMgDPUbj92775STGGdxxQUWx285uuyDY79kRhAmQGHyLiTPgwxxKLJX3+J6AND'
    'gBisMWrggeM5HP/ocE6QIVO3AvQA0iMM/bYy7syOSZge9jF4IYQPenN99SFYB8S8OjiSV1eXDyc1OMHXO+/v8+315iw27SzY'
    'gF5NvNDVyBj07omZg0M3SbkTun/OfrHpTyYuy+GxBhWbWBYJWrbny4Bck8QCVa5KGzIqeAI4tUeMgJfAl7s9s6SbRskwS+Ez'
    'qyIIcvfjNV6JWhhFDuCsyS59pRMqu2GfBYxQyRGeAfCN+mlWmAe9VyVGDGmpDhGB7Dbf/JjLpgTmnzM6TjfskV9ZXdPDn47A'
    'ArMtOoZasLxOLwt0qOTINzU/g3gt3pyx9TSYY7x7FZoaee0M5Zsi6NS+0puolncC1nPwPriiN6p9AFhUZs2CJeAbzwmTRyEh'
    'A/QzghuZe1GHYcGO2OF74TktxWTrvuHEGpTPkHQ8V0ybWuAdJPDJJEeC4LfSJe7v7mwK7ck2sZ2C4OXRujn8ovB6qVvGwkdf'
    '70Sgwa4AubTiJVJAYcHL5gpEB5P6GAjxcfj64MaMdJoW2FEZGVDm7pRBI4j5yuVDjt2pletOrXSLV3JkDre1HaNOPq3zuuPz'
    'ez+wur2/uh2Qm5s/d8fkj2EHyBpQs7g/IYq8YBwgZF/VFgX3dkwrIZlp5sUh+DzGpBM4axLhwRqNU0N1UOzgcBE5o5BJzlP4'
    'qsAwdn3h3LuCWXTMuJMlrXDmgPUPnIjD28zYu55zvHhYdCK04/aTwbJJEy9EWzg8Z8NFBBw7/zSg/m0mI5ScVD710fVS9sOh'
    'rKfq6QRGH+ytITTN6Q29CNiwHROZSfAwPKhhK+PQ3GB73NcTGvuiuAOzmPjLZ0c2/i/vLv/yBfE3Vv+yHTRpWfQrx+DhFj1z'
    'ByLjXkDLJfMc80UylqlAAZCs4ZlYrSpxALXRXmyVNq2zZiO49cOLcACjpcAMiXy++MCuEEgmy5Yc3nW8M084EYx5Ni6jfA5q'
    'Mh4WdGG5NEIaYGmE/gEIaVRSXwnrO4yDxYC92TIuEyRctK1e7t8BLDWyHgdsFDYEyIeIlqCZh0Gp8NwZDpagoWolRWxsHArk'
    'zYmR2AJUK3mPx6uzp/VoPhw/mrk/42jIcNnPwJQn75/o2syUCLYItG7me+3s8YU5XsT4WC+cYMKBvzjYxZhtEIbQx6ai430H'
    'CZx5uoNkQ7UggsK+NISl7wheaW8MGu/zx7tJAfYo2rp2CCEcZK3/HnNtFNpu+2zdOj+L3bEWtz2f2RpNVmj40NyUxzeV7w5i'
    'YmKXe24jiE5TZX2LOB/JcmvzwmJ/eRcUdEBA3213gOnpJOwAmlUFa1ZNA7slQOuhCD2pYDATbg2E+wNTKDwZgH2MOkvnZzIS'
    'FYFm2CdAu0Z2te+/YiJcyseYTDKRj8SbBX3LLJyHjBToETnZTps4QeXBfnmBzZpXhCPxwuVIKJRJoPHuEGbwn/Xonku3pFAQ'
    'KXgQ8wVTjJIUZAAhTy++CFEWxZ9OuvRk/YO3hciWjCSCo3S/SXxsAncp2hDHc/lST7aYYeWTYOPkm2CgmCkgjlRztUaHMreB'
    'XFrG8b/dLwI+u5UjXMCyfZ5z0K8AYdPQjKSgYHMhajcara0U0zErnhAyIOialNmb++OF4A3ZPtVXpmhJFCLU6W4k5CvHLTKl'
    'G+GMZS4Bnf1Pqcz+ckuwFB4D+bvnE4xIuHxMqE8D/0bidSJFGeJ1FDTREkPPGzRUfi3lEJ0m+oaaksHfsi2bG1iLcj8BqMDQ'
    'AnSDlftEELYZWBXDkScl7UthXpRRPYG36M677roe1sGJg/8VEPgppT7WFi3n+LB1a+c2t2x5DlpK35NyPJwFIk3xItioLQ1X'
    'mBFmJo4b+USYo8J6ZrMb7yMR64i3u22Yzeq0qQOUhU/urdoIhXhXbjcwykxP2CdCBTxJF7zOWuJAKOQqLXiLQ8yjQs2A6USI'
    'xS1/Wky7zmc5hnSPiNs0homdJINYDZ1HY20wF/5pG/GVDgSmx69uO/rPz74xjzdiuRBd6rws9Frg/IM4IJKI5C6y/e3xFK/c'
    'f1nqLvTLW0XeknDwudthh8Elv4xKJUjSagVazqPnFyjM3Kdy+tFEgoicZhTwKPoY2rGydhOOETTY9r873YhaIAnuuGrespeH'
    'V3Y802KpcIAg05fSEHTKMVEa9wpnJGjA3AsYJwmzJTQGOmL26wm5FBDEJJREfYgwLyNT2dZfd1v6YCH7h6yKTGU5su4weQt4'
    'Udw/Hys6RHYF5gRmRU1rlWqsc8qxX6KotSG8lsyZx+OohpJFZ/PUCnGviZ4QGfEAnUn0DSLt4mg183hMiMfsvze9N0igUglB'
    'yqloZIYLWwMAI7mgtshfLlW9rLitC85oDKfRilMXvWi/ESQ4fp8Pcu7I874y+ejr20bWyQpknTz/FjNN5ii91M+r3zpyHun8'
    '+p7ykfrp8cPLX0eShhZuI9DD6BhxN9am1uForLIURJC0jJjAVgWohykokKU66zJj4qmsg41FRgJaAynDPR0k5LowVmgNYRCT'
    'snks0boiFQuVuTYJymsmwgpa4fUFrkr7ncYpzXPU0VlcC63mEn/oAiFEf0r9L6iuqWuRWt1jUuhFxRNCWZgvnd7aHdbxG1yQ'
    'jSWu1VK/hsiYfWOxzqd948gwptUDMwlcp67V+VfkUMkZ+/N5VsBbbyTk+9HLMcV+3McDMyhIGExA50IBly0IFMnUraeq72Ib'
    'zXhdPddr3S//W0yH38a51TU2JldfTv5raWcc56JHYclFNrafGCRlg7CsTsW+fgzlNLszYreMCEgE2Zham1F5GA/o92MOINKo'
    'a79mXDzE8Nvo1MYZbHm+JZnYyfihQG0BsUJFgeXxyvzEABgL47DJq1M9mPJPuGfBN8neach8ip4ldvEUrMVr3qnJu46N15R6'
    'IKIUeyJIKU+DkaD9zQHiY0OmU3BLEelY3i0285lzP6uNJMJCUdizmOjbGsBefu9ccEMuszjr/L4EetYNd/jV98HpnY+zG8cT'
    '16W0Voejm85u1ai5I9TYGn45DTs6fvhcLq+s1Qx8sSx7GAT25nDTU3lhPECad50USWfpti4lIjZGNblzMuVFoJVWWwzr284u'
    'sysDx5opJxYbSCkzUt51XARHwgoyUQ2ZHhnQWfdDD81y+8ci+1ZhPgYJ+AA5ySBMTI6ORCapuhg4L5voL9JDUnW0hEKbxYrx'
    'lJqM5etITdDGqqYDRQPpGusTR21uSzXI8LjshWx4ESaWGHdv/9pYEmBwMzDKpplSM5K68rnE4U04Jyp81in9lZK3cGMtLC0e'
    'rqZVU3Vov4AI59lz6AhD82XM92SsY+N123BLS4nKrm2JlSvQ1sr+7IsGH/alE8tdngMn+dm3GM1N6q8fe6SPEAgew7GFnvDa'
    '/ZdQ4B3+6rlQAbdgaETufOro8++xmnB4JhidYLQJIMHXELLWanTxiCvrTaX8UT20nZDJ1NNstTAgT6iLncOE2XfMRY9g+YA6'
    'GAURBxcgkwrKa0xnlonHAzwJ9RepUrYQUaGeAYpcYu+msI7ayQNRojct+MDOAyFZrub/O2rBcpwer0l3ozFqRUUnR8omRDs0'
    'W4cicdR1gRiKCIsJz2HdhF65N0TcMxOgEAqyKgeRzHXMemYSaC3SgZYzz07iwoICwDgeXHBd6fwEys8aRk8RKi/HJAUENSnn'
    'kaLCpNXBtbsFLBaRTZ/jiiAxIMCjTy8yJgVGtr8g28FkILdK5Wo3phTMkqRuFou67WZPJkGGdVYqFr9YAZxgQoAFprBZhOIr'
    'TWZQKnv+UMAlOr6z6uFEyPwOkVstRSHzMfXNn1i1/CRN3CqZA/Rs9U2XLnwE2KsjcC4nQgzK+83W4PYcnGL6r6JOFXg1283T'
    '6ToDtSOBW7jtRfyXJXlyQaOHZHMU8kSHiB7oelJoKfXK3QEqsmvlUYoUyS5+rAW6pUQE6lM3mD5SUFJYmBKzPkFEYyQFdsKI'
    'NLWxtcYjfajYB6TIW2WwmIHvI4C8hn2JWqKybihToSAhoTiK4J3hVJFLA3YwRkjYUg/0KRk5Z6YxI3ZGYpkXh8raoTzfB4Pz'
    '1gM48i4HeOsRL5aclRM0JL0BWWNkVplvILGhK+I3rMVU/87XX1ek+YpjyPIWZCn2DA/MNgZCDAqPg38/ZHm8KrE8TrxSS615'
    'ZVke6++D5HGiTP7x7WbzgWmTr55amxxBZi51o6L1DanaHb7ZdjOGYtGU4Moiy8MJIdYGyAmOE35qkfCxHuQagQ7JQuS5aESF'
    'CFLMW42gUjERtBRZzNYAwIkGimfNCxUNrQvgaByzLOVc7nxHgiBfLSCfFgAs8rgi/By8LYargIlTZbdmqh/APYeUzGMyWjhE'
    'HxIve8HZ56dJqSQW49tT8W4LZ7JwZCjp2gfpqAZ9SkO9TM+psIvY9Am66kJuSBvJQAiLppaP9tmI3HkNdwlBDQz0BWZsJ69e'
    'GmUokyCcBIgX3c+5FwuYwxECGNdm3NguGl1Q9MdZ+Y9QtnxQ02m9O6WiXh/1GNQTxamHS0Gpc1/gIbxyNOOhwkO5l0xO3tNC'
    'PNGZt2SB40Y9CcQyNH2GMwdWA5gDvhZhKYGGHrduGoqTFZOLtM9RaV1BilIKFTPyGQAkkyb9Ss19Snl9WuE1q3oBLDf2i9no'
    'Ebo6H5qzXVVjCqHwLP8+iwImHwtZMno+ENEIQB71blSU/OWi7qOUVuNAvIoPxRQw6nPYEo/kBA5WpmwjgX+1bPPQZSWDnA+G'
    '+5qAgapSyHagSou5cns4yirkReCTUpkXXhTbNjo89YiUJsfadnu/VCUqVSIrl3JGE/xIil1/9IFOEDEbAmGgfHJmRe+0ck+S'
    'E5mcTbT67zazBRiApQ3eRkGVxQp9Qh5RVYJWmn/drKFpQQHPqjYvQeS1yHED5rM0Usr9npkeASwPi97SEJ8UfUlNArtLU9ua'
    'FlpREPdB+wAc8dB8ookjrDqjha4qNLPIIwxXvyV25VRHR5eXkQo3pj7cQ2whCWh53ucRPTPYFpSLWX7TWTBNAZnz57MCYoNL'
    'iXD063lRL2aOCGu+9ghzdljIvFKp2jI2E5XStdsvX/RiRJ6C7o8Tv+/AGVUqhUc8GPrNWZVk9MTLOEy9aZU6jsaIyNIdTvDN'
    '5dV7oCK2VeiCgS2WZlNpNtNQmRmS0x1vUaiiSOtsVBgKqXmTdGmAi20hNaZLoHh0juVcIPudDwLmETOqKwEF/nQId5oRBGuD'
    'WG4Pc7wUaumyqyzG+0LEEEoJ+ydVLCCXKGXjX87eJQm5uDGeMZmSqMBkuBW1+jy+kCaJ+YlgBDuKRvfIgSOIYBzoBF2OCl7R'
    'qP6UE1xS0oVjytJ+8nMrlbPGU4Lj3lRHGQPaapNMPSovK+ePBv2ZtoQT+Dx0mefVBnHbpExf7IGAFZuko8KvMyuMtBcbg/UF'
    'KqSvASlg5coV1PgC7SfuhmYE9JkgNFo6BZharmFg0bptPtDJdeAD4loWZM/BkYV0RFZIfH9GWX4b7UcgsQkpdJSibA8/TEs7'
    'v030jhARQyF5+M2TLwgCR4hnDvppj4lOdeMT5t4JcnoCe+4Nc4N7rn7IZDcyKl9fbR/odvD0yBeOstDmcTaoUOS4QoCDthNs'
    'PIfuoKilB/guO4y4ETzEKCmMEtg0mttwLSVejyqFqy64cERk2yT20jgxJj9DNTLmRDvQE0oaXhaLkEdClmYEMGt60i0KJjwx'
    'aNEvPZNxxzTa/Vesp9OoVqfUAAuJPHbUf/707vLNb59vtptPD1O7p5V2q8NIx4ZSvAaTQl9v9hdPRvF1SFHrtjIWFqLKiH85'
    'OUYUU5EPTiVXiLKnoj0VAFsM6zB7MPSnHszpo7bbVc9LvHFvb/9Hy8hmbr8zG5NiMoHNt5x66nfb4ovJR6Fxp8e7DgBXwmdh'
    'ayyzqGNboeohXvIomE9BGUEKXyro3sv3Z9YZEEVkPFpWWKuhlQWSoGkVwZJcohT8oGX5EkydZ3rKWnTEU0l8Ua+eC+yz7IYC'
    '6c4uPL1WZFQz42Qu3DOkodOgqk7k+JtSPwHQRg+QjVR4MK0oE+ioGeiIXKFAtitm7NGcUclXR/iVVAkQtCmlDtalGLq7mg3k'
    'HGXWX7SJhusXNIn2BIP7ZvG2Oequr8fnzGrYzRC6H3VKvYOc8+NG5NbxiE8SFhsiqlMg5dWRH9Vw1nxSAOXobqisQkaTnhsD'
    'r6xiFHUMQl4R4X7sguaRbMoU2mjiqMPXMWSCEN8pKJ5DMvDqmdOJquyplPCYlTc481th+EWxaP0oqaPCoiC4DqFSZ4no7cqH'
    'BLhLWdA+WMV6izK3HEkgF/TLia846wGhZfMbRlp08LKqkCq7PHHjJeqyqTnJiKPVSzzm3qfDz6ScsRLdKYo0BlkkUemAnuS3'
    'JCvp78EkeTNsmKpmLwrD1W7/VcvvKu4D8sTQlGr6hVIbCqtseCNEt3656icQWr9+ufonSRYM/Przol//vMqT8Z9GdCpZrGmI'
    'umrdm/adFdb6QaBBzg6RExwpSYaPxxNU/FKwBsnhCa6ciFgZU4WYeQOZt+SCpFBDGBE6JWZUZiuxlySxh2pCY2X+lAButfKp'
    'xOuIuE5qtlF2Fc9Qm10pvCwqszDJtkiQwQvoRPO3GgNQpMxtQvNCbgpDv5LU/1LtC5vEQAPwkc6vn59j1/rQ3SdHPl0ZpRif'
    'ypa9nyz58fszy5oMylQK/L2FlsTWLpBmmHho71gGYijjgIRncmdKAr7fKpcTIf8Vk/cD0M9dDbmaABrCRSt3BJluKq2xeprI'
    'LBcGgMmYmSWyMPRVPzqY/hotiZhIf1VFSe2H2hlBlhs6B0TWfYB802Cbd+gNX3WSJgLtsCU7WdMLsDd4pmcFUyLHeoTApdLr'
    'QWdsj43TVMQ6CRGKKnRtfEIPdV1sDmWl/axcZohmEoEw/KDpv8XkxJeO9P5y2ci9e+Wl3iF5sZffT6HCPP9nWcQJ1zSDbC1I'
    '5vPihl76Weo6FLXqYwHY4ITMt0zCJelZz8xAoVRQ0XISGN45jhD6dhROLeCpmSpgBVaQp+81VWXvFSaMDAgq/1uoVyhxRtx1'
    'mEZorACAaNHpTqBIjMrJsQvpO3pmms9H8g+z9EgDRzxBYckgYaI7WKpIL6WSFGCisu4yJIAnawpW4XLjWSZQ8RHrJ+Q/0Bwa'
    'm5mmnWWjSqWyog7+jpRqdPhqaAMgbCVOKG5GIFm2UYoasuJUdzlv51KehC5wqSe4gMJGxwoHnAoe8heE+4vVA0EZiYx1xJao'
    'os65S0DUdE6YPJuITsAxx9wqPTss3vCaVJ5Su4Whzf5UCetmIZnaNn+XLacgw4EKD0hiU9CffuE47+uUBmyACtPcXV9IFSyv'
    'AmKgCGbSmLXviwXeB8JrmggkC8BwJh9DkbTKkcGqOq04Vyqk+IAe/OTM5EtwM31f+ko1BIgzxc5bCkprTQCJAe+jo94i7Utr'
    '6yA9oZbyUb2BXyeBiwHnIoGrWwJLpfgX9DrrmW65jMeqR8kMBTUqK6TGBeZnJsGEcy9p/J/qU2/bzCpJpzhRmUiLZ+bkEWJg'
    'dBQFiqmIktSjJizNot9q/k7EqmDS3p3am0Vpean2G/U6yxxJdUcwxbt0qQdVK68MgtIDI2IlKJ+HUQyUVEE9j4rt5p5WUixh'
    '2Mk45ACDTg8zlAXByGuUmxWBIIVpwyMECpglXxW0sgOgCvCqehppY5rzk9FwAqIlRdTK4cEC6es+CdSaEkcq1WGwF28ECb6u'
    'i+dZt1gGCvy+CSxOh2TgkHfSpumofDB8DJFEu0fM7RP4Ta72j5L3tygtoByXaHeTLLH0zzct8zMduDnVf1oFAgVV7FLBPMkX'
    '9qEcrivMzP1Rpj1simDSgLbdWSnzqv5sYrVakDpCS75Gp/BQ5R8WAQ3NmhR5vi/8w8VxEmLNPOe+4qoy7VSe7UZFv1py19Ei'
    '9q2jSpU+PXkG7Ep0F94WBCxZyT0bs4yDn0IrF8NLXyLOTgrlYPFwHxsoMowC5I3SPryTZExgwzD9yxqz7HLKL2Qp2iFswZjH'
    'h04edffNXSghJ9ZFsjZylVi1Ti4zBBYdlBTokCKzo1HOQWFq1HJQwP0K4IFcBCpDRWepY0IGctqNR7UM3YIQCYmvICVL5Qqs'
    'MkwTBbS0dyrZlpMsmRH3PYckq/RQCZwNdYNJDn3K9+WAX9gMRGNRcppyTUurKMdyRc8MFvHKy34CiUrfPm4xCzkFZAXmqSmM'
    'AxDKIWocYy1grRVdbmhGhpZKEKMGDfRbP4dHRxNVKJyiEgQaKTqaKUJC6jQxivEDhtWKUlCrepliLgbQqSenO5qU+EWnqx8A'
    '1KrT6THKnFBVKhFRwyhDmeQEPwWF5O1+SKGQVLhUgXXTCw7pjBetNqU8U2MtBmpUPGVHUurqLUVawl1jQg5J4QozJmksn5V6'
    '1iWXSXXkiNAR+5S+d5lqkcTwSt7KPASjJR/YTIropBXTFv0FGqXguDlT1Lflyfts+PdEjDCAUBAjm3Rw+Szj5TpxcETDYOIa'
    'KnUhbFmYi2SIHiphrX7TgKg7hAYt9QSrK8mFgiyKC5qilhsHzauXLCqk8gB2wPlznBQCNuNPT+Z0C/ky82SKhMW5UA1CQeBj'
    '5f6ReqFUu0IB24BzFhf5YDRs6kgIEdamNGeQScazShKRMe7UIgEPD1YXsnKoV98YTOq4oAHS1T+qZPAOx1Jg/VEqTME+LxSR'
    '5gkWnUJQQuQ5ojxvxUALdo6YGSQ3UfG+w3x3ZvclzI8KH94vEqiFqXrYAGN8q0dQnJDOZBumjsZdgOiohYD/DG8ZXcmgLcpA'
    'PSU2yLpuCmceEdnF3PQjb5uZDUomRiaVEERGOQBAg9JCXcQU9TfiqR+RJXaLNKK5B3l9tSVHW775mCg5GvmUrUFU5Ss50bsE'
    'tNhmmcbErlUUfi0MDpGIlJpRTGIcPhyVSPj40Sh451MEjhkjP9nYs6e8WdXD9HxfpsjC9HY10UL+bojnMlYT54i7BfdSOGno'
    'dNI6Lf5FkWoEQ83FHK3E+/E80KLvcGSEe7sH+Sn9DFjuirdaIoHJ7dSZprQdrLxkvl19gCEmv+uZn0KsVK0RqIWO0QZu75ut'
    'nBeg5/9WoIEwsTmcRCXqWEMrIicraG+pPqpKAqAhOKG9FPirelMhBBbqN4SAULVp9DqU6zHQRvZHjV7VA0eqCB/v3T2glBYN'
    'oZasZxTWPZm489tEDgazq/ddgckApx0mTusLFvuZ9GkVR5mZ3b9vFHBtc7m1Nui1a+JzOa5sXSrTPPLBriil3UGCrhLQGVub'
    'M/K9bv8ft7Eg1Q=='
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
