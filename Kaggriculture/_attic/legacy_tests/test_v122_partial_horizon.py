"""Focused checks for v122's only behavioral change."""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def load(path, name):
    spec = spec_from_file_location(name, path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    parent = load(
        Path(r"C:\Users\Vinee\Downloads\a_v119_midgame_fertilizer_collect.py"),
        "v119",
    )
    candidate = load(ROOT / "a_v122_partial_horizon.py", "v122")

    expected = {
        "WHEAT": {1: None, 2: (2, 3, 2), 3: (3, 4, 3), 4: (4, 5, 4)},
        "CARROT": {1: None, 2: (2, 3, 2), 3: (3, 4, 3)},
        "MELON": {9: None, 10: (6, 7, 10), 12: (6, 9, 12)},
    }
    for crop, cases in expected.items():
        for days_left, value in cases.items():
            assert candidate.crop_yield(candidate.CROPS[crop], days_left) == value

    assert parent.crop_yield(parent.CROPS["WHEAT"], 2) is None
    assert candidate.crop_season(candidate.CROPS["WHEAT"], 2) == (2, 3, 10.0)

    for crop in candidate.CROPS:
        for days_left in range(30):
            value = candidate.crop_yield(candidate.CROPS[crop], days_left)
            if value:
                units, actions, span = value
                assert 0 < units <= candidate.CROPS[crop]["my"]
                assert actions >= 2 and span <= days_left
            if candidate.CROPS[crop]["ong"] or days_left >= candidate.CROPS[crop]["myd"]:
                assert value == parent.crop_yield(parent.CROPS[crop], days_left)

    print("v122 partial-horizon checks: PASS")


if __name__ == "__main__":
    main()
