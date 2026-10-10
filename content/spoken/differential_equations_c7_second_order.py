"""Spoken forms for math runs in Second-Order Linear Equations whose notation is ambiguous to read-out.

Keyed by the exact run text; see content/AGENTS.md, "Write math a voice can read".
The first group names sine and cosine without an argument, which the rules
read as the abbreviations "sin" and "cos"; a bare function name has one
meaning wherever it appears in a math run, so the readings are safe to share.
The second group is runs whose bracket is followed by a prime: the rules drop
"the quantity" there, so (t·e^(rt))′ would be heard as t times the rate of the
exponential. The last group reads subscripted functions of 0 and t in the
Wronskian lesson.
"""

SPOKEN = {
    "sin": "sine",
    "cos": "cosine",
    "−sin": "negative sine",
    "−cos": "negative cosine",
    "+cos": "plus cosine",
    "cos′": "cosine prime",
    "cos″": "cosine double prime",
    "sin″": "sine double prime",
    "−(sin′)": "negative sine prime",
    "sin′ = cos": "sine prime equals cosine",
    "cos′ = −sin": "cosine prime equals negative sine",
    "cos′ = sin": "cosine prime equals sine",
    "sin′ = −cos": "sine prime equals negative cosine",
    "cos″ = −cos": "cosine double prime equals negative cosine",
    "sin″ = −sin": "sine double prime equals negative sine",
    "cos″ = (−sin)′ = −cos": "cosine double prime equals the rate of negative sine, which is negative cosine",
    "sin″ = (cos)′ = −sin": "sine double prime equals the rate of cosine, which is negative sine",
    "sin″ = (sin′)′ = (cos)′ = −sin": "sine double prime equals the rate of sine prime, which is the rate of cosine, which is negative sine",
    "sin′ t = cos t": "sine prime of t equals cosine of t",
    "cos′ t = −sin t": "cosine prime of t equals negative sine of t",
    "cos″ t = −cos t": "cosine double prime of t equals negative cosine of t",
    "sin″ t = −sin t": "sine double prime of t equals negative sine of t",
    "sin″ 0 = −sin 0 = 0": "sine double prime of 0 equals negative sine of 0, which is 0",
    "cos′ 0 = 1": "cosine prime of 0 equals 1",
    "cos′ 0 = 0": "cosine prime of 0 equals 0",
    "cos′ 0 ≈ −0.459698": "cosine prime of 0 is approximately negative 0.459698",
    "cos′ 0 = −1": "cosine prime of 0 equals negative 1",
    "sin′ 1": "sine prime of 1",
    "sin′ 1 = cos 1": "sine prime of 1 equals cosine of 1",
    "y″(0)": "y double prime of 0",
    "y″(0) = −y(0)": "y double prime of 0 equals negative y of 0",
    "sin′ t = cos t       cos′ t = −sin t": "sine prime of t equals cosine of t, and cosine prime of t equals negative sine of t",
    "cos″ t = −cos t      sin″ t = −sin t": "cosine double prime of t equals negative cosine of t, and sine double prime of t equals negative sine of t",
    "cos″ t = −(sin t)′ = −cos t": "cosine double prime of t equals the rate of negative sine of t, which is negative cosine of t",
    "x² + v² = cos² t + sin² t = 1": "x squared plus v squared equals cosine squared of t plus sine squared of t, which is 1",
    "(e^(rt))′ = r·e^(rt)": "the quantity e to the power r t, prime, equals r times e to the power r t",
    "(t·e^(rt))′ = (1 + r·t)·e^(rt)": "the quantity t times e to the power r t, prime, equals the quantity 1 plus r times t, times e to the power r t",
    "(t·e^(rt))″ = (2r + r²·t)·e^(rt)": "the quantity t times e to the power r t, double prime, equals the quantity 2 r plus r squared times t, times e to the power r t",
    "(C·e^(−2t))′ = −2·C·e^(−2t)": "the quantity C times e to the power negative 2 t, prime, equals negative 2 times C times e to the power negative 2 t",
    "(C·y₁ + D·y₂)″ = C·y₁″ + D·y₂″": "the quantity C times y sub 1 plus D times y sub 2, double prime, equals C times y sub 1 double prime plus D times y sub 2 double prime",
    "(C·y₁ + D·y₂)″ + (C·y₁ + D·y₂) = C·(y₁″ + y₁) + D·(y₂″ + y₂) = C·0 + D·0 = 0": "the quantity C times y sub 1 plus D times y sub 2, double prime, plus the quantity C times y sub 1 plus D times y sub 2, equals C times the quantity y sub 1 double prime plus y sub 1, plus D times the quantity y sub 2 double prime plus y sub 2, which is C times 0 plus D times 0, which is 0",
    "[(a·r² + b·r + c)·t + (2a·r + b)]·e^(rt)": "the quantity, the quantity A times r squared plus b times r plus c, times t, plus the quantity 2 A times r plus b, all times e to the power r t",
    "y″ + 4y′ + 4y = [(4t − 4) + 4(1 − 2t) + 4t]·e^(−2t) = 0": "y double prime plus 4 y prime plus 4 y equals the quantity 4 t minus 4, plus 4 times the quantity 1 minus 2 t, plus 4 t, all times e to the power negative 2 t, which is 0",
    "y₁(0), y₂(0)": "y sub 1 of 0, y sub 2 of 0",
    "y₁(0)·y₂′(0) − y₁′(0)·y₂(0)": "y sub 1 of 0 times y sub 2 prime of 0, minus y sub 1 prime of 0 times y sub 2 of 0",
    "W(t) = y₁(t)·y₂′(t) − y₁′(t)·y₂(t)": "W of t equals y sub 1 of t times y sub 2 prime of t, minus y sub 1 prime of t times y sub 2 of t",
    "y₁(0) = 1": "y sub 1 of 0 equals 1",
    "y₂(0) = 2": "y sub 2 of 0 equals 2",
    "C₁·y₁(0) + C₂·y₂(0) = y(0)": "C sub 1 times y sub 1 of 0, plus C sub 2 times y sub 2 of 0, equals y of 0",
    "y₂(0)": "y sub 2 of 0",
    "W(0)·C₁ = y₂′(0)·y(0) − y₂(0)·y′(0)": "W of 0 times C sub 1 equals y sub 2 prime of 0 times y of 0, minus y sub 2 of 0 times y prime of 0",
    "W(0)·C₂ = y₁(0)·y′(0) − y₁′(0)·y(0)": "W of 0 times C sub 2 equals y sub 1 of 0 times y prime of 0, minus y sub 1 prime of 0 times y of 0",
}
