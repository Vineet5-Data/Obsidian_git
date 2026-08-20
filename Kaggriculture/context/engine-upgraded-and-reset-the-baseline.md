---
name: engine-upgraded-and-reset-the-baseline
description: "Live engine is kaggle-environments 1.32.7; it added the \"hinge\" scarcity curve and reset the v186 baseline from 68.4% to 50.0%."
metadata: 
  node_type: memory
  type: project
  originSessionId: 208236e3-55b9-4521-bc1c-8aa6d1b33e2a
  modified: 2026-08-20T10:25:11.533Z
---

The live Kaggriculture engine is **kaggle-environments 1.32.7**. Confirmed
exactly on 2026-08-20: replaying (agent, opponent, seed) triples from the 50%
report reproduces its margins **to the coin** on 1.32.7 (−41,653 / −32,504 /
−30,749) and misses by ~80 on 1.32.6. Develop and measure on 1.32.7.

Two engine changes matter, both invisible to anything built before them:

1. **Town demand collapsed.** Old: `TOWN_CENTER_DEMAND_SCHEDULE`
   `[(20,4),(10,2),(0,1)]` every 12 steps → 8 units/product/day from day 20.
   Now: **1 unit/product/day, flat** (`townCenterSellInterval` 24). Season town
   absorption per product **140 → 30**, all of it after day 20. This is why
   `a_v186` measured 1203-557 (68.4%) then 880-880 (**50.0%**) with identical
   agent bytes, opponents and seeds — it is not a regression, the two numbers
   describe different games.

2. **1.32.7 added the `hinge` price shape** (`HINGE_GAIN = 8.0`,
   `u + 8*max(0,u-1)**2`, `u = x/T`) on the below-I0 side of **CARROT, TOMATO
   and EGG**, and raised CARROT's `below_target` 0.20 → 1.00. Past the knee the
   scarcity price runs away quadratically.

**Why:** every price table copied from an older engine is now wrong on exactly
the three belts the rival does not supply (tomato 0.00 units, egg 0.20, carrot
0.02). `a_v186.price()` under-prices TOMATO at 600 short by **$768** (thinks
132, engine pays 900), EGG by $104, CARROT by $71 — it can neither chase nor
defend a spike it cannot see.

**How to apply:** verify any local `MP` / `MARKET_PARAMS` / `_shape` copy against
`market_price` in the installed engine before trusting a price-based conclusion
— a loop over ±1500 inventory for all 9 products catches it in seconds. Pin
`kaggle-environments` in the benchmark notebook, otherwise `pip -U` silently
moves the target between runs.

Related: [[env-src-must-be-copied-from-installed-engine]],
[[loss-analyzer-inflates-opponent-revenue]]
