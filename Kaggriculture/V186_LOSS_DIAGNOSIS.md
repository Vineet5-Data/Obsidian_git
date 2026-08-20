# v186 Loss Diagnosis + Upgrade Roadmap

> **STATUS — revised after fixing the analyzer.** Two things changed since the
> first draft:
> 1. `_econ_loss_analysis.py` / `_loss_analysis.py` were rebuilt to report
>    FILLED market volume at per-unit prices instead of requested-quantity x a
>    single pre-trade quote. Measured error before the fix: an opponent's
>    reconstructed cash was **4.2x** its true money delta. After: median
>    residual **0.5%**, max 4.8%, and every window now prints `cash_residual`.
> 2. `_env_src.py` was a **stale copy of the engine** (56 lines added / 46
>    removed vs. the shipped one, including the town-demand model). The
>    first draft's headline finding (FM-1, a town-centre absorption bug in
>    `a_v186.py`) came from that stale copy and **is wrong** -- see FM-1 below.
>
> Every "combined supply" figure below still comes from the OLD broken
> analyzer and must be re-measured. Sink figures are engine-derived and stand.

Baseline `a_v186.py`, 1203-557 (68.4%). Everything below is derived from the
installed engine and `a_v186.py`, not fitted to results.

---

## 0. Data validity gate — what in `v186_loss_analysis.md` is safe to use

**This has now been fixed** -- what follows is the diagnosis of the old output.
`_econ_loss_analysis.py` built `units_sold` and `revenue` from the **requested**
quantity on each market order, priced at a **single pre-trade quote**. The
engine (`_commit_unit`) fills unit-by-unit at the marginal price and **aborts
the whole order on the first failed unit**.

So every opponent revenue/production/spend line is `requested x quote`, not
`filled x realised`. The opponent issues 2x our SELL orders (`mkt:SELL` 64.6
vs 32.3), so their inflation is roughly 2x ours.

Proof by construction: opponent "FERTILIZER +941 units / +$45,958, days 0-19".
`_daily_refresh_animals` sets `fertilizer_available = True` once per animal per
day; `COLLECT_FERTILIZER` yields exactly 1 unit. Their 13-animal herd caps at
**~260 units over 20 days**. And FERTILIZER has **zero demand drain** (excluded
from `TOWN_CENTER_PRODUCTS`, present in no shop), so its price is a one-way
ratchet at 0.2/unit — the market cannot pay $48.8/unit for 941 units.

| Signal | Verdict |
|---|---|
| opponent revenue / production / spend tables | **DISCARD** — order-spam artifact |
| our own telemetry (created/admit/assign/emitted/exec, cap ticks, expiry) | trust |
| action counts (`op` table) | trust |
| money delta by day | trust |
| crop tiles / herd end-of-window | trust (board snapshot) |
| land + wage spend | trust (fixed prices) |

**Consequence:** the two conclusions the report invites — "chase fertilizer",
"chase wheat revenue" — are half-priced off nothing. The wheat *tile count*
(opp 23.2 vs us 7.2) is real; the wheat *revenue* number is not.

---

## 1. The real model: nine conveyor belts with fixed, knowable throughput

`_town_consume` (`_env_src.py:705`) is fully deterministic:

* every **4** steps (6x/day): each unlocked shop drains 1 unit of each of its
  products, or **2** if the shop sells a single product;
* every **24** steps (1x/day): the town centre drains **1** unit of every
  product **except FERTILIZER**;
* shops unlock one per 3 days from empty, up to `MAX_SHOP_INSTANCES` = 8, drawn
  **with replacement** -- the same shop can appear several times and each
  instance consumes independently.

Total per-tick shop drain across all 8 shops, `D_p`:
WHEAT 5, STRAWBERRY 4, MILK 3, CARROT 3, EGG 2, TOMATO 2, WOOL 2, MELON 0,
FERTILIZER 0.

Season absorption = `99*D_p` (shops) + `30` (town centre: 1 unit per product
per day, every `townCenterSellInterval` = 24 steps -- there is no day-scaled
multiplier; the first draft used a stale engine copy that had one):

| product | season sink | balance vs. supply | realised | base |
|---|---|---|---|---|
| WHEAT | 525 **+ ~500 feed buys = ~1,025** | short | $39-71 | 25 |
| STRAWBERRY | 426 | short | $154-206 | 120 |
| CARROT | 327 | very short | ~$42 | 35 |
| MILK | 327 | near the line | $149 | 160 |
| TOMATO | 228 | short | $85 | 60 |
| EGG | 228 | short | $61 | 50 |
| WOOL | 228 | near the line | $133 | 200 |
| MELON | **30** | **badly oversupplied** | $94 by d20 | 250 |
| FERTILIZER | **0** | ratchet only | — | 100 |

Two sinks are far smaller than the first draft claimed. MELON absorbs **30
units for the whole season** against roughly 180 produced by the two farms
together -- its price collapse is not marginal, it is structural. FERTILIZER
has no sink at all: it is excluded from `TOWN_CENTER_PRODUCTS` and appears in
no shop, so every unit sold ratchets the price down 0.2 permanently.

The sink column above is engine arithmetic and stands. The supply side must be
re-measured with the fixed analyzer before any unmet-demand total is quoted --
the first draft's "~1,690 units unmet" used both the stale town constant and the
broken supply figures, and is withdrawn.

What survives without re-measurement, because it does not depend on either:
**every product whose realised price sits above its base is a belt running
below capacity** -- WHEAT ($39-71 vs 25), STRAWBERRY ($154-206 vs 120), TOMATO
($85 vs 60), EGG ($61 vs 50), CARROT (~$42 vs 35). MELON ($94 vs 250) and WOOL
($133 vs 200) are the saturated ones. Those realised prices come from the
observation stream, not from the order-counting that was broken.

---

## 2. Tile-days are the currency, and the ranking is not what v186 plays

`window_start = (max_yield_day+1)//2` (`_env_src.py:383`); water adds `+1`, or
`+2` inside a 3-day FERTILIZE window. Non-ongoing tiles clear to `None` on
harvest and can be replanted the same step.

| crop | cycle | units | u/tile-day | u/worker-op | $/tile-day |
|---|---|---|---|---|---|
| **WHEAT + FERTILIZE** | 5d | 6 | **1.20** | 0.86 | **$66** |
| WHEAT plain | 5d | 4 | 0.80 | 0.80 | $44 |
| CARROT + FERTILIZE | 4d | 4 | 1.00 | 0.67 | $42 |
| MELON | 11-13d | 6 | 0.55 | 0.60 | $52, falling |
| STRAWBERRY | 18d | 4 | 0.22 | 0.33 | $44 |
| TOMATO | 13d | 4 | 0.31 | 0.40 | $28 |

Fertilised wheat is the best asset in the game and the only one whose 5-day
cycle can be **cohort-staggered to match its own belt** (20 tiles / 5 cohorts
= 4 tiles/day x 6 units = 24 units/day, against a 21-38/day wheat drain).

We hold ~480 fertilizer units/season (16 animals x 30d) and spend **47**.

---

## 3. Failure modes, ranked and sized

### FM-1 — RETRACTED: the absorption code is correct; the engine copy was stale

The first draft claimed `a_v186.py:545` / `:693` understated town-centre demand
by 2x-8x, because `_env_src.py` showed the town draining `center_mult` (1/2/4)
units every **12** steps. The installed engine
(`kaggle_environments` 1.32.6) drains **1 unit every 24 steps**, with no
multiplier and no `TOWN_CENTER_DEMAND_SCHEDULE`. `steps_left / TPD` is exactly
right. **No change to make here.**

What is real is the cause. `_env_src.py` had diverged from the shipped engine
(56 lines added / 46 removed), and the divergence was concentrated in exactly
the mechanic under test:

```
-TOWN_CENTER_DEMAND_SCHEDULE = [(20, 4), (10, 2), (0, 1)]
+MAX_SHOP_INSTANCES = 8
-    center_interval = max(1, int(get(cfg, "townCenterSellInterval", 12)))
+    center_interval = max(1, int(get(cfg, "townCenterSellInterval", 24)))
-        center_mult = next(m for threshold, m in TOWN_CENTER_DEMAND_SCHEDULE ...)
```

That file is the reference every strategy claim in this repo is derived from.
It has been re-copied from the installed engine (`kaggle_environments` 1.32.6).
Re-copy it after any upgrade; never edit it by hand.

One live lead surfaced while checking this: `a_v186.py:1758` emits
`["PICKUP", "WHEAT", 0]`, and the engine's PICKUP returns immediately on
`n <= 0`. If that 0 is not rewritten before emission, the job is a guaranteed
no-op occupying a worker slot. Unverified -- worth one grep.

### FM-2 — wheat is hard-gated to days 0-2

`a_v186.py:1582`:

```python
if day < 3 and crop_slots > 0:
    quick = min(crop_slots, max(6, int(round(crop_slots * 0.40))))
    want_crop["WHEAT"] = quick
```

After day 2 wheat never re-enters `want_crop`; only STRAWBERRY / MELON / TOMATO
compete for slots. Result: 7.2 wheat tiles at d19 vs the opponent's 23.2, into
the deepest sink in the game — the one belt also drained by **both** players'
FEED purchases. `BUY_PRODUCT WHEAT` removes market inventory, and the below-`I0`
curve is `sqrt` at amp 1.0 while the above-`I0` curve is `log` at amp 0.834:
buying pushes wheat up fast, dumping barely moves it down. Wheat is dump-proof.

Every wheat unit is also a FEED unit we currently buy at ~$55. 212 FEEDs/game.

### FM-3 — phase inversion: labour is free exactly when we do not use it

| window | PASS turns/game-day | HARVEST exec/day |
|---|---|---|
| d0-14 | **48.75** | 3.87 |
| d15-19 | 3.58 | 16.17 |
| d20-24 | 1.13 | 25.01 |
| d25-29 | 5.86 | 24.45 |

~731 idle worker-turns/game in d0-14 (~20% of early capacity), then saturation.
Wheat's 5-day cycle is the **only** crop that can consume day-0-14 labour —
strawberry, melon and tomato do nothing until day 8-10. Meanwhile wage spend
d0-19 is us $5,128 vs opp $3,113: we pay 65% more for hands that PASS.

### FM-4 — the shed is a 100-unit hole with a nightly incinerator

`_drop_inventories_to_shed(private, shed_cap)` runs at **every day boundary**
(`_env_src.py:856`) and its docstring is explicit: "overflow is discarded".
`SHED_CAP` is 100 **total across all 9 products**.

Standing harvestable stock at day 20 is ~172 units (22 strawberry tiles x 4 +
8.7 cows x 6 + 5.4 sheep x 6). We cannot bank a day's harvest. This is why
HARVEST admit% is 38.5% in d20-24 and why `crop expiry with held yield` runs
992.89/game for STRAWBERRY in the same window — the agent correctly refuses to
harvest into a full shed and the yield rots on the tile.

Treat the shed as **flow, not stock**: sell before harvesting in the same step,
and stagger plant cohorts so harvest waves match belt throughput.

### FM-5 — melon is the one crop to cut; fertilizer must never be sold

MELON: sink 140/season, combined supply 183, **zero shop demand**, quadratic
decay (`250 - 0.01*(inv-I0)^2`), 11-13 tile-days locked for 6 units, and it caps
at max_yield around age 8 while still advertising WATER (the v186 item-3 fix).
Our melon seed spend is *higher* than the opponent's ($1,808 vs $1,229) for a
product realising $94 by day 20.

FERTILIZER: sink **0**. Every unit sold ratchets the price down 0.2 permanently;
total sellable across both players before the floor is ~500 units, ever. Its
only correct use is FERTILIZE — which on wheat converts 4 units into 6.

### FM-6 — carried over, unverified

Job-board truncation ranks on raw value while the objective is
`value - move_rate*d` (~2,003 zero-travel jobs cut/game); `move_rate` inflated
by synthetic priority flags used as a **veto** rather than a ranking.
`HUNGARIAN_JOBS = 48` columns against 4,288 WATER jobs created/game-day.

---

## 4. Tactical refinements (priority queue / rolling window)

1. **Fix the absorption horizon** — `steps_left/12 * center_mult(day)`, summed
   exactly across the day-10 and day-20 schedule breaks. Both call sites.
2. **Let wheat compete every day**, sized by residual sink
   `absorb[WHEAT] - sim_supply[WHEAT] - opp_visible_wheat`, not by `day < 3`.
3. **Cohort-stagger non-ongoing crops.** Wheat's 5-day cycle x 5 cohorts makes
   the harvest wave self-matching to the belt. Free; changes no valuation.
4. **Couple HARVEST admission to a per-step shed ledger** that counts the sell
   orders already queued this step, instead of gating on `shed_used` alone.
5. **Spend fertilizer on wheat**, never on a tile at `max_yield`, never sell it.
6. **Delay hires until `PASS/day` falls below a threshold.** `hire_bill` is
   Fibonacci; we are paying for 48.75 PASS/day in d0-14.
7. **Truncation key = `value - move_rate*d`**; keep the synthetic priority as a
   ranking and remove it from the feasibility veto.

## 5. Opponent counter-play

Both agents share exactly one channel: `market["inventory"]`. Everything else is
private. The public levers already exist in the file and are underused —
`sale_value`, `race_score`, `one_unit_denial_bonus` (`a_v186.py:263-300`).

* **C1 — belt-share targeting.** Read `opp_crop_counts` (already computed,
  `a_v186.py:1492`) and allocate the marginal tile to
  `argmax(absorb[p] - our_supply[p] - opp_supply[p])`. This anti-correlates the
  portfolio automatically and is the general form of "cut melon, add wheat".
* **C2 — race the doomed tiles.** A rival tile past `max_lifespan_step` holding
  yield is a *forced* seller within 8 steps. `race_score` already prices selling
  before vs after; extend it from a sell decision to a **harvest** decision.
* **C3 — claim the empty lanes.** TOMATO (83% unmet, opponent grows zero), EGG
  (84% unmet, opponent keeps zero geese), CARROT (97% unmet). Small individually,
  uncontested, and invisible to mirror screening.
* **C4 — never mirror-screen any of this.** Both sides share one market, so a
  supply-side gain cancels in a mirror. Use `screen_top.py` against `.top/`.

## 6. Experiment queue — one hypothesis, one change, each independently testable

| # | change | branch-fires check | predicted move |
|---|---|---|---|
| ~~H1~~ | ~~absorption fix~~ | **RETRACTED** -- the code was already correct | — |
| H2 | wheat competes every day, sized by residual sink | wheat tiles at d19: 7.2 → 15-20 | late revenue up; feed spend down |
| H3 | melon capped / banned after ~day 10 | melon seed spend d10+ → 0 | melon realised price recovers |
| H4 | FERTILIZE prioritised onto in-window wheat | FERTILIZE emitted 47 → 150+ | wheat units/tile 4 → 6 |
| H5 | per-step shed ledger couples harvest to sell | HARVEST admit% d20-24: 38.5% → ? | strawberry expiry-with-yield falls |
| H6 | hire gated on `PASS/day` | wage spend d0-19: 5,128 → ~3,500 | — |
| H7 | truncation key `value - move_rate*d` | dropped zero-travel jobs → 0 | — |

**Re-run the fixed analyzer first**, then start at H2. The corrected tool
already reverses the report's single largest line: on a 4-game sample the
FERTILIZER "gap" of opp +32,646 became **us +3,099 ahead**, because the
opponent's fertilizer revenue was almost entirely unfilled SELL orders. H3
(melon) is now better supported than before -- its sink is 30 units/season, not
140. H2 and H5 are unaffected by the retraction; both rest on tile counts and
telemetry, which were never part of the broken accounting.
