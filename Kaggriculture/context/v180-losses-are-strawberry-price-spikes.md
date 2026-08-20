---
name: v180-losses-are-strawberry-price-spikes
description: "Kaggriculture v180 (88.2%) loses only in games where strawberry goes scarce and expensive; we hold 59% of the opponent's strawberry volume off an identical tile count, and the gap is fertilizer coverage."
metadata:
  node_type: memory
  type: project
  originSessionId: fc4033e5-1cec-4206-81f6-8cf2efa8416b
  modified: 2026-08-17T18:36:23.766Z
---

`a_v180_merged.py` benchmarks **1412-188 (88.2%)** — the champion as of
2026-08-17, up from v140's 86.4%.

**The losses are not an early-game problem.** Decomposing net cash by window
(wins derived by subtracting the losses-only panel from all-games):

| window | wins gap (opp−us) | losses gap | delta |
|---|---|---|---|
| day 0-19 | −15,701 (we lead) | −15,507 (we lead) | +194 |
| day 20-24 | +1,034 | +12,049 | **+11,015** |
| day 25-29 | +1,443 | +6,364 | +4,921 |

Our early game is *identical* in wins and losses. The entire loss is the
opponent's day-20-24 surge, and one line carries it: **opponent STRAWBERRY
revenue $30,476 in losses vs $16,509 in wins — on identical units (161.9 vs
160.7).** It is price, not volume: **$188/unit vs $103/unit**, and both sides
realise the same price.

Engine `market_price` (`kaggriculture.py:179`): `inventory < I0` →
`price = base + (below_target*base/shape(f,T)) * shape(f, I0-inventory)`.
STRAWBERRY is `base 120 / T 100 / below sqrt 0.70`, so
`price = 120 + 8.4*sqrt(I0-inv)`. **$188 ⟺ inventory ~64 BELOW I0** (shops
drained it); $103 ⟺ ~9 above. Shops unlock every 3 days
(`townShopUnlockInterval`, cap `MAX_SHOP_INSTANCES = 8`).

**So we lose exactly the games where strawberry goes scarce — because we are
structurally short strawberry.** Same tiles (29.6 vs 30.0 at day 19), 59% of
the units (167.5 vs 282.7 per game).

**The volume gap is fertilizer coverage, and it reconciles from two
directions.** STRAWBERRY is `fyd 10 / iv 2 / my 4`: four production ticks, each
`yield_units += 2 if (was_watered and fertilized_until_day >= day) else 1`
(`_daily_refresh_plants`). Coverage 59.5% (us) vs 90.9% (them) predicts 6.4 vs
7.6 units/tile; measured off seed spend, 5.7 vs 7.7.

**FERTILIZE is assignment-limited, not supply-limited.** We produce ~372
fertilizer units/game and apply only ~58; the rest is sold at ~$41 against a
$188 strawberry unit. Telemetry `assign%` sits at **6-9%** in every window of
both v180 and v183. See [[v140-only-deleting-work-wins]] for why the large
`move_rate` makes a $351 job reachable only by a worker already standing there.

**How to apply:** the strawberry volume gap is the live axis, and the mechanism
is getting a fertilizer-carrying worker onto a due tile — not more tiles, not
more watering, not market timing (we match or beat them on realised price for
every product). Do not re-open melon: we win it 5.71 vs 4.87 units/plant.
