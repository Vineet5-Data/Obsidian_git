---
name: kaggle-entry-point-must-be-last-callable
description: "Kaggle runs the LAST callable in a submitted file, not the one named agent; the a_v186 lineage guards this with a trailing rebind — verify after edits."
metadata: 
  node_type: memory
  type: project
  originSessionId: 208236e3-55b9-4521-bc1c-8aa6d1b33e2a
  modified: 2026-08-20T14:27:53.494Z
---

`kaggle_environments/agent.py:64` resolves a submitted Python file with:

```python
return [v for v in env.values() if callable(v)][-1]
```

The **last callable bound in the module namespace wins, regardless of its
name**. Any `def` after `agent` is what actually runs. In this repo that would
be `_self_check(observation, configuration)`, which takes no arguments, raises
`TypeError`, and the engine substitutes the default PASS for all 720 steps — the
agent scores its starting money and the failure is silent.

**The a_v186 lineage already guards this** with a trailing
`_kaggle_agent_entry = agent`, which rebinds the same function object last so
`[-1]` resolves to `agent`. Verified empirically 2026-08-20 for a_v186, a_v205,
a_v206, a_v209 — all resolve to `agent`.

**Why:** local harnesses (`_loss_analysis.py`, `_econ_loss_analysis.py`) load
`m.agent` by name and never exercise this path, so a broken entry point passes
every local benchmark and only fails on submission.

**How to apply:** the guard must stay the last statement in the file. After any
edit that appends code, re-check with:

```python
from kaggle_environments.agent import get_last_callable
get_last_callable(open(f, encoding="utf-8").read(), path=f).__name__  # == "agent"
```

Related: [[kaggriculture-candidate-loop]]
