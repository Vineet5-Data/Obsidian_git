---
name: mirror-screening-is-blind-to-real-gains
description: Kaggriculture mirror-match screening has been wrong in both directions; only screen_top.py predicts the real benchmark.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: fc4033e5-1cec-4206-81f6-8cf2efa8416b
  modified: 2026-08-16T12:07:44.195Z
---

Screening a Kaggriculture candidate against its own baseline (mirror match) has
now been **wrong in both directions**:

| change | mirror said | real instrument said |
|---|---|---|
| no-op service suppression | +82, t +0.44 (parity) | **+1.8 pts** |
| `FERTILIZER_CURRENT_UNIT_MULTIPLIER` 4.0 → 3.0 | **+1,081, best of 5 values** | **−19.2 pts**, McNemar χ² 54.1 |

**Why:** a mirror match shares one market between the two sides, so the price
impact of any change lands on both players and largely cancels. What is left is
noise that can point either way.

**How to apply:** a mirror near-zero is NOT evidence of no effect, and a mirror
positive is NOT evidence of a gain. Use `screen_v140.py` only to reject changes
that lose by thousands. Decide everything else with `screen_top.py <cand.py>
--baseline <current.py> --seeds 2`, which runs a *paired* comparison against the
real `.top/` tapes (same opponents, same seeds) with a McNemar test on the games
that flipped. It caught the 3.0 regression in 640 games, before it cost a
1600-game Kaggle run.

`top_tournament.py <agent> --mode random --seeds 10` reproduces the user's exact
1600-game benchmark; `.top/_loss_analysis.py` is the tool that emits their
loss-analysis markdown (`--offset N` selects a held-out seed set).

See also [[v140-only-deleting-work-wins]].
