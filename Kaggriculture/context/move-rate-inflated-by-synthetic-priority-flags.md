---
name: move-rate-inflated-by-synthetic-priority-flags
description: "In Kaggriculture v180, move_rate is the mean of the top-N job values and is inflated ~65x by synthetic +50000 priority flags; the repair pass uses it as an absolute veto and refuses ~303 feasible jobs per game."
metadata: 
  node_type: memory
  type: project
  originSessionId: fc4033e5-1cec-4206-81f6-8cf2efa8416b
  modified: 2026-08-17T20:31:44.034Z
---

Measured on `a_v180_merged.py` over 2 instrumented games (2026-08-17):

```
move_rate mean          23,584.6      <- what the code uses
move_rate if clean         359.8      <- same formula, synthetic jobs excluded
top-N jobs >= 1,000       3.12 of 8.82  (35%)
top-N jobs >= 10,000      2.47
PASS total                   749 /game
  .. with jobs still left    306  (41%)
  .. best residual        -20,482
repair rejects resid<=0      303 /game
```

`move_rate = MOVE_FRAC * mean(top active_jobs job values)` (`:1822`,
`MOVE_FRAC = 1.5`). The WATER pricing adds a synthetic **+50,000** when
`consecutive_unwatered >= 1` and **+1,000** in the yield window — priority
flags, not coins. On a typical turn 2.5 of the ~8.8 top jobs are those flags,
so the "opportunity cost of one worker-turn" reads 23,585 coins per tile.

**The same number plays two different roles, and only one is load-bearing:**

- Main Hungarian (`:1863`) uses it to RANK: `-(value - move_rate*d)`. Since
  every entry is dominated by `-move_rate*d`, minimising total cost degenerates
  to nearest-job-first — which [[v140-only-deleting-work-wins]] shows is
  correct on a dense board. Harmless here.
- Repair pass (`:1974`) uses it as an absolute VETO:
  `if residual_score <= 0.0: row.append(BIG)`. At 23,585/tile that rejects
  essentially every job at d >= 1 — **303 rejections/game** — and those workers
  fall through to `["PASS"]` (`:2077`) or the unguarded idle-DROP (`:2056`).

Sizing: on real leaderboard replays we PASS **11.5%** of worker-turns against
current top players' **9.7%**, i.e. ~+134 idle turns/game — the same order as
the 303 vetoed assignments. The `:2072` comment shows v180 deliberately *raised*
PASS to chase a "14.9%" figure taken from the local `.top/` panel; against the
current leaderboard that target is wrong, and we overshot.

**Why the old MOVE_FRAC sweeps do not close this.** The recorded failures
(0.25 → −3,490; 10.0 → −9,522; median sweeps −3,490…−9,522) all replaced
move_rate **globally**, breaking the main pass's nearest-job-first ranking.
Changing only the repair veto is a different, untested edit.

**Candidate built on this:** `a_v186_repair_veto.py` — two-line diff,
`veto_rate = MOVE_FRAC * jobs[ncand // 2][0]` (median of the already-sorted
admitted jobs) used for the gate only; the cost row still uses `move_rate`, so
nearest-job-first is bit-for-bit unchanged.

**Smoke, 8 seeds / 16 paired mirror games, seat-cancelled: mean +115, sd 2,793,
t = +0.12** (5/8 seeds positive, 8/16 games). Dead neutral on margin — but every
behavioural metric moved as designed over the 10-game batch: PASS −12.2,
DROP −4.6, MOVE −15.2, FERTILIZE +2.7, ongoing units +2.7. The mechanism fires;
the mirror cannot price it, which is the exact regime
[[mirror-screening-is-blind-to-real-gains]] describes.

Seed-level detail: +630, +1710, +1601, +838, −3831, −2896, −1804, +4669. On the
losing seeds (41, 53) FERTILIZE and strawberry moved the *wrong* way — waking a
worker for any job clearing the lower gate can displace a fertilizer run. If a
tighter form is wanted, the measured honest rate is ~360 (top-N mean excluding
synthetic flags) versus the median actually used; the two could not be
distinguished at this sample size, so the threshold-free median was kept.

**THE AXIS IS CLOSED — the inflated rate is load-bearing in every window.**
Three candidates, all built on the honest median rate, differing only in where
it applies:

| candidate | scope | 16-game paired smoke |
|---|---|---|
| `v186_repair_veto` | repair-pass veto only | **+115, t = +0.12** (neutral) |
| `v187_honest_move_rate` | whole assignment, all day | **−3,933, wins 1/16** |
| `v188_morning_rate` | whole assignment, hours 0-3 only | **≈ −5,286** (8 games, stopped) |

v187's behavioural deltas say exactly why: MOVE **+284.6**, HARVEST **−40.7**,
PASS **+44.1**. An honest rate lets workers chase distant value and they deliver
less. The 23,585 figure is not a bug to fix — it is what collapses the
assignment into nearest-job-first, and on a dense board that maximises
throughput. Only v186's narrow form (a gate the main ranking never sees)
survives, and it survives as noise.

v188 is the sharpest warning: its self-play output was **+33%** over v180
(213,562 vs 160,274) and it still lost head-to-head. Across v186/v187/v188,
self-play total was *anti*-correlated with head-to-head margin — never treat
mirror output as evidence of strength.

**How to apply:** when a constant serves both as a ranking weight and as a
threshold, check each role separately — a value that is harmless (or helpful)
as a ranking can be destructive as a gate. But do not reopen move_rate itself.
