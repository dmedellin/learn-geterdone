"""Spoken forms for the runs in Differential Equations and Euler's Method.

Keyed by the exact run text; see content/AGENTS.md, "Write math a voice can read".
Every entry is a run that reads wrongly under the global rules and must keep its
notation: `1/h` is read by the engine as "1 per h", and a rounded figure in
scientific form as "e 23".
"""

SPOKEN = {
    "E(h) = |y_N − y(T)|,  N = (T − t₀)/h": "E of h equals the absolute value of y sub N minus y of T, and N equals the quantity T minus t sub 0, over h",
    "E(h) = |y_N − y(T)|": "E of h equals the absolute value of y sub N minus y of T",
    "|y_N − y(T)|": "the absolute value of y sub N minus y of T",
    "1/h": "1 over h",
    "N = 1/h": "N equals 1 over h",
    "h²·(1/h) = h": "h squared times the quantity 1 over h, equals h",
    "(1/h)·h² = h": "the quantity 1 over h, times h squared equals h",
    "≈ 6.77729e23": "is approximately 6.77729 times 10 to the power 23",
}
