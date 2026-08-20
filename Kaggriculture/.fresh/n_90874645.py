"""Route 90729118 (best of 42 under our layers) + v27 functional stack (v30)."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vHNmR/C8886D+JLU3jlReCeYMBYpywzsgBgOsDQML72Hs22L/+8pSf1RVRkZG5nvd4szOrdFsVr3vlxkZGfnj/1z9'
    '9edf/v6XX67+7cer7z69v3/704e7j0+fHoer5+urv/383//5j89/+fzx7z//8l9/+efnzz9evXv/5a/ah+8+/fmnux/ef393'
    'f3V99eZhd3W9NF9/fDcMH0Z/+DgMbz9/vXs33D1dXd/Mvv5+uH/44ep6cfz5h8eHt5/ePJ3+Y/v8/L/X4459eP/mj58+nN60'
    'GPXtx6vd8PHpS1t/eHh8evfl0/Gr2YfpQHwc7u9Pb13N33p43OhVoCHj154+zacCNWD2Onf2YA+PLfkyJ4tJX/e/Iu/6cH/3'
    'ZvDGE/Xn8A/gbbN2k7fu/2U8nqYdX7774bQYJn3dz5Tzs3CEh7v5+0/L4+5peJwvovl309UDl+5yvog+PnyaLyK7OP/wr50x'
    '+WbWOzaVdnCmAzwbpVP/3tztl+bhR1935qjrqbk8DZd96WEUxr8KpwvsPzQ5YCeYFUzesh97MGaj4TAzZn+jz9h+3OnQTZ47'
    '33mnIbTT5KzLhXC4gc3gHq38bJl0QRtZdOjEk3doqT6W8jfxPIIh3J8wYI6iedMH8fiO44fPZ+9H9CE3cKdxb3nw/pd00vs+'
    'n054lw4c/nf0pq7PDT98g8fObpWVY00Gh2niAunzVLMn+zx2fmSTn5oLv89j57ZLn6e+ebi/H948/fSH4fHp/f37/5ieCZ3G'
    'ufySxBIpvyMxrpmZPdzao/a4e+joiMx+7Fzlm+eEBfiit0pifud9XNe929D+85xHySIBRsHRzgb+aYNnYRsON0HZtDIGPnrO'
    '3GZMGdrHgUHeV9xC5lohR0G3lpWxZm0PbWTgAthFlzAXgTdGjPmwecy5q7UP2OkvvYHAlj99lYcarNk+f0HtcSfXemZW16Am'
    '5wzxnI5amwsGKb/g3XZ3sahPQ9zLIUK2gfZ0x1ho9wr6+hiXe5psGIBxW2CEe6GC41mDwjcAinjY6RZiOArCvjWUCIBjFm1z'
    'tl6li8zoOJ4e8G6Pnkxu8Kj9CRtHM0lqBlmhByXoydom+gDpdjKxWBrtTLBNIPzsgpw5M4FERkoL1Q4MXfhzcKr25CZkCw0K'
    'jNh0vTROUPyv4bHHCE/fx55COC8QQvz9sWd7rA53QbtnnTNw8nH6I1SVN4NcRGTKKli1mV30SivGfM54wY+Ctpqx1Q/YMZfO'
    '2fAT4Li/u3v8UzQlUoQdMSjkQB9r/RAH/FJzgUyVU5uP43Fy/Bvb7Y5HitlRwrNq1lBo6wJkJH4NwafGY34aLTNP5OmnJ8BN'
    'B5gsx86cXqNsBRYcBZvqOoBNUm8aP/X3+/33x/5qQtubtOU05Q1uG0Eka9usu0BKjOu4HXVjCohVMKcEyXJbQphUM3H6LmOF'
    'aJYPv2BaA1x6jKNk17Sal+5d1GzE9MHqKh23xgm31AWIrBaMQIMRW3HM5QBhmRb6GgSYzIr4+i6BvHb4F4qWuWG2nLkGwmBz'
    'x6wY86nE68DVhRAxYLQWbkVklPaz60Znw+GKncfDGpGwfm0N4bCK7/prin5t+6NAZzNFynaHm+aRu1LkqJXieSVBFXvCnYmJ'
    'El8vwMwAKMP8SvhyiO8eHu6/mHTQCDv8MWr/6NCyM1yBs+bNm/SC23m0J9f1OQJJFzS7JGHBqKSvYl6MmyBTtiwKYVXQQEr3'
    'aUFx/SenjheeUNREEAPgENjm6mKNbFm0dZoAPHSizDG7Hoign4tRBAJdGlDRsHSDrjmb54zEp29rmlRSTz97Hm+vStGtPQTz'
    '8enxbvfd8Pj4539lrobb3OZ5pu990P1lwiBTs1SZ+ZTphRuYG49cJjoHW+vlzzpNY3m5zVwLe/Da1p08D4te9TT24hRnBcuy'
    'Xvi82TmDEaXxovVmQIXRmpmmV0L+iPnyfGOqpAOPE3djyII4COrbfEu5D7ePEpcsRjibvHm47Tg8zdAcDSFGJLivf68al35i'
    'gswmUFYHzcaNA6i4VbEtxbquUAHIqEsHTzuLjxqT7mGes+SZK2xwV3dTgMsKnmPhDgHxbQBWoqQFHWCNnALwTNAGwN09fgiP'
    'BiWDQp+H4ykxe0ivFA7WpAQObd/JxlD5gMZDgO4nwweSuWfDW21JDlWn2f7lF4KFWnOSgH8Y82p7JmOfk+t3k/E7xlHm2SV4'
    '7fxMRYqXLc6dbhMeDTt07x//qGPIfhoDyl5N2I4CmYeRvk7WkzkgBUpmxdqemcwuvQ1orkC3FveZebRNkfeDBfP9+/s/zlc4'
    '+JvO4FRImHB3fH0bkdNaEYjjNd4hmxSkHSw7EmMP03qonZkym6zGksTXDewZPQIVcgbMLqVrGPtlxgvXXe6GTc6yj5kXM0QJ'
    'tufh1QbHJeZ70gZVIpLJlGhGEgXrcsLGdGa+KV6CHBshhuI3J9PB3LCedn7MEb6OyEv+EZYy69l1S0WkkEqTZJPn7jvm2ABO'
    'cs3s1lso+6M6Mypokut3pXwDm/GOVp52FzZPs9I85yWWtFOY7kSqotJUAAFa34r6hxfJ5xt/AFwq7zS8SFJgpiF9opW5JnV2'
    'ozu15iws9MWr7jT0cWy0o5pBoIGr+o/tUEWC1MGCnwl/DHa9QHZrGf7Y78qYtSW3NJu/WZIBBo8GS0uALa61FM1UTIChssgy'
    'hsAG6jUPf+mcd2DS+QGIJfYjv/Le1p7xB59CI6jZXJXT+x1cI8HCoqivmZLRqyOwj9rtM6eedrMikBESvoEnxnJXWzKl65Cg'
    '1cEGbhlrf8xWzNH5mEJzeGJaDCPUT7GTRF3p8tAToqeFZeMmuLeKB481irQjMFVYDDlR5iIhlYZgEbYwCAFD24UW+TXiAGu4'
    '23iy7XoRwl9FBi0jZeG0Y9NTlIlnnQr7sBwoduo4I+uCAgfEXWXhRe9JObl7+4LEtWJdn1DlL7cwwDo2oxwL9EUD2eDJIT7c'
    'MbXJLrtv0EIy57UPBYQhddue2y9/4bDBb6p5c5xj2a8ukSko1FMhmbsoPVEK5s0GwaisYyujDLABotIR/VknoaLMREZcRYsS'
    'tYsspROCmLGT6HYmTYuFfYKQopLPloKiiugLkTEyxYyEBYARgdnjStqW1N8Ag82zrlR9gdSoMqfNrk4mbcHM9BrVNTD8mYeq'
    'SIDtJ7eZJI4s6EpDmr1ROErOqmFN5bFwi2rWGsmJzHaShWPFdf5DdP42gVeddoM8tB4SHNalItrzsB83mYpfoKFHMtu4XCNp'
    'MUUOmBTbicg2fhOKmyxKU0MQIuXYSPCTtRH2MzWEg27Ia9ux1LvpHG9TRhCHt4xYwHQdkc14+OG2QjPjlik/ISCUBDOrpy1d'
    'ZjQOGHRJNj2C/MkejFN/gNMtlD2klD32VYL7oSUlGQzs1Gy3IkaArCg2CkOj3M4GwB4BzMR84dVz3eue7brN6PAd8Zgvl3S9'
    'XMVRC5n0LYVO8QVU9vDBEkG0Ac4liGJH4n9LYEAfNgKKZtsJcZxI2XyKLC4SOinplvjh7nDEadXieXpagUJfEX7xcoM3lSBt'
    'yCumofFG5omu41OIL3KsRssk0DOUE+xmANlwn5M47uH0xXupZR5g3WVzglhrZ9ZcxsThHBSRcB1zk40lFTZaoZOLSRABfaCg'
    'S+DX6r4u5VsCT0rwtipCQGEOttxCIUf0Wk3RLyl8xnk7IpysqQfIFX6aNzmNjPuAQUp2gvyz69wkA/2RfoncVkXWy6GUaTpg'
    'icBEuNRQyzTwTv3Pyrbn64eNeWVJoe3WNgHVYwsRbthuB04wrGfQpFBdWUy7wXfTQSeBDI7/q9RMqCspnz0BGk8qTRVU9aI0'
    'HH0NUUDD7oeU5u55DiOJQKMX9mol/WhNjJYOMNhfEheIY3IXZo5YvErSFOyOY3laGSSJZkye17/konzdU2vscWN9YBxyNBg3'
    'oZzqEiAJosixobbFevROwrFSm47qi8ARRJc2ur4TqM/2Wc9TBg0OhDmMIiLOc5nbs0XZXtvQkMSqs0Gq1eIIySJC/DzBqlDn'
    'QUu7O0Ddz6Xgi6Z35xhPtZIbGm+OUeTsJq7Knrbn6HGfnTsbiZZJutlUuI0NUUlgmWwJkVQWgRYV1T+i9SZm54toYptPxZBq'
    'lH0WbFNAoaphOXpOlMSLsmkNMDQ7P8xMEINWUNLYCztJCYYU3Zk3MlPbSx9fRJKyhkOCysISnLD+B5lPiqf08tPtopGSCEUQ'
    'aj6Nq+eqLL1YixxFbqIHlop9qMhc+PbWIV1kaDT5TxRbqjSPxX1oLhytAFADRau+8mqsI/ElD/m25D33TIcAapfNX15GgYK4'
    'eTZd8viNmkKratxHHcsIk5uYPwMAmfk/t+3yTr4yuEii02/dOBJuHKoJGdCMfFHC1zqpTJITcE+wC90UymJ6nGQUybjObZBa'
    'pUe7UUJmalnGoMiYpMr8tPo8828yxbvYYkOIDfNlZKe+MTXBWqgY+aLEUp9ToJdCWtw8JzKiYrNfVnKoISDER9X032mG3hmc'
    'Vaa2KGoc1uqtE4whXUNA0y2tnB6aWiZPA2AbormKbS6rCmyGXhkMjPif1NhglY6VtCIxiWiVyF2g7ZWDFZJkLHNzptZidqkM'
    'IYNOXLaV1EatpCiImZOwNkeuNaRbrvaVHG3uUw7phaICCzU+YVHnAtwVIRhRTZeQBzz1IYGisPQYbXX3iJaPC6Y6lReA5uQ5'
    'ff818uiTX6JFcVaHXmC/VQuF+f54oNNQMZok/5qVkmird0OcZZyCzDCGTn4wc9dTKEHN8WVu5vH1s2TmVofWxp9DUkeV6oxC'
    '90TyLXEr5ZgDTDaWcB1yqvR6/Qw4s+tkWlDl4GkzQ5UKFbXanBo7Xw3C56aNFZfLq7PkGfVsliipSLf7muqmUmiLZE5kh8HO'
    'DMsWpG5ild2jherVChPznPyJtfeqHNSTxA58tny1gMmQSwDoOQUSYKNnnCYXJm3RILAgilkRymQk/LxSgc+LBCg3LEB5Tl9k'
    'gzyM5Jeig3rBMCS0ZyKteB6TRJTkMtGYOT+OyXutUgMp0WbqzTQ6TlHoajzg3udR3MHtN564lE4TVY7XiybkDj3cVtjPlRdE'
    'FmM8SS62TnsBK41e9LqhjhEgUANkXRH8Riq6Exn8DRGi1ChMoDAiZdzQPI4FuhP0SUY+HTa5HOiRHSiUNyhCe5uYaGSxggSX'
    '/S7kOgfVN1rYtIDNjjb5puxY8U9NDEjSCYndHhZVd+s7FMmRrJ0VUczArWyiBaDSD6y2eFrd34k91TA6JDEFSEQ8zk4I+C7U'
    'UdShoIU1hH0StDITCAf2BatIojWAhvDdWH4xy5zdnGxZ0kQLb2FX/X46prJDSIuBuDd+alwj01iWpqBAC43TJoBktHrVBlbQ'
    'B9puMdR7ppwOrMU3shtvosR3Fv4lnvLo6UpkFBTzicTVSL1Gm0YezX+cRF1T97cvSKW4S2nb4R3ZD9fZ9sF1tIRsAe7ZIhAn'
    '+aVQtn3R1G3d7QFHoQs0EC07gzio7uoqBfUwPwqnH5XKIvYGEKJgbAAXuPyiZrgGVY0OwBXdYqhhYzAWxsakVEOCwfFi7QpJ'
    'u782BizQrLnnLaXHEZIxiiXuJ1hn6Ra9VDoNktbaqK3tHADcbXc4hi5UG+L40VOxtiKJnEc4EGjeIGNGmRLmZSGXDj5fBH1q'
    'O9QibZRzSVHSlO8ONue0z3btTqBzkprQxpbRE5Ad4zpsWTM1A9kKWopEBsOiVCYx3Uj3TCvheHFAwszupoSQar3qUaACLvs4'
    '37uV60RdbgqIlFAwnZmiLy5/mXX16UblkrtHs4mcekdPjcANXx21W8aK7tg5DeUMo6S3glPniGp0aDHwOrPh90D2ftzXbbMd'
    'Lho1PKEJMrA7UuwAAM1p4EEyJZFkK0nlk2RhauJPQcPFItIzsfgFOZOUmkHQ1JqPMBxMMUaWIMTTmod+JSMzmCOUjXuyAWOk'
    'Fh6j8nvAfoYmbFjKqViJiZF9mEMOttDUNGlzAW37aEiU5UnQhO9CBpdGHaUwjpjxXnDV7HCBpSaCTRxbKJcxtHn/iiqFUJWA'
    'z6ss+6gnAicNUtBwuW5Ll7lQSoZpZrN3sQZ5oiLnZ10iQlIYKIwxUvUCD/jS1GZfz7tzGjGq9UyFFDTBQqo1UGz9vHlqzEJn'
    '9zuHPPbCIfYV8wWtbC7gjGsMEF47T5EE0KS36BZhnkhJey1R8NBO7HRS1E5tS+6V9lV00rI01ThYVqw4GoBcGleG9h/BRYUt'
    'n8ZAxjXsFrdOrnR3AOHlBLKXl8tZYFrUYEX4oEEmU6GzfpqWrx0Z2JWca2WoAdaAKfrcYdNzJMs4SXMGuUbEZXJnU+u+Neuc'
    'rBkUmLf4SKAer4eOJRklgPqQ+uBxNV5sW+uNZixYka4d5WNrVYf9yarxosFiFqWzjPE5SutoqcdIYLdNB2NNEnXn5fwGQUEu'
    'nhQQqwF7U09RoI69zCYlkGNNhkzLGa5kC2iqeIo/z07Qt+//PVEGs4F+1AaT22Pk0PCdcJHGC0UtFRlTta17qEtKSWGGpPuu'
    'Q5jMKDh9AgsGXl2ZwE4Qq2vpQpreoAhpcqneIFmVNB8CPuGT7YxolQSpawjHv1SUk8eAKF0AmzV63YQe+i4M7mG7oqQPQNU/'
    'mSBkHggiHPnoNrWdBamqTK5OJv9T/VINTiH91JQMqwJ8SvE2EVYRusCWIunwhTrQhgvdmLSHxfa3gf9szwX/oGyhpP5BWHg6'
    'Q4CR8B5MvRgYY1MUwwkp/Lf9sxqSwVNq+E/QiS7SMloGhLZmeO1CWUxec5Vp1pqUZWL9ecD/IMVvqCKVLlEGe3QbqzRo6k1c'
    'Z4GXQSdes2puLEsCIukVEhXQwa6JIBamdYqkiTTXLwh/J51jtU1DFVgoUoBjr8h2D2qBak1nnHtwk2nnL493MhxDs7ylYn5q'
    'NcNowH3opge9Atx2pASnkgAkC49oKjCMEMoWCK9zwLBVljFSXR/UqJAQC4uWuWuloHMvSO0UICAJ8SoFroWDnGXVUeANG9OH'
    '8W/YjpnbR0dAkqVPoqdwdnGSmWJHnmNJ0kxp8iuOcVZoMrUW89vDvyri2/NVpm5xkYYlwabujRD3YfFcibdq3B8CulPyIg7p'
    '7X3G5wRR2AJqU1glVdZhlyRKkBnw+tKI61g5i7PIVlwmF4oM35jrA8Zhdf5kqEIOjoABNEiWUhUmlY10G3NpRM+ja7V6moHA'
    'U00GzQ8I9QZzERrAS6EDGLl7sfSCzy8rUfGVVHRE6qEOqkeODGCU/CnKwt3I8XcI/ZkwNtr5EWc9HHOWGaTxxahbSG4vNtw3'
    'iaJi4WmQEVCIE56CtdY6+AHCztc871FTTpk9ZBxvTk+x19WZnPGdr5plouA8y3nl6AHnX7PSNfSAWRwMI+HolDCdaevCtopq'
    'sroAip8gP+u5IGkclE1NimOy/2PsYmd+lqvnBI0OdwVE5fe12JfuWWBzTpxJdg90WgQeFEFbLDNTFQI/JHuGwY+zEdp6e47A'
    'j/t/XWYmLuZJcVowNw/htJ8hS9mzSKjJGq00YKapkQKy2m4TJyKA1XLlB2zAh6quUNFe8gi2KD1le7bHsplNKl8xXYCc9WiT'
    'QW6VREBujbGJU8i73A9oWZOiTrouJxUNlD6NgcLE8aq+rkaOgwwJ52ag0TGe22DPaNa114mJbUTQXltm1BKaRZ7qbwvyZE1H'
    'bIa4aHw/YpQ34EulnjFC85TSMlBOqIkp5p2B7TQwSqEgSYPMSa843+pxHefNsXzB8GaOnahVZZSB8cJGGTAppFJK8v5eC1BT'
    'iIsi2p2mo8KyNQMHtsQeCm4oMBUs6anvVAgC6xDECEAcsOL0XeCUSKX9W2XiDxJ3LlUqdydcwyZhOQIJSP4gD42IYcUALj9v'
    'V2gbmQFvIXR8vYNvBYZ427RwGVfctuh4YCl9ZOO71cX27uhK6Sor78LwsimXdS1kCtPgeImyOi2pZjQt0cG4H5pNIpZ/LBQ0'
    'Nn9f5cN5hXIuJE6aGxzb9niMMveGTvHRvH52qKmsJWmnR1JaURk9gR6f+rFX028NbTuFeKPtkIy11liADMkOGSiU8K5KlRal'
    'BU57XRHvkqUVwtWQCU+o/V89d1DIjiIB9NTnEFjn6QZ+1Qmt4ZRoBOCE+l+FrBk/Lt5tFG56bHVSTg8lssAob0yYSRo9tk6R'
    'PwrrpOCdpjHOZdYieC8120vlFJeKjFt+MDmnmNVeSKKqHtRt2OVqYbHLjSMA9pstZHW2/E+AMSUKVym8OwWo7JYNCptxI6BN'
    'yN4nOrt9ypa7MZcU808XyakUPGhODd3JBndADEkoiSnkwNsSdqiRpTU1WaAzl8vNVeqPU5xJE9/kHM+hQ/kfWlaWqUv5hIg5'
    '4FkrD0TehNZtxLGMPPCy+ghJMGHqvw55R1SDEfKcak1WjwSVoSt48olK0Fq1NTpgatZgmHGS4g8TnDRi28T63LxLcciubdw1'
    '/iA9+FxqnEeAiGdg9ZyQTwSzHo86K6QQZfwK1JNNjWXIJALSte7cu5Q3/FrW5iBFsxlJUAoESixD+yPZIquHFROltpmQfB4l'
    'o4rn7srhHGyd1kEPEdKK4v1X1BaLJT9cEGEQlCY4j1+sruT8t0kgF4n0hHkpWOqB4p3BvYx7SKp0W9AMId9u5W+hdnMt8Jeq'
    'Ry5VKNcV2FDX8A5cJypE1ToSlZkfnV9VoTInCNeXo2fDozes5N+cwduFB2eJhxeCwDSiX7vAP8T9Nk16+Vm9NKrIUc+UzSnl'
    'U917VhRmN+h5v11QMmrs6mqqQvCrQZBVg8JCxlWqQFuUplcb91DYfB0KbHGlrSjQRqhzbkT8uQCM8aIREboD+USCdljr9NCx'
    'JQw5XkqotJfhFaTWRBOUgGh6vMLkoPoFLLIhiMeWaGlkfoKCJXr5BLDTpBi9kBNakrVJKPenCDfhD5omGBH0lrU8Ukk/hjqV'
    'FMKnuc9FrmhLvhE7qWi5BgIuhHPN5OC7xbW3CU8GozyGmLhMAXbRnmHgO+2gaZKXAoRdvFcJ6qEmd3Xw21MQvlLUrNtiEFTJ'
    '3NuG7l27DfJajwWVtU3uILipCWxmy2PaX2VCObl8MmEVxIQdBg+LwGdEPLKkbqu3pBatXKRm3W50hEr5SCDorPmNhq5ma45q'
    '8/m1MbyarRTiJ6g/5VjPZCCLiHBL5KNScMlW2qFds+vX0t3z8Q+XMp9fBhHJnC7RZN3jOMdcWRMjvFHeuqyGu0hp0eY7XwOt'
    '03Zug2OXVmH9lsGxHbDXVxidXCxeIC1xPFSW17tYnqUcawqWDZIjU9qBPizbBMImin6ykLqgkNcHdyW1NuIMzvOgp1KBeJrK'
    '2AqTclTWlUIjh38ImyvwZlZkLy4y17vwicWLA2auPoKaOJ4CQsImZRJHBAJrjSSnoeyUyuCpFGrDlxK1nsYQbvVCEVqMbHZP'
    'V0A5XSeZpcX0HtKAn58W1dMyNHWgKxw1w54YrQCxvLUHEWaWAGPesStP6JXIrs0UB41cED0VmVezpOsikFMryQWnYLyUDq2d'
    'CLJaBGFdOcxCwrME0ib7tTrIrB6vEB3np0WmCjLMzqss2Z0mQcsFKitF7pWgRMwsEK0r6VRziCpBIVgKDuePtrj4barxGmZM'
    'VKy1gmUufpjS9W1DE17L3K5FL25XQHH6f5TaaBkFQSFL36LuXsqSFeIMOSacy9GZfWX9tsC2oDJUQlG6jLTlIGkRsQp7MdWt'
    'KF5O0xWVSitKEc1k4iDRzwFpqsZP5/SVZEHPlIMONkfogWiyJgUpQOUuJoeQAqLxcaW5PEmXghm0NOKRIuLopBwRX5K0vyqJ'
    'xxwBKuZTuek5q2wQiunJM2xSrgFFEhNruTgStRykBgMkVdSH9iaPiTUrqpPyJM5fhACUCplFJ0ZRxlWb9vStQIcImZmE6aF8'
    's2PMWyjFlSpj5k30Bsh0JawVfVRUx0ZW7w4yblsovaB6GqEyiYRHTW4hX6FR0shsE9iyJJeSpZLkso19r/q+rRbIBDkLCZtM'
    'ZS29qrGvSWlVU/6WwlKo45lKU6m6O4aUlFAHKNULBUmAYpbc607zAnp4+A1LYyz2wLAvhC1jJsXWTwYEZ5LLiJhQCy2LMaZD'
    'LTyoaXmBrMaVksPYUNMTbSFMo/lW6l65gp/eGE0G9RtAZrtK4U+tAm7EpeqDq5HgNAnh9FX8yoivW9pDVJSvWT2KqfUnUZ2U'
    'mcsKoCV8RqeO39yjFJNougCqqHIhQyhZEgzBLBMDyDA1qmwe0lsCJR1fJ6W1KmSyignl1FH7vhqZZeXaOrRZZmdtBdMf4NYc'
    'rt4Nitq8pHiVy/pdJ7RPmOQcBNRFMdmcgpWOkDTwT6oqkFr+jaLGU6mjm9Z+9POrOdFFzBhZKuuNCfZy7kqiYp44MvHq0xWf'
    'shXutFyHHWFLpFTUCKw6WR9CglmmcqGSsmpNkBQjAqwo8cgN5NyDHFOP6sEhpmo9THqteSUVtlIMgEGOWnrs6WVRHVq2/Xlo'
    '3Ck8yJA1QsYREKfbVDGmSB5UVMMldLQE5emmvMyYZKt8bUb4WfuCc3YTWF38YgNIERL+VwC0GC173Y4SoSDLOfKsXgYPqqxv'
    'tb4c1hNUhFLoPpfHdzhDIrogd0O5nMW6MtaJ0omwY4EKrJjevhbyuCWzLc5GCHuRlmZZ12o+Fr0iSR1NwmE0ygC7mKnSbkoq'
    'QyEUBoG5jvlfkUwei3gV5yBR8INFyGB6NKcQhXsnYRstnytwGaPWOAkBzL+bQyYpK0fKLOLjTeOyKZ+7s6A3d76Yf6oRJ3x/'
    'kHdBD3NGJDSan0Ed8EGpNCgS+ALrMrQuEMU5AgO0VFrKaJGwD+t1EvCDkefC/BjVlxFul8QJZssEI4zU706UwMQJVOSIaV1U'
    'yYKRt+mEG4q2j4dlRmkhqIdYpsyHc6PADzigLV8iS1RJ4R46Ak99BDExzZEOrZ9my4TQKT1tmeja6W9Whi1Jn0yImItosjYt'
    'M9EcWRKvDeAXu2DH2RXFaz2FjLyWfTfUoLOC8HYpJAo0dNfm2UiMJnuoAb7NEdDqC7Mk8iNoiF2TAg8bCHZe6JlD7yRIi6CG'
    'KOdtLTsMqnRflnMhWGSXYFahGSvp/rYV27JjyWRVuNVUKEEY5k7Z8eO4Xsya4vZ4QKbWFiiTULODatcmbrjYnWKhLK5dQrVG'
    'ojJ3ik6+9ZcJeYdqxZIqnTwIK2g/eBJWwWBpsS/hMKFRYPtoJrkc8BAy4hNR0eWAUDNoSdhkr+dmUU+UBhivxryygFGmWrdG'
    'OqRQSQKvDSomIFOX+9Nk6gRvh6rcploOl2UtY36nXTgSmahQmgKY3eAEOv5qgiaSEk5C7kPG8QFxZjiqJN2hTyOD86g4TuF/'
    'Flq6/99xiLlDXSv9wwUa2/Lh9+ZdrHnz04cGx26N5+yRFByt3LK7Gsga8VMchXHE90oaI8GF57tsqVyMOCwb2E+ZelD4KJU0'
    '2UW5+pyaqbWa+Qt9h7luM7IcWEnhPGfhs0KStGJy0jmEU02KXsqqCkUznRHSHLKqcBDG422fopoO+mvFsVbekuuu8NLGm+ab'
    'vxEgmi+hkxROP1c3OZovWdvzBOfHhw/hfiG0Lz+WQCiQK5wSHGRhKBaXOkAJzXL7WtBnAmVJMZ/KO9W+0tzc8MX7BdL2QY1F'
    'f10eSF5gfSH7ezo2z/8HL5i5uA=='
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
SMOOTH_FLUSH = 16            # last turns: dump everything, unsold goods score 0
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


def agent(obs):
    try:
        step = min(max(0, int(_get(obs, "step", 0) or 0)), len(_ACTIONS) - 1)
        action = _aligned(_ACTIONS[step], obs)
        action = _weed_repair(obs, action, step)
        action = _fix_animal_species(obs, action)
        action = _idle_fill(obs, action)
        action = _impact_slots(obs, action)
        action = _terminal_liquidation(obs, _aligned(action, obs))
        return _smooth_sells(obs, action)
    except Exception:
        return {
            "farmer": ["PASS"],
            "hands": [["PASS"] for _ in (_get(_farm(obs), "hands", []) or [])],
            "market": [],
        }
