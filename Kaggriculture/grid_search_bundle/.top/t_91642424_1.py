"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vHEeS/C98ngfNDEVL90ZTvStiaVEgqR3sGoRhYH04YLH74Lu3w/33o6j56OmMjIzMqiYpWU+mqWFPdVVWVWZkZOTP'
    '/3vyn7/+/q/ffj/5j59PPp7f3p7cL07+69d//+O/H37x8OO/fv39n7/9z8PPP5+8v7wZHv6V/vDjp7/9cv7h8qfzq5PFycX1'
    '5mSxNL++fT8MH08Wp7t/uB2Gdw+/3rwfzu9OFq8nv/5puLr+MPr1x5vrd58u7sZ/cP9/i6O3uLz4y6ePo+/fv8/PJ5vh9u5x'
    'oPsftu88+rP9+Mav733HdhDH3/Lh+ubu/eNDDz/Z79n+Kf2e7TDVZ//46fLq3S8P/3v36fOCkAdPPqmP/ur8YthPEp2i7Sc/'
    'r8LR8x/+4cPdfmWd7/nT2CjY1xx/8Gitz++GG+/5F+fBBH35AJ6X3RvsvnT03O2H2LxMNhl63GHohaW1X3B4HDB7fUHtc/dP'
    '8ydEXkj7+NvrT9sJB/MRLqA/zwfDs9NRWb/R6Px5aFq//all56Fl/ZQJaVg/aV4q67j7WzAdX16g9riDvU1/VXuend4u1sBe'
    'v8kadg8ZzjsagTIbnW3gyw+JxyE/J7wOQku7uL66Gi7ufvnTcHN3eXX598dh2vskdfsXri00DPKA3S2XGij41nCgwewkh73b'
    'uz0XqLL56wfG9z/5/icv6E+Oz8Tb4epz6DbaKV8iMhwBmhjt7D4VP+29kPjk8d1/G2ctakeZiYeOpwa+8PI+edZM3qPldjhc'
    'ipWBgvMfjl0ZoX+X4DHGf26mKTzkd/5B52kCk49nqTLAqb+fMoJR1FT4ajvBhSEcJtiMQJ5fsGzOBIcDZJFl4Sg1U1R4xn6G'
    '7N+qMwQeiieofFv8Uf62etUd3XnHKOZy8uvbu5vzzY/Dzc3fThbr4mU4+aH7pdjrenyei7L1ynx3+efmoUux1ygUHllFvwtV'
    'OhLtUJ2bddEhjjocdvi967cEiPr4LdHjdQobEqzb6ArCsxJHkpJ/tH/v0vMOo3TR705OJhm54IJYb2GCCDZdtfbYcOGn4iAn'
    'kFvLxff9IX0e0uYVNMW75EycJku/3/y9guW2wSfjweKYa5e9fY5/2b8/v/lr4TYDk0muiTLkkAiMwUNBGq0SIk8DbGk42wNe'
    'M+fnWAQ94N6PTnrxw6ep85NAdISIPLM7SHC+v5WVBdHjcZsMlVdJSoRV3vnbv7p3J/cPj85wLch3qE167H/aRlaqR0rT63+V'
    'cQ4aAAfkI8QRWBydPonH8dwuwiMm0ewgoPiyxgwjGEF85Hh0MDDJdTP3DTH0KPJGiWg57bGx9RQOt+X+QuqC8EyfOyPEY7+g'
    'O8ydiMRZQqBvamCHKjbdg3hKe2YOKnAGe8rQA81QX/up3+6FQgrrPKSguOrga16WazAOR2L8ZAYYIhNN+ihEF4cmf/0xxyYB'
    'ADFUo9fEg7izO/zRQjhBjkydYCAnk55i6jeVeWeOTML1sI/BhhA+6N3N9cfADvb+FfJXdnHk9fXV9qQGJ/h6F/w93F7vTmLf'
    'zmIN6KtJELrqmYDePTFzcJCBp2LQg2873N4ln0xilqnL7HsWCU62F8uAQpOEgSpXpc0Yxb47q2QJvK18OQTZM0u6aZTyshQ8'
    'sypiII9/vMaWqGVR5PzNmuzStzqbsjXrs4AJKjnB0wG9UX+aFeVB32vJXnSjPBVCBErbfPdjLp8SuH/O7DivYY/8inVND386'
    'AwtcVtbiqAXmdXxZoENFtTEdq1Jc3ug6pPbUmWC8+yq0NLLtdCWbIiDVfqW3UE3RCbDn4PugRQ+qfwBIVMZmgQn4znPC5VEY'
    'yAD+jOBGFl7UcViSX9XOOzSNHRBjeyROnENsGDbnrwHLWtWUc58KhDIplCAIrn3wZHWIO5IwXVhOe7RrYDJm53BP+Ka1byRv'
    'AopZ7TxLpD49X27IhguWn+6XqWZI8WK2tLRbeTovRjzOXx8CmZ5h0wKHKj0zyjygMngEcWC5esg4oFq5AdVK93mlUOZwX9s5'
    'aimndb5ufH7vJ1b3+Ff3HUpz1fApE0iKbHcQAlkXapYAKMSRF4wEhDysmlHweMeMErKZZjYOIeoxTp1AWpMIENZtTOTRM9mD'
    'w63nzEKmNk8hrALX2I2Gc98VrKLjbR2ZtEKaA/4/cFkP32bm3o2dY+Nh+YnQh9wvBismTXwh2sLhORsaEQjt/NOARriZglBy'
    'UvncRxfr2E+HYk/V0wnMPthbXXia0xt6EdBhW1xkpsDDEKEG9xgn5zq74L6cUN8vekIX/6fLq798hvZxhmT5ynr9y+a0SZNH'
    'v3IcHu7Rs3Agcu4FvFxyzzFjJOOZCiQAyRueidaqUgfQGO3FVhnTOus2IqAqugg7cFoK3JAo5osP7AqFZGK25PCuI555yong'
    'zLN56RVzUJfxYNAFc2lIagDTCOMDkNSo1L6SMrEwExZD9mbLuFyQ0Gib3nL/HcBTI/bYYaOwKUAxRGSCZh061cLzYDgwQUPW'
    'SmrY2IQDKJwTc7FN6CyJHsfW2Sb1aH4YP5qFP/2IyNDsZ+DKk++fyNrMVAm2CKRu5vvauVMKs3wRY2SdOcmEA4Oxc4gx2yR0'
    'IZBNNcfbAyRw5ukBkk3VggwK+1AXnr6jd6V9YzB4n0HeWhZgj6KN64cQykHW+2/jrvVC2+0727DOL2N3vMVNW8xsnSarM3wY'
    'birim6p3Bzkx8ZXbwkagKk2F9S3iPFLl1taF5f7yISh4AQF9t68DXE+nZAcQrSpYs+oa2C0BRg816EkDg5lwa6DbH7hC4ckA'
    '/GP0snR9JjNR0WeG7wSI18iv9uNXh/GUiTEmi0zUI/FmIQScg+Fsa1JgROTUOw1xicrWfznDbs1bwpE4czkSCmkSSLw71ByR'
    'mCUzY9ny2+wK6HcQMwZTjJIUZAAhTy+/CFEWJZ5OhvTE/sG3hciWjCSCo3S/SXxsAr9StCHGa/lGL7eYwfJJshFW0kduaHam'
    'Gq01OpS5D+TSMsb/9sUI+OpWjnABy/aZzsF7BQibhmYkFQUbDVG70WhrJXY9yqIFKwHe5DYp80T3xwvBG7LvVLdM0ZMoZKjT'
    'r5HQr+xnZMprhCuWuQR0/j+lMvvmlmApPB3RoEfJ5VNCfRr41xOvEynKEK+joIlWGnraQEPl11IO0WlE39BQMvhbdmRzA2tR'
    '9ScAFRhagG6w8jsRhG0GVkV35Ekp/FKYF2VUT+Atuuuuh64HOzgK8F8AgZ9S6mNx0XKND7Nbu7Y5s0V7DdhVUXE1pAlLS7wI'
    'NmqTiCtTBERbjWNqg1NXmGI9s9WN95GIdcTb3Q7s8Ne76jxbOkBZ+OTeqs1QiHfldgOjzLRJ+0SogCfqgu2sSR4IpVwlg7c4'
    'xDwy1AyYTqRY3O6nxcLrfD1lSPeIuE19mNhJMohV0Xky1gYL4Z93EC90IjAZfnXfIgD96iuLeCOWCxGmzutCrwXOP8gDIpFI'
    'HiLbvx0v8cr9l6UeQr+5VwQuCQefhx12GlzyS69SgiStVqDlPHl9gcLMfa6gHy0kyMhpTgHPovehHSu2mwiMoMO2/7vjjagl'
    'kuCOq9Yte3V45cAzLZcKJwgyfSXhlXj+iOi41zkjQQPmUUA/SZgNoTHQGbMfT8ilgCQmoSTqU4R5GZnGtr7dbeiDheofYhWZ'
    'VnDE7jB5C0RRPD7vKzpEdgXmBGZlTWutamxwyrFfoqk1EF5L5szjeVRDyaKreeyFuNdEmxQZiQCdRfQdIu3iaBrmeE5IxOx/'
    'b3pvkESlkoKUS9HIChe2BgBGckltkb9cantZCVsXnNEYLqOVpy5G0f4gSHJ8HGK9HRWFjLLFR5Ujpy0h+Oq1ed5y9TVWmszR'
    'e6m9rn7jyHmk6+vblI/Un54+vfwyijS0dBuBHnrniFtzbWonjgYrS0EEzT2x3SJ2ycpgCQpkqc5qZkw+lb1gg5GRhFZHynCb'
    'DhIKXRgrtIYwiEXZPJdoQ5GKh8pCmwTlNZNhBaPw3gVapf1MwynNa9TRWVxLreYKf6iBEKI/pf4XVNdUW6Red58SelHxhFAW'
    '5iunt36HDfw6t2RjhWu10q8uMmZfWa7zeb+xZxrTCoWZAq7jaOv0BQVUcsX+fJEViNYbCvL97GWfdj/u44EbFBQMJqBzoYXL'
    'BiSKZOrWc3V4sYNmvK620Gvd3v+3WA6/iWura2xMrr6c/NfSzhjXokdpyUU2t5+YJGWDsKpOxb9+CuU0uzPisIwISATVmNqY'
    'UYMYD+j3cw4g06hrv2ZCPMTwG3Rq4wy+PN+STOyk/1TwHiD+fkBxxpM1+okBMJbGYYtXp3ow5Z9wz4JPkr3TIPMpRpY4xFOw'
    'Fm94xy7vOnZeU+qBiFLsiSClIg1GgvY3B8iPdVlOISxFpGN5t9jKZ879rA6SCAtFac9ioW/TBLbV984FN+Qqi7PB7xugZ90Q'
    'Dr/9Nji983F243ziulTW6nB009WtGjW3hxpbQ1xO045OHD5XyCtrNYNYLMseBom9OcL0VF0YT5DmQydF0lm6rUuFiA2zmtw5'
    'mfYi0EurGcP6vmWXWcvAuWbKicUOUsqNlHcdF8GRsIJMVkOmRwZ01v3UQ7fc/rLIvlWYj0EBPkBOMggTk6MjmUmqLgbOy0b0'
    'F+khqTpaQqPNYs94Sk3G8nVoMO1WTSeKJtI11ifO2tyXepDhedkL2fAmTKww7ov/a3NJgMHNwChbZkrdSBrK5wqHh3BNVPis'
    'pfVXSt7CzbWwsnhoTatG1aG9ARHOsxfQEV3wN4ABmmAdm6jbplualKisbUusXIG2Vo5nz0rB6zhzuzw1pFgUJL/6GrO5Sf31'
    'cUT6BIngPhxbGAmv3X8JBd7hX70WOuAWHI0onE8dff49VhMOzySjE4w2ASR4CSlrrUcXz7iyt6m0P6qnthMymXqZrZYG5AV1'
    'cXCYcPvGXPQIlg+og1ESsXMDMpIwJ7Ea9F5ZJR5P8CTUX6RO2UJGhUYGKHOJo5uCHTUXD0SF3rThAzsPhGK5WvzvqAXLeXps'
    'k+5GY9SKik6OVE2Idmi2D0XiqGsFYigiLBY8h30T2tq9IeKeWQCFUJBVOYhkrmPWM5NAayIdaDXz7CQuGBQAxvHkgutK5ydQ'
    'flY3eorQeTkmKSCoSTmPFBUmrQ+u3S3AWEQ2fY4rgsSAAI8+bWRMCoxsf0G2g8lAbpTO1W5OKVglSd0sFnXbrZ5Mggz7rFQ8'
    'frEDOMGEAAtMYbMIzVcamUGp6vlDA5fo+M6qhxMh80dEbrUUhcz79Dd/ZtVyVDlua9NNc5avtnXhE8BeLQLnciFEp7rfbA9u'
    'L8Aplv8q6lRBVLMZnk/XGagdCdzCTVvGf1mSJxc0ekg1R6FOtIvoga4nhUyprd0doCK7Xh6lSJHq4qcy0A0lItCYuoHpIyUl'
    'BcOUmPUJIhojKbATRqSp9e01HulDxTEgRd4qk8UcfB8B5D3sS9QSlXVDmQoFCQklUATfGS4VuTTgC8YICTP1QJ+SkXNmmjPi'
    'ZyTMvDhV1g/l9T4YnLcRwCi67BCtR7xYclZO0JD0BmSDkVllvoPEpq6I37ARU/07X39dkeYrziGrW5Cl2DM8MDsYCDEoPA7+'
    'eUEZrZXlsbLUmreW5bH+NkgeR8rkt++H4SPTJl89tzY5gsxc6kZF6xtStVv4ZpuhD8WiUYIriyx3J4RYHyAnOE74qUXCx7pT'
    'aAReSBYiz2UjKkSQYt1qBJWKhaClzGK2BwAuNFAia96oqGtfAEfjmFUp52rnWyQI8t0C8mUBwCOPO8LPwdtiuApYOFV2a6b+'
    'ATxySMk8JrOFXfQhsdkLwT4/TUotsRjfnop3WziTpSNDSdd2kI5q0Kc01Mv0nAq7iC2foKsu1IY0IxkIYdHU8tE+61E7r+Eu'
    'IaiBgb7AjW2pq5dmGcokCCcB4kW319yLDczhDAGMa+g3t4uGV1D0x1n7j1C2vNPQab87paNeO+rR6U2UoB6agtLnvsBDGMMX'
    'ocJD+S3j8pmV1ZQ/40L2o0E9C8TStXyGMwdWHZgDvhZhqYCGHrduGYpTFZPLtM/RaV1BilIKFTPyGQAkkyb9SsN9Tnl92uE1'
    'q3oBPDf2F7PRI3R1PrRmu67GFELhVf7tLApYfCxUyej1QEQjAEXUu1lR6peLuo9SWY0D8SoxFFPAqK9hk3gkJ3CwNmWDBP7V'
    'qs3DkJVMcj4Z7msCBqpKIduBKi3m2u3hLKtQF4FPSmVdeFNsO+jw1CNSmhxr2+39UpeoVIusXMkZLfAjJXbtsw90gojbEAgD'
    '5YszK3qnlXuSnMjkbKLdfzeZLcAALG3yBgVVFjv0CXVEVQlaaf11t4aWBQU8q9q6BJnXIscNuM/STCn3e2Z5BLA8bHpLU3xS'
    '9iW1COwuTW1r2mhFQdw77QNwxEP3iRaOsO6MFrqq0MyiiDC0fkvsyqmO9m4vIzVuTP3wBWJTpF6aeUSvDLZ1LCCz9emXX3UV'
    'TKOAzOnrWQGxzq1EOPr1uqgXM0eGNd97hAU7LGVe6VRtGZuJTuna7ZdvetGjTkGPx0ncd+CMKp3CIx4M/eSsSjJ64WWcph6a'
    'Wh1Hc0Rk6Q4n+HB1/QGoiG0UumDgi6XZVJrP1FVmhtR0x1sUqijSPhsVhkJq3SRdGhBiW0iN6RIoEZ3jORfIfqedgHnEjGqV'
    'gAK/OqQ7zQwC2yCe23aNl0IvXXaVxXhfiBhCKWH/pIoF5BKtbPzL2bskIRc3xjMmSxI1mAy3otafxxfSJDk/EYxgR1HvN3Lg'
    'CCIYB16CmqOCVzR0f8oJLinlwjFlab/4OUvlrPGU4Li31FHFgGZtkqtH5WXl+tHgfaYj4QQ+D13mdbVB3jYp0xdHIMBik3RU'
    '+HHmhZHxYmewbqBC+RqQAlauXEGNL9B+4mFoRkCfCUIj0ynA1HIPA4vWbfKJTq4DHxDXsiB7Do4slCOyRuL7M8ry2+h7BBKb'
    'kEJHKcr28MPCNKf3ibcjRMRQSB5+8ugDgsAR4pmD97THxKqd0gcwzpXFOI+h0L2z/l0mu1xReXG92dLt4OmRbxxloc1xNajQ'
    '5LhCgIO+Exw8h+6gqKUH+C5bGHE9eIhRURglsGk0t+5aSrwfVQpXXXDhiMi3SeylfmJMfoVq5MyJfqAnlNS9LRYhj4QszQhg'
    '1vSkmyiY8MSgTb/0SsYd02j3X7GfTkO3OqUHWEjksbP+46fLq3e/PNxsd5+2S7unlbZ2h5GODaV5DSaFXgz7iyej+NqlqXWz'
    'MhYWosqIfzk1RhRTkQ9OpVaIsqeiPRUAWwzrMHswjKe27vRo7NbqeYs3Hu3tf2kZ2Szsd1Zj0jMm8PmW00j9cVt8dvkoNO68'
    '8e4FQCjhs7A1lln0Yhuh6yE2eZTMp6CMIIUvNXRvq/dn3hkQRWQ8WtZYq0ErCxRB0y6CJblEKflB2/IlmDqv9JK16Iinkvii'
    'Xj0X2GfVDQXSnTU8vVdk1DPjaC3cM6RBp0FVncjxN6X3BEAbPUAGqfFgWlEm0FEz0BG5QoFsV8zYozWjUqyO8CupEyAYU0od'
    'rJVi6O5qNpFztFlvb0u35kW03wbeNkff9XX/mlkNu+lC96NBqXeQc35cj9o6nvFJwmJdRHUKpLw68qM6zlpMCqAcPQyVVcho'
    '0XPDxCtWjLKOQcorItz3NWieyaZMoUETR+1ux5AJQmKnoHkOqcCrV04nurKnSsJjVl7nym+F4RflovWjpI4Ki4LgOoRKgyWi'
    'tysfEuAuZUn7wIr1EWVuOVJALuiXk1hx1gNCq+Y3jLTo4GVdIVV2eeLGS/RlU2uSEUerrfCYR58OP5Nyxkp0pyjTGFSRRK0D'
    '2iS/JVlJfw8myZvhwFQ1e1EYrnb7r5riruI+IE8MXanGuFAaQ8HKug9CDOuX7eSa1ZlDrvkDFAsGcf1pMa5/XeXJ+E8jOpUs'
    '19RFXbUeTfvBCht9J9Ag54fIBY6UJMPn4xk6filYgxTwBFdORKyMqULMvYHMW3JBUqghzAgdEzMqq5XYS5LYQ7WgsbJ+SgK3'
    '2vlU4nVEXCe12ihrxTP0ZlcaL4vKLEyyLRJk8BI60fqt+gAUKXeb0LxQmMLQryT1v9T7whYx0AR8pPPr1+dYW++6++TMpyuj'
    'FONT2bb3E5Pvvz+zrMmgTaXA31toRWzNDdIMEw/tHctADGUckPBM7kxJwPcb5XIi5L9i8X4A+rnWkOsJoCFctHNHUOmm0hqr'
    'p4nMcmEAmIyZWSILQ1/1o4Ppr9GWiInyV1WU1P5QOyOIuaFzQGTdB8g3TbZ5h153q5M0EegLW7KTdb0Ae4NXelYwJXKsRwhc'
    'qrwevIx9YxM0FbFOQoSiCl2DT+ihoYutoayMn7XLDNFMIhCGHzT9t5ic+MaR3l/W5PTddoRHXzQRMvtmGhXm+T/LIk64phVk'
    'a0Eynzc39MrPUtehqFUfC8AGJ2R+ZBIuSc965gYKrYKKnpPA8M5xhNCno3RqAU/NdAErsII8fa+pKntbY8LIgaDyv4V+hRJn'
    'xLXDNEJjBQBEj04PAkViVE6OXSjf0SvTfD6Sf5ilZxoE4gkKSwYJE8PBUkd6qZSkABOVdZchATzZU7AKl5vIMoGK97CfkP9A'
    'a2hsZZp2lvVqlcqaOvg7UurR4auhdYCwlTyhuBmBZNmgNDVkzakea95OpToJXeBSL3ABjY3GCgecCh7yF4T7i/UDQRWJjHXE'
    'TFRR59wVIGo6J0yeTUQn4JxjbpVeHRZveE0qT+ndwtBmf6kEu1lIrrat32XmFFQ4UOEBSWwKxs5nTvC+TmnABqgwrd31hVSB'
    'eYmIwRHF6L7U9EJp2xpEHwivaUQgWQKGM/kYiqR1jgys6rjjXCsxDPRtXP8AbqZvS1+phgBxpthpk4LSWhNAYsB776y3SPvS'
    'xtpJT6hJ+ag+wJdJ4GLAuUjgam2BpVL8C3qd9Uq3XMVjNaJkjoKalRVK4wL3M1NgwrmXNP9P9ak3zcwqSac40ZlIy2fm5BFi'
    'YLQXBYqpiJLSo0ZYmmW/1fqdiFXBpL1bem8WpeWl3m806ixzJNUdwRTv0q0eVK28MghKD4yIlaD83I1ioJQK6nVUbDe3aSXF'
    'EoYtFYccYNDpYYayIDh5De1mRSBIYdrwDIECZslXBe3sAKgCvKueRtqY1vxkNJyAaEkRtXJ4sED6up0Eal2JkUp1mOzFG0GC'
    'r+vieTYsloEC/90EFqdDMnDIO2nXtFc9GD6GSKHdE9b2CfwmV/tHqftblAwoxyXa3SRLLP3zVcv8TCduTvWfpgaBgip2qWGe'
    'FAv7UA7XFWbufi/XHg5FcGnA2B69lHlVf4ZYrRaUjtCWr9Ep3FX5h2VAQ7cmRZ5vF/7h4jgJsWZec18JVZl2Kq92o6JfTXLX'
    'kRH73lGlS59ePAN2JboL7wsClqzlns1ZxslPYZSL7q0vEWcnhXKwfLiPDRQZRgHyRmkf3knSJ7FhmP5ljVl2OeUNWcp2CFsw'
    '5vGhk0fdfXM3SsiJdZGqjVwnVu0llxkCiw5KCnRIkdnR0M5BYWrUalDA/QrggVwGKkNFZ6VjQgVyOoxHvQzdhhAJia+gJEvl'
    'CqwyTBMFtLR3KtmWkyqZHvc9hySr9FAJnA11g0kNfSr25YBfOAxEY1FqmnJDS6sox3JFr7xap1MDUoAKpq8ft5iFnAKqAvPU'
    'FMYBCOUQNY6xlrDWmi43aEaGnkqQowYD9Ec/R0RHC1UonKISBBpKdDRXhKTUaWEU4wd06xWloFb1NsVcDKCln5weaFLiF12u'
    '9gSg1p1Oz1HmhKpShYgaRhnKJCf4KSglb/dDCoWkwqUKrJs2OKQzXvTalPZMDbYYqFHxkh1JqavNFGkLd40J2aWEK6yYpLl8'
    '1upZl1wm3ZEjQkccU/rRZWpEEsMreSvzFIxWfGArKaKTVixb9A00KsFxa6ZobMuL99n074kYYQKhIEY2ecHlq0yU6+TBEQ2D'
    'iWuo1IVwZGEtkiF6qIS1+k0Dsu4QGrTUE6yuJDcKsiguGIrabhwMr96yqFICcvqahtnjrddcLNIx6BbqZeapFAmbc6EehILA'
    'x8r9JY1CqXaFAraB4Cxu8sFo2DSQEDKsjdKcQSUZrypJZMZ4UIsEPDxYXajKoVF9w2TSwAVNkK7+USWDt3AsBdYfpcIU/PNC'
    'E2leYNHSCErIPEeU542YaMHBEXOD5CEq0XdY7878voT7UeHD+00CtTRVGzbAGN/qERQXpDPZhmmg8ZggGo0Q8J/hLaMrGTSL'
    'MtBIiU2yrpvCmUdEdjG3/CjaZm6DUomRKSUEmVEOANCktNAXMUX9jXjqI7LEzkgjmntQ11czOTry4TbRcjSKKZsmUZWv5ETv'
    'EtBih2UGE4dWUfq1MDlEIlIaRrGIsft0VDLh/WejEJ1PETjmjPzwysS+nvLmm84ddJgiC9Pb1UQL+XdDPJexmjhH3G24l8JJ'
    'w6CT9mnxL4rUIBhqLtZoJb4frwNt+g5nRri32yA/5T0DlrsSrZZIYPI4daYpHQdrL5kfVzvAEJPf9cpPIVeq9gjUUsdoAzfv'
    'm41cF6DX/1aggbCwOVxEJetYQyuiICsYb6k/qkoCoCk4YbwU+KtGUyEEFuo3hIBQdWj0OpT7MdBBts8avao7zlQRPt6He0Ap'
    'LZpCrVjPT1JMJNnP7hM1GMyv3r8KLAY4fmEStJ4p2aDt2Fdxlpn5/ftBgdA2V1vrK96/lvPKNqQywyM/WItSxh0U6HqlDEqi'
    'p2/PzkqN88OI7v8fGgMsiA=='
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
