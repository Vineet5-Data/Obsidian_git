src = open("main.py", encoding="utf-8").read()

# The species swap is net negative: cutting our own milk output makes milk
# scarcer for the opponent.  Base loses every elite matchup 96.6k vs 100.4k;
# leaving the recorded 8 COW / 6 SHEEP split ties it exactly at 92.3k.
src = src.replace("ANIMAL_SWITCH_DAY = 3", "ANIMAL_SWITCH_DAY = 999\nLIQ_LEAD = 6", 1)

old = '''def _terminal_liquidation(obs, action):
    if int(_get(obs, "step", 0) or 0) < len(_ACTIONS) - 1:
        return action'''
new = '''def _terminal_liquidation(obs, action):
    """Liquidate over the closing steps rather than only on the final one.

    Both sides of a cloned route dump the shed on step 719 into the same
    order book.  Starting `LIQ_LEAD` steps early sells into their pre-dump
    prices instead of the crater that the simultaneous dump creates.
    """
    step = int(_get(obs, "step", 0) or 0)
    if step < len(_ACTIONS) - 1 - int(LIQ_LEAD):
        return action'''
assert old in src
src = src.replace(old, new, 1)

open("v8.py", "w", encoding="utf-8").write(src)
print("v8.py written")
