# v97_cap70 replay analysis — ladder games 91759049 / 91759966

Source: two live ladder replays, we are seat 0 in both.

| replay | result | us | opponent | margin |
|---|---|---|---|---|
| 91759049 | WIN | 101,974 | 81,240 (Gaddam Shiva Teja) | +20,734 |
| 91759966 | LOSS | 102,503 | 103,571 (Moshel) | **-1,068** |

Both games: 3 quadrants unlocked (NW/NE/SW = 75 tiles), SE never bought.

---

## Headline finding: planting does not respond to the shop draw

The two games had almost opposite markets. Our crop mix was the same.

| planted | 91759049 | 91759966 |
|---|---|---|
| WHEAT | 76 | 90 |
| STRAWBERRY | 29 | 32 |
| MELON | 23 | 21 |
| CARROT | 18 | 20 |
| **TOMATO** | **0** | **0** |

Shops that consume each product, by end of game:

| product | 91759049 | 91759966 |
|---|---|---|
| STRAWBERRY | **1** | **6** |
| MELON | **0** | **0** |
| TOMATO | 2 | 3 |
| WHEAT | 2 | 4 |
| WOOL | 3 | 2 |
| MILK | 3 | 2 |

Strawberry had **one** buyer in game 1 and **six** in game 2. We planted 29 and 32.
That is noise, not adaptation.

Two products are planted the same way regardless of draw:

* **MELON: ~22 planted, 0 shops.** Melon appears in no shop's product list in the
  engine (`SHOPS` table) — only the town centre consumes it.
  **This is NOT waste — tested and disproved, see below.**
* **TOMATO: 0 planted, 2-3 shops.** Both PIZZA_SHOPs were known from day 10 in
  game 1; all three FARMERS_MARKETs known by day 19 in game 2. Still unexplained.

### Melon is a release valve, not a misallocation (measured)

Removing MELON from the `CROPS` table (`v112_nomelon.py`) redirects its tiles into
wheat and carrot and collapses the agent:

| | self-play bank (seed 23394720) | planted |
|---|---|---|
| v97_cap70 | 93,286 | WHEAT 104, STRAWBERRY 22, MELON 20, CARROT 13, TOMATO 2 |
| v112_nomelon | **41,936** | WHEAT 177, CARROT 45, STRAWBERRY 18, TOMATO 8 |

`top_tournament` confirms: **v112_nomelon 4-156 (2.5%), mean -24,129** against
v97's 43-117 (26.9%), mean -6,679. Worst result measured this session.

Melon has no shop demand, but that is exactly why it is useful: it is the only
crop whose price the shop-driven glut does not touch, so it absorbs tiles that
would otherwise crash wheat and carrot. Zero shop demand is not zero value.

This pairs with the `crop_cap` result (raises lost, monotonically). Both point at
one law: **bank is limited by market absorption, not planting throughput.**
Concentration and de-diversification both lose. Remaining upside is in *where*
production goes, not *how much*.

Shop unlock cadence is one per 3 days starting day 4, so 8 shops are only fully
known at day 25 — but 5-6 are known by day 16-19, which is when the crops that
later collapsed were still being planted.

---

## Selling: good on 6 of 7 products, catastrophic on one per game

Quantity-weighted realized sell price vs that product's mean market price:

| 91759049 | ratio | | 91759966 | ratio |
|---|---|---|---|---|
| WHEAT | 1.09 | | STRAWBERRY | 1.10 |
| WOOL | 1.02 | | MELON | 1.10 |
| CARROT | 1.00 | | WHEAT | 1.05 |
| MELON | 0.98 | | WOOL | 1.02 |
| MILK | 0.92 | | CARROT | 1.00 |
| FERTILIZER | 0.86 | | FERTILIZER | 0.94 |
| **STRAWBERRY** | **0.64** | | **MILK** | **0.42** |

The sell layer itself is fine. The failure is one product per game that we
overproduce, crash, and then liquidate into the crash.

**91759049 STRAWBERRY** — 165 units total:

| day | qty | avg sold | market |
|---|---|---|---|
| 12-20 | 2-10/day | 178-190 | 180-192 |
| 21 | 16 | 151 | 181 |
| 22 | 22 | 112 | 153 |
| 23 | 9 | 28 | 105 |
| 24 | 9 | 5 | 37 |
| 28-30 | 67 | ~5 | 3-14 |

76 units (46% of volume) returned ~2.7% of the peak price.

**91759966 MILK** — 77 units: days 9-16 sell 20 at 65-132; days 25-30 dump
**57 units (74%) at 7-28** while the market sits at 3-28.

Note `avg sold` falls well below `market` on dump days (day 23: 28 vs 105;
day 22: 112 vs 153). Settlement is per-unit lockstep, so a bunched sell walks
its own price down inside the step. Two separable defects:

1. the tail exists at all (overproduction past absorption)
2. it is liquidated in bunches rather than spread

Game 2 was lost by 1,068. The milk dump alone left several thousand on the table.

---

## User-reported issues, checked

| claim | verdict |
|---|---|
| doesn't use the full quadrants | **True but not the differentiator.** Mean planted tiles 28.7 / 32.1 of 75 (38-43%). Opponent 31.1 / 35.2. Both sides leave most of the grid idle. |
| pasture built day 1 turn 11 at q1 r1 c2, cow only day 4 | **Timing doesn't reproduce here.** First pasture step 1 (d1 t2) at tile (row 4, col 4); first animal SHEEP step 4 (d1 t5); first COW step 9 (d1 t10). Possibly a different replay or viewer indexing. |
| ...but the underlying instinct is right | **Confirmed defect: idle pasture.** Steps where a built pasture holds no animal: **us 257 / 228, opponent 108 / 103.** We build more pasture (max 16 vs 14) and leave it empty ~2.2x longer. |
| leftover seeds at end | **True, minor.** g1: CARROT 10, WHEAT 10, STRAWBERRY 4, TOMATO 1. g2: CARROT 8, MELON 5, WHEAT 3, STRAWBERRY 1, TOMATO 1. Shed is empty at end (good — no unsold stock), but ~25 bought seeds never planted. |

Weeds: mean 3.0 / 4.0 tiles vs opponent 2.0 / 3.0. Minor.

---

## Ranked fix candidates for next cycle

All must be measured on `top_tournament.py` (80 current top players, both seats),
**not** on `bench/panel_top.py --top-dir refleague`, which cannot rank correctly.
Baseline to beat: **43-117, 26.9%, mean -6,679**.

1. **Absorption should gate planting harder.** `v97_cap70.py:403-409` spreads
   speculative demand for unknown shops evenly across all 8 types, diluting the
   signal from shops we *have* seen. Weight known shops more as the game progresses.
   This is the direct expression of the "where, not how much" law and the only
   candidate that attacks the shop-blindness shown at the top of this document.
2. **Spread liquidation.** Cap units sold per step for a product whose price is
   below its own moving average, instead of dumping 40 in a day. Attacks defect (2)
   of the dump — the bunching — without touching production.
3. **Tomato: stop excluding it.** 2-3 shops consume it in both games, we plant zero.
   Worth finding why the crop scorer never selects it. Note melon's lesson: confirm
   the exclusion is a defect before "fixing" it.
4. **Idle pasture.** Don't build pasture until the animal purchase is funded.
   Smallest of the four; 257 vs 108 idle-pasture-steps.

## Confirmed dead — do not retry

Measured on `top_tournament.py`, baseline v97 = 43-117 / 26.9% / -6,679:

| change | W-L | win% | mean | median | worst |
|---|---|---|---|---|---|
| `crop_cap` 0.62/0.75 (`v110_cc62`) | 24-136 | 15.0% | -8,689 | -9,280 | -24,786 |
| `crop_cap` 0.85/0.95 (`v111_cc85`) | 19-141 | 11.9% | -9,322 | -9,649 | -25,885 |
| melon removed (`v112_nomelon`) | 4-156 | **2.5%** | -24,129 | -25,106 | -40,567 |
| melon out of contest loop (`v113_nocontest`) | 43-117 | 26.9% | -7,249 | -9,372 | -26,877 |

`v113_nocontest` ties v97 on record but is worse on **every** margin metric
(mean -7,249 vs -6,679, median -9,372 vs -8,634, worst -26,877 vs -22,329,
sweeps 14 vs 15). A tie on W-L that loses on all four margins is a reject, not a
wash — contesting the opponent's melon is doing real work.

Both directions from the current crop mix lose. v97_cap70's allocation is at a
local optimum on the concentration axis — stop tuning it.

## Harness note

`top_tournament.py:93` defaults to `min(10, cpu-2)` workers. On a 16-core box that
idles 6 cores; pass `--workers 14`.
