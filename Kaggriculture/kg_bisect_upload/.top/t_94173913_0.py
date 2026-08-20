import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXctuXNmR/Beua6F6sETOji2VR4LZTYGkpuBpEI0G7IEBw160ZzeYfx8NWY97b0ZGRuY5RVJt7kql4r3nfTIjIyN//p+z'
    '//r1t7//5bezf/v57Ievn68//vLl6u7+6+3m7GF29tdf//Hnf377n28f//7rb3/7y39/+/zz2afPj/+rffjh659+ufrp849X'
    '12ezsw8327PZwnx992mz+TL4j7vN5uO3r7efNlf3Z7P3k69/3Fzf/HQ2mx9+/uX25uPXD/fHv1g/PPzvbNixL58//PHrl+Ob'
    '5oO+/Xy23dzdP7b1p5vb+0+Pnw5fTT6MB+Juc319fOty+tb94wavAg0Zvvb4aToVqAGT17mzB3t4aMnjnMxHfd39irzry/XV'
    'h403nqg/+z8Ab5u0m7x19yfD8TTtePzup+NiGPV1N1POz8IR3lxN339cHlf3m9vpIpp+N149cOkupovo7ubrdBHZxfmH/98Z'
    'o28mvWNTaQdnPMCTUTr278PVbmnuf/S0MwddT83lcbjsS/ejMPxVOF1g/6HJATvBrGDylt3YgzEbDIeZMfsbfcZ2406HbvTc'
    '6c47DqGdJmddzoXDDWwG92jlZ8uoC9rIokMnnrx9S/WxlL+J5xEM4e6EAXMUzZs+iId3HD58O3vv0IfcwB3HveXBu1/SSe/7'
    'fDrhXTqw/9vBm7o+N/zwAo+d3CpLx5oMDtPEBdLnqdOzNbN9n70FU3uE/NSYEX1a8OHm+nrz4f6XP2xu7z9ff/7P8ZnQafDK'
    'L0kskfI7TjQH+1t70B53Dx0ckcmPnav8/CFhAb7q9Z+Y32kfV3XvNrT/Gm0SYN4Z83FghIOFW/EzgDEC9wTu1W5pp8xk3odh'
    'b6M+hgMIHPuEQcpcFfgpeiAbC/QpfCDzCET7scEf9ZtcdKD8QZVsX2UDUd88nn/i6bS5vgrwFD4OessJ5wEY98dHWmMw3vwW'
    'OCG2Zdy+1ONCU5XgZs9sWL89rf/T5Hsf2FArFeSuGwa+rWAP5zGMPp/A4t9OvdsbhNRIxyG7aqVDsmI/HN46OLDyd6fY9pbO'
    'pYYQIetNdwK9X5uMDXrRVoaF2zEuFJlxmqL2J8wmankQk6Fgj9FFf0T9QmyUoFfBYMSQYebgnUJZvx/g6u2xb4/9Dh+rA1g9'
    'TB0/8g5D+CHkdJ4GUJyQvH238WCZO6fhK0WvMYGntAUgI4uoAoLkUKlM+0lUvdWRZRe8Mzafrm7/w+tYvxs/gRaIUWw0VIe+'
    'FIdoOBYtFAM7ODYGeSATNAEpfNAPHXt6a27QkVF1GJThSMVwCMBXRsvuuEb3g3KMeMqDfnwiumqG7yP2tBBh3pM06IU28AFa'
    'Qsz2wZYn9WY38MdOaWsGL3gzpwIDhY7mI1sRGFjnmAw5z5hbO8Pm7v72avvD5vb2T8C6KaFOrg01fhXkYS66401ua/bMz4cT'
    'YE/PCDmlbsqE0TgFnqo3p48jVGGmUxlUQ1tkiCzl8CQOoTStj8OHwwUeP05D1fbX72CHYqprx8Bmky8yHYHiKvD6nfr6qZlV'
    '+w99empoJaBqLzBCbxOY2ZnHVUDBk5Hv3sJYLxUUW2eQovNGi2X5UDg+hehYYCMQqwQdr4rrTD3zCHqpXCsMmxhcgtubm+vH'
    'JBhop+7+czdB387Hj2dlw+7ovePeJr6Wjs6ZNNWMENGJoTIdau9WCDuKZyW9lg8TIUJwMHL8XuD6gLyk3oZCaYqY06FFw9T7'
    'WgKdmshguu/SxoWysc4QF5OwWvOpjG5uvGyIXBMBSDoNvuaaiDDFAUNqnEbQvAsSnbfTjY6+6WlR2QZsmNEnfVDAqWPh4mmi'
    'TI3fBXySiXl7KitqncyNnZfic8D8muMI3Sq2ymDuatpUE8lTmhMsB7omDIscWILyeEHeqdMGcDWzq05HMhRfOxog52t7yzs/'
    '5HCDepawyYa5u3Gids56kO50mpvnk74UuIGBZ4cYUwIJBPN/FeRWMwr5IQxFcpuDTNMWy4LtIJpqqmeWs2zW9AqEf9BoHE8G'
    'MqR7gTHTb2DiX9gwMJgKv41FMNINDuOeMvumYmwA68AEZE3ue2rEbeddS2cm/l+JWsneYT+URtwubjKW5OUsLRigvs3ZM7EN'
    'av8vdd6xYaVdY39SdJRCkJdA7vv///j536tZHCzbhGZT5yae5ZHIqeBFYB3Y13qaeA32BYwQzU9p5wXO32G3w4DBexvix8/X'
    'fxy7VNDhQlYC/Bn0RXb9PbzrxK7XMoaSDtcrsup0SzDLyHOcMEghAsag51yYW1vhc3I8qg5P6NB8xdPUnx6ey2wLgPXhvC9a'
    'LNZaHbn1JA9C2UoCQePK4MdAWQg5HLJzqyhMyS4qpVeri0fzKksAuMbosI790aBnNk87XdAaWdaVAAY3CXNxzS/fKUomsV2R'
    'OAfwhpgThEmeSaOFuAp2IFHriesM42QtTFAFfZ4FsRqjMpCbU0AjBVPjGLNkaNE2AJup2SRFMQuuNgeaOFx5llRcCaqArkrC'
    'Ulacz3xj/7ySRHBUp/Pf7dKSo/OQtQzZufMK60dyx1gXjk+SMmWERh5mPdcQyaMpJD+COe7iRPXPl+zy4a0x331jmmOGY7r5'
    'OdXSLUsXMOXao5AClvwjv9NEqzoKLlj7TPemCYc3F+KMKd5dPGoS/EuRgowvtJRgAWxrqHmURRGozimbABA/rBIUUEGecwWb'
    'Cf9GfpMAKzxRzVZ4BSILuwKC8E+cfzKixK0S2bumh4E7Fuhg0PhaoeWpNIEMPkYzIixZo9FJ5444H13iX3IZDPVo2vpwJVgA'
    'fj6uE033GHNtVCoSEWOxSBaBpT1rg20CasYgdCPGzTWPS+dlEV+VrzpE6/BtPbSWC20DKb77NxBnSwqLMY2WOo7OHD7ij/W1'
    'o0mzaqPWpVXIbD7N0EQpvtWD59SukaRkcpWW4XvZFfeCrQIW62to1tvC6rA7dazglH5+c5D9FO58JTouBqH16Dhx5Edwe96V'
    '1zx42Uq+KKWwOMGDFI+44utWGGR6WFx3z70uCbKMuQR/FgiXnD8cVixrEFDFxehdEh7l++K1WQdxz2jyQh0omhTaONN0uIYv'
    'EcPujXLR3EUkCR44sg1ACZRtB+Df+bvEHYBfadsNf4e0NxNrkcytxmGQyKRgr9UIpWx4qCNMcvq8HGkbodDbiV6Cdx/jyhK4'
    'iZfvc8mL84dElB4tANAiDY7SkFKn6iEBQqhaXLCKD/y0YR1GX24N88SGfxssGJAgOyg8R5oCOsH/gNyxiIk47sti5S+g80QG'
    'd9gINf8pk4ZLsm84EYfCkZDrBMZfWij9VC/ZeFZ5qS0aWGg0veqUodmlCwTySIrLlBmmIrhz6Y2kmoqPjglB2jVXe03KMii4'
    '9hGrJssBQIdlwFlfGH2PHgT2xbIKIHBU4bWACV7R3ZTfeHKWwBHgpgnZYMfmfOL4tinSkYEfJEAMkiscpSkPR6qiwGNdzirO'
    'UKQ7OF9bC2fYUz0PVll2ajYH46OG3ZDBrctU5gf1wBkBn5oKCfG5XPRIXm7UiyMMW4kMkROvMeuFuTW0IdRtrTFamYSV5cCw'
    'rALKAwdyE12WCIDmkHIJ5WWceIFI08CIVtS3YAuHcx4aFw5oMVvpPs1dE6iEg705zaKye/jYD1PiffIqufqM23a0t6rLitCX'
    'gtwJpXlhQSBsU7hBmZnUJ4UxEq93zhVrXVDVHYQBGi0Px62e1LDIEqdUuB9Yi3kylo++psec0OE4JimIugXARfeLLr1aWYpR'
    'uoOVygijdskZXUrx0/zM5KvksOoLeOAlPOV511EOEGr8kFojaRDoCPhIcnIdgKCeWE8WFTo97APwH6ivS6TjhjNw0SxYejia'
    '9XyQOjODIbxx42EGiD2gbfJECIsEYdBUuQj9VrSL4jgZXXEaN/RQ87GjVurjzkBQjjlUCEhKeIQaeFZ3L8BA1Qy084cKm7yW'
    'CYS48OhBmVx8pmDAcpnUxPuEoh9JawBYCwcaZJ1KG8Su6dzxLBclqYmwPIQ8SJ00IUJSaKTt8NHofSWkIuXOxOku/Rh1YJAG'
    'cId6WWbGiTm+mE6Hv+U7ZIp0dMXkmEZD4LB7leuw3o+4PxYJlETUyuDaLKDjovLDIoOD8I2riwBqcpDSsmDoIPdGo1Xs075K'
    'BYHQutKYFQA4ronZi7WlhONEbjs7KKvLkQLpSZikDxaxUSrECkrQ8a+fz2Wfz4fct8eU4QvLhnv/YgIPPXz5Z+NwMNOWe/Ug'
    'XzWTZJ+nb1hzvF0DwbpDBpogjlKrMDpMe4n0ICiLIJmxkEN52msVKTNRwQUa4SLG0JAEQ9heqCaM2FWiii1QS6FQVodmjzG0'
    'QeevcFpLI+8mTHBTx9XehsWCXDZfg/CI7XplA8xu6sCgUPzpqu+qSobsQYNJdktUWBQbConLRVFyDFIN/fyFFH+cpmhyfIDa'
    'kInKWqxRqLYAA1KQsRsKR1XQOhGzUDd7aeA0F1WCdlR60qZP1QLx9qCrrteQiTFmxSGWEgJqpYLEJtG2iWWTixweVmINudCo'
    'XZLTv21JtuPvV79zkB0L1FJEuRbez3M9RKBAL0mhaDU+lpWoK30mGlPz9y8df39l3P317y0cX3DLHNA7yh1v9JQy8TqYFtm3'
    'sK21o5MKDc39KQTzZL9E11bQA82FOS9mwfihvnaPOFvnNSqNoURKkn6xW11i988om6Krd6NLtqZ1Hmq5sahORSo7prbjqPk6'
    'nppadWZF30BbpqfUMFDlRitTDN57ZDVFA9wmayK6KYIwR03pE3DmRS+94iXJXKYARm4q584K/HEkpVdxZg52shyXSnK/Xwc7'
    'IaxSeTHNx6Bsfbz7VAxN8X+0WilKsLgDI1HJ1ghc8WeOZ55/n/4NsqM6RiitLKkaoUTYoxjEa0guZ9FJNd8X7B9qsGWJxmoI'
    'UvkcyN31EF5X6MY6qKxLnAnkcJ5vjUkLBXYyWEthh3V/SRy7sG/vXf2ey1p1enChjCXq16FtJQmbERH6jCYU3fE6k5xFmqvH'
    'AGM1a7UC6SiHW6mNFotcCCBil8iN8OGxQJ0tYZHaVAjqD6guQsI1YoxUOT9DLUhABfYrQSkWk6XDlj0QlIkmizKVZJSrD070'
    '/IqLctgW5JiJLivPbGDQVSGnSKd38QxhiUsraTIuMvVZoTvocHs3ufxhehhMG73KlmQNHHeJHEqDdY2DDlitPBiCFz8l9jTq'
    'nIJ1wa4c5sBjIUn354zVrRx4wL8XgQZ+SGgrg2VJSWXQwcBr4XlxxQqAV48Ekm6Z1aZWDCKRxIBUEfKYX3gc7iEYMlTKA0zu'
    '0UOerPP5qgkhQQP+akjcCVuOC9qFnnslp5bkCwGvLRcxrCdlV8PHylYMlMZ1c5CUY26MHzdHaPuOdgtoVhnOpuVL8QdN/zsT'
    'ymBadbrhGxUTgFu/MVOeYlHUa6ywuFEBDKbAw4ObT21PQY0anosMxnGghaWXZjLKQLKCJw69duGa8TOYZu466zRYr12L8Vcy'
    'l9kuBgYajHxN1geOTMfrxlrLgLUNjpEYDbS259OAJsuoGYsdTAvTiXCPwBzxQ4cMQ5xekPNOm+CIT87iSVw7YFPwGIOADT10'
    'hWBzSuDczp9nS8JajkQUUyx2IMwYHC9Fwcw7qDWosGGNTZsS8PC5yW77haeFTPqp6c45lz/t6VfV4NdYDB5X1ZmZ2sTGPb14'
    'C9aD0qGDyxdEbNjV8xKhekbSE0xwmDy8rLKscqnDWzlQDzAs5sg2+qQoHlZGA0aDDQCs1+O/AutKUckZxLbdskBTy5ZEr+eL'
    'lLi7WmgxYb5mUm2b0v6YWjo8e6KYulaHrNGrBvJDwIFSpfC6sraJtpeVIVMqQIV2/KZL3izlFzoRoDh1N8EgSQC3doW6lbbW'
    '0+aPrVY9Mqolf3vuv6QTxQgPqrRakzb4vCieXSpZSoOjvkFc5FfT5S1coeNlE0lMtSlLAYiKRlYZl4NuTVtJK1cLTdKI96si'
    'Ot/x00TOx8tJF2Y5L2HVyLB9wDUkuvQADYiABJGJEjYUi+5KQW3CHAv8GS39rRU4UClG+bwFucS3I7sVEfcZcEpQDpLNfzgM'
    'Hp36ZVaPEP5ocGqSMPeSyI8VgEexNIiQiC9K1kYrcvXQhw4wDOTvz+T3ChHgiL28Cbe5wd8gzysuetIbXjmAQUkPP1HtrJa1'
    'mE6OKAbYMxnw7DrplAlv147AuNiqfrNeDFEX+4r1H/fHSCW7gnopOjrAPZuYmgKrUpTyJmies8/6aSu5WEtjzPPRfQeGc5d1'
    '4FVKlqBp6uiajhZSZV/1yqLgLQ/yWf2wfrfECfCKWECBZ9Z1yp6glcNaVkFKh59lTwTOn5/8Hum4ZW5aLUnfNmU8y4KKOo6D'
    '9ko3Bwfrpi6/R7xLhxBfk6NWlwJcFtzjYCzzTip51GVlYX3JaXRUP5Lh8nmp6Anq2V6c69gw+41SsTPtyrF1I4m/5aZCG4UE'
    '4vvuIXEBijuUrReGFhS+YVjKOcYQlhnlP6n4N7jDtEyPNItDqBIkKTfy9EMF0A4DqrXEDd4KAFFp3K2qlu/gRQrQmIV1hoDN'
    'fOXQaC4N4WZpsJ3Fmyp/H1V+Lfz6DJoXkTtXEFmIBfvPTyPJj+PIHXq4DTmFpQuvIJORyqfntuFLZo1U60DIKzGTupOU97fA'
    'jCooRUKUqcRaSeIwTh9LqqNrieOLhxbl/wz6qlqJXAPmJLr/Lqo1S9Ea3J6yCbh8KOgslkRPUtLi2lKfuxI184yOpkRGGEar'
    'eIyYXnDSlNgYWUGgMS3gmhHU96tEeROyqPQBX9EcvtICqH22hoZRhyihgABEgz71MQv6llsetWspgyavkvOHikTmVkiC1oRD'
    'AhmZcIkwEExlavNbKa6ryhp8kTgxqWVNT3NI7B44lWt3uUk6F8H2NW/KzxlDvzQmsQS5MNSJ+f9D79WbzFmxnKVacEpLnaY3'
    'S7xcL8tYGZFhokrBG4E+5A9M0VhZJ+5GUQbXIs4im001UE4BPO3kRRYOeWicuTVgZLXIrM5ko/4VVpg4HdVIIhgFfmnPVK4E'
    'FSfOahW1J05XqgKQVRQXlqldlWQ/UgJjOUQqk5wD8mb0qhCCn7g+xdpL6MHQ4tuvQ/wGrMh86EXO3Uf8r4VgqklQllSjY/wv'
    'QqZRSPmlg0JBuojNgrEtRmjiHJQQmVMwLS8A79F7MgcDp44Ip8B5Y+0XZMKqwo9BZZIOZeFoPdm02JKiozDdD8Wkl03RQQ+L'
    'ISRySaSknBbacpwW16lGSsitS9RtYaQuZ/FWksjUIeIVdrSSUGX8HpAXE+uB04o5XbASRbErJJ+oGWCrsXJsTr2WUKEJPyyK'
    'pGssK+AlFHWQVAyE4JRx9Vg+sLMipY20SWoc6HBCuCepXbvRYqlMokhLuBfVXwU142yubGDpCWV82TpZdgJrlg5Ws7bqrvM3'
    'SZ0GLhCnWL6SojeBIIOeIvRidW+8H8jEq9Pka0UhxO7au6KzuD8EmvK0dOkDxWvQJVI8HKItSysv9KIs0ATxD1YVnTXYviS9'
    'i1hkCfWNWEBUqGgXo0e5TLBY3HLTNJFSWY2ZT6eoBvgY1uXvKseJpEQfwVwVSkklM8lSdcCwaZX0vpZslipZaDyQPpQsZPIa'
    '4VnZyEGSUpPI0tIlY9Haouh8cbbmDyXlHioOJ2kjAzXsPntHrhCdIgpH9I6nOC1FOlj3opDvwp/B88yRn047gTqsgz157u1J'
    'kUs03XJKb4I6BhzOCYKLrqZu2Jd1k70B+qTll2ZrwtY4XlTchehb+kl3PJU3oIvFoZx54oKiCj6UZxJw2QKnVq9jnCShlGYL'
    '6NeS+VMIv0VURlPj2ko2TDwdfhihQ8psbHdRQfFNSuZWiko1JcYtbALcOIT9BHqdI79k5rswv/NkOfcgWlYcl2kLV+6XcLnr'
    'f87tlizQRkDADOGJsW98QZtauRRJEjlSHIbonJZ5k4hvAWO6kLPXwPvhwEEtWgqmWPd9KYxbyGFsWTY8Mh7JBumZFInUy5S6'
    'LFhdIKRNQS45rVHgtCwzLmuYJmmVRYiiMa8k3KTHYl+bEB6P1lDmMGiS6gFNEqm2WjGY2PCXMJt4lCjM5NFIxFSm2CZeZbYn'
    '0vo0J08gnOMVlmJGa1FQFxH3RCpGCE/7WEbamGeleVMlNcJVo/IcxaiAIlAbCGxyKSqMpcSlyYI5UcQDqUxJRIKRZHIDnys9'
    'G+u6ijAWs5LkrTROKjyZWxiaWk3KgIwk5wfSWtjVSnf+kqYp6xQYsatsn59UrL4QyJzJa5gmtInpebW1rXLqJf1y7+jhqsCl'
    '9RwgMdHIK3+QkJ8r8pdAgujS5pR9t9XAUEiljYd1Wn2jjMLuSfhNsoBrQmoRihpdnEbUSK8XlnOxYR/mpygs1l71S5qdVmJX'
    'TclIl3NJCYpTF6DEgK+qHAU7fivxGrMx/cs2ySON1Z7SGCqIocfBundNYkmpsD5jK8Dg2GMYfFJmM3bP3gmsrZyW0iYtwzKO'
    '4V/INcFJob4L2y0yrauKBBPPOop92kGX15kCXTbVPk1KISwhKXXz8GcHLV1mOAa5HV3lihAvTcmKCOz+RF7NZUelKCoAF3me'
    'YmqNf9RV6Y1KDIxTKWL0KQNfXjbFA3Hc0pPUUc1taB1JZIuaTIZUpINCGLMw58cBGHptlijHgUH2gXvQSdeI3DANZatSuVzR'
    'FLKTT9mQqcmEOSOqaLg4XUI2p6TGFRVFV2rMszRDmnvG0tFiHpBA5RA5ZZIuvTwhe+PA7sITscrELFk6FRpJOF5YahZoD4Um'
    'whh3ZJzeOwSokycILhB2lvzyVASoy0wOdx8SF+NCrSnrFvW+icwCc+Eg2Sna97W6oQrRKQlMidBIHD8uY4EyhpEmFYWe/aoJ'
    'Ni4WpcMD3BSyPG+ClcFC74xzcggwH1SWyPi2x5LfnihVUqJt0TuZyh5TaTsHfDDXfSNACVKb+gnhB2em0AMhK5asD2BruoFK'
    'YulVNdFWqaQAdBpS/ltMTvNo6qk1E9AiaEJatHB6jb9T6kiADeC1LGmv0rmJ6Wn2xoxDqALuKflsgOh4vETw/vDR9wH27I6b'
    'CFqPOntOsIYC24GI1nHWg77NwgyvkoALhZlFp5vNY5sSzpakwsRsO0XIPWWjMmc+PWo8kc7jfCYHkmnAkyMFrVlaDOBxsUfL'
    'cZlYjpLUNZtzE1AJfZL9kH/rzO3NpF2Tan9Z0aL4sPPg3XiOOXndp7sRvlWBZbsbNPkQTYM0u9QzgBGv3uqxdeErgRWq8pWe'
    'vw5bEKGrnO4vXmKt6gm8gjJr2AXTnLEn+PW8LewOEpdkfKjogObVi4YW6PtUsGvRSGUCt1UoM69VomOIup4mPO9FdtKsBJLp'
    '0EtmpQeNKUWXE/arEsUbA54nYzJtMtMUjQPHePQKJQpHSRW1hFtKrDEnILh9OEphe4A+E4vrFfRITFRtWANFjMXmqq5xm5yZ'
    '9Zlo5WW/0nDsdGsZ+klYtbRB6BBKFac4tSShCHPZFq1Dy8Kv88VyoT39QNb49wxVnFVLfLO6nHpuk6OFhYEECQQud0jkEkjs'
    'l1KtOWKjXTwUACQhdUyFtA3ioU4FwkeVzEynbHzYQ86xosvKe55ZoheVFbhI6LVQ0hWwDUgmalPEcIm7skpUk2P1CSWLjebS'
    'q6p4Hv2mdlD46hmyS7AlIpUHlraS6q9yiNbtd0CV++S5aq8dVmurK9ci3CTQjXzppcKf+OEWzY3rKOPE9Zo457UCzLXwmFRW'
    'B+X+5yUZ2HoZOYSU4sQt4hg4FXnXKyv6llgovCBMpN5UBec0aHE0R4ICCIFoqLITulpEAaFmaXNd/oaBpbr0ybYHmNEOBzJm'
    'uMWb9GiDWhCvDt0yNfDidtGFomLItGaotamN6bJv+i8zmvSLhClAJWp4HSqvlFugGBt6BnmOFdgPCF+nZcryOcRFGCpzcIPF'
    'FdQGi/SNUgLztXB9pHgSSUuq6o0nFPxvEFqSYgGF7L4UgLFJgZeafk2Ki7qss89ojTAGdtO1KNLthCZDFqTJc+YlZEhNlu2m'
    'vdTZvLTEDWMolMtUKGlCflerJhNvBwBxVNX3/azShNUG2hDPf+T3sE2jY0zcqDavuBkWAjAiiq4z6JFtBk8w5fkYWmvHzF9/'
    '5wpUVm2rX+9eQ5m9AjLjIfm0LpbD+E/UPBMNFwnGCxqYqraXRsEvpBOPwROVwUwyf2IQT4pF1gv55aUUslkeQq7fNkeUytZU'
    'cyMSPPm+VOcvgdxtRV2UzhzHRaWiHzXTY0qnJ+nXmBQnVY2kRYn5AVtRWCeJbzpZKDG0UsizpboznXp2gY6j6MWK2Tq3FLzY'
    '0rRiak2qnVqyKKV3aSXKU/KJcpF2hbgOQraiN47rApLo+WExgXfiDeqyisSYimpLrON6h9QbYcJGHlo2LKLq8IaIl6YlKYpl'
    '8qDlFPDquAfJP201fGrYncu2nEtNdI0J0lrPnWF0vDpeTRTaod1NcRWeNzcEYHx7nBxHNM0+4mJy1SWpDp6QlgbmHxzROb2h'
    'QM6UE0kz841vsOlxyTBhtD4lJoRz8nVRCXpCPEBA7MILbM49wt0wCL9HxRYV4ACwDnujIi+RxRZlGG21Qws2RFTPkc0fJSJG'
    '6yHBGy5VM6ae1BWa+aq4cauMtsb1pWXrqVOk50twnRVgMdMoZKX4GCU5b1XqbC1SG1+VnASWyYykyn/KLaS425J41UwTv8st'
    'qGylN7H6aij4kTg4cCpg8Ea1bkCuTUEZ3mD2NAFlTurJVWqhm1TSMWCKb5XWySLHLKttuylUacu1TpUwDggEXIIubCJTIpHj'
    'KgEIlhEggWYJZ7GLDhZ0uq7u7pK30sCYf/xjIQ4Rf3t4VNwgxGsaRW33jwINnXZ89PN8W7DSk3my/q5aM7alNnQeCzAv0kjY'
    'STp8cOb1dNNCX0g+JIBYmg5oOdlrx3Nc4sJOQdZwk4sZHExMmyPpOlaUHKUgWqogaogkhnFgEsQJ3450/SRNeQaQK7a0FuEI'
    'zHdwtsQOEOgyLhqwfyQ3G6ZHTPHsYsck1P42rSufVOSWQNCafCYhDo3SXTjwfW4I8sTGA5gP8SA+0/WtiElo5q7xlaGw6fb3'
    '2e9/yV5+vL350tJL90e5ipILYE3YIg9Pb4DhxV0/6ICBtlayVHZmUdg4MmPgMtngb1gshwwH6LM0HkIEybzVDv3hG/Jfk29y'
    'y+WCmqmJBVTYTNH2evg/rRf1bw=='
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
