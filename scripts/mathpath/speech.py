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
import re
import unicodedata

# --- layer 1: the symbol table ----------------------------------------------

SYMBOLS = {
    # relations
    "=": "equals", "≠": "is not equal to", "<": "is less than",
    ">": "is greater than", "≤": "is less than or equal to",
    "≥": "is greater than or equal to", "≈": "is approximately",
    "≡": "is congruent to", "∝": "is proportional to", "~": "is approximately",
    "≪": "is much less than", "≫": "is much greater than",
    "≅": "is isomorphic to", "≺": "precedes", "≼": "precedes or equals",
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
    "′": "prime", "″": "double prime", "∠": "angle", "□": "end of proof",
    "∎": "end of proof", "✓": "check", "✗": "fails", "★": "star",
    "—": ",", "–": "to", "“": "", "”": "", "‘": "", "\\": "minus",
    "½": "one half", "⅓": "one third", "⅔": "two thirds", "¼": "one quarter",
    "¾": "three quarters", "µ": "micro", "ℓ": "ell", "‾": "bar", "∼": "is related to",
    "≁": "is not related to", "≢": "is not congruent to", "⊊": "is a proper subset of",
    "⇏": "does not imply", "⟷": "corresponds to", "⟼": "maps to",
    "⊛": "convolved with", "¢": "cents", "£": "pounds", "€": "euros",
    "⌊": "the floor of", "⌋": ",", "⌈": "the ceiling of", "⌉": ",",
}

# ASCII spellings of the same relations. Longest first, so `<=>` is not read
# as `<=` followed by `>`.
ASCII_OPS = {
    "<=>": "if and only if", "<=": "is less than or equal to",
    ">=": "is greater than or equal to", "!=": "is not equal to",
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
    "Pr": "the probability",
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
    r"|(?P<ascii><=>|<=|>=|!=|==|->|=>|:=|<-|\+=|\*\*)"
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
    if re.search(r"[A-Z∪∩{}∅]", inner) and not re.fullmatch(r"[A-Z]\s*[−+-].*", inner):
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
    return any(t in ("¬", "∧", "∨", "⊕") for _, t in tokens)


def _arrow(tokens, i):
    """`→` is "implies" in a logic formula, "to" in a function's type, and
    "goes to" elsewhere (`n = 3 → 3`, `p/n → 0`)."""
    texts = [t for _, t in tokens]
    if _logic(tokens):
        return "implies"
    if ":" in texts[:i]:
        return "to"
    _, before = _sig(tokens, i, -1)
    if before in ("ℕ", "ℤ", "ℚ", "ℝ", "ℂ") or (before or "").isupper():
        return "to"
    return "goes to"


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
GREEK = set("αβγδεζηθικλμνξπρστυφχψωΓΔΘΛΞΠΣΦΨΩϕϵ")


def _bound(tokens, i, step):
    """The operator beside token i, or None at a gap or the end of the run."""
    j = i + step
    while 0 <= j < len(tokens) and tokens[j][0] == "ws":
        j += step
    if not 0 <= j < len(tokens) or tokens[j][0] == "gap":
        return None
    return tokens[j][1]


def _product(tokens, i, tok):
    """Is a short letter run a product of variables (`ax`, `kE`) or a word?"""
    if i and tokens[i - 1][0] == "num":
        return True  # 4ac
    before, after = _bound(tokens, i, -1), _bound(tokens, i, +1)
    beside = before in _ARITH or after in _ARITH
    if tok.lower() not in COMMON_WORDS:
        return beside or before == "(" or after == ")"  # Θ(nk)
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

    for i, (kind, tok) in enumerate(tokens):
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
            elif call and tok in SINGLE_LETTER_PRODUCTS and tokens[i + 1][1] == "(":
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
                                and tokens[i + 1][0] == "ws"):
                say("divides")  # m | (a − b); a table's rule sits in wide gaps
            else:
                say(",")
        elif tok in "({" and i in brackets and (tok == "(" or pt in ("^", "_")) \
                and not (paren_ctx and paren_ctx[-1] == "fncall") \
                and _is_quantity(tokens, i, brackets[i]):
            if i and tokens[i - 1][0] == "sub" or (
                    pk == "num" and i > 1 and tokens[i - 2][1] == "_"):
                say("of")  # log_3(x + 6), Vₜ(i + 1)
            elif pt == ")" or (pk == "num" and tokens[i - 1][0] == "num") or pt == "!":
                say("times")
            say("the quantity")
            paren_ctx.append("quantity")
        elif tok == "{" and pt in ("^", "_"):
            paren_ctx.append("group")
        elif tok == "(":
            if paren_ctx and paren_ctx[-1] == "fncall" and pt and pt not in _OPERATORS:
                paren_ctx[-1] = "prob" if pt in ("P", "Pr", "E") else "call"
            elif i and tokens[i - 1][0] == "sub" or (
                    pk == "num" and i > 1 and tokens[i - 2][1] == "_"):
                say("of")
                paren_ctx.append("call")
            elif i and tokens[i - 1][1] in (")", "!") or (i and tokens[i - 1][0] == "num"):
                say("times")
                paren_ctx.append("group")
            else:
                paren_ctx.append("group")
        elif tok in ")}" and paren_ctx and paren_ctx[-1] == "quantity":
            paren_ctx.pop()
            say(",")
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
        elif tok in (".", ":", ";"):
            say(",")
        elif tok == "!":
            say("factorial" if pk in ("num", "word") or pt in (")", "!") else "")
        elif tok in ("−", "-"):
            if tok == "-" and pk == "word" and nk == "word" and touching_next and tokens[i - 1][0] == "word":
                say("-")  # a hyphenated English word
            elif (pt is None or pt in _OPERATORS - {")", "]"} or pt in SYMBOLS
                  or bars.get(i - 1) == "open"
                  or (i and tokens[i - 1][0] in ("ws", "gap") and touching_next)):
                say("negative")
            else:
                say("minus")
        elif tok == "/":
            if (pk == "num" or tokens[i - 1][0] == "ws" or pt in UNIT_SAY) and nk == "word" and nt in ("s", "sec", "day", "year", "request", "requests",
                                        "hour", "h", "min", "ms", "node", "user", "op", "write"):
                say("per")
                if nt == "s":
                    tokens[i + 1] = ("word", "second")
            else:
                say("over")
        elif tok == "^":
            if nk == "num" and tokens[i + 1][0] == "num":
                say(_script(nt, sup=True))
                tokens[i + 1] = ("ws", " ")
            else:
                say("to the power")
        elif tok == "_":
            say("base" if pt in ("log", "lg") else "sub")
        elif tok == "*":
            say("star" if nk in (None,) or nt in _OPERATORS else "times")
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
    text = _CHOOSE.sub(lambda m: "%s choose %s" % (m.group(1), m.group(2)), text)
    return _say(text)


def unspoken(spoken):
    """Characters the spoken form still carries that a voice cannot say."""
    return {c for c in spoken if not _SPOKEN.match(c) and not _latin(c)}


def is_rule(line):
    """A display line that is only the ruling of a hand-set table."""
    return not _SILENT.sub("", line).strip(" -=|+")
