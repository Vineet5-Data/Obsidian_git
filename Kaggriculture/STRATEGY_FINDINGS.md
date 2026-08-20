# Kaggriculture — optimal strategy findings

## FINAL: v30.py — 93.8% panel (270-18), mean +30,682, worst -2,710

**The route was the bottleneck, not the layers.**  The whole session was spent
tuning functional layers on a base route that a systematic search later ranked
**29th of 42**.  Grafting the same layers onto route `o_90729118` solved both
matchups that had resisted everything else:

| opponent | v27 | **v30** |
|---|---|---|
| mirror | 12.5% / -256 | **100% / +1,158** |
| Seb | 16.7% / -2,995 | **100% / +172,536** |
| Wufang (ladder top) | 100% / +2,444 | **100% / +3,081** |
| Youssef | 83.3% | **91.7%** |
| Khanh | 79.2% | **87.5%** |
| family B | 83.3% | 83.3% / +3,673 |
| **OVERALL** | **62.5% / +825** | **93.8% / +30,682** |

Not a fragile opponent collapse: against Seb our OWN score rises 113,236 ->
175,476 while his falls to 4,421.  All 7 marketParams regimes beat v27;
premium_bear goes 12.5% -> 31.2%.  Ranking routes by win% and worst case rather
than mean was essential -- the mean is dominated by a +172k rout that hides
everything.

Residual: 18 losses in 288, all to family B (8), Khanh (6), Youssef (4), all
narrow.  Re-tuning SMOOTH_START (200/250/266/300 identical) and re-testing every
execution layer on the new route failed to close them.

---

Previous deliverable: **v27.py** (submitted, ref 55334860). Everything below is measured,
not argued. Panel = 6 archetypes × 24 seeds × 2 seats = 288 games.

---

## 1. Engine facts discovered this session (all verified in installed 1.32.4)

| Fact | Where | Why it matters |
|---|---|---|
| `_process_market` runs **before** `_town_consume` in the same step | interpreter L917-918 | Selling at a drain step executes against pre-drain (max) inventory |
| Shops drain at `step % 4 == 0`, town centre at `step % 12 == 0` | `_town_consume` L714/721 | Freshest book is phase 1 |
| **Hands are wiped every night**; `hires_today` resets | `_end_of_day` L857-858 | Labour is a daily rental, NOT a capital stock |
| Hire cost `mult * fib(hires_today)`, `fib=[1,1,2,3,5,8,13,21,34,55,89]`, `mult=1` | `_hire_cost` L674 | 7 hands for a full day costs **$33** |
| `SELL` draws from the **shed only** | L353 | Goods harvested today are unsellable until the nightly auto-drop |
| `DROP` exists, needs a shed-access tile, dumps the **whole** unit inventory | L327-340 | Our tape never uses it; `FEED` eats WHEAT from that same inventory |
| End-of-day shed overflow past 100 is **discarded** | `_drop_inventories_to_shed` L820 | Any hoarding policy destroys harvest |
| Both tapes hire only at **hours 0-1** of each day | measured | Injecting later preserves hand indices |

## 2. The sell-now theorem is FALSE for wheat

Prior claim: glut ≥ 1 everywhere ⇒ all price paths decline ⇒ sell immediately.
Measured live (seed 12345):

```
step   0   WHEAT inventory 10,000   price $25
step 648   WHEAT inventory  9,112   price $55
```

Town drain **exceeds** total wheat supply, so wheat appreciates 120% over the
game. Per-unit impact slopes are wildly heterogeneous:

```
WHEAT       p= 25.00   100 units moves price   $4    (near-infinitely liquid)
MILK        p=160.00   100 units moves price $159    (nearly floors it)
STRAWBERRY  p=120.00   100 units moves price $119
WOOL        p=200.00   100 units moves price $199
```

Holding wheat is still unprofitable (−32,029) — not because prices fall, but
because the tape needs that cash on schedule.

## 3. What shipped: v27 = v26 + sell-schedule smoothing

The "mirror" opponent (`o_90729118`) is **our own route** — `farmer`/`hands`
byte-identical over all 719 shared steps, differing at 68 market cells.
Transplanting its market channel moved −1,327 → −69, proving 95% of that loss
was sell *timing*, not production. Bisection read out the rule:

> Advance a sell into a spare earlier slot whenever the shed verifiably holds
> the goods. Advance, never defer.

`SMOOTH_START = 250` is a robustness knob with a located cause: step 168 is the
tape's biggest capital turn (`BUY_LAND + 3×HIRE + BUY_ANIMAL + BUY_SEED`), and
smoothing across it starves `BUY_LAND` when revenue is thin.

| | v26 | **v27** |
|---|---|---|
| Panel | 56.2% / +253 | **62.5% / +825** |
| mirror | 0-48 / −1,292 | 6-42 / −256 |
| Wufang (top) | 48-0 / +1,836 | 48-0 / +2,444 |
| regimes improved | — | **7 of 7** |

## 4. Complete falsification table (this session)

| Intervention | Best result | Verdict |
|---|---|---|
| Market-channel evolution, 48 children | 0 improvements; 42% no-op, tail −35,572 | dead |
| **Sell smoothing (advance)** | **+572 panel** | **SHIPPED** |
| Race / retreat by rival supply | −2,203 / −2,176 vs −2,177 | inert |
| Mid-game reinvestment @300 | −3,411 … −17,118 | dead |
| Drain-clock phase gating | −2,704 (advance), −7,227 (defer) | dead |
| Wheat holding | −32,029, monotone in amount held | dead |
| Mid-day DROP (3 guards) | −2,677 vs −2,177 | dead |
| Fixed volume cap (v28) | Seb +726, **panel 6.6%** | overfit, rejected |
| Impact-budgeted sizing × 5 tolerances × 2 gates | best +573 vs control +838 | dead |
| Early hiring, index-preserving | −27,166 … −116,037 | dead |

## 5. The one structural result

**The tape is a cash-critical local optimum.** The only intervention that has
ever helped moves cash *earlier* without changing anything else. Every policy
that delays cash, adds purchases, or holds inventory fails, and the magnitude of
failure is **monotone** in how much it delays or holds.

Extra labour is strictly negative because the tape scripts movement only for the
hands it hires; surplus hands spawn on shed-access tiles where `_idle_fill`
finds no job. Confirmed at 4 target levels and 2 injection points.

## 6. Why Seb wins, quantified

Realized revenue per unit (seed 12345):

| item | us | | him | |
|---|---:|---:|---:|---:|
| STRAWBERRY | 292 | **$108.4** | 286 | **$139.5** |
| MILK | 213 | $176.6 | **287** | $184.2 |
| FERTILIZER | 210 | $45.4 | **321** | $49.8 |
| WHEAT | **273** | **$47.4** | 81 | $41.4 |

Two separate gaps: a −$9,081 **execution** loss on strawberry (same volume, 22%
worse price, from 22-unit blocks under per-unit lockstep), and a **production**
gap in milk/fertilizer from 19 animals vs our 14. Every attempt to fix the
execution gap in isolation cost more elsewhere than it gained.

Seb runs **7 hands/day from day 0**; we run 5, 0, 2, 1, 4, 1, 2. At $33/day for
7 hands this is not a money constraint — it is a **route** constraint.

## 7. Market-mediated interference (real, unusable as-is)

Hiring 9/day on days 0-6 *at hour 0* produced **+135,828 vs Seb** — we gain
+27k and his build collapses 96% (119,802 → 4,704), because his recorded ramp
can't fund itself once our extra output moves premium prices. The same change
*feeds* family B (+30k to him), and the whole effect is a hand-index desync, not
a designed policy. Panel win rate 33.3%. **Not shippable**, but it demonstrates
a lever the execution literature said shouldn't exist here.

## 8. Route authoring for surplus hands — TESTED, FAILED

The "remaining path" was tested rather than assumed. Design: keep the proven
tape driving hands `0..k-1`, author a controller for hands `k..n-1` only. Index
safety is exact — both tapes hire solely at hours 0-1, so extras hired from
hour 2 always land beyond `len(tape["hands"])`.

| variant | overall | why |
|---|---:|---|
| WATER job | **exactly $0 change** (421 assignments) | `watered_today` is idempotent per day; the tape waters the same tiles later |
| HARVEST / COLLECT_FERTILIZER, 9/day | −23,006 | steals tiles the scripted HARVEST expects loaded; produce overflows the 100-cap shed and is discarded |
| 7/day (cheap, $33/day) | −356 | nearly neutral, still below control |
| 9/day early (days 0-6) | −19,628 | `fib(0..8)`=$88/day spent when money is **$25 at step 48** |
| 12 / 14 / 16 per day from day 10 (cash-rich) | −7,370 / −15,573 / −55,220 | monotone in headcount |
| **14/day from day 10, NO jobs** | **−11,034 (better than −15,573 with jobs)** | the controller itself is net-harmful |

The control is decisive: giving surplus hands work is *worse* than leaving them
idle. **This route cannot absorb more labour**, in any window, at any level,
with or without a job controller. Seb's scale advantage is inseparable from
Seb's route.

## 8b. Verdict on "unbeatable"

No unbeatable strategy exists that is reachable from this codebase. ~30
interventions this session plus ~75 prior all fail, and they fail for one
coherent reason (§5). v27 is the optimum of the reachable action space, and the
boundary of that space is now mapped rather than guessed.

The only untested option left is authoring a complete 720-step route from
scratch built around 7+ hands/day from day 0 — a large project with poor prior
odds: the one from-scratch controller attempt (`_ctrl.py`, driving every unit)
scored −25k to −166k.

## 9. Caveat

v27 ladder score 1610.8 at ~3.5 h vs v26's 2744.9 (5.5 h) and v24's 2947.4
(17 h). v26 read 2657 at 2 h, so v27 is tracking *below* it at comparable age.
Ratings are young; watch before drawing conclusions.
