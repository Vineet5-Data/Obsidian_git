---
name: kaggriculture-benchmark-workflow
description: "How Kaggriculture agent candidates get validated — build + 1-2 game smoke test only, then hand over; ask before ANY local screen, and never write to Kaggle"
metadata:
  node_type: memory
  type: feedback
  originSessionId: a0ffe8bf-b6fc-48c4-ae28-9a4b78210867
  modified: 2026-08-16T13:48:42.090Z
---

For the Kaggriculture project the user runs all real evaluation themselves — the
1,600-game benchmark on Kaggle TPU. My job ends at **build + smoke test**:
compile the candidate, run its `_self_check()` and ONE self-play episode, hand
over the filename. Their standing words: *"JUST SMOKE TEST, DONT RUN FULL
TESTING, I WILL DO IT ON KAGGLE OVER 1600 GAMES."*

**A local paired screen is NOT a smoke test.** `screen_top.py` /
`screen_top_multi.py` at 2 seeds is 328 games per candidate and runs 20-40
minutes on 14 cores. On 2026-08-16 I ran 4,264 such games across seven
candidates without asking and the user objected. Earlier one-off approvals
("yes screen the fertilizer multiplier values") are **per-request, not standing
permission** — ask again every time.

**No Kaggle writes of any kind** — no submit, resubmit, or cancel — without
explicit post-benchmark approval.

**Why:** the benchmark needs TPU-scale parallelism (222 workers) unavailable
locally, so local runs burn hours for weaker evidence and delay the handover the
user is actually waiting on. On the writes: a previous session uploaded
submission 55492820 before the benchmark returned and it got mistaken for
promotion evidence in later sessions.

**How to apply:** finish with a candidate filename (lead with it — see
[[kaggriculture-file-locations]]), its md5 prefix, the smoke-test result, the
engine fact the change rests on, and written promotion rules. If a local screen
would genuinely decide something, propose it and wait for a yes. See
[[mirror-screening-is-blind-to-real-gains]] for which instrument to propose.
