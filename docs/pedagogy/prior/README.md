# Prior pedagogy assessments — superseded, kept for comparison

These are the first-pass assessments of `market-structure` (trading course 1) and
`logic-and-proof` (discrete mathematics course 1). The repairs they describe are
**live** — they are committed, on `main`, and verified green by the full gate set.
Nothing here is being reverted.

They were moved aside because both courses are being **re-assessed from scratch**
by the `pedagogical-expert` subagent on fable. A reviewer that reads the previous
verdict before forming its own tends to ratify it; the point of the second pass is
an independent read, so the current assessment directory starts empty for these two
courses and `scripts/pedagogy-run.sh` treats them as unvisited.

When the new assessment lands at `docs/pedagogy/<slug>.md`, the value of the file
here is the delta: what the second pass caught that the first missed, and anything
the first pass claimed that the second disputes. A disagreement between the two is
a finding in itself and belongs in the new assessment, not in a silent overwrite.
