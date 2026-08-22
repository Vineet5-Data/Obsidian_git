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
agent                 pool win%   real-agent W-L (2 seeds)   verdict
a_v186                   50.0%    7-1 / 5-1 / 1-3 / 2-2      BASELINE (restored)
a_v206_wheat_mirror      59.1%    identical to v186, 4/4 seeds  INERT no-op
a_v180_merged               --    2-6 / 2-4 / 2-2 / 0-4      beats v186 on 1 of 4 seeds
a_v213_no_goose          66.7%       4-4  /  0-6            de-adopted
a_v209_wheat_surplus     67.8%       0-8  /   --            DE-ADOPTED, loses to all
a_v208_price_1327        49.7%        --                    noise; correctness only
a_v207_jobboard          40.2%        --                    REJECTED
```

Pool win% is measured against 88 open-loop replays and **does not rank agents**.
Real-agent W-L is `_roundrobin.py`, 4 seeds. v186/v180 is not settled
(v186 takes 3 of 4, margins swing +/-6k); v209 and v213 are. Confirmed
independently by your v209-vs-v180 head-to-head (9-11) and the leaderboard.

> [!success] Scoreboard Discrepancy — RESOLVED 2026-08-21
> **The benchmark opponents cannot react.** Every `.top/t_*.py` is an open-loop
> replay whose entire agent is `act = _ACTIONS[obs.step]` — it never reads its
> farm, its cash, the market, or us. The actions were recorded in a *different*
> game, so replayed here they reference tiles, seeds and cash that need not
> exist.
>
> The only channel we have to a tape is the **shared market**. So an agent that
> trades harder breaks more of its scripted orders and wins **without farming
> better**. Against a do-nothing PASS control, one tape scored 147,083 and fell
> to 87,481 against v209 — its own score swings −60k to +15k on *who it plays*,
> which is larger than almost every margin we have been reading.
>
> `_roundrobin.py` re-ranks the same agents against each other, where both sides
> respond. **The pool ordering is close to the reverse of the truth**, and your
> leaderboard observation is correct.
>
> Two adoptions are void: **v209 is de-adopted** (baseline reverts to `a_v186`),
> and **v206's +9.1 is void** — v186 and v206 returned byte-identical results in
> all 14 round-robin games, so the wheat mirror never fires against a reactive
> opponent.
>
> Your instinct was half right: the loss analysis *arithmetic* is sound (market
> replay, residual ~0.5%) — it is the **opponent pool** that cannot rank agents.
> Keep the report for diagnosis; adopt with `_roundrobin.py`.
> See [[top-tapes-are-open-loop-replays]].

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

Rank candidates against **reactive** opponents before adopting anything:

```bash
python _roundrobin.py
```

Then re-test the ideas that the tape pool mis-scored. The engine mechanisms found
this cycle were read from source and verified by patching the engine directly, so
they survive; only the win rates attached to them do not.


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
| **v207** align job admission with the assignment objective | 3-13 vs v186 over 8 seeds -- the pool's -9.8 rejection was right, by accident |
| **v225** rank species by return per worker-action | inert -- gross and per-action rankings agree |
| **v223** early herd target scaled to land | 1-7 vs v186 -- the herd at 16 is load-bearing |
| **v224** early herd target flat 13 | 2-6 vs v186 -- same conclusion from the other angle |
| **v221** MAX_HANDS 12->10 | 10-14 vs v186 -- worse than the baseline |
| **v222** MAX_HANDS 12->11 | 7-9 over 8 seeds, mean margin +38 -- null. MAX_HANDS is settled both ways |
| `a_v188_nogeese.py`, `a_v206_wheat_mirror.py` | inert -- dead-code edit / identical to v186 |
| **v220** rescue banked CARE on unfed tick days | **7-5 vs v186's 10-2** (3 seeds, roundrobin). Branch fired hard: 1,236 jobs, animal output +39 units (MILK 249->280, WOOL 88->96). Output rose, margin fell -- the FEED turns cost more than the bonus returns. |

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
- [[a_v213_nogoose_loss_analysis]] -- 66.7% on the pool, 0-6 against real agents
- [[v186_loss_analysis]] -- the corrected 50.0% baseline
- [[REPLAY_ANALYSIS_91759]] -- single-episode replay teardown
