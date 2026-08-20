src = open("main.py", encoding="utf-8").read()

# 1) Never drop a recorded animal purchase just because the upgrade is
#    unaffordable - fall back to the species the route actually recorded.
old = """                if extra_cost > extra_budget:
                    # Do not lock scarce cash into the lower-value species just
                    # because the recorded order happened to name it.  Omitting
                    # the order is the explicit equivalent of the old silent
                    # failure and leaves room for the next price check.
                    continue
                extra_budget -= extra_cost
                order[1] = animal
                planned[animal] += quantity"""
new = """                if extra_cost > extra_budget:
                    # Cannot afford the upgrade: keep the recorded species.
                    # Skipping the order outright loses the animal for the whole
                    # season (11 placed vs the winner's 15 in episode 90487461).
                    animal = recorded_animal
                    extra_cost = 0
                    if planned[animal] + quantity > int(MAX_ONE_ANIMAL):
                        market.append(order)
                        continue
                extra_budget -= extra_cost
                order[1] = animal
                planned[animal] += quantity"""
assert old in src
src = src.replace(old, new, 1)

# 2) Value animals by season yield per dollar rather than per-unit sale price.
old_pref = """    cow_value = 1.5 * max(1, int(prices.get("MILK", 160) or 160))
    sheep_value = (4.0 / 3.0) * max(1, int(prices.get("WOOL", 200) or 200))"""
new_pref = """    cow_value = COW_BIAS * ANIMAL_YIELD["COW"] * max(1, int(prices.get("MILK", 160) or 160)) / ANIMAL_COST["COW"]
    sheep_value = ANIMAL_YIELD["SHEEP"] * max(1, int(prices.get("WOOL", 200) or 200)) / ANIMAL_COST["SHEEP"]"""
pass  # preference untouched
src = src.replace('ANIMAL_COST = {"COW": 400, "SHEEP": 500}',
                  'ANIMAL_COST = {"COW": 400, "SHEEP": 500}\n'
                  '# Cared season output per animal, measured in-engine.\n'
                  'ANIMAL_YIELD = {"COW": 39, "SHEEP": 38}\n'
                  'COW_BIAS = 1.0', 1)

open("v7a.py", "w", encoding="utf-8").write(src)
print("v7a.py written")
