"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vG1mS/C8682CSsmzvTW1zpoVRW4YsLzHbEBoNzCwWWMweeve22P++skSyipWRkZH5XlGyxzdaJqve98uMjIz89X/P'
    '/v33P/7x9z/O/uXXs0+Xnz+f3S/O/uP3//rbfz/84eHjP37/4z///j8Pn389+/nqdvPwv/TDT1/++tvlx6tfLq/PFmfvb7Zn'
    'i6X58+efN5tPZ4vz/X983mw+PPx5+/Pm8u5s8Xry51821zcfR3/+dHvz4cv7u/EP7v9vcdSLq/d/+fJp9P5Df349224+3z02'
    '9PBh1+fRzw7tG3ffe8euEcdv+Xhze/fz40OHT/Y9u5/S9+yaqT77py9X1x9+e/jn3ZevE0IePPmm3vrry/ebwyDRIdp98+ss'
    'HD3/4T8+3h1m1nnPn8aLgr3m+ItHc315t7n1nv/+Mhigpy/gcdn3YP/S0XN3X2LjMtlk6HFD0wtTa18wPA4se31C7XMPT/MH'
    'RJ5I+/jPN192Aw7GI5xAf5yHhWeHozJ/o9b549A0f4dTy45Dy/wpA9Iwf9K4VOZx/1swHE8dqD1uWG/TP9WeZ4e3y2pg3W9a'
    'DfuHbC47LgJlNDqvgacPicchOye8DsKV9v7m+nrz/u63P21u766ur/7tsZn2Pknd/oVrCzWDPGB/y6UaCt4aNjQYnWSz93u3'
    '5wRVNn/9wPjxkx8/eUE/OT4TP2+uv7puo53y5JFhD9D4aBf3Kf/pYIXEJ49v/ls/a1E7yow/dDw0sMPL++RZM+lHy+0wXIqV'
    'hoLzH7ZdaaF/l+A2xj83wxQe8nv7oPMwgcHHo1Rp4NTeTy2CkddUeLUd4EIThgE2LZDHF0ybM8BhA5lnWThKzRAVnnEYIftb'
    'dYTAQ/EAlW+Lf5bfVq+6ozvvGMVcTv78+e72cvvT5vb2r2eLdfEynHzofin2uh6f56JsvTL37uloplp7IrliCwBUlq9U/d6w'
    'jbPHGh6RZrdqev023RPA76MXcY8OGNgzO0JgEhHWGfuSioU0LI/S84aGufh3JzPTMz00I8TaCxNMsOmytQeHC0AVGzkB3Vqu'
    'vh8P6fOQNrugyeMlZ+I0XPrj7u/lLrc1PukRFtts/Oeii+Y40l9X7+XtvxYuMDCY5Joogw4JEwc8FATSKk7y1MWWmrM74LXl'
    '/ByToLvch9ZJHR++jT1wG/3Ox/CabAfinh9uZWVCdI/chkPlWZJCYZU+f/9X9/7kfvNoDNfcfIfcpHv/5210pbqnNL3+Vxnj'
    'oAFyQDZC7ILF7mlsKbUbHM9tISAH8wTmAiGH+XZDfGp7hLC+o+yvRHW040PYYwNE46z2wdoKw315uJKePrRtoulje8A6Dipy'
    'AqQ74YqzmECLK66iaC3XIutmfUwVuOTED2kK0xji0Ylm4DlBhXUeVFCMdfCal2UcjB2SU9gFzN0I/Ukfh+gCouTvv0T4gUFA'
    'DNfoNfDA8+wOgLSQTlBso24G6BGkEwz9tjLuzJBJ2B72MXghhA/6cHvzKVgHxL4aPMmbm+vdSQ1O8PXe/Xu4eD6cxbadRRvQ'
    'q4kbuuoZhN4/MXNw6DYp90IPzzksNv3JxGkZHmtgsYlRkOBle94MSDZJLFDlqrQxo4IrgHN7xBB4CX153DNLummUFLMUQLMq'
    'oiCPP17jlajFUeQIzprs0nc6o7I17rOAISo5xNOC3yQ/zQr0oPeqPl2XluogEUhv882PuWxKYP45o+N0wx75ldU1PfzpCCww'
    '3aLFUAuW1/FlgQ6VHPum5mcQr8WbM7aeOpOM969CUyOvna6EUwSe2ld6E9XknYD1HLwPruiNah8AGpVZs2AJ+MZzwuRRWMgA'
    'nIvwRuZe1HFYEmHVzjs0jB34VPZInBiHeGHYqL/GHtQyp5z7VKCUSa4EgXDtgyezw8JJ+tKFKbVHuwY99mBwf7j68+RLhTfG'
    'hD9k46OvtwShwb4AbxevkUqEmIG8i9kC02726bzEs3EEe3BkerpNC+yq9Iwpc4fK4BHEgOUKImOHauU6VCvd5pVcmeG+tmPU'
    'klLrvG58fh8GVrf4V/cd0nNV9ynjSCopZNgFsibULA5QiCMvGA0IWVi1RcH9HdNKyGeaeXEIXo8x6gTamkR6sGbj1CzqFD0Y'
    'bj1nFDL5eQplFZjGrjece1cwi461dbSkFdocsP+ByTq8zYy96zvHi4fFJ0Ib8jAZLKE08UK0hcNzNlxEwLXzTwPq4WaSQslJ'
    '5bMfXazjMBzKeqqeTmD0ESekB1NzekMvAkJsi4nMVHgYItRgHuPgnGIYT63ai/s8zwOIDPW1/p/J6F++Gln9v1xd/+Xr8Bg/'
    '4E1rHKXJxF85FhA38Zl/EFn7AoAu2euYQpIxVQVWgGQe5+zl7lwC1EZ701XatM7akQi5im7GDiSXAlkkcgLjE7zCKZksW3Ka'
    '1yHQPAdFsO7ZuPRyQqgNOSzownJpiHKApRE6DCDKUUmHJVTwMDQWY/hmy7jkkHDRNvXy8A5gupH12GGjsCFATkW0BM08dEqP'
    '595xsAQNeyspbGMjECCXTgzONsG1xJ0cr842/UfzYfxo5g/1y5mCy34G9jx5/0TrZqbksEWgfzPfa+eOMczyIkbRunCiCwOl'
    'sbOLMdsgdGGUHQuRv+ngIIEzT3eQbOwWhFTYl7oQ9x0RLO2NQeN9SnlrnoA9irauHUI4CFnrv8ihq+FYtmvWe/MT2B2jsLEr'
    '1jayGsNDc1OO3VS5O4iFiV1u8w5BAhMV1bdI80iRW5sXFvPLe5qgAwLqbrsDLEwnVQcQrCoYs2oB2C0BWg/150nxgpnwaqDZ'
    'H1g84ckAzGDUWTo/k5GoaDPDPgHCNTKffTfVYTplXInJJBPlSLxZCPFmWDi7XBTo+Dh5Tps4NWVnplx41ovPjXjrciMUsiSQ'
    'd3coOSIhS2bEsum3URVQ6yBmCkImScL/h/ilFz2EkIniHCf9c7LKwdtCmEqGBcGBedgKPtCAuxQt+/GMXbjr+90J1jcJJU6+'
    'CQaKXfjiSDWu1ujo5ZaOS7oY/9/TIuCzWzmoBWDa5zEH/QrgMg2aSCoGNi5E7d6ixZPYJShLEqwErJKvSZkFejheCHiQ7VN9'
    'ZYr2QiHanO5GQp+y3yJTuhHOWOYS0Nn9lKjsL7cE4+AUMN4TN6BHQuUpcTsNyesJvokEZAi+UWhES/w8byCZ8msph9s0Qmmo'
    'KRkwLduymUmqYW4ngA4YJoBusHKfCI42A0WiO76kpHUpNIoydiewEt151x3UYR0cufEvgJ5PCfOxeGg5g4etWzu3uWWL9hpY'
    'V0VF1ZAELE3xItioTSKtMMXMTBw38onwRoXTzGY33kci1hFvd9uw4df73DubGEA59uTeqo1QiGrldgPjv7QJ90SogCfZgtdZ'
    'k/gPip9KC97iEAWZaUzOXQnsLwpLJwIsbt3TYrp1Posy5HREBKY+bOsk48Nq51Tu3rndnmDVPWOzKvnQJxiaFi3oV9+Yc0zZ'
    'LSl1SEzdB3E+JP7InWP72/FRuXL/Z6k7z2/vFeFKQqXnDocdBpfD0isjIMmOFdg1J08TUAi2z+Xuo4kEsTjNHOBR8j7sYWXt'
    'JlwiaKodfne8EbUQEtxx1XxkL7+u7HKmZVDhAEHCriSoEo8fERH3amIk2Lzc/u8n9bIlNAU6YvbrCRkUEL4kzEJ9iDDvIlO0'
    '1l93W/pgIYmHrIpM0Tiy7jA5C/hP3DPvKyZEdgXm/GXlSmtFaKxbylFfopW1IbyVzJnHI6iGckVn89gKca8JhZI0NvHeCVFf'
    '5vo5c+vbSdp9UhJIQ7Q04ir7701vGRK5VGKSMm2BTLyyYxoS5XLhb5HPzAhElbYl/NUF5zyGM26Fq4vus98Ilo3/mBhybvLP'
    '1/cNvvdq/Lxd6snqm0steeZ0+a0j25FOm29TOFI/nT7Q3CYkfNrAG4EiekeLW6NuasWNhlWWggySlhIT0qpA8zDlBF43sy4z'
    'JpPKOtiwyEhoqyN5uE3vCLkyjB9aQxzEXGseVbSuScU0Za5OgvyaibWCVnh9gavSfqfhlOap5+gsrgVZc4k+dIEQyj9NAiio'
    'q6lrkVrVzJbmgdFcoj5FwwmpYb7seWuPWE+wc0k2lsBWSwHrImN2qgje6Xm1L4rJO87HNwktxz7V+gW5TVoifgf/CXjYDdn0'
    'fsyyT/Ee9/HA2AnSABOAuVCQZQvCQzJV67nqtdhGMx5Xm4O1bi/oW0xy38YZ0zX2JddSTv5vaWeMM8yjYOQiG9FPDJKyQVgW'
    'p2JFn0L2zO6M2PkishBB9qXWZlTuxcPx/UgDiC/qSq4ZRw4x9zY6lXEGi51vSaZU0n8oeEUPfz8gb+JkZXtimItFadjk1Qke'
    'TLYn3LPgm2TvCKommpuI/TIFOPHsAeAyvo3N0ZTMH6ILe2pFKR+BEZz9jQAiWrmpqzuUiDgs7wwbHuR81WojiTRQFMFsyn6V'
    'hqstU/d01Wbm8kXffR98WVvyZqmrn1R4tXGMb11KOnV4tOncU40+20P4rMGLpqFAx2uey0GVZZGB55Rl+IJg2xxOdSpriwct'
    '846OQryQ7ttSmmDDqCZ3Tqa0BzS2gsXQspnsAsBhXkpPxZZMDxk3rjsjueuZMIHMSwx4pIeBhiaz/WOR9qpQDoOcdwBeZEAe'
    'pvNGQoBUtgscgo0ALJIgUqWrhMqVxSLslBOMdeFQY9pXNR0oGrEu8Sq16l14AA4iMbx8EUumezJqn2hnwBO9cP4umAMUKLKp'
    'ndRopP53Lol3E06WCm21FNlKSU24cZCmFHUq9XNYWYRX7DllhED5FhAo8QJbJbSKrJtsYyFNjrFd3BLNVWCOzeWrjqOky3Mb'
    'Jj0qpTSam28qcpqXMB97mjVXNxWO7cNnhR7u2v2fUCMd/uq1UFW2YGtEbnrqkPNvuKK+eCIknGCPCc7/Swgca2WueNyT9aZS'
    'QageYE6IU+oprlowjiezpb1BZhCOed8RYB7Q9KJQXucaXlK5eY1VzLLgePwlobkiVZ8WYh3UOUDxQ+zgVFCFVqJ+lGRNiymw'
    '80DISKtBAI5Grxwtx2vS3WiM4FBRoZFS9tAOzdZ4SBx1rVgMRXrFZOOwJkFbxTREnzMToIT1swoDkbh0nMnMhMeaQv9avjo7'
    'iQsLCgDeeHDBdaWzBChLqhtJRKhmHHMIENqknEe62FNUStbuFrBYRIZ6jrGBhHgANz29yJjQFtn+gmQGE1/cKtWg3VhRMEuS'
    'dlgsmbafPZmKGNYwaS+eTTAeQLlS6CRC/ZJT1uMeaqBEp3RWmpuohD8ib6ulqBLepxD4MycS7Dv3jiKQx/VNvuUifydAt1rU'
    'w+Wsg06ptNlq1Z4fU8yoVQSgAudlu3k+0WQgKCSQ+7ZiwL5OIA3wjdDc7aFM3UVHQJdsQkuprWIc4P26xhxlOJGE3VMt0C2l'
    'HFDXuYGoI0UZhYUp0dgTPDJGR2AnjMgy61uVO5Jgil09CrBVBovZ8T7Qx6u9l0gkKr+GchIKqgyKPwjeGU4VuTRgB2MghC31'
    'QAKS0XBmGjNiZySWuTpUmgyZNU95zg2G5q1jMPItO/jqEduVHKETLCS9L1ljZFqZbzexoSuiN6zFVGLO1zZXRPGKY8gyDGSZ'
    '8wwRzDYGIg8KXYN/vyeZY2UpNO++hyz4RT8ndm6Vb1a83hAxKqrZkFDdwhPbbvoQJhrFq7I4cXd6h73qc9LdhHBapG+sO3lA'
    'oEOypHcutlChdRRzQSNEVMy6LMUJs2r6OE9AcaB5sZ+uCvuOWjDL/M3lo7ek9ed19/M8f2B4x7XT52BhMfgETJwqWDWTEj/3'
    'BFICicnYXxdlRbzsBZ+enyalslKMJ09lsC1qyYKLoRhqOxZH1dxTauRlsk2FK8SmT1AoF5I9mgELBKRouvNon0k1lY7VBxYN'
    'OB5fxPFRQYkaxBdrHWsoSiCcB4jr3NSyQGrCeumMhCsOWMN8KwrbrERGKMydEiuntd2U6nHtKMRcyodwKpXC7gVuAIAUljWl'
    '8ydVc0/A7yjvrK1q9zeRhjJLRN4X1Cvln9CTzc3icJJKchHsOcqDK9BMSrhhRp4AwEDSnFmpuc+pBE/LkmbFIICpxH4xG+1A'
    'l5hDc7YvxUsxC54n385OgFm6QpKJnk5DsuyRC7sfFSXRtyheKGWlOJiq4rQwxYj6HDYpIHJiBKuwpdWgr6Vlhz4iGeR8kNkX'
    'tgvEhkIWAZULzFWKw2FKIa0An5TF8u/0SApPPaIHycGt/d6PHWmqkiOMVi5ji+bHkQy19tEH8jnEbAj0cvK5jRXRzso9SU5k'
    'cjbRwrXbzBZgiJE2eBsFxhWLywlpOFUdVWn+dbOGZtUE/KXavAShziJ3DJjP0kgp93tmegR0OqzXSmNqUrgjNQnsLk1ta1oT'
    'pAHizmnnSjcsJ5zSTA1WWtCCUEJqypsCaBP7k+HesbyqnG5nfMXnlEH756Q8gWyKzkpdVvRIpOWI8POqH73nZaSmNIq3nF+c'
    'KL+lSzENDp29Lmq1zBEPzVffYJ4SC3BXKjRbvmSiQrh2debLPvRIHtCdeeI0DoxNpUJ2xFqh35xVxUXPhoyDyhmXWS2sLYke'
    'Dif75vrmI0gZ3SrkvsCQS3OfNIOrq8QLyaeOtyjUNqSVJip8gtS8SZowwD+3eBzTBFDcQcfsLlDzzjuh+ojH1Cq/BP40xDvN'
    'CIK1QQy33RwvhZqx7CqLwcIQboRKvv5JFYu3JYq5+Jezd0lC5mwMhkymRC6k6G1FrUKNr2JJAoYiksGOot49crAMItYGOkGX'
    'owJ2NNQ/yokdKTm8MZHoMPm5lco53krOSzjVEb9fW22SqUe1XeWkzqA/05Zwup0HTfNk1yDom5TIiz0QsGKT5FH4dWaFkfZi'
    'Y7C+QIXkMaC3S65cyCf3QyuB9BL3RDMS9kx5OVGdm11/cs0AC+pt84HS4J4m2j4iMJ9DKlPn4X6pre4TpbMHg8Env+lRe3gK'
    '+SAiPwZtIl6iX5zXZ7sf5iYefUFQHkKwOeihPSpW982K1FwHfLDNFxDj/o7YgV21qZ3Ex6G6E6zeMF8VppVa61Cxj2A7OTzX'
    'i9bXBw3RSzbxb8a0vk7lnBhjjRdwolKepP0EZCxvklZJGdpTGPVLyEDjbz+SX15AxShBpzfOPmE4aUN9KW51JVIH+YNqhZNK'
    'edJBQzaSjjSL2BRlobivpnRo+Pae1sVcCRdmCByWZr3rwJvBQ8utripBUsqPVnVPfNat5R3jlWQOpNBN+enL1fWH3x7spLsv'
    'PklNTGojHUA6Du0HDspyur58v9nZUmldL+vCgA7s50LLc5xYzwaS2b2SnTzkHoaB8QAYJrMUMdcnZWgCK3cZWSk8MRr9L4ee'
    'KhXgl4mwQuDSR0UCxIpoCW2oROINPB0P6z0KBQHIZ78NiMVk8gKCrh15nq9iwxeuC7+MH3bkyVUQFxuclUeA19ZhzkDeYyTN'
    'ly11zit/LUFlqhwZlBrinuwW1zPrUjQsAAijOhUWHLLt9FreJynVZpvqaUAceUt2oFZCLo1Trc89VOobJ9810eTW/ZNOU4hH'
    'I+eNY0Zx4oSPL3UqNUbkg5KgUhc5mAJBjRUUiyhnBfWdOt9ML0qtS2P7SSkph4+VIA1rvgs6FaVdxE1mRe1KglvaNhIYMD8k'
    'GVRgIXlo3dKkmResS5gr1Xka5LnklE0pmylRIbWturKGiGZLt3jeQK4hlWKTQT0kSTs2U+OHZB0GDSAVuyrrD4xffgHmsw/Z'
    'KkhUE+RpwXQdsixPgmVUbvqnwy7SfUvg7bSsmZzedOQcLkvkI3w5Chruouub216IzGVUnehNRVzBhvmXz3isRyVXiQR8i2BM'
    'yyuYyTkpzidQNg8rW/kLMqsprcl1l9ZgyrUE7ThF4XJP6/qfIPNtJgf9ddVBh0+7UMtzx3T5k5Z5YkYe+Usnx98aV2JRKIlE'
    'QBn9fFi+mcJSauHOiBY4Ty0qNNz63UhxBPQ1E6c9XfUqOuR561y1iBmHOuHzRnQCRaaNhuBDVqrEZ69SCIpbMpUkibkRG5dd'
    'EBnk4PAKw/kBN7VPhWQAxCaGiQYU29lGgK4gQAtbSf49Wf6ZUJe61h6WfPwCq1+vqGEQwgrGG4bF6fmi5GzJ+8yui5qIFZVU'
    'sUQwCn4aSgxNZhOoQ/k1aKdMWIJy+egUa4vaePxeKXmICdn2LUj9SYn74+C7WDhdPV8W9fAROSloSi9YuYi9An5AjhVftH2q'
    'ElOeZAXEV+IumtHGjqPiKWTTByyAAjDWUcJw8kiNilai/CpFQmJH71tUr0wAgAnALYmE2TSsaBvrOBWTlxcIYRa1Y+cpyZFi'
    'yrzTLxVhN0YHC0aWSl1R58gD9lLU3py6l66vFTyIHYSc4ZfHHUHi2ZMM1/eCPDZV0PPhxXWxoh5N/e2VQCZmg3kEIFEmau6M'
    'MeoRaEYjk//qCZNIVe/ptzX1ohMnjGACU5RLFc2lyNdO5ImwxRBd+5LmFdWETgM1WsE9jjkSzsFCK7TVVmmPa3crn6Oi1QV+'
    'VLggfYs+o+i1FTJCtDMmHV0A5h5TyQkRt00PZVxJzSnWV1brGDLx3ZaERbSRWFpEZKiKuQItrD/0yV/JoYpyVqla5vuJPmaY'
    'jNg712Saah07aSFUNGT1aHU6XXHqQMwj51sqmCcAKDOcsCATZmw8v7tPKOpL+FqNXQmR2ImHVizxjtI1jWANBXn5bk01K9CM'
    'lxqmiHF5dV6Soipo3Rng4zBPNgWP2kFMDPNJnnrpVXAD8tTnbmZXotiCKGdjBwUwvcg0kZ7zphcLDUrtZdhwT4LV0eTZZKr9'
    'DWAz8p4K+j0L9jGzunijhPi5J9anMK3W5YpEvXlUoqwOLbrW1FiJfSHypsRWuhf8KQlRLIVKUzFXKVGi+bfUlXa2gkiLTomK'
    'ayxGCEpf+hNn5Oh5sIwVI0U8O0B0lcwTJPoVGT2qUkp/6I5xWjhrSawS149olk9WFEh27uTRLJJSlalsihUrkMWbwuYrF4YT'
    'NkBc90ZRIFcchPrOhpgpXfu5anfqmde6nUnKhFxYkDnqjEDk66P2YKzxhNlErMDPfsR9qMQOJEwtELEIdJrJBs9hN3SVE9xP'
    'pJCxinWFJLUEvYpikXJNwYCE0rph4cETUFqzpZ0VxgaDsvKIS/0UYlQiSb6Mqubl0BkjyNFIHAKtjQRqaL+c2T5+XY2RktXw'
    'kVk1XVo334cZkCGrbv0aIEOvXhAXphkYemmiOJQVQ/mnXWRyVJKMVPKNMWmeQTZHG1pDeTyFPJumoiNZVFLN5Beur0Pzv1iY'
    'UKBnboTUIJr9KUe9yXS1RuUFQ4slYIThb8Ab7h+o9zHOHIPXoGwNoNOJhXyqKVfZRIFlXVmFhcBld4bWbBfJfcVuUVUP1rlQ'
    'YrXCJ1MUgZSCVaJGkKr13Jg0pFQrRc2KLyqrxsWLmCQjz5GLlwddJbokW/uhKIoieilJicNy36SqXODqHxtOuT2QSyETcllY'
    'TIJhuCLCH+RiGWXbYuZrZB75gRvGOOA1oRJBAMb6IVgtDWnCU0khLLW2M7y1jYdgD1elzlOVrkRektNGIDJHx9Si/LFD6EuC'
    'llGExyCIxuld/m5gY5/Tk1I+TJ/diuKMdJKi1CajDDRJefoOwJ2mRKdzfH1IeU3rhKxLY2KTEMzkfBcR9Ik9apIiIXsUlZJY'
    'bWpGy3K+Qboyli5+3KUjXHZSAM40gSIqMtGt4pOUC1QvF0zv11wOTnobSEJpEfoKfIuygHZhB0R1lHRat1T3RocmCRwm7lqK'
    'urOyOB1D2v7WVNXQtjMu4JS4QEr1JoJYW7NxeLEgsjGRm0TCHb2IGBKmHJN49LVQgQeFEt86i6RN7Tt4EefUsihAUb/eWsM2'
    'exRQFbfkvCeSlaIL9Da22TMZw2EZNKbG6KnGRFVg3lWrwHh8AKvPawuRqclgrB9681iNbibkFepssBv2IuHZu+WoBxGXEJyy'
    'PWoETmpSJCyLSNleY6f7vLNLLKU6kUZWYIW9S/yaZgyNe33hbMj1y80m8nCRctMi6wMWWkRhP3T0BFUaaUJlAZiPJQuYZ6so'
    'FPdXM+VsSn7j+A5Ln/op1BNXY0wqV5uTV/VGJwtQ6ZkMfHWlCHcJ4UI9/Zz5BPHyZSq0ihxwkKKRoFJTjjqlRTEHrO8EKhyv'
    'nG/JfaDNrDKZbOXEKlc1B1JLx1RyvEo+o20QMD2hEKNcJ5aU9i2UilRELrapSja1Ir0NNyAFJrTUUV4GOU0yhk8OSwJvNM2H'
    'zNDlGsZJDm3lyFhokcSQSQFxv6oO2QZv1W2gOKOghrBW4IdX1RF3bsa34mcPRAFY5Zv42k95Jk0R5R+NEBoxvZaYLfx6zdzX'
    'RtkJ6CvmKsQTs5HGf3gbVABV0wIjNk2lKiEXG2MNiYctG3On5h33epkFGg8LrXwe8LZTadVt4yNakqIEYkYqjqajq+/jRkgO'
    '8adBeGcFi3pXkeFZrdMQZZdS3qh/NtQXUSK1NWp7olHWMxW8R0HrVc0PSDVNCKTxk1w6VYsbr0KyVOmfyZFjqnrBYDB2Ri30'
    'C5d95CtGLhT9Df1xasGhk0dQJIDf0oFp4JhTlQJWsOPgr2iQdBzN2IHzF/e1RnOWXoiSoAzGxx7SgE4DIkJHEriF5MP02yzZ'
    'HZQ6WV24tNa4G4lmQSfXLZOa7USCm2sr3z41izpYSh+KvdrTsS5U6ce+5Q9gL+Pmvnlo1f3/A1CjAsk='
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
