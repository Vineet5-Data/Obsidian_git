import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent
def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / filename)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

v135 = load('v135', 'a_v135_market_denial_fix.py')

def test_animal_limits():
    # day < 15 -> target = 16
    t, n, s, cap = v135.animal_allocation_limits(day=10, days_left=20, quadrant_count=4, slots=100, beast_count=0, struct_count=0, pending_animals=0)
    assert t == 16, f'Expected 16, got {t}'
    
    # day >= 15 -> scales to 20 based on quadrants
    t, n, s, cap = v135.animal_allocation_limits(day=18, days_left=12, quadrant_count=4, slots=100, beast_count=16, struct_count=16, pending_animals=0)
    assert t == 20, f'Expected 20, got {t}'
    
    # days_left < 8 -> target = current_assets
    t, n, s, cap = v135.animal_allocation_limits(day=25, days_left=5, quadrant_count=4, slots=100, beast_count=20, struct_count=20, pending_animals=0)
    assert t == 40, f'Expected 40, got {t}'
    print('PASS: v135 animal limits')

test_animal_limits()
