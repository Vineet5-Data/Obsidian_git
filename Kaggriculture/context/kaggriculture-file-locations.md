---
name: kaggriculture-file-locations
description: "The user looks for Kaggriculture agent files in Downloads, not the repo — deliver new candidates to both"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a0ffe8bf-b6fc-48c4-ae28-9a4b78210867
  modified: 2026-08-14T08:02:22.803Z
---

The user's Kaggriculture agent files are split across two directories:
older ones (v113-v120) live in `C:\Users\Vinee\Downloads\`, while v122 and
everything newer was created in the repo at
`C:\Users\Vinee\Desktop\Kaggriculture\`. The user looks in **Downloads** when
uploading to the Kaggle `kg-bisect` dataset.

**Why:** a session delivered `a_v123b_harvest_atrisk.py` to the repo only and
the user reported "there no such file" — they were looking in Downloads.
Benchmark inputs also arrive in Downloads (`*_loss_analysis.md`,
`KAGGRICULTURE_SESSION_CROSSOVER*.md`).

**How to apply:** when a candidate is finished, copy it to Downloads as well
as the repo, verify both hashes match, and send it with SendUserFile. The repo
copy stays authoritative. Re-sync Downloads after any later edit — even a
docstring change moves the SHA the user is told to verify. See
[[kaggriculture-benchmark-workflow]].
