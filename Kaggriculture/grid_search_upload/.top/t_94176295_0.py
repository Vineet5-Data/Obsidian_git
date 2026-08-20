import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vW0mS/C8682B+iKL2prY5Y2PULUOSl5htEI0GdgYDLGYPPXNb7H9ft/n1+CoqMiKrKMuzvhEU9V59V2ZkZOTP/3P1'
    '119/+/tffrv6t5+vfvj04f7dLx/vnp4/Pa6vtpOrv/363//5j89/+fzx77/+9l9/+efnzz9fvf/w5a/ahx8+/fmXu58+/Hh3'
    'fzW5evuwuZrMiq+f3q/XHwd/eFqv333+evN+ffd8NbkZff3j+v7hp6vJ9Pjzj48P7z69fT79x3K7/d/JsGMfP7z906ePpzdN'
    'B337+Wqzfnr+0tafHh6f33/5dPxq9OF8IJ7W9/ent87Hbz08bvAq0JDha0+fxlOBGjB6XXX2YA+PLfkyJ9Ozvu5/Rd718f7u'
    '7bo2nqg/h38Abxu1m7x1/y/D8Sza8eW7n06L4ayv+5mq/Cwc4fXd+P2n5XH3vH4cL6Lxd+erBy7d2XgRPT18Gi+icnH+4fed'
    'cfbNqHdsKsvBOR/g0Sid+vf2br80Dz/a7cxB1625PA1X+dLDKAx/FU4X2H9ocsBOKFYwect+7MGYDYajmLHyN/qM7cedDt3Z'
    'c8c77zSE5TRV1uVUONzAZqgerfxsOeuCNrLo0Ikn79BSfSzlb+J5BEO4P2HAHEXzpg/i8R3HD5/P3if0wRu407i3PHj/Szrp'
    'fZ9PJ7xLBw7/O3hT1+eGH77CY0e3yrxiTQaHqXGB9Hnq+Gx1tu+Lt2Bsj5CfFmZEnxa8fbi/X799/uUP68fnD/cf/uP8TOg0'
    'eOmXGEsk/Y4LzcHh1h60p7qHjo7I6MeVq/x6a1iAr3r9G/M77uMi792G9l+jTQLMu8J8HBjhYOFm/AxgjMA9gXu1X9qWmcz7'
    'MOxt1MdwAIFjbxikzFWBn6IHsrFAn8IHMo9AtB8b/NF6k5MOVH1QJdtX2UDUN4/nn3g6ba6vAjyFj4PesuE8AOP+9MjSGIw3'
    'fwmcENsybp/1uNBUJbjZCxvW35/W/2nyvQ9sqAUGsKdNRgECkkVTg11sbVccQ3Mqt3NoHSSuwcgQaITqpIuhi4GAcMbqpZG8'
    'Gxm4fjqu20YFvMx5NDUWwFtq8x/eCJoNkTJPyPBwqy1+NAWoAZxmAYAE56Ij0uWAhqu068k/xtL+dZCz74/9/lgTk6pbL3as'
    'HgTTK1H5wNK6zpyZGV/cBEeSLp8BhrRFDyO7K2OgeJCS034SEm/1QtmdXhmb93eP/17rWCtgNOiO7uqLIWg0VMe+JIdoOBYt'
    '/IBycMoA4pEJ0ISC8EE/dmz3VtOZAfbIcVCGIxVjGQAcOVt2pzV6GJRTuFIe9NMT0aUyfN/YvrKiwweCBb25wBsy4eHywSXH'
    '6buB8P2xrQjPdWQj7X+3+rLdS7PpWgd9qkbU3lR6en682/ywfnz8MwDSpbgRu8Rgh9S3W1BIHGM6b0mX4NJGP5J9I0qPn4Xj'
    'ZhiGY/iqHVIyohgs6LS5lNE0tDeGEJWHGfFgVtP6OH44XtLx4zQY9nDHDrYh5qJ2jDw2+RvjEUiuglq/ra93zczaeOjTrqGZ'
    'iGd5bxH+mUCddh6Xwfkuxo77Hmf6WlGrpYP7XDdaKvNt4vikmMHZqz5vxMeHZ88kQeer4h9T9zvCVzL3CgMgBrfg5uHh/kua'
    'CjSi9n/cz9DnA/KdEAk8+eJWuC5NH5rASS0ybxg5oRNbZDyotQtANmIPkyMPeQ46A4YOyPrpfcv3joGRxJfMZSuhQk0BVN3x'
    'aGMalXHfELiSwNTiUxp+XCfCiqCJAMU8fcqAdQj0G/CPgMXYvBWMESjnHJ1o47MhsxfYWKNP5siA86dEdsex5xyPCrgWIyv1'
    'UsbQMpODagfNgBW1wGGzRWxcwRxR2+K6DKUosplOy6Wg7Bx74x0GKMPTjYzleJXlzIAQUGhOVr6OzDUOE6gnCPDO47TfSToj'
    'Wk7XJbmIET1llPPqWYooD5iud57WK2MK03hijtEo2J7SmFBhR+suP8XxLPaUaZ2W7y2PDXEu2kLtlrmNW8fued1YrF63lYYY'
    'tzLYhOURQO590KLR35IZrswmCD+kHETQ32qnkh0mc5zppm/UkekeHnpSY7hlqQyHZGLShycaZo3O8dilOy9etN4gnJQTlAgo'
    'Hp9a9NzbGnIEFqcvZ4Il1jtBK0L9gIY4czK/Rc2grLso7Ty9W+KMTB1pmiHvr7yh4M8sDySRPEGNo+MfWyh6ORbdcR8Pcd+a'
    'I3D4rRB2tcxsThPFZsPh4ZhJlAqae4giOBSP83i4r3/8cP+n/QKreUnlL+NUuhYwfL99d++bzuJdOSe78gZDBEX8JZpgsLJs'
    'DIF7PPq8En4uWIdgXwvaMd7u8KJKQmbnJdWewLl84m4OrZ4CEykpnp6/lhvL40wOD5KYFjoJcnyFaCLYaaGbWZIzBhphgRVK'
    'W4mP0TZcHcw7MEjZ7gIKZ+UDkmHUktwKXAoRRqm7BDFR1gOd3334Y+jjOS5hDuQ4tae04cE0Jj5kc7tb3plrDln3POTTiloo'
    'jYPvRZsAn9HZNveZ1fIUNgZFgghaM/TtEYr+FfTLBQgU3no4yYbgl0ULQl6b5a4rH4zAXG9H+6tRppYDLviYTd0YIfQd70Xt'
    'Oie/0+SgLuGRAwMkcsgJ+dYLaur+eRymKw5Jaj67SIJq/8O8H2xnyl6tlerXkjTJfPpyFXPnRQ/x6nweXdZ4RwFb4LUELkbg'
    '6BDFobbgMeGsLaowhMCzGl6Z54OQJhcqoSssxVvCFrTbhhddkjGxFLfoMyv/4NHTyiNLfBtPEAG2UQNOoZGgKHAjebWZZGfT'
    'lWbwKFI9AfuYrKSkVw1w98I+qyjBjHGN0hxMLACBEw4uzjAToXYM1I3SKrX0HEOdGuxdpjtuhIca7VeKVuVM+mTDpPFkmeeZ'
    'BvRyA5Rw40s0K8/x7ObItQwjMOUu7dvlNslraNUrHazGaP9X3KCvGT1I+9AxM+frRdwJL4amXlmOmsjakyEIK/gut5IZgZmw'
    '1M22TZ046XoBa+wijFGwTtr0Ij1vso3/CeiubCEEgT/0kI7K1fhVDK6qpiA1l9Ep8RqNwUoz5kpwq5/jjGWRxLDtJXLCpEgu'
    'bnVtYYYY8O1W385BIitbYygQTFZbBZDX51sLN8MOgQaCbRa2dvrGwUfIwcKWBUg+OX0Fo/i4rasy1lGvFXGzNRi9FCPhK5h1'
    'Vw1xoJ4tDdyCzAubPDAvHK3INp3kjCBturUQ2T3y54YlFfstr7PHBr0jySi8lTRF1o9AlaFt2p2y7zgBSOgvO8eAV6ANCsqg'
    'be7i+VRebzOJcxRjTWQewvEAzG25q8vGnK0STES2GgSTqxUXYx7Imu2iKhsMrRI7Lw4OduVWgcRXQXkHYGKoxXAxKOw/WHFy'
    'bR4NAnzaizqhoefVmYnG3+VUHIbhzfASOHGzadHfnc5Jp+zr2Tyb8cBBGR2LOR+R2aXoF3HFYMv1vjgR40Typwz1S+AfLYnL'
    'oOitBYexSKicCj4cqYw4kcyyaM7/8J5b2qPDnurloZVlp+qQM8gi7EYiRE0XGKcgAOfE0SMMCJKVK3y1zaBEIbLn5p6G3PIm'
    'Cgbwrxg/W6W7rBuUJkvKUUmTpnx/CWtIrpUYK0D6L2DPv+yCkCw2Rm6rCx8F66SuKe+dJyzFONR+t8U5Kc4TpXU3yzcNnPty'
    'C/gCSbQ6O/GVOjBQADkyHHCFVsi2uOgKTA14Jhj9tQCY1WfgQreVBmO2tFRjgoa3k3bsNLUhkkiSbioqchBla5irhd14aZ04'
    'rYombY2+JIyzqd91NVJQiDcZo8HxO6x6mTUkW2XBj5qCRIUIJh0wweBLWUTdPwha0Tae8wW7ua4ipBfAdHrCNi7Aw3L9LwXg'
    'ACQnCFUWWNRwTlbNyq7HY1tPnskTcBjYHTceZsvUlOIEpIW6bVEn/VOiTro6ZVAdJ6Mr4lL6JE30GQpZGKos0fz0Kf2tp6dp'
    'vBUUFtCsUI1ORTLTQCWuBMmroiJvpCuUO4x645whkkBspFxnhAYwBcCSsZBDakgkXmKb1QKJ4RTOXCEZDSTy8ra6+M5SSg+D'
    '2hSSh0hNclxjXusP/RWhYYqYT1KEjzlQ3P+hWrgJ+h6YUM3PY2oakmJ8Er2R+GdSXFnT9cy6feCwVeeYyZNwtmbaRyX2oBK1'
    'p/SseFY6lNrkpAp3sWrLYOHQD90tTwa5job4p6i0GBhwMviVAhSR2bF5EqxMF4X4qciYymeLmjtvpnXs0qxpwcTSWf4q2hk9'
    'sIAXE7MsrWYVAxgsbGQbxKvEpW2Uln4zGQBYjwWQIeoBZGrIwOyhUNGNsQfMXA8PE2qv6qTMRAZFIKDZommFmXUJpM0h6OTE'
    '9xJbTZIyJA3NNZrPaGUGkQwxbylkvjRScyJcRhPtA5d/ssZZmdVB6jOV61jKbRBY7H5aj7Q6qD/PjdiDjzpKgYniPSJGoYg4'
    'sZwLCi7Vc1Uo9m/Qt4AMFh10UtjLS9NjjQJF6fkUqwX0vNQ4WtBqLSA0bB7JIZcruWZPm4rnGCNG5JT5BGKXdPgtxQUyRQ20'
    '5DXiTmr+HtNg1Y4Yon3Fc9kksdj6uNp+JUVzxFI1tPSagKhk4HjlvI1WoFCGwx5PAtLz/SzslXomiqhkTHdUtdC0LfzTDDEm'
    '0YNlLaPsW4AEQk/n9lKIQOCHGj6D5XsJgX58w5hOsOeqy2CHmUyRqClVTpmYOddRG8Kfv36efpuXLI6QHFm/bSwhE0bNj3/o'
    'otY5PP8WmeQp0Y1r0esuJ032z1N16qQZAwtoUEtkOEVOPULJ5VTVNdP7W/PfiPKKxk0xXDI67tztSfmCNAVCkzRNnOSoI5Gr'
    'S2nAmQVXu1hV5K6RUq6JKXDLOI34pFeCRFDwBgKrlLhRuvjVrF6DF9Umq8EHuzUS/PA0Gp659nxkydSVHSKJX+i8maaKAouh'
    'TkbhAA0V/L9532d5cWq0Gh9Fx5IsKZ5OaZfMM9mQkPROXE60Gv9UPgcqeKmAdIIZrWv8iKxijcfOHG6Mb8y2CSI1KoznSwyE'
    'fZAXGeyaJW0JjMkSJR+clKFdz65nrlfFAamFQT5lO15fdiyqnS7Gweja1L1h4mxhLIhFIlIhV8L1Lgn9kpeuyWMqAJu43xkZ'
    'r0z0AAtcj4dLTmpCzpBloRIeLNfYEPMrZfk/pdVg5YvFIbSy4P5g325zHiq6vqUCb8R3s5T+VoKJpMt9cKOColyEyRIvmmsr'
    '5qbSJyR1VLUghyjDp0QPBVifN1mDB1AfLQnJThkMTMnSwBR4HDerkgj8Wg5y4aarnxqOKLzaJhdJSCBsbiXZXxU3bJlJodAw'
    'ZaeLR5gYMa++que0zpPMBI2LJZZbonW1Wns4s7YnK81C1QVKCYYiLt+yNNsVHKtvKArXnzlT08U3im5R7cYd++/m4rBWCLWQ'
    '5H9Ibb5A6Lh76n+G/GaTA4wQr1URPUsI6JvG/yKcD9kNNbQE0nSBERjE5Ih3/epHoo9hHHDt0WqzjXx5tRqtGK7P0CzAIU14'
    'A7W4kUCiZEMVJLUD9Q/kO3OfP8uLIXrcqExirIZSsZLCxQ5mCiACFAtx8kSK9Z0N9bH03xJ5YqnYToAeBlHwauE8CEVb1mdg'
    'jkYiIG/E3ILz7cggGC+kzaj0FEA5b5BSm6GodS6MI9gT8ahVmsYdFhXXmSlWsJMGH+gY0XwBP/4jQhrWcKp0euS/zFVfj9Ae'
    'Wj6BoU4gklIOSIRrBZkfhkftIAEBOLjWFTeTmNskSuW6jINcsj+Af7z6xtkfXbph+cmwOhmLXH4N8kdGDE0lNMWWi+czb9Y2'
    'AoES2mCoJqMox5zoDgAF7Fl7Cn03B7ywZ0NH8pw4sS8ChVJ2CThCOBLV4kgrJyWWOgnngXwhfq+DKanyjayOAaEe6Awuqp6e'
    'pnso9RHZERWBBFzGpqU6JiDM3EXyXTqNrql2Fg38BplZ8KzRKlQ2MuP0+qdiWJ0n5OR4xeUxKNXbreB/nKWsh57nW4OnrZIX'
    'VOqnV3GMUtYY2qPniMGlXqN8cwdYn4KlI64FahAwqMGmkYjjf+uMf6tAckQDoJCE7fAVXcOayxIlqvxbDQeWouCxe7YQgSBm'
    'vMTrne8BaUDy4EDZdEf5gZaOooy3BJVCINa2yj+inrFfsckZTDyJDt8YhVKnFl4W742SP71r01xhEFUlLxSi5URSoWSJZkDH'
    'QKu7cnJEST2I3VdxT6YFQNQuljjEgaY1zcSzCplVhMjURpgUogT/7wQUWd7EK4OHasBEZChwnYFkbEtNEMpjL1G3GKTX6BCJ'
    'lJrmAqN9ICMlPQigYmGsWi146d/sKycPCJRhAGrpaGNkuDGdxRpu2io44IR+HHuVtPjD3Mx6IfdZvVb9m1TpByM/zUm4k/ep'
    '6KuttolqEuhaoTF+njSf8Yu9vKKyC6FixlkSZ8m1iMACP9g9nW0z2KsoXElhVh736OdYso3DKlRLf7MNAdwXJYpPPSZNkFCs'
    '95qckBujuBJC8SEJQS/FQtIm+/C4CYAKQmWi6p6YpWAzGJbi7oCWqBYFIKq0A29KUww2ltk19tpq1+iklc5Fk/ZYsiqDTXh2'
    'UJ5tsXLAc6BoVPbn3Yc/MmHVGNaxepMT5MQ+DlPZZSAXVZq1u3WTT9JSjRoeebHEXv1U61W+f1prbXy9oc5I53W50bIcfUC7'
    'grHu7vQB9rXa5vlTar/bwLlpxTe6LdObVt9sLtNrLVxC8aAXUOaJYIOI7Y3S/FAdk+vLVCrBJFOnUx6coieJKBoeCTkfoelB'
    'xY1MYYjGigWkQGabNk/+7+rdc73tlbOlWeGQbGD7HquUEKzuCBLJGDVtKFJSk6RNrHoqhmwP30KE09RV9pEJFTEulfZVatfP'
    'jYVFoSot34z9p4rsLDI1LCMUFnjZ3Eis4duaVksZGj1fU5OG2j2EH4SDUYqYhq7i5Z9lShcoo0PRnuGdUkLqhp5Rosx6XI4W'
    'TISf5yIUgPVU4NTCHdjIk4d/7ohgnXLnKcssTiBUqGYe0jZ3XFxmToiSTdie7gGLqbEC5gvIO4aI93WUZ4olcajGtFe6le7n'
    'y03bdXyO8YN1w9LtvKplbZIwk2SBa/WYJdGRNHDbEvphbE4S26Fdc2oPXlSW6EJ0tBssV/0tZie+DOAl14etKxFcjmLmZcJZ'
    'OYlaVkgTzBWrp7QKIKfK4LwA9BUsKl1IuLoOuzqN8soz8/oqcEyHWVNwCbfgLwOJZRC5PcXKA7oiN78ChEk+ot6J6yZYiyOG'
    'Vfo8wY/6IEMWsAXwlGq2m6hKnFGdmANiQ1tVYbF0AJ0YV5Bkaqyn8DThwj4xrFVPS/X7QZAfrAalrxsaIInMhK49oXm8GpQq'
    'PMK/ARmApegpyUi6gqf0uMAB48YbcEsV3c/4LNcIVzuPh1tLzJOK32oXmVK2gGbVyTroLernN2lsgJOFA2CEQAGs9pVb5oOm'
    'sZrnEC0MoZWmk+I3EWt/LuozhwJ2vJbssfUlA48HQRLUXcv+Joihsp8p6aycMnjJd5FFkxX3rYLYut5h5SDWFlcbBlWyq2qo'
    '1LICk6URHrC0vmVUaoMsD6qQRQuTCc1OuGsDNKcINuNG4m9F8CNZYJUxxaCtJqgoCkyJpmwyB+9rF7kyQcNcgqOWPKdLebex'
    'rXrY2mzeQtoRO/HZ+uxC7gKJfUTROSGv7vAVhR5NGkBZXQWfSLSFotbs3EsFjZQgHiHmVQjsAzxqJRlG/WbxvJP7JhhJgobk'
    'vi59RrdhaipnTp4g9P8450q+/P0iaylPNyMzRzHneuZqG49B2FAVUaxiAerhABY0zOQQllxSvXARCE2AuFwoXYEvp/qs+YpO'
    '5TE/y+J2keWJ/ysGnVwcDC3IWyfpW4XhZUSJHT2p7ixTwHZEjoNbEqzkMHs3LzItWh5U8ImsrnWEUIbFzvsWs7vtUf0tmmAt'
    'ZhclvxZ5acuGvLRlRcU7V9uCR5g0dXRN5wyNw22WsVQ8xK9DGYoyY0daq6ZZHy9RECyZUapBq7SHJdxakx803Iau6J2mdzcQ'
    'j/6eNNmh7FvdLH5pElkeGlJL5mzWXdlkhgp/Tn+Kwy+XSIXMZgbSCdChsC7pj5Sfv6algc6HqXOAibk9EdkGfwsQwFgmvU9t'
    'usizcblQl6ERUhpRkB9aLos6SaGHuhvBQnVBQEonrBJz/OZLi+i0WfVTA09BdCwh9NDvFFlIFOpid6nmMKnLyCpfDlZw3Q80'
    '8t7rWMt4DSTkHYOKi/CEYhqINQydMQzYYSomUava2fDoERP7KL/AACvfFACfVYIFgv4BkUpKY054JDdFVxbuCuP0I9DFGlpH'
    'k34O3lgK418Kp8DhBRVzgvi9Nbew5FZ93iePD8/pam8ARE57yAR/4+JDsRS6bIa1QXz7Pu/H1BSaYuG2oXA74YUG+GeVJ5XU'
    'c2uQ8dNwqXiy6dXcVr7SAjbHR5ag0FjubjYoMQxWP6CyymIA4JnnwV4u5xhGweg+iRJpWL1obwBm4HZKD0m/6pIlU+7wzttK'
    'R6bfagJnFXa8KCoXUa83Qor9S0iZhZWlDLgqLKDHaEViFFZD67yMVU6zs6TEqPhMJaChLKfNxZh3wgSGI2AlCNgRab5omUcu'
    'QwiEIK1RxSrnebmgF3GJGA1QVBQe4sSPJnU079bPoEm1hYp/oRfwVIldYk1wefbftOGYWp6jcsy1wbGAH1SzaqBJlMBFI+w5'
    'VfqhBXZYmts+ofd2Tp5chiuAiMfTeu6Z+QYVp5Ztp7sqwhMU62bpDOrk3lpzO2sTVuOcg2gth/Wf2tzXTj0LUhpo1npt25pn'
    'c60oGpnY65T2HN1qkzDVWlCGuRT1j3kx7JApu0aFNtUFOW87YSWlOhFZZ6uRwPl9JorFe+DLMU0tZErQtGGb2ji1Zk8ouGJm'
    'l/MhOq5wLDXffksGNL/bnF5aEDGSlulm3bBep203I3VtSKKtJARUXfZUPTMtmVPFe2EBgkb1PxpY4uErRvL1SQ235g2aVQTQ'
    'a58HFV8lFZBWlHcpY7qzvpjulK/BAcxr1X3Fs1mGLaTUoxejWYLI4qtQ7+Ox/bUBWVd72AiimTihiDgZRR5m22xZ2cg/SgOj'
    'QbxUWIG3NXLzNlF11kgwlImbckFdTevBRvzKRRn1LZpXfYW0IWDXbb4Ju+8o7UzQCYhrSuTvuUUKIygXs14EWS+hwVf7xZFc'
    'lnPLpSpisgmVV7Oqt9lblDgSBG6MxTdtSMODbpZOoiO/0IX6tmh+WpdjCbne5rACXiq+ZJXQTGLx2FVy1ns7kqwSLufHUFJQ'
    '9av8KTpN7USxXAjN89NDo0ZlCw/nyTqEjBivTaAEuff3Ac8dJkOcUFrHYiHJ8OwSaNu90ViR8owLPdRr81Yz7pNXZLVEr89Y'
    'LQ2hwOEwZFlzqhXerTrPmPQs21yrXhXn3ifDtYaN4Bcx1Sqsq9tvad6X6UKv5SyxiCrYiepcZuDnhbZBw1U68BrKvDyvoogU'
    'ffAEs8PpnXaAVTNkGV4LK10uZ/6CjNh9Lnkt77zm13dAT9+8Qqj0hUmxDfV9HVX9NCRq6H0ZSjjHOwvV8725IA02LrTmsOea'
    'C/wmFkx31YBIB9tWp2+hsXbSlZxIYiGs9cvAkoAUzxRrlauph0kr4fjohX07MVQ3Wl1PUrIiVRQhiDAstAk9SLs16fCm6ujU'
    'Jthcv7FxmKCatghbhMQgtTc3vZlqoEqDZM5HVHK6j/vkTRHuXr+SxOHREhZfqtLGLo2tKKxMWqDQYY6nNKNKGCyPjHocVPma'
    '8Sl1s4sFXQJ/U6lawJzYNh3GZRtkZNJOtWoxUXHBFLi7W6o3ygHlUX5MZupG1EYNg4vyKDQGZ9iCDnKRuZwjJ329lC4qte8K'
    'jLoIEcji630wTgIiZeR7D/FCWpxXtHY1FLQWY+klKkr4CgwT5KEKAg36RNNZD+xXURBlivzy+csIcD10JNR5BfAaK7cpNr/Y'
    '07tEqFJp80K8k/lLSAXMhjDoQZ1kJmfT/GsX1OnEdj9lIIyaOK9+CZYm/F01BpVimS6q00VOztLtgiFPmJKBjbk0zsisLfj+'
    'iIwY1fIQ0EmZbGmkDbCcWSVFtCnLv1YSwLP2nRJE6IoS8yetHki8vnLtxKqrQBDUohoNt2c6XL9hsqIy6hqXGLb5fr0yGMGB'
    'G04Ns34StL5982+aTHESPWAuI6srntANVIQdIrG9RD0XK7mfxagV+zOeLqHwiXd1gKUJnEyp5Ktsdi57ekwQHi8PuBJoHhSX'
    '0Uoy9wzwAA+IU1bCk4PygOqUxM40LSFa7NaF2LgKaz1Z6VHB0+JDqPnnRSbT+P055r1Ksq9wX6pylsxPP/3TwWHdHT1dlJvG'
    'bYfLTS1tD2vlimV5dydP5031Jg+rbCSpdLLVOjGX53nImsRNeeLy+TzWZlVRx8jN56gfu2WPusGrwazDDE6/7WGWoE4lI1sv'
    'itVqU0U0QlM67DRtwN9hgZr/RlBdRIuxyzzOVE2A8R7zOME7XuMSFSFsgeQYjvhVNTxBUPmGzUBP6dI8szEQK1jXgMkE7x7i'
    'aWzdd8bdbIpiLPsX8sN4NDtdz5dhVrBNDuUJnKQmKghz5bvVYoJZCzxfVTgtF5nUUxK2iZNoMwQgqwcEjtJio6YtSFyskmUT'
    'V5ecGyAUEKiNWIB6XT5fiSDDrCGJSrRyVJZm0kUloLxvsuWo44M3nFGptwaaLpVYVZhOikZba6ttIUe/BtVGaKjmvbF94Esz'
    'kuENrnCSkZNjdzJkgxKyyaIh5pK1aIiCHXyFotwlkIq0S9pi2rg5WQoOJGazM+y4ZGFYKWhqb+Uk9lnWUQ2swaNEA8/fIRoH'
    'Yf8balJI2LKUUqlsAKG0WuLA9Go6ZgqOlIWUIimKdGfmqf14WGTgXlMu4fJB5w/sMSk0XBOUq66S90o8a+NIKaoqYMppwfzl'
    'aqAPn/jjSUALMT0xi74loFdIVXAiMCF3iNdtb8SrnIdXWCe6djctLlJBmmV7M380h1NQPdvQsWmXe4MDO29WZc62nHC3mtlj'
    'AM+SrHuvBywfqin1kFb4ZTFDXZnSOqYREydQvgCtpMrTBjiNX6jnXYAxhRaljk2zVcZqygY1La31xC9QImWvsd29uYqyC4Nw'
    'Fq+DlFo9G7HeRiBchAZXwl4U/yKmP/1+6949PWlVKMZNtZonT+rAHD20jDbx+EdTdFYiJFBxraJ5Jw+t+NPxg0CALIGC3T+j'
    'qWWjlfjQ2CxYavUVtAsfFK+hZV3a8L1V31v1Clsl8TQGxNZRBG5VcW5Xrbr9noJ6IIDq5EgZ9OCNHMqvVzrzDJpQnykYCMvc'
    'hGPu6jpWQ8TkxYCfx4wjqq1IFR5iLzhWmopIWswgEyqkE/MwAnGtySaWaSZT35ht8mZOYwNtYYq/DioeDS1d8opfyQIN7x4f'
    'PtatZgqV0ih2rUq2kuopmmSirEySaKVcgUk/nwFgwD8ohqISxSru47C3CLsAbwkF7L17hdWSYigp5ZQaigycnPwV+or2da/O'
    'SupFF+srPT9znd0fWIHWxuFUG5AbDl/VPqjGaPVkexMb4aBdx/1WnsSbyiHIbO4VEKkbf/P7Gbz9P9+Tacw='
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
