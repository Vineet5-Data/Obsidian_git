---
name: non-ongoing-crops-are-destroyed-by-their-own-harvest
description: "Kaggriculture WHEAT/CARROT advertise HARVEST and WATER on the same tile from the same age; harvesting first destroys the tile and the remaining units. Our wheat reached 1.85 units/tile vs the opponent's 3.75."
metadata: 
  node_type: memory
  type: project
  originSessionId: fc4033e5-1cec-4206-81f6-8cf2efa8416b
  modified: 2026-08-17T07:37:27.872Z
---

Non-ongoing crops (`ong: False` — WHEAT, CARROT, MELON) do **not** get yield
from `_daily_refresh_plants`; it skips them outright (engine `:774`). Their
units come from three places only:

* `+1` free unit at planting (`:210`)
* `+1` (or `+2` fertilized) per **WATER**, but only while
  `(myd+1)//2 <= age <= myd` (`:425-430`)
* nothing else — and HARVEST sets the tile to `None` (`:455`), ending it

WHEAT is `fyd 2 / myd 4 / my 6`, so **HARVEST unlocks at exactly the age the
water window opens**. The same tile simultaneously advertises "harvest me for
the 1 free unit" and "water me three more times", and whichever fires first
ends the tile.

Measured over one full game vs `t_91631405_0`, average units reached per wheat
tile: **us 1.85, opponent 3.75** (of a possible 4.00). Wheat is the largest
single line in the v157 loss analysis — the opponent takes **+$10,409** on it
across days 25-29 (288.1 units vs our 80.1) — and wheat's market is the deepest
in the game (`T=400`, `af "log" 0.20`), so volume there barely moves the price.

MELON is unaffected by the same fix: its window opens at age 6 and it is
already at `max_yield` by the time HARVEST unlocks at age 10.

**Why:** this is a *destructive* action, not merely a wasteful one, so it
belongs to the change class that has actually won (see
[[v140-only-deleting-work-wins]]) rather than the capacity-addition class that
lost. Suppressing it also frees worker turns instead of spending them: tiles
consumed fell 98 → 52 for the same banked units.

**VERDICT: the fix LOST.** `v160_growfirst.py` (the `still_growing` guard:
`not cd["ong"] and age < cd["myd"] and held < cd["my"] and not expiring and
step < DUMP_STEP`) benchmarked **1302-298 = 81.4%**, five points below the
champion's 86.4%. The mechanism was real — wheat production days 25-29 rose
80.1 → 116.0 units — but holding tiles longer cut tile turnover, and the freed
worker-turns went to jobs that were worth less than the harvests they replaced.

**How to apply:** do not re-open this. The measurement that "our wheat reaches
1.85 units/tile against their 3.75" is still true and still not the lever;
per-tile yield is not what separates us. The 10 real leaderboard replays in
`New_Losses/` point at routing instead — see
[[job-board-truncation-drops-zero-travel-jobs]]. Note also that the local
telemetry line `crop expiry with held yield: STRAWBERRY=947/game` is an artifact
of the weak local opponent panel: against real top players we rot 13 tile-turns
per game and they rot 17. See also [[kaggriculture-candidate-loop]].
