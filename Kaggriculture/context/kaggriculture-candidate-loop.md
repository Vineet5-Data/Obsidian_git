---
name: kaggriculture-candidate-loop
description: "One hypothesis, one change, prove the branch fires, hand over the filename — the user runs the 1,760-game benchmark and returns the loss analysis."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 208236e3-55b9-4521-bc1c-8aa6d1b33e2a
  modified: 2026-08-20T14:29:35.981Z
---

The Kaggriculture improvement loop is: **one hypothesis, one change, prove the
branch fires locally, hand over the filename.** The user runs the full
1,760-game benchmark on Kaggle TPU and returns the loss analysis. Do not stack
two changes into one candidate — attribution is the point.

**Why:** local runs are capped at 20 games ([[never-run-local-benchmarks-over-20-games]]),
which resolves mechanisms and rejects disasters but cannot measure a 9-point
move. Candidates generated without measurement ran at roughly one hit in seven
across the 2026-08-20 session (v206 adopted; v207, v208, v210, v211, v212 and
the melon cohort all died). Generating more of them is noise, not progress.

**How to apply:** when a candidate is queued and unmeasured, **stop and wait**
— asked directly on 2026-08-20, the user chose "You run v209 on Kaggle, I wait"
over lifting the local cap. Do not keep producing candidates to look busy. Screen
a candidate with `screen_pair.py` (20 games, paired, reports win-rate delta and
cells regressed) before handing it over; "0 cells regressed" is the bar for
spending a Kaggle cycle, not a positive margin t.

Record every dead hypothesis with the number that killed it, in the roadmap doc,
so no later cycle re-derives it.

Related: [[kaggriculture-benchmark-workflow]], [[kaggriculture-file-locations]],
[[v206-wheat-mirror-won-conversion-is-next]]
