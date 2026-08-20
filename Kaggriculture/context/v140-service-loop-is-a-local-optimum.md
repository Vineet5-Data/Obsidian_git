---
name: v140-service-loop-is-a-local-optimum
description: "Re-pricing v140's HARVEST/FERTILIZE/DIG service jobs off engine mechanics is a measured dead end; the price gates are correct."
metadata: 
  node_type: memory
  type: project
  originSessionId: fc4033e5-1cec-4206-81f6-8cf2efa8416b
  modified: 2026-08-16T08:26:10.819Z
---

As of 2026-08-16, re-pricing v140's worker-service jobs is a **closed axis**.
Five interventions were screened head-to-head vs the v140 baseline (12 seeds ×
both seats) and every one lost or was neutral:

- HARVEST/CARE/FEED priced off a floor instead of crashed spot: −4,746 (t −3.21)
- DIG reclaim of decayed tiles + weeds: −5,281 (t −4.32)
- reserving fertilizer from sale: −6,019
- all three together: −7,873 (t −6.33), **0 wins in 24 games**
- widening FERTILIZE into its full 3-day buff window: −1,057 (t −0.90)

**Why:** strawberry clears at ~$206/unit for *both* sides during days 20-24, so
the market is rich, not crashed. Withholding a $100 fertilizer unit to grow one
more crop unit is a bad trade, and boosting HARVEST only *moves* worker-turns
off jobs already worth more. The baseline's `product_price < 50` and
`incremental > 12` gates encode a correct principle: when a product is worth
less than the labour and inputs to chase it, the tick is not worth rescuing.

Full write-up with engine citations, the reproduction harness (`screen_v140.py`)
and the ablations (`v140_ablations/`) is in the repo at
`V140_SERVICE_LOOP_FINDINGS.md`.

**Why this matters:** the engine mechanics that motivate these changes (yield
clamped at max_yield, decay to WEED, fertilizer doubling) are all genuinely
real, so this looks like an obvious win every time it is re-derived from the
loss telemetry. It is not. Do not re-litigate without new evidence.

**How to apply:** the strongest untested lead is `move_rate` — a second-dry-day
WATER job injects 50,000 into the job board and `move_rate` averages the top N,
so 51% of worker-turns are movement. Swapping mean→median alone loses; it must
be swept together with `MOVE_FRAC` (try 0.3-0.6) in one experiment. See also
[[kaggriculture-benchmark-workflow]].
