"""Spoken forms for the math runs in First-Order Linear Equations.

Keyed by the exact run text; see content/AGENTS.md, "Write math a voice can read".

Almost every entry is a derivative of a bracketed product or sum, `(mu y)'`,
which the rules read as the product of mu and y prime. A voice has to say "the
derivative of" before the bracket, so each such run is spoken here.
"""

SPOKEN = {
    "fit C last:  y(t₀) = y_p(t₀) + C/μ(t₀)": "fit C last. y of t sub 0 equals y sub p of t sub 0 plus C over mu of t sub 0",
    "1/μ(t₀)": "1 over mu of t sub 0",
    "(C·y)′ + p·(C·y) = C·(y′ + p·y) = C·0 = 0":
        "the derivative of C times y, plus p times C times y, equals C times the quantity y prime plus p times y, equals C times 0, equals 0",
    "check:  y_h = C/μ,  and (e^(−3t))′ = −3·e^(−3t)":
        "check. y sub h equals C over mu, and the derivative of e to the power negative 3 t equals negative 3 times e to the power negative 3 t",
    "(5y)′ − (2 + t²)·(5y) = 5·(y′ − (2 + t²)·y) = 0":
        "the derivative of 5 y, minus the quantity 2 plus t squared, times 5 y, equals 5 times the quantity y prime minus the quantity 2 plus t squared, times y, equals 0",
    "(μ·y)′": "the derivative of mu times y",
    "(μ·y)′ = μ·q": "the derivative of mu times y equals mu times q",
    "(μ·y)′ = μ·y′ + μ′·y = μ·(y′ + p·y)":
        "the derivative of mu times y equals mu times y prime plus mu prime times y, equals mu times the quantity y prime plus p times y",
    "y′ + p·y = q   becomes   (μ·y)′ = μ·q":
        "y prime plus p times y equals q, becomes, the derivative of mu times y equals mu times q",
    "(μ·y)′ = μ·y′ + μ′·y": "the derivative of mu times y equals mu times y prime plus mu prime times y",
    "(tᵃ)′ = a·t^(a − 1) = (a/t)·tᵃ":
        "the derivative of t to the power a equals a times t to the power the quantity a minus 1, equals the quantity a over t, times t to the power a",
    "(μ·y)′ = μ·(y′ + p·y)": "the derivative of mu times y equals mu times the quantity y prime plus p times y",
    "μ′ = (∫p dt)′·e^(∫p dt) = p·μ":
        "mu prime equals the derivative of the integral of p d t, times e to the power the integral of p d t, equals p times mu",
    "(e^(2t)·y)′ = e^(2t)·e^t = e^(3t)":
        "the derivative of e to the power 2 t times y equals e to the power 2 t times e to the power t, equals e to the power 3 t",
    "(t²·y)′ = t⁴": "the derivative of t squared times y equals t to the power 4",
    "left side is (t²·y)′,  so  (t²·y)′ = t⁴":
        "left side is the derivative of t squared times y, so the derivative of t squared times y equals t to the power 4",
    "(t³)′ = 3t² = (3/t)·t³":
        "the derivative of t cubed equals 3 t squared, equals the quantity 3 over t, times t cubed",
    "(t·y)′ = t·1 = t": "the derivative of t times y equals t times 1, equals t",
    "(t²·y)′ = t²": "the derivative of t squared times y equals t squared",
    "(y_p + y_h)′ + p·(y_p + y_h) = (y_p′ + p·y_p) + (y_h′ + p·y_h) = q + 0":
        "the derivative of y sub p plus y sub h, plus p times the quantity y sub p plus y sub h, equals the quantity y sub p prime plus p times y sub p, plus the quantity y sub h prime plus p times y sub h, equals q plus 0",
    "(y − y_p)′ + p·(y − y_p) = (y′ + p·y) − (y_p′ + p·y_p) = q − q = 0":
        "the derivative of y minus y sub p, plus p times the quantity y minus y sub p, equals the quantity y prime plus p times y, minus the quantity y sub p prime plus p times y sub p, equals q minus q, equals 0",
    "(y₁ − y₂)′ + 2·(y₁ − y₂) = 6 − 6 = 0":
        "the derivative of y sub 1 minus y sub 2, plus 2 times the quantity y sub 1 minus y sub 2, equals 6 minus 6, equals 0",
    "y_p(t₀)": "y sub p of t sub 0",
    "2.06115e-9": "2.06115 times 10 to the power negative 9",
}
