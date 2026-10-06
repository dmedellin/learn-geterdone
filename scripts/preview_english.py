#!/usr/bin/env /usr/bin/python3
"""Render the English Subject to a scratch directory WITHOUT wiring it.

Wiring a Subject touches about two dozen declaration sites (AGENTS.md section
0), and nothing should reach GENERATED_PATHS by accident. This renders the same
pages build_paths would, into the scratchpad, so the page weight, the band
check and labcheck's expectations can all be measured before anything is
declared anywhere.
"""
import json
import pathlib
import sys

REPO = pathlib.Path("/home/dmedellin/.hermes/workspaces/learn-ui-standardization")
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/english-preview")
sys.path.insert(0, str(REPO / "scripts"))
sys.path.insert(0, str(REPO / "content"))

import build_paths                                        # noqa: E402
from english import PATH                                  # noqa: E402

OUT.mkdir(parents=True, exist_ok=True)
expectations = {}
for rel, markup, expect in build_paths.path_pages(PATH):
    dest = OUT / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(markup, encoding="utf-8")
    if expect is not None:
        expectations[rel.rsplit("/index.html", 1)[0]] = expect
    print("%8d bytes  %s" % (len(markup.encode("utf-8")), rel))
(OUT / "expectations.json").write_text(json.dumps(expectations, indent=2))
print("\n%d page(s) -> %s" % (len(list(OUT.rglob("index.html"))), OUT))
