---
name: v140-only-deleting-work-wins
description: "On Kaggriculture v140, deleting fake job-board priority is the only change class that raises win rate — 77.6% to 86.4% — while six other axes are measured dead."
metadata: 
  node_type: memory
  type: project
  originSessionId: fc4033e5-1cec-4206-81f6-8cf2efa8416b
  modified: 2026-08-17T20:35:08.090Z
---

As of 2026-08-16, v140 is **labour-bound**: 13 workers, ~63 assets, 51% of
worker-turns spent moving, PASS 1.6/day. A freed worker-turn is the only
currency, so **the winning question is not "is this action wasteful?" but "how
much priority is this fake signal commanding?"**

Benchmark progression (1600 games, 80 opponents):

| agent | record | win rate |
|---|---|---|
| baseline | 1241-359 | 77.6% |
| + suppress no-op FERTILIZE/WATER (capped + doomed tiles) | 1270-330 | 79.4% |
| + stop advertising the +1000 WATER bonus on a capped tile | 1365-235 | 85.3% |
| same agent, **held-out seeds** (`--offset 10`, k=11..20) | **1383-217** | **86.4%** |

The third change alone beat the first two 3:1, because 1,000 is enormous next to
a real job value of 40-600 — a capped MELON tile was stealing a *top-priority*
worker slot to buy exactly nothing.

Six axes swept, each with a control point that scored exactly +0 (harness sound),
all lost: re-pricing service jobs −4,746 · DIG reclaim −5,281 · reserve
fertilizer −6,019 · all three −7,873 (0W-24L) · 4th quadrant −5,009 · `move_rate`
median sweep −3,490…−9,522 · `MAX_HANDS` 14/16/18 −4,947/−24,702/−50,717.

The big `move_rate` (~7,872 per tile walked) is load-bearing: nearest-job-first
maximises services delivered on a dense board. Wages are Fibonacci
(`hire_bill(18)` = $6,764/day, hands rebought daily).

Full detail, open leads and reproduction commands: `V140_SERVICE_LOOP_FINDINGS.md`.

**The `crop_cap` axis is closed in BOTH directions.** Lowering loses (0.36
−11.0, 0.30 −18.9) and raising loses too: `v157_cap50` (0.50/0.62) benchmarked
**1328-272 (83.0%)**, −3.4 points against the champion, despite winning a
hard-tape sanity check by +1,940 paired margin at t +2.59. Do not re-open it,
and do not trust a 16-game paired sanity check as evidence of a real gain —
that one pointed the wrong way with a healthy t-statistic.

**The original rule was too strong; the corrected form still holds.** Deleting
capacity loses (drop TOMATO −22.6, the crop caps above) and *adding* capacity
also loses (v157). What wins is deleting work the engine discards or punishes.

**Two more failures narrow it further.** `v160_growfirst` (suppress HARVEST on a
still-growing WHEAT tile) benchmarked **1302-298 = 81.4%**, −5.0 points, even
though its mechanism fired exactly as designed —
[[non-ongoing-crops-are-destroyed-by-their-own-harvest]]. And `v161_freehaul`
(stop the forced mid-day shed trip, since engine `:865` banks every inventory
free at end of day) died at smoke stage: shed traffic is driven by PICKUP jobs
priced at 600, not by banking, and starving the shed starves the sell pipeline
that reads `shed_used`.

So per-unit yield and haulage are both dead ends. The live axis is **which jobs
the assignment matrix is allowed to see** —
[[job-board-truncation-drops-zero-travel-jobs]].

**The rule has a hard limit, found 2026-08-17: a provably-zero-yield job can
still be load-bearing as a proximity anchor.** `a_v180_merged.py` is the
champion at **1412-188 (88.2%)**. Watering an ongoing crop (STRAWBERRY/TOMATO)
on a non-production day provably adds nothing — `_daily_refresh_plants` only
ticks on the interval, and the `+1` lands watered or not — yet v180 advertises
it at the full crop spot every day. Gating it to production days deleted 238
dead waterings/game and did **not** raise weeds (26 → 23), but measured
**negative** over 6 paired smoke games: strawberry units **198.8 → 185.7**,
FERTILIZE **57.5 → 51.2**, PASS **+71**, mean margin **−960**. The columns were
holding workers inside the strawberry block; with the large `move_rate`,
removing them made *all* strawberry work uncompetitive. Never shipped.

`a_v183_adaptive_herd_reserve` (cap the speculative herd at 14 until four shops
are visible) benchmarked **1254-346 = 78.4%**, −9.8 points, and the herd it
produced was GOOSE 1.6 / SHEEP 5.8 / COW 8.6 against v180's 1.9 / 5.6 / 8.5 —
**still 16 animals, same species mix**. It delayed the buys, the same greedy
loop picked the same species at day 12, and ~1,756 of early lead paid for it.
Deferring capacity is the same losing class as deleting it.

**The animal axis is closed — the herd plan is a non-binding over-plan.**
`a_v184_guarded_residual_species` wired up v180's dead
`allocate_residual_species` helper (`:605`, defined but never called) to swap at
most one COW↔SHEEP in the speculative fallback. Telemetry confirms the branch
fires **16.3 times/game**, always COW→SHEEP — yet across 6 paired smoke games
the herd was **identical in every single game** (5/8/5, 6/6/4, 3/9/4 on both
sides) and the seat-0/seat-1 margins were exact negatives (−8,586/+8,586,
+7,383/−7,383, −2/+2), the signature of a pure mirror. **v184 plays exactly like
v180.** Cause: the fallback emits a speculative over-plan (`base={'COW': 10}`
for a herd that lands at 8) which money, shop stock and structure demand clip
downstream, so editing one unit of it changes nothing.

Size the axis before touching it again: day 20-24 loss gap is **+12,048.6**,
strawberry revenue gap alone is **+14,404.6**, and the animal *spend* gap moves
only **~65 coins** between wins and losses. The opponent's herd is unchanged
between our wins and losses (COW 7.7→7.8, SHEEP 4.2→4.2) — only ours drifts
(COW 8.5→9.9, SHEEP 5.6→4.2), so our mix is a *symptom* of the market state that
beats us, not a cause. See [[v180-losses-are-strawberry-price-spikes]].

**`MAX_HANDS` is now closed in BOTH directions.** The recorded sweeps only went
up (12→14 −4,947, 12→16 −24,702, 12→18 −50,717). Downward was untested and the
wage evidence looked good — the loss analysis shows wage spend day 0-19 at us
5,001.1 vs the top players' 2,956.1, i.e. we run ~11 hands where they run ~10.
`a_v189_leaner_crew` (12 → 10) measured **mean −1,685, t = −1.21, 3/8 seeds**
over 16 paired games. It did exactly what it was built to do — PASS −136.7,
MOVE −506.1 — and delivered less: HARVEST −35.6, ongoing units −7.2,
strawberry −4.0. Fewer hands is fewer services; 12 is the optimum.

**How to apply:** ask whether a change deletes a no-op action (good), deletes
capacity (always lost), or adds capacity that is provably idle (the new, working
class). Verify any branch fires before spending a benchmark slot — CARE-on-capped
animals looked identical to the winning pattern but touches only 1.1% of jobs.
See also [[mirror-screening-is-blind-to-real-gains]],
[[kaggriculture-candidate-loop]] and [[v140-service-loop-is-a-local-optimum]].
