---
name: never-run-local-benchmarks-over-20-games
description: Hard cap of 20 games on any local Kaggriculture run; the user benchmarks full sets on Kaggle TPU themselves.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 208236e3-55b9-4521-bc1c-8aa6d1b33e2a
  modified: 2026-08-20T10:11:44.946Z
---

Never run more than **20 games** locally for Kaggriculture. Stated 2026-08-20
while a 3,520-game paired run was in progress (it was killed). The user
benchmarks the full 1,760-game set on Kaggle TPU themselves.

**Why:** a full local run costs ~8s/game and saturates the machine for the best
part of an hour, which is the user's machine, and the Kaggle run is going to
happen anyway.

**How to apply:** smoke tests only — enough games to prove a branch fires and
to sanity-check step latency, typically 1-4. Build the candidate, prove the
mechanism, hand over the filename, stop. Do not start a background benchmark
"while waiting", and do not treat a small local sample as evidence of strength;
a single seed is a cherry-pick, not a measurement.

Related: [[kaggriculture-candidate-loop]],
[[mirror-screening-is-blind-to-real-gains]]
