import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXctuXFly/Beua8F6kuUdW6oZCcNuCpQ0hXGj0GhgxjBgjBdt7wz/u9VkPe69GRkZmeeUWjC0KxSL9573yYyMjPz5f27+'
    '7dff/vmP327+5eebHz6/f3z7y4eHj58+P+9uDrObf//1P//+X1/+8uXjP3/97T/+8d9fPv988+79y1+1Dz98/tsvDz+9//Hh'
    '8WZ28+ZpfzNbmK8/vtvtPgz+8HG3e/vl6/273cOnm9nd5Osfd49PP93M5ueff3h+evv5zafLf2wOh/+dDTv24f2bv3z+cHnT'
    'fNC3n2/2u4+fXtr609Pzp3cvn85fTT6MB+Lj7vHx8tbl9K2nxw1eBRoyfO3l03QqUAMmr3NnD/bw3JKXOZmP+nr8FXnXh8eH'
    'NztvPFF/Tv8A3jZpN3nr8V+G42na8fLdT5fFMOrrcaacn4UjvHuYvv+yPB4+7Z6ni2j63Xj1wKW7mC6ij0+fp4vILs4//b4z'
    'Rt9Mesem0g7OeIAno3Tp35uH49I8/eh1Zw66nprLy3DZl55GYfircLrA/kOTA3aCWcHkLcexB2M2GA4zY/Y3+owdx50O3ei5'
    '0513GUI7Tc66nAuHG9gM7tHKz5ZRF7SRRYdOPHmnlupjKX8TzyMYwuMJA+Yomjd9EM/vOH/4cvZ+RB9yA3cZ95YHH39JJ73v'
    '8+mEd+nA6X8Hb+r63PDDH/DYya2ydKzJ4DBNXCB9njo9WzPb96u3YGqPkJ8aM6JPC948PT7u3nz65U+750/vH9//6/hM6DR4'
    '5Zcklkj5HVeag9OtPWiPu4fOjsjkx85Vvj4kLMBvev0n5nfax1Xduw3tv0abBJh3xnwcGOFg4Vb8DGCMwD2Be3Vc2ikzmfdh'
    '2Nuoj+EAAsc+YZAyVwV+ih7IxgJ9Ch/IPALRfmzwR/0mFx0of1Al21fZQNQ3j+efeDptrq8CPIWPg95ywnkAxv3lkdYYjDe/'
    'BU6IbRm3L/W40FQluNlXNqy/P63/0+R7H9hQKwxgz5uMAgQki6YGu9jarjiG5ji3c2gdFK7ByBBohOqki6GLgYBwRvfSKN6N'
    'DFy/HNdtowJelnk0NRbAW7z5D28EzYYomSdkeLjVFj+aAtQATksBgATnoiPS5YCGq7TryT/F0v7/IGffH/v9sUlMyrde0rF6'
    'EEx3ovKBpbWunJkVXzwJjhRdvgQY0hY9jOyuioGSg5Qy7Sch8VYvlN3pzti8e3j+q9exVsBo0B3d1RdD0Giozn0pDtFwLFr4'
    'AXZwbADxzARoQkH4oJ879vrWpDMD7JHzoAxHKsYyADgyWnaXNXoalEu4Uh70yxPRpTJ839S+SkWHTwQLenOBN1TCw/bBluP0'
    '3UD4/thWhGcd2UjH392/bHdrNq110Mc1oo6m0sdPzw/7H3bPz38D7EApbsQuMdgh5+3zQwsUEseYxi3pElza60dy3ojS42fh'
    'uCUMwyl81Q4pJaIYLOi0v5bRNLQ3hhBVDjPiwaym9XH+cL6k48dpMOzpjh1sQ8xF7Rh5bPI3piNQXAVev1NfvzazauOhT68N'
    'rUQ87b1F+GcCdTrzuArOdzV23Pc40x8VtdpkcJ/1V7RUfPTA7rTjq75sxOcnlC6RBNoV/5i63xG+UrlXGAAxuAX3T0+PL2kq'
    '0Ig6/vE4Q18OyLdCJPDii6fCdWX60AxO6uqQICd0YotMB9W7AGQj9jQ58pDXoDNg6ICsn963fO8YGEl8qVy2EirUFEDVHY82'
    'ppGN+4bAlQSmmk9l+HFXCCuCJgIU8/KpAtYh0G/APwIWY/NWSIyAnXN0ok3PhspeYGONPiVHBpw/Ftmdxp5rPCrgWkys1GsZ'
    'Q5tKDmo6aAYRFxg2W8XGFcwRTVtc16EURTbTZbkYys65N7nDAGV4ZiNjNV6lnRkQAgrNSefryFzjMIF6ggDvPE77nZUzouV0'
    'XZKLGNFTJjmvOUsR5QHT9c7Tei2mEI7/OegEX2ttBhVdTF3Zl3BdiiSVNELte+3pIA55W0Q9ZVXj1rHrXLcJ3VvVaUji8gV7'
    'ze50cr2DFk3+VkxkZVd/+KHkB4L+up0qdpjMcaWbeduNTPfwbEMWOaXSOSBtZKIxU/L8mhCXzLH67BCcz9ZpZsKsU6gRdPOi'
    'gSBHtWvvButdfmwxawNYD9d+ZUuMuPhKQLXQvIp2at38FjsJBho9HW0/vn/8y9gBgu4RunLgz1hU+fyuPv7Q9qDvX3Txn/+o'
    '4zei/eB4RpCCc97usd1vKFEK85HDRXXgQEe9K+6f/vTwZmUrHawP533RYiHe6Yxn44k7xtkEEjHCGudAcgeZ5Na8jrpPpJdk'
    'F5OSlNWFBb4CBloJu9aYFPbWvnAmqY2OuXhlUI54jCxQT2JNXBpLhO9Ly/byyfaBO9aYUFmZa+ZyoiaTMUYwb3J2Ce8SBJMc'
    'a1xB8Cmdo6qMxAndbAuDtoDtlRxMe8udnwkGkx4nzkhbfnPCIyewS9IvRVEQ+/smQGa44RR3FdhlzT4taR47t5JONZxN3fMH'
    'qef4JayBzO8l3Xn7/s/l2Bx7k20OG9Pzj5NHXy/PjkEUpDPdKFRWXVIAVC6/vsZA5pqkoC+2lW5Mf+y6Cuw5qSktH6I2zg/d'
    'I4xj/vOKBB11XzqhJjt8L5LhI7/ThKTKrbawlbUFdSef0HZz4dCY1Z139EFTtCw7Kg0BvbClBFZgJ6Wo61DRaGpP9wSIqzU4'
    'QKRDC3NWEI6ckOmAmLbC6wuYdM3BZepg6zmxE0acwO0bWl7jrgdsORanT4pBRa0mJxJT1BBoaGrgvBJDBOeRXS908HZSyFGn'
    'K60OGSaXH0qtHpM5b4zdQ8Rak2S9o9XREleUfEb6leSXJ7DmmWRSEWeOOeeSixQ7S82iy7mm6Q5UMT8LtNBl0okNS0Rambog'
    'hq0mZ2fKhnfdg5ogHJcw6h9dVHFzJZ4L6a9tLS5IRbDHwsIK147Y7ncJ+b/U7mgJ0H+brQIGNHmcZVB8C4NlORZ90QEhBVAG'
    'CMqOcszoaQ7sd2xbU6i+rp8mgwznJTP0fAuReuaTVYzmu0ObVrHSHXnQr8It1YP0uvPKZQE7MkVp7J24WTCOAuP3rWoD51dG'
    'b6IRdRJjr0iFkhA1dTsTYItFsGoTSwdo+JIort9JmVp9NGsKDN4phcuGMO82S+yA8knugsKnKgK/yEp08PdC4BVuWO7igxaC'
    'fw6bOy+5ytTDx0cByRgMgLNRc+9teGN90G8BPyfQWzksxn35G8z+lnuw8SmZ84RxwdpMv6KjIq8k2LFEtqIvrhYQEs4kvWEl'
    'RqJmh9lyw3+udo8Sz2Erd9JkKHc9wsyifqBOT5E1uybX8ZpkqOpkIDbO9PpdpinHcqc3wkmiJdcKLZxpckRoBddW67zkNJHl'
    'BZtYZw6bfsSKp5SIik03PvrEriHSiKorlZOGtXilM9BaLmS8dFYick6IMq4SY1dIZNzs+2ayxIQW7SRiv8qcdEo2WCwL7ImN'
    'i6ZYuricRDE4+q7BoYgLBqcc7auzKS4AoxSgL4raxCHGIl8cuJECIiMd91EeuKntUAx2tlb1KPJAwvvCRo30utDKglPTcFhk'
    'K+xEoYK05RjzZqV2bU53T7h07w8VNCjE74CJQJiTPChf4QLY5cJcAS1e7Fo7aXoiM4oBj0hjMah8huL6KXD1qThEcYGwsRAZ'
    'rRlAgLqSUoMFRExeSIuEhBlY+BLpPlCz33EmvnYKBfPBOIKmRL3L0hf1J7hmf3VJEeeLQYBghnZCxgSdYqJ+qN4JhBfIIgVx'
    'oSx+EHRYW4rbAAT+nRZwiAnsEr/ERKuqPy2oYFeB2nKu1FaqpVB+TXBpcwG54npRqqNWzkB9ofBVlFg8oOU8349qi/DZ8X9W'
    'baCItieFQbqYPt0lLSTunHBaNOA47ZIYPeGZ85fD9twHaE4nagxxtQFIw7zROBe+5gGjTJYMO0aGWJLchiBlpUZ+IWENG2ys'
    'iQvlc5S6JNpQoKjm7IKVoausoE/lcmvEMdmTwkp6BVFiygsW7vZQoT1RWIYs1OmPBMH3hDyDzs/i6EZFnoEpatJok6Z2AngQ'
    'NaUNKfG9qCQHZ3DRxGEJ5y/ijOwa0miQGAklz8EmgBRm841O+Vgd9LnmXgbKGWAeqxofv8fBwFpUFgZdI/dY2mZhP+4Svj/1'
    'bjUYABL08o3EMsPcC2MwsM+c8Ne172YidoEBJoDnHE+5llJJXGeZNbYUg92sPEQPX5+FZsSRZi59nU3kgqWdW9gITUmfeg8q'
    'A5ILyFR1WEmOCq1UCrAFhmgSCgZvX9qBf02I9uoezu+GlC3j6w+LDH5Dbv66RMsYUu6u6vrvTQVeTDgO7xIhC0bBAC4+6flP'
    'xYC/7P1W8vmkpItIgy8gHBeyCMD8Wom7PrIakUPLqQiNSJFdJRpMJVqSOieCSuMH7IhoBDulvIT7B6wVCKzHkvg1lAdY1vZv'
    'EeiUAFgKGcaUNSr54DScWFiBTElQ1LAM/LOGHCbmK2kJOPEkFuATNlHEaaJZCJ02KT9QlOqyxZpIkv+uwg07JWuqIW6vV2lW'
    'be+kJqgwnlSVlHoQzOcFeUW5KmZicFKrx8Bi9K4fF4c0AGJg8QolQKoG5ivFa1sjoao6ZEEUkg0J0XOAs9ml0K+dtdSHuM3f'
    'SFS7f4W4V/d2O3RvX3xjN7vHOsLLdK4ClyW7YoICCkJ09HGBpjMoeW/Q7z5yaOA6hdFt6AImQ6n77uHqDqFTZYaaJSH2xRHL'
    '0RKQ4r42gI1VyCJhEH189JhyiklPI8g2k210dN2+Du3xm6aopEKc1z1JcjRMHIGiMykJu/iuwZVkT0hwOZqlNpkLMX+iMORU'
    's566UplBT6oQsUz8DFoRyGBQfy5wP5qcW2d5scB+Y0FU5kEkSq7mxl+sDz3eOglF1HZnc5dJoC+kH3K86fo9Hdp34iC7GQY5'
    'Fzod9dNo89WsEu7thjBzrYT7H0vTnbotmz+SuCubLd9KVA9pcQT+UKc86ysE/CSN69geV2m/LLs1Gm3haiz7EwozGBOWugQG'
    'g/CxgV4bmcFt8v5depxnH61cJZ37jPyimBQe2iC+V6aRaEU6CPFJpKw7sJoyZSMkKRTqXTLWMoJ50u4VMCf8ALNQFyXBbqav'
    'HiIg1gGsxLJTm6WQJBxEPjlxEwdbwG/zU2D3AM2UZ2RysNPR3EmWbvsOjqsK1PxObia3MDtZrWw0fJQTEfDW8epSiX+LBIcZ'
    'r1jaYuWwqZw/SB+vJkJGyGfxvhXSmEtdyVDhAx1J5hrr1UdbFSd1Pz+lzUfy2yQZilJv7qT6U0m+OdzarICekDPSInN6pwq2'
    'CWn30qpUU1H8Sig9+ymlHGTyd+rZ635lz7ZFXM1RoAubqWuQSo2cPsMoR90nOlczghbosb96KWKqlnlp7dqik3jhXCLNDxUI'
    '73tT50GJG1h8BX3p0gPmIlH+vk+LoyAhtjBGeYIIPptTw71axjwr4+9dZeUEeYDP5JG5dlimwOflry8y5TXJxFyAwXq2cpFP'
    'mUVQYfq28hFCHKGJrp2vIKJjaJXYe1rRMWaSF+u0RZUrsqJ7cdQMZTaPUEgJL1AC+OkIGtXO4snfQsgeGNW1qCpTSkOK3dWJ'
    'K9qa2Bm1qqFipU+5jPfMpA3qQxoufsZkTxfUUNZdMfO53irFqA48doSSKRT3Lm3T9APFVN20PIJS50FND88lEWvl3lv5A11a'
    'LLr8m1Sd3vYRbJlmFkKhih0arKJukM2hiWVoUXuhoT0pIENHdOU4yxUOyIlaEi+oFPeZCx51ZHJo2tkQhwxtXp/YIXRKv1rD'
    'weTFwLI1t52c+2JRPQpVey5/lS1QErhP+R26/FhXnT1ugUZOsRYEJvpTwGZrq/PJQ+KyGbg6lPETh8FBza4oEthtbmz1JxKf'
    'pPbhudDNJftJETPyHEp5Zu7i7CeGzWDh62lP4DniEVaV+Yr7tTFX4zaj37VTxN/FBFYt7V3VfdnWpkeW3uAwjcvKULpSAmvS'
    '4hLQRBBVRryYRiXLAiyT8ZJXNTJ8KCh/dwBzELqy7OU0awWsLrTRezC4vAuBYhk07SLexXnmHCkTHMAJLKNAKSsrgW/EchKP'
    'N5qyT0GIMhvRrgVNoKxZqazvOgB3p43Xqpp7ynrO43Us3GxbDbLwWddIkrtKmWhrLwn52x8DosNXaTYIxoOvrtzer1MekXSC'
    '/X911JuwmznVI+iI4JATetqBVS5xZxXcx4NspasAPZqQE8hbc3vYVBrRDnSANgU2p54pH8WUXz9UEtfZTWk7pHNAKrknZXQn'
    'wDA1YSaZn7FXyxjAZbjqwiawNbIA25ySYIwnewXZcyZFOGg4dPPBTpe5JRXFJ8BQYTkH+t6lIKAMKr1CLw1OT7SQ6PGlq9Xn'
    'kZiUIYyUGljtARYqEIuLaKZCpDQgtreoEBIkFurs94WefUcZIiqrB/2Hcns3w5rLFPARRGjUwpwYdgZ/L+S9iO2X8HrV4koX'
    'O7FIGc49aFDjqMxFKjskHneJ9gQBRyYA6mKDlbyWI5BvosurDvMTEv4DPhvLFytEklhaoYlJDB+19bcsRfhpETtZdf+uB1VF'
    'SzNMV+JLp7ttpWWVbke+4Vku07bIDBJrDMjY3TQdfQg0rIXVdOtkOqwPNTEZiunmPzHtSq1qFlP8zMqhiiUxJwUiCm2ewC3r'
    'FLzkicSsrwbHFLg1VTbQFPRaJmlLOvwAgIBzZeBY/jKv+yK7+JnuZGhNm4QQvI701OjbsoR90qPTCnEEpg8hQ40pDEekt0he'
    'UoT1avMQJpgzGETLwRCjuQELJyzz4nik01NinhG9DIAAZI/qAh7umtQ8cED55EpeQE2qlp9F9a/oAnV0BUhgcRhlgDP8xWwp'
    '5Q+puhkensBVH0psQ41nozKH6NMqWVihNIank8QUiCKtmBKwz0ENjXDi9FYsRVq4ODJDKjJ8qK8hnazr+BDxaL0iCYV3hUFp'
    '/EZIHAosFSa6spyvFXxDz+aJ5Tkk7rKMo7BjvaKdMlTUF3L40zFUpSxnNFEY8ElpUKyFiUpmYlG7VeKLMrUKvQhsWY+BljGl'
    '59NeSiskVYTjqjl9u0oLiphmaj2mRUZCLlIO88mq4pDuSrmXiI2jyKewkiqtvRQmlVrytiAok1E5fzVKls4ykrrOYVLspVe9'
    'FyJFFxyo1+FfgaN8sews72I5IBeML8PAWqtUpc6EKzXFDl1FUfg2g5bJMF+6KCILtbVqrDju7PbQTvcJ/m7JK5HDL9zTOQdN'
    'ych3JE7AnIx/WaHHtdbgCIkztnYRuyJ9gKVYvIjMfb5mJHHwOfjVKFXtU1uC8AMmVgp/LYrmcHLffU4/SlnyybQIz9YJFCw4'
    'QURUDJaoF6lWS3cVhpmiiyBe+kzZpjIFHF5x+JC6bj6tcUuT8TD2Oq8TEFhGK5yjAIFw/Hv9REq5g5xxCbrLmTkh14dLxRAB'
    'X7b67hzjd1ESyBz3MODEYKAwCgsJx8NdIlDAQlsB/LtXEU/+XYrMVwKXmApWMosxB4WmoYiV0EFVPUsvFqXJeecVZrZdITMG'
    'H4nKOOFu47ZFPH/z4gJNxI/SguwxCtpxIucZPWWmF52WTw7RbmaJHIPF+CpoUFVmAU5NpY1BZ8w1F66JdbkTqTLLqQ/QREgF'
    '50Buno6FLco5h8OnLA3hQgh9dhSTQh1rwu2YWx3SebzYKHPDu2JjKlUvS+/PJ8LBbi0aGAhBU7JqU1a1JfHfIVwA5JauxujL'
    'py2KhB92Fm1ir4iF4LNNCYtYccyHnByhH3FflsENcRwJyCSKToUkNaX2hz1EpGpKPAMklIhLK7KuiK1ivUGhLJbv0apabZfu'
    'nqoiIHL+wp3EhH+4cS7kRcmt4nosueoYXwb2+UkRq1EDnovURC8Ty1k+6hPAFEcABmusT6EeSSImX+4qMhvAt0WX353IdSqd'
    'kZQJjHI2T3sV7fIrzhy9RxzwhXNA6V7UMlev1jUyP2zG8IJ1T9W2wnGrzJnqrdvFbYoTFfONKZ+W3T1dKtBlQUczL9OQHeUz'
    'R7nu00UtcUTdLtpmtvQdVbj25tTVCNNrXiRshdu2c5f12rJDxnkwK6e3qGvTEVx0EGG06ETJPCKiJZQFxwM6LbqYbVaepu5P'
    'Z6tLEjBGkWd+/DHso5h5CynE5uzaeB11TYb6AbRpxdM9pD9VycH5VIsRbK/N51vcmg2e18Inoe5xJpmScMq5fcMv3Yvjq/D7'
    '7LmdKYEmZMFqqFSbiL6t9qUdYkHuQ4DNboo8Mlp7yIp3JXltapkzBrPoFFaSIb1XihWUtPyL5EM67pqKXnTNi8BmjRBHwLck'
    'KVXLy6JyXVWcm2lds+s5SD8CXMs+ioeM/+yEZB2y4l46aQo1BYapstlMYMgyo5Jq5MinOajVNE9dPI2dRUkh8mq6ZzKljWak'
    'UhdYT7iMQx7rTMAGv5j7MixBFfzqxabmMZrWUQ5mOshnOOMq1crrCjYPVZACYTAJsk+kqKYqa3UkjESrmzFgAjOPo/JfIfWK'
    'z2sUMdMk9MFXLmbWhtbn+b9ROI0IWxHNRxmOUL3zVtplWktNozgVigQqcd6LU0+TdTx+HtHwQ32O7pBUxcY0+JUt56HWS6gX'
    'Tthch2pITgGYtkDod2y2xKROZbJoJrWUoMrk3PiUtnRDTLptkXRb3vZg6a0qLD2JpZFxWL4OSa/IolI8nRyaImON9znGJD5G'
    'Q2ylKZM1ZPbd96XF1csuMjBBZspN+JopAbUUanatWQvEv2NduE2KrQDK9wUJQWRyuF+bhUfWLdsORe0C7aigqkfIEFZznkan'
    '+X2GFRRw8ljmNXU5M1mdfirazE2UN/GYRIAgmBUZcxnXopwmWQtI0V22WkMAVFD3AV2KbqWB2iaar2IiMFuMHPE1Wtw+jTKd'
    'FFsXSF7UGFDoMIGdbSlyWopJr1NB+NuehGgRFFfS/nRCzLbIzhMMikwqW1BKdd/QGX3ymCeJ2+XRy1zTFJyper5amp8WyMjv'
    'dwIMSrwdCuHk+S+Sezxp4KBfp7mILgcZHSUGWqn+cDuuwbALn2/I8BmGe/tPJMuEAVcuXSUgqs0bBpEQv0KIXfqjUMe1Yv05'
    '8hLLQ6VUV7o4hEiFygZ9Vm07PDhbs+nEUhmdytytOiCXYoWMKO9C+nRNxE+rv5KuWZIrq9ElFSzNzovInaMAy+iQve8st3f1'
    'gqcd2XjcraR6PoHI3ia2KcXxpCTublVNJ45qJwU9UxCT0XvCqgpcDitJ/JL8jABzChNN93nBM00HzwxsK7is4RNVWJmViuTx'
    'vlyqbnINMHuGMhHl9HwBJepZYjS3CjSGnb4/w1KvAJDyXXu+QMJKfJORr7ATIyocGi0BWMpAFebIK1a6gLdDukQaLTVCWqZC'
    'A3qlKE1TKUk50vl53BCkQABhFSdl/uepenFGNQzjuipyH6nGZjRjAk5nS3HbnaLrx4Ut6Pksx7hw7U6dDDm2VJXFn5oTb+mj'
    'TBurHe8jNATsk2M/lczLKl7ZwKmG2WleCLqgmbWsVbuNWAuAqMjmCuXvK/Xc9NTC16fSMD6GJNSa1gOJEAxwFgXzRVaSDzmx'
    'jtqlxRYZZRjv6oI1ZaiJpqFHIcRT3wWGexOChqvaKcUrsmiNzYk+br+Zl6W62HCFXHP6XQkl0YtD9s2kZIcdjXg5CuCk8qAD'
    'UTkd6c0sC1t+HZZZ7Iyu43BHJpXVgZWFUC9XA2zUNN9XtOyikq9DZQrhuU1h6WWNSD9t61yu3qUvTRcZnmfoIcs25QKSH+zb'
    '2KoOWWR2EVpjOhsClBm12opRvi3AY0XUW957ZcLLtsgzo/g9OvhDkmBXbWZF5U/RR0vmrxSYnA1aNkLBBYmFM0OSN1wB0HyX'
    'pLe8XHbKRLK0Tc64olVq4Gp08ZrS0ixrbM1TFSe4VqVywbt/66PUE8HpbGex5E9eLLFUlqD79iPjv586+EjmgyUZN8mewa1Y'
    'Yt8wHOPUNVY6ktWQImd2b/GlZUrXDp0UWzHreKYj29JkmzZkFoHgd2sVz1iqK6gcRpIrKzbBOrlxtcUOem5XNAX5bKBTLCTd'
    'aZ3XYTK2kC1HloBHgnximmo4v9UrXWZUk8X6vgFp01SvMOe6XUU1neRV110dqP6BT2BVs7HJpAFt2FFdLj1jRC54DpRGMVBC'
    'P1fKthUxUE9Oe3R2mEylDjpztoDGvIKTbMQUTfh/aFYqKcdOXhbLq6PRt6pemE9VE5hvSBceADMAsYiq1se6Yalyn1WluODf'
    'ePXAArybIpmxSnkElFVjbuD61Ke/yGqqirQJWSi19bIXSiWHMjT+p26lgfUMb8bhIRHvhEqmIPRGxXxUe0FNslkkYNiYBpA6'
    'SlnEJLUgY0NBaReYIz9Hq5XHxGTkuHsKtCN8tze3hRhxazhAkuFJcxGcGgglQoglWNIcSeWPllyZZwiIL0TlFY0T4w9vlqQY'
    'xBVYxIWnKab4k8QZDuo0acgrA1yVtKszyyfjtMolUWJ2p1EKjJluqw4QE5cwTmW3EuZOgbVnKFRUeoHhKd6I00hHYsmsxWkA'
    'nphxmMW6OikPoccSArUthbXBlASdJBPkQZxGKRT5XBU177XhRBvEqdDJGrm8FhgxhB7WxrNeOlgEgEvKxT0dCWGdOOSeKhrq'
    '0xF3aFEJ0yt5RqQbrawnH45ilU9RVHivRL2Tnr1YzNMb5g6sJ0Zq75FL1g5T5XXJNBEbnSgAbTUIESITAf2O45JuQmiNtL2t'
    'llQzHiOQPt9rNUYrE8EPU1YsGJj8FV5OU3Rhmwjqj4Xh5ouEoFEG7SPAPuKwrbMZdrKsrV1j4fTE0lZiZLtk8OFuMFOcwIi+'
    'DcaNqVqMUdNxE106KdNt0SNyGNpNDvdHpaelvJ5KyWaapSulfkhLLXWiyhJkUepURMd0w/ep5oIVztnnhbqtLqqSaimVMlHF'
    'LGeJHGVNx6QkzS4pjYI/wkxDEwTYtuVyKZp0TNSc30IReK9UL26dCNsYAAGj5WS5IIZMU2kiUbjgwqiBfpjH2uL41u9tSTXf'
    'Wl00KYLreUnkjVgM+S5BlafantsoqidqBojp31cpVHi0P9ce4fAWpN2BpJL5HUBnHLLKpo900rSrS+TZLR3V9ItV1yfjzjbP'
    'HiRyab+aXy2CMFYNJwJj4KXvxsoE7ZBMvgNwL1kdRXC60CTMSmtpcLMRD9IylltIAjwTC5ysAvZImHM6AQAAHiFmFciDcqIi'
    'nO1lOXET3st8tDnfIoYB2UqMco8j359nCwWl59q4dRoLQVe9SCh9q7mLcUJyZh73NJQeRYGpbcG9n1SbuPi5XNTOp+6x1rBS'
    'QgxwSPjXCdWReU6xRhdKYSkEWchqfqhNqV7SLShJWRBl8lsYSBHFK35fQcWrY5gsXe/+KNU2CVfgNQZ5ltM5+FwZOb5FWG0s'
    'vUzbtJxWqoFIvun0vBEYSBrIqpIlQveS5LhDCYCtgB3xiqqlWmbLotUadvG0C1SHsL4RxQO8EhpW73wDvOGV4zpvQc2RgmcJ'
    't02g/VUSAq6g7DkifGwIhbTCRCFcLb+i0ms5hQK0MNt5kYoVSRvna55pgSiNolGnYARvbJtsXWbQnlttvSZWhD3+gkK0JMST'
    'KLnAKlKGpJjCm/mFCv8Kc3XN1RAnugvXE74uJ4NF3vr2+elDw1vh65nNdSqwNtNi7vbOJsuPLUgd+GHVUwHNkbGtEzR1+1aA'
    'W7KX9u4qE7T1YzlNHdVKh/i1g1Kbi+ZqkK7SgGohXJNXZgg7C9wD9Ozj1qcftPCxpdMGUjRjFhEWRbeDZ5unnAGT/2KxJSBs'
    'ALjAv1OqD/8Hmm3hTw=='
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
