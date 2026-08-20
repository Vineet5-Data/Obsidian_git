---
name: the-gap-vs-top-players-is-the-dawn-ramp
description: "On real Kaggriculture leaderboard replays our agent matches top players on every op from hour 4 onward; the entire gap is hours 0-3, where they do animal chores and we PASS."
metadata: 
  node_type: memory
  type: project
  originSessionId: fc4033e5-1cec-4206-81f6-8cf2efa8416b
  modified: 2026-08-17T20:26:17.787Z
---

Hands are destroyed every night — engine `:867` `farm["hands"] = []`, farmer
respawns at `_default_spawn`, `private["inventories"] = [{}]` after
`_drop_inventories_to_shed`. So **every day reopens the same problem: turn N
empty-handed bodies standing at the shed centre into work.** Positioning at
end of day is worthless; they teleport back.

Measured over the 10 real leaderboard replays in `New_Losses/`, PASS and work
rates per hour:

| hour | us PASS% | opp PASS% | us work% | opp work% |
|---|---|---|---|---|
| 0 | 38.7 | 19.3 | 10.3 | 7.0 |
| 1 | 33.3 | 16.6 | 8.8 | 12.1 |
| 2 | 0.2 | 0.1 | 15.5 | **23.9** |
| 3 | 0.3 | 0.3 | 21.3 | **32.1** |
| 4-23 | within 1-5 pts | — | within 2 pts | — |

**From hour 4 on we are at parity on every operation.** The whole gap is the
dawn ramp. Action mix, hours 0-3 only, per game:

| op | us | opp | gap |
|---|---|---|---|
| CARE | 14.6 | 39.4 | **−24.8** |
| COLLECT_FERTILIZER | 25.8 | 46.7 | **−20.9** |
| FEED | 49.1 | 59.0 | −9.9 |
| HARVEST | 26.9 | 35.6 | −8.7 |
| PASS | 72.3 | 37.2 | **+35.1** |

**We do not do less animal work — we do it later.** Over the full game we do
*more*: CARE 321.7 vs 311.3, COLLECT_FERTILIZER 343.8 vs 331.2, FEED 319.7 vs
313.6. But fertilizer collected at dusk is banked and sold at ~$41; fertilizer
collected at hour 2 arms a carrier for the whole day, and a carrier standing on
the tile is the only way a FERTILIZE ever happens
([[move-rate-inflated-by-synthetic-priority-flags]]).

Dawn is also when `move_rate` is worst: every tile unwatered overnight has
`consecutive_unwatered >= 1`, so the synthetic +50,000 flags are maximally live.

**Do not trust the local `.top/` panel's loss analysis over the replays.** Three
independent metrics now disagree between the two sources: movement (panel says
we move +104 more, replays say we move 101 *fewer*), PASS (panel −51, replays
**+134**), and strawberry fertilizer coverage (panel 59.5% vs 90.9%; replays
show both sides **100% ON_TICK**, us 52.2 vs their 55.3 applications, ~104 vs
~111 ticks covered). The panel tapes are `t_916xxxxx`; the live episodes are
`937xxxxx`.

**How to apply:** measure candidate changes against the replays' hour profile,
not the panel's aggregate action table. The live question is the dawn ramp.
