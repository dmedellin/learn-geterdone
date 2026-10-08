"""Spoken forms for the math runs of Philosophy course 10, Paradoxes and Their Exits.

Keyed by the exact run text; see content/AGENTS.md, "Write math a voice can read".
"""

SPOKEN = {
    '∀x (Shaves(b, x) ↔ ¬Shaves(x, x))': 'for every x, the barber shaves x if and only if x does not shave x',
    '∀x (Villager(x) → (Shaves(b, x) ↔ ¬Shaves(x, x)))': 'for every x, if x is a villager then the barber shaves x if and only if x does not shave x',
    '□': 'the box, read as it is known that',
    'p ∧ ¬□p': 'p and it is not known that p',
    '¬□p': 'it is not known that p',
    '□(p ∧ ¬□p)': 'it is known that p and it is not known that p',
    'Moore: p ∧ ¬□p, read as p but I do not know p': 'Moore. p and it is not known that p, read as p but I do not know p',
    '□(p ∧ ¬□p): true at no reflexive world': 'it is known that p and it is not known that p, is true at no reflexive world',
    '□p → p': 'if it is known that p, then p',
}
