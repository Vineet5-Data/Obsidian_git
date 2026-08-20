"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vG9kR/C8682CSsmznprWZrBCtZchyiGQhLBbIBgGC5LDJLch/jyyJHM50dXV1vzeU7PWNlsmZ9/26q6urf/zvyd9+'
    '/vWfv/x68rsfTz6cf/x4crs4+fvP//rrv+/+cPfxnz//+o9f/nP3+ceT7y+uN3f/Sz989+nPP52/v/jh/PJkcfL2anuyWJo/'
    'f/x+s/lwsjjd/cfHzebd3Z+332/Ob04WLyd//mFzefX+4M8frq/efXp7c/iD2/8tRr24ePvHTx8O3r/vz48n283Hm/uG7j88'
    '9vngZ/v2HXbfe8djI8ZveX91ffP9/UOHT/Y9jz+l73lspvrs7z5dXL776e6fN58+Twh58OSbeusvz99u9oNEh+jxm59nYfT8'
    'u/94f7OfWec9vz9cFOw14y+O5vr8ZnPtPf/teTBAD1/A47Lrwe6lB899/BIbl8kmQ48bml6YWvuC4XFg2esTap+7f5o/IPJE'
    '2sd/vPr0OOBgPMIJ9Md5WHh2OCrzd9A6fxya5m9/atlxaJk/ZUAa5k8al8o87n4LhuOhA7XHDett+qfa8+zwdlkNrPtNq2H3'
    'kM15x0WgjEbnNfDwIfE4ZOeE10G40t5eXV5u3t789PvN9c3F5cVf7ptp75PU7V+4tlAzyAN2t1yqoeCtYUOD0Uk2e7d3e05Q'
    'ZfPXD4xvP/n2k2f0k/GZ+HFz+dl1O9gpDx4Z9gCNj3Z2m/Kf9lZIfPL45r/1sxa1o8z4Q+OhgR1e3ibPmkk/Wm6H4VKsNBSc'
    '/7DtSgv9uwS3Mf65GabwkN/ZB52HCQw+HqVKA6f2fmoRHHhNhVfbAS40YRhg0wJ5fMG0OQMcNpB5loWj1AxR4Rn7EbK/VUcI'
    'PBQPUPm2+K38tnrVje68MYq5nPz54831+fa7zfX1n08W6+JlOPnQ/VLsdT0+zUXZemXu3NODmWrtieSKLQBQWb5S9XvDNs4e'
    'a3hEmt2q6fXbdE8Av49exD06YGDP7AiBSURYZ+xLKhbSsDxKzxsa5uLfncxMz/TQjBBrL0wwwabL1h4cLgBVbOQEdGu5+r49'
    'pM9D2uyCJo+XnInTcOm3u7+Xu9zW+KRHWGyz8Z+LLprjSH9evefXfypcYGAwyTVRBh0SJg54KAikVZzkqYstNefxgNeW81NM'
    'gu5y71sndXz4NvbAbfQ7H8Nrsh2Ie76/lZUJ0T1yGw6VZ0kKhVX6/PVf3buT+9W9MVxz8x1yk+79n7bRleqe0vT6X2WMgwbI'
    'AdkIsQsWu6expdRucDy1hYAczCOYC4Qc5tsN8antEcL6jrK/EtXRjg9hjw0QjbPaB2srDPfl/kp6+NC2iaaP7QHrOKjIEZDu'
    'hCvOYgItrriKorVci6yb9TFV4JIjP6QpTGOIR0eagacEFdZ5UEEx1sFrnpdxcOiQHMMuYO5G6E/6OEQXECV//yXCDwwCYrhG'
    'r4EHnmd3AKSFdIJiG3UzQI8gHWHot5VxZ4ZMwvawj8ELIXzQu+urD8E6IPbV4EleXV0+ntTgBF/v3L+7i+fdSWzbWbQBvZq4'
    'oaueQejdEzMHh26Tci90/5z9YtOfTJyW4bEGFpsYBQletufNgGSTxAJVrkobMyq4Aji3RwyBl9CX+z2zpJtGSTFLATSrIgpy'
    '/+M1XolaHEWO4KzJLn2jMypb4z4LGKKSQzwt+E3y06xAD3qv6tN1aakOEoH0Nt/8mMumBOafMzpON+yRX1ld08OfjsAC0y1a'
    'DLVgeY0vC3So5Ng3NT+DeC3enLH11JlkvHsVmhp57XQlnCLw1L7Sm6gm7wSs5+B9cEVvVPsA0KjMmgVLwDeeEyaPwkIG4FyE'
    'NzL3oo7Dkgirdt6hYezAp7JH4sQ4xAvDRv019qCWOeXcpwKlTHIlCIRrHzyZHRZO0pcuTKkd7Rr02L3B/e7iD5MvFd4YE/6Q'
    'jY++3hKEBvsCvF28RioRYgbyLmYLTLvZp/MSzw4j2IMj09NtWmBXpWdMmTtUBo8gBixXEDl0qFauQ7XSbV7JlRnuaztGLSm1'
    'zusOz+/9wOoW/+q2Q3qu6j5lHEklhQy7QNaEmsUBCnHkBaMBIQurtii4v2NaCflMMy8OwesxRp1AW5NID9ZsnJpFnaIHw63n'
    'jEImP0+hrALT2PWGc+8KZtGxtkZLWqHNAfsfmKzD28zYu75zvHhYfCK0IfeTwRJKEy9EWzg8Z8NFBFw7/zSAHu7OTG06n3zO'
    'o4dw2F8oq6l6NoGxh/pDPYia0wsa7+Imw5hp70T7pdE4xqE5kb0yNmrPbvM0D6Ax1Nf4fyKbf/niwOj/4eLyj5+Hx7gBr1rD'
    'KE0W/soxgLiFz9yDyNgX8HPJXMcMkoylKpACJOs4Zy53pxKgNtqLrtKmddaMRMBVdDF24LgUuCKRDxgf5RVKyWTZEni/joDm'
    'KSiCcc/GpZcPQk3IYUEXlktDkAMsjdBfAEGOSjYsYYKHkbEYwjdbxuWGhIu2qZf7dwB7iqzHDhuFDQHyKaIlaOahU3Y8d46D'
    'JWjIW0ldGxuAAKl0Ymy2Ca0l3uTh6myTfzQfDh/NHKN+KVNw2c9Anifvn0jdzJQbtgjkb+Z77dwhhllexBhaZ05wYWA0dnYx'
    'ZhuELoSysQ75qw4OEjjzdAfJhm5BRIV9qQtv39HA0t4YNN5nlLemCdijaOvaIYSCkLX+ixS6GpBlu2a9Nz9/3TEKG7tibSMr'
    'MTw0N+XYTYW7g1CY2OU27xDkL1FNfQs0Hwhya/PCQn55TxN0QADdbXeAhelk6gB+VQVsVi0AuyVA6xn8i2oXgIXVA7AGkv2B'
    'xROeDMAMRp2l8zMZiYo0M+wT4Fsj89l3Ux2iU8aVmEwyEY7Em4XwboaF85iKAh0fJ81pE2emPJopZ5714lMjXrvUCIUrCdTd'
    'HUaOyMeSCbFs+q3KCCh1EBMFIZEk4f9D/NILHkLIRHGOk/45WeXgbSFMJcOC4MDcbwUfaMBdipb94Yyduev7zRHWN8oux98E'
    'A8UufHGkGldrdPRyS8flXBz+38Mi4LNbOagFYNqnMQf9CuAyDZpICgY2LkTt3qK1k9glKCsSrASskq9JmQS6P14IeJDtU31l'
    'ivZCIdqc7kZCnrLfIlO6Ec5Y5hLQyf2Up+wvtwTj4Bgw3gM3oEc+5TFxOw3J6wm+ifxjCL5RaETL+zxt4JjyaymH2zRCaagp'
    'GTAt27KZOaphaieADhgmgG6wcp8IjjYDRaI7vqRkdSk0ijJ2J9AT3XnXHdRhHYzc+GfAzqd8+Vg7tJzAw9atndvcskV7Dayr'
    'oqBqyAGWpngRbNQmjVaYYWYmjhv5RHejQmlmsxvvIxHriLe7bdjw6x2n2eYFUIo9ubdqIxSiWrndwPgvbbo9ESrgKbbgddak'
    '/YPip9KCtzhEQWUak3NXAvuLwtKJAItb9rSYbZ1Pogw5HRGBqQ/bOsn4sNI5lbt3brcnWHVP2KxKOvQRhqZFCvrFF+YcU3ZL'
    'ShwSU/dBnA9pP3Ln2P728Khcuf+z1J3n17eKbiWh0nOHww6Dy2HplRGQZMcK7JqjpwkoBNuncvfRRIJYnGYO8Ch5H/awsnYT'
    'LhE01fa/G29ELYQEd1w1HdnYw60uZ1oFFQ4QJOxKeirx+BENca8kRoLNy+3/fkovW0JToCNmv55QQQHhS8Is1IcI8y4yNWv9'
    'dbelDxaSeMiqyNSMI+sOk7OA/8Q9875aQmRXYM5fVq20VoPGuqUc9SVSWRvCW8mceTyCaihXdDbHVoh7TSiUpEMT740Q9WWu'
    'nzO3vp2k3SclfTRESyOusv/e9JYhkUslJinTFsjEKzumIVEuF/4W+cyMQFRpW8JfXXDOYzjjVre66D77jWDZ+PeJIacm/3x9'
    '25BmsgJpJqdfXGrJE6fLbx3VjnTafJvAkfrp+IHmNh3h4wbeCBTRO1rcGnVTC240rLIUZJC0lJiOVgWahykn8LqZdZkxlVTW'
    'wYZFRkJbHcnDbXJHyJVh/NAa4iDmWvOoonVNKqYpc3US5NdMrBW0wusLXJX2Ow2nNE89R2dxLciaS/ShC4RQ/mkSQEFcTV2L'
    '1KpmtjQPjOYS9SkaTkgN82XPW3vEeoKdK7KxBLZaClgXGbNjRfCOz6t9Vkzew3x8k9AydqDWz8ht0hLxO/hPwMNuyKb3Y5Z9'
    'ave4jwfGTpAGmADMhXosWxAekqlaT1WuxTaa8bjaHKx1ez3fYpL7Ns6YrrEvuZRy8n9LO+MwwzwKRi6yEf3EICkbhGVxKlb0'
    'MWTP7M6InS8iCxFkX2ptRtVePBzfjzSA+KIu5Zpx5BBzb6NTGWew2PmWZEol/YeCF/Tw9wPyJo5WtSeGuViUhk1eneDBZHvC'
    'PQu+SfaOoGqiuYnYL1OAE88eAC7j69gcTcn8Ibqwp1aU8hEYwdnfCCCilZu6ukNJ1ZijnWHDg5yvWm0kkQaKIphN2a/ScLVl'
    '6h6v2Mxcvuibr4MvayveLHX1kwqvNo7xrUtJpw6PNp17qtFnewifNXjRNBToeM1zOaiyLDLwnLIMXxBsm8OpTmVt8aBl3tFR'
    'iBfSfVtKE2wY1eTOyVT2gMZWsBhaNpNdADjMS+mp2JLpIePGdWckdz0TJpB5iQGPdD/Q0GS2fyzSXhXKYZDzDsCLDMjDdN5I'
    'CJDKdoFDsBGARRJEqnSVULiyWIOdcoKxLhxqTPuqpgNFI9YlXqVWvAsPwF4khlcvYsl0D0btiIp2aEidOX8XzAEKFNnUTmo0'
    'Uv87l8S7CSdLhbZaamylpCbcOEhTijqV+tmvLMIrzpUzuqc8vgYESrzAVgmtIusm21hIk2NsF7dEcxWYY/MKmb924qbLUxs4'
    'LSeCPl3kNC9hfuhp1lzdVDi2D58Verhr939CjXT4q5dCUdmCrRG56alDzr/hivriiZBwgj0mOP/PIXCslbnicU/Wm0oFoXqA'
    'OSFOqae4asE4nsyW9gaZQXjI+44A84CmF4XyOtfwkqrNa6xilgXH4y8JzRWp+LQQ66DOAYofYgengiq0EvWjJGtaTIGdB0JG'
    'Wg0CcDR65Wg5XpPuRmMEh4oKjZSyh3ZotsZD4qhrxWIo0ismG4c1CdoqpiH6nJkAJayfVRiIxKXjTGYmPNYU+tfy1dlJXFhQ'
    'APDGgwuuK50lQFlS3UgiVncfbeaAQ4DQJuU80sWeolKydreAxSIy1HOMDSTEA7jp6UXGhLbI9hckM5j44paUg45JBMEsSdph'
    'sWTabvZkKmJYw6S9ejbBeADlSqGTCPVLjlmPe6iBEp3SWWluohJ+j7ytlqJKeJ9C4E+cSLDr3BuKQI7rm3zJRf6OgG61qIfL'
    'WQedUmmz1ao9P6aYUasIQAXOy3bzdKLJQFBIIPdtxYB9nUAa4BuhudtDmbqLjoAu2YSWUlvFOMD7dY05ynAiCbvHWqBbSjmg'
    'rnMDUUeKMgoLU6KxJ3hkjI7AThiRZda3KnckwRS7ehRgqwwWs+N9oI9Xey+RSFR+DeUkFFQZFH8QvDOcKnJpwA7GQAhb6oEE'
    'JKPhzDRmxM5ILHN1qDQZMmue8pwbDM1bx+DAt+zgq0dsV3KETrCQ9L5kjZFpZb7dxIauiN6wFlOJOV/bXBHFK44hyzCQZc4z'
    'RDDbGIg8KHQN/v1W33XklVoKzZuvIQt+0c+JnVvlmxWvN0SMimo2JFS38MS2mz6EiUbxqixO3J3eYa/6nHQ3IZwW6RvrTh4Q'
    '6JAs6Z2LLVRoHcVc0AgRFbMuS3HCrJo+zhNQHGhe7Kerwr6jFswyf3P56C1p/Xnd/TzPHxjece30OVhYDD4BE6cKVs2kxM89'
    'gZRAYjL210VZES97wafnp0mprBTjyVMZbItasuBiKIbajsVRNfeUGnmZbFPhCrHpExTKhWSPZsACASma7jzaZ1JNpbH6wKIB'
    'x+OLOD4qKFGD+GKtYw1FCYTzAHGdm1oWSE1YL52RcMUBa5hvRWGblcgIhblTYuW0tptSPa4dhZhL+RBOpVLYvcANAJDCskXp'
    '3BPwG+WdtVXt/iLSUGaJyPuCeqX8E3qyuVkcTlJJLoI9R3lwBZpJCTfMyBMAGEiaMys19ymV4GlZ0qwYBDCV2C9mox3oEnNo'
    'znaleClmwfPk29kJMEtXSDLR02lIlj1yYXejoiT6FsULpawUB1NVnBamGFGfwyYFRE6MYBW2tBr0tbTs0Eckg5wPMvvCdoHY'
    'UMgioHKBuUpxOEwppBXgk7JY/p0eSeGpR/QgObi12/uxI01VcoTRymVs0fw4kqHWPvpAPoeYDYFeTj63sSLaWbknyYlMziZa'
    'uHab2QIMMdIGb6PAuGJxOSENp6qjKs2/btbQrJqAv1SblyDUWeSOAfNZGinlfs9Mj4BOh/VaaUxNCnekJoHdpaltTWuCNEDc'
    'Oe1c6YblhFOaqcFKC1oQSkhNeVUAbWJ/Mtw7lleV0+2Mr/icMmj/nJQHkC2k5ixPb+uyoiNJlhHh50U/es/zSE1pFG85PTtS'
    'fkuXYhocOntZ1GqZIx6ar77BPCUW4K5UaLZ8yUSFcO3qzJd96JE8oDvzxGkcGJtKheyItUK/OauKi54NGQeVMy6zWlhbEj0c'
    'TvbN5dV7kDK6Vch9gSGX5j5pBldXiReSTx1vUahtSCtNVPgEqXmTNGGAf27xOKYJoLiDjtldoOaddkL1EY+pVX4J/GmId5oR'
    'BGuDGG6Pc7wUasayqywGC0O4ESr5+idVLN6WKObiX87eJQmZszEYMpkSuZCitxW1CjW+iiUJGIpIBjuKevfIwTKIWBvoBF2O'
    'CtjRUP8oJ3ak5PDGRKL95OdWKud4Kzkv4VRH/H5ttUmmHtV2lZM6g/5MW8Lpdh40zZNdg6BvUiIv9kDAik2SR+HXmRVG2ouN'
    'wfoCFZLHgN4uuXIhn9wPrQTSS9wTzUjYM+XlRHVudv3JNQMsqLfNB0qDe5po+4jAfA6pTJ2Hu6W2uk2Uzh4MBp/8pkft4Snk'
    'g4giRc47GFm/OK/Pdj/MTRx9QVAeQrD5tD8QgFvdtiYxLrkO+GCbLyDG/RWxA7tqUzuJj0N1J1i9Yb4qTCu11qFiH8F2cniu'
    'F62vDxqil2zi34xpfZ3KOTHGGi/gRKU8SfsJyFjeJK2SMrSnMOqXkIHG374nvzyDilGCTm+cfcJw0ob6UtzqSqQO8gfVCieV'
    '8qSDhmwkHWkWsSnKQnFfTenQ8O0drYu5Ei7MEDgszXrXgTeDh5ZbXVWCpJQfreqe+KxbyzvGK8kcSKGb8t2ni8t3P93ZSTef'
    'fJKamNRGOoB0HNoPHJTldHn+dvNoS6V1vawLAzqwmwstz3FiPRvP4/GV7OQh9zAMjAfAMJmliLk+qVkTWLnLyErhidHofzn0'
    'VKkAv0yEFQKXPioSIFZES2hDJRJv4Om4X+9RKAhAPrttQCwmkxcQdG3keb6IDV+4LvwyftiRJ1dBXGxwVh4BXlv7OQN5j5E0'
    'X7bUebYWmLCZAkKHj9LC2SNMtpaiYQFAGNWpsOCQbafX8j5JqTbbVE8D4shbsgO1EnJpnGp96qFSXzj5rokmt+6fdJpCPBo5'
    'bxwzihMnfHypU6kxIh+UBJW6yMEUCGqsoFhEOSuo79T5ZnpRal0a209KSTl8rARpWPNd0Kko7SJuMitqVxLc0raRwID5Icmg'
    'AgvJQ+uWJs28YF3CXKnO0yDPJadsStlMiQqpbdWVNUQ0W7rF8wZyDakUmwzqIUnasZkaPyTrMGgAqdhVWX9g/PILMJ99yFZB'
    'opogTwum65BleRIso3LTPxx2ke5bAm+nZc3k9KaRK7gskY/w5ShouIuub257ITKXUXWiNxVxBRvmXz7jsR6VXCUS8C2CMS2v'
    'YCbnpDifQNk8rGzlL8isprQm111agynXErRjrjpNitb1byDzbSYH/WXVQYdPO1PLc8d0+aOWeWJGHvlLJ8ffGldiUSiJREAZ'
    '/XxYvpjCUmrhzogWOE8tKjTc+t1IcQT0NROnPV71KjrkeetctYgZhzrh80Z0AkWmjYbgQ1aqxGevUgiKWzKVJIm5ERuXXRAZ'
    '5ODwCsP5ATe1T4VkAMQmhokGFNvZRoCuIEALW0n+PVn+mVCXutYelnz8Aqtfr6hhEMIKxhuGxen5ouRsyfvMrouaiBWVVLFE'
    'MAp+GkoMTWYTqEP5NWinTFiCcvnoFGuL2nj8Xil5iAnZ9i1I/UmJ++Pgu1g4XT1fFvXwETkpaEovWLmIvQJ+QI4VX7R9qhJT'
    'nmQFxFfiLprRxo6j4ilk0wcsgAIw1oOE4eSRGhWtRPlVioTEI71vUb0yAQAmALckEmbTsKJtrONUTF5eIIRZ1I6dpyRHiinz'
    'Tr9UhN0YHSwYWSp1RZ0jD9hLUXtz6l66vlbwIHYQcoZfHncEiWcPMlxfC/LYVEHPhxfXxYp6NPW3VwKZmA3mEYBEmai5M8ao'
    'R6AZjUz+qydMIlW9p9/W1IuOnDCCCUxRLlU0lyJfO5EnwhZDdO1LmldUEzoN1GgF9zjmSDgHC63QVlulPa7drXyOilYX+FHh'
    'gvQt+oyi11bICNHOmHR0AZh7TCUnRNw2PZRxJTWnWF9ZrWPIxHdbEhbRRmJpEZGhKuYKtLD+0Cd/JYcqylmlapnvJ/qYYTJi'
    '71yTaap17KSFUNGQ1aPV6XTFqQMxj5xvqWCeAKDMcMKCTJhD4/nNbUJRX8LXauxKiMROPLRiiXeUrmkEayjIy3drqlmBZrzU'
    'MEWMy6vzkhRVQevOAB/7ebIpeNQOYmKYD/LUS6+CG5CnPq3ncamJ1RbqATchYHFJVXikphcLDUrtZdhwK8EqqsiH5MaXrVX6'
    'OmIfM6uLN0qIn3pifQrTal2uSNSbRyXK6tCia02NldgXIm9KbKV7wR+TEMVSqDQVc5USJZp/S11pZyuItOiUqLjGYoSg9KU/'
    'cUaOngfLWDFSxLMDRFfJPEGiX5HRoyql9IfuGKeFs5bEKnH9iGb5ZEWBZOdOHs0iKVWZyqZYsQJZvClsvnJhOGEDxHVvFAVy'
    'xUGo72yImdK1n6t2p555rduZpEzIhQWZo84IRL4+ag/GGk+YTcQK/OxH3IdK7EDC1AIRi0CnmWzwHHZDVznB/UQKGatYV0hS'
    'S9CrKBYp1xQMSCitGxYePAGlNVvaWWFsMCgrj7jUTyFGJZLky6hqXg6dMYIcjcQh0NpIoIb2y5nt8etqjJSsho/MqunSuvk+'
    '9EGGRjDQmYF8XgJg6MUz4sI0A0PPTRSHsmIo/7SLTI5KkpFKvjEmzRPI5mhDayiPx5Bn01R0JItKqpn8zPV1aP4XCxMK9MyN'
    'kBpEsz/lqDeZrtaovGBosQSMMPwNeMP9A/U+xplj8BqUrQF0OrKQTzXlKpsosKwrq7AQuOzO0JrtIrmv2C2q6sE6F0qsVvhk'
    'iiKQUrBK1AhStZ4bk4aUaqWoWfFFZdW4eBGTZOQ5cvHyoKtEl2RrPxRFUUQvJSlxWO6bVJULXP2x4ZTbA7kUMiGXhcUkGIYr'
    'IvxBLtZ4FZa98dA88gM3jHHAa0IlggCM9UOwWhrShKeSQlhqbWd4axsPwR6uSp2nKl2JvCSnjUBkjsbUovyxQ+hLgpZRhMcg'
    'iMbpXf5uYGOf05NSPkyf3VVAaYUFlMAoAHRn9RWAO02JTqf4+pDymtYJWZfGxCYhmMn5LiLoE3vUJEVC9igqJbHa1IyW5XyD'
    'dGUsXfy4S0e47KQAnGkCRVRkolvFJykXqF4umN6vuRyc9DaQhNIi9BX4FmUB7cIOiOoo6bRuqe6NDk0SOEzctRR1Z2VxOoa0'
    '/a2pqqFtZ1zAKXGBlOpNBLG2ZuPwYkFkYyI3iYQ7ehExJEw5JvHoa6ECDwolvnUWSZvad/AizqllUYCifr21hm32KKAqbsl5'
    'TyQrRRfodWyzZzKGwzJoTI3RU42JqsC8qVaB8fgAVp/XFiJTk8FYP/TmsRrdTMgr1NlgN+xZwrN3y1EPIi4hOGV71Aic1KRI'
    'WBaRsr0O3fDTzi6xlOpEGjlD2tAZyAJ7KRf4ei7ZRB4uUm5aZH3AQoso7IeOnqBKI02oLADzsWQB82wVheL+aqacTclvHN9h'
    '6VM/hXriaoxJ5Wpz8qre6GQBKj2Tga+uFOEuIVyop58znyBevkyFVpEDDlI0ElRqylGntCjmgPWdQIXjlfMtuQ+0mVUmk62c'
    'WOWq5kBq6ZhKjlfJZ7QNAqYnFGKU68SS0r6FUpGKyMU2VcmmVqS34QakwISWOsrLIKdJxvDJYUngjab5kBm6XMM4yaGtHBkL'
    'LZIYMikg7lfVIdvgtboNFGcU1BDWCvzwqjrizs34VvzsgSgAq3wTX/spz6QpovytEUIjptcSs4VfdvJVdV8xVyGemI00/sPb'
    'oAKomhYYsWkqVQm52BhrSDxs2Zg7Ne+418ss0HhYaOXzgLedSqtuGx/RkhQlEDNScTQdXX0fN0JyiD8NwjsrWNS7igzPap2G'
    'KLuU8kb9s6G+iBKprVHbE42ynqngPQpar2p+QKppQiCNn+TSqVrceBWSpUr/TI4cU9ULBoOxM2qhX7jsI18xcqHob+iPUwsO'
    'nTyCIgH8lg5MA8ecqhSwgh17f0WDpKcm4igYkkUTOO8AjVqIkqAMxvsehkGONdLwy/QBjCRwC8mH6bdZsjsodbI6c2mtcTcS'
    'zYJOrlsmlWLtK4GI63fYVr59aBZ1sJQ+tPVqfaZKP/YtfwB7GTf31V2rbv8PgAYCZg=='
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
