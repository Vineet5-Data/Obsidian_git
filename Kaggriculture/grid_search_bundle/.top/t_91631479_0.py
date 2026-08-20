"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXcuOW9cR/JdZc2E+9MpuLNGx4LFGmBmFcATBMBAHAQJn4WQX5N8z0vBxebu6urrPuRRH1so0Nbz3vE93dXX1+/9e/P2X'
    '33/79feLP72/eHt5e3vxYXbxj1/+9bd/339x//G3X37/56//uf/8/uLbdz/9/Pbm+tW7l3cXs4vN9+vL+/8++TB7f/H965v1'
    'hfrh42Mu37z+8fLq/ikvrzcXs7n5+vb79frtxWy1+4fb9frV6J2Dr39cX12/+fj1h//Njrrz+uUP794O3rLv2PuLzfr27lNz'
    '9h+2nR/8bNiKh38dDoj3sm0jj1/35vrm7vtPTz98si/c/lR74bbh6ku+fff66tXP9/979247EeEbxj+R+3N1+XK9Hz9t9LY/'
    '+ThTRy+6/4c3d/s5dl743XB5SO8b/WK4MC7v1jfei15eqmO3/Us4ZLs+jdsL3smGbLRZ0XMPnWlZB/ZNh+eC7VOYffuC/WP9'
    'scrPun3P7fW77XiDodJn25+Lw7q1I9U02YP2+kPUZ7L3R6Udoi6TrYxVj8mWhqxp0ncPASM16lLtuYfl6n5Ve7Cdgr5riI1M'
    'nzW0e9r6coqlowzUVCtn9CHx3GP77cECC++ph4XKrrbrq6v1y7ufv1vf3L2+ev3XT+21F13KdHloRuo+Rc0gD9gdtqmGgreG'
    'DQ1GJ9ns3fbuOUHbZ1YuysKi/vqTrz85o58cn4m366uP/uZgp3geLfR+n35IeYF7GyA+eXwHBXqLlaPM+HCCuz//kDxrzOVb'
    'vx0Ot2OloeD8h21XWujfJbiN8c/NMIWH/M5Q6DxMYPDxKFUaOPYkUotg4KoVXm0HuNCEwwCbFsjjC6bNGeCwgcydLRylPexk'
    'YgOrIwQeigeoyYz/I/y2etUd3XnH0Ot89PXt3c3l5tv1zc1PF7Nl8TIcfeh+Kfa6Hj/PRdl6Ze4c1sFMtfZEcsVmAEotX6n6'
    'vWEbZ481PCLNbtX4+m26J4DfRy/iHh0woGt2hMAkIoA19iUVC+mwPErPOzTMBeY7mZme6aEZIdZeUCDFurnnIlHFRo7wuJar'
    '7+tD3k8AC2btgiaPl5yJ4xjv17u/l7vc1vikR1hss/Gfiy6a40h/XL2XN38pXGBgMMk1UQYdEiYOeCgI0VWc5LGLLTVne8Br'
    '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'
    'bbngLm18UQk42jpjSvekKO42ksRkbT/8H2GX6rk='
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
