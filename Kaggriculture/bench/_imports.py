"""Report which Top_players files import cleanly and expose a callable agent.

benchmark_vs_top.py swallows import failures in a bare `except` and prints a
one-line Skipping notice, so a silently-dropped opponent looks identical to an
opponent that was never there.  results.json is missing all six 908* bots;
this says why.
"""
import importlib.util
import os
import sys
import traceback

TOP = os.path.join(os.path.dirname(__file__), "..", "Top_players")

for fname in sorted(f for f in os.listdir(TOP) if f.endswith(".py")):
    path = os.path.join(TOP, fname)
    try:
        spec = importlib.util.spec_from_file_location(fname[:-3], path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        fn = getattr(mod, "agent", None)
        if fn is None:
            print(f"{fname:16s} NO agent ATTR")
        else:
            print(f"{fname:16s} ok  argcount={fn.__code__.co_argcount}")
    except Exception:
        exc = traceback.format_exc().strip().splitlines()[-1]
        print(f"{fname:16s} IMPORT FAILED  {exc}")
