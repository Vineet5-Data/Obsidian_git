import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vW1ly/C961oNJUV9589jc2FjNyJDtEJuBMBggGwQINg+TvAX57/FaFHl5T3V1VZ9DWl74yQRF33u+T3d1dfWv/3v2'
    '77//8be//nH2T7+e/fT5/d3b3z68/vjp88P67PH87D9+/69/++8vf/ny8W+///Gff/2fL59/PXv3/utftQ8/ff7Lb69/ef/z'
    '67uz87M395uz82Xz9cd36/WHyR8+rtdvv3y9ebd+/ens/Hr29c/ru/tfzs4Xu59/eLh/+/nNp/3/uHp8/L/zacc+vH/z588f'
    '9m9aTPr269lm/fHT17b+cv/w6d3XT7uvZh8OB+Lj+u5u/9aL+VufHzd5FWjI9LX7T/OpQA2YvS6cPdjDXUu+zsnioK/bX5F3'
    'fbh7/WYdjSfqz/N/AG+btZu8dftfpuPZtOPrd7/sF8NBX7czFfwsHeH16/n798vj9af1w3wRzb87XD1w6S7ni+jj/ef5ImoX'
    '55/+vjMOvpn1jk1lOziHAzwbpX3/3rzeLs3nHz3tzEnXrbncD1f70udRmP4qnS6w/9DkgJ3QrGDylu3YgzGbDEczY+1v9Bnb'
    'jjsduoPnznfefgjbaQrW5UI43MBmCI9WfrYcdEEbWXTo5JP33FJ9LOVv8nkEQ7g9YcAcZfOmD+LuHbsPX87ej+iDN3D7ce95'
    '8PaXdNLHPp9O+JAOPP/fyZuGPjf98A0eO7tVLgJrMjlMjQtkzFPnZ6uzfU/egrk9Qn7amBFjWvDm/u5u/ebTb39aP3x6f/f+'
    'Xw/PhEGDV36JsUTK7zjSHDzf2pP2hHto54jMfhxc5ZePhgX4ote/Mb/zPq7q3m1q/3XaJMC8a8zHiREOFm7FzwDGCNwTuFfb'
    'pW2ZybwP095mfUwHEDj2hkHKXBX4KXsgGwv0KX0g8whE+7HDH42bXHSg4kGVbF9lA1HfPJ9/4un0ub4K8JQ+DnrLhvMAjPv9'
    'I1tjMN/8LXBCbMu8fdbjUlOV4GYnNqx/PG380+R7H9hQKwxgL7qMAgQki6YGu9j6rjiG5gS3c2odFK7BzBDohOqki2GIgYBw'
    'xvDSKN6NDFzfH9d9owJe5jyaGgvgLdH8pzeCZkOUzBMyPNxqyx9NAWoAp1kAIMG56IgMOaDhKh168s+xtH8c5OzHY3881sSk'
    'YuvFjtWDYHoQlU8srcvKmVnxxU1wpOjyGWBIX/Qws7sqBooHKTntJyHxXi+U3enB2Lx7/fAvUcd6AaNJd3RXXwxBo6Ha9aU4'
    'RNOx6OEHtIPTBhB3TIAuFIQP+q5jT281nRlgj+wGZTpSOZYBwJGDZbdfo8+Dsg9XyoO+fyK6VKbvm9tXVnT4mWBBby7whkp4'
    'uH1wy3H6YSD8eGwvwnPp2EiXX/f8AY3vRgd9QiNqayp9/PTwevPT+uHhL4AdKMWN2CUWNhy8ffHYA4XkMabDlgwJLm30I9k3'
    'ovT4WTpuhmE4h6/6ISUjisGCTptjGU1Te2MKUXmYEQ9mda2P3YfdJZ0/ToNhn+/YyTbEXNSBkccuf2M+AsVVEPXb+vqpmVUb'
    'D316amgl4tneW4R/JlCnncdVcL6jseN+xJm+VdTqyrZpTmSpxOhBu9O2r/qyER/uUbqECbQr/jF1vzN8pXKvMABicgtu7u/v'
    'vqapQCNq+8ftDH05IN8KkcC9L26F68r0oXM4qQ23jJETBrFF5oMaXQCyEfs8OfKQ16AzYOiArJ/Rt/zoGBhJfKlcthIq1BVA'
    '1R2PPqZRG/dNgSsJTG0+leHHdSGsCJoIUMz9pwpYh0C/Cf8IWIzdW8EYgXbO0Yk2Pxsqe4GNNfpkjgw4f1pkdx57rvGogGsx'
    's1KPZQxdVXJQ7aAZRFxg2GyVG1cwR9S2uI5DKcpspv1yaSg7u954hwHK8HQjYzVeZTszIASUmpPB15m5xmEC9QQB3nme9nte'
    'zoiW03VJLmJGT5nlvHqWIsoDpuudp/XKmIIAv+6iUbA9rTGhwo7WXb6P41nsKdM6bd/bHhviXPSF2i1zG7eO3fO6sRhet0FD'
    'jFsZbML2CCD3PmjR7G/FDFdmE6QfSg4i6G/YqWKHyRxXuukbdWS6p4ceMtUpxy5AbzPbjdmYu9ekgKVH92uHYHe2zlMWzgfF'
    'IEE39+IIcri79m6w3uXHFtM5gFlx7Ff2BI+rrxTTImO/o598d4u9CEtqZsrja28c+DPLoygkQ1BjZ/fHHspdjRW327RTHDcy'
    '7J9/K4RRMyEh0WikfFBsHzy/FVOGStFxDzoER+P+ON5ezD+/v/vzduVF7lD7yzxnrgf13m7pp/ctlvlOXTIswJ5KsLhsWIA7'
    'MfoMEsotWHFgawtyMJZfaQaKhGTNYwo4gaN5T8ecGlgNzNGyNj0XrDaWu5mcHhk50/M8SdsVAoTNWF7kiGjLt5jIfmGjFflY'
    'bSvxgdkHlYN5B04G211AtKx9QDEy2vJVgcsiIiOxH5NzXz0cubWqmQPn+Hs1BAOMGZjHwodqvjb1JE/ROnYAxvzuIhihNAgO'
    'BNoI4C7LzpSjT2x7EgdNkgbU7E5tSxizZqEPVYzk7ft/lhXRAP2JABgVyChbjZ57y3Aa/3/0MvwNQKc7ydONEk5Z01LgsBYh'
    '9B31VXT3k99pclDH8OCBtZI58IR86wU1dX8+D9M1xo/m1vc4+I2rALN+sEkqu7ryD3szGZmj365h7ueM60s5A/SQVbbCywpY'
    'WcBBWucx8cTsN7lrK4JSpM799FY9HIEyyZBH7pSYG+2sYW+2VEwsxE3da+mIqOS3guOKvSuBPwVvfAyngPKfmPQWhz+6JFkk'
    '57v1poHNSrblIJhDSpd6LXi34G+inohO347AaZZeJHnCwOgDXYx/1ZnCrKyF1kBVQpet6VonAPKNfuwW20tAZDH0ugm5koYQ'
    'sIRc074YY9quii7eCZoFTLkhrzzlaJ2sVS90sIbTAsZI2oxmDtRaJaf+yaBC2bXOCTvfLnBPmDSVwH1dN02GJUoBfGrimfI4'
    'wcq6fuzTKFa6Iw/6UaijYGX0CUdW3ckKERTwXiUOOYyVomd0qwxAIkfiV8ek/NCDKYZxyKvUVLwsy7OY7NV61GCApi8R4769'
    'eWLqo1lTYIBeKVg2BYZvXWoKlE3SXGIaWCYrMQDodTo7eHE2z7SJ4D+n7W1JQMWQGW4GFBMLZbTy1t60yjiXj/otwNjOfN22'
    '34BJK7X/KoRFFwvDtGCrmDEmwLzwLEG5WwZCZwbcG/2Wg+KL5vo6+L/VzlFGudhIOBzCLd/GcvN+oE7PKYPterzM1yNDhmcD'
    'cZVM7oYdIoAoLff6SjhENDwZ3CbmLOLF0bNcF53+EvDpUBtTaymqZMlX7P4dufYpSAtj87HRDKiwB5JDdS5hkiRvAO+blkNI'
    'jhRWHTM0hfPF1tcvDzksAqyokR3wSXxsTBjftGbwk0zKoOTtZTnBgoM3LyXZIqoubHnnRydt7PMERsTLhVxsicxhCJYA71MA'
    'chjyIKeNT0eqImQkczK6U0i85x7ogDQhY72UtLLs7EA7WEhpNwqR7JZrwptl7V1Pqk+4qW8eK0BSCv0Bd5iEcDlbvYurgbjM'
    'Sl63xieIyGSJecCMasBektIK6IpvTCJz8ejIQmMsH1wKp1ofxYA4GHtz2XBXfvy6aRO72LLxVD65e5CR1PvljvYBK5lL76qU'
    'sJ1VXVbEQeMLWmkdo2sRZcTw8D8vdmkT1y6gUCeA4uJ+l264pCtU0CxbaKD1FA1Rim1UE4coVAherCym9jeOnB1ZJeKxyKXl'
    '0F8HLhWllirXuYu/pvcJ/WrYyqEhP8CpEoHZmvIhHVoK3OeaEcHPh9xSw3UuJFhIkJm2oZw9btMvjzESjNl9OW3PTYLdHB+c'
    'ASiNm/+9rqsU7e4llDHjcGpkhMVkRCSpMTXKDAmJtDHKmuKQnwvVr9/sZI7oHgtYGRWllgzBquioMdYJEyww8EBZ0fj2sUKV'
    'ongMo8/PvxLU4Y1kA53Uxf2NQSLWwI6WU4sUypa16FpAQnS+mKsrTuKywn2hIoNSZmNlzpA/ltb7VXOGsGtdm0YavszoV4qK'
    'TdV7ZNFX5qUzX8tliS0fK66YFiQW5IFGDCN1N0AJwMTvdeoPMWcp9eckbFbx8IQccaEUEwVhxO9Ely5YiRqiRNte9zzDVe5v'
    'IdZCx8vXiH9HaW95mkctWaFYk1DsPMAnGHyEGBFS+/r96Ke05+vAs14hytX34myfjArRutaQ1qzlM4cIQcHt3ruBuz8VA+yy'
    'bVXBXaXsiExMDcBwnXR/ML+7TZw5q1VJgxJ/oROcaVcJGlX+nURLezprFiFR9cbgtGuCKjkpJvUe3EwCS7IxfSkS+UuLAqmS'
    'F7TZHme9/VsGhxgJPAXdSbhGGVvCzivpUWzUFPr5J2mqC3PqrCqP6jdEWYFmpFGPIf5Z5yRy8VLm4kis3gqhGmENdExSqkJn'
    'oTBlL4lXS5iq1F/c4NlYnz5fiHRF7HtFL3bIfcL8exaLjAlXCB+Y/TcfAdDCvHkBW7woou6NCKRv1qrOiSuTUlHt7GwNIFr5'
    'zWpd416hE5o7kKV0jExwUD5M+K1KmWWtkTVv/jbw3S9b333x7Xx3nrWAdupAv3y/NJF2W4gqdNU0BX5WG0aEyatZrLnXty7m'
    'D5RDrMoMdetNbIoj5rEXmDtWHh+lgpleNiRFauTg801NC5E6V88064PUx1dPQ7v9JjMxJpWZO/3YbPUh1nd8WOiC7xKfnmUk'
    'aZyCgSorJOybzVufqobIqS8Mueh6UwX+ircGBh3eAgpnl3VYrQmj5pCETo9ZFwIvMOzRSVV58qQ6YkEbxV2HoGoslKxQAIqF'
    'y6nntYY7mbzYjv5dGAF/Y87HjQHFHQgVPXS8izba1FCdTgbPznFzQBSPt6AGU+NWD+YCX7Rez813E7F03KCTBizRrkjcpkFp'
    '20eIZUplznKzXSURkw/ZYAuXpVH+ReAVg8BTnacN77NKVn0nxbhdOYcFAJ9kMozxn1jrGuc3rQaIBGFeGemUvXzw6bxjIyCP'
    'ClU8SsknAYuSBdAw+0508VJT5trhWOYnlOT7VEq3ixj9zaPBk6aBNuoQptatr10mbI/E1dLKMogV42UpvFd9SoOeJaj1Mm/0'
    'smGMXT1WyNpeXDb0C8ULUFN61FjcbMXD5lj5tYVlQ+LACUFSS2RNRAxE4UTB81MUJrM/4jOfHDmDW66xvJPDh/IC6kKVi5Lz'
    'raV1JELCHYRh1JMLqcSVLdFITJtU5nBMP9orQNyaElbFeP00sFrtjhbnZ3RYArmQs3+YNu2yX2hCLqKkpNrwjJf6Qryspz88'
    'lb3c/8sC4pQO//yAiCNx1I7Z4NMBuDt98VTwDzToFosQvsRYfI02PyYqX3cSxsTjMz9aD5gfJ0ivlzXoYoX68fm0FYNxH2V+'
    'W7GpQZKOnbF84P6noRcj01mL0ushb3Rj02u2EIBnke1qbopSuF6KxKuCjagWmRwVUojG4AWHC0cyNY4jPGeKEzKlgW7YU5BN'
    'Vv6zsoBYZUjiVCXFNhzpJAUGoJqQxP2pBPglM9aOiRSUczVUDFoclAXdSUXVkskVsTMKC1dDwVqUXNNUGKZjwBjZkly/RpBP'
    'FxloB5+EtSAbGkfXR4wTkSl1gbdcsbEwjZRyNUTL7TiO4NTfW70k5w4Qm78pxQCQZ2WOAbmIRlAKaBxOl9/uJEdUvEN4a+lf'
    '8qBcgcMpO4zZ3wUHG6P+/XnY4yXuMjsVHMByIF+N3MXZ1rePBd81NZ8jhyTrGFyScwtWwQJL3jANtYuMeskbyxaeAbrPI7Jt'
    'iFDxvA+brDtUPK+0dxLnfVuWJOl5CFMtJ9QTN3cILyTWxP1GTSmu3GQvaVysZIH+A+WAjwl9EixBVQwI6C0MCRkS/DQOcnbm'
    'ifwRNXyFHtdTfvC6PdYMvgxN1ggwM8owaLfi5D/nHbzumrMk9CtVZMmO5DGzdlUNzEvSg0hWW/FqramS4toaA0TL5whXId1b'
    'Iw6QelCbOxMM8MTUg6eKKxNP+ir1+rLONk/LyDCsaMFG6exaPVbIMOZ9XPVOk0QaId2LKBl506+sMZeybawu9PDXOvYR0RwA'
    'UgetpkP7DeBYxLeA2LdjkySeHNBkcz6BZsvVC0vUWb4cHX9SwEYUZhOAvyFZORaCY0R5aV3IYmqOLLlwrv/3fkn6UxQA2KjF'
    'DAbLLVj5OoX8fFl+jvars15AJtZA/a0UxU0KpA6sI4A+RRBXaSdLqpHTE/m2VG+AeRl4ZI1JEG9bK9FGpJ6I5TmH8veV0gU4'
    'dSuxjvOJmH62fLtSgQNebEHKIaJF1VVY69pItBEXxIG8XdMyYUfYy0gtsG7ncKEeIzOIYKqFHK4Ij+8sycB3Ns5rUecvZmMd'
    'CxtRgUOhqKWpjNDRr1V9GinqQROEaFIKtC1raRsK+NO65lr9WIZ6D5bp73HK25Of5sl0lEgY3kGHTEO70mRcnHim8o7QKKNQ'
    '9TOD9XtKhlT7NLSwyUvYSqw4Bi1yyfuKYOEnhTj60MqZ374imdYultgioIlBN+ebAWH7K+ZllNRANhFnT6t0rIvhYFjGa5OR'
    'Auh+yohFgAEoKeSGB2w4zjL3p8SOWRrLypI+rVPUsg6HAeb8/Lo1FmaloqY8V8hIN5YomshXiA9gWAsMYBNUSVg58gR0c70L'
    'tDkb4oOzsFntelHWUkMliSTrMpQyuhEmlh2whYKwnJ+m4U/5HMfzuayRByRWpUoH4SaX3MmrvnVIeWCqVejk+Im9IAuO1ltR'
    'txN9hoyb6RxddFilTHvNY/TVmZRzW8qUi07wCA+iw24sF8XLkxIjNwpfU62F4vs7wjnLc7iIng2txkuL3Ba2K/BqaO6IluCY'
    'l1PqwxOt9L9ixiSZGHbPDWEvJxnHa5tOdLyp6EDoFY62tPCEdToOyyXHE1tpCXtM4ifZ4jS1YwpUsolr2ygMK1SDZoBCUp16'
    'qVWf0mropN0uL72LQaVsLl5F6NySFbn53ivaDFbTwUafXuYmNfgG0MYyyCCFnwyf0NB0ZogYZVYMKQPbXYU3V1v3qtym7TRc'
    'NZ0mNT43E1jjh16DmQWX8hq5na5RtLS4mF3A1tEf767tgtScCXUmcuU0GkpNTAbQxTg4lGR6ZG1VVGUYVsRAzijFSSOs+hjn'
    'pXFRST6JukOpC617OFcVMN1JD6TNSxRh/dYTcIjmxMJW0Fw6xtlRXbRXNYiIqcxKSwZvSxXqbmWx+zwxirpzCIjnlxUiFheP'
    'BbIz15KItgNFLdExVsiQAta9egBSckVwuIb7WnWuLi3IK9NIFxWEGa+mmFI0l2LNE9eSJFX0KboPDGGqU6NIBPtis/BMiHkK'
    'sq2cKY3DEkVZ5LmbP2usDgymhzfUhG6IQTcpgbQzhVQHcyQlNZeUpmhC9KQAvhL7IgqwMWZkSNttya0h1FUwKvooWzeUsjWt'
    'LwaJKT+wKaXMGNV8hbDV6niaYAcYE0kKEXGhcfXElLxKWQnMqJfRU1cMJcl36385RdE6Smkr4klwsfiZrAp8pmeTaulnTFW3'
    '9U3WidywLBJTiEIujNxFeO+osGai0yuvu0JCGssKivYtUGFa8+LMYHQgcKG4KrKwDctzVCzVc5mgoJcWrkiQLUocNnhUJPWe'
    '5RrcLGLeEShfhpN7YyRSbjydsqwANJHnqszmpTCbJNGS67Axeok+35WDxZpNwDm9MVa0XNITbGRH/KjTdf3arwthuomSOp9u'
    'NSE7AzeOxiw2oAmmm4a3KDuvWa28ojycIVc+zZbESlOHy1ChJCURoT6lv0S76rpUfkooJpLXnq8zWCONvz4hMpN+JVU9GKLS'
    'eO1sNq9YtPIhXOknWY5kL4bgnaeTdu5VkhuK+104dRQVybLnPFx5Y9q9u/QU+LVxp7ERRSGwQP4t8smWq4hPdvOPVX1tPHHs'
    'QGMip46FaZgnZ46lWusOkHZaElmlutvLZoodQfj+W7DG0irn6AaiIncyLUyiSVBemCojnPC+bWihlperr3xKUKG6TGPSjAdQ'
    'ySrYVZH4ZlLK1sqICmVpLY9vNYhORr9Kh9QlMl2OIpEF6AgmFyYsRAfNXfXxyBLeS6pRJZWc9wMcjE3mysr4pfx8WfWrfi5Z'
    'JvFORah06o2RBFpVfeN4y0ZA0azCJIPzQjUtNEo7CyvJKBXtSqnsUjEGhRjCwdKZdt2c2eRQhISiescVQFLYTzsnnzSWRRCk'
    'O61nklVCG0B3uA4htYTbnz8PFDDr2hrzfSw2jfNE2ZeaBB5doaGo35fj8OG+V3Rfn2ml48kl1y5yqhVYKFNc7OJ2KGXOHtA0'
    'Awdum+/actem+aMBbTHO0CzJtyXw5WUe7Ovjyl0qXLnF98SJA7286Gp/P1eOE9COXC8zoTu5LLkjFck8GlHueFUzvxVPbmzR'
    'TE2xXfGOOc0pBRX1+vC2nsptyVeWYDWH18jkgY20pZzgI5aSa5atXD+CUyb46IyJ0IoONVyTQc6CTjA8sBAbO2FZKueTc/JY'
    '9UyRk6cSRXq0iyLrZtn6pQo7j/BGw4nWGbxOiYwxnB9jGysJiNTntD/1YxBbG7XCuuTgHE055FNr1GHpLuu5EHAlQsZLNTDR'
    'rAWpjb1dlSmXKg+aziWYVZovHp68fbDgsqStnzFi49hA8oiZ/nuRZZiuyLZHCSdJVAcLuQkEth96z+gcPJrILdY+ZWjfuA5e'
    'yeS8ZYWcp1YsoWK01D3rLfFao1RyUfsWDIvX9wTqsyXTrFVbxnhzBl9C/iLIp1qX6wQjsgcKU6ORr0gNuTdIdfVuX9YXgtJr'
    'VRxHLFkBntJRzUHY6iM4hTNp9ta6e7F458krmPq6JRsBY8Ozf/0NxOl0oKO3kMPNo5c5zCqXVgXqEukrk42nVDwVqwwomVUG'
    '+lbhSZKKptlqScP+XOurs26pbLlKGtvS6BFMpvVtTXF8VhqGhpINpxRJxms3pUbBtBYe8y1Sfi1D9sQkBD13kBEkBXmlIyw7'
    'KhpJRc1VJYh0nZmFPTOUtcLFy0dOqtDJeVlcdD30fFNr8KKcVwaCmSKVQa0fo5bAETJy0Uae9kXXJuWTk9WTcDXZLX02tPlS'
    'tF68yMaF+qKGwFgRYUihKVGc6YKkHxt0qYXsflX02JsnFVXlRohwaXKEaimhECGxYDqkrn4ecFGM8gxpCovEVaOyXb5QvtF+'
    'xi9cKwVqn2G5nKhYJjYvvRMjl4/VwPQbMUTb0a+IZdYLqWhgznWgd/DdVMhsWXEnqpnp660pMHRbN/WElDIBk2FmV28JzE2h'
    '/qVaY65AGDsMhhyLMyam53XqrkdtUglgCROl10NseV0MQWE5iWrVBFxrMRN8sThc3joAJ4wq616B96+UlJSVwXUBzQZ/g2el'
    'nJ+sdu6CRGf6GFxZUw1UNNaWjaZXcUm6qFp5dbA0540c0iJ5Up+3nuUqL75EoknRaq8welZ95CxJL42Y60rVV1HKUJ3Pm8pC'
    'DdOX1Bya4kYTZdCqEeF2mTIh7qAolZAWZavHWCdrq6/wNBFowbZTBM6g9kco5XHiCvRKoz096rJO5SF5jKwmAMkDkzZtXR5o'
    '1bVlKSTU7lWt6Akh/ZQqiyTZuE9zvhCr8XmYHzuu2GAAbAihFU8OowxJLM3NXCc6YUQvqSwwGS+Wx9lbh/U8TkYbTt+jjMN4'
    'h7McUIUIPu3YdUSxWXo730oGXZTGSImwsb/x+LqxSF4dRWiRSXn6EkN2DGY1Yvcvu2HK55UTVSENTY7vLNN1e62YTe/IQmFZ'
    'odMECfhlUiRikT9WEasrkBraD2kaKaDJsWouekSbfahqy8lEuQKHpchMK1Hy+ih7NZKEzlLLZODV6gs50AxEXMAc89Corv0d'
    'VyFgeOei55hJyxEVp0Cj0KlhxWUJTkHpuIL0oAX2a0ozaVrircHESTPR0qQ1JZuG9eM6LOukH2IGm0aV4c1sQxHlUI4otQ6D'
    'Fg2w+QGrUr4OY2ROqA9Eh08YiHLoomSNqyc9orGtY+E+BfoOE/80B5qnyFDWH/Qp0oZemNx4Bj0rSZcq5CmdN44AVab1Zzqm'
    'rZzcBL3QK/qWFz2cJq3IhHJf9UpNXTgZZN3qcXYCpTezlPrrhE6KRQFU6UxOWaXkve4EMj2JcmVp7PM5oIRQKswR79/B8KK+'
    'isWp4nASGZkSfXQCnKtpg50gYrv+gZIcX+qRACZdB6UtkJ3aeNhuhwFsFzSulV02y4vvEHM7WH8XeKmeRnBOyvfRyYKwQQpS'
    'leqv0TybFFeBLqzoNTEE09INsoTniKKuW0+WKe6bxS77Kk/wTQEOnG0VxqtHA7zCgnIJqFMi2/RK5g2pStjmm7oxXJ7Cxa6U'
    'PDqzMCAIPVvRQSATFXBzsoZWNmunDhNmRFNKJBwbVQQXJZSV2oA06Wba8hkjgcxJJ4SKX5/lbCQwnidOnu+jpVOEVctwkqmC'
    'YmDa3A5aRRuaiyYdXB7mdW0YUzAtn0CMyaC2kppWQwnZHihAENCQKuXN68dYTdRKJOgSfM4eze2O65QTGFynidAZVbtJtOQV'
    '+Nyt2KhgUES10k8s54jciLNExZsol5PhjvFBWmi+wMsCa4LQK5uakvBMiU9+a1eQ5ZMpXXgYJqKJhNTCWgbbOME0JgSSl/BS'
    'a7xsqrevU8a05f1tasJN3jITAfQB+l2tJR/SDUOcZkhlg3YSjpqQ2k/uWvYlpkb2tVg6oAZ+yBQosKaZQUoRBQFnujBkVbtl'
    'xooEqyF1DlRsTpdLY45wLR2V1xMUpWs4X0bbUJqaQwoeZvhHEqU2qupt4sLPeY1hsdCcnjyXrjV2PG0ILzMfpHZ1UVebiom1'
    '5A6eQVDMb9dlzzPZqUp9ZJVJLkptQWETq0G5f66XEaUb0JOd4xVorDgC8ws4JO+YwNypd+v2Cm6iRiyplf1hRVeMPK+opWC+'
    'NSM7ybGMN43VPHYdbYy9IpZ9HTN+iWKbVLY4xuL9NmKaE+YkI27HrEAcLB43q0XXOcl7h7t50QEnqWUytP9h/jeraZxWE9fS'
    'K3zon9Kx7REblsdK59NLuRgIQLzmNf4aVYCpN92XEJXwOPmFiDyxOimEAh1CzF5JjElqcKYXWFgTUHl5MtaUbppo4WevZrdM'
    'EpLKuLG55g81ZTKNRk6CT23Q3E4RBTx11Yh06OFJLyasJuVM9XeDOy+gxSplVAXKF7m22LU7uLd4yMlrK0cKeRwfWaOzG+dy'
    'BKqSgX3jYRTKm8grKz5t+yapElxvT4kqJimu09VTEKFKxFP94qmgp/TwUwoJnbavOnGvv69xK8lr3z7cfzh86/abyQfeV/Cz'
    'p69YsrnBwBfUl9pd13Zi92H349k3hGC00lt7EFeMjOW/d+nx/wGY3ZP+'
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
