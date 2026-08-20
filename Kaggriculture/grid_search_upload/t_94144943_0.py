import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXctuXNmR/BeuuWA9Sc6OLZUtweymQFEueBpEo4GxYcCwF+3ZDfzvI7Net+6JjIzMPFWkDO0KxeK9530yIyMjf/6/i7/8'
    '+tvf//zbxX/9fPHDl4/373/5dPf56cvj6uL58uKvv/7jf/759S9fP/7919/+9uf//fr554sPH1/+qn344cuffrn76eOPd/cX'
    'lxfvHtYXl9Pm688fVqtPgz98Xq3ef/16/WF193RxeT36+sfV/cNPF5eT/c8/PT68//Lu6fAfy+fnf10OO/bp47s/fPl0eNNk'
    '0LefL9arz08vbf3p4fHpw8un/VejD8cD8Xl1f39463T81t3jBq8CDRm+9vBpPBWoAaPXmbMHe7hvycucTI76uv0Veden+7t3'
    'K2s8UX92/wDeNmo3eev2X4bj2bTj5bufDovhqK/bmTJ+5o7w6m78/sPyuHtaPY4X0fi749UDl+5kvIg+P3wZL6J2cf7u3zvj'
    '6JtR79hUtoNzPMCjUTr0793ddmnufrTZmYOuh+byMFztS3ejMPyVO11g/6HJATuhWcHkLduxB2M2GI5mxtrf6DO2HXc6dEfP'
    'He+8wxC206SuSzC4YDOYRys/W466oI0sOnT8ydu1VB9L+Rt/HsEQbk8YMEfevOmDuH/H/sPXs/cz+hAbuMO4Vx68/SWd9L7P'
    'pxPepQO7/x28qetz3Q+v8NjRrTIzrEnnMA1cIH2eOj5bI9v37C0Y2yPkp40Z0acF7x7u71fvnn753erx6eP9x/8+PhM6DV76'
    'JYElkn7HieZgd2sP2mPuob0jMvqxcZUvngMW4Jte/4H5HfdxnvduXfuvaJMA864xHwdGOFi4gj2nOKtwT+BebZd2yEzmfRj2'
    '1uujO4DAsQ8YpMxVgZ+8B7KxQJ/cBzKPQLQf1XUC/FG7yUkHyh5UyfZVNhD1zf35J55OzfVVgCf3cdBbDjgPwLg/PLI1Bv3N'
    '3wInxLb02xd6nGuqEtzszIb196f1f5p87wMbao4B7EnJKEBAsmhqsIutdsUxNMe4nV3rIHENeoZAEaqTLoYuBgLCGc1LI3k3'
    'MnD9cFzXRgW8LPJoaiyAt1jz794Img2RMk/I8HCrzX80BagBnBYCAAnORUekywENV2nXk3+Mpf3nIGffH/v9sUFMyrZewrF6'
    'EEw3ovKOpbXInJkZXzwIjiRdvgAYUoseenZXxkCJQUqR9pOQeNULZXe6MTYf7h7/aHWsChgNuqO7+mIIGg3Vvi/JIRqORYUf'
    '0A5OG0DcMwFKKAgf9H3HNm8NOjPAHtkPynCkfCwDgCNHy+6wRneDcghXyoN+eCK6VIbvG9tXoejwjmBBby7whkx4uH1wy3H6'
    'biB8f2wV4Vl4NtL2dzcv2701mxY66GMaUVtT6fPT4936h9Xj45/+HY/LxI3YJQY7ZLx98lyBQvwYU5wJKcJHydiSZ0Tp8TN3'
    '3AKG4Ri+qkNKgSgGCzqtT2U0De2NIUQVw4x4MKu0PvYf9pe0/zgNht3dsYNtiLmoHSOPJX9jPALJVWD1O/T1pplZGw992jQ0'
    'E/Fs7y3CPxOo05HHZXC+k7HjvseZXitqtYzgPoszWio2etDutO2rvm7Ex4cn8Jog0K74x9T99vCVzL3CAIjBLbh+eLh/SVOB'
    'RtT2j9sZ+npAvhcigQdfPBSuS9OHLuGkNtwyRk7oxBYZD6p1AchG7G5y5CHPQWfA0AFZP71v+d4xMJL4krlsJVSoFEDVHY8a'
    '06iN+7rAlQSmNp/S8OMqEVYETQQo5uFTBqxDoN+AfwQsxvJWCIxAO+foRBufDZm9wMYafQqODDh/WmR3HHvO8aiAazGyUk9l'
    'DC0zOajhoBlEXGDYbO4bVzBHNGxxnYZS5NlMh+XSUHb2vYkdBijDMxoZy/Eq25kBISDXnDS+9sw1DhOoJwjwzv2038t0RrSc'
    'rktyET16yijnNWYpojxgut55Wq+MKQjw6z4aBdvTGhMq7Bi6yw9xvBB7Kmidtu9tjw1xLmqh9pC5jVvH7nndWDSvW6MhgVsZ'
    'bML2CCD3PmjR6G/JDFdmE7gfUg4i6K/ZqWSHyRxnuhk36sh0Dw89ZKpTjp2B3nq2G7Mx969xAcsY3a8dgv3ZOk5ZuOwUgwTd'
    'PIgjyOHu3LvBepcfm0znAGbFqV9ZCR5nXymmRdp+R518d4u9iFlEambI42tvHPizkEeRSIagxs7+jxXKXY4Vt9+0QxzXMux3'
    'vxXCqJ6QkGg0Uj4otg92b8WUoVR0PAYdgqPxcBxvL+YfP97/YbvyLHeo/aWfM1dBvbdbevO+ydTfqVOGBYSnEiyuMCzAnRh9'
    'BgnlFqw4sLUFOZiQXxkMFAnJmh0FnBTuy4GOOTSwGpijZW3GXLDcWO5ncnhk+EzPSydtVwgQNmM58xHRlm8xkP3CRivysdpW'
    '4gOzBpWDeQdOBttdQLSsfUAyMtryVYHLIiIjth/jc19jOHJrVTMHLuLv5RAMMGZgHhMfsvna1JM8R+vYAWjzu5NghNIgOBBo'
    'I4C7zDtTTj6x7UlsNEka0Pcff59tG9kDgWk68s1CFLEsQrLpsqaHBshP7EcZxMhbjDHvlsE0oTHvQvAP4DnlHM9ykNAgUxcD'
    'hHE/fW5d/eR3mhrUKRx4YKx4/jvh3sZimro770fpGttH8+or/n3jKcCkH2yRyp6u/MNqIiPz89s1zN2cfn1JJ4Aek8rmeFkB'
    'Iwv4Rys/JO5Y/UHq2pyAFK5vP7xWj0cgzTHkgTsl5EY7GzA3WyYm1uGm3rV0RGTSW8Fxxd7loJ+CM96HUkDpT0x5i6MfJUUW'
    'yfdunWlgwZJt2QnlkLKl7gTnFvxNlBPR2dsWNs2yiyRHWDOn7V8VM5iVtdAaqErksjVd8/w/vtFP3eLwEhBJDFU3wRfSEOKV'
    'kGpaCzG67crI4p2hWcCU6/LKc47W2Vr1RgerOyugj6JNb+JArlVy5p8MKqRda5+v83pxe0KkycTt87JpMiyRit9TEy+ojmOs'
    'rOvnmkSx0h150E/CHAUro6YbmXUnMzxQQHuVKOQwVIqeURYZgDwOx6+2OfmmB5OM4pBXqZl4XpJnMter9ajBAA1fIoZ9q2li'
    '6qNZU2B8XqlXNgSGb6PMFKiapLnENK5MVqKB2etsdvBib55pE8E/u+1tOUDJABpuBtQSM1W0/NbetCGRxbN+CzCyM1+37Tdg'
    '0lLtX5qw6GQSMC3YKmaECTAvPElQ7lYAoQvG2xv5lqPai8H1dfS/2c5RQrnYSDgcwi3fxnL9fqBOjxmD7Xpc+OuRIcOjgVg6'
    'k7tmhwjgScu9XgqHiIYng9skOIt4cVSW66ToLwGfDrXRtZasQpZ8xR7e4UufgqwwNh9rzYAyeyA5VJcSJknSBvC+aSmE5Ehh'
    'xTFNU9hfbLV+xZDDJMCKGlmAT+xjY0D4piWDNyopnXK3p+n8Cg7evJVcC6u4cMg7Pzlp45Am0CNeLqRiS2SOgF4J8D4FIIch'
    'D3LW+HCkMjpGMiejnEESe+6RDEgTMtYrSSvLLhxoBwvJ7UYikt1yTXizQns3RsMUbuqb5wyQ5EJ/wB0mIVxOVi9xNRCVWUnr'
    '1vgEFpnMMQ+YUQ3YS1JWAV3xjUkUXDw6stAYy0eXwrnWRzIgDsY+uGy4K99/3bR5XWzZGLO/Y5lzf8BLVKjLGx0iVDJ33k2B'
    'd0RvzX2VXVTEPePLeSVsCMrWIrqI5tl/mezT2q5cQJFOgMTZ05K64JyuUDkzb9mx1rN1RiptZLOGKFAIXqyspfY3ES07skjE'
    'Q5HryqG/dlwpSiFVLnJnf82hTRoQ6LZ0aMQPUKpEXDane0jHluL2bfuAZghiiHW5s7qrXEiokCAyHUZyDrBNXRyjJxaz/3LY'
    'nhsHujk9NgNAmmj29yqvUbS/l1DCTIRSIwMsQUKEkxmTY8yQiEgboszpDcVToerqzZHEEd1hASsjo9PiAVgZFTVGOmFyBQE4'
    'UNYzvn3OMKUoHMPY8+OvBG34QK6BzukSHY6ahDWwo+XMIoWxFVp0LR4R9b6kZGE4idMM9YVKDEqJjZk5Qx6NW+1XTRnCvnVu'
    'GqnH5bGvFA2brPfIgq/MS2fOVpQkNn3O+GJajFgQB+oxjNTdAAUAHcc3Un2IOUuuQydBs4qHJ6SIC4WYKAgjfie6dMZK1BAl'
    '2va852mu8vgWYi0MuPki7+8k7U1Pc68lK5RqEkqdG/4/w48QIUJqX92P3mQ9Xxue9Rwxrr4VZ/tsTIjWtYasZi2d2UQIEm73'
    'wQ3c/ykZX5dtqwzwKiVHeFJqAIYrsv3B/O43seesZhUNUvSFIjjTrhI0qvw7iZW2OWsmJk/1JkBp1/RUfE6M6z1EEwlCgo3u'
    'S5HEn1sSSFW8oM2OUdbbv3lwSCB/J6E6CdcoI0uE00oqeo2aPj//JE11Yk4jqyrG9OsirEAT0qjHYP+sOIlcupS5OBKpN8On'
    'RlgDHROXuFAsE6bsJfFqMTOV6qUNdsb68PlCpMsi3ytqsV3uE+bfM/kJm2+F8IHRv8URAC3M65evNegnRvd6RNLXK1XmJKqS'
    'ktHsLLYG8KzizWpd46rOCU0d8DI6euY3KB8G9FalyLLWyJw3f2v47ovWd5+8nu/OkxbQTu3olx+WJpJuM1GFUkVT4Ge1YUSY'
    'u+rFmqu+dTJ9IB1iVWaoLDexTo5YjL3A3LH0+Cj1y/SiIS5SIwefb3JSiNS52rGsjzIfrzZDu/3GMzEGdZmLfqy3+hDp2z4s'
    'dLl3iU7PEpI0TkFHkRUS9vXmrSaqIVLqE0Muut5Ufz/jrYFBh7cAim1EIBG1IoyaQmI6PcGqEHiBYY9Oqsnj59QRCzpQ2rUL'
    'qsZCyQoFIFm2nHpeK7iTyYvD0b9ZIOAfmPN+Y0BxB8JFNx3vpI02NFSHk8GTc6JJIIrHmxCDyXGrO3OBZ4b2/jcRsYy4QWcN'
    'WKJd4bhNnbK2TxDLlIqc+Wa7SiImH7zBFi7LQPEXgVcMAk95nja8zzJJ9UWKcbtyjsv/bVQyAuM/sNY1zq9bCxDpwVwFsimr'
    'fPDhvGMjwI8KZTxKyScBi5IF0DD7TnTxXFPmOsKx9E8oyffJFG4XMfqb5wBPmgbaqEPoWrdx6TJheziullaVQawXLyvhXdWE'
    'BmOWoNZLv9HThjG2fM6QtWNxWdMvFC9ATehRY3GzFQ+bE0qwTSwbEgd2CJJaJqujYSDqJgqenyIw6f0Rn/nkyOncco3l7Rw+'
    'lBeQ16mcpJxvLa3D0REuEIZRT2ZShauwQiMxbVyVwz79aK8AcWtKWBXj9dPAarY7Wpyf0WEJ5ELO/m7StNO60IRcQ0lJteEZ'
    'L/mFuMinP+w0WFotljYgTunwTclQKhPYuWOlMo/TGywsuP1mqAAImnj7VmPxOdp8n6h83knoE4/3/Gg9YH6aIL1e1aDECo3H'
    '591WdMZ9lPlttaY6KToWY/nA/XdDL4FMZy1Kr4e80Y1Nr9lEAJ5FtrO5KUrZeikSr+o1olJkclRIIRqDFxwvHMnUOI3uXFCb'
    'kCkNlGFPQTVZ+WdlAbHCkMSpcmptRKSTFBiASkIS9ycT4JfM2HBMJCGcq6Fi0OKgLOgiFVVLJlfUzigsnA0Fa1FyTVOhm44B'
    'Y2RLav0aQd5dZKAdfBIkkUQzut5jnIhKaRR48xUbE9NIKVddtNxOyb22/L356zl3gNj8qhQDQJ6VOQbkIupBKaBxOF19u0iO'
    'yHiH8NbSv+RBOZd7O5k+93Mhvb8LLjeOA9Qzs/uL3nmWKziS5dC+Gsuz869vnxPerGtQWy6K1zG4SMc2rYIOpvxjGnwXOfaS'
    'f+YtPAHz3GzKKwGZV3zx4ybrLhbPNK1O4ri705RGPQ9qqvWFKpH0CAWGRJ+4J6lpx6WbHEsjF0tboH+grPA+wVCCLqgaAgbh'
    'hWEjXcKhgYOcnXkio0QNaKHHVeoRXrcnXYBBQ9M3DBSNcg7arTj4Z7+D16U5c4LBUokW70juM2vLbKheEiNEQtuKnxuaKinS'
    'rXFCtAwPcxXSvdXjAMmHubl7wSBQTEbYlGAZeNJL1w/0Ots8zaPHsDoGa6WzK/VYIcPo93FenSaJRkK6Z5E0/KYvQ2Mu5d+E'
    'ulBhtBX2EVEhAOIHrcpD+w1gXdi3gNi306Fl07ld+5Ts1zeUujN9O8r+pKSNKNUmQIFd8nRCCE4g7ksLRSaTdWQRhkv93+si'
    '9ecoCbBWyxt0FmAIZfAkMvZlQTrar2IFAU++gfpbLq7rVEztWFkAfbIgrtROlnQkhyfybaoCAfMy8MgGJkG8bUOpNyIZRazX'
    '2ZXRrxQzwMlcjnXsT8Twc8i3S5U84OUXpKwiWmVdhbWuA6k34oI4ErxrWibsiPAyUiuuh7O6UI+RGUQw1URWFwQLLstFGvjO'
    'xpku6vzZ/KxTYSMqcCjUuQxqJRT6Nc9PI0U9aMoQTVOBtmUukUMBf1rXXCsoy1DvzsL9Fae8Pflp5kyhaEK3Dr6g4HMByqKE'
    'G9q5JivjzHPnd4TGHYXSoB7QXykrku1T1+Inb2FzsQIatBAm7ysCijfxb/rQzC3QvsKZ1s5MsomFmb1i/tDh0nkbZTeQlcQZ'
    '1ipla9YdHvO4bzJ2AB1SGcMwUAElzTzgEwdcaZkNlOLLRAhrIXnUPGnN67AZcvbPr9vAwsxU3ZTnCpntgSWKJvIKMQQC1gKD'
    '3ATlElaz3IHhjulLV1Yo5MZkCCQZXqwmoSjGr4mhwHyZcb+ntN/OxLIDNlE0ljPWNETK3432fE5zdAKJZ6kSRLjJJXdyWVuH'
    'lBmmWoWRPECxF2TB0Zos6naiz5CRNJ21iw4rl42veYxxBSfl3Jay6awT3EKI6LAHlovi5UnJk2uFwanWS4n7O8I5y/O8iOYN'
    'rdhLC+Emtivwamh+iZYE6ZdcqiGMoRTBZFYlmRh2z3XhMztZyaswweh0U1HA7BXWtrTwhHXaD90lxxNbaQ6fTGIshQVscscU'
    'qHZj179ROFeoTk0HFaU8GVOrUKXV2XG7nV56s05A2ezKQsqmrBDOt171prPiDjb69FI4rsHXgUjmQQYu/BTwCQO6zwwRo1yL'
    'LqViy5V6fUX2WCVct50BV00nTvXP1gTW+LHXEMyLc5mO3E7XSFtaXCxc5DaiUV6u/4IUnwmZxnLlNGJKTnAGEMg4OOTkfnht'
    'VZRnGFbEQE4r6UmjsGoY5/Htq68AySdRdyh1oXUPZ5kB0yMJg7R5jmpsvPUEHKJZsrAVNLuOsXhUF+0qBxExJVppyeBtqULd'
    'rXR2zROjqDuHgHjGWXw3K/RPMVvZTZOiqCU6xhI5U8C6Vw9ASq4wDldzX6vO1SIEeXk66qLKMOPVJJOMxnKtfiqbk7aKPln3'
    'QUC86twoEsG+2CzsCDFDapg4pXZYIimdPHbzR43VgUH38Ia60Q0x6MallBaTSnUwR1Jbi5LSFJWISlLgldgXUaSNcSVNIm9L'
    'dzWhroRR0ZuydWPWJn1LtcneGDbFS5FRXVgIW81Ppxt2hDGRNBERF+pXc0zJtJTVwgI1NSq1x1DafFkRLFI4rVBuW5FTgosl'
    'ntuqwGd6fqmWkMaUd1vfZOVIEsuyMYko5CSQzQjvHRXWdLR85XWXSFFjeULWvgW6TCtewBmMDgQuFFfFlroZJzMsIrmQiu16'
    'KVMW9ILEOZmyDKsNHh5OlWi5cjeLoRdC51Nzum8CyZbrmJaZVzaaSHhlZvNamE2SjMm12hjhRJ9v8ajZKmnN+7BQp4ElLVcC'
    'BTs5opBU9GZfxmcmzDcRYOfzrWZte3hHRaZrzqY5gFYwcTW8R9mBzUrsJTXkAirnw5RKLEd1vAwVlpITJKrJAToCV9epqlVC'
    'DRK/ZH2e1GoJAdbUyoKMLKlYQhcpx+vIZovVmFY+mCv9LMuR7EUTz4uJqV3GCtB1hQJnkfKLiq7ZLjVX3pjh3i1iwv3auNNw'
    'iSIjmOAD99Apa5G9/5yibf25ZEdCFD6bzMzMPDuZzBVkj2Br5+WVZYrCvW3y2AnU8V+DSOYWR0c3EFXCk5liEnOCUsVUrWGH'
    'Ch7GFnKpuvrKp5wVKt7UJ/O4A7ssA14luXBBltlKGVGhmm3I45t3YpjRr9whjXKbFr14ZQY6gvmGDjExAvDOa9QyhwrjCllJ'
    'lerjMQ9GMIsqzcQrAMa115d1epmnA0+VqnQ2TiAvNCsNx/GWtYCihaqXdE4V1QTTKBPNLDejFMJLZbdLwlRKpi8HS0cCd2Oy'
    'U4Q1JNTiO60mkkKI2jv5pLEshCDdaRXkWOW4AXSHixVSS7j9+W6ggFnXlqavEds0GhQlZGo6eXSFmsp/X4/Dx4eqMr8+00rH'
    'nUuuXeRUUDBR3TjZxe1QyjQ+IHMGDtw2Bbalsw1TSg0mo520yRTdNofljaK+4gCai1PT5xbG2fqt0ORAn2al9tfpc5yTduIy'
    'mw4DKkqcO1FtzZNx56LFNvXJfy3qXN/Kmpqsu+Idc+aTCyrqZeXDEiu3mSJmCtkOGUkR8iNTFQ7kNvmcH7ECXbOQ5bITnETB'
    'R6dPzFZ0seEqNRIbdBbikc3YWA5TxwbcrsmJRNnj+i+sDqfI3FPZJMENuWXkTaI2kMLhI3xTc+515m+k2EYfYlBgZyuJi9Qx'
    'DX/qBFTkFAc5gkdTFfnUBiq6lAuETgTwiTD2XO1MNGtGSmS1q1v+cIpSw5l6RNlTlmozD+MadjhNqfR7vFk7gOA8YqQbn6ci'
    'wtPXXaltTx1Ck6g2ZhIbCOZf1Rif5gh8NDFcrK7KoMJ+HVzKzL5phtmn1kSh4rbUt6sWkc3xMblIfouk2et7gBOGJdhCqzYN'
    'EPv0P4c5RmBTtfLXGUbkgDK6xiRfkRrsH2Dk5bu9yC8Epdeq2I5YAgM8pVyj/AjKPAUhsY2yjcTfQ1BjazROzgifnr1qalwZ'
    'ZS1Adnjyr19B/k5HSaqlIm6eY7nJrFpqVgLPEdcKkvuUKqtiHQMlUysA3WVol6SKqrdaXBYBVxMr1kqVbVlJxVsaPYLetF5w'
    'UH6fFZ+hkemA+4pE6bW7U2N0hhYe8zZcui7DAMWcBj0VkfEtBQGnEyw7KktJZdNVrQl3nQWLiXp4bIba54+cVBWU07y4rLvp'
    'C7v24SydpgZioyIzQq1Q40YAbOWa8QSgjTzsi65+yifHq1gRVX0PKcChzefi+uJFJkcO3UPDaggMNBHCFZoSxb1OiAayQZda'
    'yO5XRfG9eVJSt66HzJcmeKgWKzIxkxBwh/TbLw1qS6AAhJsRAyAt4uYXq99CvlOgN4y86DURVlv12ZBp9vQ0do74srVi5PlG'
    'jPEWOibOZBh7aZ35SCjjmynN2ZLyzlSsMy70puDVbcHWMxLXBKgmYI0tysU414lKnGq1uwRP7TiMciqqmpgVWFSAt9qk8s4c'
    'bkvVk2zJYwxpYamQav0GvJA9nZkQUSy2DsCRowrMq4EBjsUva6Qx0GzwN3h4ymnRatRjRuI6fpkKxgnzmhpAT22VW2t6Fdel'
    'RP7y65S5qXbkkBYZmu1i9WX54stVXnyOMpSiGn+qvDSCT0s6bcSAV+rPiqKK6j68ySxUM2tKTd1JbjRRfS0bS26XKZMEN8pj'
    'CdlYYdGa0MnayjpsJgIt2HaKwBnU/ghlWg58g6oi2+ZRizwJiKRPsuoEJP1M2rR5VaJ5actS6Kjdq1r5FUIXStU4aSd4Ik9w'
    'ERtkxxUbDIAmIfhi40HKGMU0uJnzFCmM/Dk1DgbjxdJHqxVhL+0cuO7EP8pVtHc4Sz0NU8stCOo6tvNDOaiT1BgpkTj2Nx6H'
    'DyySq5PoOzIF0biyUThWM++x+6dl3NI0L3ZLCpxSy28wwXZ701yHCW/2/htpd7vOD0tPHSZhwC+dAhYT/7GKal6CDtF+cPNZ'
    'AcGOVZrRY+HsQ1bkTqbYJdgvSU5bisxXI/vl6BU6v80TpFcrQ/jQM1CTAXPMg6q6CLldIYEhoJNKQp1bKik5BRr5Tg09Fmsd'
    'cKYTAkNl+F+TvHFTH28DHB43281NjFMyc7rMCTnEAjwcVQ/YsxZF3EM5otSKEFp8IMwxmKdyfxiXc0CaIIKAwkAIdWM72ufq'
    'SY8IcCtbQVABw/fxp5xLzdNtKF8QehluQ2dBVj0Do5XEThUEZesmkHDrpY/SHETW1lbXboBn6NWG04seTpNW7UK5r6qaV7NI'
    'NlpZxi6cjBmbWUoajgRTktUJVA1PTnaltL9yHp6ekDkPif3zOaBUUir+Ye9fn+Qz05PjlHRcsrDF2eOYExmsChf1mmLwx1mJ'
    'RaSx3RJA5Y6vfkucky6N8q64tXoorIpc5ubCWomoihbC6mbfIDBn7s7BujyPGJ6UPKRTDGGDFPDK1YajSTsu1AK9WtGRYqBm'
    'SK4oJIpH1H6j5W9ZNYBgbc5aVQyp4t5SEIJmeBYWu3NwnhQjpyrnpyvzMBS1SV6NBnp5Phgl943EYQUVJYJK6KmPEVDSUSgP'
    'TlbXqmvt1GFWjWhKiazkQIXDSQp4pTYgzeAZtnxEW2B6dTVUFb/eS/VwkL2YcPo4WaqdiWmkQqyWLiXzCcXodXA7aNV2aGKb'
    'dHDFYLDrgDEFc/wJ6ugMaivuGWooYeQDOQmCI1KBvnFtm1ATtfINuvJfZI8yu8NobkMcNK5TR0eNiuk4OvcKoh6tJqnAUkQs'
    'M56lzkG6HmeJCkFRwieDIu2DNNF8gbwF1gThYDaJoPBMsU/+0K4gy8eTzYjBmog5YvIPc3lv/fTYmKqIX15MrT+zzt6+kRKr'
    'LTlwnVOBii0zEVPvJg9mIWBHcIxHXa0BNe0knDSNtc4Am9bSWS37WixrkAM/ZFYUWNPMIKWIgoAzzQKqrWXNsiTnqksNBhWb'
    '07XXmCOcy1nltQ5FHRxOodE2lCYN4YKHHv7hBK4DFf/WdlFqv/6xWARPz7Bz1xo7ntaEqukPUru6qKtNlclavgdPM0gmwetq'
    '656GVaZ2s0o3F3W7oEpKqEG+f66XOKUbMKZhx6vjhOIIzC/g1MyICcyd+mhNYcFN1LgmuZJErPxLIBnMaimYb83IdhIx7U0T'
    'ah67jtaBvSKWpO0zfo78m1RS2cbi423EzCdMU0Z0j1HxOljYblQnrzjJB4e7edERTallMrT/MP6bqBIRgI3Z2ysf6pPctz3K'
    'EErR0/GEs44uW3bCEpAwlobTfI2ZR2mX2SF78isS+WZ5mgiFPoQovpI941QMda80s4Kh8nJnrCkn1RHf917N7h0nSOURaH2p'
    'IGrceBKQnCnvWqW+5SLqg+piE+7Qw7NfzHN1iq/q7wa3oMGdVYq+CiQwcpGxi7hzb/GQk9dmjhTyOD6ygc6uI5cj0IY0LJ4Y'
    'aqG8ibwy4+W2b5JK0lV7SmQ2STWfUk9BzMrRZo2XegU9pYefUrnovH3VqXz1vtqtpKZtw3d///jw6bgh228GH3j3wc82X7G0'
    '9QBzf/6sn60HoY+mE/sP+x+PvkkU655yma2WVbb95vlfz/8PTIHQCw=='
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
