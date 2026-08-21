---
tags:
  - kaggle
  - moc
project: Kaggriculture
status: in-progress
baseline: a_v209_wheat_surplus
win_rate: 67.8%
target: 80%
engine: kaggle-environments 1.32.7
updated: 2026-08-20
---

# Kaggriculture

> [!abstract] What this is
> A Kaggle two-player farming simulation. 30 in-game days = 720 turns, 10x10
> board in four 5x5 quadrants, dynamic market. Winner = most money banked.
> Our agent lineage is **deterministic rule-based heuristics -- explicitly no RL**:
> a per-turn job board, a Hungarian assignment of workers to jobs, and a
> rolling forecast of market absorption.
>
> This note is the map. Everything else in the vault hangs off it.

## Current state

```text
a_v186   (baseline, superseded)   880-880    50.0%     --
a_v206_wheat_mirror              1040-720    59.1%   +9.1   OLD baseline
a_v208_price_1327                 874-886    49.7%   -0.3   noise
a_v207_jobboard                   707-1053   40.2%   -9.8   REJECTED
a_v209_wheat_surplus             1193-567    67.8%   +8.7   ADOPTED (but see note below)
a_v209_wheat_surplus (vs v195)      9-11      45.0%   -5.0   Smoke Test (20 games)
a_v213_no_goose                  1174-586    66.7%   --     
```

> [!important] Scoreboard Discrepancy (v195 vs v209)
> Although we changed the loss analysis script and benchmarked the v209 as the best agent with 68% and v195 with 50% but on kaggle scoreboard v195 is peforming much more better. Need to Identify this thing. Our new loss analysis is not worth it.

n = 1760 (88 opponent tapes x seeds k=11..20 x 2 seats), engine 1.32.7.
**One standard deviation is +/-1.19 points** -- anything under ~2.4 pts is noise.

> [!warning] The 68% to 50% drop was not a regression
> `a_v186.py` is byte-identical across both measurements. The Kaggle notebook
> runs `pip install -U kaggle-environments` every session, so it silently
> adopted a new engine. Town-centre demand fell from 8 units/product/day
> (day 20+) to **1/day flat** -- season absorption per product 140 to 30.
> Old margins do not replay on 1.32.7; new ones reproduce to the coin.
> See [[engine-upgraded-and-reset-the-baseline]] and [[V206_ROADMAP]].

## Next action

`a_v209_wheat_surplus.py` is built, fully measured, and **ADOPTED** (67.8% win rate). The next step is to proceed to the strawberry 0.90 factor or fewer hands. The user runs the full sets on Kaggle:

```bash
cd /kaggle/working/bisect && python -u _loss_analysis.py a_v209_wheat_surplus.py --workers 222 --seeds 10 --offset 10
```

Two numbers to read first in the report:

1. **wheat revenue d20-24** -- v209 successfully closed the wheat revenue gap.
2. **`cash_residual`** -- market accounting remained stable.

With the wheat-conversion thesis proven, the diagnosis now shifts to the next lowest-hanging fruit (strawberry factor).

## Start here

| If you want... | Read |
| --- | --- |
| the game rules, price curves, full tables | [[README]] |
| how to build / test / submit an agent | [[AGENTS]] |
| how to restart a session cold | [[HANDOFF]] |
| the live plan and the ranked queue | [[V206_ROADMAP]] |
| the strategy derivation from engine source | [[STRATEGY]] |
| what the agent measurably does wrong | [[V186_LOSS_DIAGNOSIS]] |
| every hard-won fact, one per note | [[MEMORY]] |

## Where the money is lost

Net cash across all games splits cleanly by phase:

| window | us | opp | delta |
| --- | --- | --- | --- |
| d0-19 | +36,251 | +30,091 | **+6,160** |
| d20-24 | +23,895 | +26,217 | -2,323 |
| d25-29 | +21,639 | +23,631 | -1,992 |

We win the first two thirds and hand it back. Realized prices
(`revenue / units` on filled orders only) say which belts are short:

| product | base | d0-19 | d20-24 | d25-29 | reading |
| --- | --- | --- | --- | --- | --- |
| **WHEAT** | 25 | 35.81 | 48.64 | **51.36** | short, rising all season |
| TOMATO | 60 | 66.46 | 72.27 | 76.56 | short, rising |
| EGG | 50 | 53.87 | 57.73 | 60.61 | short, rising |
| CARROT | 35 | 40.45 | 40.52 | 41.66 | short, flat |
| STRAWBERRY | 120 | 198.69 | 166.39 | 108.87 | good early, saturates by d25 |
| MILK | 160 | 179.47 | 151.65 | 132.67 | saturates from d20 |
| WOOL | 200 | 168.52 | 165.64 | 127.34 | **always below base** |
| MELON | 250 | 162.87 | **51.77** | 47.51 | 30-unit season sink |
| FERTILIZER | 100 | 67.74 | 25.66 | **7.27** | **zero sink, pure ratchet** |

A product realizing above base is a belt running below capacity. Four are short
all season and we are barely in three of them.

## Engine facts that bite

- **1.32.7 `hinge` curve** on CARROT / TOMATO / EGG below `I0`:
  `u = x/T; u + 8*max(0, u-1)**2`, and CARROT's `below_target` went 0.20 to 1.00.
  Measured neutral in play ([[engine-upgraded-and-reset-the-baseline]]).
- **FERTILIZER has no sink at all** -- not in `TOWN_CENTER_PRODUCTS`, in no shop.
  Its price is a one-way ratchet down.
- `shedCapacity = 100` total, and end-of-day overflow is **discarded**.
- `DROP` dumps a worker's **entire** inventory; `PLACE item n` banks a quantity.
  `FEED` pulls WHEAT from the **worker's** inventory, not the shed.
- The market is a per-unit lockstep loop: both players quote, player 0 commits
  first, and an order **aborts on the first failed unit**.
- Kaggle resolves a submission as `[v for v in env.values() if callable(v)][-1]`
  -- the **last callable wins, whatever its name**. A silent failure mode; see
  [[kaggle-entry-point-must-be-last-callable]].
- `_env_src.py` must be re-copied from the installed engine, never trusted as a
  snapshot -- a stale copy produced a confident wrong finding. See
  [[env-src-must-be-copied-from-installed-engine]].

## Hard-won facts

One note per fact, in `context/`. Each cost a benchmark cycle -- do not
re-derive them.

- [[v206-wheat-mirror-won-conversion-is-next]] -- the current thesis
- [[engine-upgraded-and-reset-the-baseline]] -- why the baseline moved
- [[the-gap-vs-top-players-is-the-dawn-ramp]] -- hours 0-3, CARE 39.4 vs 14.6
- [[move-rate-inflated-by-synthetic-priority-flags]] -- safe as a ranking,
  destructive as a veto
- [[job-board-truncation-drops-zero-travel-jobs]] -- 2,003 under-foot jobs cut
- [[v180-losses-are-strawberry-price-spikes]] -- the 88.2% era's loss shape
- [[non-ongoing-crops-are-destroyed-by-their-own-harvest]] -- real mechanism,
  the fix still lost
- [[v140-only-deleting-work-wins]] -- six axes measured dead, one deletion won
- [[v140-service-loop-is-a-local-optimum]] -- the price gates are correct
- [[loss-analyzer-inflates-opponent-revenue]] -- the analyzer bug, now fixed

## Rules of engagement

- [[kaggriculture-candidate-loop]] -- one hypothesis, one change, prove the
  branch fires, hand over the filename. **Do not stack two changes.**
- [[never-run-local-benchmarks-over-20-games]] -- hard cap. Smoke tests are 1-4
  games; the user runs full sets on Kaggle.
- [[kaggriculture-benchmark-workflow]] -- build + smoke test only; never write
  to Kaggle unasked.
- [[mirror-screening-is-blind-to-real-gains]] -- a mirror match called parity on
  a change worth +1.8pp. Use `screen_pair.py` for anything near zero.
- [[kaggriculture-file-locations]] -- deliver agent files to Downloads **and**
  the repo, and re-sync after edits.

## Dead ends

Closed by measurement. Any retry needs a reason why the engine change flips the
sign.

| change | result |
| --- | --- |
| job-board admission scored on `value - move_rate*d` | **-9.8 pts** (v207) |
| reserve FERTILIZER from sale like WHEAT | -6,019, t -5.0 |
| re-price HARVEST / CARE / FEED off a floor not spot | -4,746, t -3.21 |
| reclaim decayed tiles + weeds with a real DIG value | -5,281, t -4.32 |
| widen FERTILIZE into the full 3-day buff window | -1,057, t -0.90 |
| buy the 4th quadrant | -5,009, t -3.05 |
| MAX_HANDS 12 to 14 | -4,947, t -5.49 |
| MAX_HANDS 12 to 16 | -24,702, t -28.1 |
| season mirror (v210), harvest race (v211), melon cohort (v212) | inert / unreachable, discarded |
| per-tile melon yield fix (v160) | lost at 81.4% |

Only *increases* to `MAX_HANDS` were ever tested. **Fewer** hands is still open
-- wages run +58% vs the rival while PASS is about 96/game.

## Tooling

| file | what it does |
| --- | --- |
| `_loss_analysis.py` | entry point for the full benchmark + report |
| `_econ_loss_analysis.py` | exact per-seat market replay (`replay_market`) |
| `screen_pair.py` | 20-game paired local screen; reports cells regressed |
| `_which_engine.py` | identifies engine version from a recorded episode alone |
| `_duel.py` | single head-to-head run |
| `_env_src.py` | working copy of the engine -- **re-copy before trusting** |
| `.top/t_*.py` | 88 extracted opponent tapes |

The Kaggle dataset `kg-bisect` carries `_duel.py`, `_econ_loss_analysis.py`,
`_loss_analysis.py`, `_which_engine.py`, `screen_pair.py` and the agent files.
`grid_search` carries the opponent tapes.

## Benchmark reports

- [[a_v206_wheat_mirror_loss_analysis]] -- the adopted baseline
- [[a_v207_jobboard_loss_analysis]] -- the -9.8 rejection
- [[a_v208_price_1327_loss_analysis]] -- the neutral price sync
- [[v186_loss_analysis]] -- the corrected 50.0% baseline
- [[REPLAY_ANALYSIS_91759]] -- single-episode replay teardown
