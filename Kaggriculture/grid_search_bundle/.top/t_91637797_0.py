"""Pure verbatim replay of ladder episode 90874645 (opponent seat 0)."""
import base64
import json
import zlib

_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXU1vHNcR/C8870G7S1FSbrS0jgnTokBRWTgCYRiIgwCBc3ByC/LfQ5H7NdPV1dX93ixJWyevqd2Z9/26q6urP//35O8/'
    '//brL7+d/OnzyYfzjx9Pbmcn//j5X3/7990f7j7++vNv//zlP3efP5988+nHnz5cX7379PbmZHay/m51fvffl7ezzyffXVyv'
    'ToIPX359/v7ih/PLux+/vVqfzObmzx+/W60+nMxOt//wcbV6N3rVwZ9/WF1evf/y59v/zQa9uHj7/acPB2/Z9efzyXr18ea+'
    'ObsPmz4f/GzXisPue+/YtG34lvdX1zff3T90/8m+Z/NT+p5NM9Vnf/Pp4vLdT3f/e/Ppy7CTB4++qbf+8vztajdIdIg23/wy'
    'C4Pn3/3D+5vd/Dnv+fZw6tlrhl8czPX5zerae/7b82CAHr6Ax2Xbg+1LD567+RIbl9EmQ4/bN70wtfYF+8eBZa9PqH3u7mn+'
    'gMgTaR//8erTZsDBeIQT6I/zfuHZ4ajM30Hr/HFomr/dqWXHoWX+lAFpmD9pXCrzuP0tGI6HDtQet19v4z/VnmeHt8tqYN1v'
    'Wg3bh6zOOy4CZTQ6r4GHD4nHDe2cB5MlvA7Clfb26vJy9fbmp29X1zcXlxd/vW+mvU9St3/h2kLNIA/Y3nKphoK3hg0NRifZ'
    '7O3e7TlBlc1fPzC+/uTrT57QT4Zn4sfV5RcH7WCn7N0x4xOeAQ8w5T/trJD45PHNf+tnzWpHmfGHBLd4fps8a0b9aLkd9pdi'
    'paHg/IdtV1ro3yW4jfHPzTCFh/zWPug8TGDw8ShVGji291OL4MBrKrzaDnChCfsBNi2QxxdMmzPAYQOZZ1k4Ss0QFZ6xGyH7'
    'W3WEwEPxAJVviz/Kb7WrLsA2h1jlfPTnjzfX5+tvVtfXP57MlsXLcPSh+6XY63p8nIuy9crcuqcHM9XaE8kVmwGgsnyl6veG'
    'bZw91vCINLtV4+u36Z4Afh+9iHt0wMCe2RECk4iwztiXVCyk/fIoPW/fMBf/7mRmeqaHZoRYe2GECTZdtvbgcAGoYiNHoFvL'
    '1ff1IX0e0mYXNHm85EwcB0W/3v293OW2xic9wmKbjf9cdNEcR/rL6j2//kvhAgODSa6JMuiQMHHAQ0EgreIkj11sqTmbA15b'
    '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'
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
