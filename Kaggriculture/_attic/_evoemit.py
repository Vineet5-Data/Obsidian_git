"""Materialise an evolved genome into a real, submittable agent file.

The evolver keeps genomes as a sparse {step: market} diff so mutation stays
cheap.  This bakes the diff back into the base64+zlib tape blob, so the output
is a standalone agent -- no diff file, no import of _evolve at match time.

Usage:  python _evoemit.py [.evo/best.json] [.evo/v27.py]
"""
import base64
import importlib.util
import json
import sys
import textwrap
import zlib

BASE = "v26.py"
BLOB_START, BLOB_END = 10, 110          # 1-based, inclusive (verified in v26.py)


def main():
    genome_path = sys.argv[1] if len(sys.argv) > 1 else ".evo/best.json"
    out_path = sys.argv[2] if len(sys.argv) > 2 else ".evo/v27.py"

    spec = importlib.util.spec_from_file_location("emit_base", BASE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    tape = module._ACTIONS

    genome = json.load(open(genome_path))
    for step, market in genome.items():
        tape[int(step)]["market"] = market

    blob = base64.b64encode(
        zlib.compress(json.dumps(tape, separators=(",", ":")).encode(), 9)
    ).decode()
    body = "\n".join(f"    {line!r}"
                     for line in textwrap.wrap(blob, 96))
    replacement = ("_ACTIONS = json.loads(zlib.decompress(base64.b64decode(\n"
                   "    (\n" + body + "\n    )\n)))\n")

    lines = open(BASE, encoding="utf-8").read().splitlines(keepends=True)
    assert lines[BLOB_START - 1].startswith("_ACTIONS ="), lines[BLOB_START - 1]
    assert lines[BLOB_END - 1].rstrip() == ")))", lines[BLOB_END - 1]
    out = "".join(lines[:BLOB_START - 1]) + replacement + "".join(lines[BLOB_END:])
    open(out_path, "w", encoding="utf-8").write(out)

    # round-trip check: the emitted file must decode to the tape we intended
    spec = importlib.util.spec_from_file_location("emit_out", out_path)
    check = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(check)
    assert check._ACTIONS == tape, "emitted tape does not round-trip"
    print(f"{out_path}  {len(out):,} bytes  {len(genome)} edits baked, "
          f"round-trip ok")


if __name__ == "__main__":
    main()
