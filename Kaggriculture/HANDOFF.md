# Kaggriculture — Handoff Note

Written 2026-08-08. Read this first in a new session.

---

## 0. How to restart the session

```
cd C:\Users\Vinee\Desktop\Kaggriculture
claude
```

Plain `claude`. **Do not** pass `--agent`, and **do not** `@`-mention an agent
in the first prompt.

### Why the last session was broken

It was bound to the `openevolve-researcher` subagent for its whole lifetime.
Evidence: the session's system prompt was the verbatim body of
`~/.claude/agents/openevolve-researcher.md` ("You are a RESEARCH AGENT ...
NEVER attempt to implement"), and the available tools exactly matched that
file's `tools:` whitelist.

That whitelist omits `Edit`, `Task` and `TodoWrite`. Consequences:

* no `Edit` — every change had to be a full-file `Write`,
* no `Task` — **a subagent cannot spawn subagents**, so the requested
  "research using the openevolve-researcher agent" was impossible from inside,
* a system prompt actively instructing against implementation work.

Probable trigger: `/goal ... Do research using @"openevolve-researcher (agent)"`
bound the session to the agent rather than dispatching it as a child. Context
compaction then carried that identity forward.

Optional, so the agent is usable either way in future — add `Edit` to line 4 of
`C:\Users\Vinee\.claude\agents\openevolve-researcher.md`:

```
tools: Read, Write, Edit, Grep, Glob, Bash, WebFetch, WebSearch, mcp__scrapling__fetch, ...
```

Takes effect only on the next session start.

---

## 1. Standing constraints (do not violate)

1. **Show test results and ask before submitting to Kaggle.** Never submit
   unprompted.
2. **No cloning of any type. Pure strategies only.** Do not graft opponent
   action tapes. Do not route-shop among replays. Strategy must be a function
   of the observation.
3. Governing project doc is `Kaggriculture/claude.md` — *not* the
   `AlphaEvolve_research` CLAUDE.md.

---

## 2. Engine — this bit is critical

**Local must be `kaggle-environments==1.32.6`.** The ladder runs 1.32.6; a long
stretch of earlier work was measured on 1.32.4 and was silently invalid.

```
pip install --upgrade "kaggle-environments==1.32.6"
```

Differences 1.32.4 → 1.32.6:

| | 1.32.4 | 1.32.6 |
|---|---|---|
| `townCenterSellInterval` | 12 | **24** |
| `TOWN_CENTER_DEMAND_SCHEDULE` | `[(20,4),(10,2),(0,1)]` | **removed** (flat 1×) |
| `TOWN_CENTER_PRODUCTS` | no MELON | **includes MELON** |

Env source: `C:\Users\Vinee\miniconda3\Lib\site-packages\kaggle_environments\envs\kaggriculture\kaggriculture.py`
(1073 lines). Everything in §3 was read from it directly.

---

## 3. Mechanics reference (verified against source)

Board 10×10, 4 quadrants of 5×5. 720 steps = 30 days × 24 turns.
Start $3000, NW unlocked, farmer at (4,4).

**Reward = final `farm["money"]` only.** Unsold shed stock scores zero.

### Shed
* Capacity **100 total across all items** (`sum(shed.values())`), not per item.
* Animals bought sit in the shed and count toward the cap.
* `_drop_inventories_to_shed` at end of day: **overflow past 100 is DESTROYED**.
* `SELL` draws from the shed only, and is clamped to shed contents.
* `DROP` needs a shed-access tile `{(4,4),(5,4),(4,5),(5,5)}`, dumps whole
  unit inventory.
* Seeds live in `private["seeds"]`, never pass through the shed.

### Labour
* `hands` cleared and `hires_today` reset every night — **labour is a daily
  rental, not capital**.
* `hire_cost = mult * fib(hires_today)`, `fib(0..)=1,1,2,3,5,8,13,21,34,55,89,144,233,377,610`
* Cumulative per day: 5 hands $12 · 8 hands $54 · 10 hands $143 ·
  12 hands $375 · 14 hands $986 · 16 hands $2583.
* Hand hired at hour *h* appears at *h+1*, spawns on a shed-access tile.

### Plants
* Must be watered **on the planting day** or it dies that night
  (`consecutive_unwatered` starts at 1; 2 ⇒ WEED).
* Afterwards it can miss exactly one day.
* Watering only adds yield inside the window `[(myd+1)//2, myd]` for
  non-ongoing crops; fertilizer doubles the increment.
* Ongoing crops accrue on the daily refresh, capped at `max_yield` productions.

| crop | seed | first yield | max yield day | interval | max units | ongoing |
|---|---|---|---|---|---|---|
| WHEAT | 10 | 2 | 4 | – | 6 | no |
| CARROT | 20 | 2 | 3 | – | 4 | no |
| TOMATO | 50 | 8 | – | 1 | 4 | yes |
| STRAWBERRY | 100 | 10 | – | 2 | 4 | yes |
| MELON | 80 | 10 | 12 | – | 6 | no |

### Animals

| animal | cost | structure | first yield | interval | max held | product |
|---|---|---|---|---|---|---|
| GOOSE | 300 | COOP | 4 | 1 | 4 | EGG |
| COW | 400 | PASTURE | 8 | 2 | 6 | MILK |
| SHEEP | 500 | PASTURE | 6 | 3 | 6 | WOOL |

* **Base production of 1 happens even if unfed.** Feeding does two things:
  resets `consecutive_unfed` (2 ⇒ the animal escapes, structure remains), and
  makes the CARE bonus redeemable.
* `cared_today AND fed_today` ⇒ `pending_care_bonus += 1`, consumed on the next
  *fed* production day ⇒ **2 units per interval instead of 1**.
* `FEED` consumes **1 WHEAT from the unit's own inventory**, not the shed.
* Pipeline to place an animal: `BUY_ANIMAL` → lands in shed → `PICKUP` at a
  shed tile → walk → `PLACE` on a matching empty structure.

### Town — the strategic core
* `townShopUnlockInterval = 3`: a shop unlocks at the end of days 3, 6, 9, …, 24.
  Max **8 instances**, drawn **with replacement** from `sorted(SHOPS)` using
  `random.Random((seed * 1_000_003) ^ day)`. Duplicates are common and each
  instance drains independently.
* Every 4 steps each shop instance removes 1 of each of its products
  (**2× if the shop has a single product**).
* Every 24 steps the town centre removes 1 of every product except FERTILIZER.

| shop | products |
|---|---|
| BAKERY | EGG, WHEAT |
| PIZZA_SHOP | MILK, TOMATO, WHEAT |
| BRUNCH_SPOT | EGG, WHEAT, STRAWBERRY |
| YARN_STORE | WOOL (×2) |
| ICE_CREAM_SHOP | STRAWBERRY, MILK, WHEAT |
| PET_CAFE | CARROT (×2) |
| SMOOTHIE_SHOP | STRAWBERRY, MILK |
| FARMERS_MARKET | WHEAT, CARROT, TOMATO, STRAWBERRY |

**MELON appears in no shop** — only the town centre drains it, 30 units/game.

### Market
`price(inv) = base ± amp·f(|inv − 10000|)`, floored at 1, `I0 = 10000` for all.
Selling raises inventory (lowers price); the town draining lowers it.
Buying `WHEAT`/`FERTILIZER` is quoted at `price(inv − 1)`.
Sales at price 1 do **not** add to market inventory.
Max **10 market orders per turn**. Per-unit lockstep settlement between the two
players, matched by slot index.

Total revenue from dumping *N* units into an untouched market (integral of the
price curve) — this is why product choice dominates everything:

| product | base | practical ceiling | revenue at ceiling | note |
|---|---|---|---|---|
| EGG | 50 | 800+ | ~$32,000 | log decay, deepest market |
| MELON | 250 | ~158 | ~$26,400 | quadratic crash, no shop demand |
| CARROT | 35 | ~800 | ~$10,600 | |
| WHEAT | 25 | ~400 | ~$8,300 | also the feed input |
| WOOL | 200 | ~59 | ~$7,800 | cubic crash — worthless without YARN_STORE |
| TOMATO | 60 | ~200 | ~$7,200 | |
| MILK | 160 | ~76 | ~$6,100 | linear crash |
| STRAWBERRY | 120 | ~62 | ~$3,750 | |

Sum of all ceilings ≈ $101k, yet top ladder scores are ~137k. **The gap is
shop drain.** A YARN_STORE unlocking on day 3 removes ~324 wool over the
episode, so wool can absorb ~380 units near base price ≈ **$76k from wool
alone** — on a seed where it would otherwise be worth $7.8k.

### Interpreter order per step
unit actions → `_process_market` → `_town_consume` → `_decay_plants` →
`_end_of_day` (if last hour). Selling on a drain step therefore hits
pre-drain inventory.

---

## 4. Where the project actually stands

### Tape lineage (violates the no-cloning constraint — reference only)

Measured on engine 1.32.6, `_real.py` panel = 12 real current opponents
(6 from `v27_losses` + 6 distinct top-leaderboard builds), × 6 seeds × 2 seats.
All 12 are pure verbatim replays and every recorded game reproduces to the dollar.

| agent | W-L | win% | mean | worst |
|---|---|---|---|---|
| v27 (on ladder, ref 55334860) | 56-40 | 58.3% | +704 | −30,674 |
| v30 | 60-36 | 62.5% | +3,169 | −8,544 |
| v31 | 66-30 | 68.8% | +1,967 | −25,030 |
| v33 | 112-32 | 77.8% | +4,612 | −10,438 |
| **v35** | **114-30** | **79.2%** | **+4,651** | **−10,319** |

`v35` = `v33` with `SMOOTH_WINDOW` 8 → 16. That re-tune is *mechanistic*: the
town centre interval went 12 → 24, so the drain cycle that makes spreading
sales profitable is twice as long. Measured: window 16 → 79.2%, window 8 →
75.0%, smoothing off → 75.0%.

**v35 is unsubmitted.** 41,534 bytes, sha256
`d34889d90265be481c662227e89b0eee43486aa5b045f329f8e6361472c7197b`,
worst turn 104.7 ms of a 1000 ms budget, stdlib-only.

Negative result worth not repeating: **the route classifier cannot be re-fitted
on the real field.** Opponents with identical public features want opposite
routes (`90897383` and `90916037` are both delta −27…−25 with 7 animals, and
want B and A respectively). The information is not in the observation.

Ladder scores last seen: v24 2947.4 · v26 2877.4 · v27 2340.6.

### Pure-policy line (what the constraint actually asks for)

`g1.py` → `g2.py` → `g3.py`. No tape, no opponent data. Each is a full
observation-driven planner: absorption model → supply projection → marginal
tile allocation → job board → greedy (unit, job) assignment → market orders.

Measured with `python _gdiag.py <agent>.py 7` (mirror match, seed 7):

| build | result | what the trace showed |
|---|---|---|
| g1 | $30,592 | **0 animals ever placed** — bought 3, never picked up from the shed. 534 wool drained (3× YARN_STORE) and we sold none. |
| g2 | $21,182 | Animal pipeline fixed (10 placed). But money sat at $3–$50 from day 12 to 25: hiring 14 hands/day ($986) on a calendar schedule, and selling the wheat the herd eats. Animals starved, 9 → 0 by day 17. |
| g3 | $3,925 | **`market inv delta WHEAT: −1722`.** Bought 1,722 wheat to feed 9 animals: units picked up 6 each (212 pickups → 103 feeds), surplus destroyed at the day-end shed cap, then re-bought. Consumed every dollar. Hand count also collapsed to 2–6. |

For scale: the top ladder builds score ~137,616.

---

## 5. Next step — the g4 fix list

All six are diagnosed, none are speculative:

1. **`FEED_CARRY` 6 → 3**, and size the `PICKUP` to the number of animals still
   unfed this turn. Surplus carried past dusk is destroyed.
2. **Cap wheat purchases** at `n_beasts` per turn and skip entirely when
   `wheat_buy > ~45`. Unbounded top-ups bankrupted g3.
3. **Value WHEAT at replacement cost, not sale price**, while the herd is short
   of feed — then the allocator grows feed instead of buying it into a rising
   price.
4. **Size the workforce to the farm**, not the calendar:
   `want_hands ≈ ceil((n_plants + 2·n_beasts + free_tiles) / 9)`, clamped 3…14.
5. **Shrink the working-capital reserve** to feed-only so animals actually get
   bought; order of spend = wages → animals → seeds → wheat top-up.
6. **Multi-cycle crop value** — a wheat tile completes ~5 cycles a season, a
   melon tile only 2. Counting one cycle undervalues fast crops and lets melon
   monopolise the board and starve the opening of cash.

Also still open: crops decay into WEED tiles that were never dug (34 weeds by
day 24 in one run), and movement dominates work ~4.6:1 (4,327 moves vs 939
waters in g1) — locality of the job assignment needs attention.

**Do not tune on seed 7 alone.** Build a multi-seed harness before trusting any
number; a fixed-volume-cap variant once looked great on one opponent (+726) and
scored 6.6% on the full panel.

---

## 6. Files

Root was cleaned 214 → 28 files. Everything removed is recoverable in
`_attic/` (a plain folder, nothing deleted destructively). Only genuinely
disposable things were erased outright: `.tmp_replay_*.json` (115 MB of my own
temp dumps), `*.log`, `__pycache__`.

| file | role |
|---|---|
| `g1.py` `g2.py` `g3.py` | pure-policy line — the constraint-compliant work |
| `_gdiag.py` | per-day pipeline trace; found every bug above |
| `_real.py` + `_duel.py` | the honest 12-opponent benchmark, engine 1.32.6 |
| `v35.py` | best tape build, 79.2%, unsubmitted |
| `v33.py` `v27.py` `main.py` | tape lineage (`main.py` == v27, on the ladder) |
| `_mkpure.py` `_mktop.py` `_extract_fresh.py` | rebuild opponent panels from replays |
| `_retune.py` `_reclass.py` | smoothing re-tune / classifier fit harnesses |
| `_env_src.py` | cached copy of the engine source |
| `claude.md` `AGENTS.md` `STRATEGY*.md` `RESEARCH_NOTES.md` | project docs |
| `.pure/` `.top/` `.field/` `.loss/` | extracted opponent replays |
| `Top_fresh-21/` `v27_losses/` `recent _loss/` | raw replay JSON (≈660 MB) |

`_attic/` holds ~190 superseded builders, sweeps, one-off probes and old agent
versions. Safe to delete once you're satisfied nothing is needed.

---

## 7. The one idea to carry forward

A policy that reads `obs.town.unlocked_shops` and re-allocates production
toward whatever the town is actually draining has an edge that no replay can
answer. That is the whole thesis of the `g*` line, and the g1 trace already
proved the upside is real — it simply failed to capture it.
