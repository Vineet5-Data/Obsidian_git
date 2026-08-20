import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent
def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / filename)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

v136 = load('v136', 'a_v136_aggressive_clear.py')

def test_aggressive_clear():
    # Test adjusted_sell_hold unconditionally clearing at >95
    sell_hold = v136.adjusted_sell_hold(0.8, 100.0, 96, 5, 20.0, 15.0)
    assert sell_hold == 0.0, f'Expected 0.0, got {sell_hold}'
    print('PASS: adjusted_sell_hold unblocks shed')

    # Test crop_service_jobs emitting DIG when harvest is worthless and crop is at cap
    # cd for Strawberry: myd=16, my=4, ong=True
    # If storage_load > 90, gain *= 0.1
    # If harvest_price is low, gain will be < 25.0
    tile = {
        "kind": "PLANT",
        "crop": "STRAWBERRY",
        "planted_day": 10,
        "yield_units": 4, # at cap
        "max_lifespan_step": 696 # expires day 29
    }
    
    # Simulate step = 600 (day 25)
    # spot("STRAWBERRY") = 1
    # shed_load = 99
    # This should emit HARVEST (with low gain) and DIG (with gain 25.0)
    
    # We have to mock spot() temporarily
    
    
    jobs, fertilize = v136.crop_service_jobs(0, 0, tile, step=600, day=25, storage_load=99, spot=lambda item: 1.0, opponent_crop_counts={}, opponent_wave={}, market_inv={})
    
    
    
    dig_jobs = [j for j in jobs if j[2][0] == "DIG"]
    assert len(dig_jobs) == 1, f"Expected 1 DIG job, got {dig_jobs}"
    assert dig_jobs[0][0] == 25.0, f"Expected DIG gain 25.0, got {dig_jobs[0][0]}"
    print('PASS: crop_service_jobs emits DIG for capped useless crop')

if __name__ == "__main__":
    test_aggressive_clear()
