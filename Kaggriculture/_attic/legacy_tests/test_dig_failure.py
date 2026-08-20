import sys
from a_v137_reality_harvest import crop_service_jobs, hold_fraction, adjusted_sell_hold

def test_case(name, tile, step, day, storage_load, price):
    print(f"\n--- {name} ---")
    def spot(crop): return price
    jobs, fert = crop_service_jobs(
        x=2, y=2, tile=tile, step=step, day=day,
        storage_load=storage_load, spot=spot,
        opponent_crop_counts={}
    )
    for j in jobs:
        print(f"  {j[2][0]} with gain={j[0]}")

def main():
    # 1. Expiring Strawberry (low price) -> Should add DIG (25) and HARVEST (4)
    test_case("1. Expiring Strawberry (low price)", 
        {"crop": "STRAWBERRY", "yield_units": 4, "max_lifespan_step": 600, "planted_day": 5},
        step=600, day=25, storage_load=10, price=1)

    # 2. Healthy Strawberry at cap (low price) -> Should add HARVEST (~144), NO DIG
    test_case("2. Healthy Strawberry at cap (low price)", 
        {"crop": "STRAWBERRY", "yield_units": 4, "max_lifespan_step": 800, "planted_day": 15},
        step=600, day=25, storage_load=10, price=1)

    # 3. Expiring WHEAT (normal price 15) -> Should add HARVEST (29), NO DIG
    test_case("3. Expiring WHEAT", 
        {"crop": "WHEAT", "yield_units": 1, "max_lifespan_step": 600, "planted_day": 20},
        step=600, day=25, storage_load=10, price=15)

    # 4. Expiring Strawberry (high price 120) -> Should add HARVEST (480), NO DIG
    test_case("4. Expiring Strawberry (high price)", 
        {"crop": "STRAWBERRY", "yield_units": 4, "max_lifespan_step": 600, "planted_day": 5},
        step=600, day=25, storage_load=10, price=120)

if __name__ == '__main__':
    main()
