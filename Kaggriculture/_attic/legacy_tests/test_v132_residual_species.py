import importlib.util
import math
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / filename)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


v128 = load('v128', 'a_v128_terminal_value.py')
v132 = load('v132', 'a_v132_residual_species.py')


def blank_supply():
    return {k: 0.0 for k in v132.PRODUCTS}


def blank_inv():
    return {k: v132.I0 for k in v132.PRODUCTS}

# 1. Known absorption uses revealed shops only; unknown-shop expectation is absent.
steps = 400
none = v132.forecast_known_absorption([], steps)
yarn = v132.forecast_known_absorption(['YARN_STORE'], steps)
cream = v132.forecast_known_absorption(['ICE_CREAM_SHOP'], steps)
assert yarn['WOOL'] > none['WOOL']
assert cream['MILK'] > none['MILK'] and cream['STRAWBERRY'] > none['STRAWBERRY']
assert yarn['MILK'] == none['MILK']
assert v132.forecast_known_absorption([], steps) == none

# 2. Exact price-curve monotonicity: more background supply cannot improve
# incremental revenue for the same candidate batch.
for item in ('EGG', 'MILK', 'WOOL'):
    last = float('inf')
    for background in range(0, 1200, 5):
        value = v132.projected_incremental_revenue(
            item, v132.I0, background, 0.0, 20)
        assert value <= last + 1e-9, (item, background, value, last)
        last = value

# 3. Demand actually changes species choice rather than being diagnostic-only.
base = blank_supply(); minv = blank_inv(); counts = {k: 0 for k in v132.ANIMALS}
plan_yarn, _ = v132.allocate_residual_species(
    5, 20, 10, counts, {}, {}, base,
    v132.forecast_known_absorption(['YARN_STORE'], 400), minv)
plan_milk, _ = v132.allocate_residual_species(
    5, 20, 10, counts, {}, {}, base,
    v132.forecast_known_absorption(['ICE_CREAM_SHOP', 'PIZZA_SHOP'], 400), minv)
assert plan_yarn.get('SHEEP', 0) == 5, plan_yarn
assert plan_milk.get('COW', 0) == 5, plan_milk

# 4. Rival/own residual supply can reverse the same public-demand choice.
base_milk = blank_supply(); base_milk['MILK'] = 400
plan_sat_milk, _ = v132.allocate_residual_species(
    5, 20, 10, counts, {}, {}, base_milk,
    v132.forecast_known_absorption(['ICE_CREAM_SHOP'], 400), minv)
assert plan_sat_milk.get('COW', 0) < 4, plan_sat_milk

base_wool = blank_supply(); base_wool['WOOL'] = 400
plan_sat_wool, _ = v132.allocate_residual_species(
    5, 20, 10, counts, {}, {}, base_wool,
    v132.forecast_known_absorption(['YARN_STORE'], 400), minv)
assert plan_sat_wool.get('SHEEP', 0) < 5, plan_sat_wool

# 5. Species cap is hard and exact.
plan, _ = v132.allocate_residual_species(
    12, 20, 4, counts, {}, {}, blank_supply(),
    v132.forecast_known_absorption([], 400), minv)
assert all(n <= 4 for n in plan.values())
assert sum(plan.values()) == 12, plan

# 6. Pending/owned animals consume the same cap.
owned = {'COW': 4, 'SHEEP': 0, 'GOOSE': 0}
plan, _ = v132.allocate_residual_species(
    5, 20, 4, owned, {}, {}, blank_supply(),
    v132.forecast_known_absorption(['ICE_CREAM_SHOP', 'PIZZA_SHOP'], 400), minv)
assert plan.get('COW', 0) == 0, plan

# 7. Self-limiting economics: selecting a species adds its projected output and
# weakly lowers the next identical candidate's revenue/score.
for species in v132.ANIMALS:
    supply = blank_supply()
    known = v132.forecast_known_absorption([], 400)
    first = v132.residual_species_economics(species, 20, supply, known, minv)
    assert first is not None
    supply[v132.ANIMALS[species]['prod']] += first[2]
    second = v132.residual_species_economics(species, 20, supply, known, minv)
    assert second is not None
    assert second[4] <= first[4] + 1e-9, (species, first, second)
    assert second[0] <= first[0] + 1e-9, (species, first, second)

# 8. Randomized feasibility/conservation for days where all three species can mature.
rng = random.Random(132)
for _ in range(20000):
    days_left = rng.randint(8, 29)
    cap = rng.randint(2, 12)
    owned = {k: rng.randint(0, cap) for k in v132.ANIMALS}
    shed = {k: rng.randint(0, 2) for k in v132.ANIMALS}
    carried = {k: rng.randint(0, 2) for k in v132.ANIMALS}
    # Clamp visible/pending state to the cap for a valid synthetic state.
    for k in v132.ANIMALS:
        extra = max(0, owned[k] + shed[k] + carried[k] - cap)
        if extra:
            carried[k] = max(0, carried[k] - extra)
            extra = max(0, owned[k] + shed[k] + carried[k] - cap)
        if extra:
            shed[k] = max(0, shed[k] - extra)
    feasible = sum(max(0, cap - owned[k] - shed[k] - carried[k]) for k in v132.ANIMALS)
    slots = rng.randint(0, min(20, feasible + 4))
    supply = {k: rng.uniform(0, 700) for k in v132.PRODUCTS}
    known = {k: rng.uniform(0, 700) for k in v132.PRODUCTS}
    inv = {k: v132.I0 + rng.randint(-300, 700) for k in v132.PRODUCTS}
    plan, sim = v132.allocate_residual_species(
        slots, days_left, cap, owned, shed, carried, supply, known, inv)
    assert sum(plan.values()) == min(slots, feasible), (slots, feasible, plan)
    for k, n in plan.items():
        assert owned[k] + shed[k] + carried[k] + n <= cap
        assert n >= 0
    assert set(sim) == set(supply)

# 9. All non-species mechanisms remain v128-identical under randomized states.
rng = random.Random(8132)
for _ in range(10000):
    args = (
        rng.uniform(0.0, 0.8), rng.uniform(0.0, 5000.0), rng.randint(0, 100),
        rng.randint(0, 20), rng.randint(0, 40), rng.randint(1, 100),
    )
    assert v132.adjusted_sell_hold(*args) == v128.adjusted_sell_hold(*args)

for _ in range(8000):
    day = rng.randint(0, 29); step = day * v132.TPD + rng.randint(0, 23)
    name = rng.choice(list(v132.ANIMALS)); a = v132.ANIMALS[name]
    tile = {
        'animal': name, 'yield_units': rng.randint(0, a['mh']),
        'fed_today': bool(rng.getrandbits(1)), 'cared_today': bool(rng.getrandbits(1)),
        'consecutive_unfed': rng.randint(0, 2),
        'fertilizer_available': bool(rng.getrandbits(1)),
    }
    prices = {p: rng.randint(1, 500) for p in v132.PRODUCTS}
    spot = lambda item, prices=prices: prices[item]
    assert v132.animal_service_jobs(1, 1, tile, step, spot) == v128.animal_service_jobs(1, 1, tile, step, spot)

for _ in range(5000):
    day = rng.randint(20, 29); slots = rng.randint(0, 35)
    market = {k: rng.uniform(0, 600) for k in v132.PRODUCTS}
    own = {k: rng.uniform(0, 250) for k in v132.PRODUCTS}
    absorb = {k: rng.uniform(0, 500) for k in v132.PRODUCTS}
    inv = {k: v132.I0 + rng.randint(-200, 600) for k in v132.PRODUCTS}
    args = (day, slots, market, own, absorb, inv, rng.randint(10, 80), rng.randint(0, 20))
    assert v132.late_terminal_crop_mix(*args) == v128.late_terminal_crop_mix(*args)

# 10. Successful fertilizer-denial math remains exact.
for inv in (9800, 10000, 10020, 10100, 10300):
    for rival in (0, 1, 5, 10, 20, 50):
        assert v132.one_unit_denial_bonus('STRAWBERRY', inv, rival) == v128.one_unit_denial_bonus('STRAWBERRY', inv, rival)

# 11. Source guard: failed v129/v130/v131 mechanisms are not present.
source = (ROOT / 'a_v132_residual_species.py').read_text()
assert 'exclusive_rematch' not in source
assert 'fertilizer_deadline_candidates' not in source
assert 'animal_deadline_harvests' not in source
assert 'legacy_purchase_slots' in source and 'allocate_residual_species' in source

print('PASS: v132 residual-species suite: targeted economics + 20,000 randomized allocations + 23,000 parent-parity checks')
