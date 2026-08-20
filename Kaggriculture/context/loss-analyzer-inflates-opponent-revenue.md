---
name: loss-analyzer-inflates-opponent-revenue
description: Loss-analysis market accounting counted requested order qty at one quote; fixed 2026-08-20 with an exact replay — reports cash_residual now.
metadata: 
  node_type: memory
  type: project
  originSessionId: 208236e3-55b9-4521-bc1c-8aa6d1b33e2a
  modified: 2026-08-20T08:24:55.142Z
---

Until 2026-08-20 `_econ_loss_analysis.py` (and a duplicate copy inside
`_loss_analysis.py`) built `units_sold`/`revenue` from the **requested**
quantity on each market order at a **single pre-trade quote**. The engine fills
unit-by-unit at the marginal price and aborts the order on the first unit that
cannot commit. Opponents that spam large SELL orders came out ~3-4x inflated —
measured 4.2x on one game (+104,507 reconstructed against a real +32,936).

Fixed by `replay_market()`, which recovers joint filled volume exactly from the
observable market-inventory delta plus the deterministic town drain
(`traded = inv_post - inv_pre + town_drain`), bounds each seat by its own shed
(DROP dumps a worker's whole inventory; PLACE/PICKUP adjust it), and prices each
unit on the real curve. Result: median `cash_residual` 0.5%, max 4.8%.
`_loss_analysis.py` now imports from `_econ_loss_analysis.py` — one copy only.

**Why:** the old numbers reversed a real conclusion. The v186 report's largest
single line, a $32,646 FERTILIZER gap to the opponent, became **us ~$3,100
ahead** once fills were counted — fertilizer has no demand sink at all, so their
volume was mostly unfilled orders.

**How to apply:** every window now prints `cash_residual (should be ~0)`. If it
drifts far from zero, the market accounting is wrong again — do not trust
revenue/production until it is back near zero. Any analysis run before
2026-08-20 (including `v186_loss_analysis.md`) needs re-running.

Related: [[env-src-must-be-copied-from-installed-engine]],
[[mirror-screening-is-blind-to-real-gains]]
