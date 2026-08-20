# 50% → 80%: roadmap from the corrected v186 baseline

Baseline `a_v186.py`, **880-880 (50.0%)**, n=1760, engine `kaggle_environments`
**1.32.7**, seed pool k=11..20, 88 `.top/` opponents.

Engine confirmed exactly: the report's margins reproduce **to the coin** on
1.32.7 (−41,653 / −32,504 / −30,749) and miss by ~80 on 1.32.6.

## Why 68.4% → 50.0% is not a regression

The 68.4% was measured on an **engine that no longer exists**. The notebook runs
`!pip -q install -U kaggle-environments` every session, so each run silently
adopts the latest environment.

Proof — replaying exact (agent, opponent, seed) triples on the current engine:

| pairing | reported | local seat0 | local seat1 | |
|---|---|---|---|---|
| `t_94142273_0` @1042155578 | NEW −41,653 | −41,574 | −28,528 | reproduces |
| `t_94135296_0` @28251350 | NEW −30,749 | −30,746 | −22,992 | reproduces |
| `t_94134439_1` @535203464 | OLD −38,671 | −6,055 | −6,004 | does not |
| `t_94138728_0` @535203464 | OLD −35,264 | **+640 (win)** | +640 | does not |

`a_v186.py` is byte-identical (102,872 B) across both runs, both used seed pool
k=11..20, and `margin`/`win` are computed identically. Only the engine moved.

What moved in it — the old `_env_src.py` copy is a snapshot of the prior engine:

```
-TOWN_CENTER_DEMAND_SCHEDULE = [(20, 4), (10, 2), (0, 1)]
-    center_interval = ... "townCenterSellInterval", 12
+    center_interval = ... "townCenterSellInterval", 24
```

Old: town centre drained `4 × 2 ticks/day = 8` per product per day from day 20.
New: **1 per product per day, flat.** Season town absorption per product
collapses **140 → 30**, concentrated entirely after day 20 — exactly the window
where the agent bleeds. `a_v186`'s own forecast is already correct for the new
engine ([a_v186.py:545](a_v186.py:545), [:692](a_v186.py:692) use
`steps_left / TPD`, +1/tick); its **tuning** is not.

**Treat 50.0% as the true current baseline. Discard the old report.**

## Where the 1,845-coin average lead evaporates

Net cash, all games: d0-19 **us +36,251 / opp +30,091 (we lead +6,160)**,
d20-24 us +23,895 / opp +26,217 (−2,323), d25-29 us +21,639 / opp +23,631
(−1,992). We win the first two thirds and hand it back. At 50% the margin is
variance-dominated, so a structural fix should move several points at once.

Realized prices, now exact (`revenue/units` on filled orders only):

| product | base | d0-19 | d20-24 | d25-29 | belt |
|---|---|---|---|---|---|
| **WHEAT** | 25 | 35.81 | 48.64 | **51.36** | short, **rising all season** |
| TOMATO | 60 | 66.46 | 72.27 | 76.56 | short, rising |
| EGG | 50 | 53.87 | 57.73 | 60.61 | short, rising |
| CARROT | 35 | 40.45 | 40.52 | 41.66 | short, flat |
| STRAWBERRY | 120 | 198.69 | 166.39 | 108.87 | good early, saturates by d25 |
| MILK | 160 | 179.47 | 151.65 | 132.67 | saturates from d20 |
| WOOL | 200 | 168.52 | 165.64 | 127.34 | **always below base** |
| MELON | 250 | 162.87 | **51.77** | 47.51 | 30-unit season sink |
| FERTILIZER | 100 | 67.74 | 25.66 | **7.27** | **zero sink, pure ratchet** |

A product realizing above base is a belt running below capacity. Four are
short all season and we are barely in three of them.

## Ranked queue

### BENCHMARKED (n=1760, engine 1.32.7, 1 SD = ±1.19 pts)

```
a_v186   (baseline)          880-880   50.0%     --
a_v206_wheat_mirror         1040-720   59.1%   +9.1   OLD baseline
a_v209_wheat_surplus        1193-567   67.8%   +8.7   ADOPTED -- new baseline
a_v208_price_1327            874-886   49.7%   -0.3   noise
a_v207_jobboard              707-1053   40.2%   -9.8   REJECTED
```

`a_v207` is closed: re-scoring job **admission** on `value − move_rate·d` is the
same mistake as the earlier move_rate work — that constant is safe as a ranking
and destructive as a veto, and admission is a veto. `a_v208` is neutral, so the
1.32.7 hinge spike rarely binds in play; keep it only as a correctness fix.

| # | change | measured gap | status |
|---|---|---|---|
| 1 | ~~mirror the rival's WHEAT~~ | +9.1 pts | **DONE — baseline is now `a_v206`** |
| 2 | bank surplus wheat instead of hoarding it for feed | acreage matched (23.17 vs 24.15) but revenue $801 vs $9,353 | **`a_v209_wheat_surplus.py` — ready to benchmark** |
| 4 | cap MAX_HANDS 12 -> 10 | eliminates late-game wage bloat while preserving Geese and early stability | **`a_v215_keep_geese.py` — ready to benchmark** |
| 5 | herd sizing off saturated WOOL/MILK belts | both below base from d20 | queued |
| — | ~~reserve FERTILIZER from sale~~ | **measured −6,019, t −5.0** (old engine) | parked |
| — | ~~delivery-window crop pricing (anti-MELON)~~ | **retracted — early melon is profitable** | dropped |

### Axes already closed by measurement

The v140 header records a paired benchmark that closes several directions.
These were run on the **old** engine, so they are not conclusive today, but any
of them needs a reason why the engine change flips the sign before it is worth
a cycle:

```
reserve fertilizer from sale the way wheat already is   -6,019   t -5.0
re-price HARVEST/CARE/FEED off a floor instead of spot  -4,746   t -3.21
reclaim decayed tiles + weeds with a real DIG value     -5,281   t -4.32
widen FERTILIZE into the full 3-day buff window         -1,057   t -0.90
buy the 4th quadrant (LAND_PRICES[2])                   -5,009   t -3.05
MAX_HANDS 12 -> 14                                      -4,947   t -5.49
MAX_HANDS 12 -> 16                                     -24,702   t -28.1
```

Fertilizer's realised price collapsing to **$7.27** by day 25 is a real change
in the economics — its sink was always zero, but the opportunity cost of every
alternative moved when town demand fell. Even so, reserving it lost heavily
once already; it is parked behind the untested axes, not promoted. Note that
change 3 is *fewer* hands, which the table above never tested — only increases
were tried, and both lost.

### 1 — WHEAT mirror (in hand)

Root cause, [a_v186.py:1599](a_v186.py:1599):

```python
for crop in ("STRAWBERRY", "MELON", "TOMATO"):
    strategic_target = min(crop_cap, int(math.ceil(0.90 * opp_wave_ready_counts.get(crop, 0))))
```

The mirror never iterates WHEAT, so the only wheat we ever plant is the
`day < 3` opener. The data matches the rule exactly: their strawberry 33.60 →
ours 29.91 ≈ 0.90 × 33.60; their wheat 25.04 → ours 7.62.

`opp_wave_ready_counts` is already built for every crop
([a_v186.py:1422](a_v186.py:1422)) — only the tuple needed changing. WHEAT is
placed **after** STRAWBERRY so the premium position is untouched and wheat
claims the budget that previously fell through to the residual scorer.

Functional diff is three lines (one behavioural, two telemetry):

```
<     for crop in ("STRAWBERRY", "MELON", "TOMATO"):
>     for crop in ("STRAWBERRY", "WHEAT", "MELON", "TOMATO"):
>         _MIRROR_PLANTED[crop] = _MIRROR_PLANTED.get(crop, 0) + n
> _MIRROR_PLANTED = {}
```

**Branch fires** (one game, seed 1042155578 vs `t_94142273_0`):

```
a_v186    day 19 tiles: WHEAT=7   STRAWBERRY=31  TOMATO=11  MELON=1
v206      day 19 tiles: WHEAT=12  STRAWBERRY=31  TOMATO=5   MELON=3
          mirror branch fired: {'WHEAT': 2182, 'STRAWBERRY': 93, 'MELON': 75}
```

Strawberry is untouched; wheat took tomato's slots. Wheat still reaches only 12
tiles against the rival's 25 — `room` and `crop_cap` bind before the 0.90
target does, so there may be a follow-up in raising the ceiling.

**Not evidence of strength.** The margin on that seed moved −41,574 → −23,399,
but it was the worst loss in the report and is a favourable cherry-pick by
construction. Needs the full 1,760-game run.

### Parked — FERTILIZER is sold into a belt with no sink

`TOWN_CENTER_PRODUCTS` excludes FERTILIZER and no shop lists it, so its
absorption is **0 units/season**: every unit sold ratchets the price down 0.2
permanently and it never recovers. Realized $67.74 → $25.66 → **$7.27**.

We produce ~358 units/season and spend only ~51 on FERTILIZE. At $7.27 a unit
selling is near-worthless, while a FERTILIZE on wheat doubles the water tick —
6 units in 3 waters instead of 5, i.e. a 5-day cycle becomes 3. It would
compound with change 1 — but "reserve fertilizer from sale" is exactly the
change that measured **−6,019 (t −5.0)** on the old engine. Do not re-run it
blind; if it is retried, the hypothesis must be that wheat acreage (change 1)
is what makes the reserved fertilizer worth more than the sale, which was not
true when the original test ran.

### 2 — the job board is admitted on the wrong objective

[a_v186.py:1774](a_v186.py:1774) sorts the board by raw value and truncates to
`HUNGARIAN_JOBS` = 48 columns; the cost matrix then scores
`value − move_rate * d`. A zero-travel job worth 300 loses its slot to 48 jobs
worth 301 sitting eight tiles away, which score deeply negative once the walk
is charged.

Telemetry says travel is the binding cost after day 15: movement runs
**152-167 worker-turns per game-day against ~150 productive ones**, while PASS
has already fallen to ~1/day. Half of all late-game labour is walking. That is
the volume gap — in days 20-24 the rival out-produces us on every line
(strawberry 109 vs 85, wheat 92 vs 42, fertilizer 78 vs 57, wool 32 vs 18,
milk 53 vs 42) while we realise *better* prices per unit on most of them.

`a_v207_jobboard.py` keeps `top_avg` / `move_rate` calibrated off the value
ordering — that is what "opportunity cost of a worker-turn" means — and changes
only admission: rank each job by its best case over the free workers, an upper
bound on any score it could win in the matrix.

**Branch fires** (one game, seed 1042155578 vs `t_94142273_0`):

```
a_v186   worker-turns 7,794   MOVE 4,161 (53.4%)   productive 2,858 (36.7%)
v207     worker-turns 7,762   MOVE 3,711 (47.8%)   productive 3,185 (41.0%)
         rerank fired: {'steps': 320, 'dropped': 13812}
         step latency median 2.4ms  p99 7.8ms  max 161ms  (actTimeout 1000ms)
```

450 walking turns converted into 327 productive ops, at no measurable latency
cost. Same cherry-pick caveat as v206: margin on that seed moved −41,574 →
−31,709, but it is the report's worst loss.

### Retracted — "melon is a trap"

An earlier draft of this roadmap called for suppressing MELON because its
season sink is 30 units and its price collapses to $47. The collapse is real
but the conclusion was wrong: **melon early is the most profitable crop we
plant.** Days 0-19 it returns 92.30 units at $150.30 = **$13,876** against
$1,762 of seed. The same ~10 tiles run as wheat for those 20 days would yield
roughly 240 units at $35.81 ≈ $8,594. Melon wins the early window by ~$3,900.

Only *late* melon is worthless, and we already barely plant it (10.45 units in
days 20-24, 2.9 after). There is no gap to close here. The residual scorer
ranking melon first is not, on this evidence, a defect.

### 3 — the agent's price table predates 1.32.7

1.32.7 introduced a `hinge` shape (`HINGE_GAIN = 8.0`,
`u + 8*max(0,u-1)**2`, `u = x/T`) on the below-I0 side of CARROT, TOMATO and
EGG, and raised CARROT's `below_target` 0.20 → 1.00. Past the knee a scarce
product's price runs away quadratically.

`a_v186`'s `MP` table and `_shape` were copied from 1.32.6, so against the live
engine:

```
item        x=I0-inv   agent  engine     err
CARROT           600      42     113     -71
TOMATO           600     132     900    -768
EGG              600      86     190    -104
```

Those are exactly the belts the rival does not contest — tomato 0.00 units,
egg 0.20, carrot 0.02. The agent can neither chase the spike nor defend it,
because it cannot see it. `a_v208_price_1327.py` syncs the table and `_shape`;
verified zero mismatches against `market_price` across ±1500 inventory on all
nine products.

Effect is subtle on a single seed (the hinge only bites when a product goes
genuinely short), so this one especially needs the full run.

## Loop

Three independent candidates, each `a_v186` plus one change, so all three
attribute cleanly against the same baseline:

- `a_v206_wheat_mirror.py` — WHEAT joins the strategic crop mirror
- `a_v207_jobboard.py` — job admission aligned to the matcher's objective
- `a_v208_price_1327.py` — price model synced to engine 1.32.7

Smoke, engine 1.32.7, seed 1042155578 vs `t_94142273_0` (one game each —
mechanism proof, not strength):

```
agent                        margin   MOVE%  prod%  wheat@d19
a_v186.py                   -41,653   53.4%  36.7%          7
a_v206_wheat_mirror.py      -23,385   52.7%  37.6%         12
a_v207_jobboard.py          -31,752   47.8%  41.0%         11
a_v208_price_1327.py        -35,404   53.2%  36.7%          6
```

They touch disjoint subsystems (crop selection / worker assignment / price
model), so if they hold up they should compose.

### Negative results — do not re-derive these
**Dropping Geese crashes crop markets.** Tested dropping Geese and lowering target to 12. Removing Geese frees 4 tiles and 1,200 coins, which the residual allocator dumps into Strawberry/Melon. This crashes their highly sensitive price curves (`linear, 1.60` and `sq, 3.60`). Eggs (`log, 0.20`) are the ONLY asset that can safely absorb our early-game tile/cash surplus without crashing. Geese are structurally load-bearing for this agent.

**Season-horizon mirror (v210, built and discarded).** Extending the mirror's
`day + maturity > CASH_WAVE_END_DAY` gate to `LAST_DAY` so STRAWBERRY keeps
being matched past day 14. Built twice and measured **byte-identical games**
both times:

- gate only: inert, because `opp_wave_ready_counts` is keyed on the same
  constant, so the rival's late plantings are invisible too and the deficit is
  structurally zero;
- gate plus matching season-horizon counts on both sides: still inert
  (`_MIRROR_PLANTED['STRAWBERRY']` = 93 in both). We already match their
  strawberry through days 15-19.

**Why the strawberry gap actually exists.** It is the mirror factor, by design:
they hold 33.26 tiles at day 19, we hold 29.84, and `0.90 x 33.26 = 29.93`.
Closing it means raising 0.90 toward 1.0, which takes slots straight back from
the wheat that just won +9.1 points. That is a tuning knob with a known
opposing cost, not a structural fix — do not spend a cycle on it before the
wheat conversion result is in.

**`late_terminal_crop_mix` is correct.** Strawberry gets no slots from day 20
because `fyd` 10 puts its first yield on day 30, past `LAST_DAY`. Not a bug.

### Melon is lost on timing, not volume (measured)

v206 losses carry a $3,486 melon gap across days 0-19 that is **entirely
price**: realised $165/unit against the rival's $200. Melon's whole-season town
sink is 30 units and `above_target` is 3.60, so the price crashes
quadratically with combined supply and never recovers — the split between the
two farms is decided purely by who sells first.

Traced on seed 1042155578. Our melon shed is **0 all game**, so sale policy is
not the constraint; we sell everything we harvest, immediately:

```
        d10   d11  d14  d16  d17  d23   qty-wtd quote
us       17     -    6   18   42   24        $139.0
opp      60    12    -    6   30   12        $159.3
```

Melon matures on day 10 (`fyd` 10) with ~15 tiles x 6 units ready, and HARVEST
takes a tile's entire yield in one action — 15 actions against ~312 worker-turns
in the day. HARVEST is already valued at `held x spot` = 6 x $272 = $1,632, so
priority is not the blocker either. **Their melon matures as one cohort; ours is
staggered**, which is a planting-cohort property, not a harvest-priority one.

**v209 already fixes this, and fixes it better.** A melon-specific candidate
(`a_v211_harvest_race.py`, adding `one_unit_denial_bonus` to HARVEST for
crash-prone crops) reached a weighted quote of $147.6. `a_v209_wheat_surplus.py`
reaches **$158.1** against the rival's $159.3 — on the same seed, with day-10
volume unchanged at 17:

```
v206                     melon wtd quote  $139.0
v211 (melon-specific)                     $147.6
v209 (banking fix)                        $158.1     rival: $159.3
```

The banking gate was throttling **all** produce, not just wheat: a worker
carrying any wheat alongside melon was blocked from the shed, and SELL requires
the goods to be in the shed. Fixing the gate lets every crop reach the market on
time. v211 is strictly dominated and has been deleted.

This raises v209's expected value: it targets the $17,025 wheat gap **and** the
$3,486 melon gap through one mechanism.

### Melon cohorting — the prize is real, small changes cannot reach it

Priced with the engine's own `sale_value` on measured volumes (seed 1042155578,
us 103 units vs their 120):

```
they dump 60 first, we trickle (current)   us $12,189   $118.3/unit
we sell our whole 103 first                us $22,165   $215.2/unit   +9,976
we dump 60 first, then they                us $14,344   $139.3/unit
perfectly interleaved 1:1                  us $13,325   $129.4/unit
```

+9,976 coins is comparable to the whole wheat gap, so this lever is alive. Two
measurements bound how to reach it:

**We already win the day-10 race.** Step-level trace under v209: we sell at
hours 12-13, the rival starts at hour 17. v209 alone lifts the melon weighted
quote $139.0 -> $158.1 against their $159.3. Racing harder buys almost nothing.

**The loss is cohort maturity, and a planting cutoff does not fix it.**
`a_v212_melon_cohort.py` (skip MELON after day 2) was built and discarded:
day-10-ready units moved only 28 -> 25, because melon planted on days 0-2 still
matures across days 10-12. It cut volume 103 -> 75 while lifting price to
$190.0/unit — net revenue $14,250 against v209's $16,284.

To actually capture the $9,976 the farm needs ~100 melon units mature on ONE
day, which means a single-day planting of ~17 tiles plus shed management for a
100-unit dump against `SHED_CAP` 100. That is two coordinated mechanisms, not a
one-line change, and it competes with the day<3 wheat opener for the same early
slots. Do not attempt it before v209 is measured.

### v209 local screen (20 games, paired, at the local cap)

Same (opponent, seed, seat) for both agents; `screen_pair.py`.

```
opponent           cand W-L   base W-L   mean margin delta
t_94133552_0          2-0        2-0            +8,125
t_94141444_0          2-0        2-0           -11,096
t_94172951_0          2-0        0-2           +11,697   <-- 2 cells gained
t_94173920_0          2-0        2-0           +21,738
t_94177272_0          0-2        0-2              +934

margins:   n=5 opponents, mean +6,280, sd 12,270, t +1.14, positive 4/5
win rate:  candidate 8/10 (80%) vs baseline 6/10 (60%), +20 pts,
           2 cells gained, 0 regressed
```

Two methodology corrections came out of this and are now baked into
`screen_pair.py`:

**Mirrored seats are one observation, not two.** For some opponents the seat
swap returns exactly mirrored rewards (verified: 81,194/80,360 ->
80,360/81,194), so the margin is identical. Counting both inflated the first t
from a true +1.14 to +1.55. The tool now aggregates per opponent.

**Margin is the wrong statistic; win rate is the scoreboard.** The one negative
cell (t_94141444_0, -11,096) is not a failure -- both agents WIN it, +38,936
against +30,697. Margin punished v209 for winning by less, which scores
nothing. On cells, v209 gains 2 and regresses 0.

A candidate that regresses no cell is safe to spend a full run on even when the
margin t is weak.

### Melon cohort — CLOSED, structurally unreachable

The +9,976 prize assumes ~103 melon units ripe on one day, i.e. a single-day
planting of ~17 tiles. Measured early-game budget (seed 1042155578, v209):

```
day  unlocked  empty   cash
  0        25     10     $45
  5        25     10  $1,112
  6        50     14    $578
```

Day 0 offers **10 empty tiles and $45** against a requirement of 17 tiles and
$1,360 of seed. The second quadrant does not unlock until day 6, and melon
planted then ripens on day 16 -- after the rival's day-10 cohort has already
taken the top of a curve that never recovers (30-unit season sink).

The farm cannot physically create the cohort the prize depends on. Melon is
closed: v209 already captures the reachable part of it ($139.0 -> $158.1/unit
against the rival's $159.3) by getting produce to the shed on time.

## Ledger

| status | item |
|---|---|
| adopted | v206 wheat mirror (+9.1 pts), v209 wheat surplus banking (+8.7 pts), 50.0% -> **67.8%** |
| rejected | v207 job admission (-9.8), v208 price sync (-0.3) |
| discarded pre-benchmark | v210 season mirror (inert x2), v211 harvest race (dominated by v209), v212 melon cutoff (revenue-negative) |
| closed | melon cohort (unreachable), FERTILIZER reserve (-6,019), 6 axes from the v140 table |
| open, has opposing cost | strawberry 0.90 mirror factor -- trades directly against v206's wheat slots |

Everything reachable without a full benchmark cycle has been taken. The next
step depends on where v209 lands.
