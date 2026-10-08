"""Spoken forms for Philosophy, Mind, Language and Meaning.

Keyed by the exact math run. The read-out rules say a long run of digits as one
enormous number, say a row of truth values such as TTF as a word, and say the
sentence letter a as a capital; each run here is the exact text the lesson
prints, and the words are what a listener should hear.
"""

BIG = ("thirty-six quadrillion, five hundred twenty trillion, three hundred "
       "forty-seven billion, four hundred thirty-six million, fifty-six "
       "thousand, five hundred seventy-six")

SPOKEN = {
    "v(F(k)) = k / 10000": "v of F of k equals k over 10000",
    "v(F(k) → F(k − 1)) = 1 − 1/10000 = 9999/10000": "v of F of k implies F of k minus 1, equals 1 minus 1 over 10000, equals 9999 over 10000",
    "24¹²  =  36 520 347 436 056 576": "24 to the power 12, equals " + BIG,
    "12      24¹² = 36 520 347 436 056 576": "12 turns, 24 to the power 12 equals " + BIG,
    "3       24³ = 13 824": "3 turns, 24 cubed equals thirteen thousand, eight hundred twenty-four",
    "12 144": "twelve thousand, one hundred forty-four",
    "true rows of A:   TTT   TTF   TFT": "true rows of A, true true true, true true false, true false true",
    "true rows of B:   TTT   TTF   TFT": "true rows of B, true true true, true true false, true false true",
    "a  n  |  a → ¬n   n   |  ¬a": "a, n, a implies not n, n, not a",
}
