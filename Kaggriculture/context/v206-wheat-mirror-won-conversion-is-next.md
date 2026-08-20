---
name: v206-wheat-mirror-won-conversion-is-next
description: v206 wheat mirror is the 59.1% baseline; v207 job-board admission lost 9.8pts; wheat acreage now matches the rival but revenue does not.
metadata: 
  node_type: memory
  type: project
  originSessionId: 208236e3-55b9-4521-bc1c-8aa6d1b33e2a
  modified: 2026-08-20T12:06:31.204Z
---

Benchmarked 2026-08-20, n=1760, engine 1.32.7, seed pool k=11..20, 88 `.top/`
opponents. One SD is ±1.19 points.

```
a_v186   (baseline)          880-880   50.0%     --
a_v206_wheat_mirror         1040-720   59.1%   +9.1   ADOPT -- new baseline
a_v208_price_1327            874-886   49.7%   -0.3   noise; correctness only
a_v207_jobboard              707-1053   40.2%   -9.8   REJECT
```

**v206** added WHEAT to the strategic crop mirror
(`for crop in ("STRAWBERRY", "WHEAT", "MELON", "TOMATO")`). +9.1 points from
moving wheat tiles at day 19 only 7.62 → 9.37.

**v207** re-scored job-board admission on `value − move_rate·d` instead of raw
value. Lost 9.8 points. Same shape as the earlier finding that `move_rate` is
safe as a ranking and destructive as a veto — admission is a veto. Do not retry
admission re-scoring without a different mechanism.

**v208** synced the price table to 1.32.7's `hinge` curve. Measured neutral, so
the scarcity spike on CARROT/TOMATO/EGG rarely binds in practice. Keep it as a
correctness fix only if something later depends on accurate scarcity pricing.

**Why the next step is conversion, not acreage:** in v206's report wheat tiles
across days 20-24 are **us 23.17 vs opp 24.15** — matched — while wheat revenue
is **us $801 vs opp $9,353**, and days 25-29 **us $4,165 vs opp $13,142**. The
acreage gap is closed and the cash gap is not.

Cause found at the banking gate: `if feed_load > 0 and unfed > 0 ...:
must_bank = False` blocked a worker from banking whenever it held ANY wheat and
ANY animal was unfed. With 16 animals that is nearly always true, so harvested
wheat rode around on workers and never reached the shed to be sold.
`a_v209_wheat_surplus.py` retains only `min(feed_load, unfed)` units and banks
the rest via `PLACE` (not `DROP`, which dumps the whole inventory — and FEED
pulls from the worker's inventory, not the shed).

Related: [[engine-upgraded-and-reset-the-baseline]],
[[move-rate-inflated-by-synthetic-priority-flags]]
