# Research Notes: Kaggriculture — Gap-Fill on STRATEGY.md

> Research date: 2026-08-06. Companion doc to `STRATEGY.md` (which covers verified game/market/production
> mechanics from `kaggriculture.py` source). This doc fills four specific gaps: (1) leaderboard/eval mechanics,
> (2) discussion-tab community findings, (3) counter-strategy analysis, (4) GitHub issues/PRs on bugs/balance.
> **Tooling caveat**: Kaggle's competition Overview/Rules/Discussion pages are a pure client-side React SPA —
> no content is present in the raw HTML/initial request, and this session's browser-automation tool
> (`mcp__scrapling__*`) was permission-denied throughout. Everything below for those pages is therefore
> reconstructed from (a) Google/Bing-indexed snippets of Kaggle's own boilerplate on **sibling** competitions
> (Orbit Wars — same host, same launch batch, same env-template family) and (b) direct GitHub source/API access
> (unrestricted, high confidence). Anything not directly confirmed against `kaggriculture`'s own page is flagged
> **[INFERRED]**. Re-verify with a logged-in browser before relying on submission-limit or rating-decay specifics.

---

## TL;DR

Kaggriculture is a `kaggle_environments` sim comp: 720-step / 2-agent episodes, `actTimeout=1s`,
`remainingOverageTime=60s`, reward = final bank (all confirmed directly from `kaggriculture.json` source — high
confidence). Leaderboard almost certainly runs Kaggle's standard sim-comp ladder: N(μ,σ) skill rating seeded at
μ₀=600, validation self-play episode on upload, continuous matchmaking against similar-rated opponents, ~5
submissions/day with only the 2 most recent active **[INFERRED from Orbit Wars boilerplate]**. The competition
launched only days before this research (~early Aug 2026) — no indexed community discussion, exploit reports, or
top-agent writeups exist yet; the discussion tab itself is unreachable by this session's tools. The richest new
finding is the **engine's live GitHub history**: 13 commits since May 8, 2026, including a shed-capacity
market-buy exploit patched **Aug 4** and a locked-tile action bug still **open** as of Aug 5 — i.e., the ruleset
was still being patched *two days before* this research date, and is not fully frozen. STRATEGY.md's numbers
(cow $400, starting money $3000, town intervals 12/4, hire mult 1, no-arb round-trip) all match the *current*
post-patch engine exactly — good sign it wasn't sourced from a stale doc/version.

---

## 1. Leaderboard / evaluation mechanics

**Confirmed directly from `kaggriculture.json`** (source of truth, GitHub, high confidence):
- `episodeSteps: 720`, `actTimeout: 1` (second), `remainingOverageTime: 60` (episode-wide overage budget),
  `agents: [2]` (fixed 2-player, no 1v1v1 or ffa mode) — matches STRATEGY.md's stated budget exactly.
- `reward`: "Player money at end of game (final score)" — confirms win/score = final bank, not incremental.
- Episode seed: `kaggriculture` and `orbit_wars` both adopted a shared `resolve_episode_seed` utility
  (PR [#1242](https://github.com/Kaggle/kaggle-environments/pull/1242)) that draws a random 31-bit int per
  episode, strips it from the observation agents see, but preserves it in the replay JSON — so each ladder
  episode is randomly seeded and **not observable/predictable by the agent**, and replay-mining for RNG patterns
  across *future* episodes isn't possible (new random seed every match).

**[INFERRED, from Kaggle's generic simulation-competition template]** — reconstructed via search-engine-cached
text from the sibling **Orbit Wars** overview page (`kaggle.com/competitions/orbit-wars/overview`) and
`kaggle-cli`'s own docs (`github.com/Kaggle/kaggle-cli/blob/main/docs/simulation_competitions.md`), both part of
the same May–Aug 2026 environment-template family as kaggriculture:
- Each submission gets an estimated **Skill Rating modeled as a Gaussian N(μ, σ²)**; σ (uncertainty) shrinks as
  more episodes are played.
- On upload, a submission first plays a **Validation Episode against a copy of itself** to confirm it runs/is
  legal before joining the ladder pool.
- Once validated, it joins the pool with **μ₀ = 600**, and the scheduler repeatedly matches submissions with
  **similar current ratings** ("fair matches"); **newly submitted agents get an increased episode rate** for
  faster initial feedback.
- Win → μ increases and opponent's μ decreases; draw → both μ move toward their mean; magnitude scales with how
  surprising the result was (relative to pre-match μ) and with each side's σ (TrueSkill-style Bayesian update).
- **Submission limits**: up to **5 agent submissions/day**; only the **2 most recent submissions stay active**
  in the matchmaking pool at once, though the leaderboard displays your **highest-scoring** submission overall.

**Gap remaining**: the exact σ-decay curve, per-day episode-count budget, and whether Kaggriculture deviates
from this generic template in any way (e.g., different μ₀, different submission cap) were **not independently
confirmed on kaggriculture's own page** — the page is a JS SPA and returned no body content to any fetch tool
available this session (`WebFetch`, `mcp__scrapling__fetch/get`, raw `curl`). **Action for user**: manually open
`https://www.kaggle.com/competitions/kaggriculture/overview` and `/rules` while logged in, or grant
`mcp__scrapling__*` tool permission in a future session, to confirm these numbers verbatim for kaggriculture
specifically before relying on the submission cadence for a versioning/testing schedule.

---

## 2. Discussion-tab community findings

**Direct access**: not possible this session — `kaggle.com/competitions/kaggriculture/discussion` is a pure SPA
shell (confirmed via raw `curl`: 5.6KB response, `<div id="root"></div>` empty, all content loaded by
client-side JS after auth). `WebFetch` cannot execute JS; `mcp__scrapling__*` tools were permission-denied.

**Web-search sweep** (multiple queries: exploit/strategy/melon-dump/reddit/twitter/blog) found **no indexed
discussion posts, strategy writeups, or exploit reports** for Kaggriculture specifically. This is consistent with
the competition being brand-new — the earliest announcement tweets
([Kaggle](https://x.com/kaggle/status/2084326711248687165),
[Paige Bailey](https://x.com/DynamicWebPaige/status/2082871191921144055),
[Abdel Sghiouar](https://x.com/boredabdel/status/2084980345691144535)) are all within roughly the last one to two
weeks of the 2026-08-06 research date, so meaningful community strategy discourse likely hasn't accumulated yet.

**Best available proxy for "community-clarified rules"**: the engine maintainers' own commit trail shows
competitors *are* already giving feedback through some channel (presumably the discussion tab or Kaggle support,
even though we can't read the thread directly). PR
[#1385](https://github.com/Kaggle/kaggle-environments/pull/1385) — *"Update kaggriculture readme/agents docs
based on competitor feedback"* (merged 2026-08-04, docs-only, no engine change) — resulted in these
**now-explicit rule clarifications** (useful as de facto "competitor-clarified edge cases"):
- *"Plants (and animals) must be watered/fed a minimum of every other day. Watering only needs to be done once
  per day, and subsequent watering actions are a no-op."* — confirms wasted-action risk of double-watering, and
  that the *minimum* cadence is every-other-day, not strictly daily (relevant for hand-routing efficiency).
- *"A new seed starts with `consecutive_unwatered = 1` … There is no grace period for fresh plantings."* —
  directly confirms STRATEGY.md's "planting day counts as unwatered day #1" claim, from the doc-review side, not
  just source-reading.
- Unwatered plants → weed after **2 consecutive missed** end-of-day refreshes (not 1); unfed animals **escape
  irretrievably** after 2 consecutive missed days.
- A commit note also references clarifying **"the 24-day window for prices"** (exact text not recoverable from
  the PR diff summary tool used — likely the town-shop-unlock-to-full-market window STRATEGY.md already derives
  as "all shops active by day 24–27").

**Action for user**: periodically re-check the discussion tab manually (or with an authenticated browser tool)
as the competition matures — competitor-discovered exploits and top-agent approaches will likely surface over
the following weeks given the Sept 23 deadline is still ~7 weeks out from this research date.

---

## 3. Counter-strategies against the STRATEGY.md plan, and mitigations

No public opponent agents or discussion-tab counter-play reports exist yet (see §2), so this section is
**derived analysis** from verified engine mechanics (kaggriculture.py, cross-checked against the PRs in §4) —
not observed opponent behavior. Presented as candidate threat models per the user's request, not as
implementation guidance.

**a) Melon-dump race (opponent copies the same jackpot play).**
Engine fact: `first_yield_day` for melon is fixed at 10 — an opponent cannot make their wave mature *earlier*
than day 10 by watering harder; the only lever they control is **wave size** (more tiles = more land bought
day 0) and **dump day** (0 through however long they wait). Per STRATEGY.md's own read of `_process_market` /
`_commit_unit`, same-day dumps resolve **per-unit in lockstep** — the shared curve is split by *order of orders
within the turn*, not doubled/duplicated per player. Real risk to the plan isn't timing (both mature day 10
regardless) but **relative wave size**: if the opponent commits more of their day-0 cash to melon tiles + land
than the plan's 13-tile opening, they capture a proportionally larger slice of the shared $21.7–26.6k curve
purely on volume. *Mitigation*: STRATEGY.md's Phase 1 already says "watch opponent's farm... count their melon
tiles and planted_days" (public `farms[i].tiles`) — extend this to **day 0–1**, not just pre-harvest, and treat
an oversized opponent wave as a trigger to divert Phase-0 spend from geese/wheat toward matching melon tile
count if the bank allows, since melon is the single highest one-time EV item in the whole game.

**b) Premium-market flooding (opponent deliberately crashes MILK/WOOL/STRAWBERRY).**
Engine fact confirmed by PR [#1199](https://github.com/Kaggle/kaggle-environments/pull/1199) (merged
2026-06-02): the glut-crash slope for any resource with base price > $100 (strawberry, melon, milk, wool) was
**quadrupled** specifically to make oversupply punishing — this is *why* STRATEGY.md's floor-unit counts are so
low (76/59/62 units). Because market inventory is a **single shared pool**, one player dumping these goods
crashes the price for both. STRATEGY.md's existing mitigation ("if opponent floods, abandon — stop selling, stop
CARE on that species, keep feeding since 1 fert/day still pays") is consistent with the source: recovery back
toward `I0` is slow and gated by town-drain only (`townCenterSellInterval`=12 turns, 2–8/day scaling;
`townShopSellInterval`=4 turns per unlocked shop) — there is no faster way to un-crash a floor than waiting for
town consumption, so abandoning a flooded line rather than fighting it is correct given the source. One added
wrinkle: a losing opponent late-game is playing to maximize **win probability**, not money (rating = win/loss
per STRATEGY.md's own framing) — so a "spite dump" of premium goods they don't even profit much from (floor
sales are worthless, and per STRATEGY.md's note, floor-price units "do not add to inventory" so they can't even
be selling for volume) is *individually rational for them* purely as denial. *Mitigation*: avoid concentrating
animal-species investment (coop/pasture counts) so heavily in one product that a single opponent flood removes
most of the premium income stream at once — STRATEGY.md's mixed goose/cow/sheep allocation already does this;
worth keeping as an explicit design constraint rather than an emergent property.

**c) Shed-capacity bypass via market BUY orders (historical exploit, now patched).**
Until PR [#1386](https://github.com/Kaggle/kaggle-environments/pull/1386) (merged 2026-08-04, **2 days before**
this research), `BUY_PRODUCT`/`BUY_ANIMAL` market orders deposited into the shed **without checking the
100-item cap** — a player could exceed `shedCapacity` by buying past it (every other deposit path — PICKUP/DROP,
PLACE, end-of-day drop — already enforced the cap). This is now fixed: overshooting orders **partially fill to
exactly capacity and stop**, no charge/no depletion beyond that. Practical implication: **verify the locally
installed `kaggle-environments` pip package is ≥ the release containing this fix** (package version bumped
1.32.3→1.32.4 same day, PR [#1389](https://github.com/Kaggle/kaggle-environments/pull/1389)) — testing against
an older pinned version would validate against stale, exploitable rules.

**d) Locked-tile action gap (currently live bug, opponent-irrelevant but self-relevant).**
PR [#1381](https://github.com/Kaggle/kaggle-environments/pull/1381) (merged Aug 3) fixed farm hands getting
permanently **stranded** on locked shed-access tiles by allowing movement on/off locked terrain. But issue/PR
[#1391](https://github.com/Kaggle/kaggle-environments/pull/1391) — **still OPEN as of 2026-08-05** — covers a
follow-on bug: a unit standing on a locked tile still **cannot** perform `PICKUP`/`DROP`/`PLACE` (shed-access
ops), even though it's now free to stand there. STRATEGY.md's own gotcha ("(5,4) is in locked NE — passable,
actions no-op there until bought") is **currently accurate** per the live engine, but this is an open,
in-progress fix — if merged before Sept 23, any hand-routing logic that deliberately avoids locked shed-tiles
for pickup/drop could become unnecessarily conservative (leaving throughput on the table) once the fix lands.
Not opponent-exploitable (symmetric rule), but worth a periodic recheck of engine version before the deadline.

**e) Atomic PLANT seed-shortage — reclassified.**
STRATEGY.md already flags "if two units PLANT the same crop with too few seeds, all fail." Per the observation
schema (`private.seeds` is per-player, not shared), this **cannot be triggered by an opponent** — it's a
self-inflicted scheduler bug risk only, correctly already filed under STRATEGY.md's own "Gotchas checklist"
rather than a cross-player counter-strategy. No opponent mitigation needed; only internal scheduler correctness.

**f) No-arbitrage market restriction rules out a manipulation vector.**
PR [#1135](https://github.com/Kaggle/kaggle-environments/pull/1135) (merged 2026-05-20) restricted `BUY_PRODUCT`
to **only WHEAT and FERTILIZER**, with buy quotes computed on **post-buy** inventory so "an immediate buy + sell
against an unchanged market nets exactly zero." This directly confirms STRATEGY.md's "round-trip = $0" claim and
rules out a whole class of counter-play: neither player can bait the other into a profitable market-timing
arbitrage loop, and there's no mechanism for one player to manipulate market price *for* the other's benefit or
detriment except through the shared-inventory glut/scarcity curves already covered in (a) and (b). No additional
mitigation needed here — the engine already closes this off.

---

## 4. GitHub issues/PRs — bugs and balance changes (kaggriculture.py history)

Full commit history for `kaggle_environments/envs/kaggriculture/kaggriculture.py`, pulled via GitHub commits API
(`api.github.com/repos/Kaggle/kaggle-environments/commits?path=...`) — **13 commits total**, 2026-05-08 through
2026-08-04, i.e. the engine is ~3 months old and was still being patched days before this research:

| Date | PR | Change | Relevance to STRATEGY.md |
|---|---|---|---|
| 2026-08-04 | [#1385](https://github.com/Kaggle/kaggle-environments/pull/1385) | Docs clarified from competitor feedback (no engine change) | See §2 — watering/weed/animal-escape rules now explicit |
| 2026-08-04 | [#1386](https://github.com/Kaggle/kaggle-environments/pull/1386) | **Bugfix**: shed-capacity now enforced on `BUY_PRODUCT`/`BUY_ANIMAL` (was bypassable) | Verify local pip package ≥ this fix (see §3c) |
| 2026-08-03 | [#1381](https://github.com/Kaggle/kaggle-environments/pull/1381) | **Bugfix**: hands no longer permanently stranded on locked tiles; movement onto/off locked tiles allowed | See §3d |
| 2026-08-05 | [#1391](https://github.com/Kaggle/kaggle-environments/pull/1391) (**OPEN, unmerged**) | Would allow `PICKUP`/`DROP`/`PLACE` while standing on locked terrain | Currently still a no-op per STRATEGY.md's gotcha — may change before deadline |
| 2026-07-24 | [#1364](https://github.com/Kaggle/kaggle-environments/pull/1364) | Docs-only: corrected stale goose/cow/sheep price docs to match actual `ANIMALS`/`MARKET_PARAMS` in source | Confirms source-of-truth was previously out of sync with docs — always trust `kaggriculture.py` over README, as STRATEGY.md already does |
| 2026-06-12 | [#1242](https://github.com/Kaggle/kaggle-environments/pull/1242) | Added shared `resolve_episode_seed` helper; kaggriculture uses random 31-bit seed per episode, hidden from obs | See §1 — confirms no seed predictability |
| 2026-06-02 | [#1199](https://github.com/Kaggle/kaggle-environments/pull/1199) | **Balance**: quadrupled glut-crash slope for premium goods (base >$100: strawberry, melon, milk, wool); cow cost 600→400 | Explains STRATEGY.md's low premium-good floor unit counts (§3b); STRATEGY's $400 cow price is current |
| 2026-05-21 | [#1145](https://github.com/Kaggle/kaggle-environments/pull/1145) | **Balance**: startingMoney 2000→3000; townCenterSellInterval 6→12; townShopSellInterval 2→4; farmHandCostMult 10→1 | All match STRATEGY.md's assumed defaults exactly |
| 2026-05-21 | [#1142](https://github.com/Kaggle/kaggle-environments/pull/1142) | Added `DROP` action (dump inventory into shed) | STRATEGY.md's blueprint already references this |
| 2026-05-20 | [#1135](https://github.com/Kaggle/kaggle-environments/pull/1135) | **Balance/anti-exploit**: `BUY_PRODUCT` restricted to WHEAT/FERTILIZER only, no-arb round-trip | See §3f |
| 2026-05-19 | [#1107](https://github.com/Kaggle/kaggle-environments/pull/1107) | **Balance**: animal buff — cost −25%, first-yield-day −20% faster (toned down from an initial "8x" proposal after reviewer pushback) | Explains why animal ROI is currently favorable in STRATEGY.md's math; a further buff/nerf here is plausible before the deadline |
| 2026-05-19 | [#1112](https://github.com/Kaggle/kaggle-environments/pull/1112) | Fibonacci hire-cost model introduced with configurable multiplier | Basis for STRATEGY.md's `fib(n)` hire-cost table |
| 2026-05-18 | [#1108](https://github.com/Kaggle/kaggle-environments/pull/1108) | **Rewrite**: per-resource shape-function price curves (linear/sq/sqrt/log/log10) | Basis for STRATEGY.md's entire §1 price-curve math |
| 2026-05-12 | [#1092](https://github.com/Kaggle/kaggle-environments/pull/1092) | Rebalance: market-order cap set to 10/turn (now configurable); starting money to 2000 (later re-raised to 3000 by #1145); melon removed from town-shop consumption (was "overpowered") | Confirms `maxMarketOrdersPerTurn=10` origin; confirms melon's one-time-jackpot character (town never buys it back — matches STRATEGY.md's "fertilizer 0, melon 8/day center only" table) |
| 2026-05-08 | [#1072](https://github.com/Kaggle/kaggle-environments/pull/1072) | Initial "advanced version of kaggriculture" created (from an earlier simpler prototype) | Origin commit — env is genuinely new (~3 months old at research date) |

**Note on env naming**: the repo currently contains **two** kaggriculture folders —
`kaggle_environments/envs/kaggriculture` (title *"Kaggriculture"*, description *"Advanced farming
simulation..."*, 10×10 board, full market/animals/town) and
`kaggle_environments/envs/kaggriculture_beginner` (title *"Kaggriculture (Beginner)"*, 5×5 board, **fixed
prices, no animals/town/inventory/farm hands**). The live competition at `kaggle.com/competitions/kaggriculture`
maps to the **advanced** folder (confirmed: matches STRATEGY.md's 10×10/quadrant/market description exactly).
The beginner variant appears to be a separate tutorial/teaching environment from the same May 2026 development
window (PRs [#1159](https://github.com/Kaggle/kaggle-environments/pull/1159),
[#1137](https://github.com/Kaggle/kaggle-environments/pull/1137)) — flagged only so it isn't mistaken for the
competition engine if encountered in the repo or in unrelated notebooks/tutorials.

**Notebooks checked**: `kaggle.com/code/bovard/kaggriculture-getting-started` (official starter — content is
essentially the same walkthrough now folded into `AGENTS.md`, no strategy beyond the wheat-loop example already
covered in STRATEGY.md) and `kaggle.com/code/pilkwang/kaggriculture-observable-economic-control` (could not be
fetched — returned HTTP 404 both with and without the version query string; Kaggle notebook pages are also
SPA-rendered and inaccessible to this session's tools). No other public strategy notebooks were found via search.

---

## Sources

- [`kaggriculture.py`](https://github.com/Kaggle/kaggle-environments/blob/master/kaggle_environments/envs/kaggriculture/kaggriculture.py) — engine source (39KB), source of truth for all mechanics
- [`kaggriculture.json`](https://github.com/Kaggle/kaggle-environments/blob/master/kaggle_environments/envs/kaggriculture/kaggriculture.json) — spec: `episodeSteps`, `actTimeout`, `remainingOverageTime`, `agents`, config defaults, observation/action schema
- [`AGENTS.md`](https://github.com/Kaggle/kaggle-environments/blob/master/kaggle_environments/envs/kaggriculture/AGENTS.md) — getting-started guide, full observation/action field reference, CLI workflow
- [kaggriculture_beginner folder](https://github.com/Kaggle/kaggle-environments/tree/master/kaggle_environments/envs/kaggriculture_beginner) — separate simplified tutorial env, not the competition
- PRs (chronological, all fetched via `gh`/GitHub API/WebFetch):
  [#1072](https://github.com/Kaggle/kaggle-environments/pull/1072),
  [#1092](https://github.com/Kaggle/kaggle-environments/pull/1092),
  [#1107](https://github.com/Kaggle/kaggle-environments/pull/1107),
  [#1108](https://github.com/Kaggle/kaggle-environments/pull/1108),
  [#1112](https://github.com/Kaggle/kaggle-environments/pull/1112),
  [#1135](https://github.com/Kaggle/kaggle-environments/pull/1135),
  [#1142](https://github.com/Kaggle/kaggle-environments/pull/1142),
  [#1145](https://github.com/Kaggle/kaggle-environments/pull/1145),
  [#1199](https://github.com/Kaggle/kaggle-environments/pull/1199),
  [#1242](https://github.com/Kaggle/kaggle-environments/pull/1242),
  [#1364](https://github.com/Kaggle/kaggle-environments/pull/1364),
  [#1381](https://github.com/Kaggle/kaggle-environments/pull/1381),
  [#1385](https://github.com/Kaggle/kaggle-environments/pull/1385),
  [#1386](https://github.com/Kaggle/kaggle-environments/pull/1386),
  [#1391 (open)](https://github.com/Kaggle/kaggle-environments/pull/1391)
- [`kaggle-cli` simulation competitions doc](https://github.com/Kaggle/kaggle-cli/blob/main/docs/simulation_competitions.md) — generic sim-comp CLI workflow reference
- [Orbit Wars overview](https://www.kaggle.com/competitions/orbit-wars/overview) — sibling competition, source of the **[INFERRED]** skill-rating/submission-limit boilerplate (indexed snippet only, not directly fetched)
- [Kaggriculture competition](https://www.kaggle.com/competitions/kaggriculture) / [discussion](https://www.kaggle.com/competitions/kaggriculture/discussion) — unreachable this session (SPA, no tool access); prize pool $50,000, entry deadline Sept 23 2026 confirmed via [Kaggle's announcement tweet](https://x.com/kaggle/status/2084326711248687165)
- [Kaggriculture: Getting Started notebook](https://www.kaggle.com/code/bovard/kaggriculture-getting-started) — official starter, content mirrors AGENTS.md
- [Kaggriculture: Observable Economic Control notebook](https://www.kaggle.com/code/pilkwang/kaggriculture-observable-economic-control) — could not fetch (404 via WebFetch, SPA-blocked)
- Announcement tweets: [Kaggle](https://x.com/kaggle/status/2084326711248687165), [Paige Bailey](https://x.com/DynamicWebPaige/status/2082871191921144055), [Abdel Sghiouar](https://x.com/boredabdel/status/2084980345691144535) — timeline/prize confirmation only

---

## Analysis

The single most useful discovery beyond STRATEGY.md's existing engine-source read is that **the ruleset is not
frozen** — three balance/bugfix PRs landed in the 48 hours immediately before this research (Aug 3–4), and one
more is open and under active review (Aug 5). This means STRATEGY.md's numeric tables, while verified against
current source, have a real shelf life risk over the ~7 remaining weeks to the Sept 23 deadline: premium-good
glut slopes, animal costs, and hire multipliers have each been rebalanced at least once already in the engine's
3-month life, and shed-capacity/locked-tile action bugs were still being found and fixed within the last week.
Every number in STRATEGY.md should be treated as "correct as of 2026-08-06" rather than permanently fixed, and
re-diffed against `kaggriculture.py` periodically (a low-cost `git diff` against the pinned commit used for the
original research would catch this cheaply). Separately, the almost-total absence of discoverable community
discussion is itself informative: this is early enough in the competition's life that there is no meta yet to
react to, and no evidence any competitor has found an exploit beyond what the engine team is already patching
proactively (in fact, PR #1385's "based on competitor feedback" suggests competitors are the ones surfacing
these edge cases to the maintainers, which is worth mining directly if discussion-tab access is regained).

## Open Questions / Gaps

- **Kaggriculture's own skill-rating formula, σ-decay rate, and submission cap were not independently confirmed
  on its own page** — everything in §1 beyond the JSON-confirmed engine params is inferred from a sibling
  competition's boilerplate. High probability of being correct (same template family, same launch window) but
  not verified first-hand.
- **Discussion tab content is completely inaccessible this session** — no way to distinguish "no one has said
  anything yet" from "content exists but our tools can't reach it." Needs a logged-in/authenticated fetch to
  resolve definitively.
- **PR #1391 (locked-tile PICKUP/DROP/PLACE) is unresolved** — outcome and merge date unknown; re-check before
  finalizing any hand-routing logic that special-cases locked shed-access tiles.
- **No visibility into other competitors' actual submitted agents or their strategies** — §3's counter-strategy
  analysis is necessarily theoretical (derived from engine mechanics), not observed. This will remain a gap
  until episodes/replays against real opponents are available (post-first-submission).
- Whether kaggriculture will receive further balance patches before Sept 23 (animal ROI, premium-good curves,
  and hire cost have each already been tuned at least once) is unknown and worth periodic re-checking.
