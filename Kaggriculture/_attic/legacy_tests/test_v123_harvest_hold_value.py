"""Focused checks for v123's only behavioral change.

v123 replaces v122's hard 0.0 HARVEST value for price-crashed MELON/STRAWBERRY
with max(spot, hold_fraction * base).  Everything else must stay identical, so
these checks are mostly equivalence assertions against v122.
"""

import random
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def load(path, name):
    spec = spec_from_file_location(name, path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def harvest_gain(mod, jobs):
    for gain, _pos, ops, _arg in jobs:
        if ops == ["HARVEST"]:
            return gain
    return None


def tile(crop, held, planted_day=0, **extra):
    row = {
        "crop": crop,
        "yield_units": held,
        "planted_day": planted_day,
        "watered_today": True,
        "fertilized_until_day": 99,
    }
    row.update(extra)
    return row


def call(mod, crop, held, step, day, storage_load, prices, planted_day=0):
    return mod.crop_service_jobs(
        3, 4, tile(crop, held, planted_day), step, day, storage_load,
        lambda item: prices.get(item, 100), {"STRAWBERRY": 5, "TOMATO": 1},
    )


def main():
    parent = load(ROOT / "a_v122_partial_horizon.py", "v122")
    cand = load(ROOT / "a_v123_harvest_hold_value.py", "v123")

    crashed = {"STRAWBERRY": 1, "MELON": 20, "FERTILIZER": 100}
    healthy = {"STRAWBERRY": 120, "MELON": 250, "FERTILIZER": 100}

    # 1. The v122 defect: a ripe STRAWBERRY at a crashed spot is worth zero,
    #    so the job is never scheduled and the yield is destroyed on the tile.
    v122_jobs, _ = call(parent, "STRAWBERRY", 4, 480, 20, 30, crashed, 4)
    assert harvest_gain(parent, v122_jobs) == 0.0

    # 2. v123 prices it at the reservation we would insist on when selling.
    v123_jobs, _ = call(cand, "STRAWBERRY", 4, 480, 20, 30, crashed, 4)
    expect = 4 * cand.hold_fraction(480, 20, 30) * cand.MP["STRAWBERRY"]["base"]
    assert abs(harvest_gain(cand, v123_jobs) - expect) < 1e-9
    assert harvest_gain(cand, v123_jobs) > 200.0

    # 3. The floor is never above what we would accept for the unit: it is
    #    bounded by HOLD_EARLY * base, and it decays with the sell reservation.
    per_unit = []
    for day in (10, 20, 25, 29):
        step = day * cand.TPD
        floor = cand.hold_fraction(step, day, 30) * cand.MP["STRAWBERRY"]["base"]
        assert floor <= cand.HOLD_EARLY * cand.MP["STRAWBERRY"]["base"]
        per_unit.append(floor)
    assert per_unit == sorted(per_unit, reverse=True), per_unit
    assert cand.hold_fraction(cand.DUMP_STEP, 27, 30) == 0.0

    # 4. Above the gate the two agents are identical, on every crop and phase.
    for crop in cand.CROPS:
        for day in (5, 12, 18, 22, 27, 29):
            for held in (0, 1, 3, 4):
                for shed in (10, 60, 95):
                    step = day * cand.TPD
                    a, af = call(parent, crop, held, step, day, shed, healthy)
                    b, bf = call(cand, crop, held, step, day, shed, healthy)
                    assert a == b and af == bf, (crop, day, held, shed)

    # 5. Below the gate only the HARVEST value may move, only upward, and only
    #    for the two gated crops.  WATER/FERTILIZE are untouched everywhere.
    changed = 0
    for crop in cand.CROPS:
        for day in (5, 12, 18, 22, 27, 29):
            for held in (0, 1, 3, 4):
                for shed in (10, 60, 95):
                    step = day * cand.TPD
                    a, af = call(parent, crop, held, step, day, shed, crashed)
                    b, bf = call(cand, crop, held, step, day, shed, crashed)
                    assert af == bf
                    assert [j[1:] for j in a] == [j[1:] for j in b]
                    non_harvest_a = [j for j in a if j[2] != ["HARVEST"]]
                    non_harvest_b = [j for j in b if j[2] != ["HARVEST"]]
                    assert non_harvest_a == non_harvest_b
                    ga, gb = harvest_gain(parent, a), harvest_gain(cand, b)
                    if ga is None:
                        assert gb is None
                        continue
                    assert gb >= ga - 1e-9
                    if gb > ga + 1e-9:
                        changed += 1
                        assert crop in ("MELON", "STRAWBERRY"), crop
    assert changed > 0

    # 6. Shed pressure discourages a crashed-price harvest twice over, and
    #    both effects survive: hold_fraction clamps to 0.40 above SHED_SOFT,
    #    then the existing >90 storage damping scales the job by 0.1.
    dense, _ = call(cand, "STRAWBERRY", 4, 480, 20, 95, crashed, 4)
    sparse, _ = call(cand, "STRAWBERRY", 4, 480, 20, 30, crashed, 4)
    base = cand.MP["STRAWBERRY"]["base"]
    assert cand.hold_fraction(480, 20, 95) == 0.40
    assert abs(harvest_gain(cand, dense)
               - 0.1 * 4 * 0.40 * base) < 1e-9
    assert abs(harvest_gain(cand, sparse)
               - 4 * cand.hold_fraction(480, 20, 30) * base) < 1e-9
    assert harvest_gain(cand, dense) < harvest_gain(cand, sparse)

    # 7. Randomized differential characterization, same protocol as v121.
    rng = random.Random(20260814)
    crops = list(cand.CROPS)
    diff = 0
    for _ in range(3000):
        crop = rng.choice(crops)
        day = rng.randrange(0, 30)
        step = day * cand.TPD + rng.randrange(0, cand.TPD)
        prices = {c: rng.randrange(1, 300) for c in cand.CROPS}
        prices["FERTILIZER"] = rng.randrange(1, 200)
        args = (crop, rng.randrange(0, 5), step, day,
                rng.randrange(0, 100), prices, rng.randrange(0, day + 1))
        if call(parent, *args)[0] != call(cand, *args)[0]:
            diff += 1
    print("v123 differential: {}/3000 states change ({:.2%})".format(
        diff, diff / 3000.0))
    assert diff < 450, diff

    # 8. v123b is v123 restricted to yield the engine is about to destroy.
    atrisk = load(ROOT / "a_v123b_harvest_atrisk.py", "v123b")

    #    Safe yield below the gate: v123b must match v122, v123 must not.
    safe = dict(crop="STRAWBERRY", held=1, step=480, day=20,
                storage_load=30, prices=crashed, planted_day=4)
    args = (safe["crop"], safe["held"], safe["step"], safe["day"],
            safe["storage_load"], safe["prices"], safe["planted_day"])
    assert harvest_gain(atrisk, call(atrisk, *args)[0]) == 0.0
    assert harvest_gain(cand, call(cand, *args)[0]) > 0.0

    #    At the yield cap the next production is discarded, so v123b rescues.
    capped = ("STRAWBERRY", cand.CROPS["STRAWBERRY"]["my"], 480, 20, 30,
              crashed, 4)
    assert harvest_gain(atrisk, call(atrisk, *capped)[0]) > 200.0

    #    at_cap is not redundant with expiring.  Replaying the engine's
    #    _daily_refresh_plants for a never-harvested STRAWBERRY: unfertilized,
    #    it reaches the cap on the same day max_lifespan_step is stamped.
    #    Fertilized, it reaches the cap at production 2 of 4 -- two days
    #    earlier -- and productions 3 and 4 are discarded outright, half the
    #    tile's lifetime yield, with max_lifespan_step still unset.
    spec = cand.CROPS["STRAWBERRY"]
    for fertilized, expect_gap in ((False, False), (True, True)):
        held_units, lifespan, gap = 0, -1, False
        for current in range(30):
            nxt = current + 1
            since = nxt - 0 - spec["fyd"]
            if since < 0 or since % spec["iv"]:
                continue
            count = since // spec["iv"] + 1
            if count > spec["my"]:
                continue
            held_units = min(spec["my"], held_units + (2 if fertilized else 1))
            if count == spec["my"]:
                lifespan = (nxt + 1) * cand.TPD
            if held_units >= spec["my"] and lifespan < 0:
                gap = True
        assert gap is expect_gap, (fertilized, gap)

    #    An expiring tile rots, so v123b rescues that too.
    expiring = atrisk.crop_service_jobs(
        3, 4, tile("STRAWBERRY", 1, 4, max_lifespan_step=470),
        480, 20, 30, lambda i: crashed.get(i, 100), {})
    assert harvest_gain(atrisk, expiring[0]) > 50.0

    #    Above the gate v123b is identical to v122 everywhere, as v123 is.
    for crop in cand.CROPS:
        for day in (5, 12, 18, 22, 27, 29):
            for held in (0, 1, 3, 4):
                for shed in (10, 60, 95):
                    step = day * cand.TPD
                    a, af = call(parent, crop, held, step, day, shed, healthy)
                    c, cf = call(atrisk, crop, held, step, day, shed, healthy)
                    assert a == c and af == cf, (crop, day, held, shed)

    #    v123b never values a harvest above v123 and never below v122.
    for crop in cand.CROPS:
        for day in (5, 12, 18, 22, 27, 29):
            for held in (0, 1, 3, 4):
                step = day * cand.TPD
                ga = harvest_gain(parent, call(parent, crop, held, step, day,
                                               30, crashed)[0])
                gb = harvest_gain(atrisk, call(atrisk, crop, held, step, day,
                                               30, crashed)[0])
                gc = harvest_gain(cand, call(cand, crop, held, step, day,
                                             30, crashed)[0])
                if ga is None:
                    assert gb is None and gc is None
                    continue
                assert ga - 1e-9 <= gb <= gc + 1e-9, (crop, day, held,
                                                      ga, gb, gc)

    print("v123 harvest hold-value checks: PASS")


if __name__ == "__main__":
    main()
