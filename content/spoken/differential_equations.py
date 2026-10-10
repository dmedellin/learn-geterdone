"""Spoken forms for math runs whose notation is ambiguous to read-out.

Keyed by the exact run text; see content/AGENTS.md, "Write math a voice can read".

Most entries put a prime on a bracket, `(f·g)′`. The rules read `(…)²` as "the
quantity …, squared" but `(…)′` as "… prime", so `(f·g)′` comes out "f times g
prime", which a listener hears as f·(g′); each such run is spoken with "the
derivative of" before the bracket. Where the prose could say "the derivative
of" in words instead, it was rewritten and needs no entry.

The rest, by course:

* Accumulation and the Integral: the differential `dt` named on its own, read
  "d t" as the rules already read it inside an integral.
* Differential Equations and Euler's Method: `1/h` (read "1 per h" by the
  rules), the error `|y_N − y(T)|`, and rounded figures in scientific form
  (read "e 23").
* Separable Equations, Growth and Decay: the lab's crossing-step tile strings
  as the prose quotes them; the pause after the step number is what makes the
  time audible as a time.
* Equilibria, Stability and Phase Lines: sign patterns read off a phase line,
  which the rules read with a lone "−" as "negative"; a sign pattern is minus
  and plus wherever it appears.
* Second-Order Linear Equations: sine and cosine named without an argument,
  which the rules read as the abbreviations "sin" and "cos" (a bare function
  name has one meaning wherever it appears, so the readings are safe to
  share), and subscripted functions of 0 and t in the Wronskian lesson.
* Oscillators, Damping and Resonance needs none: the runs that read wrongly
  were rewritten to the conventions of docs/differential-equations/PLAN.md
  section F instead (`cos φ` became `cos(φ)`, and the lowercase `a`, `b` that
  sound like the amplitude `A` became other letters).
* Laplace Transforms: a number over `s` -- `1/s`, `6/s³` -- is read as the
  unit "per second", because System Design writes `req/s`; here `s` is the
  transform variable, and the one bare `1/s` elsewhere in the library (System
  Design's sampling fraction) also means "1 over s", so these readings correct
  that page as well. `e^(at)` and `e^(−st)` are read with "at" and "st" as
  words; `∫₀^∞` has no superscript infinity to write, so the caret is read "to
  the power infinity"; and `ℒ[f](s)`, the transform evaluated at `s`, is read
  "f s".

Every key is a complete run, never a lone symbol or a tuple, and every reading
is the literal one, so no other Subject writing the same run is misread.
"""

SPOKEN = {
    # Rates of Change and the Derivative
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
    "(bᵗ)′ = bᵗ·(a constant); e makes it 1": "the derivative of b to the power t equals b to the power t times a constant, and e makes it 1",

    # Accumulation and the Integral
    "dt": "d t",
    "(c·F + d·G)′ = c·f + d·g": "the derivative of c times F plus d times G equals c times f plus d times g",
    "(F·G)′": "the derivative of F times G",
    "(t³/3)′ = 3t²/3 = t²": "the derivative of t cubed over 3 equals 3 t squared over 3, which is t squared",

    # Differential Equations and Euler's Method
    "E(h) = |y_N − y(T)|,  N = (T − t₀)/h": "E of h equals the absolute value of y sub N minus y of T, and N equals the quantity T minus t sub 0, over h",
    "E(h) = |y_N − y(T)|": "E of h equals the absolute value of y sub N minus y of T",
    "|y_N − y(T)|": "the absolute value of y sub N minus y of T",
    "1/h": "1 over h",
    "N = 1/h": "N equals 1 over h",
    "h²·(1/h) = h": "h squared times the quantity 1 over h, equals h",
    "(1/h)·h² = h": "the quantity 1 over h, times h squared equals h",
    "≈ 6.77729e23": "is approximately 6.77729 times 10 to the power 23",

    # Separable Equations, Growth and Decay
    "step 3 (t = 3)": "step 3, at t equals 3",
    "step 6 (t = 3/2)": "step 6, at t equals 3 over 2",
    "step 8 (t = 8)": "step 8, at t equals 8",
    "step 58 (t = 11600)": "step 58, at t equals 11600",

    # Equilibria, Stability and Phase Lines
    "−, +, −, +": "minus, plus, minus, plus",
    "+, +, −": "plus, plus, minus",

    # First-Order Linear Equations
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

    # Second-Order Linear Equations
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
    "(e^(rt))′ = r·e^(rt)": "the derivative of e to the power r t equals r times e to the power r t",
    "(t·e^(rt))′ = (1 + r·t)·e^(rt)": "the derivative of t times e to the power r t equals the quantity 1 plus r times t, times e to the power r t",
    "(t·e^(rt))″ = (2r + r²·t)·e^(rt)": "the second derivative of t times e to the power r t, equals the quantity 2 r plus r squared times t, times e to the power r t",
    "(C·e^(−2t))′ = −2·C·e^(−2t)": "the derivative of C times e to the power negative 2 t equals negative 2 times C times e to the power negative 2 t",
    "(C·y₁ + D·y₂)″ = C·y₁″ + D·y₂″": "the second derivative of C times y sub 1 plus D times y sub 2, equals C times y sub 1 double prime plus D times y sub 2 double prime",
    "(C·y₁ + D·y₂)″ + (C·y₁ + D·y₂) = C·(y₁″ + y₁) + D·(y₂″ + y₂) = C·0 + D·0 = 0": "the second derivative of C times y sub 1 plus D times y sub 2, plus the quantity C times y sub 1 plus D times y sub 2, equals C times the quantity y sub 1 double prime plus y sub 1, plus D times the quantity y sub 2 double prime plus y sub 2, which is C times 0 plus D times 0, which is 0",
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

    # Systems and the Phase Plane
    "(x² + y²)′ = 2x·(2y) + 2y·(−2x) = 0": "the derivative of x squared plus y squared equals 2 x times 2 y plus 2 y times negative 2 x, which is 0",
    "(x·y)′ = x′·y + x·y′": "the derivative of x times y equals x prime times y plus x times y prime",

    # Laplace Transforms
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
