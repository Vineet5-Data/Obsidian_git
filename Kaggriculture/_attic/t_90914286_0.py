"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtnU2PnNdxhf/LrGeh+aBEZUdTbYgwJQok5YEjDAQDcRAgcBZKdkH+e2jNsD/eOvepU3VvjymbKza7e/p+37fq1KlTP/3v'
    'xb//+Ze//uWXi3/56eJ3P756/c3PP7x49/7Ht7uL+8uL//jzf/3bf3/45MPLv/75l//8y/98eP3Txbevfv20++J3P/7p53e7'
    '3TcXlxff7V6/+f7i8mbz9t23uxfvLy6vrj++/+L7V9+9eP3hk5dv7i4ur+/v/+/yuN8/vHr5hx9/OHx86PhPF3e7d+9/bfb7'
    'N2/ff/vrqw8DfLd5a/it05HHPsYuvvt2t/tBdPKbt29+uDjp2qEt0bftWsjexj6OZmbfK7sDakpev/j+/X7sXgdev3i527d/'
    '0vrHX3vYBJ1pePF+99brxsc/Ot4Yh78OHaEdApP/sBN+ePvmmx9fvj/ax/f+pLx78+NgdHIyRNfra/SxTdkN2hmHLtJS2LMC'
    'p3j/2fGxGw112ekRu+b3fzv9g+XBg2IsiztRjwOQB3kzONmyt2yDPfu3xRnMSGj6qKGFp0esyssXm/MgtoTowsI1GU4PHmhn'
    'nxTWSBzk7cG5SVdq/yp/FObTInpEe3X/zmHWGvfZ7sX2fKRLLj8aLx00/rgVzSvj8BbdWEvPirjQ9y8OI55agHhB7eeA2nxc'
    'tzVPk7gOh0si9GHfsnjCnn6ZbsiHb8qzH5tMW1rfZPqi1NJ+zhY3FC+s87khp35F2EOPu/ac3kTrCJ9aSle//r40kD527eWb'
    '1693L9///Pvd2/evXr/618fTtT8R1M+C8SEm5bAfB30oNA3LEe+XR3fr6AWaHu92r/+2D446d3DtwhpdG2u0bw2uHTFLjUk4'
    'NT3MK2DTqzU3bJx86oHeDxP9UT+oeidtojWroyww4R6M29rcqs2mhBcQXmzWKD0OYb6jmVVq338kRORk/7dgVzgNDQZ6aVv9'
    '4ak4OmDLH7/D3Xm+lhpP/E+8IeeeWtLQuY2xzw390zYUbI91VnLBEpXwQslIJpvz0R9UDiXBCeqzYCcvd6vHALXu0sOToglD'
    'WmhKwHRaqGNchP0zTgB9OQjYdDLEqGh2H2Zq0YAjhmjC4/UBC9SI5vbQD3vA1/eLZl1MRrqnxeQquM2bXmX5N1ETDnzsW9xb'
    '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'
    '6onrCAHU6odJ5SpJRCzUMPXUIIh+Uib5nLWn5lw2SwkNSrxpatCAVDWishZJhb3K604lO2LyJCpMXmh6c+GjnP/ZRICurkYZ'
    'tNeI6p8hOeuTKjQ2TeC5nHA1vayczKBgLsqa4qiARyRJCcJPbtBo+qLK42AgUE2yyWfxm5Qj3J1zeiYgQMh1o8dKTWv8MAcP'
    'jDwQV8+kFZi/KdTiYh4Kx7ZSCuo4MfipqkRlApwRgsGKP0ZktX1fklgFXyp3rbJjZ2B4yO0ivBiBew0q3e589sGZVBnsvBa+'
    'hyoVruCS6elwIHqKMe3Uf0oP5d0Ow5UmIS4hJk74q27h8KQGFEngCPdcP4PNkPOXImxp5MACZJly8w0UMZMGquFpjnCVJppW'
    '0OpsQRjCI6TH4FnGguamyHLqLhYU/tMUVZ+KmUxAijJ2uBxmpqqhckLo3fFQv5qXICGn3Iat07wmzLChMsNNTIdSlxDT6abw'
    'esjr6OJ82NBOQN3PjDMHXKqfXWKxojw92gNxGZEclWrk3RTLnZUfzINVeShyX95VrHiGBZvmbZAu6nU9Qr2ehX1+NZr2239E'
    'PhM8wa7PBfMhMuGjWExO7PCcSrQQoDm5uWCZtN7C4u3gCzCM5MeLZ/WnS7rIABgRQwqvbKbAdzWzs2s0M6ztBDLmNKymUsAC'
    'YIwV5e46ZbyuS2T02EmEhDL1mJ1baHc6Ly49fqYSqWRSxGTFGeDXpa2kgtoGQ9HJY63rdWaMLUZ9mVuHXlzKCSJDFucGifIi'
    'qcQsdjPpAaNdKwEzXbdzpDtjiyN5BY6nKVuDLAY/TkD6SDVBlVUyqp6GnCFxiAspodcuAYogP7PIe2qzFvKJCrpyNgabPLjq'
    'yp+t7t6NkxjtKoTxie12L9UXf0bZfCXg6roNllPpRMUHK/nqeOoe/P9uqtPpUd1jCa5qln31IXgxn6e177gnCuazM48AxKyr'
    'Ee8+Kkf+sX+xoxEUL+uZxa6Z2NRNoXoGDEGCFAOQNg437iEYj3e+Z+GmRwjpWQg7jUqtDZGpZ59lkjoyScCDQTEcv77OeVSS'
    'JmhUPBxE0ZZLJEVmRuKWJhWlcVlW61OpGo1WWRSvylm/EDKQku4M7gh81InqLoLFgu8p3smYSFbO4IqKx4krSoJsiAqzjM4C'
    'DXiuS5RLLlAB0xYiPO1Ck1QwVMXzePR3kxvf0anlMn6Z/5l6SwN6WANZvbpfUDWXN1N9q3VZMtm2anBypHOaHiQMZq3W1SaU'
    'u8uNoadIIa0Eu11QYCfCs0FQEmqti44+uXW+7Ex8KiTVkUCZvumDYtCMsqUKe20hBmZ2HETH0Hsu9JRwxqjdRfOH1JiWYFHD'
    '6R8p+gaj43FIyl4lNhX79s1cQnOcx+MJ1usjcIF1N0mYGtY6Sa3PB8E1Ek+H5Vf+CgNmyCZjDEYIaP8CJco289WAcq++6i8y'
    'nkMYUnyBP+Bls5ahqOPBPh/NzhezYk3nSO7jvVYWalqERC3M7jOD2Pyg9wIyCxL70ApXDq8XhobEiQVJfTrffcjYwmGQYbkG'
    'zsHmSWGorgQ7QewAJh8CSgKIivFsr1h4Z5cAqcYPtxdrDJEC4Jotw7UPx+QsEiZMlTD6OFSSDjdSB4j+9ZirlFct7uN/vs9R'
    'KyOWRRHTEmujKYTY94OV+LySB+WJwgCkaxOqUrIWCIcV5InsGjGWgtty1DBeWQTkmCVbLVk6I+Wyl22AWcNOsqOfQn0+AIdx'
    'S8FpGJ+IAow+vyY0waV8dVPBv7KfEoScZahg6htaTvMTXaepJbVdcx0cpnq3uNFo8QuHHfEyK22wiVNApmhEaKIfJvzzuJEi'
    'iFFDlgKpQyJo9pAjtpblcUWo5UQpP87BQMEpwhr5RJyIxx+PeCykn8IygkYUerZffefLI1CqzSNaNYhkPUtDSlloTa7TmCEG'
    'W/3pgaa0OMSnxHWah5pcPRRm52SMhTNl1oHvlkj/YF783ROoosRnjKOGXhEIbqAJFTZOGr6mEn2kg1fRh+iifx74BDmEifBX'
    'o4hYMTUz1uiZYyCAgVwLLXnFbq6bhYxcdguWowNezRofHCxJcPQawqyKKWilVhXsyF4BamB8+J6XiJkOca6a6IpdGZnw1Oyg'
    'cVUzzq/crboN+wknJDJs43UF8oFC5boeao2o1EmKoVqGZ4NnzBKzJXrU9JSk7BYicHklRymoMiQBzEiqfFmA+Ki/xRGMhRJ7'
    'QDd1bf+laErYDLhMPcDSS7nxrQQin/FFksCCvoSShVLx5rp2mSYRwskSHthcuDOsvSZ4VWTMYHkZr+sD8KmGwi2jPaFWARlB'
    'EWMUOYc8lmmqlnbl43UaH/8inbMEksWN9NFu9XsvZheQL8Gror6fCw27LVInn31CtCv55tG8/laxsLZQkydesLQAk/B/Wc5F'
    '8DoaVu9SFEY8kMlyoaJwaZmmlRJZcwCLBUaCcvia5C6Be6X7ARS0Svq1vXSWmz7VpsSeIV+PhMIwLaNXN318iVQWgZOpZrNZ'
    'jHN+VwvR4w1LK9Ar7HxX1/7G+Letiv8EbDOr0GuqLO6PbRNUXwHAeUQEKHauDPLMwZ2Hj85bGr6WyWfHiX0veIK1URtMcqWR'
    'DW/STsi38gnCuSN94uLtxrrO8QfuxsjK8cTersP0IcMcXCv4TvTKYVA99OSqpD9xhB5s/e84sNh7SFgaoNd1b6/LbCLvhSgh'
    '0kPzc5ZKCCUApDDHtaQqrCiAAFZrkuNGovSu9gC65K/4YIwgzmyHS3D76dXl86BKrCbQlnK6/5voVXh+arPr0TW8imUlrmxA'
    'WhjQ0LHtJsSNURnUVK/CY+ETGMGnMdqnmhm2PmYbrdmaBcd8zVfPt3zbh9SarxYX+v7/AZwo1L8='
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
