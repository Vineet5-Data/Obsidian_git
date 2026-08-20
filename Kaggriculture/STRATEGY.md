# Kaggriculture — Highest-Reward Winning Strategy

> Research date: 2026-08-06. Sources: local `README.md` / `AGENTS.md`, and the actual engine source
> [`kaggriculture.py`](https://github.com/Kaggle/kaggle-environments/tree/master/kaggle_environments/envs/kaggriculture)
> (all mechanics below verified against source, not docs). Leaderboard = head-to-head episodes,
> skill rating from win/loss — **objective is P(win), money margin is the tiebreaker for robustness**.
> Per-turn budget: `actTimeout = 1s`, 60s total overage → heuristic scheduler only, no deep search / RL needed.

---

## 0. TL;DR

The game is a **logistics + market-microstructure problem**, not an RL problem. Three economic facts
(computed from the engine's exact price curves) decide the winner:

1. **EGG and WHEAT are infinite money sinks.** Their glut curve is `log`, so price never crashes:
   1,000 eggs sold ≈ **$39,800** (price still $38 at +1,000); wheat holds $18–20 forever.
   Geese with daily CARE produce **2 eggs/day each, indefinitely** → the core engine.
2. **MELON is a one-time ~$20–26k jackpot** (price $250 base, but `sq` glut curve floors at +158 units).
   Plant a full wave on day 0, harvest day 10, dump before the opponent's wave lands. First mover eats the curve.
3. **MILK / WOOL / STRAWBERRY are traps if dumped** (floor at 76 / 59 / 62 units) but **gold mines if
   trickled**: the town's demand is guaranteed to reach ~20–30 units/day/product by day ~24 (all 8 shops
   always unlock — 9 unlock slots, 8 shops). Selling *exactly at the town's drain rate* keeps the market
   in deficit → scarcity prices ($220–270 milk, $230–250 wool). Most opponents will dump, crash the price
   to $1, and conclude these are bad — this is the exploitable edge.

Plus a force multiplier: **farm hands are absurdly cheap** (fib cost: 8 hands = $54/day for 192 extra
actions ≈ $0.28/action, vs. $15–35 marginal value per action). Hire aggressively every day.

Expected end-bank with full execution: **$60–90k** vs. typical greedy agents' $10–25k.

---

## 1. Verified market math (from engine source)

`price(inv) = base ± amp·f(|inv − I0|)`, `amp = target·base/f(T)`, floor $1, I0 = 10,000.
Cumulative revenue selling N units from I0 (no town regen — regen only makes this better):

| Item | Units to $1 floor | Rev(100) | Rev(300) | Rev(1000) | Price @+100 | @+300 | @+1000 |
|---|---|---|---|---|---|---|---|
| WHEAT | never (>20k) | $2,193 | $6,313 | **$20,043** | 21 | 20 | 19 |
| EGG | never (>20k) | $4,371 | $12,559 | **$39,799** | 42 | 40 | 38 |
| MELON | 158 | **$21,721** | $26,627 | $27,327 | 150 | 1 | 1 |
| FERTILIZER | 493 | $9,010 | **$21,030** | $25,552 | 80 | 40 | 1 |
| TOMATO | 529 | $4,318 | $9,207 | $11,599 | 35 | 16 | 1 |
| CARROT | 842 | $2,738 | $6,510 | $10,838 | 23 | 15 | 1 |
| MILK | 76 | $6,205 | $6,405 | $7,105 | 1 | 1 | 1 |
| WOOL | 59 | $7,969 | $8,169 | $8,869 | 1 | 1 | 1 |
| STRAWBERRY | 62 | $3,847 | $4,047 | $4,747 | 1 | 1 | 1 |

**Scarcity prices** (market deficit of 50 / 150 / 400 units below I0 — town constantly drains everything):

| Item | @−50 | @−150 | @−400 |
|---|---|---|---|
| MILK | 221 | **266** | 334 |
| WOOL | 234 | **243** | 251 |
| STRAWBERRY | 179 | **223** | 288 |
| MELON | 284 | 294 | 303 |
| FERTILIZER | 110 | 130 | 180 |
| WHEAT | 32 | 37 | 45 |
| EGG | 53 | 59 | 74 |

**Town demand is guaranteed and grows**: town center eats 1 of every product /12 turns (×2 after day 10,
×4 after day 20 → 2/4/8 per day). A shop unlocks every 3 days (day 3,6,…,27 = 9 slots for 8 shops →
**all shops always active by day 24–27**; only the *order* is random). Each shop eats each of its products
6/day (single-product shops 12/day). Late-game guaranteed drain/day: wheat ~30–38, egg ~16–20,
milk ~18–26, strawberry ~24–32, wool ~12–20, carrot ~16–24, tomato ~12–20, melon 8 (center only),
fertilizer 0 (center excludes it; only player buy-backs restore it).

**Key market micro-rules (from `_process_market` / `_commit_unit`):**
- Orders resolve per-unit in lockstep; both players see the same quote each unit. No front-running within a turn — front-run across *days* instead.
- Sales at the $1 floor do **not** add to inventory (floor stays responsive) — dumping at $1 is pure waste, never do it.
- Only WHEAT and FERTILIZER can be bought back; buy price is quoted post-buy (round-trip = $0).
- Max 10 market orders/turn — plenty; batch sells.

---

## 2. Verified production math (from engine source)

**Watering bonus window** for one-time crops starts at `(max_yield_day+1)//2`:
- **WHEAT** (seed 10, `max_yield_day` 4): water d0 (mandatory — planting day counts as unwatered day #1!),
  skip d1, water d2,3,4 → harvest d4 with **4 units**. 6 actions/cycle, 4-day cycle (tile freed instantly on
  harvest, replant same day) → **1.0 wheat/tile/day**, ≈ $11.7/action at $20.
- **MELON** (seed 80, window ages 6–12, `first_yield_day` 10): water d0, d2, d4, then daily d6–d10 → harvest
  **d10 with 6 units** (cap). 10 actions/cycle. Fertilizer is useless on melon (cap hits at age 8 but harvest
  gate is age 10 anyway). Decay starts age 13 (−1 unit / 2 turns) — harvest on time or lose everything fast.
- **CARROT** (seed 20, window ages 2–3): water d0, d2, d3 → harvest d3 with 3. 5 actions, 3-day cycle. Early filler only.
- **TOMATO / STRAWBERRY**: production fires at end-of-day refresh (tomato ages 8–11 daily ×4; strawberry ages
  10/12/14/16). Fertilized+watered day → 2 instead of 1. `yield_units` caps at 4 → **harvest between fires**
  or production is silently lost. Niche: small fertilized strawberry patch sold into scarcity only.

**Animals — CARE is the whole game** (from `_daily_refresh_animals`):
- Refresh order per night: production fires (consuming banked bonus **if fed today**) → then fed+cared banks +1.
- **GOOSE** ($300 + free coop build): production every day. Fed+cared daily = **2 eggs/day forever**.
  Yield cap `max_held=4` → harvest every 2nd day (1 action nets 4 eggs). Steady state ≈ 3.5 actions/day
  (FEED+CARE+½HARVEST+COLLECT_FERTILIZER) for 2 eggs (~$80) + 1 fertilizer (~$40–80) − 1 wheat feed (~$20 opportunity)
  → **$25–35/action, payback < 3 days**. Micro-opt: start CARE at age 1 (not 0) so the banked bonus (3) exactly
  fills first production to the cap of 4 — a bank of 4 would overflow.
- **COW** ($400): first milk age 8, every 2 days; 2 banked care → **3 milk/production = 1.5/day**.
- **SHEEP** ($500): first wool age 6, every 3 days; 3 banked → **4 wool/production = 1.33/day**.
- Every surviving animal drops **1 free FERTILIZER/day** (even unfed); `COLLECT_FERTILIZER` = 1 action for
  $40–110 of product — collect while fert price ≥ ~$40, else skip (save the action) or use on strawberries.
- FEED consumes 1 WHEAT **from the unit's carried inventory** → morning routine: PICKUP WHEAT at shed, walk the animal ring.
- New animal survives its first day unfed; a new plant does NOT survive its planting day unwatered.

**Hands**: cost `fib(n)` per nth hire of the day (1,1,2,3,5,8,13,21,34,55,89,144…), reset daily, hands vanish
nightly. 8 hands = $54/day; 12 = $376/day. Marginal action value in a built farm is $15–40 → **hire 5–6 on
day 0, ramp to 10–14 mid/late game**. Hands spawn at the 4 shed-access tiles ((4,4),(5,4),(4,5),(5,5)) —
note (5,4) is in locked NE (passable, actions no-op there until bought).

---

## 3. The strategy — four phases

### Phase 0 — Opening (day 0)
Bank $3,000. Turn 0 market: `HIRE`×5, `BUY_SEED MELON 13`, `BUY_SEED WHEAT 6`, `BUY_SEED CARROT 4`,
`BUY_ANIMAL GOOSE 2`, `BUY_PRODUCT WHEAT 4` (feed until own wheat lands). ≈ $2,000 spent, ~$1,000 buffer.
Turns 1–23: plant all melons in outer NW ring, wheat/carrots mid, build 2 coops adjacent to shed-access tile,
carry geese from shed → PLACE. **Water every new plant the same day it's planted** (engine: planting day
counts as unwatered day #1 — miss it and it's a weed by morning).
Beware atomic PLANT rule: if two units PLANT the same crop with too few seeds, *all* those plants fail — the
scheduler must count seeds vs. simultaneous PLANT orders.

### Phase 1 — Ramp (days 1–9)
- Wheat/carrot cycles for cash + feed; first own wheat day 4 (= first goose feed self-sufficiency).
- Geese: feed+care daily from day 1; first eggs day 4; sell eggs immediately (log curve — never hold).
- Collect fertilizer daily; sell while ≥ ~$50 (early fert is $80–110 revenue for 1 action).
- `BUY_LAND` NE (~day 3–5, $1k) → 4–6 more geese + wheat tiles as egg/fert income allows.
- Watch opponent's farm (public): count their melon tiles and `planted_day`s → know exactly when their wave matures.

### Phase 2 — Melon jackpot (days 10–12)
- Harvest all melons at age 10 sharp (decay from age 13 is brutal).
- **Dump timing beats dump size**: if opponent's melons mature later, sell the entire wave immediately —
  first ~100 units into the curve capture $21.7k of the $26.6k total. If they mature the *same* day, sell
  everything at once anyway (per-unit lockstep splits the curve evenly; hesitation only loses).
  If theirs mature *earlier*, hold and trickle ≤ town-regen (8/day) at the elevated post-recovery price instead.
- Proceeds → `BUY_LAND` SW+SE ($6k), 12–20 more geese over days 10–16, 3–5 cows, 3–4 sheep, 2nd melon wave
  (plant ≤ day 19 — harvest by day 29; a ~day-11 planting harvests day 21 into a part-recovered curve ≈ $100–150/unit).

### Phase 3 — Scarcity farming (days 12–27)
- **Core loop**: N geese × (feed, care, harvest-alt-days) + wheat engine sized to N geese feed + surplus wheat sales.
- **Premium trickle rule**: sell MILK/WOOL/STRAWBERRY only while `market.inventory[item] < I0` (deficit) —
  i.e. ride the scarcity price the town creates; never push inventory above I0. If the opponent floods one of
  these, abandon it (stop selling; stop CARE on that species; keep feeding — 1 fert/day still pays for feed).
- Fertilizer: collect + sell while ≥ ~$40; below that, apply to strawberries (doubles production, +$220/pop at scarcity) or skip.
- Hands: 10–14/day; each unit owns a contiguous zone; animals ring the shed (3–4 touches/day), wheat mid-ring, melons outer.
- Shed cap 100 (excl. seeds) — sell surplus daily; never let end-of-day inventory drop overflow (overflow is discarded).

### Phase 4 — Liquidation (days 27–29)
- Last plantings: melon ≤ day 19, tomato ≤ day 17, wheat ≤ day 25, carrot ≤ day 26.
- **The end-of-day-29 refresh never pays out** (reward is set at step 718 of 720) → last production that counts
  is the end-of-day-28 refresh. Day 29: no FEED/CARE/water spend, pure harvest + haul + sell.
- Dump order on days 28–29: premium goods first down their curves (holding = $0), then everything else;
  sell fert stock; final turns = SELL every shed item. Unsold inventory is worth **nothing**.

### Win-condition adaptivity (rating = win/loss)
- Opponent farm + money are public. If **ahead** late: mirror-deny — whatever they're about to harvest in
  volume, sell yours into that market first. If **behind** late: variance — all-in second melon wave +
  hold premium stock for one coordinated scarcity spike instead of steady trickle.

---

## 4. Implementation blueprint (for the coding agent)

**Architecture** (single `main.py`, stateless — obs is a complete state; optional module-level cache for layout/assignments):
1. **State digest** — parse tiles into task objects: `WATER_DUE(tile, deadline)`, `HARVEST_READY(tile, value, decay_deadline)`,
   `FEED/CARE/COLLECT(tile)`, `PLANT_TARGET(tile, crop)`, `DIG(weed)`.
2. **Task-value function** — $/action from §1–2 tables, live-adjusted by current `market.prices`.
3. **Unit scheduler** — greedy nearest-deadline-first assignment of farmer+hands to tasks within zones;
   Manhattan pathing (all tiles passable incl. locked). Feed-carrier role: PICKUP wheat at shed first.
4. **Market module** — threshold rules: sell-floors per item (egg/wheat: always sell; premium: only in deficit,
   except endgame), melon dump trigger (own wave ready OR opponent wave imminent), fert sell-vs-use switch,
   HIRE count schedule, BUY_LAND triggers, feed buy-backs (wheat ≤ $28 when short).
5. **~20 tunable params** (hand counts/day, land-buy days, melon wave sizes, sell floors, animal mix, care cutoffs).

**Tuning** (fits compute constraints — pure CPU, no VRAM; engine is lightweight Python, ~seconds/episode):
- Local round-robin harness: candidate vs. {starter, random, previous-best, mirror} × many seeds; track win-rate
  AND mean bank. Mirror matches matter most (shared-market interaction).
- Evolve params with OpenEvolve/CMA-ES locally (RTX 4060 box, CPU-only, thousands of matches/day) or on Kaggle
  CPU sessions. **No RL** — 1s/turn budget and the combinatorial action space make it strictly worse than the
  tuned scheduler; do not spend GPU on this.
- Success bar per version (project convention): v_N must beat v_{N-1} ≥ 55% over ≥ 200 seeds before submitting.

**Submission**: single `main.py` (or tar.gz with `main.py` at root), function `agent(obs)`; smoke-test
`env.run(["main.py", "starter"])` full 720 steps + a 0-money and full-shed edge-case seed before every
`kaggle competitions submit kaggriculture -f main.py -m "..."`.

**Gotchas checklist** (all verified in source):
- Planting day = unwatered day #1 (water same day or lose the plant). New animals get one free unfed day.
- Atomic PLANT validation drops ALL same-crop plants if seeds short.
- Harvest ongoing crops/animals before their next production tick or the cap eats the yield.
- Never sell at the $1 floor. Never let premium inventory cross above I0.
- DIG can't remove an occupied coop/pasture; animals themselves can never be sold or removed.
- Market orders execute *after* unit actions in the same turn → seeds bought at hour h plant at h+1.
- Day-29 end-of-day refresh pays nothing; reward = bank at step 718.
