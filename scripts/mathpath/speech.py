"""Math notation -> the words a voice should say.

A browser's speech engine reads `|A ∪ B|` as "vertical line A union B vertical
line" and drops the `!` in `n!` as punctuation, so read-out needs a spoken form
for every math run the content emits. That is computed here, at build time, so
it is deterministic and testable in Python, and an author can override a line
it gets wrong.

Three layers, in order of reach:

1. a symbol table -- one symbol, one phrase, whatever surrounds it;
2. structural rules for what a table cannot say: paired bars, postfix `!`,
   function application, super- and subscript runs, unary minus, the wide gap
   that separates a formula from the prose comment beside it;
3. author overrides, for a reading no rule can infer (`Σ deg(v)` sums over a
   `v` the formula never writes).

`unspoken()` is the coverage check: whatever `say()` could not turn into words.
A run with an unspoken residue would reach the reader as symbol names, or as
silence, so it is a defect to be fixed in the table or by an override.
"""

import html
from pathlib import Path
import re
import unicodedata

# --- layer 1: the symbol table ----------------------------------------------

SYMBOLS = {
    # relations
    "=": "equals", "≠": "is not equal to", "<": "is less than",
    ">": "is greater than", "≤": "is at most",
    "≥": "is at least", "≈": "is approximately",
    "≡": "is congruent to", "∝": "is proportional to", "~": "is approximately",
    "≪": "is much less than", "≫": "is much greater than",
    "≅": "is isomorphic to", "≼": "precedes or equals",
    # arithmetic
    "+": "plus", "±": "plus or minus", "∓": "minus or plus", "×": "times",
    "·": "times", "∗": "times", "÷": "divided by", "√": "the square root of",
    "∛": "the cube root of", "∞": "infinity", "%": "percent", "‰": "per mille",
    "°": "degrees", "∂": "partial", "∇": "del", "∫": "the integral of",
    # logic and sets
    "∀": "for every", "∃": "there exists", "∄": "there is no", "¬": "not",
    "∧": "and", "∨": "or", "⊕": "x or", "⊻": "x or", "⊤": "true", "⊥": "false",
    "∈": "in", "∉": "not in", "∋": "contains", "∅": "the empty set",
    "∪": "union", "∩": "intersect", "⊆": "is a subset of",
    "⊂": "is a proper subset of", "⊇": "is a superset of",
    "⊃": "is a proper superset of", "⊄": "is not a subset of",
    "⊈": "is not a subset of", "∖": "minus", "∁": "the complement of",
    "△": "symmetric difference", "∘": "composed with", "⊢": "proves",
    "⊨": "entails", "∴": "therefore", "∵": "because", "∣": "divides",
    "∤": "does not divide", "∑": "the sum of", "Σ": "the sum of",
    "∏": "the product of", "Π": "the product of",
    # arrows
    "→": "to", "←": "gets", "↦": "maps to", "⇒": "implies", "⟹": "implies",
    "⇐": "is implied by", "⟸": "is implied by", "⇔": "if and only if",
    "⟺": "if and only if", "↔": "if and only if", "⟶": "to", "↑": "up",
    "↓": "down", "↗": "rising to", "↘": "falling to", "⇄": "exchanges with",
    # number sets
    "ℕ": "the natural numbers", "ℤ": "the integers", "ℚ": "the rationals",
    "ℝ": "the reals", "ℂ": "the complex numbers",
    # Greek
    "α": "alpha", "β": "beta", "γ": "gamma", "Γ": "Gamma", "δ": "delta",
    "Δ": "delta", "ε": "epsilon", "ϵ": "epsilon", "ζ": "zeta", "η": "eta",
    "θ": "theta", "Θ": "theta", "ι": "iota", "κ": "kappa", "λ": "lambda",
    "Λ": "Lambda", "μ": "mu", "ν": "nu", "ξ": "xi", "π": "pi", "ρ": "rho",
    "σ": "sigma", "ς": "sigma", "τ": "tau", "υ": "upsilon", "φ": "phi",
    "ϕ": "phi", "Φ": "Phi", "χ": "chi", "ψ": "psi", "Ψ": "Psi", "ω": "omega",
    "Ω": "omega",
    # punctuation that is spoken as a pause or not at all
    "…": "and so on", "⋯": "and so on", "⋮": "and so on",
    "′": "prime", "″": "double prime", "‴": "triple prime", "∠": "angle", "□": "necessarily", "◇": "possibly", "◊": "possibly",
    "≻": "is preferred to", "≽": "is weakly preferred to", "≺": "precedes",
    "∎": "end of proof", "✓": "check", "✗": "fails", "★": "star",
    "—": ",", "–": "to", "“": "", "”": "", "‘": "", "\\": "minus",
    "½": "one half", "⅓": "one third", "⅔": "two thirds", "¼": "one quarter",
    "¾": "three quarters", "µ": "micro", "ℓ": "ell", "‾": "bar", "∼": "is related to",
    "≁": "is not related to", "≢": "is not congruent to", "⊊": "is a proper subset of",
    "⇏": "does not imply", "⟷": "corresponds to", "⟼": "maps to",
    "⊛": "convolved with", "¢": "cents", "£": "pounds", "€": "euros",
    "⌊": "the floor of", "⌋": ",", "⌈": "the ceiling of", "⌉": ",",
    # ℒ[f] is written with square brackets, which say nothing after a symbol
    "ℒ": "the Laplace transform of",
}

# ASCII spellings of the same relations. Longest first, so `<=>` is not read
# as `<=` followed by `>`.
ASCII_OPS = {
    "<--": ",", "-->": ",", "<=>": "if and only if", "<=": "is at most",
    ">=": "is at least", "!=": "is not equal to",
    "==": "equals", "->": "to", "=>": "implies", ":=": "is defined as",
    "<-": "gets", "+=": "plus equals", "**": "to the power",
}

FUNCTIONS = {
    "gcd": "the gcd", "lcm": "the lcm", "deg": "the degree", "log": "log",
    "ln": "the natural log", "lg": "log base 2", "exp": "e to the",
    "max": "the max", "min": "the min", "argmax": "the arg max",
    "argmin": "the arg min", "sin": "sine", "cos": "cosine", "tan": "tangent",
    "mod": "mod", "det": "the determinant", "rank": "the rank",
    "floor": "the floor", "ceil": "the ceiling", "sqrt": "the square root",
    "abs": "the absolute value", "Var": "the variance", "Cov": "the covariance",
    "Pr": "the probability", "tr": "the trace",
}

# Words that are not a product of variables even beside an operator.
UNITS = {
    "ms", "us", "ns", "s", "sec", "min", "h", "hr", "hrs", "day", "days",
    "year", "years", "KB", "MB", "GB", "TB", "PB", "kB", "Mb", "Gb", "ops",
    "req", "rps", "qps", "TPS", "QPS", "RPS", "IOPS", "B", "bits", "bytes",
    "per", "of", "or", "and", "is", "if", "at", "to", "on", "in",
    "for", "not", "the", "mod", "max", "min", "log", "ln", "lg",
}

UNIT_SAY = {"ms": "milliseconds", "us": "microseconds", "ns": "nanoseconds",
            "KB": "kilobytes", "MB": "megabytes", "GB": "gigabytes",
            "TB": "terabytes", "s": "seconds"}

SUPER = dict(zip("⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿⁱᵀᴺᵏʲˣᵐᵃᵇᶜᵈᵉᵗʳᵖ˟ʰˢᴸ",
                 "0123456789+−=()niTNkjxmabcdetrp*hsL"))
SUB = dict(zip("₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₐₑₒₓₕₖₗₘₙₚₛₜᵢⱼᵤᵥᵣ",
               "0123456789+−=()aeoxhklmnpstijuvr"))
SUB["ᵦ"] = "β"

COMBINING = {"̄": "bar", "̅": "bar", "̂": "hat",
             "̃": "tilde", "̇": "dot", "̈": "double dot",
             "⃗": "vector"}

# Box drawing and block elements are the ruled lines of a hand-set table.
_SILENT = re.compile(r"[─-▟]")

_TOKEN = re.compile(
    r"(?P<gap> {2,}|\t+)"
    r"|(?P<ws> )"
    r"|(?P<num>\d{1,3}(?: \d{3})+(?:\.\d+)?(?!\d)|\d+(?:\.\d+)?)"
    r"|(?P<word>[A-Za-z]+(?:'[a-z]+)?)"
    r"|(?P<sup>[%s]+)"
    r"|(?P<sub>[%s]+)"
    r"|(?P<ascii><--|-->|<=>|<=|>=|!=|==|->|=>|:=|<-|\+=|\*\*)"
    r"|(?P<other>.)" % (re.escape("".join(SUPER)), re.escape("".join(SUB))),
    re.S,
)

_OPERATORS = set("=+−-·×/^<>≤≥≠≈≡(),[]{}") | set(ASCII_OPS)
_ARITH = set("=+−-·×/^<>≤≥≠≈≡±") | set(ASCII_OPS)

# Short English words that sit beside an operator in prose comments
# (`latency cap ≈ 14 s`). They are split into letters only when the run is
# operator-bound on both sides, as `by` is in `ax + by`.
COMMON_WORDS = set("""
a an and are as at be but by can cap day do each end for get go has hi how if
in is it its key log low max min new no nor not now of off old on one or our
out own per put row run set so ten the top two up use was way who why yes yet
all any few her him his lot may met one sum six who add big bit cut due far
fit hit let lo mid odd pay raw red sat tie try via win won
""".split())

# What survives in a spoken string. Anything else is unspoken residue.
_SPOKEN = re.compile(r"[A-Za-z0-9 ,.'$?\-£€]")


def _latin(c):
    """An accented Latin letter (Bézout, Erdős) is a word a voice can say."""
    return c.isalpha() and unicodedata.name(c, "").startswith("LATIN")


def _tokens(text):
    out = []
    for m in _TOKEN.finditer(text):
        kind = m.lastgroup
        out.append((kind, m.group()))
    return out


def _sig(tokens, i, step):
    """The nearest non-space token from i in direction step, or (None, None)."""
    j = i + step
    while 0 <= j < len(tokens):
        if tokens[j][0] not in ("ws", "gap"):
            return tokens[j]
        j += step
    return (None, None)


def _pair_bars(tokens):
    """Index of every '|' -> 'open', 'close' or 'sep'.

    A bar with space on both sides separates (`P(A | B)`, `{x | x > 0}`, the
    rule of an augmented matrix). Bars touching their contents pair up, left to
    right, as size or absolute value.
    """
    roles, open_at = {}, None
    for i, (kind, text) in enumerate(tokens):
        if text not in ("|", "∣"):
            continue
        spaced_l = i == 0 or tokens[i - 1][0] in ("ws", "gap")
        spaced_r = i == len(tokens) - 1 or tokens[i + 1][0] in ("ws", "gap")
        if open_at is None:
            if spaced_r and not spaced_l and i > 0:
                roles[i] = "sep"  # a stray closing bar: say a pause
            elif spaced_l and spaced_r:
                roles[i] = "sep"
            else:
                roles[i], open_at = "open", i
        else:
            roles[i], roles[open_at] = "close", roles[open_at]
            open_at = None
    if open_at is not None:
        roles[open_at] = "sep"
    return roles


def _bar_phrase(inner):
    """`|E|` is a size, `|x − 3|` an absolute value: decide by the contents."""
    inner = re.sub(r"_\w|[%s]" % "".join(SUB), "", inner)  # h_L is not a set
    if re.search(r"[A-Z∪∩{}∅ℕℤℚℝℂ]", inner) and not re.fullmatch(r"[A-Z]\s*[−+-].*", inner):
        return "the size of"
    return "the absolute value of"


def _script(plain, *, sup):
    if sup:
        if plain == "2":
            return "squared"
        if plain == "3":
            return "cubed"
        if plain == "T":
            return "transpose"
        if plain == "*":
            return "star"
        if plain in ("+", "−"):
            return "plus" if plain == "+" else "minus"
        return "to the power %s" % _say(plain)
    if plain.isalpha():
        return "sub " + " ".join(_say(c) for c in plain)  # c̄ᵢⱼ: c bar sub i j
    return "sub %s" % _say(plain)


def _logic(tokens):
    return any(t in ("¬", "∧", "∨", "⊕", "□", "◇", "◊") for _, t in tokens)


def _arrow(tokens, i):
    """`→` is "implies" in a logic formula, "to" in a function's type, and
    "goes to" elsewhere (`n = 3 → 3`, `p/n → 0`)."""
    texts = [t for _, t in tokens]
    if _logic(tokens):
        return "implies"
    if ":" in texts[:i]:
        return "to"
    _, before = _sig(tokens, i, -1)
    if before in ("ℕ", "ℤ", "ℚ", "ℝ", "ℂ") or ((before or "").isupper() and before not in GREEK):
        return "to"
    return "goes to"


def _script_arg(tokens, j):
    """The text of a `_` or `^` argument starting at j: a {group} or one token."""
    if j < len(tokens) and tokens[j][1] == "{":
        depth, k = 0, j
        while k < len(tokens):
            depth += {"{": 1, "}": -1}.get(tokens[k][1], 0)
            if depth == 0:
                break
            k += 1
        return "".join(t for _, t in tokens[j + 1:k]), k + 1
    if j < len(tokens):
        return tokens[j][1], j + 1
    return "", j


def _one_operation(tokens, i, close):
    """A single-argument call whose argument holds an operation at its top level."""
    depth, found = 0, False
    for _, t in tokens[i + 1:close]:
        if t in "([{":
            depth += 1
        elif t in ")]}":
            depth -= 1
        elif depth == 0 and t == ",":
            return False
        elif depth == 0 and t in ("+", "−", "-", "/", "·", "×", "±"):
            found = True
    return found


def _match(tokens):
    """Index of each bracket -> index of its partner."""
    pairs, stack = {}, []
    for i, (_, t) in enumerate(tokens):
        if t in "({":
            stack.append(i)
        elif t in ")}" and stack:
            j = stack.pop()
            pairs[i], pairs[j] = j, i
    return pairs


def _is_quantity(tokens, i, close):
    """Does a bracketed group need saying as one unit?

    `√(b² − 4ac)` and `1/(32/640 + 19/640)` read flat leave the listener no
    way to hear where the root or the denominator ends. The group is announced
    as "the quantity" and closed with a pause when it is the operand of a root,
    a fraction or a power and holds an operation of its own.
    """
    inner = tokens[i + 1:close]
    _, before = _sig(tokens, i, -1)
    if before in ("√", "∛") and len([k for k, _ in inner if k != "ws"]) > 1:
        return True  # √(2KDh)/2: the root must be heard to end
    if not any(t in ("+", "−", "-", "/", "·", "×", "±", "∧", "∨", "⊕", "∪", "∩", "→")
               for _, t in inner):
        return False
    _, before = _sig(tokens, i, -1)
    _, after = _sig(tokens, close, +1)
    after_kind = tokens[close + 1][0] if close + 1 < len(tokens) else None
    touching = i > 0 and tokens[i - 1][0] in ("num", "word") or (i > 0 and tokens[i - 1][1] in ")!")
    logic = ("∧", "∨", "⊕", "→", "⟹", "⇒", "⟺", "↔")
    return (before in ("/", "^", "√", "∛", "÷", "−", "-", "·", "×", "¬") + logic
            or after in ("/", "^", "÷", "!") + logic
            or after in ("×", "·", "*", "(") or after_kind in ("sup", "word", "num")
            or touching)


SINGLE_LETTER_PRODUCTS = set("abcijkmnxyz")
# Words after which a relation is prose: "some box has ≥ 2" is "has at least 2".
_PROSE_VERBS = {"has", "have", "holds", "hold", "needs", "need", "takes", "take", "costs",
                "cost", "contains", "contain", "gets", "get", "keeps", "keep", "uses", "use",
                "least", "most", "only", "costs", "waits", "wait", "sees", "see"}
GREEK = set("αβγδεζηθικλμνξπρστυφχψωΓΔΘΛΞΠΣΦΨΩϕϵ")
# Symbols that end a value: a minus after one subtracts (`⌈n/k⌉ − 1`, `λ − μ`).
_VALUE_END = GREEK | set("⌋⌉∞∅ℕℤℚℝℂ′″‴½⅓⅔¼¾ℓ…")


def _bound(tokens, i, step):
    """The operator beside token i, or None at a gap or the end of the run."""
    j = i + step
    while 0 <= j < len(tokens) and tokens[j][0] == "ws":
        j += step
    if not 0 <= j < len(tokens) or tokens[j][0] == "gap":
        return None
    return tokens[j][1]


_TIME_OPS = ("+", "−", "-", "/", "·", "×", "*", "^")


def _time_arg(letter, inner):
    """Is a bracket's content (tokens, spaces included) the argument of a
    function of time or of a number: `t`, `tₙ`, `t + h`, `0`, `1/2`, `−1`?

    `y(t)` and `y(0)` are a solution evaluated, not y times t: `y` is in
    SINGLE_LETTER_PRODUCTS because `y(y − 2)` is a product, and the calling
    letter inside the bracket is exactly what keeps that reading.
    """
    toks = [(k, t) for k, t in inner if k not in ("ws", "gap")]
    if not toks:
        return False
    if toks[0] == ("word", "t"):
        if any(k == "word" and t == letter for k, t in toks):
            return False
        rest = toks[1:]
        if rest and rest[0][0] == "sub":
            rest = rest[1:]
        return not rest or (rest[0][1] in _TIME_OPS and len(rest) > 1)
    return _numeric_arg(inner)


def _numeric_arg(inner):
    """One number, or a fraction of two, with an optional leading minus: `0`, `−1`, `1/2`."""
    toks = [(k, t) for k, t in inner if k not in ("ws", "gap")]
    if toks and toks[0][1] in ("−", "-"):
        toks = toks[1:]
    kinds = [k for k, _ in toks]
    return kinds == ["num"] or (kinds == ["num", "other", "num"] and toks[1][1] == "/")


def _signed_number(inner):
    """One number with an optional leading minus: `0`, `−1`, never `1/2`.

    `f(−1)` needs no "the quantity" to say where its argument ends, but
    `f(3/2)` does: "f of 3 over 2" is also how f(3)/2 is said.
    """
    toks = [t for k, t in inner if k not in ("ws", "gap")]
    return _numeric_arg(inner) and "/" not in toks


def _time_call(tokens, i):
    """A single letter applied to time or to a number: `y(0)`, `x(t)`, `u(t − c)`."""
    kind, tok = tokens[i]
    if kind != "word" or len(tok) != 1 or i + 1 >= len(tokens) or tokens[i + 1][1] != "(":
        return False
    if i and (tokens[i - 1][1] in ("_", "^") or tokens[i - 1][0] == "num"):
        return False  # w_a(t + p_a) is a subscript; 3x(-2)² is a coefficient times x
    close = _match(tokens).get(i + 1)
    if close is None or not _time_arg(tok, tokens[i + 2:close]):
        return False
    after = tokens[close + 1] if close + 1 < len(tokens) else ("ws", " ")
    if after[0] in ("word", "num") or after[1] == "(":
        return False  # c(9/10)n: a bracket glued to what follows is a factor
    inner = [t for k, t in tokens[i + 2:close] if k not in ("ws", "gap")]
    # c(9/10)²: a fraction or a negative bracketed under a power is a factor too
    return not (after[0] == "sup" and (inner[0] in ("−", "-") or "/" in inner))


def _product(tokens, i, tok):
    """Is a short letter run a product of variables (`ax`, `kE`) or a word?"""
    if i and tokens[i - 1][0] == "num":
        return True  # 4ac
    if i + 1 < len(tokens) and tokens[i + 1][0] == "sup":
        return True  # ax², at²
    before, after = _bound(tokens, i, -1), _bound(tokens, i, +1)
    beside = before in _ARITH or after in _ARITH
    if tok in ("th", "st", "nd", "rd") and i and tokens[i - 1][1] in ("-", "−"):
        return False  # the j-th character
    if tok.lower() not in COMMON_WORDS:
        return beside or (before == "(" and after == ")")  # Θ(nk), not P(job ...)
    return beside and before in _ARITH | {None} and after in _ARITH | {None}


def _say(text):
    tokens = _tokens(text)
    bars = _pair_bars(tokens)
    brackets = _match(tokens)
    words = []
    paren_ctx = []  # what opened each bracket: fncall, call, prob, quantity, group
    brace_depth = 0

    def say(w):
        if w:
            words.append(w)

    skip_to = 0
    for i, (kind, tok) in enumerate(tokens):
        if i < skip_to:
            continue
        pk, pt = _sig(tokens, i, -1)
        nk, nt = _sig(tokens, i, +1)
        touching_next = i + 1 < len(tokens) and tokens[i + 1][0] not in ("ws", "gap")
        if kind == "gap":
            say(",")
        elif kind == "ws":
            continue
        elif kind == "num":
            say(tok.replace(" ", ""))
        elif kind == "word":
            call = touching_next and tokens[i + 1][1] == "("
            if re.fullmatch(r"d[a-z]", tok) and tok not in COMMON_WORDS \
                    and any(t == "∫" for _, t in tokens[:i]):
                say("d " + tok[1])  # ∫N(t) dt: the differential, d t
                continue
            if tok == "inf":
                say("infinity")
                continue
            if tok == "x" and pk == "num" and nk == "num" and tokens[i - 1][0] == "ws":
                say("times")  # 3 x 41
                continue
            if tok in ("log", "ln", "lg", "sin", "cos", "tan", "exp") and i and (
                    pk == "num" or (pk == "word" and len(pt) == 1)) and tokens[i - 1][0] != "gap":
                say("times")  # n ln n
            if tok in FUNCTIONS and nt == "over":
                say(FUNCTIONS[tok])
                continue
            if tok in FUNCTIONS and (call or (nk in ("word", "num") and tok not in ("min", "max"))):
                say(FUNCTIONS[tok] + " of" if call or tok not in ("log", "mod") else FUNCTIONS[tok])
                if call:
                    paren_ctx.append("fncall")
                continue
            if tok in ("O", "Θ", "Ω", "o") and call:
                say({"O": "big O", "o": "little o"}.get(tok, tok))
            elif tok == "min" and pk == "num":
                say("minutes")
            elif tok in UNIT_SAY and pk == "num" and (tok != "s" or tokens[i - 1][0] == "ws"):
                say(UNIT_SAY[tok])
            elif (len(tok) in (2, 3) and not tok.isupper() and tok not in UNITS
                  and tok not in FUNCTIONS and pt != "_"
                  and _product(tokens, i, tok)):
                # `ax + by` is a product of letters, not the word "by"
                for ch in tok:
                    say("A" if ch == "a" else ch)
            elif call and tok in SINGLE_LETTER_PRODUCTS and tokens[i + 1][1] == "(" and pt != "_" \
                    and not _time_call(tokens, i):
                # n(n + 1) is a product; f(x) is not
                say("A" if tok == "a" else tok)
                say("times")
                continue
            elif tok == "a" and nk == "word" and len(nt) > 2 and nt.islower():
                say("a")  # the article: "a different quantity"
            elif tok == "a" and (pt in _OPERATORS or nt in _OPERATORS or pk is None):
                say("A")  # the variable, not the article
            else:
                say(tok)
            if call:
                say("of")
                paren_ctx.append("fncall")
        elif kind == "sup" and tok == "⁻¹" and pk == "word":
            say("inverse")  # p⁻¹, e⁻¹
        elif kind == "sup":
            say(_script("".join(SUPER[c] for c in tok), sup=True))
        elif kind == "sub" and pt in ("Σ", "∑", "∏", "Π"):
            words[-1] = words[-1].replace(" of", "")
            say("over %s of" % _say("".join(SUB[c] for c in tok)))
        elif kind == "sub" and pt in ("log", "lg"):
            words[-1] = "log"
            say("base %s" % _say("".join(SUB[c] for c in tok)))
        elif kind == "sub":
            say(_script("".join(SUB[c] for c in tok), sup=False))
        elif kind == "ascii":
            say(ASCII_OPS[tok])
        elif tok in ("|", "∣"):
            role = bars.get(i)
            if role == "open":
                j = next(k for k in range(i + 1, len(tokens)) if bars.get(k) == "close")
                if pk == "num" and tokens[i - 1][0] != "ws":
                    say("times")
                say(_bar_phrase("".join(t for _, t in tokens[i + 1:j])))
            elif role == "close":
                say(",") if nk not in (None,) and nt not in (")", "]", "|") else None
            elif paren_ctx and paren_ctx[-1] == "prob":
                say("given")
            elif brace_depth:
                say("such that")
            elif tok == "∣" or (tokens[i - 1][0] == "ws" and i + 1 < len(tokens)
                                and tokens[i + 1][0] == "ws"
                                and sum(k == "num" for k, _ in tokens[:i]) < 2):
                # 3 | 12 and m | (a − b) divide; 4 −2 6 | 18 is an augmented matrix
                say("divides")  # m | (a − b); a table's rule sits in wide gaps
            else:
                say(",")
        elif tok == "(" and i in brackets and brackets[i] + 1 < len(tokens) \
                and tokens[brackets[i] + 1][1] == "‾":
            say("the complement of the quantity")  # (A ∪ B)‾
            paren_ctx.append("complement")
        elif tok in "({" and i in brackets and (tok == "(" or pt in ("^", "_")) \
                and not (paren_ctx and paren_ctx[-1] == "fncall") \
                and _is_quantity(tokens, i, brackets[i]):
            if i and tokens[i - 1][0] == "sub" or (
                    pk in ("num", "word") and i > 1 and tokens[i - 2][1] == "_"):
                say("of")  # log_3(x + 6), log_b(M·N), Vₜ(i + 1)
            elif pt == ")" or (pk == "num" and tokens[i - 1][0] == "num") or pt == "!":
                say("times")
            say("the quantity")
            paren_ctx.append("quantity")
        elif tok == "{" and pt in ("^", "_"):
            paren_ctx.append("group")
        elif tok == "(":
            if paren_ctx and paren_ctx[-1] == "fncall" and pt and pt not in _OPERATORS:
                paren_ctx[-1] = "prob" if pt in ("P", "Pr", "E") else "call"
                if paren_ctx[-1] == "call" and i in brackets and _one_operation(tokens, i, brackets[i]) \
                        and not (_time_call(tokens, i - 1) and _signed_number(tokens[i + 1:brackets[i]])):
                    say("the quantity")  # f(2x + 6): where the argument ends
                    paren_ctx[-1] = "callq"
            elif i and (tokens[i - 1][0] == "sub" or tokens[i - 1][1] in ("'", "′", "⁻¹")) or (
                    pk in ("num", "word") and i > 1 and tokens[i - 2][1] == "_"):
                say("of")  # log_b(x), v'(S)
                paren_ctx.append("call")
            elif i and tokens[i - 1][1] in (")", "!") or (i and tokens[i - 1][0] == "num"):
                say("times")
                paren_ctx.append("group")
            else:
                paren_ctx.append("group")
        elif tok == ")" and paren_ctx and paren_ctx[-1] == "complement":
            paren_ctx.pop()
            say(",")
            tokens[i + 1] = ("ws", " ")
        elif tok in ")}" and paren_ctx and paren_ctx[-1] in ("quantity", "callq"):
            paren_ctx.pop()
            say(",")
            if i + 1 < len(tokens) and tokens[i + 1][0] in ("num", "word"):
                say("times")  # (n + 1)2ⁿ
        elif tok == "}" and paren_ctx and paren_ctx[-1] == "group" and not brace_depth:
            paren_ctx.pop()
        elif tok == ")":
            if paren_ctx:
                paren_ctx.pop()
            if nt == "(":
                continue
        elif tok == "[":
            if pk == "word" and not (i and tokens[i - 1][0] == "ws"):
                say("of" if pt in ("E", "P", "Var", "Pr") else "at")
        elif tok == "]":
            continue
        elif tok == "{":
            say("the set")
            brace_depth += 1
        elif tok == "}":
            brace_depth = max(0, brace_depth - 1)
            say(",")
        elif tok == ",":
            say("and" if paren_ctx and paren_ctx[-1] in ("call", "prob")
                and words and words[-1] != "and" and _arity(tokens, i) == 2 else ",")
        elif tok == ":" and brace_depth:
            say("such that")  # {x ∈ U : x ∉ A}
        elif tok in (".", ":", ";"):
            say(",")
        elif tok == "!":
            say("factorial" if pk in ("num", "word") or pt in (")", "!") else "")
        elif tok in ("−", "-"):
            if tok == "-" and touching_next and i and tokens[i - 1][0] in ("word", "num") \
                    and tokens[i + 1][0] == "word" and (tokens[i - 1][0] == "word" or len(tokens[i + 1][1]) > 2):
                say("-")  # a hyphenated word: in-order, a 30-character text
            elif (pt is None or pt in _OPERATORS - {")", "]", "}"}
                  or (pt in SYMBOLS and pt not in _VALUE_END)
                  or bars.get(i - 1) == "open"
                  or (i and tokens[i - 1][0] in ("ws", "gap") and touching_next)):
                say("negative")
            else:
                say("minus")
        elif tok == "/":
            if (pk == "num" or tokens[i - 1][0] == "ws" or pt in UNIT_SAY or pt in UNITS) and nk == "word" and nt in ("s", "sec", "day", "year", "request", "requests",
                                        "hour", "h", "min", "ms", "node", "user", "op", "write"):
                say("per")
                if nt == "s":
                    j = next(k for k in range(i + 1, len(tokens)) if tokens[k][0] == "word")
                    tokens[j] = ("word", "second")  # 1200 / s
            else:
                say("over")
        elif tok == "^":
            if nk == "num" and tokens[i + 1][0] == "num":
                say(_script(nt, sup=True))
                tokens[i + 1] = ("ws", " ")
            else:
                say("to the power")
        elif tok == "_" and pt in ("Σ", "∑", "∏", "Π", "max", "min", "argmax", "argmin"):
            lower, j = _script_arg(tokens, i + 1)
            upper = None
            if j < len(tokens) and tokens[j][1] == "^":
                upper, j = _script_arg(tokens, j + 1)
            words[-1] = re.sub(r" of$", "", words[-1])
            if upper is not None:
                say("from %s to %s of" % (_say(lower), _say(upper)))
            else:
                say("over %s of" % _say(lower))
            skip_to = j
        elif tok == "_":
            say("base" if pt in ("log", "lg") else "sub")
        elif tok == "*":
            touching_value = touching_next and tokens[i + 1][0] in ("num", "word")
            say("times" if touching_value or (nk in ("num", "word") and pk in ("num", "word")
                                              and tokens[i - 1][0] == "ws") else "star")
        elif tok in ("'", "’"):
            say("prime")
        elif tok == "&":
            say("and")
        elif tok == "#":
            say("number")
        elif tok == "@":
            say("at")
        elif tok == "$":
            say("$")
        elif tok == "?":
            say("?")
        elif tok == '"':
            continue
        elif tok in COMBINING:
            say(COMBINING[tok])
        elif tok in ("…", "⋯") and words and words[-1] in ("plus", "times", "minus") \
                and nt in ("+", "·", "×", "−"):
            words.pop()  # a + ar + ⋯ + arⁿ: "and so on", not "plus and so on plus"
            say(", and so on,")
        elif tok in ("≥", "≤") and pk == "word" and len(pt) > 2 and pt.lower() in COMMON_WORDS | _PROSE_VERBS:
            say("at least" if tok == "≥" else "at most")  # some box has ≥ 2
        elif tok == "∫" and i + 1 < len(tokens) and tokens[i + 1][0] == "sub":
            # ∫ₐᵇ f(t) dt: the limits are where the integral runs, not a subscript
            lower = _say("".join(SUB[c] for c in tokens[i + 1][1]))
            if i + 2 < len(tokens) and tokens[i + 2][0] == "sup":
                say("the integral from %s to %s of"
                    % (lower, _say("".join(SUPER[c] for c in tokens[i + 2][1]))))
                skip_to = i + 3
            else:
                say("the integral over %s of" % lower)
                skip_to = i + 2
        elif tok in SYMBOLS:
            phrase = SYMBOLS[tok]
            if tok in "⌊⌈√∛" and i and tokens[i - 1][0] == "num":
                say("times")  # 2⌊log₂ m⌋
            if tok in ("→", "⟶"):
                phrase = _arrow(tokens, i)
            elif tok == "≡" and _logic(tokens):
                phrase = "is equivalent to"  # ¬(p ∧ q) ≡ ¬p ∨ ¬q
            elif tok in GREEK and touching_next and tokens[i + 1][1] == "(" and tok not in "ΘΩΣΠ":
                phrase += " of"  # φ(12), χ(G)
                paren_ctx.append("fncall")
            if tok in ("Θ", "Ω") and nt == "(":
                phrase += " of"
                paren_ctx.append("fncall")
            say(phrase)
        elif _SILENT.match(tok):
            continue
        else:
            say(tok)  # unspoken: the coverage check reports it
    spoken = " ".join(words)
    spoken = re.sub(r"\s+,", ",", spoken)
    spoken = re.sub(r"(,\s*)+", ", ", spoken)
    spoken = re.sub(r"\$ (?=\d)", "$", spoken)
    spoken = spoken.replace(" - ", "-")  # in-order: a hyphen is never spoken
    return spoken.strip(" ,")


def _arity(tokens, comma_at):
    """How many arguments the call holding this comma has."""
    depth, commas, i = 0, 0, comma_at
    while i >= 0 and depth >= 0:
        t = tokens[i][1]
        depth += {")": 1, "(": -1}.get(t, 0)
        i -= 1
    depth, i = 0, comma_at
    while i < len(tokens):
        t = tokens[i][1]
        if t == "(":
            depth += 1
        elif t == ")":
            if depth == 0:
                break
            depth -= 1
        elif t == "," and depth == 0:
            commas += 1
        i += 1
    j = comma_at - 1
    depth = 0
    while j >= 0:
        t = tokens[j][1]
        if t == ")":
            depth += 1
        elif t == "(":
            if depth == 0:
                break
            depth -= 1
        elif t == "," and depth == 0:
            commas += 1
        j -= 1
    return commas + 1


_CHOOSE = re.compile(r"\b(?:C|binom)\(\s*([\w+−\- ]+?)\s*,\s*([\w+−\- ]+?)\s*\)")


def say(text, *, override=None):
    """One authored math run (inline span or one display line) -> words."""
    if override is not None:
        return override
    text = html.unescape(re.sub(r"<[^>]+>", "", text))
    # Ā and ŷ are a letter with a bar or hat on it, not a foreign letter
    text = "".join(unicodedata.normalize("NFD", c)
                   if any(m in unicodedata.normalize("NFD", c) for m in "\u0304\u0302")
                   else c for c in text)
    if text.strip() in RELATION_NAMES:
        # "turn each `≤` into a `≥`": a lone symbol is named, not read as a relation
        return RELATION_NAMES[text.strip()]
    text = _CHOOSE.sub(lambda m: "%s choose %s" % (m.group(1), m.group(2)), text)
    return _say(text)


RELATION_NAMES = {"≤": "less-than-or-equal", "≥": "greater-than-or-equal", "<": "less-than",
                  ">": "greater-than", "≠": "not-equal", "=": "equals sign", "<=": "less-than-or-equal",
                  ">=": "greater-than-or-equal"}


def unspoken(spoken):
    """Characters the spoken form still carries that a voice cannot say."""
    return {c for c in spoken if not _SPOKEN.match(c) and not _latin(c)}


def is_rule(line):
    """A display line that is only the ruling of a hand-set table."""
    return not _SILENT.sub("", line).strip(" -=|+")


# --- tables -------------------------------------------------------------------

TABLE = "a table, shown on the page"

_NUMERIC_CELL = re.compile(r"[−\-+]?[\d.,%×$/ ]+[a-zA-Z%×]{0,3}")


def is_table_row(line):
    """A ruled line, or three or more wide-gapped columns most of them numbers.

    Read aloud, a row is a run of figures with no headings to hang them on
    ("2, 800, 24.92, 10"); the reader is pointed at the page instead.
    """
    if is_rule(line):
        return True
    cells = [c for c in re.split(r" {2,}|\t+", line.strip()) if c]
    numeric = sum(bool(_NUMERIC_CELL.fullmatch(c)) for c in cells)
    if re.search(r"[=≈<>≤≥]", line) and numeric < 4:
        return False  # one worked calculation laid out in columns: speedup  100 / 6  =  16.67×
    return len(cells) >= 3 and numeric * 2 >= len(cells)


def say_block(lines, overrides=None):
    """A display block -> one spoken line per authored line.

    Consecutive table rows collapse into a single pointer to the page.
    """
    overrides = overrides or {}
    out = []
    for line in lines:
        if line in overrides:
            out.append(overrides[line])
        elif is_rule(line):
            continue  # a blank spacer or a drawn rule says nothing on its own
        elif is_table_row(line):
            if not out or out[-1] != TABLE:
                out.append(TABLE)
        else:
            spoken = say(line)
            if spoken:
                out.append(spoken)
    return out


# --- what no rule can settle ---------------------------------------------------

_AMBIGUOUS = (
    # x(t) is a function of t; λ(r + 1) is lambda times r + 1. Same shape.
    ("letter-call", re.compile(r"(?<![A-Za-z])[a-zα-ωΓ-Ω](?:[₀-₉ₐ-ₜᵢ-ᵥ]*)\((?!\))")),
    # (n/2) log₂ n -- a group then a function, with the product left unwritten
    ("implicit-product", re.compile(r"\)\s*(?:log|ln|lg|sin|cos|max|min)\b")),
    # (1,1)=5 (1,2)=10 -- a table written along one line
    ("inline-table", re.compile(r"\(\s*\d+\s*,\s*\d+\s*\)\s*=\s*\S+\s+\(\s*\d+\s*,")),
    # 3/2x -- does the x sit under the bar or beside it?
    ("fraction-extent", re.compile(r"\d/\d+[a-zA-Zα-ω(]")),
)

# Single letters the library uses as functions often enough that f(x) is safe,
# and the asymptotic and big-operator letters, which are never a product.
_FUNCTION_LETTERS = set("fghFGHPTCEVLRSWNQUDMOKAB") | set("ΘΩΣΠΦΓΛ")


def _settled_call(text, m):
    letter = m.group()[0]
    if letter in _FUNCTION_LETTERS:
        return True
    # y(0), x(t), u(t − c): a letter applied to time or to a number reads as a
    # call (speech._time_call), so the reading is settled
    if m.group() == letter + "(" and letter.isascii():
        tokens, at = [], None
        for t in _TOKEN.finditer(text):
            if t.start() == m.start():
                at = len(tokens)
            tokens.append((t.lastgroup, t.group()))
        if at is not None and _time_call(tokens, at):
            return True
    # n(n − 1), x(x − 2): the letter multiplies an expression in itself
    rest = text[m.end():]
    return bool(re.match(r"\s*%s\s*[−+\-]" % re.escape(letter), rest))


def ambiguous(run):
    """Reasons a run's reading is a guess. Empty when the rules can be trusted."""
    text = html.unescape(re.sub(r"<[^>]+>", "", run))
    reasons = []
    for name, pattern in _AMBIGUOUS:
        for m in pattern.finditer(text):
            if name == "letter-call" and _settled_call(text, m):
                continue
            reasons.append(name)
            break
    return reasons


def load_overrides(subject):
    """`content/spoken/<subject>.py`'s SPOKEN dict: math run -> what to say.

    It lives outside the subject packages, not in them, so a spoken form can be
    added without touching the content-preservation contract, which inventories
    every module inside a subject package.
    """
    import importlib.util

    path = SPOKEN_DIR / ("%s.py" % subject)
    if not path.exists():
        return {}
    spec = importlib.util.spec_from_file_location("_spoken_%s" % subject, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return dict(module.SPOKEN)


SPOKEN_DIR = Path(__file__).resolve().parents[2] / "content" / "spoken"


def all_overrides():
    """Every subject's spoken forms in one map.

    A run is spoken the same way wherever it appears; tests/test_speech.py
    fails if two subjects ever give one run two readings.
    """
    merged = {}
    for path in sorted(SPOKEN_DIR.glob("*.py")):
        merged.update(load_overrides(path.stem))
    return merged


# --- math written into prose without backticks ----------------------------------

_SYMBOL = re.compile(r"[∀∃∄∈∉∋∪∩⊆⊂⊇⊃⊄⊈∅≤≥≠≈≡≢∝√∛∑∏Σ⟹⟺⇒⇔→←↦ℕℤℚℝℂ∞×·÷±∓∘¬∧∨⌊⌋⌈⌉|^_"
                     r"⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻ⁿⁱᵀᴺᵏʲˣ₀₁₂₃₄₅₆₇₈₉₊₋ₐₑₒₓₖₗₘₙₚₛₜᵢⱼ"
                     r"αβγδεζηθκλμνξπρστφχψωΓΔΘΛΞΠΦΨΩ]|&(?:le|ge|ne|lt|gt);")
_OPERATOR = re.compile(r"[=<>+−\-/*%(),.:;!]+|&(?:le|ge|ne|lt|gt);")

# Sounds written into prose. A pronunciation spelling such as <dfn>tə</dfn> is
# not math, but a voice reads it letter by letter all the same, so it is an
# island too, and its words come from the Subject's spoken forms (a test
# fails while one has none). So is a stress pattern such as s.S. (a dot for
# a light part, S for the strongest), which a voice would read as initials.
_IPA = re.compile(r"[əðʃʒŋɪʊæɑɒɔɜʌːˈˌ]")  # not θ: it is also a math symbol
_STRESS = re.compile(r"(?=.*S)(?=.*\.(?!$))[sS.]{2,6}$")  # a dot before the end: s.S, not S.


def _seed(token):
    """Does a prose token start an island: a math symbol, a sound, a stress mark?"""
    bare = token.strip(",;:!?\u201c\u201d\"'()")
    return bool(_SYMBOL.search(token) or _IPA.search(bare) or _STRESS.match(bare))
_ISLAND_TOKEN = re.compile(r"\S+")


def islands(text):
    """Spans of plain prose that are math written without backticks.

    "compare |r| with 1 before any formula" holds one, `|r|`; "Finish when
    |r| < 1 is a question about rⁿ" holds two. An island is a run of
    space-separated tokens around at least one that carries a math symbol,
    grown over operators, numbers and short variable names, and trimmed of the
    English words at its edges, which the voice reads as they are.
    """
    # Typographic entities (&ldquo; &mdash;) are prose; blank them to the same
    # width so every offset still points into the original text.
    masked = re.sub(r"&(?!(?:le|ge|ne|lt|gt);)#?\w+;", lambda m: " " * len(m.group()), text)
    tokens = [(m.start(), m.end(), m.group()) for m in _ISLAND_TOKEN.finditer(masked)]
    text = masked

    def mathy(tok):
        if re.fullmatch(r"&(?:le|ge|ne|lt|gt);", tok):
            return True
        bare = tok.strip(".,;:!?“”\"'")
        if not bare:
            return False
        if _SYMBOL.search(bare) or _OPERATOR.fullmatch(bare):
            return True
        return bool(re.fullmatch(r"[A-Za-z0-9]{1,3}|\d[\d.]*", bare)) and bare.lower() not in COMMON_WORDS

    out, i, floor = [], 0, 0
    while i < len(tokens):
        if not _seed(tokens[i][2]):
            i += 1
            continue
        lo = hi = i
        grows = bool(_SYMBOL.search(tokens[i][2]))  # a sound or a stress mark stands alone
        while grows and lo > floor and mathy(tokens[lo - 1][2]):
            lo -= 1
        while grows and hi + 1 < len(tokens) and mathy(tokens[hi + 1][2]):
            hi += 1
        start, end = tokens[lo][0], tokens[hi][1]
        # sentence punctuation at the island's edge is prose, not math
        while end > start and text[end - 1] in ".,;:!?”\"":
            end -= 1
        while start < end and text[start] in "“\"(":
            if text[start] == "(" and ")" in text[start:end]:
                break
            start += 1
        if end > start:
            out.append((start, end))
        i = floor = hi + 1
    return out
