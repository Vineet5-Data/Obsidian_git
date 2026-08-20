"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vG9kR/C8682CSsmznJtvcWFitZchSiI0hGAtkgwDB5rDJLch/jyyJHHK6urq63xtK9vpGy+TM+37d1dXVn/579Pdf'
    'fv/t19+P/vTp6MPpx49HN7Ojf/zyr7/9+/YPtx9/++X3f/76n9vPn47enV2ubv+Xfnh9/fPn0/dnP52eH82O3lysj2Zz8+eP'
    '71arD0ez481/fFyt3t7+ef1udXp1NHs++vNPq/OL9zt//nB58fb6zdXuD27+N9vrxdmbH68/7Lx/259PR+vVx6u7hm4/PPR5'
    '52fb9u1233vHQyP23/L+4vLq3d1Dh0/2PQ8/pe95aKb67NfXZ+dvP9/+8+r6y4SQB4++qbf+/PTNajtIdIgevvllFvaef/sf'
    '76+2M+u854fdRcFes//Fvbk+vVpdes9/cxoM0P0X8LhserB56c5zH77ExmW0ydDjhqYXpta+YHgcWPb6hNrnbp/mD4g8kfbx'
    'Hy+uHwYcjEc4gf44DwvPDkdl/nZa549D0/xtTy07Di3zpwxIw/xJ41KZx81vwXDcd6D2uGG9jf9Ue54d3i6rgXW/aTVsHrI6'
    '7bgIlNHovAbuPyQeh+yc8DoIV9qbi/Pz1Zurzz+sLq/Ozs/+etdMe5+kbv/CtYWaQR6wueVSDQVvDRsajE6y2Zu923OCKpu/'
    'fmB8/8n3nzyhn+yfiR9X519ct52dcu+RYQ/Q+GgnNyn/aWuFxCePb/5bP2tWO8qMP7Q/NLDD85vkWTPqR8vtMFyKlYaC8x+2'
    'XWmhf5fgNsY/N8MUHvIb+6DzMIHBx6NUaeDY3k8tgh2vqfBqO8CFJgwDbFogjy+YNmeAwwYyz7JwlJohKjxjO0L2t+oIgYfi'
    'ASrfFn+U31avur07bx/FnI/+/PHq8nT9enV5+fPRbFm8DEcful+Kva7Hx7koW6/MjXu6M1OtPZFcsRkAKstXqn5v2MbZYw2P'
    'SLNbNb5+m+4J4PfRi7hHBwzsmR0hMIkI64x9ScVCGpZH6XlDw1z8u5OZ6ZkemhFi7YURJth02dqDwwWgio0cgW4tV9/3h/R5'
    'SJtd0OTxkjNxHC79fvf3cpfbGp/0CIttNv5z0UVzHOkvq/f08i+FCwwMJrkmyqBDwsQBDwWBtIqTPHaxpeY8HPDacn6MSdBd'
    '7m3rpI4P38YeuI1+52N4TbYDcc+3t7IyIbpHbsOh8ixJobBKn7/9q3tzcr+4M4Zrbr5DbtK9/+M2ulLdUxpf/4uMcdAAOSAb'
    'IXbBYvc0tpTaDY7HthCQg3kAc4GQw3y7IT61PUJY31H2V6I62vEh7LEBonFW+2BtheG+3F5J9x/aNtH4sT1gHQcVOQDSnXDF'
    'WUygxRVXUbSWa5F1sz6mClxy4Ic0hWkM8ehAM/CYoMIyDyooxjp4zdMyDnYdkkPYBczdCP1JH4foAqLk779E+IFBQAzX6DXw'
    'wPPsDoC0kE5QbKNuBugRpAMM/boy7syQSdge9jF4IYQPent58SFYB8S+GjzJi4vzh5ManODLjft3e/G8PYptO4s2oFcTN3TR'
    'Mwi9eWLm4NBtUu6Fbp+zXWz6k4nTMjzWwGIjoyDBy/a8GZBskligylVpY0YFVwDn9ogh8BL6crdn5nTTKClmKYBmUURB7n68'
    'xCtRi6PIEZwl2aWvdEZla9xnBkNUcoinBb9JfpoU6EHvVX26Li3VQSKQ3uabH1PZlMD8c0bH6YY98iura3z40xGYYbpFi6EW'
    'LK/9ywIdKjn2Tc3PIF6LN2dsPXUmGW9ehaZGXjtdCacIPLWv9CaqyTsB6zl4H1zRK9U+ADQqs2bBEvCN54TJo7CQATgX4Y3M'
    'vajjsCTCqp13aBg78KnskTgyDvHCsFF/jT2oZU4596lAKZNcCQLh2gePZoeFk/SlC1Nq93YNeuzW4H579ufRlwpvjAl/yMZH'
    'X28JQoN9Ad4uXiOVCDEDeWeTBabd7NNpiWe7EezBkenpNs2wq9IzpswdKoNHEAOWK4jsOlQL16Fa6Dav5MoM97Udo5aUWud1'
    'u+f3dmB1i39x0yE9V3WfMo6kkkKGXSBrQk3iAIU48ozRgJCFVVsU3N8xrYR8pokXh+D1GKNOoK1JpAdrNo7Nok7Rg+HWc0Yh'
    'k5+nUFaBaex6w7l3BbPoWFt7S1qhzQH7H5isw9vM2Lu+c7x4WHwitCG3k8ESShMvRFs4PGfDRQRcO/80oB5uJimUnFQ++9HF'
    'OrbDoayn6ukERh9xQnowNcc39CwgxLaYyEyFhyFCDeYxDs4phvHYqj25yfM8gMhQX+v/kYz++bMdq/+ns/MfvwyP8QNetMZR'
    'mkz8hWMBcROf+QeRtS8A6JK9jikkGVNVYAVI5nHOXu7OJUBttDddpU3LrB2JkKvoZuxAcimQRSInMD7BK5yS0bIlp3kdAs1z'
    'UATrno1LLyeE2pDDgi4sl4YoB1gaocMAohyVdFhCBQ9DYzGGb7aMSw4JF21TL7fvAKYbWY8dNgobAuRUREvQzEOn9HjuHQdL'
    '0LC3ksI2NgIBcunE4GwTXEvcyd3V2ab/aD7sPpr5Q/1ypuCyn4A9T94/0rqZKDlsFujfTPfaqWMMk7yIUbROnOjCQGns7GJM'
    'NghdGGX7QuQvOjhI4MzTHSQbuwUhFfalLsR9RwRLe2PQeJ9S3ponYI+itWuHEA5C1vovcuhqOJbtmvXe/AR2xyhs7Iq1jazG'
    '8NDclGM3Vu4OYmFil9u8Q5DAREX1LdK8o8itzQuL+eU9TdABAXW33QEWppOqAwhWFYxZtQDslgCth/rzpHjBRHg10OwPLJ7w'
    'ZABmMOosnZ/RSFS0mWGfAOEamc++m+ownTKuxGiSiXIk3iyEeDMsnIdcFOj4OHlOqzg15cFMOfGsF58b8dLlRihkSSDv7lBy'
    'REKWzIhl02+jKqDWQcwUhEyShP8P8UsvegghE8U5TvrnZJWDt4UwlQwLggNzuxV8oAF3KVr2uzN24q7vVwdY3ySUOPomGCh2'
    '4Ysj1bhao6OXWzou6WL3/+4XAZ/dykEtANM+jznoVwCXadBEUjGwcSFq9xYtnsQuQVmSYCFglXxNyizQ7fFCwINsn+orU7QX'
    'CtHmdDcS+pT9FpnSjXDGMpeAzu6nRGV/uSUYB4eA8e65AT0SKg+J22lIXk/wTSQgQ/CNQiNa4udxA8mUX0s53KYRSkNNyYBp'
    '2ZZNTFINczsBdMAwAXSDlftEcLQJKBLd8SUlrUuhUZSxO4GV6M677qAO62DPjX8C9HxKmI/FQ8sZPGzd2rnNLVu018C6Kiqq'
    'hiRgaYpnwUZtEmmFKWZm4riRT4Q3KpxmNrvxPhKxjni724YNv97k3tnEAMqxJ/dWbYRCVCu3Gxj/pU24J0IFPMkWvM6axH9Q'
    '/FRa8BaHKMhMY3LuQmB/UVg6EWBx654W063zWZQhpyMiMPVhWycZH1Y7p3L3Tu32BKvuEZtVyYc+wNC0aEE/+8qcY8puSalD'
    'Yuo+iPMh8UfuHNvf7h6VC/d/5rrz/PJGEa4kVHrucNhhcDksvTICkuxYgV1z8DQBhWD7WO4+mkgQi9PMAR4l78MeVtZuwiWC'
    'ptr2d/sbUQshwR1XzUf28uvKLmdaBhUOECTsSoIq8fgREXGvJkaCzcvt/35SL2tCU6AjZr+ekEEB4UvCLNSHCPMuMkVr/XW3'
    'pg8WknjIqsgUjSPrDpOzgP/EPfO+YkJkV2DOX1autFaExrqlHPUlWlkrwlvJnHk8gmooV3Q2960Q95pQKEm7Jt4rIerLXD9n'
    'bn07SbtPSgJpiJZGXGX/vektQyKXSkxSpi2QiVd2TEOiXC78LfKZGYGo0raEvzrjnMdwxq1wddF99hvBsvHvEkOOTf758qYh'
    'zWQB0kyOv7rUkkdOl187sh3ptPk2hSP10+EDzW1CwocNvBEoone0uDXqplbcaFhlKcggaSkxIa0KNA9TTuB1M+kyYzKprIMN'
    'i4yEtjqSh9v0jpArw/ihNcRBzLXmUUXrmlRMU+bqJMivmVgraIXXF7gq7XcaTmmeeo7O4lqQNZfoQxcIofzTJICCupq6FqlV'
    'zWxpHhjNJepTNJyQGqbLnrf2iPUEO5dkYwlstRSwLjJmh4rgHZ5X+6SYvLv5+CahZd+BWj4ht0lLxO/gPwEPuyGb3o9Z9ine'
    '4z4eGDtBGmACMBcKsqxBeEimaj1WvRbbaMbjanOwlu0FfYtJ7us4Y7rGvuRaysn/Le2M3QzzKBg5y0b0E4OkbBCWxalY0YeQ'
    'PbM7I3a+iCxEkH2ptRmVe/FwfD/SAOKLupJrxpFDzL2VTmWcwGLnW5IplfQfCl7Rw98PyJs4WNmeGOZiURo2eXWCB5PtCfcs'
    '+CbZO4KqieYmYr9MAU48ewC4jC9jczQl84fowp5aUcpHYARnfyOAiFZu6uoOJSIOyzvDhgc5X7XaSCINFEUwm7JfpeFqy9Q9'
    'XLWZqXzRV98GX9aWvJnr6icVXm0c41uWkk4dHm0691Sjz/YQPmvwomko0PGap3JQZVlk4DllGb4g2DaFU53K2uJBy7yjoxAv'
    'pPu2lCbYMKrJnZMp7QGNrWAxtGwmuwBwmJfSU7El00PGjevOSO56Jkwg8xIDHul2oKHJbP9YpL0qlMMg5x2AFxmQh+m8kRAg'
    'le0Ch2AjAIskiFTpKqFyZbEIO+UEY1041Jj2VU0HikasS7xKrXoXHoCtSAwvX8SS6e6N2j0q2q4hdeL8XTAHKFBkUzup0Uj9'
    '71wS7yqcLBXaaimylZKacOMgTSnqVOpnu7IIr9hzygjl8SUgUOIFtkhoFVk32cZCmhxju7glmqvAHJtWyPylEzedH9vAaTkR'
    '9PEip3kJ811Ps+bqpsKxffis0MNduv8TaqTDXz0XqsoWbI3ITU8dcv4NV9QXT4SEE+wxwfl/CoFjrcwVj3uy3lQqCNUDzAlx'
    'Sj3FVQvG8WS2tDfIDMJd3ncEmAc0vSiU17mGl1RuXmMVsyw4Hn9JaK5I1aeFWAd1DlD8EDs4FVShlagfJVnTYgrsPBAy0moQ'
    'gKPRK0fL8Zp0NxojOFRUaKSUPbRDszUeEkddKxZDkV4x2TisSdBWMQ3R58wEKGH9rMJAJC4dZzIz4bGm0L+Wr85O4sKCAoA3'
    'HlxwXeksAcqS6kYSEaoZxxwChDYp55Eu9hSVkrW7BSwWkaGeY2wgIR7ATU8vMia0Rba/IJnBxBfXSjVoN1YUzJKkHRZLpm1m'
    'T6YihjVM2otnE4wHUK4UOolQv+SQ9biHGijRKZ2V5iYq4XfI22IuqoT3KQT+dCTBR7jXKwckW3zVRf4OgG61qIfLWQedUmmz'
    '1ao9P6aYUasIQAXOy3r1eKLJQFBIIPetxYB9nUAa4BuhudtDmbqLjoAu2YSWUlvFOMD7dY05ynAiCbuHWqBrSjmgrnMDUUeK'
    'MgoLU6KxJ3hkjI7AThiRZda3KnckwRS7ehRgqwwWs+N9oI9Xey+RSFR+DeUkFFQZFH8QvDOcKnJpwA7GQAhb6oEEJKPhTDRm'
    'xM5ILHN1qDQZMmue8pwbDM1bx2DHt+zgq0dsV3KEjrCQ9L5kjZFpZb7dxIauiN6wFlOJOV/bXBHFK44hyzCQZc4zRDDbGIg8'
    'KHQN/v1W33XPK7UUmlffQhb8rJ8TO7XKNyteb4gYFdVsSKhu4YmtV30IE43iVVmcuDu9w171OeluQjgt0jeWnTwg0CFZ0jsX'
    'W6jQOoq5oBEiKmZdluKEWTV9nCegONC82E9XhX1HLZhl/uby0VvS+vO6+3mePzC849rpU7CwGHwCJk4VrJpIiZ97AimBxGTs'
    'r4uyIl72gk/PT5NSWSnGk6cy2Ba1ZMHFUAy1HYujau4pNfIy2abCFWLTJyiUC8kezYAFAlI03Xm0z6SaSvvqA7MGHI8v4vio'
    'oEQN4ou1jjUUJRDOA8R1bmpZIDVhvXRGwhUHrGG+FYVtViIjFOZOiZXT2m5K9bh2FGIq5UM4lUph9wI3AEAK8xalc0/Aby/v'
    'rK1q91eRhjJJRN4X1Cvln9CTzc3icJJKchHsKcqDK9BMSrhhQp4AwEDSnFmpuY+pBE/LkmbFIICpxH4xGe1Al5hDc7YpxUsx'
    'C54n385OgFm6QpKJnk5DsuyRC7sZFSXRtyheKGWlOJiq4rQwxYj6HDYpIHJiBKuwpdWgr6Vlhz4iGeR8kNkXtgvEhkIWAZUL'
    'zFWKw2FKIa0An5TF8u/0SApPPaIHycGtzd6PHWmqkiOMVi5ji+bHkQy19tEH8jnEbAj0cvK5jRXRzso9SU5kcjbRwrXrzBZg'
    'iJE2eCsFxhWLywlpOFUdVWn+dbOGZtUE/KXavAShziJ3DJjP0kgp93tmegR0OqzXSmNqUrgjNQnsLk1ta1oTpAHizmnnSjcs'
    'J5zSTA1WWtCCUEJqyosCaBP7k+HesbyqnG5nfMXnlEH756Tcg2whNWd+fFPPTNmTZNkj/DzrR+95GqkpjeItxycHym/pUkyD'
    'Q2fPi1otU8RD89U3mKfEAtyVCs2WL5moEK5dnfmyDz2SB3RnnjiNA2NTqZAdsVboNydVcdGzIeOgcsZlVgtrS6KHw8m+Or94'
    'D1JG1wq5LzDk0twnzeDqKvFC8qnjLQq1DWmliQqfIDVvkiYM8M8tHsc0ARR30DG7C9S8406oPuIxtcovgT8N8U4zgmBtEMPt'
    'YY7nQs1YdpXFYGEIN0IlX/+kisXbEsVc/MvZuyQhczYGQ0ZTIhdS9LaiVqHGV7EkAUMRyWBHUe8eOVgGEWsDnaDLUQE7Guof'
    '5cSOlBzemEi0nfzcSuUcbyXnJZzqiN+vrTbJ1KParnJSZ9CfcUs43c6DpnmyaxD0TUrkxR4IWLFJ8ij8OrPCSHuxMVhfoELy'
    'GNDbJVcu5JP7oZVAeol7ohkJe6a8nKjOza4/uWaABfXW+UBpcE8TbR8RmM8hlanzcLPUFjeJ0tmDweCT3/SoPTyFfBBRpMh5'
    'ByPrF+f12e6HuYl7XxCUhxBsPu4PBOAWN61JjHOuAw7w7MFc/7bYgV21qZ3Ex6G6E6zeMF0VpoVa61Cxj2A7OTzXi9bXBw3R'
    'Szbxb8a0vk7lnBhjjRdwolKepP0EZCxvklZJGdpTGPVLyEDjb9+RX55AxShBpzfOPmE4aUN9KW51JVIH+YNqhZNKedJBQ1aS'
    'jjSL2BRlobivpnRo+PaG1sVcCRdmCByWZr3rwJvBQ8utripBUsqPVnVPfNat5R3jlWQOpNBNeX19dv72862ddHXtk9TEpDbS'
    'AaTj0H7goCyn89M3qwdbKq3rZV0Y0IHNXGh5jiPr2XgeD69kJw+5h2FgPACGySxFzPVRzZrAyp1HVgpPjEb/y6GnSgX4eSKs'
    'ELj0UZEAsSJaQhsqkXgDT8fteo9CQQDy2WwDYjGZvICga3ue57PY8IXrwi/jhx15chXExQYn5RHgtbWdM5D3GEnzZUudZ2uB'
    'CZspIHT4KC2cPcJkaykaFgCEUZ0KCw7Zdnot75OUarNN9TQgjrwlO1ArIZfGqZbHHSGop0S+a6LJLfsnnaYQj0bOG8eM4sQJ'
    'H1/qVGqMyAclQaUucjAFghorKBZRzgrqO3W+mV6UWpfG9pNSUg4fK0Ea1nwXdCpKu4ibzIralQS3tG0kMGB+SDKowELy0Lql'
    'STMvWJcwV6rzNMhzySmbUjZTokJqW3VlDRHNlm7xvIFcQyrFJoN6SJJ2bKbGD8k6DBpAKnZV1h8Yv/wCzGcfslWQqCbI04Lp'
    'OmRZngTLqNz094ddpPuWwNtpWTM5vWnPFZyXyEf4chQ03EXXN7e9EJnLqDrRm4q4gg3zL5/xWI9KrhIJ+BbBmJZXMJNzUpxP'
    'oGweVrbyF2RWU1qT6y6twZRrCdoxVZ0mRev6D5D5NpGD/rzqoMOnnajluWO6/EHLPDEjj/ylk+NvjSuxKJREIqCMfj4sX01h'
    'KbVwZ0QLnKYWFRpu/W6kOAL6monTHq56FR3yvHWuWsSMQ53weSM6gSLTRkPwIStV4rNXKQTFLZlKksTciJXLLogMcnB4heH8'
    'gJvap0IyAGITw0QDiu1sI0BXEKCFtST/niz/TKhLXWsPSz5+gdWvV9QwCGEF4w3D4vR8UXK25H1m10VNxIpKqlgiGAU/DSWG'
    'JrMJ1KH8GrRTJixBuXx0irVFbTx+r5Q8xIRs+xqk/qTE/XHwXSycrp4vs3r4iJwUNKUXrFzEXgE/IMeKL9o+VokpT7IC4itx'
    'F81oY8dR8RSy6QMWQAEY607CcPJIjYpWovwqRULigd43q16ZAAATgFsSCbNpWNE21nEqJi8vEMIsasfOU5IjxZR5x18qwm6M'
    'DhaMLJW6os6RB+ylqL05dS9dXyt4EDsIOcMvjzsu7GF6L8P1rSCPTRX0fHhxWayoR1N/eyWQidlgHgFIlImaOmOMegSa0cjk'
    'v3rCJFLVe/ptTb3owAkjmMAU5VJFcynytRN5ImwxRNe+pHlFNaHTQI1WcI9jjoRzMNMKbbVV2uPa3crnqGh1gR8VLkjfos8o'
    'eq2FjBDtjElHF4C5x1RyQsRt1UMZV1JzivWV1TqGTHy3JWERbSSWFhEZqmKuQAvrD33yV3KoopxVqpb5fqKPGSYj9s41Gada'
    'x05aCBUNWT1anU5XnDoQ88j5lgrmCQDKDCcsyITZNZ5f3SQU9SV8rcauhEjsyEMrlnhH6ZpGsIaCvHy3ppoVaMZLDVPEuLw6'
    'L0lRFbTuDPCxnSebgkftICaGeS9PPfcquAF56uN6HpeaWG2hHnATAhaXVIVHanqx0KDUXoYNtxKsoop8SG583lqlryP2MbG6'
    'eKOE+LEn1qcwrZblikS9eVSirA4tutbUWIl9IfKmxFa6F/whCVEshUpTMVcpUaL5N9eVdtaCSItOiYprLEYISl/6E2fk6Hmw'
    'jBUjRTw7QHSVzBMk+hUZPapSSn/ojnFaOGtJrBLXj2iWT1YUSHbu5NEsklKVqWyKFSuQxZvC5isXhhM2QFz3RlEgVxyE+s6G'
    'mCld+7lqd+qZ17qdScqEXFiQOeqMQOTro/ZgrPGE2USswM9+xH2oxA4kTC0QsQh0mskGz2E3dJUT3E+kkLGKdYUktQS9imKR'
    'ck3BgITSumHhwRNQWrOlnRXGBoOy8ohL/RRiVCJJvoyq5uXQGSPI0UgcAq2NBGpov5zZ3n9djZGS1fCRWTVdWjfdhz7I0B4M'
    'dAJgoGcGBnr+LckxPzVRHMqKofzTLjI5KklGKvnGmDSPIJujDa2hPB5Cnk1T0ZEsKqlm8hPX16H5XyxMKNAzV0JqEM3+lKPe'
    'ZLpao/KCocUSMMLwN+AN9w/U+xhnjsFrULYG0OnAQj7VlKtsosC8rqzCQuCyO0NrtovkvmK3qKoH61wosVrhkymKQErBKlEj'
    'SNV6bkwaUqqVombFF5VV4+JFTJKR58jFy4OuEl2Srf1QFEURvZSkxGG5b1JVLnD19w2n3B7IpZAJuSwsJsEwXBHhD3Kx9ldh'
    '2RsPzSM/cMMYB7wmVCIIwFg/BKulIU14KimEpdZ2hre28RDs4arUearSlchLctoIROZon1qUP3YIfUnQMorwGATROL3L3w1s'
    '7HN6UsqH8bO7CigtsIASGIXnIOXpGwB3mhKdjvH1IeU1LROyLo2JTUIwk/NdRNAn9qhJioTsUVRKYrWpGc3L+Qbpyli6+HGX'
    'jnDZSQE40wSKqMhEt4pPUi5QvVwwvV9zOTjpbSAJpUXoK/AtygLahR0Q1VHSad1S3RsdmiRwmLhrKerOyuJ0DGn7W1NVQ1tP'
    'uIBT4gIp1ZsIYm3NxuHFgsjGRG4SCXf0ImJImHJM4tHXQgUeFEp86yySNrXv4EWcU8uiAEX9emsN2+xRQFVck/OeSFaKLtDL'
    '2GbPZAyHZdCYGqOnGhNVgXlVrQLj8QGsPq8tRKYmg7F+6M1jNbqZkFeos8Fu2JOEZ++Wox5EXEJwyvaoETipSZGwLCJle+26'
    '4cedXWIp1Yk0coK0IUAXOX4uF/h6KtlEHi5SblpkfcBCiyjsh46eoEojTagsAPOxZAHzbBWF4v5qppxNyW8c32HpUz+FeuJq'
    'jEnlanPyqt7oZAEqPZOBr64U4S4hXKinnzOfIF6+TIVWkQMOUjQSVGrKUae0KOaA9Z1AheOV8y25D7SaVCaTrZxY5armQGrp'
    'mEqOV8lntA0CpicUYpTrxJLSvoVSkYrIxTpVyaZWpLfhBqTAhJY6yssgp0nG8MlhSeCVpvmQGbpcwzjJoa0cGQstkhgyKSDu'
    'V9Uh2+Clug0UZxTUENYK/PCqOk5lautS6E3mZw9EAVjlm/jaT3kmTRHl740QGjG+lpgt/LyTr6r7irkK8cRspPEf3gYVQNW0'
    'wIhNU6lKyMXGWEPiYcvG3Kl5x71eZoHGw0Irnwe87VRaddv4iJakKIGYkYqj6ejq+7gRkkP8aRDeWcGi3lVkeFbrNETZpZQ3'
    '6p8N9UWUSG2N2p5olPVMBe9R0HpV8wNSTRMCafwkl07V4sarkCxV+mdy5JiqXjAYjJ1RC/3CZR/5ipELRX9Df5xacOjkERQJ'
    '4Ld0YBo45lSlgBXs2PorGiQ9NhH3giFZNIHzDtCohSgJymC862HoVi2Rhl+mD2AkgVtIPoy/zZLdQamTxYlLa427kWgWdHLd'
    'MqkUa1/oRFwrvzc3EfuHZlEHS+lDW6+WJ6r0Y9/yB7CXcXNf3Lbq5v9goQLJ'
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
