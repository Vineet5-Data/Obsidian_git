"""Pure verbatim replay of ladder episode 90909137 (opponent seat 1)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vHMmR/C985oPmgxR1b1xpfBLMFQVK8sBeEIsF7IMBw/ewd28H//fTijPdPZ2RkZFZ1SNp5bcBOdNdlVVdnRkZGfnT'
    '/1381y+//vNvv178x08X727fv794vLz4+y///df/+fSHTx//+cuv//jb/376/NPF6zcPu0//1T788PHPP9++ffPj7d3F5cX7'
    '17vdu4vLtfnHy/v95M/vd7tXn/64f727/XBx+Xz25x93d/dvLy5X68fHf12ejPrNyz9+fDe52jD+ny72u/cfPo/n7f3Dh9ef'
    'Px0mOfnddHhPPzid+G+DePdw/+rjyw/j8Mwwfvj45u7Vz5+u/uHjZxtMRjHenA1juPD4vek45rO+u325O0xav5n5J7nDwXaT'
    'S8+nCG/hfoncithuWMFPE3472v/UhAdbPC1ko/2O93nab5/3xO2H3cPpHf/w256cjurw7ZQ5x+uOkzze4OXtwXiHL3Uy3jip'
    '4U7Dd+zWD2dg1wTYym6I2c/4Kp3cQLSe3RCxGY/XS5pv2AkN5qNbbdgJ+labX1e02rgTuhgLP6jzCUdWm7+TRKtN/qSbzdyq'
    'k7XAHHyLmH9NHq6CsYBBfBsJDySZivnQyUT2g2O0buOe2arbuE8/nP+yh7PEcfCgn7Nx3a3hC6nrGb/pcIA2XWN+tH6pcRTs'
    'a65xdKl+F5PZ3bYvTI9xvLy/u9u9/PDzH3YPH97cvfnL6curcsX39x/bl6n/sF493L9b9ml6v7v7LXSbDHmM4BbZEOEJtGq8'
    '3lfzxDHDl3dOZt/2ugmIaZO7ScUYCqvLUYE4cpyv9PQyo7OuX29+vp1cD62A8bCgSceHw7HU6jEMUMaBAP/X+nQN97ZGHZ0w'
    'a9Su026yf2yExOGYgwhiI2RuTQK60tr3mjYIW77TeYOTZKGJuxFRp3vPnQA43eHD07eXu/V3MGv+Ildi4cVsQG79+zRBIbT/'
    'Wu/c9/rf0tVm/u02499uVf+WO7pbnE1TPCslKXa4mII6MgcK3GJ+eyFSSrmqyVu2meski1Tz9ucoaW9boQCIuZWz/1VuaY1o'
    'ZwRykvCgrTrx5I6FKWbeZOy1Xr8hsWkIwfeA3cT7tUSFm44v7cSLLDEgg558gTF8dUYBic3v3ibg0P23UXpltb7KIXzTicGl'
    'LivnCj0/2Xn7d/GgrzziWR8Pehqg9fahKY9rISd6YLo0OdGE6tQwFeBVxxDictazkxxpQoqDlADHGXWsASUX3EEpbhGmu1kM'
    'IB/+9/r24U+qI7wRkNKD88+nrpNqhuHBe6B4dr65q7xDO/xxLAqlzZpm+nscMGPGILkL8qXMZQZzSVGeAIYzI83XP5NvHf80'
    '/QQuHQ2aQNmIRogzWQIzi1Awj/ebLrqdCXz6MitAGIVegk5+9qwVT54Aa8hxzWLbhR64mRjYEQdKx/C/3JYYJgCuPJ9TeErD'
    'bH1yznT3O8sZzzyNyB5fMVfOvDZ+OQPGWQ1yah6UgsNUABJTr4Kni6QGhpYoNcwwanBj59Q402RI4Sce6JcamE1rhQNL2rxi'
    'QLceIhyui4k1HIzJCXsIVMvRXA2Zv5eftIT2V+2hPfz1dd/QfdM/Yj9bnN4txWVfEYsG5X0MxCZUsQ8bNzJQRzIaQU46M4Jy'
    'gWJXdkaOhmVX8HzTjld7k8ic2GkzEEk/Qza5JLDyMGZQEYU4lwhd/CisOECFa9TE3sr6L3asyXAtgzrYCyoRuh7XNZvD2pqs'
    '3L514OTail3sYCPScNUsc/fkKoxx7+/vPlfM4xD3evL3ivt1d/v2Vb7YPw7c5vX82N9B7oLoJr6YJX7ef3i43f+we3j488Xl'
    'TfxGpmXwfvZnubTNnIU0nr++xEFSDMALY/H1xqMxcw/F0uOVwf+OAxkyILPvLG1tr+rcB7bC1w6z+3DxeWYOZSEme7x1DUC5'
    'C3pX96XNAgcGWAIkTQZLLMwjR4Y+GQjbzPMZdBqlGMl48hmnJ1uwkVq42WbTDes4fJgnUIMsTINTLi8tqFBCR6AArm8Jyzex'
    'pNZq6CDOLmRicAwTGd0sbE0wZmFdrwi7o5iMcVcZfRq9XiEYTwwWOPDkpTo13zii+CjpaD2080OLzmOGTmMlhESTvSvyvXru'
    'Ozu2JipazRxNshLqDEmtlX43Rq2UQ68zcdiuS0w1LoQ2jVa2iXBqepzDF7woRNaAz6+exW+MUVrLlvnjgSc/CVHAzaOYOXXu'
    'NMwB+KNtI3vxqAcI6E7DsOm3Kvy4zNIa+bT5G2I3d2TA2LoMkiwsCG7sutrRBO6LOC4qMsBiSaQY5lkXkOcWWnDufYb0pMjQ'
    'cuboWfblzCNchny4A+60TyH5auLe7Li7jVlOXWwK0GzzwCPGk0O8cmTQwqoj7WSH3Euw6hNPyWejacxKYZjGhyMsPOfRQSem'
    'KyqAM6WlJAvYgiwbS1nEBXKrRggUTlGwqPZ/bWkorsmHGLmVEcgJCvtcQV6nJPpZGRYMIf27SvWWXTM4jGIuhVTNebDkjdlY'
    'Quh5LiXGr+vuTHjzp2vD8OnHN3d/BEweeE73GxAJqynbNWekKDwlqUgyQMdi+XTh4YW+KQWtXNR7GrQ+d/KRq3wwu1aD2VVT'
    'MPv0oUYAs4IKLTHs/HKpd+NMqxjHV7mQtZg8nNUoBUB/v5GQTIPNhxwTfFrM7ORMxivVlgq4U3qsRAdcoC7bZSML6Sdq/Kik'
    'QNq2oXhsH1A0JofKFXyS3ppHkWRRKz4W2BF2CcNUpphnzns8WsIys8B6MoLlYMNdiKpafDxN9V6b/UX0DO5yD2MjfE7wSY1B'
    'sojwtbCbwk0WOmupEUL/FnHUXTX0JVYvgsekZeq8lk0aLL0GQfz+5cYwI/ZtlxP86GWmFmmYc+3h79MqzTL+2RhRiaZZ1kOJ'
    '8jboj1d6wIcB7nUm8rPcS5y+BKmRhdihzNEcRkHTmQ3DUZRAWHayL3VWErGwUbL9C6chl1fKOvuDRexKyZzLKleQ83ntWlnp'
    'CD/rsUSBFATKwV4XM4g9qarIgMCTRGvri3E0cByBD0UHRk+rFGFv00+/jC+8DWvh96X9maBAshiMgmwM8elLIZULYtAJAw4A'
    'xKnryj0UHyiWeYSHVNdBqkIi6JPllYCs+GLj5Af4OBLgIzAsaj7Ga71sW9MxQUMMkrqzD3y4yccm4GEghGg8rPC4SZrsGAKO'
    'nrXbIFWUIIrwU67NEu/Z+KEG+0pe0LlKTpBkfLLVtALuKYumvCntzaMEX+7Pw1RYzg9M4PinROVMWBHbDaKRcLMkfbdnreTB'
    'eptnTqz6opQU1Uokow7HAGxCpF5eewj/i47BKl15muJdh027tgHpd2ojBKkLEWLIa6zzmAWhEa8I0UdsmRfAJs4i6oXC5mkx'
    'j1/zyCJVaUJo/pUZCaIPlpsMrEkXhgVv6Yno2yti+4J8elzPFvCfwLz8Yrg+4vOUzkjr75CQJmshHGSCHdtIbnqTLMmwkKzy'
    'WadR04CEZOxHm5mKPtBiuWvx6nSrz06daNVCArp1iegJVat3zoAfPs5Fnuh5Y205Kz7+UK4eIEqlDeAE8FYB9Bkz11UqL7Xh'
    'QpWogHCqcjD0DU3J3uEB78MrnUJ8TVjysliWy6INHKfrBKC+dtBldRh1SKLTg2ddJ9JktGKfu9N//lgl8EcPhtcTPkOQoKRq'
    'rT6iwRTzGTjutvowSPQLnchF7BtjaZkNYeslwl0qaGVR5sw4pwiylQjsFprJm4EnaKK1qnOEGGHMA246rTyuxCq+FHIspNG0'
    'I/aWP2Yihv6maUfoRfbScxG3PZUL28RdoBBASMUL1Q3Pb3SpYmQBkhEA/3N7tfPAUx1ZUx8S2hKL6DC4GP+1V3/yrItaQ7qI'
    '5aoI3lqGUUkNb7WtVO5LiFZvKpMFvcZhoFpzuQioikjYlyRIl/rkiT5gLFscSyQqUJfWlZWJ4EhX0aHzyoTeI9N5aCHdZFbO'
    '7qOA09KCNV2VRRBy3lhs+QYo9VqHlDT9dK18ijSW0UGvlPw1Uz6paaatddNBn5ypoNjwATSE6mQ1pongE0lzKhP8CUssY+7R'
    'YTIZmeZf1rsbM63Mt0f4X7GUfngf+AwDgGfpj9mqKY5UBpWwd4tINt+qcY6wQYgaEr+URyIkKuTJHiomSQPtrluCCivwl1VS'
    'O4BYa0YKYoo0hC92ExOeKq150hEhW0NqszSvxwZ4s+Njmwv60tHdJh/dreJmND3kCrJBXZZe0iS1RonRvUgULHyzWcfW+ysr'
    'AMISKua7198Pkv3NW4BaP/NqVKwPi73t3vCg6ZrttZJ84n9Vm5jSdDb5k8tQaJahogNJch8y/V3Ibanu905WQpB09BmzqHH6'
    'rAAdbS0AEwMDMK3nktyWX8oRqhwWDgBKx+APHLFZoWfmpTwWygBsjw+Ylnt/eRBaGKA1VXD7LPTozCNpyuCG04XR6FQE0hBa'
    'F2NcwEyAoqDJ/HJIrofNZOWzYhVKQngQBoMkyT3dYPngp7HHU9jH+CmKezENbD5Hem6Sa11KcglZo45qbeu4jr9NjG0aaM1d'
    '/sU6ULpl930K62mN7iya6JN4ijMnGaOua7i9VyHfJ43EqgGoTTsWuNM6Cr57y/RjVHLrpx/mSc/laqlJNJJqxdKp4w4zRVda'
    'NC2IYK5rvCuaGqsA4MR6rvGmSBBmmWxGEKQ3JBWvHzPK17S8Nl6RxDCk8lRXV2Q5ziaKX1VtEO2mUlmrvWe/VqQ6h74UiYXl'
    '1uCNFNaLr+ttnXL+OP8dHaEoDowAtchkgPBZAE5CuQGx4KJnGMCN9+L3muNYLtkhpj3yHDw43ubcCAKqVZXiRA6hNYVypmG2'
    'ZlqkTrYBmW3xhIyam2AQdp8Vp3dlXkgGWVwyuaN6kBQ6O0cOiDg2dFl2MgjanifqUGt8hnQSmxXwsaT4rnvOKWtKWr7UMTvl'
    '6SkFTznVQgrNGSgk02wNz6GzdIqfiOub5knnwmhL04EtJAl06dJH7EgCjwgrdqFlSokkFobzyfAS5YTU2rhx2WyiXbiCNPOr'
    'qcwDG1tGmVDBpgNCYBtDmqHUHCypEJXdLnqiT1ZGkWazhCK7tAlywTx4eHtMhSsmRisNBN9IQdwCjYFlvm2D4FkD2bK5tVW+'
    '4O7zGbFa9808NpfXrQU1buk321Yh8e1jl6zlOix8W1pJnMbCJ00Dj0OfboQrZ3rT72yWS4paVMJ6S4EBbTlpc26PiNxAtE0i'
    'AarZPrLUALqxQ1UImR3W0DkNyXiGb86jwOHPy2dtqWIyBSriUq6Oqs+hD4TwJoGkvHzqEUe9IPY43Q3Tn4kbIjNeUgtmK2uA'
    'X09UvkznVT7mXMDEP1GlvX2D0P8mUd2HKX+MMXm68vDvrZV+pE91DUGrol8ELMy1QEgwiB3gCXSx8J5APU2YKfszwkmwoDJb'
    'GioQjWUAiIJPMZvUxtblgAuCcpBnNF1D86tc0yxlWWLZOjDKsMPwJnku0oGxZsPJ1K81EuNShLbxlcwytpFbRkT4CBKxkkjU'
    'PbW+T0r/QKS6dEngtlO6fP01psv5JwhDL5MSd+LKOM/cOztq3r7ZhsIThAvNabVAKpy5VTSB2ift7dLm3H5TlBp7hjR30P1D'
    'i48qeW3tvUR7+kRxcac0NunB48gtJ1KYwCNX6tXwCMLOPbuGFsy0onJHkya0jCjlCjKmu9arrGCt5HudYCrcQ52ynyH+Q6sr'
    'K2ta0V1H48UZssq+k/oug7Gg17xq7dDnvo4djyCS5IdWOP5ciyI9Q6vV6ON1JkKr+SBGJxJzZhtpLsJejNknPJ/M1HtEKSNv'
    'qQ6V32JmHDbfkJQZtzqW0+Y7N52gXzhBBCrBMxY8qS0dkiNMpInnsTC9wK63YHE9a1/L/VpN4pMGTp2ywV4Z6nPnvtfnYKqX'
    'S1AX5KfL7a1zid84l1lOXrfVvMYp4LWUJm7tEV2qAU1G8hT9iqbeu1R35/bHjdtci3URnVPQrB8xhYIop3Kh9uYS4SBQpSSv'
    'UCo2slDVsdkxKEmpSHX4zvGZcty8rgOkteXIzEuP9G0cxGoewYPJEgfMY3XzlZ2mAYIUcsbykgwv+mMM4MUXBewfJmOGtqXN'
    'ijg0BoFm0avviNyVVyzzEOiegeynNqm69hU6HE7ND2o9PWnXdk2adMlxLJnkNp/oi4tITT7B75hVCwxdvfU2tWnILSoMluV9'
    'KdrPapRQm7tMkHgoK17HsrFwB8ONlmg6JvpJuSl58YxdgCjepjKRsqJVfue0ZuvBQ1Uq4w9qu3J7LiFswRo4EeXk4UNt40xh'
    'iu1iqsnxgTf90HzqpLkTp1bIEvqVuoN/8yfiEvnFIByYzxaVB7LFaQ1oAclu2aecxN/0ldky4kzzF7hXs5wM8s5cqGM6Y22c'
    'cqtBYQimS5wPpskmsYJ1oBX6md4sTZCN1AgK5+0j/MlFojo1+2ZBNNW/S7GSyrz1JtE6KauKo+L8svQtGgHad5oSAZ0z+FYJ'
    'cmrSz5PQbhgyw0XReAtnaCCuFnLo1PK4jmGxnuC8YpxFvsEvkyv0OQw+4QsXOn1biF2PhOPjga6c30U8rAu+QV1ry4AQfSFF'
    '2gr4r4wgpzgLWwEDDSlubgUC5590aXZEMukR5lEMWwE8F60dtiBRzlCAqW2fdDXHe8GK0n4AqXm4naHd4oRVdg0t+8QVM0qw'
    '/krqISGKqIs6FhRedHlIodd0Azyupd52seZGlhnEcKCnb1K6qAwBkiF720aH3q6bmUnTq62uwabsIVPhVRadQ1tzfWawy+ew'
    '8GKca5XhQ8lR5ooS9rcqmKP8piHiDiKJKygB2jTTwKrkKKJUKTTA7lNXVpmJ3cWWXOQwWwEQFFea19vo1RE6xpLi5VQomAB1'
    'Y6GYVx+wjpWF2U0Wy55zgdV9l27F28SG87gFERAJvefTS+hsaEkttCX8DbwizvfZKYKTFIfKard2bVHAdjBF1FjJAls6C38s'
    'p/UPu04AEhwXDvV+EgeRoiyKlllS5SRF0dVoWe3YiY5IrsSPCKjQCjAWlWhFsfxBJN2KBQ0dvf4rWqHT38Xv7VrbU/RWDupl'
    '7A5wp1ju16kXEjIhI4ovQiRhF7zyqOByokQTAAmxFphbXB5tnr1Whg6wzKrh2ZlCzR0zZyH4UdDACWBUjTMlSEaHg5+bqEdl'
    'r+fwSxyvEIhKfp3CkbaGVK9QD2iyRO+Asyah41pWzCksmsWjvAeagG4yMJbRSCKrQfhvtrS0qCwro376aqnZie1jn16YXsnh'
    'lVvqWGSxHQPxZ2dhsK2/OIOtXKW3DjMMySq4jl11aDmlxgoT/tStpY6FO7iUAFeHx2pCC7TYARqooiwM3Tade+yAHRDyPrSB'
    'tvQKQY6M3QaqOZVe6rVlDwQVIWrFTRohkkoUzIhl0LJyA+9IAAf/P7En0mVLMmuJNK8PIZnUJhajUTaZmDgQfIPyB/TtjR5r'
    'R0JYsrwHOGga5FJXi1irN2Jty09gVJpclqmhZa1RPBk9gkQsKCWpTLqENogtcTKKOPawyEk/jimtnxFh0mYeyT2BH58SAw6r'
    '9qRqAG2iCYDNLomN5kBnJ0XVSEJWWPdysxA2xPpxd3f/tpDvgQc8q2a3FR6hnlMU54Zh6k0cUtjyMvj6tV+bt+3Ff3L/F459'
    's7KrtE4zAIUa7QgqALCLmv53veuUy49KgnBmPwBNJLafKIHcLE2dY7klPNxhJorjQrCoeKmaqFve+2FDErV9mV3Oai3C6dp8'
    'nfDPKsFy8ZlLrDtTL5rWVSd0SNCX9v/z1dK4aD0cMUuex5XYRn14XVJVnOKrpllcqTKExy7IFZij4+yy+ie4bn7avuu286la'
    'HkNE65zr15rVirI2j01dqJNFpJS9RMPcGn0tw2mifaqZhK8HgaiyyQ28pqvHtsbXUOYNxpJU74l0guqzS58LFRZaM2pZ5TvN'
    'gYrX8SaxT6V1VEGWeHV9uIQvIJzNzWOi0RPn3ESFqfSTy6gLmYXVnt0N3YLjUyR+8Go0Ou28kyghUl5GAGFLjRKCIvTEGc5K'
    'mwLSRxwton7kUhtyuJNUCTj2LNiHrItqmre3w3ovpu5IHQ4/eaE/KApzhZ/Afjolmi/DY2h6cwZ13qRlzWTEEf4IJzC8VWdz'
    'E4oVupX/6k2+dGYUeaNCFbnUoydR3LTzSWsm6YJndvyVBEFuXcLl4N6Q3lguOU2bQgihtXyrt8Nj7VC/nimpjc2zDrjh1VlQ'
    'ws4yZx7A2l3+TCOHldHBJuQPaJ5RQMgHuLKVf01MMVv8F3SSqlcoNm0HIooe8hDaxpnrMBhKmjGUIKvkXmKHBQ6IxWuwfUlp'
    'ZIZpoDHFEEMw9p8Ch56VUMmhKyOO0S3IHkqZk+dNodzdV25HFbhBQNRVExeKq3zjdQeP0as3/+l5klxcBsxNj3VIMa+uJ23X'
    'OKGQGKWbM6ROtS+01kaxbv/KK/C4/uz5S/AhNUChwpNlra69cQXUmGCLiMFXlzbmzPzHJQpnhg8kn2dVlI92gCE2F14WmAvH'
    'OEEjC6biMz6Ya7wSQs1RQdGe4VOiFhUjhp1XOx0wsyrMVEv2Kyj0b+PQ2Xq7AQoFFgQIoOHTqNaS7kSY6UULU40ptUVE+L79'
    '9mKv8ng8hi/ykQBpfB6+xVoGPH+RxbQsy5B6wcST2qGV1VpV22J8s+WUt7p1DSTdxiDosHX/c9VK21rzToVnVdeyxVBp2tb6'
    'q9CkImE+6yjVhZbVNpVNRW95nys1oN2BlL3ch4UFcSCqkqV1JqQiaVy1t1lXi/T6YywfWpkoKIAvr6yVaqUos3bIDg6qztJK'
    '37JqltYrfZ9rrU6bOTM+oDrfVRvNjAGtUWwnafELG3XdxE1KNKlGNEdJgSOpkFYj1Gk1C+zBTHUDxKvLUHGl57tKostJaznF'
    'JigEPDj2YqsHab/Ge5CFE5HFc+yYCvypRr1OGZrFNtmQHTYTxcGBVgydGbNA4lBdPcuQBZ2JMVCSn0Fa0oL8ss4a9BgXvMLW'
    'K2AKkMhama2OIkU7rsCgoX9q0/TimYKorJaUaeZUS7nKV4VRczwDBTW48N0kCe4ri1To+rCVXsOEdp6UHttHkHIipTX/Ew8P'
    'YrA5rDOIttnp7+yyktyjJMRmqEftfXZzOQdQXx7ApNYIYleFEDdc99X1n2KCh/Y9lOs1vlXbAcnrL1cRuokb+pS7dh7NWOhs'
    'aKhQzcWkDc0xy+QwCV9MFwsuxwoDwKDFdfKsMKVkv0YMYvFsAz1MyB7WaGLShggGl2iMlPGhW7FkTp4wgSpzK/vsDZofDljc'
    'JDKT66QSstWS/Dsp9gySlhQUcBGW1IAZ6Ml3OHV18TINm0nX6aXK4GDMdn+HnCDWkolscX2boErMnUgiiwUKj0ZlQlRiaSBB'
    'YK6F8tLgKEtUJ+iEOVt/4EKDuV2W8689fEJusmYCDLTEiRmhErqdyCszO2qvUkZ3UbVPDxVxevDEUag6B33ksiz1Xo+VmYOE'
    'aHboKGSkFt6aWq+qCiuR8hp4VCFxv4t7Lja3TUTjoyQwxlWL2TkEKXghSOCJUB3ls8mqp+C3hWldl1tbhvtNjhWSCnKdWIe2'
    '/WI/fXaRD22J2QW2mJ2HLDi/95Xy2Eu8NmyMGW0N2LHpCkpt10zS0uEIdebHOSDOl0Oozq9Z1pv89k0Kla1CvtU3pUOWnokP'
    'IiylOibR3erzWIbtxioiGdWNC/4k6DhLbSsGiUrvTirNpbfe25KjvyQwxlsf0gWy9JMYcmJz2+g8N1ZtGcePYUm2XBAaivep'
    'TSG3AvmLr4vUb1UkeaXRnbQ+XKT0JOj7kTVhfC6nD0NXUTFCZEMyhKGUfVl9K/X9HLQVtqMNJSVpjTGGWkagLtXVg1GdEtCi'
    'nG8hhCkJBavpi7FCRPb6YTwsbXOxb5U6F+KG0gLVxCYH0h1E2CoXsVK7HpL6gCYSgCbjMXZaAC5j2ViSLkpL+vZxH6rUU84y'
    'L7TPJn+GaZEJrTvpIfwWdt6hrDFNW5ZRlArrEGjr0QEPR374dqGzDelUm5giFpZ6CnRA+DbTVVkAlJxpF6k2OrENL2ttAOQO'
    'CcAUcqPIY3h648Blq66o3AuDjiGN/0tY99GIzN18Pa0DLFWuVSZsfRaZsLKcfEdeGORSZXA4qHDWGZMrYCRDZXqHSlOlZrNR'
    'U4w4Xml5fy3b2FtjjD0PonpW23AZayxIXrNNQpG1VJDV1KEShmocJgvqzBLi2iWpbHiyWCJGLqQCwikhZy8lnZbQUDlMxQ5g'
    'WDQmKc0FuNvWg2A+LDoOlAOlyuSIwVIT+abBciSKEpQFoPrgIfual7IDaHDUXbYG8DCL7wlG1bgClErLqZFhG9ddSiM6x7by'
    'H1dyZFPbaoZvE7PTYPMAf6J7nY1dD7O51kTUwXSfIrVQ0WbWuaJKcou5eHoDWMI+T8anYbHM+lkcBwRuRUJ0e1/l7cEIP2Tr'
    '7JPK9rYDp6XoZPpFtquEbW1cvq2rLmRrGCEDzp4ARNgtT8a0eIRhpgT2gI4mi5Si4kE7v5QUXFnozpu4C9lsY47kMJf46AVv'
    'p3HJjy/KTpO3UxIF8lNI2EnHWKucfwJbbJVqypscjvR9cNLyuE5zrWNnQllyjItiVEqJD03vnEHsXmkSVh9jIZK1thr1D+aD'
    'ZyXtGbmsc6FOrLCOql5lBPmlOkUrTe1QVag2mVgn2gDH5IhWhIpASX/AOc7tWR6f+RtYa6upqMEV+TTWdDxzoBfoUY2zLNZo'
    'ZC3s/g1DNBnYkEQ/Sq0rOctUZEdGtXClDYGMg4q2AnQ5OkQoIyK7KfaSLnSEKNKtwBt71JAeZNYIQ1NbgmlFuh0MjSYRwKBq'
    'YWlmJwNMUC5OErE/rrPP5tzYj1AG1URNLcDm2GdU7ExmeE6oVraSIlREVTI0dX69j0EZqshXmBLIU9WElxjGOWU+uYMfawsQ'
    'FC6C6XF8SugPvr6msMqpfJPI1cGCZAEgZvCUCA3VaVeA8MR/U/a0KdP+yhV0uxSxP8tj2jbBL3bTJlpwMS1Zc8iJIIUFHCXQ'
    'QQTUjiZbtEVqnAWphEYEjm9YmnWzou++Eptk2nyEGzJnWVSEVOy0KrW5D992qlxyIlDNmBffjDioPRKFXIMnw43VaSiBwK3e'
    'qpdp+oTsYfrO6oGVcNy2/NZjHeVtypC4zbzSTuJLBakqkZXM6eV6Jsrza0FIBZJItFVhlNsFtyB5SLtMKQ0SU10/p0rHhR1+'
    'WswbtvpedypOrXvTK1lnxDZjKrkuo1Eb27d+fZtYfPzX4/8DE4YIVw=='
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
