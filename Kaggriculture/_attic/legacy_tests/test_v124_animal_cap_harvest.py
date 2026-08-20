"""Focused checks for v124's only behavioral change.

v124 = v123b, plus the same at-risk harvest rule applied to
`animal_service_jobs`. Everything outside that HARVEST value must be identical
to v123b, so these are mostly equivalence assertions.
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


def harvest_gain(jobs):
    for gain, _pos, ops, _arg in jobs:
        if ops == ["HARVEST"]:
            return gain
    return None


def beast(species, held, **extra):
    row = {
        "animal": species,
        "yield_units": held,
        "fertilizer_available": False,
        "fed_today": True,
        "cared_today": True,
        "consecutive_unfed": 0,
    }
    row.update(extra)
    return row


def call(mod, species, held, step, storage_load, prices, six_args):
    tile = beast(species, held)
    spot = lambda item: prices.get(item, 100)
    if six_args:
        return mod.animal_service_jobs(3, 4, tile, step, storage_load, spot)
    return mod.animal_service_jobs(3, 4, tile, step, spot)


def main():
    prev = load(ROOT / "a_v123b_harvest_atrisk.py", "v123b")
    cand = load(ROOT / "a_v124_animal_cap_harvest.py", "v124")

    crashed = {"MILK": 1, "WOOL": 3, "EGG": 50, "FERTILIZER": 100}
    healthy = {"MILK": 160, "WOOL": 200, "EGG": 50, "FERTILIZER": 100}

    # 1. The defect: a COW at max_held with crashed MILK is worth zero in
    #    v123b, and near_cap's 2.0x multiplier cannot rescue it (0.0 * 2 == 0).
    cap = cand.ANIMALS["COW"]["mh"]
    assert harvest_gain(call(prev, "COW", cap, 480, 30, crashed, False)[0]) == 0.0

    # 2. v124 prices it at the same selling reservation v123b uses for crops,
    #    and the existing near_cap doubling still applies on top.
    got = harvest_gain(call(cand, "COW", cap, 480, 30, crashed, True)[0])
    floor = cand.hold_fraction(480, 20, 30) * cand.MP["MILK"]["base"]
    assert abs(got - cap * floor * 2.0) < 1e-9, (got, cap * floor * 2.0)
    assert got > 0.0

    # 3. Below the gate but NOT near cap, nothing is discarded yet, so v124
    #    must still agree with v123b.
    for held in range(1, cand.ANIMALS["COW"]["mh"] - 1):
        a = harvest_gain(call(prev, "COW", held, 480, 30, crashed, False)[0])
        b = harvest_gain(call(cand, "COW", held, 480, 30, crashed, True)[0])
        assert a == b == 0.0, (held, a, b)

    # 4. Above the gate the two are identical everywhere, and so are the
    #    FEED / CARE / COLLECT_FERTILIZER jobs in every case.
    for species in cand.ANIMALS:
        top = cand.ANIMALS[species]["mh"]
        for step in (0, 240, 480, 640, 700):
            for held in range(0, top + 1):
                for shed in (10, 60, 95):
                    for prices in (healthy, crashed):
                        a, au = call(prev, species, held, step, shed,
                                     prices, False)
                        b, bu = call(cand, species, held, step, shed,
                                     prices, True)
                        assert au == bu
                        non_h_a = [j for j in a if j[2] != ["HARVEST"]]
                        non_h_b = [j for j in b if j[2] != ["HARVEST"]]
                        assert non_h_a == non_h_b, (species, step, held)
                        ga, gb = harvest_gain(a), harvest_gain(b)
                        if prices is healthy:
                            assert ga == gb, (species, step, held, shed)
                        if ga is None:
                            assert gb is None
                            continue
                        assert gb >= ga - 1e-9
                        if gb > ga + 1e-9:
                            assert prices is crashed
                            assert held >= cand.ANIMALS[species]["mh"] - 1
                            assert cand.ANIMALS[species]["prod"] in (
                                "MILK", "WOOL")

    # 5. EGG is not in the gate list, so GOOSE is never rescued regardless.
    assert cand.ANIMALS["GOOSE"]["prod"] == "EGG"
    goose_cap = cand.ANIMALS["GOOSE"]["mh"]
    low_egg = dict(crashed, EGG=1)
    a = harvest_gain(call(prev, "GOOSE", goose_cap, 480, 30, low_egg, False)[0])
    b = harvest_gain(call(cand, "GOOSE", goose_cap, 480, 30, low_egg, True)[0])
    assert a == b, (a, b)

    # 6. The crop path is untouched: v124 must equal v123b on every crop.
    def crop(mod, crop_name, held, step, day, shed, prices):
        tile = {"crop": crop_name, "yield_units": held, "planted_day": 0,
                "watered_today": True, "fertilized_until_day": 99}
        return mod.crop_service_jobs(3, 4, tile, step, day, shed,
                                     lambda i: prices.get(i, 100),
                                     {"STRAWBERRY": 5})
    crop_crashed = {"STRAWBERRY": 1, "MELON": 20, "FERTILIZER": 100}
    for crop_name in cand.CROPS:
        for day in (5, 12, 20, 27, 29):
            for held in (0, 1, 3, 4):
                step = day * cand.TPD
                assert (crop(prev, crop_name, held, step, day, 30, crop_crashed)
                        == crop(cand, crop_name, held, step, day, 30,
                                crop_crashed))

    # 7. Randomized differential over the animal path only.
    rng = random.Random(20260814)
    species_list = list(cand.ANIMALS)
    diff = 0
    for _ in range(3000):
        species = rng.choice(species_list)
        step = rng.randrange(0, 720)
        prices = {p: rng.randrange(1, 300) for p in cand.PRODUCTS}
        args = (species, rng.randrange(0, cand.ANIMALS[species]["mh"] + 1),
                step, rng.randrange(0, 100), prices)
        if call(prev, *args, False)[0] != call(cand, *args, True)[0]:
            diff += 1
    print("v124 animal differential: {}/3000 states change ({:.2%})".format(
        diff, diff / 3000.0))
    assert 0 < diff < 450, diff

    print("v124 animal cap-harvest checks: PASS")


if __name__ == "__main__":
    main()
