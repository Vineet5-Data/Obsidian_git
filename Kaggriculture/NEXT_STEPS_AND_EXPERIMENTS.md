# Experiment Log & Next Steps

This document summarizes all the recent changes, experiments, and tooling upgrades we've performed to improve our Kaggle Kaggriculture agent from the `v186` baseline (68% win rate) to our target of 80%+. It also outlines the concrete next steps to achieve this goal.

## 1. What We've Done So Far (Experiments & Changes)

### Agent Tweaks (The "AP Bottleneck Fix")
- **Animal Cap Reduction**: We reduced the `animal_cap` from 20 down to 13 in recent agent iterations (`a_v200.py`). This was to prevent the agent from getting overwhelmed with feeding/caring tasks in the late game.
- **Crop Cap Share**: We adjusted `crop_cap_share` to max out at 50 crops to prevent planting explosions that consume all Action Points (AP).

### Diagnostic & Tooling Upgrades
Our primary finding was that our agents perform well in the early game (Days 0-19) but suffer severe revenue collapse and divergence in the late game (Days 20-29). To diagnose this precisely, we vastly improved our diagnostic pipeline:

- **Telemetry Snapshots**: Ensured `play_one.py` and our agents correctly log and export `telemetry_snapshot()`.
- **Unified `_loss_analysis.py`**: Merged the behavioral telemetry analysis and the economic analysis into a single, comprehensive script. 
- **Reinstated Critical Metrics**:
  - `money delta by day`: Pinpoints exactly which day we start falling behind our opponents.
  - `SERVICE TELEMETRY`: Exposes internal agent logic, tracking how many actions (e.g., `CARE`, `WATER`, `SELL`) were created vs. actually executed, as well as tracking crop expiries and missed animal yields (cap ticks).
- **New Feature - `avg realized price / unit`**: Added a new metric to the day-windowed economic breakdown. This calculates exactly what average price we are securing for our crops compared to the opponent.

---

## 2. How to Proceed Further (Roadmap)

Now that we have the ultimate diagnostic tool, our next steps should be entirely data-driven. We need to run the unified script and use the insights to patch the late-game logic.

### Step A: Generate the Baseline Report (Testing Constraint)
**CRITICAL CONSTRAINT**: The agent AI can only run local diagnostics on a maximum of **5-10 games** or use synthetic data. 
- The AI will run `python _loss_analysis.py a_v186.py --opponents 3 --seeds 1` (or similar small batches) to spot-check logic.
- The human user will then take the agent, manually benchmark it on Kaggle TPU against a massive opponent pool, and report back the full loss analysis file.
- The AI will then read and diagnose the massive loss analysis file provided by the user to find statistically significant patterns.

### Step B: Identify the Root Cause of the Day 20-29 Collapse
Review the generated report with a focus on three specific areas:

1. **Market Selling Patterns (The Price Gap)**
   - **What to look for**: Check the `avg realized price / unit` for premium goods (Strawberry, Milk, Melon) in Days 20-24 and 25-29. 
   - **Hypothesis**: If our realized price is significantly lower than the opponent's (e.g., our Strawberry avg is 150, theirs is 250), we are likely panic-selling at the bottom of the market or dumping our entire shed at once and crashing the price.
   - **Fix**: Implement staggered selling (e.g., sell only 10-20 units per turn) or implement a minimum price floor before the agent is allowed to sell.

2. **Action Point (AP) Starvation**
   - **What to look for**: Check the `SERVICE TELEMETRY` for Days 20-29. Look at the `exec%` (Execution Rate) for `WATER`, `HARVEST`, and `CARE`.
   - **Hypothesis**: If execution rates drop below 95%, our agent is generating more tasks than it has hands to complete. 
   - **Fix**: We need to hire more hands dynamically if the queue is backing up, or dynamically reduce planting caps in the late game to free up AP for harvesting.

3. **Wasted Assets (Expiries & Cap Ticks)**
   - **What to look for**: Look at `crop expiry with held yield` and `animal cap ticks` in the telemetry.
   - **Hypothesis**: The agent might be failing to harvest crops before they wither, or failing to collect milk/wool when the animals hit their storage cap.
   - **Fix**: Boost the priority of `HARVEST` and `CARE`/`COLLECT_FERTILIZER` in the late game relative to `PLANT`.

### Step C: Implement and Benchmark
Once we identify the exact bottleneck from the data in **Step B**:
1. Clone `v186` to a new version (e.g., `v202`).
2. Write the patch for the specific issue (e.g., a dynamic price floor function, or a late-game planting halt).
3. Benchmark the new version locally for 10 games to ensure it doesn't break.
4. **CRITICAL CONSTRAINT**: The AI will NOT upload the new agent to Kaggle. Instead, the AI will provide the exact file path of the new agent, and the human user will manually upload it to Kaggle for the full 500+ game TPU evaluation.
