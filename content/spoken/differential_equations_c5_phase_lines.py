"""Spoken forms for the math runs of Equilibria, Stability and Phase Lines that read-out can only guess at.

Keyed by the exact run text; see content/AGENTS.md, "Write math a voice can read".
The rules guess at none of this course's notation. The two entries below are
sign patterns read off a phase line, which the rules read with a lone "−" as
"negative"; a sign pattern is minus and plus wherever it appears.
"""

SPOKEN = {
    "−, +, −, +": "minus, plus, minus, plus",
    "+, +, −": "plus, plus, minus",
}
