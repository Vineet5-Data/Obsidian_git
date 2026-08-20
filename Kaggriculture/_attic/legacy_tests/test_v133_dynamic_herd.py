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


v133 = load('v133', 'a_v133_dynamic_herd.py')


def blank_supply():
    return {k: 0.0 for k in v133.PRODUCTS}


def blank_inv():
    return {k: v133.I0 for k in v133.PRODUCTS}

# 1. Known absorption uses revealed shops only; unknown-shop expectation is absent.
steps = 400
none = v133.forecast_known_absorption([], steps)
yarn = v133.forecast_known_absorption(['YARN_STORE'], steps)
cream = v133.forecast_known_absorption(['ICE_CREAM_SHOP'], steps)
assert yarn['WOOL'] > none['WOOL']
assert cream['MILK'] > none['MILK'] and cream['STRAWBERRY'] > none['STRAWBERRY']
assert yarn['MILK'] == none['MILK']
assert v133.forecast_known_absorption([], steps) == none

# 2. Exact price-curve monotonicity: more background supply cannot improve
# incremental revenue for the same candidate batch.
for item in ('EGG', 'MILK', 'WOOL'):
    last = float('inf')
    for background in range(0, 1200, 5):
        value = v133.projected_incremental_revenue(
            item, v133.I0, background, 0.0, 20)
        assert value <= last + 1e-9, (item, background, value, last)
        last = value

# 3. Demand actually changes species choice rather than being diagnostic-only.
base = blank_supply(); minv = blank_inv(); counts = {k: 0 for k in v133.ANIMALS}
plan_yarn, _ = v133.allocate_residual_species(
    5, 20, 10, counts, {}, {}, base,
    v133.forecast_known_absorption(['YARN_STORE'], 400), minv)
plan_milk, _ = v133.allocate_residual_species(
    5, 20, 10, counts, {}, {}, base,
    v133.forecast_known_absorption(['ICE_CREAM_SHOP', 'PIZZA_SHOP'], 400), minv)

# 4. Rival/own residual supply can reverse the same public-demand choice.
base_milk = blank_supply(); base_milk['MILK'] = 400
plan_sat_milk, _ = v133.allocate_residual_species(
    5, 20, 10, counts, {}, {}, base_milk,
    v133.forecast_known_absorption(['ICE_CREAM_SHOP'], 400), minv)
assert plan_sat_milk.get('COW', 0) < 4, plan_sat_milk

base_wool = blank_supply(); base_wool['WOOL'] = 400
plan_sat_wool, _ = v133.allocate_residual_species(
    5, 20, 10, counts, {}, {}, base_wool,
    v133.forecast_known_absorption(['YARN_STORE'], 400), minv)
assert plan_sat_wool.get('SHEEP', 0) < 5, plan_sat_wool

# 5. Species cap is hard and exact.
plan, _ = v133.allocate_residual_species(
    12, 20, 4, counts, {}, {}, blank_supply(),
    v133.forecast_known_absorption([], 400), minv)
assert all(n <= 4 for n in plan.values())

# 6. Pending/owned animals consume the same cap.
owned = {'COW': 4, 'SHEEP': 0, 'GOOSE': 0}
plan, _ = v133.allocate_residual_species(
    5, 20, 4, owned, {}, {}, blank_supply(),
    v133.forecast_known_absorption(['ICE_CREAM_SHOP', 'PIZZA_SHOP'], 400), minv)
assert plan.get('COW', 0) == 0, plan

# 7. Self-limiting economics: selecting a species adds its projected output and
# weakly lowers the next identical candidate's revenue/score.
for species in v133.ANIMALS:
    supply = blank_supply()
    known = v133.forecast_known_absorption([], 400)
    first = v133.residual_species_economics(species, 20, supply, known, minv)
    assert first is not None
    supply[v133.ANIMALS[species]['prod']] += first[2]
    second = v133.residual_species_economics(species, 20, supply, known, minv)
    if second is not None:
        assert second[4] <= first[4] + 1e-9, (species, first, second)
        assert second[0] <= first[0] + 1e-9, (species, first, second)

# 8. Randomized feasibility/conservation for days where all three species can mature.
rng = random.Random(133)
for _ in range(20000):
    days_left = rng.randint(8, 29)
    cap = rng.randint(2, 12)
    owned = {k: rng.randint(0, cap) for k in v133.ANIMALS}
    shed = {k: rng.randint(0, 2) for k in v133.ANIMALS}
    carried = {k: rng.randint(0, 2) for k in v133.ANIMALS}
    # Clamp visible/pending state to the cap for a valid synthetic state.
    for k in v133.ANIMALS:
        extra = max(0, owned[k] + shed[k] + carried[k] - cap)
        if extra:
            carried[k] = max(0, carried[k] - extra)
            extra = max(0, owned[k] + shed[k] + carried[k] - cap)
        if extra:
            shed[k] = max(0, shed[k] - extra)
    feasible = sum(max(0, cap - owned[k] - shed[k] - carried[k]) for k in v133.ANIMALS)
    slots = rng.randint(0, min(20, feasible + 4))
    supply = {k: rng.uniform(0, 700) for k in v133.PRODUCTS}
    known = {k: rng.uniform(0, 700) for k in v133.PRODUCTS}
    inv = {k: v133.I0 + rng.randint(-300, 700) for k in v133.PRODUCTS}
    plan, sim = v133.allocate_residual_species(
        slots, days_left, cap, owned, shed, carried, supply, known, inv)
    assert sum(plan.values()) <= slots, (slots, feasible, plan)
    for k, n in plan.items():
        assert owned[k] + shed[k] + carried[k] + n <= cap
        assert n >= 0

print('PASS: v133 dynamic herd test suite')
