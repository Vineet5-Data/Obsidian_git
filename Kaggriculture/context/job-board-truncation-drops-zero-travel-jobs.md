---
name: job-board-truncation-drops-zero-travel-jobs
description: "Kaggriculture v140 ranks the job board by raw value and keeps the top 48, but the assignment matrix optimises value - move_rate*d; jobs under a worker's feet (d=0) are cut before the objective sees them - 2,003 per game."
metadata: 
  node_type: memory
  type: project
  originSessionId: fc4033e5-1cec-4206-81f6-8cf2efa8416b
  modified: 2026-08-17T07:37:16.493Z
---

The champion truncates the job board **before** the objective is applied:

```python
jobs.sort(key=lambda j: -j[0])      # raw value only
ncand = min(len(jobs), HUNGARIAN_JOBS)   # 48
...
row.append(-(value - move_rate * d))     # what is ACTUALLY optimised
```

The filter ranks on `value`; the matrix maximises `value - move_rate*d`. A job on
the tile a worker already stands on has `d == 0` — the objective's best case —
and is still discarded whenever its raw number misses the top-48 cutoff.

Measured (`probe_underfoot.py`, one game vs `t_91631405_0`), under-foot jobs cut:

| op | cut | cut% | median value | cutoff |
|---|---|---|---|---|
| CARE | 797 | 57.7% | 90 | 192 |
| COLLECT_FERTILIZER | 476 | 46.9% | 128 | 171 |
| HARVEST | 296 | 35.4% | 62 | 150 |
| DIG | 22 | 56.4% | 18 | 76 |
| WATER | 77 | 6.6% | 185 | 192 |
| **TOTAL** | **2,003** | **31.5%** | | |

**Why this is the real defect:** it rank-correlates exactly with how far we walk
per job against real top players (10 leaderboard losses in `New_Losses/`):
CARE 0.96 vs their 0.11, COLLECT_FERTILIZER 1.16 vs 0.41, HARVEST 1.38 vs 0.99 —
and WATER, the one operation we barely cut, is the one where we are *not* worse
(1.38 vs 1.47). Opponents chain FEED→CARE→COLLECT on one tile; we leave and come
back. Working turns per game: us 6,666, them 5,612.

**How to apply:** admit under-foot jobs on top of the value-ranked window, and
keep computing `top_avg`/`move_rate` from the value-sorted prefix so the
opportunity-cost calibration is untouched. Extra columns can never lower a
Kuhn-Munkres optimum, so this widens what the existing pricing may choose from
rather than repricing anything — that is what makes it distinct from the
`move_rate` sweeps and from v53's wider job list, both of which lost. Shipped as
`v162_underfoot.py`. Residual risk: if `move_rate` is over-penalising travel the
agent now prefers junk under its feet to good work a few tiles away.

See also [[v140-only-deleting-work-wins]], [[kaggriculture-candidate-loop]],
[[mirror-screening-is-blind-to-real-gains]].
