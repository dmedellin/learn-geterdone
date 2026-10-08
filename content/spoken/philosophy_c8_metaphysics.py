"""Spoken forms for Philosophy, Identity, Modality and Freedom.

Keyed by the exact run text the lesson prints; see content/AGENTS.md, "Write math a
voice can read". The ship of Theseus writes its tolerance conditional as an arrow
between function applications, which the rules read as "goes to"; here it is read
as the conditional it is.
"""

SPOKEN = {
    "F(k) → F(k − 1)": "F of k implies F of k minus 1",
    "F(1000) → F(999)": "F of 1000 implies F of 999",
    "F(999) → F(998)": "F of 999 implies F of 998",
    "F(1) → F(0)": "F of 1 implies F of 0",
    "F(500) → F(499)": "F of 500 implies F of 499",
    "tolerance: F(k) → F(k − 1) at each step": "tolerance, F of k implies F of k minus 1, at each step",
    "ca": "c a",
    "cb": "c b",
    "ia": "i a",
    "ib": "i b",
    "ca → ia": "c a implies i a",
    "cb → ib": "c b implies i b",
    "ca → ma": "c a implies m a",
    "cb → mb": "c b implies m b",
    "¬(ia ∧ ib)": "not both i a and i b",
    "1.  ca            A is continuous with me": "1, c a, A is continuous with me",
    "2.  cb            B is continuous with me": "2, c b, B is continuous with me",
    "3.  ca → ia       continuity suffices for A to be me": "3, c a implies i a, continuity suffices for A to be me",
    "4.  cb → ib       continuity suffices for B to be me": "4, c b implies i b, continuity suffices for B to be me",
    "5.  ¬(ia ∧ ib)    A and B are not both me": "5, not both i a and i b, A and B are not both me",
    "drop 5: ia and ib both true is allowed": "drop 5, i a and i b both true is allowed",
    "drop 3: ib is forced true, so ia must be false": "drop 3, i b is forced true, so i a must be false",
    "drop 4: ia is forced true, so ib must be false": "drop 4, i a is forced true, so i b must be false",
    "p → q": "p implies q",
    "N(p → q)": "N of p implies q",
    "(a, b)": "the pair a, b",
    "(b, c)": "the pair b, c",
    "(a, c)": "the pair a, c",
    "(1, 2)": "the pair 1, 2",
    "(2, 3)": "the pair 2, 3",
    "(1, 3)": "the pair 1, 3",
    "(1, 4)": "the pair 1, 4",
    "(1, 5)": "the pair 1, 5",
    "(2, 4)": "the pair 2, 4",
    "(2, 5)": "the pair 2, 5",
    "(3, 5)": "the pair 3, 5",
    "(3, 1)": "the pair 3, 1",
}
