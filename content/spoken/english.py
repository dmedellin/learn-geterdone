"""Spoken forms for the English Subject: there are none, and that is checked.

Every other Subject needs this file because its math runs contain notation a
voice cannot read from the characters alone -- `P(H | E)`, `⌈log_B N⌉`,
`q(3 + k)`. English has 152 math runs and NONE of them is ambiguous, because a
language Subject's monospace blocks hold words, endings and percentages rather
than formulae:

    -s 99.85%    -ing 98.97%    -ed 98.67%
    past = the have-form     60
    FAther  S.       beLIEVE   .S

`scripts/speechcheck.py` reports `english  0 unresolved  0 spoken forms`, and
that is a measured result rather than an untested one. The detector was proved
to fire before the zero was believed: `(a + b) log x` raises implicit-product,
`1/2x` raises fraction-extent, `(1,2) = 3  (4,5) = 6` raises inline-table and
`q(3 + k)` raises letter-call. It looks at English's runs -- 152 of them -- and
flags nothing.

This file exists empty rather than not existing, because `load_overrides`
treats a missing file and an empty one identically and the next person to add a
Subject should be able to tell a verified zero from a forgotten step.

If English ever gains a lesson with real notation in it -- a frequency formula,
a probability -- this is where its spoken forms go, and speechcheck will say so
before the page ships.
"""

SPOKEN = {}
