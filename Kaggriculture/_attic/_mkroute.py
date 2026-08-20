"""Build a route agent from any extracted tape + v13's runtime overlay.

Usage:  python _mkroute.py <tape.json.z> <out.py> ["docstring"]

The overlay (hand alignment, animal adaptation, idle fill, terminal
liquidation) is v13's, carried over byte-for-byte so a screen against v13
isolates the route change and nothing else.
"""
import base64
import json
import sys
import textwrap
import zlib


def build(tape_path, out_path, note=""):
    with open(tape_path, "rb") as handle:
        tape = json.loads(zlib.decompress(handle.read()).decode("utf-8"))

    blob = base64.b64encode(
        zlib.compress(json.dumps(tape, separators=(",", ":")).encode(), 9)
    ).decode()
    literal = "\n".join("    '%s'" % line for line in textwrap.wrap(blob, 100))

    src = open("v13.py", encoding="utf-8").read()
    tail = src[src.index("def _get("):]

    header = '''"""%s"""

import base64
import copy
import json
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
%s
    )
)))


''' % (note or "Route agent built from a fresh Top-30 replay tape.", literal)

    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(header + tail)
    return len(tape), max(len(a["hands"]) for a in tape)


if __name__ == "__main__":
    steps, hands = build(sys.argv[1], sys.argv[2],
                         sys.argv[3] if len(sys.argv) > 3 else "")
    print(f"{sys.argv[2]}: {steps} steps, max hands {hands}")
