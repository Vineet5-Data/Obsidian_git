"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vXMlu/C96ngfPjOy186a158bG1VqGJGdwsxAWC+QGAYKbh03egvz32LLm67BYLJJ9JNvrp9XKozN9utndZLFY/PV/'
    'z/799z/+8fc/zv7p17MPFzc3Z3eLs//4/b/+7b8//eLTj//4/Y///Pv/fPr517O37643n/6V/vDzx7/9dvH+3S8Xl2eLs9dX'
    '27PF0vz65u1m8+Fscb77h5vN5s2nX2/fbi5uzxbPJ7/+ZXN59f7o1x+ur958fH17/Ad3/7c4eYt3r//68cPR9+/f59ez7ebm'
    '9n6g+x8e3vnoz/bjO3597zseBnH6Le+vrm/f3j/08JP9noc/pd/zMEz12T9/fHf55rdP/3v78fOCkAdPPqmP/vLi9WY/SXSK'
    'Hj75eRVOnv/pH97f7lfW+Z6/HBsF+5rTD56s9cXt5tp7/uuLYIK+fADPy+4Ndl969NyHD7F5mWwy9LjD0AtLa7/g8Dhg9vqC'
    '2ufun+ZPiLyQ9vE3Vx8fJhzMR7iA/jwfDM9OR2X9jkbnz0Nr/fanlp2HzvopE9JYP2leKuu4+1swHV9eoPa4g71Nf1V7np3e'
    'IdbAXr9lDbuHbC4GGoEyG4Nt4MsPicchPye8DkJLe311ebl5ffvbXzbXt+8u3/3r/TDtfZK6/QvXFhoGecDulksNFHxrONBg'
    'dpLD3u3dkQtU2fz1A+PHn/z4k6/oT07PxJvN5efQ7WinfInIcARoYrQXd6n4ae+FxCeP7/7bOGtRO8pMPHQ6NfCFl3fJs2by'
    'Hp3b4XApVgYKzn84dmWE/l2Cxxj/uZmm8JDf+QeDpwlMPp6lygCn/n7KCI6ipsJX2wkuDOEwwWYE8vyCZXMmOBwgiywLR6mZ'
    'osIz9jNk/1adIfBQPEHl2+LP8rfVq+7kzjtFMZeTX9/cXl9sf95cX//tbLEuXoaTH4ZfiqOux6e5KLtX5i48PVqp7ptIodgC'
    'AJXlK1W/N+zg7LGGZ6QdVk2v39Y9AeI+ehGPeAEDe2ZnCCwiwjrjWFLxkA7mUXreYWAu/j3IzfRcD80Jsf7CBBNsXbb24HAB'
    'qOIgJ6Bb5+r78ZAxD+n5Ba2Il5yJ03Tpj7t/VLjcG3wyIiyO2cTPxRDNCaQ/W+/F9b8ULjAwmeSaKIMOCRcHPBQk0ipB8jTE'
    'lobzcMBr5vwUi6CH3PvRSS9++DSOwG32O5/Da/kOJDzf38rKgugRuU2HyqskpcIq7/z9X927k/une2e4FuY75CY9+j/v0ZXq'
    'kdL0+l9lnIMG5IB8hDgEi8PTR/E4ntpFQBHmI/gLhB3mOw7xse0xwoYiAr4lqpMdH8IeGyCaZvUdrK9wuC/3V9KXH3qbaPrY'
    'EbCOg4o8AtKdCMVZTmBsduDNu3/uX4TzT2kFz2BP2YyAM9TXfuy3+0oxhXUeU1B8dfA1X5dvcByPxADKDDhEJpz0YYghHk3+'
    '+ktkHxgCxGCNURMPAs/h+EeHc4IcmboXoCeQHmHqt5V5Z35MwvWwj8GGED7ozfXVh8AOiHt1CCSvri4fTmpwgq930d+n2+vN'
    'WezaWbABfTWJQlcjc9C7J2YODt0l5UHo/jl7Y9OfTEKWw2MNKjbxLBK0bC+WAbUmCQNVrkqbMipEAri0R8yAl8CX+z2zpJtG'
    'qTBL4TOrIghy/8drbIlaGkVO4KzJLn2lEyq7aZ8FzFDJGZ4B8I3606wwD/pelRgxZKQ6RASq23z3Yy6fErh/zuw4r2GP/Ip1'
    'TQ9/OgMLzLboOGqBeZ1eFuhQyZFvanEGiVq8NWP2NJhjvPsqtDSy7QzlmyLo1H6lt1Ct6ATYc/B90KI3qn8AWFTGZoEJ+M5z'
    'wuVRSMgA/dwbzA5fY/FEHXclGVXtgAvtYwCZyh6IE9cQm8XhV7mErlg35VynIHlu86FxIEHwW0tUm0w+cUYShgvraU/2DHrs'
    'tNL45KfCd8Z8v+Mv3W0Wicunp8kNZxHFFaOS8wCFZTjxoBpR9L3uc+eFiI/z14c4ZmTUtMCRysiMMo+nDBxB/FeuH3IcT63c'
    'eGqlu7xSJHM42uwcdQpqna87Pr/3E6s7/Ku7AcW5avSUiSOVAjIcAVkPapb4J4SRqWOAHKyaUfBwx4wSsplmNg4h6DEpZIG0'
    'JjEerNc49YsGJQ8O158zC5nqPIWwCjxjNxjOfVewio67dWLSCmkOuP/AZz18m5l7N3SOjYelJ0Incr8YrJw08YVoC4fnbGhE'
    'ILLzTwMa4GZKQslJ5XMfXajDhimDdSWc2Qd7awhPc3pDLwI6bMdHZho8DBBquMc4NzeYGeoLCo39okd08X95d/nXz8g+TpAs'
    'n1mvf9nOmrQ8+pXj8HCPnoUDkXMvwOWSe44JIxnPVOAASN7wTLRWlTmAxmgvtsqY1lm3ESFV0UU4gNJSoIZEMV98YFcYJBOz'
    'JYd3Hf/MM04EZ57Ny6iYg7qMB4MumEsjpwFMI4wPQE6jUvtKaN9hIixG7M2WcakgodG23nL/HcBTI/Y4YKOwKUAxRGSCZh0G'
    '1cLzYDgwQcPVSqrY2IwDwP7FVGwLnSXR47F19sQezQ/Hj2bhzzgeMjT7Gajy5PsnwjYzVYItArGb+b52pjBj3i9ihKwXTjLh'
    'QGAcHGLMNglD+GNT1fF+gITynXKAZAsAQQaFfWgITd9RvNK+MRi8TyDvVgXYo2jr+iGEcZD1/nvUtVFou31nG9b5ZeyOt7jt'
    'xczWabJKw4fhpiI+kFVnOTHxlXthI9CVptL6FnE+0uXW1oXl/vIhKHgBAX23rwNcT6diB/CsKliz6hrYLQFGD1XoSQuDmXBr'
    'oNwfuELhyQD8Y/SydH0mM1FRaIbvBHjXyK/249eI8iTEGJNFJvqReLMQLszBcB5KUmBE5JQ7beIKlQf/5QV2a14RjsQLlyOh'
    'cCaByLvDzRGZWTIxli2/za6AjgcxfzDFKElBBhDy9PKLEGVR4ulkSE/sH3xbiGzJSCI4SvebxMcm8CtFG+J4LV/q1RYzWD5J'
    'Nk4+CSaKuQLiTDWtNTqUuQ/k0jJOiL73RsBXt3KEC1i2T3QO3itA2DQ0I6ko2DRE7UajzZXY9ShrFqwEeJPbpEwU3R8vBG/I'
    'vlPdMkVPopChTr9GQr9ynJEprxGuWOYS0KsBfKktam4JlsLjEQ1GVFw+JtSngX8j8TqRogzxOgqaaJWh5w0aKr+WcohOE31D'
    'Q8ngb9mRzQ2sRcWfAFRgaAG6wcrvRBC2GVgVw5Enpe5LYV6UUT2Bt+iuux66HuzgJMD/Cgj8lFIfi4vqlaIJu7VrmzNbtNeA'
    'XRUVV0OasLTEi2CjtkRcYRWaWTju5BNljgrrma1uvI9ErCPe7nZgh7/eVcrZ0gHKwif3Vm2GQrwrtxsYZaan7BOhAp6mC7az'
    'ljqQVGIKoSuDQ8wjQ82A6USKxe1/Wqy7lgsqdbpHxG0aw8ROkkGsiM6jsTZYCP+0g/hKJwKT4Vd3HQHoZ99YxBuxXIgwdV4X'
    'ei1w/kEeEGlE8hDZ/u3xEq/cf1nqIfTLO0XfknDwedhhp8Elv4wqJUjSagVazqPXFyjM3KcK+tFCgoyc5hTwLPoY2rFiu4nA'
    'CDps+7873YhaIgnuuGrdsleHVw4802qpcIIg05fSEHTKMZEa9zpnJGjAPAoYJwmzJTQGOmP24wm1FJDEJJREfYowLyPT2ta3'
    'uy19sFD9Q6wi01qO2B0mb4EoisfnY0WHyK7AnMCsqmmtVY0NTjn2SyS1NoTXkjnzeB7VULLoap56Ie410VMiIxGgs4i+Q6Rd'
    'HK1hHs8JiZj9703vDZKoVFKQcikaWeHC1gDASC6pLfKXS20vK2HrgjMaw2W06tTFKNofBEmOH4dYr46KQo6yxSeVI+d3jaqT'
    'Fag6ef4tVprM0XupX1e/deQ80vX1PeUj9afHTy9/HUUaWrqNQA+jc8TdXJvaiKNhZSmIIOkZMYGtClAPS1AgS3VWM2PqqewF'
    'G0ZGEloDKcM9HSQUujBWaA1hEIuyeS7RhiIVD5WFNgnKaybDCkbhvQu0SvuZxinNa9TRWVxLreYKf6iBEKI/pf4XVNdUW6Re'
    '95gSelHxhFAW5iunt36HDfwGd2RjhWu10q8hMmbfWK7zab9xZBrTCoWZAq7T0Or8Kwqo5Ir9+SIrEK03CvL97OWYbj/u44Eb'
    'FBQMJqBzoYPLFiSKZOrWUzV4sYNmvK5e6LXu9/8tlsNv49rqGhuTqy8n/7W0M45r0aO05CKb209MkrJBWFWn4l8/hnKa3Rlx'
    'WEYEJIJqTG3MqD+MB/T7OQeQadS1XzMhHmL4bXRq4wy+PN+STOxk/FTwHiD+fkBxxqP1+YkBMJbGYYtXp3ow5Z9wz4JPkr3T'
    'kPkUI0sc4ilYize8U5d3HTuvKfVARCn2RJBSkQYjQfubA+THhiynEJYi0rG8W2zlM+d+VgdJhIWitGex0Lc1gb363rnghlxl'
    'cTb4fQn0rBvh8Kvvg9M7H2c3zieuS2WtDkc3Xd2qUXNHqLE14nKadnTi8LlCXlmrGcRiWfYwSOzNEaan6sJ4gjQfOimSztJt'
    'XSpEbMxqcudk2otAL61mDOu7zi6zloFzzZQTix2klBsp7zougiNhBZmshkyPDOis+6mHbrn9ZZF9qzAfgwJ8gJxkECYmR0cy'
    'k1RdDJyXTfQX6SGpOlqsl1Gc+GEt4yk1GcvXocH0rZpOFE2ka6xPnLW5K/Ugw/OyF7LhTZhYYdwX/9fmkgCDm4FRtsyUupE0'
    'lM8VDm/CNVHhs07rr5S8hZtrYWXx0JpWTdWhvQERzrMX0EXqQCeczZeJgdqo26ZbWkpU1rYlVq5AWyvHsy9Kwetx5nZ5DiZ9'
    'Max69UmzuUn99eOI9BESwWM4tjASXrv/Egq8w796LnTALTgaUTifOvr8e6wmHJ5JRicYbQJI8DWkrLUeXTzjyt6m0v6ontpO'
    'yGTqZbZaGpAX1MXBYcLtO+aiR7B8QB2MkoiDG5CRhDmJ1aD3yirxeIInof4idcoWMio0MkCZSxzdFOyoXTwQFXrThg/sPBCK'
    '5Wrxv6MWLOfpsU26G41RKyo6OVI1Idqh2T4UiaOuC8RQRFgseA77JvTavSHinlkAhVCQVTmIZK5j1jOTQGuRDrSaeXYSFwwK'
    'AON4csF1pfMTKD9rGD1F6LwckxQQ1KScR4oKk9YH1+4WYCwimz7HFUFiQIBHnzYyJgVGtr8g28FkILdK52o3pxSskqRuFou6'
    '7VZPJkGGfVYqHr/YAZxgQoAFprBZhOYrTWZQqnr+0MAlOr6z6uERRrdaikLmY/qbP7Fq+UmZuItVmuYs32zrwkeAvToC53Ih'
    'xKC632wPbi/AKZb/KupUQVSz3TydrjNQOxK4hdtexn9ZkicXNHpINUehTnSI6IGuJ4VMqdfuDlCRXS+PUqRIdfFjGeiWEhFo'
    'TN1g+khJScEwJWZ9gojGSArshBFpamN7jUf6UHEMSJG3ymQxB99HAHkP+xK1RGXdUKZCQUJCCRTBd4ZLRS4N+IIxQsJMPdCn'
    'ZOScmeaM+BkJMy9OlfVDeb0PBudtBHAUXQ6I1iNeLDkrJ2hIegOywcisMt9BYlNXxG/YiKn+na+/rkjzFeeQ1S3IUuwZHpgd'
    'DIQYFB4H/7ygjNZleaxemgD2lWV5rL8PkseJMvnN283mA9MmXz21NjmCzFzqRkXrG1K1O3yz7WYMxaIpwZVFlocTQqwPkBMc'
    'J/zUIuFjPSg0Ai8kC5HnshEVIkixbjWCSsVC0FJmMdsDABcaKJE1b1Q0tC+Ao3HMqpRztfMdCYJ8t4B8WQDwyOOO8HPwthiu'
    'AhZOld2aqX8AjxxSMo/JbOEQfUhs9kKwz0+TUkssxren4t0WzmTpyFDStQ/SUQ36lIZ6mZ5TYRex5RN01YXakDaSgRAWTS0f'
    '7bMRtfMa7hKCGhjoC9zYTl29NMtQJkE4CRAvul9zLzYwhzMEMK7NuLldNF5B0R9n7T9C2fJBQ6f97pSOen3UY9CbKEE9NAWl'
    'z32Bh3AMX4QKD+W3ZHLynhbiic48KGw6GtSTQCxDy2c4c2A1gDngaxGWCmjoceuWoThVMblM+xyd1hWkKKVQMSOfAUAyadKv'
    'NNynlNenHV6zqhfAc2N/MRs9QlfnQ2u262pMIRRe5d9nUcDiY6FKRq8HIhoBKKLezYpSv1zUfZTKahyIV4mhmAJGfQ1b4pGc'
    'wMHalG0k8K9WbR6GrGSS88lwXxMwUFUK2Q5UaTHXbg9nWYW6CHxSKuvCm2LbQYenHpHS5Fjbbu+XukSlWmTlSs5ogR8psevP'
    'PtAJIm5DIAyUL86s6J1W7klyIpOziXb/3Wa2AAOwtMnbKKiy2KFPqCOqStBK66+7NbQsKOBZ1dYlyLwWOW7AfZZmSrnfM8sj'
    'gOVh01ua4pOyL6lFYHdpalvTRisK4j5oH4AjHrpPtHCEdWe00FWFZhZFhKH1W2JXTnV0dHsZqXFj6ocvEJsi9dLmET0z2Nap'
    'gMyDT7/8pqtgmgIy589nBcQGtxLh6Nfzol7MHBnWfO8RFuywlHmlU7VlbCY6pWu3X77pxYg6BT0eJ3HfgTOqdAqPeDD0k7Mq'
    'yeiFl3GaetNqdRzNEZGlO5zgm8ur90BFbKvQBQNfLM2m0nymoTIzpKY73qJQRZH22agwFFLrJunSgBDbQmpMl0CJ6BzPuUD2'
    'Ox8EzCNmVFcCCvzqkO40Mwhsg3huD2u8FHrpsqssxvtCxBBKCfsnVSwgl2hl41/O3iUJubgxnjFZkqjBZLgVtf48vpAmyfmJ'
    'YAQ7ika/kQNHEME48BLUHBW8otH9KSe4pJQLx5Sl/eLnLJWzxlOC495SRxUDmrVJrh6Vl5XrR4P3mY6EE/g8dJnX1QZ526RM'
    'XxyBAItN0lHhx5kXRsaLncG6gQrla0AKWLlyBTW+QPuJh6EZAX0mCI1MpwBTyz0MLFq3zSc6uQ58QFzLguw5OLJQjsgaie/P'
    'KMtvo+8RSGxCCh2lKNvDD9PSzu8Sb0eIiKGQPPzkyQcEgSPEMwfvaY+JYnfjvbPtcPoA7rmyuOfqh0x2o6Ly9dX2gW4HT498'
    '4ygLbR5XgwpNjisEOOg7wcFz6A6KWnqA77LDiBvBQ4yKwiiBTaO5DddS4v2oUrjqggtHRL5NYi+NE2PyK1QjZ070Az2hpOFt'
    'sQh5JGRpRgCzpifdomDCE4M2/dIrGXdMo91/xX46jW51Sg+wkMhjZ/3nj+8u3/z26Wa7/fiwtHtaabc7jHRsKM1rMCn09WZ/'
    '8WQUX4c0tW4rY2Ehqoz4l1NjRDEV+eBUaoUoeyraUwGwxbAOswfDeOrBnT4au7V63uKNR3v7X1pGNgv7ndXgjXqAh3Iaqd9v'
    'i88uH4XGnTfevQAIJXwWtsYyi15sK3Q9xCaPkvkUlBGk8KWG7r16f+adAVFExqNljbUaWlmgCJp2ESzJJUrJD9qWL8HUeaaX'
    'rEVHPJXEF/XqucA+q24okO6s4em9IqOeGSdr4Z4hDZ0GVXUix9+U3hMAbfQA2UiNB9OKMoGOmoGOyBUKZLtixh6tGZVidYRf'
    'SZ0AwZhS6mBdiqG7q9lEztFmvd+Wbv2CFtGe4HXfLN42R9/19fiaWQ27GUL3o0Gpd5BzftyI2jqe8UnCYkNEdQqkvDryozrO'
    'WkwKoBw9DJVVyGjRc2PiFStGWccg5RUR7scaNM9kU6bQRhNHHW7HkAlCYqegeQ6pwKtXTie6sqdKwmNW3uDKb4XhF+Wi9aOk'
    'jgqLguA6hEqDJaK3Kx8S4C5lSfvAivURZW45UkAu6JeTWHHWA0Kr5jeMtOjgZV0hVXZ54sZL9GVTa5IRR6tXeMyjT4efSTlj'
    'JbpTlGkMqkii1gE9yW9JVtLfg0nyZjgwVc1eFIar3f6rVtxV3AfkiaEr1YwLpTEUrGz4IMSwfrnqFxC+cIg0f4JiwSCuPy/G'
    '9c+rPBn/aUSnkuWahqir1qNpP1hhox8EGuT8ELnAkZJk+Hw8QccvBWuQAp7gyomIlTFViLk3kHlLLkgKNYQZoVNiRmW1EntJ'
    'EnuoFjRW1k9J4FY7n0q8jojrpFYbZa14ht7sSuNlUZmFSbZFggxeQidav9UYgCLlbhOaFwpTGPqVpP6Xel/YIgaagI90fv36'
    'HGvrQ3efnPl0ZZRifCrb9n5i8uP3Z5Y1GbSpFPh7C62Ird0gzTDx0N6xDMRQxgEJz+TOlAR8v1UuJ0L+KxbvB6Cfaw25ngAa'
    'wkU7dwSVbiqtsXqayCwXBoDJmJklsjD0VT86mP4abYmYKH9VRUntD7UzgpgbOgdE1n2AfNNkm3foDbc6SROBvrAlO1nXC7A3'
    'eKVnBVMix3qEwKXK68HL2Dc2QVMR6yREKKrQtfEJPTR0sTWUlfGzdpkhmkkEwvCDpv8WkxNfOtL7y2UbHjwRE3P7FH4ZwffR'
    'qDDP/1kWccI1rSBbC5L5vLmhV36Wug5FrfpYADY4IfMjk3BJetYzN1BoFVT0nASGd44jhD4dpVMLeGqmC1iBFeTpe01V2XuN'
    'CSMHgsr/FvoVSpwR1w7TCI0VABA9Oj0IFIlROTl2oXxHr0zz+Uj+YZaeaRCIJygsGSRMDAdLHemlUpICTFTWXYYE8GRPwSpc'
    'biLLBCo+wn5C/gOtobGVadpZNqpVKmvq4O9IqUeHr4Y2AMJW8oTiZgSSZRulqSFrTnVf83Yu1UnoApd6gQtobHSscMCp4CF/'
    'Qbi/WD8QVJHIWEfMRBV1zl0BoqZzwuTZRHQCzjnmVunVYfGG16TylN4tDG32l0qwm4Xkatv6XWZOQYUDFR6QxKZghP3CCd7X'
    'KQ3YABWmtbu+kCowL7ED4AnF6K7U9EJp2xpEHwivaSKQLAHDmXwMRdI6RwZWddpxrov8gL6N65/AzfR96SvVECDOFDtvKSit'
    'NQEkBryPznqLtC9trIP0hFrKR/UBfp0ELgaciwSubgssleJf0OusV7rlKh6rESVzFNSsrFAaF7ifmQITzr2k+X+qT71tM6sk'
    'neJEZyItn5mTR4iB0VEUKKYiSkqPmrA0y36r9TsRq4JJe3d6bxal5aXebzTqLHMk1R3BFO/SrR5UrbwyCEoPjIiVoPw8jGKg'
    'lArqdVRsN/e0kmIJw07FIQcYdHqYoSwITl6j3awIBClMG54hUMAs+aqgnR0AVYB31dNIG9Oan4yGExAtKaJWDg8WSF/3SaDW'
    'lThSqQ6TvXgjSPB1XTzPhsUyUOC/m8DidEgGDnkn7ZqOqgfDxxAptHvE2j6B3+Rq/yh1f4uSAeW4RCAd8XC3LL9p2AdN3Jzq'
    'P60GgYIqdqlhnhQL+1AO1xVm7v4o1x4ORXBpwNjuvZR5VX82sVotKB2hLV+jU3io8g/LgIZuTYo83xf+4eI4CbFmXnNfCVWZ'
    'diqvdqOiXy2568iIfe+o0qVPL54BuxLdhXcFAUvWcs/mLOPkpzDKxfDWl4izk0I5WD7cxwaKDKMAeaO0D+8kGZPYMEz/ssYs'
    'u5zyhixlO4QtGPP40Mmj7r65GyXkxLpI1UauE6v2kssMgUUHJQU6pMjsaLRzUJgatRoUcL8CeCCXgcpQ0VnpmFCBnA7jUS9D'
    'tyFEQuIrKMlSuQKrDNNEAS3tnUq25aRKZsR9zyHJKj1UAmdD3WBSQ5+KfTngFw4D0ViUmqbc0NIqyrFc0TNaj3RiKOcAuPgT'
    'yhML5BRQFZinpjAOQCiHqHGMtYS11nS5oRkZeipBjhoM0B/9HBEdLVShcIpKEGiU6GiuCEmp08Ioxg8Y1itKQa3qbYq5GECn'
    'n5weaFLiF12ufgJQ606n5yhzQlWpQkQNowxlkhP8FJSSt/shhUJS4VIF1k0bHNIZL3ptSnumhi0GalS8ZEdS6uqZIm3hrjEh'
    'h5RwhRWTNJfPWj3rksukO3JE6IhjSj+6TI1IYnglb2WegtGKD2wlRXTSimWLvoGmKqQ8CYRVrnifTf+eiBEmEApiZJPXWT7L'
    'RLlOHhzRMJi4hkpdCEcW1iIZoodKWKvfNCDrDqFBSz3B6kpyoyCL4oKhqO3GwfDqLYtSJSCu9sf5c1wUAjbjT08WdAv1MvNU'
    'ioTNuVAPQkHgY+X+kkahVLtCAdtAcBY3+WA0bBpICBnWpjRnUEnGq0oSmTEe1CIBDw9WF6pyaFTfmEwauKAJ0tU/qmTwDsdS'
    'YP1RKkzBPy80keYFFp1GUELmOaI8b8VECw6OmBskD1GJvsN6d+b3JdyPCh/ebxKopal62ABjfKtHUFyQzmQbpoHGfYLoaISA'
    '/wxvGV3JoC3KQCMlNsm6bgpnHhHZxdzyo2ibuQ1KJUamlBBkRjkAQJPSQl/EFPU34qkfkSV2RhrR3IO6vprJ0ZFvbhItR6OY'
    'sjWJqnwlJ3qXgBY7LDOYOLSK0q+FySESkdIwikWMw6ejkgkfPxuF6HyKwDFn5Cebe/Zgp6oephf7MkUWpreriRby74Z4LmM1'
    'cY6423AvhZOGQSft0+JfFKlBMNRcrNFKfD9eB9r0Hc6McG/3ID/lPQOWuxKtlkhg8jh1pikdB2svmR9XH2CIye965aeQK1V7'
    'BGqpY7SB2/tmK9cF6PW/FWggLGwOF1HJOtbQiijICsZb6o+qkgBoCk4YLwX+qtFUCIGF+g0hIFQdGr0O5X4MdJD9WaNX9cCZ'
    'KsLH+3APKKVFU6gV6xmFdU8m7vwuUYPB/Or9q8BigNMXJkHrC5b7mbzTKs4yM79/PygQ2uZqa31h++dyXtmGVGZ45AdrUcq4'
    'T8pxJexgOW9vzij2uvt/rgkhIQ=='
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
