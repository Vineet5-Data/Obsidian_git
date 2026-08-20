"""Loss opponent 90716409."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vHMmR/C985gPngxR1b1xpfBLMFQWK8sBeEIsF7IMBw/ewd28H//fTisPuns7IyMis6pG08ttgyOmuyqquzoyMjPzp/87+'
    '65df//m3X8/+46ez9zcfPpw9np/9/Zf//uv/fPri08d//vLrP/72v58+/3T25u397tNftQ8/fPzzzzfv3v54c3t2fvbhzW73/ux8'
    'bf7w6m4/+frDbvf605f7N7ubh7PzF7Ovf9zd3r07O1+tHx//dX406rev/vjx/eRqw/h/OtvvPjx8Hs+7u/uHN58/HSY5+d10eE8/'
    'OJ74b4N4f3/3+uOrh3F4Zhg/fHx7+/rnT1d/+PjZBpNRjDdnwxguPP7fdBzzWd/evNodJq3fzPyR3OFgu8ml51OEt3D/idyK2G5Y'
    'wU8Tfjfa/9iEB1s8LWSj/Z7v87TfPu+Jm4fd/fEd//DbnpyO6vDfKXOO1x0n+XyDVzcH4x3+qZPxxkkNdxr+x279cAZ2TYCt7IaY'
    '/Yyv0tENROvZDRGb8fl6SfMNO6HBfHSrDTtB32rz64pWG3dCF2PhB3U+4chq83eSaLXJV7rZzK06WQvMwbeI+dPk4SoYCxjEt5Hw'
    'QJKpmA+dTGQ/OEbrNu6ZrbqN+/jD6S97OEscBw/6ORvX3Rr+IXU94zcdDtCma8yP1i81joJ9zTWeXarfxWR2N+0L02Mcr+5ub3ev'
    'Hn7+w+7+4e3t278cv7wqV/xw97F9mfoP6/X93ftln6YPu9vfQrfJkMcIbpENEZ5Aq8brfTVPHDN8eedk9m2vm4CYNrmbVIyhsLoc'
    'FYgjx/lKTy8zOuv69ebn29H10AoYDwuadHw4HEutHsMAZRwI8H+tT9dwb2vU0QmzRu067Sb7x0ZIHI45iCA2QubWJKArrX2vaYOw'
    '5TudNzhJFpq4GxF1uvfcCYDTHT48/fdyt/4OZs1f5EosvJgNyK1/nyYohPZf6537Xv9butrMv91m/Nut6t9yR3eLs2mKZ6UkxQ4X'
    'U1BH5kCBW8xvL0RKKVc1ecs2cx1lkWre/hwl7W0rFAAxt3L2t8otrRHtjEBOEh60VSee3LEwxcybjL3W6zckNg0h+B6wm3i/lqhw'
    '0/GlnXiRJQZk0JMvMIavziggsfnd2wQcuv82Sq+s1lc5hG86MbjUZeVcoecnO2//Lh70pUc86+NBTwO03j405XEt5EQPTJcmJ5pQ'
    'nRqmArzqGEJcznp2kiNNSHGQEuA4o441oOSCOyjFLcJ0N4sB5MPf3tzc/0l1hDcCUnpw/vnUdVLNMDx4DxTPzjd3lXdohz+ORaG0'
    'WdNMf48DZswYJHdBvpS5zGAuKcoTwHBmpPn6Z/Kt41fTT+DS0aAJlI1ohDiTJTCzCAXz+X7TRbczgU9fZgUIo9BL0MnPnrXi0RNg'
    'DTmuWWy70AM3EwM74kDpGP6W2xLDBMCV53MKT2mYrU/Ome5+ZznjmacR2edXzKUzr41fzoBxVoOcmgel4DAVgMTUq+DpIqmBoSVK'
    'DTOMGtzYOTXONBlS+IkH+qUGZtNa4cCSNq8Y0K2HCIfrYmINB2Nywh4C1XI0V0Pm7+UnLaH9ZXtoD3991Td03/SP2E8Wp3dLcdlX'
    'xKJBeR8DsQlV7MPGjQzUkYxGkJPOjKBcoNiVnZGjYdkVPN2049XeJDIndtoMRNLPkE0uCaw8jBlURCHOJUIXPworDlDhGjWxt7L+'
    'ix1rMlzLoA72gkqErsd1zeawtiYrt28dOLm2Yhc72Ig0XDXL3D25DGPcu7vbzxXzOMS9mnxfcb9ub969zhf7x4HbvJ4f+zvIXRDd'
    'xJezxM+Hh/ub/Q+7+/s/n51fx29kWgbvZ3+WS9vMWUjj+etLHCTFALwwFl9vPBoz91AsPV4Z/O15IEMGZPY/S1vbqzr3ga3wtcPs'
    'Plx8nplDWYjJHm9dA1Dugt7VfWmzwIEBlgBJk8ESC/PIkaGPBsI283wGnUYpRjKefMbxyRZspBZuttl0wzoOH+YJ1CAL0+CUy0sL'
    'KpTQESiA61vC8k0sqbUaOoizC5kYHMNERjcLWxOMWVjXS8LuKCZj3FVGn0avVwjGE4MFDjx5qU7NN44oPko6Wg/t/NCi85ih01gJ'
    'IdFk74p8r577zo6tiYpWM0eTrIQ6Q1Jrpd+NUSvl0OtEHLarElONC6FNo5VtIpyaHufwBS8KkTXg86uL+I0xSmvZMn888OQnIQq4'
    'fhQzp86dhjkAf7RtZC8f9QAB3WkYNv2vCj8us7RGPm3+htjNHRkwti6DJAsLghu7rnY0gfsijouKDLBYEimGedYF5LmFFpx7nyE9'
    'KTK0nDm6yL6ceYTLkA93wJ32KSRfTdybHXe3Mcupi00Bmm0eeMR4cohXjgxaWHWkneyQewlWfeIp+Ww0jVkpDNP4cISF5zw66MR0'
    'RQVwprSUZAFbkGVjKYu4QG7VCIHCKQoW1f6tLQ3FNfkQI7cyAjlBYZ8ryOuURD8rw4IhpH9Xqd6yawaHUcylkKo5D5a8MRtLCD3P'
    'pcT4dd2dCW/+dG0YPv349vaPgMkDz+l+AyJhNWW75owUhackFUkG6Fgsny48vNA3paCVi3pPg9YXTj5ylQ9m12owu2oKZp8+1Ahg'
    'VlChJYadXy71bpxpFeP4KheyFpOHsxqlAOjvNxKSabD5kOcEnxYzOzmT8Uq1pQLulB4r0QEXqMt22chC+okaPyopkLZtKB7bBxSN'
    'yaFyBZ+kt+ZRJFnUio8FdoRdwjCVKeaZ8x6PlrDMLLCejGA52HAXoqoWH09TvddmfxE9g7vcw9gInxN8UmOQLCJ8LeymcJOFzlpq'
    'hNC/RRx1Vw19idWL4DFpmTqvZZMGS69BEL9/uTHMiH3b5QQ/epmpRRrmVHv4+7RKs4x/NkZUommW9VCivA368lIP+DDAvc5EfpZ7'
    'idOXIDWyEDuUOZrDKGg6s2E4ihIIy072pc5KIhY2SrbfcBpyeaWssz9YxK6UzLmscgU5n9eulZWO8LMeSxRIQaAc7HUxg9iTqooM'
    'CDxJtLa+GEcDxxH4UHRg9LRKEfY2/fTL+MLbsBb+v7Q/ExRIFoNRkI0hPn0ppHJBDDphwAGAOHVduYfiA8Uyj/CQ6jpIVUgEfbK8'
    'EpAVX2yc/AAfRwJ8BIZFzcd4pZdtazomaIhBUnf2gQ83+dgEPAyEEI2HFR43S5MN7VDPo7BQlCCK8FOuzRLv2fihBvtKXtC5So5k'
    'vWkF3FMWTXlT2ptHCb7c18NUWM4PTOD5q0TlTFgR2w2ikXCzJH23Z63kwXqbCydWfVlKimolklGHYwA2IVIvrz2Ef0XHYJWuPE3x'
    'rsOmXduA9Du1EYLUhQgx5DXWecyC0IhXhOgjtswLYBNnEfVCYfO0mMeveWSRqjQhNP/KjATRB8tNBtakC8OCt/RE9O0VsX1BPj2u'
    'Zwv4T2BefjFcH/F5Smek9XdISJO1EA4ywY5tJDe9SZZkWEhW+azTqGlAQjL2o81MRR9osdy1eHW61WenTrRqIQHdukT0hKrVO2fA'
    'Dx/nIk/0vLG2nBUffyhXDxCl0gZwAnirAPqMmesqlZfacKFKVEA4VTkY+oamZO/wgPfhlU4hviYseV4sy2XRBo7TdQJQXzvosjqM'
    'OiTR6cGzrhNpMlqxL9zpv3isEvijB8PrCZ8hSFBStVYf0WCK+Qwcd1t9GCT6hU7kIvaNsbTMhrD1EuEuFbSyKHNmnFME2UoEdgvN'
    '5M3AEzTRWtU5Qoww5gE3nVYeV2IVXwo5FtJo2hF7yx8zEUN/07Qj9CJ76bmI257KhW1y7QSYvl7xQnXD8xtdqhhZgGQEwP/cXu08'
    '8FRH1tSHhLbEIjoMLsZ/5dWfXHRRa0gXsVwWwVvLMCqp4a22lcp9CdHqTWWyoNc4DFRrLhcBVREJ+5IE6VKfPNEHjGWLY4lEBerS'
    'urIyERzpKjp0XpnQe2Q6Dy2km8zK2X0UcFpasKbLsghCzhuLLd8ApV7pkJKmn66VT5HGMjrolZK/ZsonNc20tW466JMzFRQbPoCG'
    'UJ2sxjQRfCJpTmWCP2GJZcw9OkwmI9P8y3p3Y6aV+fYI/yuW0g/vA59hAPAs/TFbNcWRyqAS9m4RyeZbNc4RNghRQ+KX8kiERIU8'
    '2UPFJGmg3XVLUGEF/rJKagcQa81IQUyRRoUgPrPFrh87tOZJR4RsDanN0rweG+DNjo9tLuhLR3ebfHS3ipvR9JAryAZ1WXpJk9Qa'
    'JUb3IlGw8M1mHVvvr6wACEuomO9efz9I9jdvAWr9zKtRsT4s9rZ7w4Oma7bXSvKJ/1VtYkrT2eQrl6HQLENFB5LkPmT6u5DbUt3v'
    'nayEIOnoM2ZR4/RZATraWgAmBgZgWs8luS2/lCNUOSwcAJSOwR84YrNCz8xzeSyUAdgeHzAt9/7yILQwQGuq4PZZ6NGZR9KUwQ2n'
    'C6PRqQikIbQuxriAmQBFQZP55ZBcD5vJymfFKpSE8CAMBkmSe7rB8sFPY4+nsI/xU1z30ktp2fKgmiS5kDXqqNa2juv428TYpoHW'
    '3OVfrAOlW3bfp7Ce1ujOook+iac4c5Ix6rqG23sV8n3SSKwagNq0Y4E7raPgu7dMP0Ylt376YZ70XK6WmkQjqVYsnTruMFN0pUXT'
    'ggjmusa7oqmxCgBOrOcab4oEYZbJZgRBekNS8eoxo3xNy2vjFUkMQypPdXVFluNsovhV1QbRbiqVtdp79mtFqnPoS5FYWG4N3kiE'
    'lfrk/K3rbZ1y/jj/HR2hKA6MALXIZIDwWQBOQrkBseCiZxhgSpWtUX+POY7lkh1i2iPPwYPjbc6NIKBaVSlO5BBaUygnGmZrpkXq'
    'ZBuQ2RZPyKi5CQZh91lxelfmhWSQxSWTO6oHSaGzU+SAiGNDl2Ung6DteaIOtcYnSCexWQEfS4rvuuecsqak5Usds1OenlLwlFMt'
    'pNCcgUIyzdbwHDpLp/iJuL5pnnQujLY0HdhCkkCXLn3EjiTwiLBiF1qmlEhiYTifDC9RTkitjRuXzSbahStIM7+ayjywsWWUCRVs'
    'OiAEtjGkGUrNwZIKUdntoif6ZGUUaTZLKLJLmyAXzIOHt8dUuGJitNJA8I0UxC3QGFjm2zYInjWQLZtbW+UL7j6fEas1zUWevrxu'
    'LahxS7/ZtgqJbx+7ZC3XYeHb0kriNBY+ahr4PPTpRrh0pjf9n81ySVGLSlhvKTCgLSdtzu0RkRuItkkkQDXbR5YaQDd2qAohs8Ma'
    'OqchGc/wn/MocPh6+awtVUymQEVcytVR9Tn0gRDeJJCUl0894qgXxB7Hu2H6M3FDZMZLasFsZQ3w64nKl+m8ysecC5j4J6q0t28Q'
    '+t8kqvsw5Y8xJo9XHn7fWulH+lTXELQq+kXAwlwLhASD2AGeQBcL7wnU04SZsj8jnAQLKrOloQLRWAaAKPgUs0ltbF0OuCAoB3lG'
    '0zU0v8o1zVKWJZatA6MMOwxvkuciHRhrNpxM/VojMS5FaBtfySxjG7llRISPIBEriUTdU+v7qPQPRKpLlwRuO6XL119jupx/gjD0'
    'MilxJ66M88y9s6Pm7ZttKDxBuNCcVgukwplbRROofdLeLm3O7TdFqbEnSHMH3T+0+KiS19beS7SnTxQXd0pjkx48jtxyIoUJPHKl'
    'Xg2PIOzcs2towUwrKnc0aULLiFKuIGO6a73KCtZKvtcJpsI91Cn7GeI/tLqysqYV3XU0Xpwhq+w7qe8yGAt6zavWDn3uq9jxCCJJ'
    'fmiF48+1KNIztFqNPl5nIrSaD2J0IjFntpHmIuzFmH3C88lMvUeUMvKW6lD5LWbGYfMNSZlxq2M5bb7TS9IFThCBSvCMBU9qS4fk'
    'CBNp4nksTC+w6y1YXM/a13K/VhDoqIFTp2ywp7X6wrnv1SmY6uUS1AX56XJ761ziN85llpPXbTWvcQp4LaWJW3tEl2pAk5E8Rb+i'
    'qfcu1d25/XHjNtdiXUTnFDTrR0yhIMqpXKi9uUQ4CFQpySuUio0sVHVsdgxKUipSHb5zfKIcN6/rAGltOTLz0iN9GwexmkfwYLLE'
    'AfNY3Xxlp2mAIIWcsbwkw4v+GAN48UUB+4fJmKFtabMiDo1BoFn06jsid+UVyzwEumcg+6lNqq59hQ6HY/ODWk9P2rVdkyZdchxL'
    'JrnNJ/riIlKTT/A7ZtUCQ1dvvU1tGnKLCoNleV+K9rMaJdTmLhMkHsqH13GfbLiD4UZLNB0T/aTclLx4xi5AFG9TmUhZ0Sq/c1qz'
    '9eChKpXxB7VduT2XELZgDZyIcvLwobZxpjDFdjHV5PjAm35oPnXS3IljK2QJ/Urdwb/5E3GJ/GIQDsxni8oD2eK0BrSAZLfsU07i'
    'b/rKbBlxpvkL3KtZTgZ5Zy7UMZ2xNo651aAwBNMlTgfTZJNYwTrQCv1Mb5YmyEZqBIXz9hH+5CJRnZp9syCa6t+lWEll3nqTaJ2U'
    'VcVRcX5Z+haNAO07TYmAzhn8VwlyatLPk9BuGDLDRdF4CydoIK4WcujU8riOYbGe4LxinEW+wS+TK/Q5DD7iCxc6fVuIXY+E4+OB'
    'rpzfRTysC74W2rbqgBB9IUXaCvhbRpBTnIWtgIGGFDe3AoHzT7o0OyKZ9AjzKIatAJ6L1g5bkChnKMDUtk+6muO9YEVpP4DUPOwa'
    'HjO7O6yhZZ+4YkYJ1l9JPSREEXVRx4LCiy4PKfSaboDHtdTbLtbcyDKDGA709J+ULipDgGTI3rbRoberZmbS9GqrK7Ape8hUeJVF'
    'p9DWXJ8Y7PI5LLwY50pl+FBylLmihP2tCuYov2mIuINI4gpKgDbNNLAqOYooVQoNsPvUlVVmYnexJRc5zFYABMWV5vU2enWEjrGk'
    'eDkVCiZA3Vgo5tUHrGNlYXaTxbLnXGB136Vb8Tax4TxuQQREQu/5+BI6G1pSC20JfwOviPN9dorgJMWhstqtXVsUsB1METVWssCW'
    'zsIfy2n9w64TgATHhUO9n8RBpCiLomWWVDlJUXQ1WlY7dqIjkivxIwIqtAKMRSVaUSx/EEm3YkFDR6//ilbo+Hfxe7vW9hS9lYN6'
    'GbsD3CmW+3XqhYRMyIjiixBJ2AWvPCq4nCjRBEBCrAXmFpdHm2evlaEDLLNqeHamUHPHzFkIfhQ0cAIYVeNMCZLR4eDnJupR2es5'
    '/BLHKwSikv9O4UhbQ6pXqAc0WaJ3wFmT0HEtK+YUFs3iUd4DTUA3GRjLaCSR1SD8N1taWlSWlVE/fbXU7MT2sU8vTHDp9YWDx11W'
    'GWy0VnIRBtv6izPYylV66zDDkKyC69hVh5ZTaqww4atuLXUs3MGlBLg6PFYTWqDFDtBAFWVh6Lbp3GMH7ICQ96ENtKVXCHJk7DZQ'
    'zan0Uq8teyCoCFErbtIIkVSiYEYsg5aVG3hHAjj474k9kS5bkllLpHl9CMmkNrEYjbLJxMSB4D8of0Df3uixdiSEJct7gIOmQS51'
    'tYi1eiPWtvwERqXJZZkaWtYaxZPRI0jEglKSyqRLaIPYEiejiGMPi5z045jS+hkRJmtm46EDjjR/juHzEFbtSdUA2kQTAJtdEhvN'
    'gc5OiqqRhKyQ7uU/7m7v3h1HVCDGco5SVdsp0FHyVLEUPacozg3D1Os4pLDlZfD1a/9t3rYXf+X+jS3YeuuEqptVdpmEGu0IKgCw'
    'i5r+d73rlMuPSoJwZj8ATSS2nyiB3CxNnWO5JTzcYSaK40KwqHipiqJSHuV1S1K0y3G6NifhdG2+TvhnlWC5+Mwl1p2pF03rshM6'
    'JOhL+3/5amlctB6OmCXP40psoz68LqkqTvFV0yyuVBnCYxfkCszRcXZZ/RNcNz9t33Xb+VQtjyGidc71a81qRVmbx6Yu1MkiUspe'
    'omFujb6W4TTRPtVMwteDQFTZ5AZe0+VjW+NrKPMGY0mq90Q6QfXZpS+ECgutGbWs8p3mQMXreJ3Yp9I6qiBLvLo+XMIXEM7m+jHR'
    '6IlzbqLCVPrJZdSFzMJqz+6GbsHxKRI/eDUanXbeSZQQKS8jgLClRglBEXriDGelTQHpI44WUT9yqQ053EmqBBx7FuxD1kU1zdvb'
    'Yb0XU3ekDoefvNAfFIW5wk9gP50SzZfhMTS9OUMxr9OyZjLiCH+EExjeqrO5CcUK3cp/9SZfOjOKvFGhilzq0ZMobtr5pDWTdMEz'
    'O/5KgiC3LuFycG9IbyyXnGacZtg8tsqVHS69ufC4WxdCbuO6A3p4eRKUsLPMmQh4tsufaeSwMjrYhPwBzTMKCPkAV7byr4kpZov/'
    'gk5S9QrFpu1ARNFDHkLbOHMdBkNJM4YSZJXcS+ywwAGxeA22LymNzDANNKYYYgjG/lPg0LMSKjl0ZcQxugXZQylz8rwplLv7yu2o'
    'AjcIiLpq4kJxlW+87uAxev32Pz1PkovLgLnpsQ4p5tX1pO0aJxQSo3RzhtSp9oXW2ijW7V95BT6vP3v+EnxIDVCo8GRZq2tvXAE1'
    'JtgiYvDVpY05M//zEoUzwweSz7Mqykc7wBCbCy8LzIVjnKCRBVPxGR/MNV4JoeaooGjP8ClRi4oRw06rnQ6YWRVmqiX7NbZxc/h4'
    '1tsNUCiwIEAADZ9GtZZ0R8JML1uYakypLSLC9+23F3uVz8dj+CIfCZDG5+FbrGXA8xdZLAr/wiAqL5l4Uju0slqraluMb7ac8la3'
    'roGk2xgEHbbuXy5baVtr3qnwpOpathgqTdtafxWaVCTMZx2lutCy2qayqegt73OlBrQ7kLKX+7CwIA5EVbK0zoRUJI2r9jbrapFe'
    'f4zlQysTBQXw5ZW1Uq0UZdYO2cFB1Vla6VtWzdJ6pe9zrdVpM2fGB1Tnu2qjmTGgNYrtJC1+YaOum7hJiSbViOYoKXAkFdJqhDqt'
    'ZoE9mKlugHh1GSqu9HxXSXQ5aS2n2ASFgAfHXmz1IO3XeA+ycCKyeI4dc1zJxmAhNU/sBLsW0WQDdThMFP0GCjEUzlWE3hJH6uoi'
    'QxV0JsggSX4CZUmDmR0acAY9vgWvr/XKlwIcslZkq2NI0c4r8GfoV22KXjxPEBXVkiLNnGYp1/iq8GmejyJBCy58M0ly+9KnUgWc'
    '8jAR1nlSeWwfIcqJjNb8Kx4dxFhzWGYQ7bPj39l1JalHSYfN8I7a2+zmUg6gvDxASaXNLSK8675C/mtO5Bpem3PfYdUBgbz6ciWg'
    'm1hCodym89lAhVaGhvvUXD3a0A2zzAaTAMV0deByNDCABFogJ08DU2r0a0wgFsA28MGEdGGNFyZtiGBwiU5IGbe5FTzmbAkTmTJP'
    'ss/eoAnhgLZNgjK5MCqhUy3pvZPqziBLSVEAF1JJDZihnHyHU+8WL9OwmXRhXioFDsZs93dIAmI9mMgW17cJKr3ciayxWJHw2ahM'
    'eUqsBSQFMldCPWlwlCXKEXSGnC04cLHA3C7LedQeJCF3VTMhBVrixIxQzdxOJJKZHbVXOaK7qLynh2w4PXjiuFOdgz5yWYd6r0fH'
    'zEFCACo6ChmLhfei1suowtKjvOgdlUTc7+Imi819EtH4KOuLkdNiOg7BBl4iFbwaOkcJbLLMKfhtYVpX5V6W4X6TY4WkZFwnmqHt'
    't9hPkF0kQFsmdoEeZuchK8zvfWk89hKvDRtjRlsDdmy6glLbNdOdd0hBnQlxDojz5RCq04uU9Wa7fZPKZKuQYPVNCY+lZ+KDCEvJ'
    'jEn8tvo8lqG3sRJIxm3jCj8J/s1S24pBotK7k2px6b32tuToLymK8V6HdIEs3ySGnNjcNjqxjZVXxvFjWIMtV4CGan1qF8itwPbi'
    '6yI1WBVZXWl0Jy0IF0k7CYJ+ZE0YgctpvNBVRYww15DuYKhd3485oza8TOiieeSYUEOSFhVjqGUE6lJtPBi7KQEtyvkWwpGSULCa'
    'oBirPGSvH0bk0jYX+69Sq0LcQVogl9jkQLplCFvlIlZq10OSG9BUAdBkPI5OC8BlLBtr0EVpSd8+7kOVespZ5oU21uTPMK0qoYUm'
    'PZTewlY7tLWjJibLSEmFdQjE9OiAhyM/fLvQ2YYEqk1MCgtrOwUGIHyb6TIsAErO9IdUO5vYDpc13X+5JQIwhdwZ8jk8vXbgslVX'
    'VO4l0Bmb42UvQBPJDsjc9dfTK6CRBAdWaX0SXbCyfnxHXhjkUmVwOChp1hmTK2AkQyl6h9JSpUizUUSMOF5pPX8t29hbVIw9D6Jc'
    'VttwGWssSF6zTUKRtVSQ1dSSEoZqHCYLCssSatolbWx4slgiRi6kAkopIWcvpZWWEE05TMUOYFg0piHNFbfb1oNgPiw6DqQCpVLk'
    'iMFSU/WmwXKkghIUAqCC4CH7mteuA2hw1E62BvAwi+8JRtW4ApRKy6mRYd/WXUoUOse28h9XcmRT22qGb1Ov02DzAH+ie52NXQ+z'
    'ubhE1LJ0nyK1UJVm1qqiSnKLuXh6x1fCPk/Gp2GxzPoijgMCtyKhsr2v8vZghB+ydfZJKXvbctNSdDINIttlwbY2Lt/WZRayVYuQ'
    'AWdPAKLklidjWoTCMFMCe0BHk0VKUbmgnV9K+62sbBdOvKALMMwlPnrB22lc8ucX5WKTFxXxU0jYZkWLJo9giy2WxQcp1o76Zr8L'
    'Tloe12mudexMKEuOcVGMSinxoemdE6jbK13B6mMsRLLWVqPkwXzwrLQ7o491KtSJFdZRmauMAr9Up2i1qB2qChUjE+tEG+CYHNGK'
    'UBEo6Q84x7k9y+MzfwNrfTQV+bcin8aajmcO9AI9KmqWxRqNkIXdv2GIJgMbksxHqVclZ5mK7MioFq60IZBxUNFWgC5HhwhlRGQ3'
    'xV4Sgo4QRboVeCePGtKDzBphaGoPMK1It4Oh0SQCGFQtLM3sZIAJysVJIvbHhfXZnBsbEMqgmiijBdgcjIh6iErPIXFaIT7AraRI'
    'E1GVDE2OX29cUIYq8hWmBPJUReAlhnFOjE9u2cf6AASFi2B6HJ8SGoKvryg35li+qWXLRoCYwVMiNFSnXQHCE/9N2dOmTPtLV8Lt'
    'XITAXgK8qwV+sZs20XOLicca+osIUljAUQId2vpk9O2JGmdBKqERgeMblmbdLOG7r8Qmmb4e4YbMWRYVIRVbq0p97cO3naqPnAhU'
    'M+bFNyMOao9EIdfgyXBjdRpKoGmr9+Zlmj4he5i+s3pgJRy3Lb/1WAt5mzLMKpymCs6iVJXISub0cteL9dx581IBIRVIItHehFFu'
    'F9yC5CHtMqU0SEx1/ZwqHRd2+Gkxb9jqe92pOLXuzWkylVvBPkRGoza2b/36NrH4+K/H/wc5rAPG'
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
