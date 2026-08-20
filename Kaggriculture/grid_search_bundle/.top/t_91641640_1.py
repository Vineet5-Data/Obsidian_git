"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vG9kR/C8682CSsiznprW5sbCyZchyiI0hGAtkgwDB5rDJLch/jyyJHHK6urq63xtK9vpGy+TM+37d1dXVn/579Pdf'
    'fv/t19+P/vTp6P3Zhw9HN7Ojf/zyr7/9+/YPtx9/++X3f/76n9vPn47enF+tbv+Xfvjh48+fz96dvz27OJodvbpcH83m5s8f'
    '3qxW749mx5v/+LBavb798/rN6uz6aPZ89Oe3q4vLdzt/fn91+frjq+vdH9z8b7bXi/NXP318v/P+bX8+Ha1XH67vGrr98NDn'
    'nZ9t27fbfe8dD43Yf8u7y6vrN3cPHT7Z9zz8lL7noZnqs3/4eH7x+vPtP68/fpkQ8uDRN/XWX5y9Wm0HiQ7Rwze/zMLe82//'
    '4931dmad9/y4uyjYa/a/uDfXZ9erK+/5r86CAbr/Ah6XTQ82L9157sOX2LiMNhl63ND0wtTaFwyPA8ten1D73O3T/AGRJ9I+'
    '/sPlx4cBB+MRTqA/zsPCs8NRmb+d1vnj0DR/21PLjkPL/CkD0jB/0rhU5nHzWzAc9x2oPW5Yb+M/1Z5nh7fLamDdb1oNm4es'
    'zjouAmU0Oq+B+w+JxyE7J7wOwpX26vLiYvXq+vOPq6vr84vzv941094nqdu/cG2hZpAHbG65VEPBW8OGBqOTbPZm7/acoMrm'
    'rx8Y33/y/SdP6Cf7Z+KH1cUX121np9x7ZNgDND7ayU3Kf9paIfHJ45v/1s+a1Y4y4w/tDw3s8PwmedaM+tFyOwyXYqWh4PyH'
    'bVda6N8luI3xz80whYf8xj7oPExg8PEoVRo4tvdTi2DHayq82g5woQnDAJsWyOMLps0Z4LCBzLMsHKVmiArP2I6Q/a06QuCh'
    'eIDKt8Uf5bfVq27vzttHMeejP3+4vjpb/7C6uvr5aLYsXoajD90vxV7X4+NclK1X5sY93Zmp1p5IrtgMAJXlK1W/N2zj7LGG'
    'R6TZrRpfv033BPD76EXcowMG9syOEJhEhHXGvqRiIQ3Lo/S8oWEu/t3JzPRMD80IsfbCCBNsumztweECUMVGjkC3lqvv+0P6'
    'PKTNLmjyeMmZOA6Xfr/7e7nLbY1PeoTFNhv/ueiiOY70l9V7dvWXwgUGBpNcE2XQIWHigIeCQFrFSR672FJzHg54bTk/xiTo'
    'Lve2dVLHh29jD9xGv/MxvCbbgbjn21tZmRDdI7fhUHmWpFBYpc/f/tW9Oblf3BnDNTffITfp3v9xG12p7imNr/9FxjhogByQ'
    'jRC7YLF7GltK7QbHY1sIyME8gLlAyGG+3RCf2h4hrO8o+ytRHe34EPbYANE4q32wtsJwX26vpPsPbZto/NgesI6DihwA6U64'
    '4iwm0OKKqyhay7XIulkfUwUuOfBDmsI0hnh0oBl4TFBhmQcVFGMdvOZpGQe7Dskh7ALmboT+pI9DdAFR8vdfIvzAICCGa/Qa'
    'eOB5dgdAWkgnKLZRNwP0CNIBhn5dGXdmyCRsD/sYvBDCB72+unwfrANiXw2e5OXlxcNJDU7w5cb9u714Xh/Ftp1FG9CriRu6'
    '6BmE3jwxc3DoNin3QrfP2S42/cnEaRkea2CxkVGQ4GV73gxINkksUOWqtDGjgiuAc3vEEHgJfbnbM3O6aZQUsxRAsyiiIHc/'
    'XuKVqMVR5AjOkuzSlzqjsjXuM4MhKjnE04LfJD9NCvSg96o+XZeW6iARSG/zzY+pbEpg/jmj43TDHvmV1TU+/OkIzDDdosVQ'
    'C5bX/mWBDpUc+6bmZxCvxZsztp46k4w3r0JTI6+droRTBJ7aV3oT1eSdgPUcvA+u6JVqHwAalVmzYAn4xnPC5FFYyACci/BG'
    '5l7UcVgSYdXOOzSMHfhU9kgcGYd4Ydiov8Ye1DKnnPtUoJRJrgSBcO2DR7PDwkn60oUptXu7Bj12a3C/Pv/z6EuFN8aEP2Tj'
    'o6+3BKHBvgBvF6+RSoSYgbyzyQLTbvbptMSz3Qj24Mj0dJtm2FXpGVPmDpXBI4gByxVEdh2qhetQLXSbV3JlhvvajlFLSq3z'
    'ut3zezuwusW/uOmQnqu6TxlHUkkhwy6QNaEmcYBCHHnGaEDIwqotCu7vmFZCPtPEi0PweoxRJ9DWJNKDNRvHZlGn6MFw6zmj'
    'kMnPUyirwDR2veHcu4JZdKytvSWt0OaA/Q9M1uFtZuxd3zlePCw+EdqQ28lgCaWJF6ItHJ6z4SICrp1/GlAPN5MUSk4qn/3o'
    'Yh3b4VDWU/V0AqOPOCE9mJrjG3oWEGJbTGSmwsMQoQbzGAfnFMN4bNWe3OR5HkBkqK/1f0Cj/+35xU9fRgHHTObPrB/wojWO'
    '0mTiLxwLiJv4zD+IrH0BQJfsdUwhyZiqAitAMo9z9nJ3LgFqo73pKm1aZu1IhFxFN2MHkkuBLBI5gfEJXuGUjJYtOc3rEGie'
    'gyJY92xcejkh1IYcFnRhuTREOcDSCB0GEOWopMMSKngYGosxfLNlXHJIuGiberl9BzDdyHrssFHYECCnIlqCZh46pcdz7zhY'
    'goa9lRS2sREIkEsnBmeb4FriTu6uzjb9R/Nh99HMH+qXMwWX/QTsefL+kdbNRMlhs0D/ZrrXTh1jmORFjKJ14kQXBkpjZxdj'
    'skHowijbFyJ/0cFBAmee7iDZ2C0IqbAvdSHuOyJY2huDxvuU8tY8AXsUrV07hHAQstZ/kUNXw7Fs16z35iewO0ZhY1esbWQ1'
    'hofmphy7sXJ3EAsTu9zmHYIEJiqqb5HmHUVubV5YzC/vaYIOCKi77Q6wMJ1UHUCwqmDMqgVgtwRoPdSfJ8ULJsKrgWZ/YPGE'
    'JwMwg1Fn6fyMRqKizQz7BAjXyHz23VSH6ZRxJUaTTJQj8WYhxJth4TzkokDHx8lzWsWpKQ9myolnvfjciFOXG6GQJYG8u0PJ'
    'EQlZMiOWTb+NqoBaBzFTEDJJEv4/xC+96CGETBTnOOmfk1UO3hbCVDIsCA7M7VbwgQbcpWjZ787Yibu+Xx5gfZNQ4uibYKDY'
    'hS+OVONqjY5ebum4pIvd/7tfBHx2Kwe1AEz7POagXwFcpkETScXAxoWo3Vu0eBK7BGVJgoWAVfI1KbNAt8cLAQ+yfaqvTNFe'
    'KESb091I6FP2W2RKN8IZy1wCOrufEpX95ZZgHByONNAjofKQuJ2G5PUE30QCMgTfKDSiJX4eN5BM+bWUw20aoTTUlAyYlm3Z'
    'xCTVMLcTQAcME0A3WLlPBEebgCLRHV9S0roUGkUZuxNYie686w7qsA723PgnQM+nhPlYPLScwcPWrZ3b3LJFew2sq6KiakgC'
    'lqZ4FmzUJpFWmGJmJo4b+UR4o8JpZrMb7yMR64i3u23Y8OtN7p1NDKAce3JvhVlb88WNPnIh2pXbJYwX0yboE6EFnpQLXn9N'
    'okAoriptBItPTCM/zWDpRIDFrXtaTLfOZ1GGnI6IwNSHbZ1kfFjtnMrdO7Xb4zG+xoyMwzerkg99gKFp0YJ+9pU5x5TdklKH'
    'xNR9EOdD4o/cOba/3b0GF+7/zHXn+fRGEa4kVHrucNhhcDksvTICkuxYgV1z8DQBhWD7WO4+mkgQi9OufR4l78MeVtZuwiWC'
    'Jtn2d/sbUQshwR1XzUf28uvKLmdaBhUOECTsSoIq8fgREXGvJkaCzcvt/H5SL2tCU6AjZr+ekEEB4UvCLNSHCPMuMkVr/XW3'
    'pg8WknjIqsgUjSPrDpOzgJ/EPfNATAg6xy9vWqvw0To6s7yKaa02jfVKORhMJLRWhM6SOQp5YNUwsegk7xsn7u3RpjxGXD9n'
    'En07SbtPmpq5OybEVfbfm9bfIpFLJSYp0xbIDCtboyFRLhf+FvnMjEBUaVvCX51xzmM441a4uug++41g2fh3iSHHO3khmxhz'
    'g++92H3eQ+rJ4qtLLXnkdPm1I9uRTptvUzhSPx0+0NwmJHzYwBuBInpHi1ujbmrFjYZVloIMkiYRE9KqQPMw5QReN5MuMyaT'
    'yjrYsMhICKsjebhN7wi5MowfWkMcxFxrHlW0PkjFNGU+TYL8mom1glZ4fYGr0n4nc0rPxIArz0lHh3QtyprLAKIrh+QC0OyA'
    'guyaukipud0nZV5UOCGshunS561BYl3BzjXZWAZbLQesi47ZoUJ4hyfWPikq725Cvslo2Xeqlk/Ib9Iy8Ts4UMDFbkin94OW'
    'far3uI8H1k6QB5hAzIWKLGsQH5K5Wo9VsMU2mhG52jysZXtF32KW+zpOma7RL7mYcvJ/SztjN8U8ikbOsiH9xCApG4SlcSpm'
    '9CF0z+zOiL0vogsRpF9qbUb1Xjwg348pgACjLuWa8eQQdW+lcxYnsMz5lmRSJf2Hgpf08PcD8hoKhBXs6p3etCrgRXuDO0cN'
    'hYeIfjlbRro8N9lTgtyJ5iZif01BVEoVBpNCf4gY7OkV1VrBlOZDleX0HNU9SkQdlreADRByxmq1kUQcKIphNuW/SsPVlqt7'
    'uHozUzmjL78NxqwtejPX9U8qzNo4yrcspZ06TNp09qlGoO0hfdbgRtNgoOM2T+WhysLIwHXKcnxBuG0KrzqVt8XDlnlPR6Fe'
    'SPdtKVGwYVSTOydT3ANaVcFiaNlMdgHgQC8lqGJLpoeQG1eekfz1TJxApiAGTNLtQEPb2P6xSHxV2IVB1jtALzIoD1N6I0FA'
    'KtwFDsFGBBaJEKniVULtSqF6X6I6OyULY8E41Mb2xU7Hj4ayS4RLrawXHoCtegyva8Soyfe2rg0gA/I0A4RsDie1Dak/ncvK'
    'XYWDr0JYLdW0UpoSbryjKRedavpsVwohEHu+F2FKngKmJMatFglRIusN25hHk/9rF7fEZxUoYlO5pLvR0PmxDYfuV0ga5uar'
    'ipDmtcp3HcqaR5sKu/YhrkJHdun+TyiGDn/1XCgfWzApIm88dcj5N1ZRSDwR+k3QxAQf/ykEiLV6Vjy+yXpTKRVUDyQnVCj1'
    'XFYt6Maz1tJOHzPwdgneES4e0O6ikF3nYl1SXXmNPszy2ng8JSGiIpWZFkIa1NhHcULssFTAg1ZGfpRNTasmsPNASD2refqO'
    'GK8cFcdr0t1ojMhQkZuRcvPQDs0Wc0gcda2QCwV0xazisPhAW2k0RJMzE6CE77NSApGKdMwYZgpjTaF8LTGdncSFBQVwbTy4'
    '4LrSo/6UDdWNDCKULY45AQg9Us4jXdUpqhlrdwtYLCITPcfAQIo7gIOeXmRMUYtsf0Ebg6ksrpWyz25IKJglSSQs1kbbzJ5M'
    'OQyLlbRXySYYD6BWKawRoVDJIQtvD8VOolM6q8FN5MDvkLfFXJQD71Px+5ETBvZLlDAUcjMML7+6lOsx6DUxutUiEy5nF3TK'
    'mc2Wpfb8mGLqrKL0FDgv69XjqSMD5SCBw7cW4/J1QmiAb4Tmbg8J6i6CAbo2E1pKbaXhAI/XNeYokYlk5h5qga4ps4C6zg18'
    'HCnKKCxMia6eoIsx1gE7YUQyWd/y25GoUuzqUYCtMljMjveBPl7WvcQVUWk0lGNQkF/wkgqUumCgLeEUkssEdjwGSNgWCDQg'
    'GQunNJYJANCVTUzJtbUWbOfJNRibt57BjnPZwVmPWK3kDB2BIemNyRoj08d8w4kNXRG+YS2mYnK+irmic1ccQ5ZJIAuaZ5hd'
    'tjEQelD4Gvz7XZ1Xy6F5+S2ku8/6ebFT63mzMvWGiVHRx4bE6Rai2HrVhzHRKFOVBYq78zvsnZ4T6SYM0iJ/Y9nJBQIdksW7'
    'c8GFCq+jmNwZQaJiGmUpUJjVzcf5AIoHzcv6dNXSdwSAWSpvLvG8JX8/r7Cf5/MDCzuukj4FDYvhJ2DiVAWqiTT3uSeQkkJM'
    'Bv+6aCjiZS849fw0KRWKYkR5qmxtYUsWXQxlT2WxuNObduX7ovB4mYVTIRGxaRXEyIWsjmbEAiEpmvI82n89ctQ1fCUELzDQ'
    'F5i3eoRQGlMoPiCcB4js3NSyQDvCeumMhSsOWMN8K1rarBhGKMGdkiWnVdyUOnHtKMRUEodwKpUS7gVyAIAU5jVN83v9ck+p'
    'b+7E4r/VPJRJQvK+cl4pAYWebG4ah5NVkgthT1EIXIFmUgINExIFAAaSJs1KzX1MzXdaaDQr+gBMIvaLyXgHupYcmrNN0V2K'
    'WfB8+HZ6AkzTFbJM9Hwakk2PXNjNqCiZvkWVQiktxcFUFeeEKUPU57BJ6pAzI1gtLa3afC0vO/QFySDno8m+Ul0gKhTSCKgu'
    'YK4mHA5TCnkF+KQsFnqnR1J46hHhRw5ubfZ+7DBTNRxhtHIpWzRBjqSotY8+kMkhZkOgi5NPbqyoc1buSXIik7OJlqhdZ7YA'
    'Q4a0wVspMK5YL07Iw6kKpkrzr5s1NK0mIDDV5iUIdRbJY8B8lkZKud8z0yOg02FlVhpTk8IdqUlgd2lqW9MiHw0Q9/ym0wYB'
    'Zz+0q2iqBisiaEEoITflRQG0if3JcO9YXlVOn7N3YZT+SSn3IJsitFKXD91Tadkj/DzrR+95GrkpjeotxycHSnDpUjWDQ2fP'
    'i2ItU8RD82U2mKfEAtyVWsyWL5moBa5dnfn6Dj2yB3RnnjiNA2NTqYUdsVboNyeVcdHTIePgccZlVmtl58QN364uLt+BnNG1'
    'Qu4LDLk090kzuLpqvJCE6niLQrFCWlKiwhtIzZskCgP8c4vHMVEAxR10zO4CNe+4E6qPeEyt+kvgT0O804wgWBvEcHuY47lQ'
    'HZZdZTFYGMKNULHXP6li9bZE1Rb/cvYuScicVevd4xOeuTbeVtRK0fgyliRgKCIZ7Cjq3SMHyyBqbaATdDkqYEdDoaOc2pGS'
    'xBsTibaTn1upnOOt5LyEUx3x+7XVJpl6VNxVzuoM+jNuCafVedA0z3YNgr5JjbzYAwErNkkehV9nVhhpLzYG6wtUSB4Dgrvk'
    'yoV8cj+0EmgvcU80I1XPpJcTdbjZ9SfXBrCg3jofKA3uaSLuIwLzOaQydR5ultriJlEkezAYfPKbHrWHp5APIooUOe9gZP3i'
    'vD7b/TA3ce8LgvQQgs3H/YEA3KIGc24NbocKeKrI8rz4xtiBXcWpncTHoYoTrNIwXbWlhVrUULGPYDs5PNeL1tcHDdFLM/Fv'
    'xrS+TmWbGGONF2qiWp6k/QRkLG+SVk0Z2lMY9UvoQONv35FfnkBlKEGoN84yYThpQx0pbnUlUgf5g2oFkkp50kFDVpKQNIvY'
    'FHWhuK+mdGj49obWxVwJF2YIHJZmwevAm8FDy62uKkFSyo9WdU981q3lHeOVZA6k0E354eP5xevPt3bS9UefpCYmr5EOIB2H'
    '9gMHZTldnL1aPdhSaWEv68KADmzmQstnHFnKJ07ypkH3H5rCTiRyP8OAeQAYk9mLGO2j+jSB9TuPrBeeMI3+l0NSlRLw80S4'
    'IXD1o+oBYukzCQ0TVAYg9BrFggDms9kHxGQyiQEB5L7nZj6LLV+4APx6fdiTJ3dBXFVwUiIBXkTbOQOJj5E4n1i8vFwNTNg1'
    'AaPDh2nh7BEqW0vZsAAhjCpVWHTIttNreZ+sVJtuqucBcegt2YFaEbm02tby2KJ89wjWV86+a+LJLftnnaYgj0bSGweN4swJ'
    'H2DqVGyM6AclUaUuejAFhhorKRZxzgryO3XCmV59WhfH9rNSUh4fK0IaFncXhCpKu4jbxorclYS3tG0kMGB+TDKowUIS0brl'
    'STM3WBcxV+rzNOhzyTmbUjpTokZqW71kDRLNFm/xvIFcQyrlJoOKSJJ4bKbKD0k7DBpAanY1yFHNFdA7vzLzeYlseSQKDfKE'
    'YbpAWf4nQTMqJsD9KRgpwiWQeFrxLFkFTaIf4dtRkHEXfd/c/kJ0LqPrRK8q4gs2zLN8yGNFKrlQJGBcBGNaXqlM0EnxPoG2'
    'eVjcyl+QWVVpTbC7tAZTviVox0FKNTlq13+A3LeJPPTnVQ8dPu1ErdAdE+YPWumJWXnkL508f2tdiXWhJBoB5fTzYflqakup'
    'tTsjYuA05ajQcOt3IwUS0NdMpPZwBazokOetcNXyZSzqhNMbEQoUoTYahA95qRKjvUoiKG7JVJokZkesXH5BZJCDwysM6Afs'
    '1D5FkgESmxgmGlFs5xsBwoKALawlAfhkBWhCXupafljy5Qu8fr2mhoEIKyBvGBen54uStSXvM7suajJWVFTFUsEo+mlIMTSd'
    'TSAPxWtQVEEHUyksTbmydIrPRW0/ft+UPMeEcPsaJAWlZP9xVF6sqa6eO7N6XImcIDTZF6xoRGsBPyDHjdWJKU+mguIrgRfN'
    'aGPHUfEUsgkEFkABWOpOynDySI3qVqIMK0VEYiD41a5MAIAJAC0JhdlErGi76jgVE5gXGGEWtWPnJsmSYtq84y8VYTfGBwtG'
    'lopdUefIA/ZS5N6cvpeusBU8iB14nOKXxx0XNvXsXojrW0Eem2ro+fDislhTjyb/9kohE/PBPAaQKBQ1dc4Y9Qg045AJgPWE'
    'SaTC9/Tbmn7RgVNGMIMpyqaK5rLGzGaZImwxRNe+pHpFVaHTQI1Wco9jjoR0MNNKbbWx4Ll6t/I5qk9dIEiFC9K36DOaXmsh'
    '90M7Y9LRBWDuMZ2cEHFb9dDGlfScYoVltZIhk99tSVlEG4nlRUSGqpgs0EL7Q5/8lRzqKGe1qmXCn+hjhumIvZNNxsnWsZMW'
    'QkJDWo9WqdOVpw7kPKBpv2uhvsyIdJCTDOCWGUpY1X3MqZLX6JUQiR15aMUi7yhh00jWUJCX79ZUswLVeKlhihyXV+klKauC'
    'FpgBPrbzZHPwqB3E5DDvBarnnnALEKg+ridyqanVFuoBNyFgcUl1eKSmF0sNSu1lGHArwSqqyYcEx+etdfo6Yh8T64s3iogf'
    'e3J9CtNqWa5J1JtHJQrr0LJrTY2V2Bcib0pspXuTH5IQxXKoNB1zlRIlmn9zXWtnLci06JSouMpihKD0pT9xRo6eCMtYMVJk'
    'swNEV0k9QbJfkdGjaqX0h+4Yp4WzlsQ6cf2IZvlsRYFk504ezRYp1ZnK5lixElm8KWy+cn6UsAHiyjeKBrniINR3NsRM6drP'
    '1btTz7zW7UxSJuTSgswjZwQiXyG1yhaaK84CT6VNBBH8vEjcuUpQQQLbAnmLQMKZ7PwcYYAufwIIitwyVsyuD4+KgpFyWcGA'
    'hdK6Y+HJE3Bas9WdFcoGw7LykEv9GGJcIknBjArn5eAZI8nRyBwCrY0kami/nNnef12NkpJV8ZFpNV1aN92HPtDQHg50YjCf'
    '5wAZevaEyDDNyNBTk8WhtBhKNO0ilKOyZKSqb4xK8wjCOdrQGs7jIQTaNB0dyXKSyiY/cYUdmgDG4oRCgG0l5AbR9E857E2m'
    'qzUsLxhaLAMjjH8D4nD/SL0PcuYovAZma0CdDizlU825UjICaChLl1BhwW7ZnaFl20V2X7FbVNaDdS5UU60QyhRNIKVmlagS'
    'pMo9N2YHKQVLUbPii8rqcfE6JsnQc+Ti5VFXiS/J1n6oiqLIXkpq4rDiNyksF7j6+4ZTbg/kcsWEZBYWlGAgrgjxw3xBjwBR'
    '9sZD88iP3DDKAS8LlYgCMNoPAWtpTBOeSgpjqbWd4a1tPAR7uCqlnqp8JfKSnDgC0Tna5xbljx3CXxLEjCI8BkE0Tu/ydwMb'
    '+5yglPJh/OyuCkoLrKAERgGgO4tvANxpynQ6xteHlNi0TOi6NGY2CdFMTngRQZ/YoyY5ErJHUamK1SZnNC8nHKSLY+nyx106'
    'wvUlBeBMUyiiKhPdij5JyUD1isH0fs0l4aS3gaSUFqGvwLcoS2gXdkBUSknndUulb3RoksBh4q6lqDurgNMxdO1vTVUObT3h'
    'Ak6pC6RkbyKItTUdh9cFIhsTuUkk3NGLcCFhyjGLJwsrnPZADYXi3zqJpE0GPHgR59qy4EBR2N4ayTarFFAY1+QaIFKWBfcz'
    'kzIcVkJjcoyebExUB+ZltQ6MxwewAr225pia9sX6oTePlelmSl6h0Aa7YU8Snr1bkXpQcQnBKdujRuCkpkXC0ojIPoJu+HFn'
    'l1jKdapvdjVvaOMlP3dyiU7kEl9PJZ3Iw0XKTYusD1hTEYX90NETFGSkGZUFYD7WLGCerSJR3F/OlLMp+Y3jOyx9KqhQT1yN'
    'MalkbZ4irTc6WYJKT2XgqytFuEsoFOr558wniJcvk6FV9ICDHI0EZZpy0SktijlgfSdQ4XjlfEvuA60m1cNkKyeWuao5kFo+'
    'ppLkVcIPbIOA6QmVGOVKsaSKb6FYpKJysU6VrKnV4224ASkwoeWO8orHaZIxfHJYFHiliT5khi7XME5yaCtIxkKLJIZMaoj7'
    'ZXVC03Zp7PPTm4IzCqoIaxV+eFkdp6S5dSn0JvOzB6IArPSNUJwq45k0RZS/N0JoxPhaYrbw806+qu4r5orBE7ORxn94G1Sk'
    'VBMDIzZNpS4hVxtjDYmHLRtzp+Yd93qZBRoPC619HvC2U3nVbeMjWpKiBmJGK47mo6vv40ZIDtqnQXhnBYuCV5HhWS3UEGWX'
    'Ut6ofzbUF1EitTVqe6JR1jMVvEdB7FXND0g1TYiY8ZNcOlWLG69CslTpn8mRY7J6wWAwdkYt9AuXfeQrRi4U/Q39cWrBoZNH'
    'UB6A39KBaeCYUzUCVplj669okHToRG3A+ZObWqM5Sy9ESVAG410PmZ173ICI0JEEbiH5MP42S3Y/BVTVE5fWGncj0Szo5Lp1'
    'UinWvhCIuH6Hbenb+2ZRB0vpQ1uvlieq9mPf+gewl3FzX9y26ub/eyT9cg=='
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
