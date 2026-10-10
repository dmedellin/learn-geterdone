"""Spoken forms for math runs in Rates of Change and the Derivative whose notation is ambiguous to read-out.

Keyed by the exact run text; see content/AGENTS.md, "Write math a voice can read".

Almost every entry is the derivative of a bracketed expression, `(f·g)′`. The
rules read `(…)²` as "the quantity …, squared" but `(…)′` as "… prime", so
`(f·g)′` comes out "f times g prime", which a listener hears as f·(g′). Each
such rule statement is spoken here with "the derivative of" before the bracket,
the convention First-Order Linear Equations' spoken forms already use. Where the
prose could say "the derivative of" in words instead, it was rewritten and needs
no entry.
"""

SPOKEN = {
    # the course home's key, and the power rule in The Derivative as a Function
    "(tⁿ)′ = n·tⁿ⁻¹": "the derivative of t to the power n, equals n times t to the power n minus 1",
    "(c·tⁿ)′ = n·c·tⁿ⁻¹": "the derivative of c times t to the power n, equals n times c times t to the power n minus 1",
    "(p + q)′ = p′ + q′": "the derivative of p plus q equals p prime plus q prime",
    "(c·p)′ = c·p′": "the derivative of c times p equals c times p prime",
    "(t²)′ = 2t": "the derivative of t squared equals 2 t",
    # The Product Rule
    "(f·g)′ = f′·g + f·g′": "the derivative of f times g, equals f prime times g, plus f times g prime",
    "(f·g)′": "the derivative of f times g",
    "(f·g)′ = 2t": "the derivative of f times g equals 2 t",
    "(f·g)′ = 1": "the derivative of f times g equals 1",
    "(5·f)′": "the derivative of 5 times f",
    "(f²)′ = f′·f + f·f′ = 2·f·f′":
        "the derivative of f squared, equals f prime times f, plus f times f prime, equals 2 times f times f prime",
    # The Chain Rule
    "(f(g(t)))′ = f′(g(t))·g′(t)": "the derivative of f of g of t, equals f prime of g of t, times g prime of t",
    "(uⁿ)′ = n·uⁿ⁻¹·u′": "the derivative of u to the power n, equals n times u to the power n minus 1, times u prime",
    "(uⁿ⁺¹)′ = (uⁿ·u)′ = n·uⁿ⁻¹·u′·u + uⁿ·u′ = (n + 1)·uⁿ·u′":
        "the derivative of u to the power n plus 1, equals the derivative of u to the power n times u, "
        "equals n times u to the power n minus 1, times u prime, times u, plus u to the power n times u prime, "
        "equals the quantity n plus 1, times u to the power n, times u prime",
    "product:  3(t² + 1)²·2t = 6t(t² + 1)²": "product, 3 times the quantity t squared plus 1, squared, times 2 t, equals 6 t times the quantity t squared plus 1, squared",
    # The Second Derivative's key: `(p′)′` reads "p prime prime"
    "p″ = (p′)′, the rate of the rate": "p double prime equals the derivative of p prime, the rate of the rate",
    # The Exponential and Its Rate, and the course home's key
    "(eᵗ)′ = eᵗ": "the derivative of e to the power t equals e to the power t",
    "(bᵗ)′ = bᵗ": "the derivative of b to the power t equals b to the power t",
    "(bᵗ)′ = (a constant)·bᵗ": "the derivative of b to the power t equals a constant times b to the power t",
    "(bᵗ)′ = bᵗ·(a constant); e makes it 1": "the derivative of b to the power t equals b to the power t times a constant; e makes it 1",
}
