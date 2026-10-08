"""Spoken forms for Philosophy, Arguments and Validity.

The read-out rules say an arrow as "goes to" in some positions and "implies" in
others, say the exclusive-or sign as "x or", and read the equivalence sign
between capital letters as "congruent to". Each run here is the exact text the
lesson prints; the words are what a listener should hear.
"""

SPOKEN = {
    "p ⊕ q  true when exactly one is true": "p exclusive or q, true when exactly one is true",
    "p ⊕ q": "p exclusive or q",
    "p   q  |  ¬p   p ∧ q   p ∨ q   p ⊕ q": "p, q, not p, p and q, p or q, p exclusive or q",
    "soup  salad  |  inclusive (∨)   exclusive (⊕)": "soup, salad, inclusive or, exclusive or",
    "p → q is false in one row only": "p implies q is false in one row only",
    "p only if q:  p → q": "p only if q, p implies q",
    "p if q:  q → p": "p if q, q implies p",
    "p → q": "p implies q",
    "q → p": "q implies p",
    "v → r": "v implies r",
    "r → v": "r implies v",
    "rain  off  |  r → m   what happened": "rain, off, r implies m, what happened",
    "t → e": "t implies e",
    "e → t": "e implies t",
    "p → q, p ∴ q    modus ponens: valid": "p implies q, p therefore q, modus ponens, valid",
    "p → q, q ∴ p    affirming the consequent": "p implies q, q therefore p, affirming the consequent",
    "p → q, q ∴ p": "p implies q, q therefore p",
    "p   q  |  p → q   p   q": "p, q, p implies q, p, q",
    "p   q  |  p → q   q   p": "p, q, p implies q, q, p",
    "premises:   p → q ,  q          conclusion:  p": "premises, p implies q, q, conclusion, p",
    "row  p  q  |  p → q  q  |  p": "row, p, q, p implies q, q, p",
    "A ≡ B": "A is equivalent to B",
    # part B
    "non-P": "non P",
    "non-S": "non S",
    "q → r": "q implies r",
    "p → r": "p implies r",
    "r → s": "r implies s",
    "1  p → q        p=T q=F r=F": "1, p implies q, p equals T, q equals F, r equals F",
    "2  q → r        p=T q=T r=F": "2, q implies r, p equals T, q equals T, r equals F",
    "1.  p → q     if it was set, it rang": "1, p implies q, if it was set, it rang",
    "2.  q → r     if it rang, she woke": "2, q implies r, if it rang, she woke",
    "p → q, q → r ∴ p → r     valid": "p implies q, q implies r, therefore p implies r, valid",
    "∀x (S(x) → P(x))": "for every x, S of x implies P of x",
    "∃x (S(x) ∧ P(x))": "there exists x such that S of x and P of x",
    "∀x P(x)": "for every x, P of x",
    "∃x P(x)": "there exists x such that P of x",
    "∀x ∃y P(x, y)": "for every x there exists y such that P of x and y",
    "∃y ∀x P(x, y)": "there exists y such that for every x, P of x and y",
    "∃x ∃y P(x, y)": "there exists x and there exists y such that P of x and y",
    "∀x ∃y": "for every x there exists y",
    "∃y ∀x": "there exists y such that for every x",
    "∃x ∀y": "there exists x such that for every y",
    "∃y ∀x: one y serves every x": "there exists y such that for every x, one y serves every x",
    "∃y ∀x implies ∀x ∃y, not the reverse": "there exists y such that for every x implies for every x there exists y, not the reverse",
    "∀x ∃y P    each x has its own y      a true cell per row": "for every x there exists y, each x has its own y, a true cell per row",
    "∃y ∀x P    one y serves every x      a column all true": "there exists y such that for every x, one y serves every x, a column all true",
    "∃x ∀y P    one x pairs with every y  a row all true": "there exists x such that for every y, one x pairs with every y, a row all true",
    "∀y ∃x P    each y has its own x      a true cell per column": "for every y there exists x, each y has its own x, a true cell per column",
}
