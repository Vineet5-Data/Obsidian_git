"""Pool route 90629709_p1."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vHMmR/C985oPmgxTlN640tgRzRYGSbuBbEIsFbMPAwfewd2+H++/WSjPdPZ2RkZFZ1SNq5bcBOdNdlVVdnRkZGfnT/138'
    '/Zdf//m3Xy/+8NPFu9v37y8eLy/+8ct///V/Pv3h08d//vLrf/3tfz99/uni9ZuH3af/ah9++PiXn2/fvvnx9u7i8uL9693u3cXl'
    '2vzj5f1+8uf3u92rT3/cv97dfri4fD7784+7u/u3F5er9ePj/1+ejPrNyz9/fDe52jD+ny72u/cfPo/n7f3Dh9efPx0mOfnddHhf'
    'fnA68d8G8e7h/tXHlx/G4Zlh/PDxzd2rnz9d/cPHzzaYjGK8ORvGcOHxe9NxzGd9d/tyd5i0fjPzT3KHg+0ml55PEd7C/RK5FbHd'
    'sIKfJvx2tP+pCQ+2+LKQjfY73ufLfvu8J24/7B5O7/jH3/bkdFSHb6fMOV53nOTxBi9vD8Y7fKmT8cZJDXcavmO3fjgDuybAVnZD'
    'zH7GV+nkBqL17IaIzXi8XtJ8w05oMB/dasNO0Lfa/Lqi1cad0MVY+EGdTziy2vydJFpt8ifdbOZWnawF5uBbxPxr8nAVjAUM4ttI'
    'eCDJVMyHTiayHxyjdRv3zFbdxn364fyXPZwljoMH/ZyN624NX0hdz/hNhwO06Rrzo/VrjaNgX3ONo0v1u5jM7rZ9YXqM4+X93d3u'
    '5Yef/7h7+PDm7s1/nr68Kld8f/+xfZn6D+vVw/27ZZ+m97u730K3yZDHCG6RDRGeQKvG6z2ZJ44ZvrxzMvu2101ATJvcTSrGUFhd'
    'jgrEkeN8paeXGZ11/Xrz8+3kemgFjIcFTTo+HI6lVo9hgDIOBPi/1qdruLc16uiEWaN2nXaT/WMjJA7HHEQQGyFzaxLQlda+17RB'
    '2PKdzhucJAtN3I2IOt177gTA6Q4fvnx7uVt/B7PmL3IlFl7MBuTWv08TFEL7p3rnvtf/lq4282+3Gf92q/q33NHd4mya4lkpSbHD'
    'xRTUkTlQ4Bbz2wuRUspVTd6yzVwnWaSatz9HSXvbCgVAzK2c/a9yS2tEOyOQk4QHbdWJJ3csTDHzJmOv9foNiU1DCL4H7CberyUq'
    '3HR8aSdeZIkBGfTkK4zhyRkFJDa/e5uAQ/ffRumV1XqSQ/imE4NLXVbOFXp+svP27+JBX3nEsz4e9DRA6+1DUx7XQk70wHRpcqIJ'
    '1alhKsCrjiHE5axnJznShBQHKQGOM+pYA0ouuINS3CJMd7MYQD787/Xtw3+ojvBGQEoPzj+fuk6qGYYH74Hi2fnmrvIO7fDHsSiU'
    'Nmua6e9xwIwZg+QuyJcylxnMJUV5AhjOjDRf/0y+dfzT9BO4dDRoAmUjGiHOZAnMLELBPN5vuuh2JvDpy6wAYRR6CTr52bNWPHkC'
    'rCHHNYttF3rgZmJgRxwoHcP/cltimAC48nxO4SkNs/XJOdPd7yxnPPM0Int8xVw589r45QwYZzXIqXlQCg5TAUhMvQq+XCQ1MLRE'
    'qWGGUYMbO6fGmSZDCj/xQL/UwGxaKxxY0uYVA7r1EOFwXUys4WBMTthDoFqO5mrI/L38pCW0v2oP7eGvr/uG7pv+EfvZ4vRuKS77'
    'ilg0KO9jIDahin3YuJGBOpLRCHLSmRGUCxS7sjNyNCy7guebdrzam0TmxE6bgUj6GbLJJYGVhzGDiijEuUTo4kdhxQEqXKMm9lbW'
    'f7FjTYZrGdTBXlCJ0PW4rtkc1tZk5fatAyfXVuxiBxuRhqtmmbsnV2GMe39/97liHoe415O/V9yvu9u3r/LF/nHgNq/nx/4OchdE'
    'N/HFLPHz/sPD7f6H3cPDXy4ub+I3Mi2D97M/y6Vt5iyk8fz1JQ6SYgBeGIuvNx6NmXsolh6vDP53HMiQAZl9Z2lre1XnPrAVvnaY'
    '3YeLzzNzKAsx2eOtawDKXdC7ui9tFjgwwBIgaTJYYmEeOTL0yUDYZp7PoNMoxUjGk884PdmCjdTCzTabbljH4cM8gRpkYRqccnlp'
    'QYUSOgIFcH1LWL6JJbVWQwdxdiETg2OYyOhmYWuCMQvrekXYHcVkjLvK6NPo9QrBeGKwwIEnL9Wp+cYRxUdJR+uhnR9adB4zdBor'
    'ISSa7F2R79Vz39mxNVHRauZokpVQZ0hqrfS7MWqlHHqdicN2XWKqcSG0abSyTYRT0+McvuBFIbIGfH71LH5jjNJatswfDzz5SYgC'
    'bh7FzKlzp2EOwB9tG9mLRz1AQHcahk2/VeHHZZbWyKfN3xC7uSMDxtZlkGRhQXBj19WOJnBfxHFRkQEWSyLFMM+6gDy30IJz7zOk'
    'J0WGljNHz7IvZx7hMuTDHXCnfQrJVxP3Zsfdbcxy6mJTgGabBx4xnhzilSODFlYdaSc75F6CVZ94Sj4bTWNWCsM0Phxh4TmPDjox'
    'XVEBnCktJVnAFmTZWMoiLpBbNUKgcIqCRbX/a0tDcU0+xMitjEBOUNjnCvI6JdHPyrBgCOnfVaq37JrBYRRzKaRqzoMlb8zGEkLP'
    'cykxfl13Z8Kbf7k2DJ9+fHP3Z8Dkged0vwGRsJqyXXNGisJTkookA3Qslk8XHl7om1LQykW9p0HrcycfucoHs2s1mF01BbNfPtQI'
    'YFZQoSWGnV8u9W6caRXj+CoXshaTh7MapQDo7zcSkmmw+ZBjgk+LmZ2cyXil2lIBd0qPleiAC9Rlu2xkIf1EjR+VFEjbNhSP7QOK'
    'xuRQuYJP0lvzKJIsasXHAjvCLmGYyhTzzHmPR0tYZhZYT0awHGy4C1FVi4+nqd5rs7+InsFd7mFshM8JPqkxSBYRvhZ2U7jJQmct'
    'NULo3yKOuquGvsTqRfCYtEyd17JJg6XXIIjfv9wYZsS+7XKCH73M1CINc649/H1apVnGPxsjKtE0y3ooUd4G/fFKD/gwwL3ORH6W'
    'e4nTlyA1shA7lDmawyhoOrNhOIoSCMtO9qXOSiIWNkq2f+E05PJKWWd/sIhdKZlzWeUKcj6vXSsrHeFnPZYokIJAOdjrYgaxJ1UV'
    'GRB4kmhtfTGOBo4j8KHowOhplSLsbfrpl/GFt2Et/L60PxMUSBaDUZCNIT59KaRyQQw6YcABgDh1XbmH4gPFMo/wkOo6SFVIBH2y'
    'vBKQFV9snPwAH0cCfASGRc3HeK2XbWs6JmiIQVJ39oEPN/nYBDwMhBCNhxUeN0uTDe1QL6OwUJQgivBTrs0S79n4oQb7Sl7QuUqO'
    'kmScatoc7HktGM/ePErw5f48TIXl/I7DjWfAKmfCithuEI2EmyXpuz1rJQ/W2zxzYtUXpaSoViIZdTgGYBMi9fLaQ/hfdAxW6crT'
    'FO86bNq1DUi/UxshSF2IEENeY53HLAiNeEWIPmLLvAA2cRZRLxQ2T4t5/JpHFqlKE0Lzr8xIEH2w3GRgTbowLHhLT0TfXhHbF+TT'
    '43q2gP8E5uUXw/URn6d0Rlp/h4Q0WQvhIBPs2EZy05tkSYaFZJXPOo2aBiQkYz/azFT0gRbLXYtXp1t9dupEqxYS0K1LRE+oWr1z'
    'BvzwcS7yRM8ba8tZ8fGHcvUAUSptACeAtwqgz5i5rlJ5qQ0XqkQFhFOVg6FvaEr2Dg94H17pFOJrwpKXxbJcFm3gOF0nAPW1gy6r'
    'w6hDEp0ePOs6kSajFfvcnf7zxyqBP3owvJ7wGYIEJVVr9RENppjPwHG31YdBol/oRC5i3xhLy2wIWy8R7lJBK4syZ8Y5RZCtRGC3'
    '0EzeDDxBE61VnSPECGMecNNp5XElVvGlkGMhjaYdsbf8MRMx9DdNO0Ivspeei7jtqVzYJtdOgOnrFS9UNzy/0aWKkQVIRgD8z+3V'
    'zgNPdWRNfUhoSyyiwwDO4ZNqkynSeyyh6aHWkC5iuSqCt5ZhVFLDW20rlfsSotWbymRBr3EYqNZcLgKqIhL2JQnSpT55og8YyxbH'
    'EokK1KV1ZWUiONJVdOi8MqH3yHQeWkg3mZWz+yjgtLRgTVdlEYScNxZbvgFKvdYhJU0/XSufIo1ldNArJX/NlE9qmmlr3XTQJ2cq'
    'KDZ8AA2hOlmNaSL4RNKcygR/whLLmHt0mExGpvmX9e7GTCvz7RH+VyylH94HPsMA4Fn6Y7ZqiiOVQSXs3SKSzbdqnCNsEKKGxC/l'
    'kQiJCnmyh4pJ0kC765agwgr8ZZXUDiDWmpGCmCINKRm6MTFPmnVbldiLWqdpNkvzetyQb4x+LhtEAOLobpOP7lZxM5oecgXZoC5L'
    'L2mSWqPE6F4kCha+2axj6/2VFQBhCRXz3evvB8n+5i1ArZ95NSrWh8Xedm940HTN9lpJPvG/qk1MaTqb/MllKDTLUNGBJLkPmf4u'
    '5LZU93snKyFIOvqMWdQ4fVaAjrYWgImBAZjWc0luyy/lCFUOCwcApWPwB47YrNAz81IeC2UAtscHTMu9vzwILQzQmiq4fRZ6dOaR'
    'NGVww+nCaHQqAmkIrYsxLmAmQFHQZH45JNfDZrLyWbEKJSE8CINBkuSebrB88NPY42mr9Xi6NnHdCy/ttS4luYSsUUe1tnVcx98m'
    'xjYNtOYu/2IdKN2y+z6F9bRGdxZN9Ek8xZmTjFHXNdzeq5Dvk0Zi1QDUph0L3GkdBd+9ZfoxKrn10w/zpOdytdQkGkm1YunUcYeZ'
    'oistmhZEMNc13hVNjVUAcGI913hTJAizTDYjCNIbkorXjxnla1peG69IYhhSeaqrK7IcZxPFr6o2iHZTqazV3rNfK1KdQ1+KxMJy'
    'a/BGIqzUL37iut7WKeeP89/REYriwAhQi0wGCJ8F4CSUGxALLnqGAaZU2Rr195jjWC7ZIaY98hw8ON7m3AgCqlWV4kQOoTWFcqZh'
    'tmZapE62AZlt8YSMmptgEHafFad3ZV5IBllcMrmjepAUOjtHDog4NnRZdjII2p4n6lBrfIZ0EpsV8LGk+K57zilrSlq+1DE75ekp'
    'BU851UIKzRkoJNNsDc+hs3SKn4jrm+ZJ58JoS9OBLSQJdDlMIKTiQ44k8IiwYhdappRIYmE4nwwvUU5IrY0bl80m2oUrSDO/mso8'
    'sLFllAkVbDogBLYxpBlKzcGSClHZ7aIn+mRlFGk2SyiyS5sgF8yDh7fHVLhiYrTSQPCNFMQt0BhY5ts2CJ41kC2bW1vlC+4+nxGr'
    'dd/MY3N53VpQ45Z+s20VEt8+dslarsPCt6WVxGksfNI08Dj06Ua4cqY3/c5muaSoRSWstxQY0FaNNuf2iMgNRNskEqCa7SNLDaAb'
    'O1SFkNlhDZ3TkIxn+OY8Chz+vHzWliomU6AiLuXqqPoc+kAIbxJIysunHnHUC2KP090w/Zm4ITLjJbVgtrIG+PVE5ct0XuVjzgVM'
    '/BNV2ts3CP1vEtV9mPLHGJOnKw//3lrpR/pU1xC0KvpFwMJcC4QEg9gBnkAXC+8J1NOEmbI/I5wECyqzpaEC0VgGgCj4FLNJbWxd'
    'DrggKAd5RtM1NL/KNc1SliWWrQOjFMS/c+ciHRhrNpxM/VojMS5FaBtfySxjG7llRISPIBEriUTdU+t7Gmhsv0JJ4LZTunz9FNPl'
    '/BOEoZdJiTtxZZxn7p0dNW/fbEPhCcKF5rRaIBXO3CqaQO2T9nZpc26/KUqNPUOaO+j+ocVHlby29l6iPX2iuLhTGpv04HHklhMp'
    'TOCRK/VqeARh555dQwtmWlG5o0kTWkaUcgUZ013rVVawVvK9TjAV7qFO2c8Q/6HVlZU1reiuo/HiDFll30l9l8FY0GtetXboc1/H'
    'jkcQSfJDKxx/rkWRnqHVavTxOhOh1XwQoxOJObONNBdhL8bsE55PZuo9opSRt1SHym8xMw6bb0jKjE8SD4e/TJvv3HSCfuEEEagE'
    'z1jwpLZ0SI4wkSaex8L0ArvegsX1rH0t92s1iU8aODVng6dXu8ZSqyAcf34Opnq5BHVBfrrc3jqX+I1zmeXkdVvNa5wCXktp4tYe'
    '0aUa0GQkT9GvaOq9S3V3bn/cuM21WBfROQXN+hFTKIhyKhdqby4RDgJVSvIKpWIjC1Udmx2DkpSKVIfvHJ8px83rOkBaW47MvPRI'
    '38ZBrOYRPJgsccA8Vjdf2WkaIEghZywvyfCiP8YAXnxRwP5hMmZoW9qsiENjEGgWvfqOyF15xTIPge4ZyH5qk6prX6HD4dT8oNbT'
    'k3Zt16RJlxzHkklu84m+uIjU5BP8jlm1wNDVW29Tm4bcosJgWd6Xov2sRgm1ucsEiYfy4XUsGwt3MNxoiaZjop+Um5IXz9gFiOJt'
    'KhMpK1rld05rth48VKUy/qC2K7fnEsIWrIETUU4ePtQ2zhTQ2C6mmhwfeNMPzadOmjtxaoUsoV+pO/g3fyIukV8MwoH5bFF5IFuc'
    '1oAWkOyWfcpJ/E1fmS0jzjR/gXs1y8kg78yFOqYz1sYptxoUhmC6xPlgmmwSK1gHWqGf6c3SBNlIjaBw3j7Cn1wkqlOzbxZEU/27'
    'FCupzFtvEq2Tsqo4Ks4vS9+iEaB9pykR0DmDb5Ugpyb9PAnthiEzXBSNt3CGBuJqIYdOLY/rGBbrCc4rxlnkG/wyuUKfw+AV4Apn'
    'On1biF2PhOPjga6c30U8JEjfCG1bdUCIvpAibQX8V0aQU5yFrYCBhhQ3twKB80+amh3xDPsGEtv7hK0AnovWDluQKGcowNS2T7qa'
    '471gRWk/gNQ87FqdMrs7rKFln7hiRgnWX0k9JEQRdVHHgsKLLg8p9JpugMe11Nsu1tzIMoMYDvTlm5QuKkOAZMjettGht+uuzKSV'
    'c3A2y1RcOtVG59DWXJ8Z7PI5LLwY51pl+FBylLmihP2tCuYov2mIuINI4gpKgDbNNLAqOYooVQoNsPvUlVVmYnexJRc5zFYABMWV'
    '5vU2enWEjrGkeDkVCiZA3Vgo5tUHrGNlYXaTxbLnXGB136Vb8Tax4TxuQQREQu/59BI6G1pSC20JfwOviPN9dorgJMWhstqtXVsU'
    'sB1METVWssCWzsIfy2n9w64TgATHhUO9n8RBpCiLomWWVDlJUXQ1WlY7dqIjkivxIwIqtAKMRSVaUSx/EEm3YkFDR6//ilbo9Hfx'
    'e7vW9hS9lYN6GbsD3CmW+3XqhYRMyIjiixBJ2AWvPCq4nCjRBEBCrAXmFpdHm2evlaEDLLNqeHamUHPHzFkIfhQ0cAIYVeNMCZLR'
    '4eDnJupR2es5/BLHKwSikl+ncKStIdUr1AOaLNE74KxJ6LiWFXMKi2bxKO+BJqCbDIxlNJLIahD+my0tLSrLyqifvlphvsKLmNJN'
    'cHhp4ZVb6lhksR0D8WdnYbCtvzqDrVyltw4zDMkquI5ddWg5pcYKE/7UraWOhTu4lABXh8dqQgu02AEaqKIsDN02nXvsgB0Q8j60'
    'gbb0CkGOjN0GqjmVXuq1ZQ8EFSFqxU0aIZJKFMyIZdCycgPvSAAH/z+xJ9JlSzJriTSvDyGZ1CYWo1E2mZg4EHyD8gf07Y0ea0dC'
    'WLK8BzhoGuRSV4tYqzdibctPYFSaXJapoWWtUTwZPYJELCglqUy6hDaILXEyijj2sMhJP44prZ8RYdJmHsk9gR+fEgMOq/akagBt'
    'ogmAzS6JjeZAZydF1UhCVkj38h93d/dvI/kW7yhVtZ0CHSVPFUvRc4ri3DBMvYlDClteBl+/9mvztr34T+7/2IKtt06su1lll0mo'
    '0Y6gAgC7qOl/17tOufyoJAhn9gPQRGL7iRLIzdLUOZZbwsMdZqI4LgSLipeqibq1xcwtJ0W7HKdrcxZO1+Zpwj+rBMvFZy6x7ky9'
    'aFpXndAhQV/a/8+TpXHRejhiljyPK7GN+vC6pKo4xVdNs7hSZQiPXZArMEfH2WX1T3Dd/LR9123nU7U8hojWOdevNasVZW0em7pQ'
    'J4tIKXuJhrk1+lqG00T7VDMJXw8CUWWTG3hNV49tja+hzBuMJaneE+kE1WeXPhcqLLRm1LLKd5oDFa/jTWKfSuuogizx6vpwCV9A'
    'OJubx0SjJ865iQpT6SeXURcyC6s9uxu6BcenSPzg1Wh02nknUUKkvIwAwpYaJQRF6IkznJU2BaSPOFpE/cilNuRwJ6kScOxZsA9Z'
    'F9U0b2+H9V5M3ZE6HH7yQn9QFOYKP4H9dEo0X4bH0PTmDMW8ScuayYgj/BFOYHirzuYmFCt0K//Vm3zpzCjyRoUqcqlHT6K4aeeT'
    '1kzSBc/s+CsJgty6hMvBvSG9sVxymnGaYfPYKld2uPTmmUf+emYyGTc429GIHl6dBSXsLHMmAp7t8mcaOayMDjYhf0DzjAJCPsCV'
    'rfxrYorZ4r+gk1S9QrFpOxBR9JCH0DbOXIfBUNKMoQRZJfcSOyxwQCxeg+1LSiMzTAONKYYYgrH/FDj0rIRKDl0ZcYxuQfZQypw8'
    'bwrl7r5yO6rADQKirpq4UFzlG687eIxevfmT50lycRkwNz3WIcW8up60XeOEQmKUbs6QOtW+0Fobxbr9K6/A4/qz5y/Bh9QAhQpP'
    'lrW69sYVUGOCLSIGX13amDPzH5conBk+kHyeVVE+2gGG2Fx4WWAuHOMEjSyYis/4YK7xSgg1RwVFe4ZPiVpUjBh2Xu10wMyqMFMt'
    '2a+g0L+NQ2fr7QYoFFgQIICGT6NaS7oTYaYXLUw1ptQWEeH79tuLvcrj8Ri+yEcCpPF5+BZrGfD8RRbTsp6bvfiCiSe1Qyurtaq2'
    'xfhmyylvdesaSLqNQdBh6/7nqpW2teadCs+qrmWLodK0rfWT0KQiYT7rKNWFltU2lU1Fb3mfKzWg3YGUvdyHhQVxIKqSpXUmpCJp'
    'XLW3WVeL9PpjLB9amSgogC+vrJVqpSizdsgODqrO0krfsmqW1it9n2utTps5Mz6gOt9VG82MAa1RbCdp8Qsbdd3ETUo0qUY0R0mB'
    'I6mQViPUaTUL7MFMdQPEq8tQcaXnu0qiy0lrOcUmKAQ8OPZiqwdpv8Z7kIUTkcVz7JgK/KlmjJ0yNIttsiE7bCaKgwOtGDozZoHE'
    'obp6liELOhNjoCQ/g7SkBfllnTXoMS54ha1XwBQgkbUyWx1FinZcgUFD/9Sm6cUzBVFZLSnTzKmWcpWvCqPmeAYKanDhu0kS3FcW'
    'qVQCpzxLhHaelB7bR5ByIqU1/xMPD2KwOawziLbZ6e/sspLcoyTEZmhG7X12czkHUF8ewKTWCGJXhXAvr/vq+q95zfrwDp07EKsO'
    'gOT116sI3cQNfcpdO48GKnQ2NFSo5mLShuaYZXKYhC+miwWXY4UBYNDiOnlWmFKyXyMGsXi2gR4mZA9rNDFpQwSDSzRGyvjQrVgy'
    'J0+YQJW5lX32Bs0PByxuEpnJdVIJ2WpJ/p0UewZJSwoKuAhLasAM9OQ7nLq6eJmGzaTr9FJlcDBmu79DThBryUS2uL5NUCXmTiSR'
    'xQKFR6MyISqxNJDwDq6F8tLgKEtUJ+iEOVt/4EKDuV2W8689fEJusmYCDLTEiRmhErqdyCszO2qvUkZ3UbVPDxVxevDEUag6B33k'
    'siz1Xo+VmYOEaHboKGSkFt6aWq+qCiuR8hp4VCFxv4t7Lja3TUTjoyQwxlWL2TkEKXghSOCJUB3ls8mqp+C3hWldl1tbhvtNjhWS'
    'CnKdWIe2/WI/fXaRD22J2QW2mJ2HLDi/95Xy2Eu8NmyMGW0N2LHpCkpt10zS0uEIdebHOSDO10Oozq9Z1pv89k0Kla1CvtU3pUOW'
    'nokPIiylOibR3erzWIbtxioiGdWNC/4k6DhLbSsGiUrvTirNpbfe25KjvyQwxlsf0gWy9JMYcmJz2+g8N1ZtGcePYUm2XBAaivep'
    'TSG3AvmLr4vUb1UkeaXRnbQ+XKT0JOj7kTVhfC6nD0NXUTFCZEMyhKGUfVl9K/X9HLQVtqMNJSVpjTGGWkagLtXVg1GdEtCinG8h'
    'hCkJBavpi7FCRPb6YTwsbXOxb5U6F+KG0gLVxCYH0h1E2CoXsVK7HpL6gCYSgCbjMXZaAC5j2ViSLkpL+vZxH6rUU84yL7TPJn+G'
    'aZEJrTvpIfwWdt6hrDFNW5ZRlArrEGjr0QEPR374dqGzDelUm5giFpZ6CnRA+DbTVVkAlJxpF6k2OrENL2ttAOQOCcAUcqPIY3h6'
    '48Blq66o3AuDjj3HnQVA3UcjMnfzdFoHADOvz0cUq8uEleXkO/LCIJcqg8NBhbPOmFwBIxkq0ztUmio1m42aYsTxSsv7a9nG3hpj'
    '7HkQ1bPahstYY0Hymm0SiqylgqymDpUwVOMwWVBnlhDXLkllw5PFEjFyIRUQTgk5eynptISGymEqdgDDojFJaS7A3bYeBPNh0XGg'
    'HChVJkcMlprINw2WI1GUoCwA1QcP2de8lB1Ag6PusjWAh1l8TzCqxhWgVFpOjQzbuO5SGtE5tpX/uJIjm9pWM3ybmJ0Gmwf4E93r'
    'bOx6mM21JqIOpvsUqYWKNrPOFVWSW8zF0xvAEvZ5Mj6NY6BncRwQuBUJ0e19lbcHI/yQrbNPKtvbDpyWopPpF9muEra1cfm2rrqQ'
    'rWGEDDh7AhBhtzwZ0+IRJmQP7AEdTRYpRcWDdn4pKbgkc+6SSN9N05bQOuHpNcwlPnrB22lc8uOLcrHJiwL5KSRss/IAt63QAfjG'
    'LsRNDkH6PjhpeVynudaxM6EsOcZFMSqlxIemd84gdq80CauPsRDJWluN+gfzwbOS9oxc1rlQJ1ZYR1WvMoL8Up2ilaZ2qCpUm0ys'
    'E22AY3JEK0JFoKQ/4Bzn9iyPz/wNrLXVVNTginwaazqeOdAL9KjGWRZrNLIWdv+GIZoMbEiiH6XWlZxlKrIjo1q40oZAxkFFWwG6'
    'HB0ilBGR3RR7SRc6QhTpVuCNPWpIDzJrhKGpLcG0It0OhkaTCGBQtbA0s5MBJigXJ4nYH9fZZ3Nu7Ecog2qiphZgczAiqglgTWZ4'
    'TqhWtpIiVERVMjR1fr2PQRmqyFeYEshT1YSXGMY5ZT65gx9rCxAULoLpcXyKduQzeMOpVJNlw1yrXB0sSBYAYgZPidBQnXYFCE/8'
    'N2VPmzLtrxxbe6fDC85RGk+WMpZhN22iBRfTkjWHnAhSWMBRAh3a2mb0bZEaZ0EqoRGB4xuWZt2s6LuvxCaZNh/hhsxZFhUhFTut'
    'Sm3uw7edKpecCFQz5sU3Iw5qj0Qh1+DJcGN1GkogcKu36mWaPiF7mL6zemAlHLctv/VYR3mbMiRuM6+0k/hSQapKZCVzejl32xW/'
    'FoRUIIlEWxVGuV1wC5KHtMuU0iAx1fVzqnRc2OGnxbxhhx0HstUAyyXrjPxmYB8io1Eb27d+fZtYDO54OrjHfwG1EBX/'
    )
)))


USE_WEED = 1
# Measured OFF: the stationary idle layer lost 0-12-0 (margin -519) to the same
# agent with it disabled.  rayk's +258 on a different host does not transfer to
# this route - the extra output depresses our own premium prices.
USE_IDLE = 0
USE_IMPACT = 1

_WEED_REPLAY_STEPS = 8
_WEED_STATE = {0: {}, 1: {}}

SELLABLE_PRODUCTS = {
    "WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON",
    "EGG", "MILK", "WOOL", "FERTILIZER",
}

# base, equilibrium, scale, below shape/target, above shape/target
_MARKET_PARAMS = {
    "WHEAT": (25, 10000, 400, "sqrt", 0.8, "log", 0.2),
    "CARROT": (35, 10000, 450, "log", 0.2, "sqrt", 0.7),
    "TOMATO": (60, 10000, 200, "linear", 0.4, "sqrt", 0.6),
    "STRAWBERRY": (120, 10000, 100, "sqrt", 0.7, "linear", 1.6),
    "MELON": (250, 10000, 300, "log", 0.2, "sq", 3.6),
    "EGG": (50, 10000, 332, "linear", 0.4, "log", 0.2),
    "MILK": (160, 10000, 122, "sqrt", 0.6, "linear", 1.6),
    "WOOL": (200, 10000, 105, "log", 0.2, "sq", 3.2),
    "FERTILIZER": (100, 10000, 200, "linear", 0.4, "linear", 0.4),
}


def _get(value, key, default=None):
    if isinstance(value, dict):
        return value.get(key, default)
    getter = getattr(value, "get", None)
    if callable(getter):
        return getter(key, default)
    return getattr(value, key, default)


def _seat(obs):
    return 1 if int(_get(obs, "player", 0) or 0) == 1 else 0


def _farm(obs):
    farms = list(_get(obs, "farms", []) or [])
    seat = _seat(obs)
    return farms[seat] if seat < len(farms) else {}


def _aligned(action, obs):
    action = copy.deepcopy(action or {})
    expected = len(_get(_farm(obs), "hands", []) or [])
    hands = [list(order or ["PASS"]) for order in (action.get("hands") or [])]
    if len(hands) < expected:
        hands.extend([["PASS"] for _ in range(expected - len(hands))])
    return {
        "farmer": list(action.get("farmer") or ["PASS"]),
        "hands": hands[:expected],
        "market": [list(order) for order in (action.get("market") or [])][:10],
    }


# --------------------------------------------------------------------------
# weed repair
# --------------------------------------------------------------------------
def _tile_at(farm, position):
    try:
        x, y = int(position[0]), int(position[1])
        return (_get(farm, "tiles", []) or [])[y][x]
    except (IndexError, TypeError, ValueError):
        return "LOCKED"


def _trace_actor_action(step, actor):
    trace = _ACTIONS[min(max(int(step), 0), len(_ACTIONS) - 1)] or {}
    if actor == "farmer":
        return list(trace.get("farmer") or ["PASS"])
    hands = trace.get("hands", []) or []
    return list(hands[actor] if actor < len(hands) else ["PASS"])


def _weed_repair(obs, action, step):
    if not USE_WEED:
        return action
    action = _aligned(action, obs)
    seat = _seat(obs)
    game = _WEED_STATE[seat]
    if step == 0 or step < game.get("last_step", -1):
        game = {"last_step": step, "active": {}}
        _WEED_STATE[seat] = game
    game["last_step"] = step
    farm = _farm(obs)
    positions = [_get(farm, "farmer"), *list(_get(farm, "hands", []) or [])]
    units = [action.get("farmer", ["PASS"]), *list(action.get("hands") or [])]
    active = game["active"]

    for actor, transaction in list(active.items()):
        index = 0 if actor == "farmer" else int(actor) + 1
        if index >= len(units):
            active.pop(actor, None)
            continue
        age = step - transaction["start"]
        if age == 1:
            units[index] = list(transaction["intended"])
        elif 2 <= age <= 1 + _WEED_REPLAY_STEPS:
            units[index] = _trace_actor_action(step - 1, actor)
        else:
            active.pop(actor, None)

    for index, (position, intended) in enumerate(zip(positions, units)):
        actor = "farmer" if index == 0 else index - 1
        if actor in active or not isinstance(intended, list) or not intended:
            continue
        if intended[0] not in ("BUILD_PASTURE", "PLANT"):
            continue
        tile = _tile_at(farm, position)
        if not isinstance(tile, dict) or tile.get("kind") != "WEED":
            continue
        active[actor] = {"start": step, "intended": list(intended)}
        units[index] = ["DIG"]

    action["farmer"] = units[0] if units else ["PASS"]
    action["hands"] = units[1:]
    return _aligned(action, obs)


# --------------------------------------------------------------------------
# stationary idle work -- NOTHING MOVES
# --------------------------------------------------------------------------
def _idle_tile(farm, position):
    try:
        x, y = int(position[0]), int(position[1])
    except (TypeError, ValueError, IndexError):
        return None
    rows = _get(farm, "tiles", []) or []
    if not (0 <= y < len(rows) and 0 <= x < len(rows[y] or [])):
        return None
    tile = rows[y][x]
    return tile if isinstance(tile, dict) else None


def _idle_job(tile, inventory):
    """Best stationary op for this tile, or None. Fertilizer outranks the rest."""
    if tile.get("animal"):
        if tile.get("fertilizer_available"):
            return ["COLLECT_FERTILIZER"]
        if not tile.get("fed_today") and int((inventory or {}).get("WHEAT", 0) or 0) > 0:
            return ["FEED"]
        if int(tile.get("yield_units", 0) or 0) > 0:
            return ["HARVEST"]
        # The engine banks the care bonus only on a day the animal is also fed,
        # so caring an unfed animal spends the op for nothing.
        if tile.get("fed_today") and not tile.get("cared_today"):
            return ["CARE"]
        return None
    if tile.get("kind") == "PLANT" and tile.get("crop") and not tile.get("watered_today"):
        return ["WATER"]
    return None


def _idle_fill(obs, action):
    if not USE_IDLE:
        return action
    farm = _farm(obs)
    private = _get(obs, "private", {}) or {}
    inventories = list(_get(private, "inventories", []) or [])

    def inventory_of(index):
        return inventories[index] if index < len(inventories) else {}

    def job_for(position, inventory):
        tile = _idle_tile(farm, position)
        return _idle_job(tile, inventory) if tile is not None else None

    order = action.get("farmer") or ["PASS"]
    if order and order[0] == "PASS":
        job = job_for(_get(farm, "farmer", [0, 0]), inventory_of(0))
        if job:
            action["farmer"] = job

    hands = list(action.get("hands") or [])
    positions = list(_get(farm, "hands", []) or [])
    for index, order in enumerate(hands):
        if not (order and order[0] == "PASS") or index >= len(positions):
            continue
        job = job_for(positions[index], inventory_of(index + 1))
        if job:
            hands[index] = job
    action["hands"] = hands
    return action


# --------------------------------------------------------------------------
# price-impact SELL slot ranking
# --------------------------------------------------------------------------
def _shape(name, value):
    value = max(0.0, float(value))
    if name == "linear":
        return value
    if name == "sq":
        return value * value
    if name == "sqrt":
        return math.sqrt(value)
    if name == "log":
        return math.log1p(value)
    raise ValueError(name)


def _market_price(item, inventory):
    base, equilibrium, scale, below_f, below_t, above_f, above_t = _MARKET_PARAMS[item]
    if inventory < equilibrium:
        amplitude = below_t * base / _shape(below_f, scale)
        price = base + amplitude * _shape(below_f, equilibrium - inventory)
    else:
        amplitude = above_t * base / _shape(above_f, scale)
        price = base - amplitude * _shape(above_f, inventory - equilibrium)
    return max(1, int(round(price)))


def _is_sell(order):
    return (isinstance(order, (list, tuple)) and len(order) >= 3
            and order[0] == "SELL" and order[1] in _MARKET_PARAMS)


def _impact_score(obs, order):
    if not _is_sell(order):
        return float("-inf")
    item = str(order[1])
    try:
        quantity = max(0, int(order[2]))
    except (TypeError, ValueError):
        return 0.0
    market = _get(obs, "market", {}) or {}
    inventory = _get(market, "inventory", {}) or {}
    prices = _get(market, "prices", {}) or {}
    current_inventory = int(_get(inventory, item, 10000) or 0)
    current_quote = float(_get(prices, item, _market_price(item, current_inventory)) or 0)
    later_quote = float(_market_price(item, current_inventory + quantity))
    return float(quantity) * max(0.0, current_quote - later_quote)


def _impact_slots(obs, action):
    if not USE_IMPACT:
        return action
    market = list(action.get("market") or [])
    rows = [(_impact_score(obs, order), -index, list(order))
            for index, order in enumerate(market) if _is_sell(order)]
    if len(rows) < 2:
        return action
    rows.sort(reverse=True)
    ranked = iter(row[2] for row in rows)
    action["market"] = [next(ranked) if _is_sell(o) else o for o in market]
    return action


# --------------------------------------------------------------------------
def _fix_animal_species(obs, action):
    """Keep a scripted PICKUP/PLACE legal if the two species got swapped."""
    private = _get(obs, "private", {}) or {}
    shed = _get(private, "shed", {}) or {}
    inventories = list(_get(private, "inventories", []) or [])
    units = [action.get("farmer", ["PASS"]), *list(action.get("hands") or [])]
    for index, unit in enumerate(units):
        if not unit or len(unit) < 2 or unit[1] not in ("COW", "SHEEP"):
            continue
        other = "SHEEP" if unit[1] == "COW" else "COW"
        if unit[0] == "PICKUP":
            if int(shed.get(unit[1], 0) or 0) <= 0 and int(shed.get(other, 0) or 0) > 0:
                unit[1] = other
        elif unit[0] == "PLACE":
            inventory = dict(inventories[index] or {}) if index < len(inventories) else {}
            if int(inventory.get(unit[1], 0) or 0) <= 0 and int(inventory.get(other, 0) or 0) > 0:
                unit[1] = other
    action["farmer"] = units[0]
    action["hands"] = units[1:]
    return action


def _terminal_liquidation(obs, action):
    if int(_get(obs, "step", 0) or 0) < len(_ACTIONS) - 1:
        return action
    private = _get(obs, "private", {}) or {}
    shed = _get(private, "shed", {}) or {}
    prices = _get(_get(obs, "market", {}) or {}, "prices", {}) or {}
    stock = [(item, max(0, int(quantity or 0)))
             for item, quantity in shed.items()
             if item in SELLABLE_PRODUCTS and int(quantity or 0) > 0]
    stock.sort(key=lambda pair: (-max(1, int(prices.get(pair[0], 1) or 1)), pair[0]))
    action["market"] = [["SELL", item, quantity] for item, quantity in stock[:10]]
    return _aligned(action, obs)


def agent(obs):
    try:
        step = min(max(0, int(_get(obs, "step", 0) or 0)), len(_ACTIONS) - 1)
        action = _aligned(_ACTIONS[step], obs)
        action = _weed_repair(obs, action, step)
        action = _fix_animal_species(obs, action)
        action = _idle_fill(obs, action)
        action = _impact_slots(obs, action)
        return _terminal_liquidation(obs, _aligned(action, obs))
    except Exception:
        return {
            "farmer": ["PASS"],
            "hands": [["PASS"] for _ in (_get(_farm(obs), "hands", []) or [])],
            "market": [],
        }
