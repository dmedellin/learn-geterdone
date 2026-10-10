"""Spoken forms for the math runs of Laplace Transforms that read-out can only guess at.

Keyed by the exact run text; see content/AGENTS.md, "Write math a voice can read".

Four shapes of notation this course cannot avoid read wrongly under the rules:

* a number over `s` -- `1/s`, `6/s³` -- is read as the unit "per second", because
  System Design writes `req/s`; here `s` is the transform variable, and the one
  bare `1/s` elsewhere in the library (System Design's sampling fraction) also
  means "1 over s", so the readings below correct that page as well;
* `e^(at)` and `e^(−st)` are read with "at" and "st" as words, where `e^(kt)` is
  read letter by letter;
* `∫₀^∞` has no superscript infinity to write, so the caret is read "to the
  power infinity"; `∫₀ᵀ` reads correctly and is written that way;
* `ℒ[f](s)`, the transform evaluated at `s`, is read "f s".

Every key is a complete run, never a lone symbol or a tuple, and every reading is
the literal one, so no other Subject writing the same run is misread.
"""

SPOKEN = {
    # the transform of a derivative
    "e^(−sT)·y(T)": "e to the power negative s T, times y of T",
    "e^(−sT)·y(T) − y(0)": "e to the power negative s T, times y of T, minus y of 0",
    "(e^(−st)·y)′ = −s·e^(−st)·y + e^(−st)·y′":
        "the rate of e to the power negative s t, times y, equals negative s times e to the power "
        "negative s t, times y, plus e to the power negative s t, times y prime",
    # the defining integral and the first entries
    "ℒ[f](s) = ∫₀^∞ e^(−st)·f(t) dt":
        "the Laplace transform of f, as a function of s, equals the integral from 0 to infinity of "
        "e to the power negative s t, times f of t, d t",
    "ℒ[e^(2t)](s) = ∫₀^∞ e^(−st)·e^(2t) dt":
        "the Laplace transform of e to the power 2 t, as a function of s, equals the integral from 0 "
        "to infinity of e to the power negative s t, times e to the power 2 t, d t",
    "= ∫₀^∞ e^(−(s − 2)t) dt":
        "equals the integral from 0 to infinity of e to the power negative the quantity s minus 2, "
        "times t, d t",
    "∫₀ᵀ e^(−st) dt = (1 − e^(−sT))/s":
        "the integral from 0 to T of e to the power negative s t, d t, equals the quantity 1 minus "
        "e to the power negative s T, over s",
    "e^(−st)": "e to the power negative s t",
    "−e^(−st)/s": "negative e to the power negative s t, over s",
    "t·e^(−st)": "t times e to the power negative s t",
    "e^(at)": "e to the power A t",
    "t·e^(at)": "t times e to the power A t",
    "e^(−st)·e^(at)": "e to the power negative s t, times e to the power A t",
    "e^(−st)·e^(at) = e^(−(s − a)t)":
        "e to the power negative s t, times e to the power A t, equals e to the power negative the "
        "quantity s minus A, times t",
    "e^(−st)·e^(2t) = e^(−(s − 2)t)":
        "e to the power negative s t, times e to the power 2 t, equals e to the power negative the "
        "quantity s minus 2, times t",
    "e^(−st)·(c·f + d·g) = c·e^(−st)·f + d·e^(−st)·g":
        "e to the power negative s t, times the quantity c times f plus d times g, equals c times "
        "e to the power negative s t, times f, plus d times e to the power negative s t, times g",
    "e^(−st) = e^(−cs)·e^(−sτ)":
        "e to the power negative s t, equals e to the power negative c s, times e to the power "
        "negative s tau",
    "ℒ[e^(at)]": "the Laplace transform of e to the power A t",
    "ℒ[e^(at)] = 1/(s − a)":
        "the Laplace transform of e to the power A t equals 1 over the quantity s minus A",
    "ℒ[e^(at)] = 1/(s − a),   s > a":
        "the Laplace transform of e to the power A t equals 1 over the quantity s minus A, "
        "for s greater than A",
    "ℒ[t·e^(at)] = 1/(s − a)²":
        "the Laplace transform of t times e to the power A t equals 1 over the quantity s minus A, "
        "squared",
    "1/(s − a)² inverts to t·e^(at)":
        "1 over the quantity s minus A, squared, inverts to t times e to the power A t",
    # a number over s is a fraction in s, not a rate per second
    "1/s": "1 over s",
    "1/s²": "1 over s squared",
    "2/s²": "2 over s squared",
    "2/s³": "2 over s cubed",
    "3/s³": "3 over s cubed",
    "6/s³": "6 over s cubed",
    "3·2/s³": "3 times 2 over s cubed",
    "−2/s": "negative 2 over s",
    "4/s": "4 over s",
    "5/s": "5 over s",
    "6/s": "6 over s",
    "ℒ[1] = 1/s": "the Laplace transform of 1 equals 1 over s",
    "ℒ[1] = 1/s,   s > 0": "the Laplace transform of 1 equals 1 over s, for s greater than 0",
    "ℒ[t] = 1/s²": "the Laplace transform of t equals 1 over s squared",
    "ℒ[t²] = 2/s³": "the Laplace transform of t squared equals 2 over s cubed",
    "ℒ[t²] = 1/s³": "the Laplace transform of t squared equals 1 over s cubed",
    "ℒ[t³] = 6/s⁴": "the Laplace transform of t cubed equals 6 over s to the power 4",
    "ℒ[t²] = 2!/s³ = 2/s³":
        "the Laplace transform of t squared equals 2 factorial over s cubed, equals 2 over s cubed",
    "ℒ[1]·ℒ[1] = 1/s²":
        "the Laplace transform of 1 times the Laplace transform of 1 equals 1 over s squared",
    "(1/s)·(1/s) = 1/s²":
        "the quantity 1 over s, times the quantity 1 over s, equals 1 over s squared",
    "ℒ[t]·ℒ[e^(3t)] = (1/s²)·(1/(s − 3)) = 1/(s²·(s − 3))":
        "the Laplace transform of t times the Laplace transform of e to the power 3 t equals the "
        "quantity 1 over s squared, times the quantity 1 over the quantity s minus 3, equals "
        "1 over the quantity s squared times the quantity s minus 3",
    "3·(2/s³) − 2·(1/(s + 1)) = 6/s³ − 2/(s + 1)":
        "3 times the quantity 2 over s cubed, minus 2 times the quantity 1 over the quantity s "
        "plus 1, equals 6 over s cubed minus 2 over the quantity s plus 1",
    "= 3·(2/s³) − 2·(1/(s + 1))":
        "equals 3 times the quantity 2 over s cubed, minus 2 times the quantity 1 over the "
        "quantity s plus 1",
    "= 6/s³ − 2/(s + 1)": "equals 6 over s cubed minus 2 over the quantity s plus 1",
    "6/s³ − 2/(s + 1)": "6 over s cubed minus 2 over the quantity s plus 1",
    "(−2s³ + 6s + 6)/(s³(s + 1))":
        "the quantity negative 2 s cubed plus 6 s plus 6, over the quantity s cubed times the "
        "quantity s plus 1",
    "s·(2/s³) − 0 = 2/s²":
        "s times the quantity 2 over s cubed, minus 0, equals 2 over s squared",
    "(s + 2)·Y = 0 + 6/s": "the quantity s plus 2, times Y equals 0 plus 6 over s",
    "F = 1/s − 1/(s + 1) − 1/(s + 1)²":
        "F equals 1 over s minus 1 over the quantity s plus 1, minus 1 over the quantity s plus 1, "
        "squared",
    "(s² + 3s + 2)·Y = 1/s": "the quantity s squared plus 3 s plus 2, times Y equals 1 over s",
    "(s² + 3s + 2)·Y = 4/s": "the quantity s squared plus 3 s plus 2, times Y equals 4 over s",
    "1/(s·(s + 1)) = 1/s − 1/(s + 1)":
        "1 over the quantity s times the quantity s plus 1, equals 1 over s minus 1 over the "
        "quantity s plus 1",
    "1/s − 1/(s + 1)": "1 over s minus 1 over the quantity s plus 1",
    "= 2/s − 4/(s + 1) + 2/(s + 2)":
        "equals 2 over s minus 4 over the quantity s plus 1, plus 2 over the quantity s plus 2",
    "Y = 2/s − 4/(s + 1) + 2/(s + 2)":
        "Y equals 2 over s minus 4 over the quantity s plus 1, plus 2 over the quantity s plus 2",
    # a stretch of time
    "1 ≤ t < 3": "t is at least 1 and less than 3",
}
