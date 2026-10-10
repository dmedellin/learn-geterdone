"""Spoken forms for Accumulation and the Integral (Differential Equations).

Keyed by the exact run text; see content/AGENTS.md, "Write math a voice can read".
Three runs below put a prime on a bracket. The general rules read the prime
onto the last letter inside it, so "(F·G)′" comes out "F times G prime", which
a listener hears as F times G-prime; these forms say what is differentiated.
The fourth is the differential named on its own, where the lesson teaches the
notation: inside an integral the rules already read it "d t", and the same
reading is right wherever "dt" stands alone.
"""

SPOKEN = {
    "dt": "d t",
    "(c·F + d·G)′ = c·f + d·g": "the derivative of c times F plus d times G equals c times f plus d times g",
    "(F·G)′": "the derivative of F times G",
    "(t³/3)′ = 3t²/3 = t²": "the derivative of t cubed over 3 equals 3 t squared over 3, which is t squared",
}
