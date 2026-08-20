---
name: env-src-must-be-copied-from-installed-engine
description: "_env_src.py had drifted from the shipped engine and produced a false finding; re-copy it, never hand-edit."
metadata: 
  node_type: memory
  type: project
  originSessionId: 208236e3-55b9-4521-bc1c-8aa6d1b33e2a
  modified: 2026-08-20T08:24:45.352Z
---

`_env_src.py` is the reference every Kaggriculture strategy claim is derived
from, and on 2026-08-20 it had drifted from the installed engine (56 lines
added / 46 removed vs. `kaggle_environments` 1.32.6). The drift was concentrated
in the town-demand model — the stale copy had a `TOWN_CENTER_DEMAND_SCHEDULE`
of [(20,4),(10,2),(0,1)] and `townCenterSellInterval` defaulting to 12. The real
engine drains **1 unit per product every 24 steps**, no multiplier, and unlocks
shops **with replacement** up to `MAX_SHOP_INSTANCES = 8`.

**Why:** reading the stale copy produced a confident, wrong headline finding —
that `a_v186.py`'s `forecast_absorption` understated town demand by 2x-8x. The
code was correct all along. That cost a full analysis cycle.

**How to apply:** before deriving any mechanic from `_env_src.py`, confirm it
matches `kaggle_environments/envs/kaggriculture/kaggriculture.py`. Re-copy after
any `kaggle_environments` upgrade; never hand-edit. Live config defaults are
also worth checking directly — `dict(make('kaggriculture').configuration)`
showed `townCenterSellInterval: 24`, which is what exposed the drift.

Related: [[loss-analyzer-inflates-opponent-revenue]]
