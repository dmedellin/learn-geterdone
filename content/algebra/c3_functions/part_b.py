"""Course 3, lessons 08-14 - notation, domain, shape, composition, inverse, and inequalities."""

LESSONS = [
    # ---------------------------------------------------------------- 08
    {
        "slug": "function-notation",
        "title": "Function Notation",
        "module": "Functions",
        "one_line": "f(x) is a value, not a product.",
        "summary": (
            "`f(x)` names the output that the function `f` produces from the input "
            "`x`. It is one number, not `f` multiplied by `x`, and once that is "
            "settled the notation distinguishes two different questions: evaluate a "
            "given input, and solve for the inputs that produce a given output."
        ),
        "key": [
            "f(x)      the output of f at x        NOT f times x",
            "f(3)      EVALUATE: put 3 where x is",
            "f(x) = 3  SOLVE:    which inputs give 3",
            "f(a + b)  is not  f(a) + f(b)",
        ],
        "key_label": "Four lines that prevent most of the errors",
        "concepts_intro": (
            "Lesson 7 established that an input has exactly one output. This lesson "
            "gives that output a name, which is what makes every later lesson "
            "writable."
        ),
        "concepts": [
            ("The whole symbol names one number",
             "`f(3)` is a single value. The letter `f` is the name of the rule, the "
             "brackets are not multiplication, and `x` is a slot. Read `f(3)` as "
             "\"f of 3\", never as \"f times 3\", because the second reading makes "
             "`f(a + b) = fa + fb` look like the distributive law."),
            ("Evaluating is substitution, with brackets",
             "To find `f(−2)` for `f(x) = x² − 4x + 5`, write `(−2)² − 4(−2) + 5`. "
             "Every occurrence of `x` becomes `(−2)`, brackets and all. The brackets "
             "are what stop `(−2)²` from collapsing to `−4`."),
            ("Evaluate and solve are opposite questions",
             "`f(3)` hands you an input and asks for the output; there is exactly one "
             "answer. `g(x) = 5` for `g(x) = 3x − 7` hands you an output and asks "
             "which input produced it; course 2's linear method gives `x = 4`. On a "
             "table or graph there may be none, one or several such inputs. Confusing "
             "the two questions is the most common error in this lesson."),
        ],
        "read_title": "Reading and using the notation",
        "read_intro": "What the symbol means, how to substitute safely, and the two questions it can pose.",
        "body": [
            ("def", ("Function notation",
                     "If `f` is a function and `x` is an input in its domain, "
                     "<strong>`f(x)`</strong> denotes the output that `f` assigns to "
                     "`x`. The letter naming the function and the letter naming the "
                     "input are both arbitrary: `f(x) = 2x + 1`, `g(t) = 2t + 1` and "
                     "`h(u) = 2u + 1` are three names for one function.",
                     "The brackets are borrowed from the brackets of multiplication, "
                     "and that is an accident of history, not a hint. Nothing in "
                     "`f(x)` is being multiplied. The notation is roughly three "
                     "hundred years old and predates any convention that would have "
                     "made it unambiguous, so the ambiguity is permanent and the only "
                     "defence is reading the whole symbol as one name.")),
            ("h3", "Evaluating at a number"),
            ("p", "Take `f(x) = x² − 4x + 5`. Substituting means replacing every `x` "
                  "with the input, wrapped in brackets, and only then simplifying."),
            ("math", [
                "f(x) = x^2 - 4x + 5",
                "",
                "f(3)  = (3)^2  - 4(3)  + 5 =  9 - 12 + 5 =  2",
                "f(0)  = (0)^2  - 4(0)  + 5 =  0 -  0 + 5 =  5",
                "f(-2) = (-2)^2 - 4(-2) + 5 =  4 +  8 + 5 = 17",
            ]),
            ("p", "The third line is where brackets earn their place. Without them "
                  "the first term reads `−2²`, which is `−4`, and the second reads "
                  "`−4·2`, which is `−8`; the total comes out `−7` instead of `17`. "
                  "Both slips are silent, because `−7` is a perfectly ordinary "
                  "number and nothing in the working looks wrong."),
            ("h3", "Evaluating at an expression"),
            ("p", "The slot accepts anything, including another expression. The "
                  "procedure does not change: replace every `x` by the whole "
                  "expression in brackets, expand, collect."),
            ("math", [
                "f(a + 1) = (a + 1)^2 - 4(a + 1) + 5",
                "         = a^2 + 2a + 1 - 4a - 4 + 5",
                "         = a^2 - 2a + 2",
                "",
                "check at a = 2:   f(3) = 2        and   2^2 - 2(2) + 2 = 2",
            ]),
            ("p", "Compare that with `f(a) + f(1)`, which is `a² − 4a + 5` plus `2`, "
                  "or `a² − 4a + 7`. The two differ at every value of `a` except "
                  "where `a² − 2a + 2 = a² − 4a + 7`, that is `2a = 5`, so they agree "
                  "only at `a = 5/2`. A function does not distribute over addition, "
                  "and a single accidental agreement is not evidence that it does."),
            ("thm", ("Functions do not distribute",
                     "For a general function `f`, `f(a + b)` and `f(a) + f(b)` are "
                     "different numbers. The error survives because it is correct for "
                     "`f(x) = cx`, the family met first: `c(a + b) = ca + cb` really "
                     "is the distributive law. A constant term is enough to break it. "
                     "For `f(x) = 2x + 1`, `f(1 + 1) = 5` while `f(1) + f(1) = 6`.")),
            ("h3", "The two questions"),
            ("ul", [
                "<strong>Evaluate.</strong> `f(3)` is a command: substitute `3`. The "
                "answer is one number, guaranteed by the definition of a function.",
                "<strong>Solve.</strong> `g(x) = 5` for `g(x) = 3x − 7` is the linear "
                "equation `3x − 7 = 5`, so `3x = 12` and `x = 4`. The answer is an "
                "input, not the displayed output `5`.",
                "<strong>A graph or table may give several inputs or none.</strong> "
                "Solving means collect every input paired with the requested output. "
                "The definition of a function limits outputs per input; it does not "
                "limit how many inputs may share one output.",
            ]),
            ("example", ("Reading values off a graph",
                         "A point `(3, 2)` on the graph of `f` says `f(3) = 2`, "
                         "because the graph is the set of pairs "
                         "`(input, output)`. Finding `f(3)` means reading up from "
                         "`3` on the horizontal axis; solving `f(x) = 2` means "
                         "reading across from `2` on the vertical axis and "
                         "collecting every `x` beneath. One vertical sweep, one "
                         "horizontal sweep, and they can return different numbers "
                         "of answers.")),
        ],
        "lab": ("funcops", {
            "mode": "notation",
            "panel_title": "Substitute before simplifying",
            "panel_intro": "Choose a rule and an input, predict `f(a)`, then reveal "
                           "the bracketed substitution. The panel also computes "
                           "`f(x + 1)` and `f(x) + 1` separately; it does not solve "
                           "equations, so do the linear solve in the faded task yourself.",
        }),
        "steps_title": "Evaluating without losing a sign",
        "steps_intro": "Four moves. The third is the one that goes wrong.",
        "steps": [
            ("Decide which question is being asked",
             "An input inside the brackets means evaluate. An equals sign after the "
             "brackets means solve. Answering the wrong one produces a confident, "
             "irrelevant number."),
            ("Rewrite the rule with the slot empty",
             "For `f(x) = x² − 4x + 5`, write `( )² − 4( ) + 5`. This takes five "
             "seconds and makes it impossible to substitute into some occurrences of "
             "`x` and not others."),
            ("Drop the input into every slot, brackets included",
             "`(−2)²`, not `−2²`. `−4(−2)`, not `−4−2`. When the input is negative or "
             "is itself an expression, the brackets are carrying the arithmetic, not "
             "decorating it."),
            ("Simplify, then check with a number",
             "For a symbolic answer such as `f(a + 1) = a² − 2a + 2`, put `a = 2` in "
             "both the original and the result. If `f(3)` and the new expression "
             "disagree, the expansion is wrong and you have found it in one line."),
        ],
        "worked": {
            "title": "Two functions, four different requests",
            "intro": ["Use `f(x) = x² − 4x + 5` for substitution and "
                      "`g(x) = 3x − 7` for a solve that needs only Course 2."],
            "lines": [
                "1.  f(3)                 (3)^2 - 4(3) + 5                    = 2",
                "",
                "2.  f(-2)                (-2)^2 - 4(-2) + 5 = 4 + 8 + 5      = 17",
                "        careless:        -2^2 - 4*2 + 5     = -4 - 8 + 5     = -7   WRONG",
                "",
                "3.  g(x) = 5             3x - 7 = 5",
                "                         3x = 12                 x = 4",
                "        check:           g(4) = 3(4) - 7 = 5",
                "",
                "4.  f(a + 1)             (a + 1)^2 - 4(a + 1) + 5",
                "                         a^2 + 2a + 1 - 4a - 4 + 5",
                "                                                    = a^2 - 2a + 2",
                "        check a = 2:     f(3) = 2      4 - 4 + 2 = 2           agrees",
            ],
            "after": [
                "Questions 1 and 3 are the pair to keep apart. Both mention `f`, `x` "
                "and a number; one starts with an input and returns its output, while "
                "the other starts with an output and recovers its input.",
                "Question 4 is worth comparing with `f(a) + f(1) = a² − 4a + 7`. The "
                "two expressions agree only at `a = 5/2`, so a spot check at that one "
                "value would wrongly suggest the shortcut works &mdash; which is why "
                "the check above uses `a = 2`.",
                "For a faded pass, let `p(t) = t² + 3t − 1`. The bracketed substitution "
                "for `p(−2)` is supplied as `(−2)² + 3(−2) − 1`; simplify it and "
                "check the sign of each term. Then form `p(a − 1)` by replacing every "
                "slot before expanding. Separately solve `4x + 3 = 19` as the "
                "function equation `q(x) = 19` for `q(x) = 4x + 3`.",
            ],
        },
        "quiz_title": "Notation, evaluated and solved",
        "quiz": [
            {"q": "For `f(x) = x² − 4x + 5`, what is `f(−3)`?",
             "a": ["`26`", "`2`", "`−16`", "`−2`"],
             "c": 0,
             "why": "`(−3)² − 4(−3) + 5 = 9 + 12 + 5 = 26`. `2` changes the "
                    "linear term to `−12`; `−16` leaves the square unbracketed and "
                    "also loses the input's sign in the linear term; `−2` is "
                    "`−f(3)`, which negates the output instead of the input."},
            {"q": "For `g(x) = 5x − 4`, what does `g(x) = 16` give?",
             "a": ["`x = 16`", "`x = 4`", "`x = 12/5`", "`x = 20`"],
             "c": 1,
             "why": "Solving `5x − 4 = 16` gives `5x = 20`, so `x = 4`, and "
                    "`g(4) = 16`. `x = 16` copies the output into the input; `12/5` "
                    "subtracts `4` instead of undoing `−4` by addition; `20` stops "
                    "before the final division."},
            {"q": "For `f(x) = x² − 4x + 5`, which expression equals `f(a − 1)`?",
             "a": ["`a² − 6a + 10`", "`a² − 4a + 4`", "`a² − 6a + 6`", "`a² − 4a + 6`"],
             "c": 0,
             "why": "`(a − 1)² − 4(a − 1) + 5 = a² − 2a + 1 − 4a + 4 + 5`, "
                    "so the result is `a² − 6a + 10`. `a² − 4a + 4` is `f(a) − 1`; "
                    "`a² − 6a + 6` fails to distribute `−4` to the `−1`; and "
                    "`a² − 4a + 6` adds one to the output rather than subtracting one "
                    "from the input."},
        ],
        "mistakes": [
            ("Reading f(x) as f times x",
             "It is the single most productive error in the subject: it makes "
             "`f(a + b) = f(a) + f(b)` look like distribution and `f(2x) = 2f(x)` look "
             "like factoring. Neither holds for a general `f`. The brackets attach a "
             "name to an input; they never multiply."),
            ("Substituting a negative without brackets",
             "`f(−2)` with `f(x) = x²` is `(−2)² = 4`, not `−2² = −4`. The written "
             "form `−2²` means the square is taken first and then negated, so leaving "
             "the brackets out silently changes the question."),
            ("Answering the other question",
             "Asked for `f(3)`, some readers solve `f(x) = 3`; asked to solve "
             "`f(x) = 5`, some evaluate `f(5)`. The giveaway is the shape of the "
             "answer: evaluating returns one number, solving returns a set that may "
             "be empty."),
        ],
        "standard": ("Finish when you can evaluate at a number or an expression "
                     "without losing a bracket, and can tell an evaluation from an "
                     "equation on sight.",
                     "Given `r(x) = x² + 2x − 3` you should evaluate `r(−4)` and form "
                     "`r(a + 2)` from bracketed substitutions, then solve the separate "
                     "linear function equation `s(x) = 11` for `s(x) = 2x − 5`. "
                     "For each answer, say whether it is an output or an input and "
                     "check it in the original rule."),
        "note": "Every lesson from here on is written in this notation, so the habit "
                "of reading `f(x)` as one name rather than two factors is worth "
                "forming now. Lesson 10 asks which inputs the slot is allowed to "
                "accept, which is the first question the notation makes it possible "
                "to state precisely.",
    },

    # ---------------------------------------------------------------- 09
    {
        "slug": "domain-and-range",
        "title": "Domain and Range",
        "module": "Functions",
        "one_line": "What goes in, what comes out, and what is excluded.",
        "summary": (
            "The domain is the set of inputs a function accepts; the range is the "
            "set of outputs it actually produces. Among the formulas available so "
            "far, a zero denominator and an even root of a negative are the two "
            "domain failures; finding a range needs an argument about the outputs."
        ),
        "key": [
            "domain = every input the rule accepts",
            "range  = every output the rule produces",
            "exclude:  denominator = 0     even root of a negative",
            "[a, b] includes the ends    (a, b) excludes them    U joins pieces",
        ],
        "key_label": "The two sets, and the two exclusions used here",
        "concepts_intro": (
            "Lesson 8 said a function must give an output for each input it claims. "
            "This lesson is about stating exactly what it claims."
        ),
        "concepts": [
            ("The domain is part of the function",
             "A function is a rule together with the set it accepts. `f(x) = x²` on "
             "every real number and `f(x) = x²` on `x ≥ 0` are different functions "
             "with the same formula, and lesson 14 depends on the difference. When no "
             "domain is stated, the convention is the largest set of real numbers for "
             "which the formula gives a real value."),
            ("Two checks cover every formula in this lesson",
             "Among the formulas used here, a real input fails for one of two reasons: it makes a "
             "denominator zero, or it puts a negative number under a square root or "
             "another even root. Logarithms add a new condition in course 7; for now, "
             "adding, multiplying, cubing and taking an odd root accept every real number."),
            ("The range is what actually comes out",
             "The domain can be read off the formula by inspection. The range usually "
             "cannot: it needs a graph landmark or an argument about which outputs are "
             "reachable. `f(x) = x²` accepts every real input but produces only "
             "non-negative outputs, while `g(x) = 2x − 3` reaches every real output."),
        ],
        "read_title": "Finding the domain, then the range",
        "read_intro": "Two exclusions to test for, interval notation to write the answer in, and the reason ranges are harder.",
        "body": [
            ("def", ("Domain and range",
                     "The <strong>domain</strong> of a function is the set of inputs "
                     "it is defined on. The <strong>range</strong> is the set of "
                     "outputs it produces: every value `y` for which some `x` in the "
                     "domain has `f(x) = y`. The range is a set of values actually "
                     "attained, not a set of values that look permitted.")),
            ("p", "When a function arrives as a bare formula, the domain is not "
                  "stated and has to be inferred. The convention is the <em>natural "
                  "domain</em>: every real number for which the formula produces a "
                  "real value. This is a convention, chosen because it is the "
                  "largest sensible default, and a problem is free to override it by "
                  "naming a smaller set."),
            ("h3", "The two exclusions"),
            ("ul", [
                "<strong>A zero denominator.</strong> Division by zero is undefined, "
                "so set every denominator equal to zero, solve, and exclude the "
                "solutions. For `(x + 2)/((x − 2)(x − 3))`, the denominator is "
                "already displayed as factors, so the excluded inputs are `2` and `3`. "
                "Producing such a factorisation is course 4 work, not a hidden prerequisite here.",
                "<strong>An even root of a negative.</strong> `√(2x − 7)` needs "
                "`2x − 7 ≥ 0`, so `x ≥ 7/2`. Write the exact fraction, not `3.5`. "
                "Fourth roots, sixth roots and so on behave the same way; cube roots "
                "do not: the cube root of `−8` is `−2`, a perfectly real value.",
            ]),
            ("p", "When both appear, both conditions must hold at once. For "
                  "`√(x + 4)/(x − 1)` the numerator demands `x ≥ −4` and the "
                  "denominator forbids `x = 1`, so the domain is `[−4, 1) ∪ (1, ∞)`. "
                  "Note that `−4` is included: `√0 = 0` is a perfectly good output. "
                  "It is the denominator, not the root, that produces an open end."),
            ("math", [
                "f(x) = (x + 2)/((x - 2)(x - 3))   bottom is already factored",
                "                                  domain: x =/= 2, x =/= 3",
                "",
                "g(x) = sqrt(2x - 7)               2x - 7 >= 0   ->  x >= 7/2",
                "",
                "h(x) = sqrt(x + 4)/(x - 1)        x >= -4  AND  x =/= 1",
                "                                  domain: [-4, 1) U (1, inf)",
                "",
                "k(x) = sqrt(9 - x^2)              9 - x^2 >= 0  ->  -3 <= x <= 3",
            ]),
            ("p", "The last one is worth slowing down for. `9 − x² ≥ 0` is `x² ≤ 9`, "
                  "and the inputs whose square is at most `9` are those between `−3` "
                  "and `3` inclusive. Taking a square root of both sides of `x² ≤ 9` "
                  "and writing `x ≤ 3` loses the whole left half of the answer; this "
                  "is the absolute value inequality from course 2, lesson 12, in a "
                  "new costume."),
            ("h3", "Why the range is harder"),
            ("p", "The domain is a question about the formula: which inputs does it "
                  "choke on. The range is a question about the function's behaviour "
                  "across its whole domain, and there is no equivalent checklist. "
                  "Three tools cover most cases at this level."),
            ("ol", [
                "<strong>Use non-negativity,</strong> for a square or absolute value. "
                "`x² ≥ 0`, with equality at `x = 0`, and every non-negative `y` is "
                "`(√y)²`; the range of `x²` is `[0, ∞)`. Likewise `|x| − 2` has "
                "range `[−2, ∞)`.",
                "<strong>Track the outer operation,</strong> for a root. "
                "`√(9 − x²)` takes the square root of something running from `0` up "
                "to `9`, so the outputs run from `0` to `3`, giving `[0, 3]`.",
                "<strong>Solve for the input,</strong> for a non-horizontal line. "
                "If `y = 2x − 3`, then `x = (y + 3)/2` exists for every real `y`, "
                "so the line reaches every real output.",
            ]),
            ("example", ("An excluded input removes an output, not its own number",
                         "Let `q(x) = 2x + 1` with the stated domain `x ≠ 3`. The "
                         "formula is a non-horizontal line, so each output comes from "
                         "exactly one input. Removing `x = 3` therefore removes the "
                         "point `(3, 7)` and the output `7`. The domain excludes `3`; "
                         "the range excludes `7`. Copying the input restriction into "
                         "the range confuses the two axes.")),
            ("h3", "Writing the answer"),
            ("p", "Interval notation from course 2, lesson 13, is the expected form. "
                  "A square bracket includes the endpoint, a round bracket excludes "
                  "it, and `∞` always takes a round bracket because it is not a "
                  "number that can be attained. Use `∪` to join the pieces when an "
                  "excluded point splits the domain, and list the pieces in "
                  "increasing order."),
            ("p", "One habit is worth building: after writing a domain, test a value "
                  "just inside each end and one value that should be excluded. For "
                  "`[−4, 1) ∪ (1, ∞)` try `x = −4`, which gives `0/(−5) = 0`, and "
                  "`x = 1`, which divides by zero. Two substitutions confirm both "
                  "boundary decisions in about ten seconds."),
        ],
        "lab": ("funcops", {
            "mode": "domain",
            "presets": [
                ("A zero denominator", "1/(x - 2)"),
                ("A square-root endpoint", "sqrt(x - 3)"),
                ("A root and a denominator", "sqrt(x + 4)/(x - 1)"),
                ("A square has no exclusions", "x^2"),
                ("A non-horizontal line reaches every output", "2x - 3"),
            ],
            "panel_title": "Excluded inputs, shown",
            "panel_intro": "Predict the domain before choosing a preset. The lab marks "
                           "the inputs the formula refuses and names the condition; the "
                           "range readout is proved for these simple cases and labels "
                           "itself when a more general formula can only be sampled.",
        }),
        "steps_title": "Finding a domain in four passes",
        "steps_intro": "Scan for each exclusion separately, then combine. Combining first is where answers go missing.",
        "steps": [
            ("List every denominator",
             "Including denominators buried inside a root or a compound fraction. Set "
             "each to zero, solve, and mark those inputs as excluded. This lesson "
             "supplies denominators already factored when there is more than one "
             "zero; course 4 teaches how to produce the factorisation."),
            ("List every even root",
             "Square roots, fourth roots, and any rational exponent with an even "
             "denominator. Each contributes an inequality of the form "
             "\"the inside is at least zero\". Odd roots contribute nothing."),
            ("Solve each condition on its own",
             "Keep the conditions separate while you solve them. `9 − x² ≥ 0` needs "
             "the two-sided answer `−3 ≤ x ≤ 3`, and mixing it with another "
             "condition before it is solved is how one half of it disappears."),
            ("Intersect, then write it in intervals",
             "Every condition must hold at once, so take the overlap, not the union. "
             "The union symbol appears in the written answer only because excluded "
             "points cut the overlap into pieces."),
        ],
        "worked": {
            "title": "Four domains and two ranges",
            "intro": ["The domains first, since they are mechanical. The ranges "
                      "afterwards, since they are not."],
            "lines": [
                "1.  f(x) = (x + 2)/((x - 2)(x - 3))",
                "        (x - 2)(x - 3) = 0   ->  x = 2, x = 3",
                "        domain   (-inf, 2) U (2, 3) U (3, inf)",
                "",
                "2.  g(x) = sqrt(2x - 7)",
                "        2x - 7 >= 0  ->  x >= 7/2",
                "        domain   [7/2, inf)              note 7/2, not 3.5",
                "",
                "3.  h(x) = sqrt(x + 4)/(x - 1)",
                "        x + 4 >= 0  ->  x >= -4          x - 1 =/= 0  ->  x =/= 1",
                "        domain   [-4, 1) U (1, inf)",
                "        check    x = -4:  0/(-5) = 0     defined, so -4 is IN",
                "                 x = 1:   division by 0  excluded",
                "",
                "4.  k(x) = sqrt(9 - x^2)",
                "        9 - x^2 >= 0  ->  x^2 <= 9  ->  -3 <= x <= 3",
                "        domain   [-3, 3]",
                "",
                "ranges",
                "",
                "5.  p(x) = x^2",
                "        x^2 >= 0, and equals 0 at x = 0",
                "        every y >= 0 is reached at x = sqrt(y)",
                "        range    [0, inf)",
                "",
                "6.  r(x) = |x| - 2",
                "        |x| >= 0, and equals 0 at x = 0",
                "        range    [-2, inf)              r(0) = -2",
            ],
            "after": [
                "Line 3 is the one that decides whether the technique has been "
                "understood. Both exclusions are present, they come from different "
                "parts of the expression, and the left end is closed while the "
                "interior point is open. Reading `[−4, 1) ∪ (1, ∞)` back out loud as "
                "\"from `−4` inclusive, everything except `1`\" is a fair test.",
                "Lines 5 and 6 use facts already taught in Course 1: a square and an "
                "absolute value are non-negative. Subtracting `2` changes every output "
                "of `|x|` and therefore changes the range endpoint, not the domain.",
                "For a faded domain, take `s(x) = √(x + 2)/(x − 4)`. The root condition "
                "`x ≥ −2` is supplied. Find the denominator exclusion, intersect the "
                "conditions, write the intervals, and test both `−2` and `4`. Then find "
                "the range of `t(x) = |x + 1| − 3` from its minimum and show an input "
                "that produces two different allowed output values.",
            ],
        },
        "quiz_title": "In, out and excluded",
        "quiz": [
            {"q": "What is the domain of `f(x) = √(x + 2)/(x − 4)`?",
             "a": ["`[−2, ∞)`",
                   "`[−2, 4) ∪ (4, ∞)`",
                   "`(−2, 4) ∪ (4, ∞)`",
                   "`(−∞, −2] ∪ (4, ∞)`"],
             "c": 1,
             "why": "Two conditions hold at once: `x + 2 ≥ 0` gives `x ≥ −2`, and "
                    "`x − 4 ≠ 0` removes `4`. The first choice solves the root and "
                    "forgets the denominator. The third wrongly opens the left end, "
                    "but `x = −2` gives `√0/(−6) = 0`, a perfectly good output. The "
                    "fourth solves `x + 2 ≥ 0` backwards, keeping inputs that "
                    "make the root imaginary."},
            {"q": "What is the range of `g(x) = |x + 3| − 4`?",
             "a": ["`[−4, ∞)`", "`[0, ∞)`", "`[−3, ∞)`", "`(−∞, −4]`"],
             "c": 0,
             "why": "Absolute value is never below `0` and equals `0` at `x = −3`, so "
                    "the smallest output is `−4` and every larger output occurs. "
                    "`[0, ∞)` forgets the outside subtraction; `[−3, ∞)` copies the "
                    "input where the minimum occurs; `(−∞, −4]` reverses the direction."},
            {"q": "`q(x) = 3x + 1` has the stated domain `x ≠ −2`. What is its range?",
             "a": ["Every real number",
                   "Every real number except `−2`",
                   "Every real number except `−5`",
                   "Every real number except `5`"],
             "c": 2,
             "why": "A non-horizontal line reaches each output once. The removed input "
                    "`−2` would have produced `3(−2) + 1 = −5`, so that is the missing "
                    "output. Every-real ignores the stated restriction, `−2` copies an "
                    "input into the range, and `5` loses the sign in the substitution."},
        ],
        "mistakes": [
            ("Copying a missing input into the range",
             "For `q(x) = 2x + 1` on `x ≠ 3`, the domain misses `3` and the range "
             "misses `7`. Domain values live on the input axis; pass an excluded input "
             "through the formula to find which output its absence removes."),
            ("Opening an endpoint that a root leaves closed",
             "`√(x + 4)` is defined at `x = −4`, because `√0 = 0`. Only a strict "
             "inequality or a zero denominator opens an end, and a square root "
             "produces a non-strict one."),
            ("Losing half of a squared inequality",
             "`9 − x² ≥ 0` is `x² ≤ 9`, which is `−3 ≤ x ≤ 3`. Rooting both sides to "
             "get `x ≤ 3` keeps every large negative input, all of which make the "
             "inside negative. Solve it as an absolute value inequality: `|x| ≤ 3`."),
        ],
        "standard": ("Finish when you can state a domain from the formula in one "
                     "pass, and can justify the range of a line, square, absolute-value "
                     "rule or simple root "
                     "with a reason attached.",
                     "Given formulas with displayed linear denominators and square roots you should "
                     "produce the domain in interval notation, with the right "
                     "bracket at each end, and be able to justify each excluded input "
                     "by naming which condition caused it. For a range, state the "
                     "minimum or the input recovered from a requested output; do not "
                     "read the answer from a sketch alone."),
        "note": "Domain restrictions are the reason lesson 14 needs a restriction at "
                "all, and the reason a composite in lesson 13 can have a smaller "
                "domain than either function it was built from. Lesson 11 takes the "
                "idea one step further: a function whose domain is deliberately cut "
                "into pieces, with a different formula on each.",
    },

    # ---------------------------------------------------------------- 10
    {
        "slug": "piecewise-functions",
        "title": "Piecewise Functions",
        "module": "Functions",
        "one_line": "One function, several formulas, and the joins between them.",
        "summary": (
            "A piecewise function splits its domain into pieces and gives a separate "
            "formula on each. It is one function, not several: the conditions decide "
            "which formula applies, and no input may receive conflicting outputs."
        ),
        "key": [
            "          -x - 1     if x < -1",
            "f(x) =     x^2       if -1 <= x < 2",
            "          8 - 2x     if x >= 2",
            "overlap is safe only where the formulas agree",
        ],
        "key_label": "One function in three lines",
        "concepts_intro": (
            "The definition in lesson 8 says nothing about a function being given by "
            "a single formula. It never did; this lesson takes the permission."
        ),
        "concepts": [
            ("The conditions do the choosing",
             "To evaluate, first read the conditions and find the one your input "
             "satisfies; only then use the matching formula. Evaluating first and "
             "checking the condition afterwards produces an answer from the wrong "
             "branch, and it will look reasonable."),
            ("The pieces must not conflict",
             "If two conditions accept the same input and the formulas disagree "
             "there, the rule assigns two outputs and is not a function. Watch the "
             "endpoints: `x ≤ 3` and `x ≥ 3` overlap at `3`, while `x &lt; 3` and "
             "`x ≥ 3` do not. If overlapping formulas agree wherever they overlap the "
             "rule is still a function, but exclusive conditions make that fact visible."),
            ("A gap is legal; it just shrinks the domain",
             "`x &lt; 3` paired with `x &gt; 3` defines a perfectly good function "
             "whose domain omits `3`. That is a domain statement, not an error. Only "
             "an overlap with disagreeing values breaks the definition."),
        ],
        "read_title": "Reading, evaluating and drawing a piecewise rule",
        "read_intro": "The notation, the endpoint discipline, and what happens where two pieces meet.",
        "body": [
            ("def", ("Piecewise function",
                     "A <strong>piecewise</strong> function is defined by splitting "
                     "its domain into pieces and giving a formula for each piece. "
                     "The cleanest definition uses conditions that partition the domain, "
                     "so each input selects exactly one piece. Overlap is also legal "
                     "when every formula that applies gives the same output; conflicting "
                     "outputs are what violate the function definition.")),
            ("p", "The most familiar example was written down long before the "
                  "notation was: absolute value. `|x|` is `x` when `x` is at least "
                  "zero and `−x` when `x` is negative, which is two formulas and a "
                  "condition. Course 1, lesson 4 called the two cases a definition; "
                  "the piecewise brace is that definition typeset."),
            ("math", [
                "          x      if x >= 0",
                "|x| =",
                "         -x      if x < 0",
                "",
                "|-7| = -(-7) = 7        the second line, because -7 < 0",
                "| 7| =    7            the first line",
            ]),
            ("p", "Note that the second formula, `−x`, produces positive outputs. It "
                  "looks as though it should produce negative ones, and that reading "
                  "is what makes `|x| = −x` seem wrong. The minus sign is applied to "
                  "an input that is already negative."),
            ("h3", "A three-piece example"),
            ("p", "Take the function in the box at the top of this page: `−x − 1` "
                  "below `−1`, `x²` from `−1` up to but not including `2`, and "
                  "`8 − 2x` from `2` upward. The conditions cover every real number "
                  "once, so the domain is every real number."),
            ("math", [
                "f(-3) = -(-3) - 1 = 2          -3 < -1        first piece",
                "f(-1) = (-1)^2    = 1          -1 <= -1 < 2   second piece",
                "f( 0) = 0^2       = 0                         second piece",
                "f( 2) = 8 - 2(2)  = 4           2 >= 2        third piece",
                "f( 5) = 8 - 2(5)  = -2                        third piece",
                "",
                "the wrong branch at x = -1:  8 - 2(-1) = 10   condition fails",
            ]),
            ("p", "The last line is the error this lesson exists to prevent. `10` is "
                  "a real number produced by a real formula belonging to this very "
                  "piecewise definition, and nothing about it looks suspect. It is not "
                  "`f(−1)`, because the condition `x ≥ 2` rules that branch out. The "
                  "number `10` is in fact produced elsewhere by this function; branch "
                  "selection decides the value at the requested input, not whether the "
                  "number appears anywhere in the range."),
            ("h3", "What happens at a join"),
            ("p", "At `x = −1` the two neighbouring formulas disagree. Approaching "
                  "from the left, `−x − 1` heads toward `0`; the value the function "
                  "actually takes there is `(−1)² = 1`. The graph steps up by `1`, "
                  "and it is drawn with an open circle at `(−1, 0)` and a filled "
                  "circle at `(−1, 1)`."),
            ("p", "At `x = 2` they agree. The left formula `x²` heads toward `4`, and "
                  "the right formula gives `8 − 2(2) = 4`. The two pieces meet, so "
                  "the graph connects with no break and no circles are needed. "
                  "Whether a join is a step or a connection is settled by arithmetic, "
                  "not by how the formulas look."),
            ("math", [
                "join at x = -1        left formula -x - 1  ->   0",
                "                      value used   x^2     ->   1      step of 1",
                "",
                "join at x =  2        left formula x^2     ->   4",
                "                      value used   8 - 2x  ->   4      they meet",
            ]),
            ("h3", "Endpoints, and where the dot goes"),
            ("ul", [
                "<strong>A filled circle</strong> marks a point the function attains. "
                "Every input in the domain gets exactly one filled circle in the "
                "whole picture.",
                "<strong>An open circle</strong> marks a point the graph approaches "
                "but does not include, because the condition on that piece excluded "
                "the endpoint.",
                "<strong>A vertical stack of two different filled circles is impossible.</strong> "
                "Two filled circles above the same input would be two outputs, and "
                "the vertical line test from lesson 8 rules it out on sight. Two pieces "
                "that include the same identical point still contribute only one point.",
            ]),
            ("example", ("Overlap, gap, and neither",
                         "`{x + 1 if x ≤ 3; 2x if x ≥ 3}` is not a function: at `3` "
                         "the first line says `4` and the second says `6`. "
                         "`{x + 1 if x &lt; 3; 2x if x &gt; 3}` is a function whose "
                         "domain omits `3`. `{x + 1 if x ≤ 3; 2x if x &gt; 3}` is a "
                         "function on every real number. Three rules, one symbol "
                         "apart, and only the first is broken.")),
            ("p", "An overlap is harmless when the formulas happen to agree on it. "
                  "`{2x if x ≤ 3; x + 3 if x ≥ 3}` names `3` twice, but both lines "
                  "give `6`, so each input still has one output. This is worth "
                  "knowing and not worth relying on: writing the conditions so they "
                  "cannot overlap removes the need to check."),
        ],
        "lab": ("funcops", {
            "mode": "piecewise",
            "panel_title": "Set the pieces, watch the joins",
            "panel_intro": "Edit the formulas and the cut points; the lab draws each "
                           "piece over its own condition and reports the size of the "
                           "step at every join. A join of size `0` is where the graph "
                           "connects.",
        }),
        "steps_title": "Evaluating and sketching a piecewise rule",
        "steps_intro": "The order is condition, then formula. Reversing it is the whole error.",
        "steps": [
            ("Check the conditions cover the input once",
             "Before anything else, confirm that the pieces do not overlap and see "
             "where they leave gaps. A gap tells you the domain; an overlap with "
             "disagreeing formulas tells you the rule is not a function."),
            ("Find the condition your input satisfies",
             "Compare the input against each condition in turn. Write down which "
             "piece won before evaluating anything, so the choice is a decision "
             "rather than an assumption."),
            ("Evaluate only the matching formula",
             "The other formulas are not merely unhelpful, they are not part of the "
             "answer. At `x = −1` the third formula returns `10`, but its condition "
             "fails, so `10` is not `f(−1)`."),
            ("At each join, evaluate both neighbours",
             "Compute the left formula and the right formula at the cut point. Equal "
             "values mean the graph connects; different values give the size of the "
             "step, and tell you which endpoint gets the open circle."),
        ],
        "worked": {
            "title": "One three-piece function, evaluated and joined",
            "intro": ["The function from the top of the page, at six inputs and both "
                      "of its joins."],
            "lines": [
                "          -x - 1     if x < -1",
                "f(x) =     x^2       if -1 <= x < 2",
                "          8 - 2x     if x >= 2",
                "",
                "input      condition met        formula          value",
                "-----      -------------        -------          -----",
                "  -3       -3 < -1              -(-3) - 1          2",
                "  -2       -2 < -1              -(-2) - 1          1",
                "  -1       -1 <= -1 < 2         (-1)^2             1",
                "   0       -1 <=  0 < 2         0^2                0",
                "   2        2 >= 2              8 - 2(2)           4",
                "   5        5 >= 2              8 - 2(5)          -2",
                "",
                "joins",
                "",
                "  x = -1   left  -x - 1 ->  0      open circle at (-1, 0)",
                "           value  x^2   ->  1      filled circle at (-1, 1)",
                "           the graph steps up by 1",
                "",
                "  x =  2   left   x^2   ->  4",
                "           value 8 - 2x ->  4      the pieces meet; no circles",
            ],
            "after": [
                "The row for `x = −1` is the one to check twice. It sits on the "
                "boundary, and the condition that wins is the one written with `≤`. "
                "Change that symbol to `&lt;` and `−1` leaves the domain entirely.",
                "The two joins behave differently for a reason visible in the "
                "arithmetic and nowhere else. `−x − 1` and `x²` disagree at `−1`; "
                "`x²` and `8 − 2x` agree at `2`. Nothing about the shapes of the "
                "formulas predicts this, so both joins have to be computed.",
                "Reading a range off the picture: the third piece runs from `4` "
                "downward without bound, and the first piece runs from just above "
                "`0` upward without bound, so between them every real number is "
                "produced. The range is every real number, even though no single "
                "piece has that range.",
                "For a faded rehearsal, define `g(x)` by `2x + 1` for `x &lt; 0`, "
                "`x² + 1` for `0 ≤ x &lt; 3`, and `7 − x` for `x ≥ 3`. The condition "
                "for `x = 0` is supplied: use the middle piece. Evaluate at `−2`, "
                "`0` and `3`; compute both formulas at each join; then draw the open "
                "and filled endpoints and state which join connects and which jumps.",
            ],
        },
        "quiz_title": "Which piece, and what happens there",
        "quiz": [
            {"q": "Let `h(x) = x − 1` for `x &lt; 2` and `h(x) = 5 − x` for `x ≥ 2`. "
                  "What is `h(2)`?",
             "a": ["`1`", "`2`", "`3`", "Undefined"],
             "c": 2,
             "why": "The condition `x ≥ 2` includes the endpoint, so "
                    "`h(2) = 5 − 2 = 3`. `1` uses the excluded first formula; `2` "
                    "copies the input; undefined ignores that the second condition "
                    "covers the endpoint."},
            {"q": "At `x = 1`, do the pieces `2x` for `x &lt; 1` and `x + 1` for "
                  "`x ≥ 1` meet or jump?",
             "a": ["They meet at output `2`", "They jump from `1` to `2`",
                   "They jump from `2` to `1`", "The comparison cannot be made"],
             "c": 0,
             "why": "Both endpoint calculations give `2`: `2(1) = 2` and `1 + 1 = 2`, "
                    "so the pieces meet. The two jump choices use a formula without "
                    "evaluating it at the cut point, and the comparison is always "
                    "available even though only the second piece owns the value."},
            {"q": "Which piecewise rule fails to define a function?",
             "a": ["`{x + 2 if x ≤ 1; 3x if x ≥ 1}`",
                   "`{x − 1 if x ≤ 2; x + 1 if x &gt; 2}`",
                   "`{2x if x &lt; 0; 2x if x &gt; 0}`",
                   "`{x + 1 if x ≤ 2; 4 − x if x ≥ 2}`"],
             "c": 3,
             "why": "In the fourth rule, `x = 2` satisfies both conditions and the "
                    "formulas give `3` and `2`, so one input receives two outputs. "
                    "The first also overlaps, but both formulas give `3` at `1`, so it "
                    "is harmless. The second partitions the domain, and the third is "
                    "a legal function whose domain omits `0`."},
        ],
        "mistakes": [
            ("Evaluating first and checking the condition afterwards",
             "Substituting into whichever formula is nearest gives a plausible number "
             "from the wrong branch. At `x = −1` the third formula returns `10`, but "
             "that is not `f(−1)` because the condition fails. Read the conditions first."),
            ("Writing both endpoint conditions with a non-strict sign",
             "`x ≤ 3` beside `x ≥ 3` claims `3` twice. If the formulas disagree "
             "there, the rule is not a function at all. Prefer exactly one included "
             "endpoint; if both include it, verify that the outputs agree."),
            ("Assuming a join is a break",
             "Two different formulas can meet. At `x = 2`, `x²` and `8 − 2x` both "
             "give `4`, so the graph connects and neither endpoint needs a circle. "
             "Evaluate both sides rather than drawing a jump because the formulas "
             "look different."),
        ],
        "standard": ("Finish when you evaluate by reading the condition first, and "
                     "can say at each join whether the graph steps or connects, with "
                     "the two numbers that settle it.",
                     "Given a two- or three-piece definition you should evaluate at "
                     "any input including the cut points, decide whether the "
                     "conditions partition the domain or agree on any overlap, sketch the graph with open and "
                     "filled circles in the right places, and state the domain and "
                     "range. Recognising `|x|` as a piecewise function is the check "
                     "that the idea has landed."),
        "note": "Piecewise definitions are how a domain restriction becomes visible "
                "in a formula, and lesson 14 uses exactly that device: a function is "
                "cut down to a piece on which it can be inverted. Lesson 12 leaves "
                "formulas alone and asks a different question: what moving the graph "
                "does to the rule.",
    },

    # ---------------------------------------------------------------- 11
    {
        "slug": "transformations-of-graphs",
        "title": "Transformations of Graphs",
        "module": "Functions",
        "one_line": "Shift, stretch and reflect by mapping points from a known graph.",
        "summary": (
            "Changing a formula in four standard ways moves its graph in four "
            "predictable ways. Everything done outside the function acts on the "
            "output and behaves as written; everything done inside acts on the input "
            "and behaves in the opposite direction, all captured by one point map."
        ),
        "key": [
            "y = a f(b(x - h)) + k",
            "outside x:  a stretches by |a|,  k shifts up      as written",
            "inside  x:  b squashes by 1/|b|, h shifts right   the other way",
            "(x0, y0)  ->  (x0/b + h,  a*y0 + k)",
        ],
        "key_label": "One template, four controls",
        "concepts_intro": (
            "The graph of `f` is supplied. The task is not to know a future family of "
            "curves; it is to send known points to their new coordinates and use that "
            "mapping to explain the four familiar moves."
        ),
        "concepts": [
            ("Outside acts on the output, and reads normally",
             "In `2f(x) + 5` the function runs first and the result is doubled and "
             "raised by `5`. Output changes are vertical, and they do what the "
             "symbols suggest: `+5` is up, `×2` is taller, a minus sign flips the "
             "picture over the horizontal axis."),
            ("Inside acts on the input, and reads backwards",
             "In `f(x − 3)` the input is altered before `f` sees it. The new graph at "
             "`x = 5` shows the old value at `2`, so the whole picture moves right by "
             "`3`, not left. Every horizontal effect is inverted this way, and it "
             "catches everyone the first time."),
            ("Factor the inside before reading it",
             "`f(2x + 6)` is not a shift by `6`. Writing it as `f(2(x + 3))` shows a "
             "squash by `1/2` and a shift left by `3`. Until `b` is factored out, the "
             "number next to it is not the shift."),
        ],
        "read_title": "One point map, with four consequences",
        "read_intro": "Why inside and outside behave differently, where a known point lands, and how the four constants follow from that calculation.",
        "body": [
            ("def", ("Parent function",
                     "A <strong>parent function</strong> here is simply the supplied "
                     "reference graph `y = f(x)`. The core examples use a line, "
                     "`|x|` and `x³`, whose arithmetic is already available. The lab "
                     "also offers root and reciprocal previews, but those families are "
                     "not part of this lesson's completion standard.")),
            ("h3", "Why inside is backwards"),
            ("p", "This is the one point in the lesson that repays a proof rather "
                  "than a rule. Nothing about the graph of `f` changes; what changes "
                  "is which input is asked for."),
            ("proof", [
                "Let `g(x) = f(x − 3)`. Take any point `(t, f(t))` on the graph of "
                "`f`. Ask where `g` takes that same value: `g(x) = f(t)` as soon as "
                "`x − 3 = t`, which is `x = t + 3`.",
                "So the point `(t, f(t))` on the graph of `f` corresponds to the "
                "point `(t + 3, f(t))` on the graph of `g`. Same height, input three "
                "larger. Every point moves three to the right, so the graph does.",
                "The subtraction inside produces an addition to the coordinate "
                "because the equation `x − 3 = t` is solved for `x`. That single "
                "rearrangement is the entire reason horizontal effects are inverted, "
                "and it applies equally to the stretch: `g(x) = f(2x)` takes the "
                "value `f(t)` at `x = t/2`, so distances from the vertical axis are "
                "halved.",
            ]),
            ("h3", "The four moves"),
            ("ul", [
                "<strong>`f(x) + k`.</strong> Vertical shift. Up if `k` is positive, "
                "down if negative. The `x`-values are untouched.",
                "<strong>`a f(x)`.</strong> Vertical stretch by `|a|`, and a "
                "reflection over the horizontal axis when `a` is negative. Points on "
                "the horizontal axis stay put, since `a·0 = 0`.",
                "<strong>`f(x − h)`.</strong> Horizontal shift, right by `h`. Written "
                "with a minus sign inside, so `f(x + 4)` is `h = −4` and moves left.",
                "<strong>`f(bx)`.</strong> Horizontal squash toward the vertical axis "
                "by a factor of `1/|b|`, and a reflection over the vertical axis when "
                "`b` is negative. `f(2x)` is half as wide, not twice as wide.",
            ]),
            ("p", "The two reflections are worth separating. `−f(x)` negates the "
                  "output and turns the picture upside down; `f(−x)` negates the "
                  "input and turns it left to right. For `f(x) = x + 1`, they are "
                  "`−x − 1` and `−x + 1`, visibly different parallel lines. At the "
                  "parent point `(0, 1)`, the vertical flip lands at `(0, −1)` while "
                  "the horizontal flip leaves `(0, 1)` fixed. One point separates "
                  "the two readings without requiring a new curve family."),
            ("h3", "Reading a combined formula"),
            ("p", "Take `g(x) = −2|x − 3| + 5`, in the template with parent "
                  "`f(x) = |x|`, `a = −2`, `b = 1`, `h = 3`, `k = 5`. Move each "
                  "parent point by `(x₀, y₀) → (x₀ + 3, −2y₀ + 5)`. The corner "
                  "`(0, 0)` lands at `(3, 5)`; the two points `(−1, 1)` and `(1, 1)` "
                  "land at `(2, 3)` and `(4, 3)`. Those three points determine the "
                  "transformed V without any future quadratic technique."),
            ("math", [
                "g(x) = -2|x - 3| + 5          parent f(x) = |x|",
                "",
                "parent point        new x = x0 + 3        new y = -2y0 + 5       image",
                "( 0, 0)                    3                       5              (3, 5)",
                "(-1, 1)                    2                       3              (2, 3)",
                "( 1, 1)                    4                       3              (4, 3)",
                "",
                "direct checks:  g(3) = 5      g(2) = 3      g(4) = 3",
                "the equal heights at x = 2 and x = 4 confirm symmetry about x = 3",
            ]),
            ("p", "The coordinate map makes the order explicit. The new x-coordinate "
                  "is found from the inside equation `b(x − h) = x₀`, giving "
                  "`x = x₀/b + h`; the new y-coordinate is found after the parent "
                  "has run, as `ay₀ + k`. Mixing those routes &mdash; adding `k` to "
                  "an x-coordinate or dividing a y-coordinate by `b` &mdash; is not a "
                  "small slip but a change of which quantity each constant acts on."),
            ("h3", "When a horizontal stretch and a shift are combined"),
            ("p", "Let `f(x) = x³` and `r(x) = f(2x + 6)`. The `6` is not the shift. "
                  "Factoring gives `f(2(x + 3))`, so `b = 2` and `h = −3`. A parent "
                  "point with input `x₀` lands at `x₀/2 − 3`: the graph is half as "
                  "wide and moved left by `3`."),
            ("math", [
                "r(x) = f(2x + 6) = f(2(x + 3))      f(x) = x^3",
                "",
                "parent ( 0,  0)  ->  ( 0/2 - 3,  0) = (  -3,  0)",
                "parent ( 1,  1)  ->  ( 1/2 - 3,  1) = (-5/2,  1)",
                "parent (-1, -1)  ->  (-1/2 - 3, -1) = (-7/2, -1)",
                "",
                "check at x = -5/2:   2(-5/2) + 6 = 1, so r(-5/2) = f(1) = 1",
            ]),
            ("p", "The point calculation settles both horizontal constants at once. "
                  "Reading `6` as a shift left `6` would send `(0, 0)` to `(-6, 0)`, "
                  "but direct substitution shows `r(−6) = f(−6)`, not `f(0)`. The "
                  "factored `3` and the division by `2` are not a mnemonic; they are "
                  "the solution of `2x + 6 = x₀` for the new input."),
            ("example", ("Vertical and horizontal changes kept separate",
                         "If `(4, −2)` lies on `y = f(x)`, then on "
                         "`y = 3f(x − 5) + 1` it becomes `(9, −5)`: the inside equation "
                         "`x − 5 = 4` gives `x = 9`, while the outside calculation "
                         "`3(−2) + 1` gives `−5`. Checking one mapped point forces each "
                         "constant to act on the coordinate it actually controls.")),
        ],
        "lab": ("transform", {
            "mode": "all",
            "presets": [
                ("A line shifted right 3", "id|2|2|3|0"),
                ("A cubic squashed horizontally", "cu|2|4|0|0"),
                ("Absolute value flipped vertically", "ab|-2|2|0|0"),
                ("A cubic reflected horizontally", "cu|2|-2|0|0"),
                ("Absolute value with all four constants", "ab|-4|2|3|5"),
            ],
            "panel_title": "Four sliders, one parent",
            "panel_intro": "Predict where one labelled parent point will land, then "
                           "choose a line, absolute-value or cubic preset. The parent "
                           "stays behind the image, and the table computes the exact "
                           "point map before checking the drawn curve.",
        }),
        "steps_title": "Describing a graph from its formula",
        "steps_intro": "Identify the parent, factor the input, then read the constants in a fixed order.",
        "steps": [
            ("Name the parent",
             "Identify the supplied reference graph `y = f(x)`. For assessed work it "
             "will be a line, `|x|` or `x³`; the lesson is about moving its known "
             "points, not recalling an unlearned family shape."),
            ("Factor the coefficient out of the input",
             "Turn `f(2x + 6)` into `f(2(x + 3))` before reading anything horizontal. "
             "Skipping this is the single most common source of a wrong shift, "
             "because `6` is sitting there looking like the answer."),
            ("Read the outside constants as written",
             "`a` scales the output and flips it when negative; `k` raises it. These "
             "need no reinterpretation, which is why doing the vertical part first "
             "builds confidence for the horizontal part."),
            ("Read the inside constants backwards, then verify one point",
             "For a parent point `(x₀, y₀)`, solve `b(x − h) = x₀` to get "
             "`x = x₀/b + h`, then compute `y = ay₀ + k`. Substitute that new x into "
             "the transformed formula; the result must be the mapped y."),
        ],
        "worked": {
            "title": "Two formulas, described and checked",
            "intro": ["The first maps three landmarks of `|x|`; the second factors "
                      "the input before moving three points of `x³`."],
            "lines": [
                "1.  g(x) = -2|x - 3| + 5        parent f(x) = |x|",
                "",
                "        a = -2   b = 1   h = 3   k = 5",
                "        right 3, stretch vertically by 2, flip down, up 5",
                "        point map:  (x0, y0) -> (x0 + 3, -2y0 + 5)",
                "",
                "        ( 0, 0) -> (3, 5)       check g(3) = -2|0| + 5 = 5",
                "        (-1, 1) -> (2, 3)       check g(2) = -2| -1 | + 5 = 3",
                "        ( 1, 1) -> (4, 3)       check g(4) = -2|  1 | + 5 = 3",
                "",
                "        the corner (0, 0) becomes (3, 5); equal heights remain equal",
                "",
                "2.  r(x) = f(2x + 6)            parent f(x) = x^3",
                "",
                "        factor:  f(2(x + 3))",
                "        a = 1   b = 2   h = -3   k = 0",
                "        point map:  (x0, y0) -> (x0/2 - 3, y0)",
                "",
                "        ( 0,  0) -> (  -3,  0)    check 2(-3)   + 6 =  0",
                "        ( 1,  1) -> (-5/2,  1)    check 2(-5/2) + 6 =  1",
                "        (-1, -1) -> (-7/2, -1)    check 2(-7/2) + 6 = -1",
            ],
            "after": [
                "The first point map handles all four constants without asking the "
                "learner to picture four moves at once. Equal parent heights at `−1` "
                "and `1` become equal image heights at `2` and `4`, a built-in check.",
                "The second formula shows why factoring comes before naming `h`. The "
                "raw `6` disappears into `2(x + 3)`, and each direct input check "
                "confirms the half-width and the shift left by `3`.",
                "For a faded point map, suppose `(2, −1)` is on `y = f(x)` and "
                "`q(x) = 3f(2(x + 1)) − 4`. The supplied inside equation is "
                "`2(x + 1) = 2`. Solve for the new x, compute the new y, and verify "
                "the mapped point by substituting its x into the displayed rule.",
            ],
        },
        "quiz_title": "Which way does it move",
        "quiz": [
            {"q": "The graph of `y = f(x + 5)` is the graph of `y = f(x)` moved which way?",
             "a": ["Right `5`", "Left `5`", "Up `5`", "Down `5`"],
             "c": 1,
             "why": "The point `(t, f(t))` reappears where `x + 5 = t`, that is at "
                    "`x = t − 5`, so every point moves five to the left. The plus "
                    "sign suggests right, which is why this is the most missed fact in "
                    "the lesson. Up and down are changes made outside the function, "
                    "and `+5` is inside it."},
            {"q": "The point `(4, −2)` lies on `y = f(x)`. Where does it land on "
                  "`y = 3f(x − 5) + 1`?",
             "a": ["`(9, −5)`", "`(−1, −5)`", "`(9, −7)`", "`(4, −5)`"],
             "c": 0,
             "why": "Solve `x − 5 = 4` to get the new input `x = 9`, and compute "
                    "`3(−2) + 1 = −5`, so the image is `(9, −5)`. `−1` reads the "
                    "inside shift forwards; `−7` subtracts the outside `1`; `(4, −5)` "
                    "changes only the output."},
            {"q": "Which description matches `y = f(3x + 6)`?",
             "a": ["Squash horizontally by `1/3`, then shift left `2`",
                   "Stretch horizontally by `3`, then shift left `2`",
                   "Squash horizontally by `1/3`, then shift left `6`",
                   "Shift right `2`, with no horizontal scaling"],
             "c": 0,
             "why": "Factor the input: `3x + 6 = 3(x + 2)`. Thus `b = 3` gives "
                    "width factor `1/3`, and `h = −2` shifts left `2`. The second "
                    "uses `b` instead of its reciprocal, the third reads the unfactored "
                    "constant as the shift, and the fourth reverses the direction and "
                    "drops the scaling."},
        ],
        "mistakes": [
            ("Reading a subtraction inside as a shift left",
             "`f(x − 3)` moves right. The rule cannot be fixed by memorising it "
             "harder; solve `x − 3 = t` for `x` and the `+3` appears. Any time the "
             "direction is in doubt, that one line settles it."),
            ("Reading the number beside x as the shift",
             "In `f(2x + 6)` the shift is `3`, not `6`, because the input must be "
             "written as `2(x + 3)` first. Check a parent point: input `0` moves to "
             "`−3`, because `2(−3) + 6 = 0`; a supposed shift of `6` fails that test."),
            ("Calling f(2x) a stretch by 2",
             "It is a squash by `1/2`. The graph reaches at `x = 1` what the parent "
             "reached at `x = 2`, so horizontal distances are halved. The factor "
             "that describes the picture is `1/b`, never `b`."),
        ],
        "standard": ("Finish when you can go from formula to described graph and "
                     "back, including the case where the input has a coefficient.",
                     "Given a supplied graph and `y = a f(b(x − h)) + k`, you should "
                     "factor the input, map at least three known points with "
                     "`(x₀/b + h, ay₀ + k)`, and verify one in the displayed rule. "
                     "Given `f(4) = −2`, for example, you should locate the matching "
                     "point on `3f(2(x + 1)) − 4` without needing to know any new "
                     "parent-function family."),
        "note": "Every transformation here is a composition in disguise: `f(x − 3)` "
                "is `f` applied to the output of the rule that sends `x` to `x − 3`. "
                "Lesson 13 makes that "
                "explicit and general, which is why the horizontal moves will stop "
                "feeling like an exception once composition is in place.",
    },

    # ---------------------------------------------------------------- 12
    {
        "slug": "composition-of-functions",
        "title": "Composition of Functions",
        "module": "Functions",
        "one_line": "Feeding one function into another, in a fixed order.",
        "summary": (
            "Composition runs one function on the output of another: `(f ∘ g)(x)` "
            "means `f(g(x))`, with `g` first. The order is not a convention that can "
            "be swapped, and the composite's domain can be smaller than either "
            "function's."
        ),
        "key": [
            "(f o g)(x) = f(g(x))          g runs FIRST",
            "(f o g) and (g o f) are different functions",
            "domain: x must suit g, AND g(x) must suit f",
            "the circle is not multiplication",
        ],
        "key_label": "The definition and its three consequences",
        "concepts_intro": (
            "Lesson 12's horizontal shifts were compositions written informally. "
            "Here the operation gets its own symbol and its own rules."
        ),
        "concepts": [
            ("The inner function runs first",
             "In `(f ∘ g)(x)` the function nearest the input is `g`, and it goes "
             "first. The notation reads right to left, which is the reverse of "
             "English reading order, and that mismatch is the whole difficulty. "
             "`f(g(x))` is the same statement with the order visible."),
            ("Order changes the answer",
             "With `f(x) = 2x + 3` and `g(x) = x − 4`, `(f ∘ g)(x) = 2x − 5` and "
             "`(g ∘ f)(x) = 2x − 1`. At `x = 2` they give `−1` and `3`. Composition "
             "is not commutative even when both functions and both composites are lines."),
            ("The domain is decided in two stages",
             "An input must first be acceptable to `g`, and then `g(x)` must be "
             "acceptable to `f`. Both tests happen on the original expression, "
             "before any simplification, because simplifying can erase the evidence "
             "of the first stage."),
        ],
        "read_title": "Building a composite and finding where it is defined",
        "read_intro": "The definition, why order matters, how the domain is assembled, and why simplification cannot enlarge it.",
        "body": [
            ("def", ("Composition",
                     "Given functions `f` and `g`, the <strong>composite</strong> "
                     "`f ∘ g` is defined by `(f ∘ g)(x) = f(g(x))`. Its domain is "
                     "the set of inputs `x` in the domain of `g` for which `g(x)` "
                     "lies in the domain of `f`. The symbol is read \"f circle g\" "
                     "or \"f after g\".",
                     "\"After\" is the reading worth adopting, because it says the "
                     "order out loud. `f ∘ g` is `f` after `g`: `g` happens, then `f` "
                     "happens to the result. The alternative reading, \"f of g\", "
                     "is also correct but is easier to say without thinking about "
                     "which one moves first.")),
            ("h3", "Computing a composite"),
            ("p", "Substitution again, exactly as in lesson 9, with a whole function "
                  "in the slot. Take `f(x) = 2x + 3` and `g(x) = x − 4`."),
            ("math", [
                "(f o g)(x) = f(g(x)) = f(x - 4)",
                "           = 2(x - 4) + 3",
                "           = 2x - 8 + 3   =   2x - 5",
                "",
                "(g o f)(x) = g(f(x)) = g(2x + 3)",
                "           = (2x + 3) - 4",
                "           = 2x - 1",
                "",
                "at x = 2     g(2) = -2,  f(-2) = -1     (f o g)(2) = -1",
                "             f(2) = 7,   g(7) = 3       (g o f)(2) = 3",
            ]),
            ("p", "Both composites are lines and they are still different functions. The "
                  "check at `x = 2` is worth doing every time a composite is built: "
                  "evaluate step by step through the two functions, then evaluate the "
                  "combined formula, and confirm they agree. `−1` against `−1` "
                  "catches an order or substitution error immediately."),
            ("h3", "The domain of a composite"),
            ("p", "Two conditions, applied in order. The input must be legal for the "
                  "inner function, and the inner function's output must be legal for "
                  "the outer one."),
            ("math", [
                "f(x) = sqrt(x)        g(x) = x - 5",
                "",
                "(f o g)(x) = sqrt(x - 5)      need x - 5 >= 0     domain [5, inf)",
                "(g o f)(x) = sqrt(x) - 5      need x >= 0         domain [0, inf)",
                "",
                "at x = 9:   sqrt(9 - 5) = 2          sqrt(9) - 5 = -2",
            ]),
            ("p", "Same two functions, two different domains, two different outputs. "
                  "In the first, the subtraction happens before the root, so the root "
                  "restricts which inputs survive. In the second the root goes first "
                  "and the subtraction cannot cause a failure, so only the root's own "
                  "condition applies."),
            ("h3", "The trap: simplifying before finding the domain"),
            ("p", "Take `f(x) = x²` and `g(x) = √x`. The composite simplifies to a "
                  "formula whose appearance has forgotten the inner function's domain."),
            ("math", [
                "(f o g)(x) = f(sqrt(x)) = (sqrt(x))^2 = x",
                "",
                "stage 1:  g(x) = sqrt(x) needs x >= 0",
                "stage 2:  f accepts every output from g",
                "",
                "domain of f o g:  [0, inf), even though the final formula is x",
                "",
                "the other order:  (g o f)(x) = sqrt(x^2) = |x|, domain (-inf, inf)",
            ]),
            ("p", "The simplified formula `x` accepts negative inputs, but the "
                  "composite does not: `g(−1)` never produces a real number, so `f` "
                  "is never reached. This needs no cancellation or rational-function "
                  "technique. It follows directly from the two stages: find the domain "
                  "before simplifying, and carry it beside the simplified rule."),
        ],
        "lab": ("funcops", {
            "mode": "compose",
            "presets": [
                ("Two lines: order changes the intercept", "2x + 3|x - 4"),
                ("Two shifts: this pair commutes", "x + 1|x + 2"),
                ("A root after a shift", "sqrt(x)|x - 5"),
                ("A square after a root: hidden domain", "x^2|sqrt(x)"),
            ],
            "panel_title": "Both orders, side by side",
            "panel_intro": "Predict both orders before choosing a preset. The lab "
                           "substitutes each whole inner rule, compares the outputs at "
                           "sample inputs, and carries the composite domain beside any "
                           "simplified formula.",
        }),
        "steps_title": "Building a composite safely",
        "steps_intro": "Four steps. The domain step comes before the simplifying step, and that ordering is the point.",
        "steps": [
            ("Write the composite with the inner function in brackets",
             "`f(g(x))` first, on its own line, before any substitution. For "
             "`(f ∘ g)` with `g(x) = x − 4`, that is `f(x − 4)`. Seeing the inner "
             "expression sitting in the slot prevents the order from flipping."),
            ("Substitute into every occurrence of the variable",
             "Same discipline as lesson 9: brackets around the whole inner "
             "expression, in every slot. `2(x − 4) + 3`, not `2x − 4 + 3`."),
            ("Find the domain from the unsimplified form",
             "Ask which inputs `g` rejects, then which of `g`'s outputs `f` rejects. "
             "For `f(x) = x²` after `g(x) = √x`, the inner root requires `x ≥ 0`; "
             "the outer square adds no restriction."),
            ("Simplify, then check one input end to end",
             "Now expand and collect. Then pick an input, run it through `g` and `f` "
             "separately, and compare with the simplified formula. Disagreement "
             "means the expansion is wrong; agreement at one point is not a proof, "
             "but it catches nearly every algebra slip."),
        ],
        "worked": {
            "title": "Two composites, both orders, and a domain that hides",
            "intro": ["The first pair shows that order matters. The second shows that "
                      "the simplified formula cannot be trusted for a domain."],
            "lines": [
                "f(x) = 2x + 3        g(x) = x - 4",
                "",
                "(f o g)(x) = f(x - 4) = 2(x - 4) + 3 = 2x - 5",
                "(g o f)(x) = g(2x + 3) = (2x + 3) - 4 = 2x - 1",
                "",
                "         x        (f o g)(x)       (g o f)(x)",
                "         0            -5               -1",
                "         2            -1                3",
                "        -1            -7               -3",
                "",
                "step by step at x = 2:   g(2) = -2  then f(-2) = -1      agrees",
                "                         f(2) = 7   then g(7) = 3         agrees",
                "",
                "both orders are defined for every real number",
                "",
                "-----------------------------------------------------------------",
                "",
                "p(x) = x^2           r(x) = sqrt(x)",
                "",
                "(p o r)(x) = (sqrt(x))^2 = x",
                "",
                "domain, stage 1:   r needs x >= 0",
                "domain, stage 2:   p accepts every output",
                "domain:            [0, inf), carried beside the simplified x",
                "",
                "the other order:   (r o p)(x) = sqrt(x^2) = |x|",
                "domain:            every real x",
            ],
            "after": [
                "The table is the honest way to show that order matters. Both results "
                "are lines with the same slope, so a quick glance could mistake them; "
                "the intermediate values reveal which constant was applied first.",
                "In the second example the simplified formula `x` is perfectly happy "
                "at `x = −1`, but the composite is not defined there because "
                "`√(−1)` is not real and the outer square is never reached. This is "
                "why stage 1 of the domain test is not optional.",
                "Both checks were done by running an input through the two functions "
                "in sequence. That is slower than trusting the algebra and it is the "
                "only verification that tests the order as well as the simplification.",
                "For a faded composite, take `u(x) = 3x − 1` and `v(x) = x + 2`. "
                "The first line `(u ∘ v)(x) = u(x + 2)` is supplied. Finish both "
                "orders, find each domain, and run `x = −1` through each chain before "
                "checking the two simplified formulas.",
            ],
        },
        "quiz_title": "Order, value and domain",
        "quiz": [
            {"q": "With `f(x) = 3x − 1` and `g(x) = x + 2`, what is `(f ∘ g)(1)`?",
             "a": ["`8`", "`4`", "`5`", "`6`"],
             "c": 0,
             "why": "`g` runs first: `g(1) = 3`, then `f(3) = 8`. `4` is "
                    "`(g ∘ f)(1)`: `f(1) = 2`, then `g(2) = 4`. `5` is the sum "
                    "`f(1) + g(1)`, while `6` is their product; both replace composition "
                    "with a different operation."},
            {"q": "With `f(x) = √x` and `g(x) = 2x − 6`, what is the domain of `f ∘ g`?",
             "a": ["`[3, ∞)`", "`[0, ∞)`", "`(−∞, 3]`", "`[−3, ∞)`"],
             "c": 0,
             "why": "`(f ∘ g)(x) = √(2x − 6)`, which needs `2x − 6 ≥ 0`, so "
                    "`x ≥ 3`. `[0, ∞)` keeps the outer root's usual domain without "
                    "accounting for `g`; `(−∞, 3]` reverses the inequality; and "
                    "`[−3, ∞)` moves the `−6` with the wrong sign before dividing."},
            {"q": "With `p(x) = x²` and `r(x) = √x`, the composite `p ∘ r` simplifies "
                  "to `x`. What is its domain?",
             "a": ["Every real number", "`[0, ∞)`", "`(0, ∞)`", "`(−∞, 0]`"],
             "c": 1,
             "why": "The inner function runs first, and `r(x) = √x` needs `x ≥ 0`; "
                    "the outer square adds no restriction. Every-real reads only the "
                    "simplified formula, `(0, ∞)` wrongly excludes `√0`, and "
                    "`(−∞, 0]` reverses the square-root condition."},
        ],
        "mistakes": [
            ("Composing in the written order",
             "`(f ∘ g)` applies `g` first, even though `f` is written first. The "
             "notation reads right to left. Saying \"f after g\" out loud before "
             "computing puts the order back the right way."),
            ("Treating the circle as multiplication",
             "`(f ∘ g)(1)` is `8` for `f(x) = 3x − 1`, `g(x) = x + 2`, while "
             "`f(1)·g(1)` is `6`. "
             "The circle is a small raised ring and the multiplication dot is a small "
             "raised dot, which does not help; the difference is in what the symbol "
             "does, not how it looks."),
            ("Reading the composite's domain off the simplified formula",
             "Simplifying can erase the operation that recorded a restriction. "
             "`(√x)²` simplifies to `x`, but negative inputs never pass through the "
             "inner root. Test the two stages on the original expressions."),
        ],
        "standard": ("Finish when you can build either composite, state its domain "
                     "from the two-stage test rather than from the simplified "
                     "formula, and verify the order at a chosen input.",
                     "Given two functions you should produce `f ∘ g` and `g ∘ f`, "
                     "show they differ by evaluating both at a specific input, and "
                     "give each domain with the excluded values justified by which "
                     "stage rejected them. One independent pair should be linear; a "
                     "second should include a square root whose restriction survives "
                     "simplification."),
        "note": "Composition is the machinery lesson 14 needs. An inverse is defined "
                "by what it does under composition &mdash; `f⁻¹ ∘ f` and `f ∘ f⁻¹` "
                "both have to be the function that leaves its input alone &mdash; so "
                "the order sensitivity established here is what makes that definition "
                "say something.",
    },

    # ---------------------------------------------------------------- 13
    {
        "slug": "inverse-functions",
        "title": "Inverse Functions",
        "module": "Functions",
        "one_line": "Undoing a function, and the restriction that is usually needed.",
        "summary": (
            "An inverse sends every output back to the input it came from. It exists "
            "only when no two inputs share an output; a function that repeats outputs "
            "must be cut down to a one-to-one piece first. The superscript `−1` is a "
            "label, not an exponent."
        ),
        "key": [
            "f⁻¹ undoes f:     f⁻¹(f(x)) = x     and     f(f⁻¹(x)) = x",
            "exists  ⟺  f is one-to-one   (horizontal line test)",
            "method:  swap x and y, then solve for y",
            "domain of f⁻¹ = range of f        f⁻¹(x) is NOT 1/f(x)",
        ],
        "key_label": "What an inverse is, when it exists, how to find it",
        "concepts_intro": (
            "Composition gave the language for undoing. This lesson asks which "
            "functions can be undone, and what to do about the ones that cannot."
        ),
        "concepts": [
            ("An inverse is defined by composition",
             "`f⁻¹` is the function for which `f⁻¹(f(x)) = x` for every `x` in the "
             "domain of `f`, and `f(f⁻¹(x)) = x` for every `x` in the domain of "
             "`f⁻¹`. Both directions are part of the definition, and checking both is "
             "how a candidate inverse is verified."),
            ("It exists exactly when f is one-to-one",
             "If two inputs share an output, the inverse would have to send that one "
             "output back to two places, and lesson 8 ruled that out. `f(x) = x²` "
             "sends `2` and `−2` both to `4`, so on all real numbers it has no "
             "inverse. On a graph, the horizontal line test decides it."),
            ("Restricting the domain is the usual repair",
             "Cutting the domain down until no output repeats gives a function that "
             "does have an inverse. `x²` on `x ≥ 0` inverts to `√x`; the same formula "
             "on `x ≤ 0` inverts to `−√x`. The restriction is a choice, and different "
             "choices give different inverses."),
        ],
        "read_title": "One-to-one, the swap method, and the restriction",
        "read_intro": "What the notation promises, the test that decides existence, the procedure, and the part that is usually left out.",
        "body": [
            ("def", ("One-to-one, and the inverse",
                     "A function is <strong>one-to-one</strong> if different inputs "
                     "always give different outputs: `f(a) = f(b)` forces `a = b`. "
                     "For a one-to-one `f`, the <strong>inverse</strong> `f⁻¹` is the "
                     "function with domain equal to the range of `f` that sends each "
                     "output back to the unique input it came from.",
                     "The notation is unfortunate and permanent. In `f⁻¹` the `−1` is "
                     "not an exponent, so `f⁻¹(x)` is not `1/f(x)` and the two are "
                     "almost never equal. For `f(x) = 3x − 7` the inverse is "
                     "`(x + 7)/3` and the reciprocal is `1/(3x − 7)`; at `x = −1` "
                     "they give `2` and `−1/10`. Nothing about the symbol warns you, "
                     "so this is a fact to hold separately.")),
            ("h3", "The horizontal line test"),
            ("thm", ("Horizontal line test",
                     "A function has an inverse if and only if no horizontal line "
                     "meets its graph more than once. A horizontal line is the set of "
                     "points sharing one output, so two intersections are two inputs "
                     "with the same output &mdash; exactly what one-to-one forbids.")),
            ("p", "The pairing with lesson 8 is exact. The vertical line test asks "
                  "whether a graph is a function at all; the horizontal line test "
                  "asks whether that function can be run backwards. A graph that "
                  "passes both is a function with an inverse, and the second test "
                  "says nothing about the first."),
            ("h3", "The swap method"),
            ("p", "Write `y = f(x)`, exchange `x` and `y`, and solve the result for "
                  "`y`. The swap is doing something specific: the graph of `f⁻¹` is "
                  "the graph of `f` reflected in the line `y = x`, and exchanging the "
                  "letters is that reflection performed on the equation."),
            ("math", [
                "f(x) = 3x - 7",
                "",
                "  y = 3x - 7          write y for the output",
                "  x = 3y - 7          swap x and y",
                "  x + 7 = 3y          solve for y",
                "  y = (x + 7)/3",
                "",
                "f⁻¹(x) = (x + 7)/3",
                "",
                "check   f(2) = -1        f⁻¹(-1) = 6/3 = 2        back to 2",
                "        f⁻¹(5) = 4       f(4) = 5                 back to 5",
            ]),
            ("p", "Both checks are needed in principle, and for a formula like this "
                  "one they will not disagree. They start to matter as soon as a "
                  "restriction is involved, because a candidate can undo `f` on part "
                  "of the domain and fail elsewhere."),
            ("h3", "Verifying both directions"),
            ("p", "The swap gives a candidate formula; composition proves it performs "
                  "the promised undoing. For the line above, both directions use only "
                  "the linear algebra already learned."),
            ("math", [
                "f⁻¹(f(x)) = ((3x - 7) + 7)/3",
                "           = 3x/3",
                "           = x",
                "",
                "f(f⁻¹(x)) = 3((x + 7)/3) - 7",
                "           = x + 7 - 7",
                "           = x",
            ]),
            ("p", "The first direction starts with an input of `f`; the second starts "
                  "with an input of `f⁻¹`. A single numerical round trip can catch an "
                  "error, but these two symbolic simplifications establish the claim "
                  "for every real input of the two lines."),
            ("h3", "When the inverse does not exist"),
            ("p", "`f(x) = x²` on all real numbers fails the horizontal line test at "
                  "every positive height. The output `4` came from `2` and from `−2`, "
                  "and an inverse would have to choose. Writing `√x` and calling it "
                  "the inverse of `x²` quietly makes that choice without saying so."),
            ("example", ("Restricting a square",
                         "`f(x) = x²` on `x ≥ 0` is one-to-one because the restriction "
                         "keeps only the non-negative inputs. Swapping gives `x = y²`, "
                         "so `y = ±√x`. The restriction `y ≥ 0` selects the positive "
                         "root, giving `f⁻¹(x) = √x` with domain `x ≥ 0`. Check: "
                         "`f(5) = 25` and `√25 = 5`. On the other half, `x ≤ 0`, the "
                         "same swap selects `−√x`; there `f(−5) = 25` and "
                         "`−√25 = −5`.",
                         "The `±` is where the restriction does its work. Without a "
                         "stated domain there is no way to choose a sign, and the two "
                         "choices are genuinely different functions undoing genuinely "
                         "different halves of the square's graph. Both are correct "
                         "inverses; neither is the inverse of the unrestricted `f`, "
                         "which has none.")),
            ("ul", [
                "<strong>Every line except a horizontal one is one-to-one.</strong> "
                "`y = mx + b` with `m ≠ 0` passes the test, and its inverse is "
                "another line with slope `1/m`.",
                "<strong>A horizontal line is not.</strong> `f(x) = 4` sends every "
                "input to `4`, so nothing can be recovered.",
                "<strong>Even powers and absolute value are not,</strong> without a "
                "restriction. `x²` and `|x|` both pair `a` with `−a`, and every "
                "even power does the same.",
                "<strong>Odd powers are.</strong> `x³` is one-to-one on all real "
                "numbers, and its inverse is the cube root, with no restriction "
                "needed anywhere.",
            ]),
        ],
        "lab": ("funcops", {
            "mode": "inverse",
            "presets": [
                ("A line: f(x) = 2x + 3", "2x + 3"),
                ("A square: needs a restriction", "x^2"),
                ("A cube: one-to-one", "x^3"),
                ("A constant: cannot be repaired on an interval", "3"),
            ],
            "panel_title": "Reflect in the line y = x",
            "panel_intro": "Predict whether the reflection will be a function, then "
                           "choose a preset. For a square the lab displays the exact "
                           "restriction it keeps and draws the discarded half dashed; "
                           "there are no draggable domain controls.",
        }),
        "steps_title": "Finding an inverse",
        "steps_intro": "Test first, then swap. Finding a formula for something that does not exist is the failure this order prevents.",
        "steps": [
            ("Check that f is one-to-one",
             "Use the horizontal line test on the graph, or argue from the formula: "
             "a line with non-zero slope and an odd power pass, an even power and an "
             "absolute value fail. If it fails, restrict the domain and record the "
             "restriction you chose."),
            ("Write y = f(x) and swap the letters",
             "Every `x` becomes `y` and every `y` becomes `x`, all at once. This is "
             "the reflection in `y = x` carried out on the equation, and it is the "
             "only step where the two letters change roles."),
            ("Solve for y",
             "Use Course 2 rearranging for a line. When a square appears, the `±` "
             "arrives here, and the restriction from step 1 decides which sign can "
             "return inputs from the retained half."),
            ("State the domain, and verify both compositions",
             "The domain of `f⁻¹` is the range of `f`, which is a check as much as a "
             "statement: if the two do not match, something earlier is wrong. Then "
             "confirm `f⁻¹(f(a)) = a` and `f(f⁻¹(b)) = b` at one value each."),
        ],
        "worked": {
            "title": "A line and a square restricted before inversion",
            "intro": ["The line passes the horizontal test. The square does not until "
                      "its domain is cut to one side of zero."],
            "lines": [
                "1.  f(x) = 3x - 7",
                "",
                "        y = 3x - 7   ->   x = 3y - 7   ->   y = (x + 7)/3",
                "        f⁻¹(x) = (x + 7)/3",
                "        domain and range of both: every real number",
                "        check   f(2) = -1    f⁻¹(-1) = 6/3 = 2",
                "        compositions:",
                "             f⁻¹(f(x)) = ((3x - 7) + 7)/3 = x",
                "             f(f⁻¹(x)) = 3((x + 7)/3) - 7 = x",
                "",
                "        NOT the inverse:  1/(3x - 7)   at x = -1 gives -1/10",
                "        NOT the inverse:  (x - 7)/3    at x = -1 gives -8/3",
                "",
                "2.  p(x) = x^2                    on x >= 0",
                "",
                "        horizontal test: passes on the retained right half",
                "        x = y^2   ->   y = +-sqrt(x)    swap and solve",
                "        retained inputs have y >= 0, so choose +",
                "        p⁻¹(x) = sqrt(x)                domain x >= 0",
                "",
                "        check   p(5) = 25             p⁻¹(25) = 5",
                "        p⁻¹(p(x)) = sqrt(x^2) = x     because x >= 0",
                "        p(p⁻¹(x)) = (sqrt(x))^2 = x   because x >= 0",
                "",
                "        on x <= 0 instead:  p⁻¹(x) = -sqrt(x)",
                "                p(-5) = 25              -sqrt(25) = -5",
            ],
            "after": [
                "The two rejected candidates in the first example fail in two "
                "different ways. `1/(3x − 7)` reads the `−1` as an "
                "exponent. `(x − 7)/3` does take the `7` first, which is the right "
                "order, but keeps the sign it arrived with: the `7` was subtracted "
                "last, so it must be <em>added</em> back first. At `x = −1` that "
                "candidate gives `−8/3` where the inverse gives `2`.",
                "The square example produces two different inverses from one formula. "
                "Both check out, and which one is correct depends entirely on the "
                "restriction that was stated. An answer of `p⁻¹(x) = √x` without a "
                "domain attached to `p` is incomplete, not merely untidy.",
                "For a faded inverse, let `g(x) = 5x + 2`. The swapped equation "
                "`x = 5y + 2` is supplied. Solve for `y`, state the inverse's domain, "
                "simplify both compositions symbolically, and use `g(−1) = −3` for "
                "a numerical round trip. Then explain why the horizontal line "
                "`h(x) = 4` cannot pass the same test.",
            ],
        },
        "quiz_title": "Undoing, and when it is possible",
        "quiz": [
            {"q": "Why does `f(x) = x²` on all real numbers have no inverse?",
             "a": ["Because `x²` is never negative",
                   "Because `4` comes from both `2` and `−2`, so an inverse would "
                   "have to send `4` to two places",
                   "Because `f(0) = 0`",
                   "Because `x²` is not a linear function"],
             "c": 1,
             "why": "One-to-one fails: two inputs share an output, so running the "
                    "assignment backwards produces two outputs for the input `4`, "
                    "which lesson 8 forbids. The first choice describes the range and "
                    "is true but irrelevant &mdash; `x³` has range every real number "
                    "and `√x` has range `[0, ∞)`, and both are invertible. The third "
                    "is a single value. The fourth is false as a criterion: `x³` is "
                    "not linear and does have an inverse."},
            {"q": "For `f(x) = 4x + 5`, what is `f⁻¹(x)`?",
             "a": ["`(x − 5)/4`", "`1/(4x + 5)`", "`(x + 5)/4`", "`4x − 5`"],
             "c": 0,
             "why": "Swapping gives `x = 4y + 5`, so `x − 5 = 4y` and "
                    "`y = (x − 5)/4`. The second choice is the reciprocal, not the "
                    "inverse; the third adds instead of undoing the added `5`; the "
                    "fourth performs the two inverse operations in the wrong form."},
            {"q": "`f(x) = x²` is restricted to `x ≤ 0`. What is `f⁻¹`?",
             "a": ["`f⁻¹(x) = √x`", "`f⁻¹(x) = −√x`",
                   "`f⁻¹(x) = x/2`", "The restriction still does not help"],
             "c": 1,
             "why": "Swapping gives `y = ±√x`, and the original restriction means "
                    "the recovered value must be non-positive, so choose `−√x`. The "
                    "positive root belongs to the `x ≥ 0` restriction; `x/2` treats "
                    "a square as multiplication by two; and retaining one half does "
                    "make the square one-to-one."},
        ],
        "mistakes": [
            ("Reading the superscript as an exponent",
             "`f⁻¹(x)` is not `1/f(x)`. For `f(x) = 3x − 7` the inverse is "
             "`(x + 7)/3` and the reciprocal is `1/(3x − 7)`; at `x = −1` they give "
             "`2` and `−1/10`. The notation collides with negative exponents and "
             "there is no fixing it, only remembering it."),
            ("Undoing the operations in the order they were applied",
             "`3x − 7` multiplies first and subtracts second, so the inverse adds "
             "first and divides second: `(x + 7)/3`. Writing `x/3 + 7` inverts both "
             "operations but applies them in the order `f` applied them, and it "
             "fails the check at the first value tried: `f(2) = −1`, while "
             "`−1/3 + 7 = 20/3`, not `2`."),
            ("Dropping the restriction",
             "Calling `√x` the inverse of `x²` is only true once `x²` has been cut "
             "down to `x ≥ 0`. Without that sentence the claim is false, since the "
             "unrestricted `x²` has no inverse at all, and the omission hides the "
             "fact that `x ≤ 0` would have given `−√x` instead."),
        ],
        "standard": ("Finish when you test for one-to-one before hunting for a "
                     "formula, and can produce an inverse together with its domain "
                     "and the restriction it required.",
                     "Given a non-horizontal line or `x²` restricted to one half-axis, "
                     "you should apply the swap method, state the inverse domain, make "
                     "the sign choice forced by the restriction, and verify both "
                     "compositions. Rational-function inverses and shifted quadratics "
                     "wait for the courses that teach their algebra."),
        "note": "That completes the toolkit the course promised: notation, domain, "
                "shape, composition and inverse. The path can now use function "
                "notation and inverse reasoning without smuggling in factoring, "
                "rational-function algebra or the quadratic formula before their "
                "own courses teach them.",
    },

    # ---------------------------------------------------------------- 14
    {
        "slug": "linear-inequalities-in-two-variables",
        "title": "Linear Inequalities in Two Variables",
        "module": "Lines",
        "one_line": "A boundary line, and which side of it is the answer.",
        "summary": (
            "Replacing the equals sign in a linear equation with an inequality turns "
            "a line into a half-plane. The line itself is the boundary, solid or "
            "dashed according to the symbol, and a single test point decides which "
            "side gets shaded."
        ),
        "key": [
            "boundary: replace the inequality sign with =",
            "solid line for <= or >=      dashed line for < or >",
            "test any point off the line; true means shade that side",
            "dividing by a negative reverses the inequality",
        ],
        "key_label": "Three decisions and the rule that catches people",
        "concepts_intro": (
            "A linear equation in two unknowns had a line for its solution set. An "
            "inequality has half the plane, and finding which half is one "
            "substitution."
        ),
        "concepts": [
            ("The solution set is a region",
             "A solution is still an ordered pair that makes the statement true, "
             "exactly as in lesson 1. There are simply infinitely many of them "
             "filling an area rather than lying along a line, and shading is how an "
             "infinite set gets drawn."),
            ("The boundary is in or out, and the symbol says which",
             "`≤` and `≥` include the line, drawn solid. `&lt;` and `&gt;` exclude "
             "it, drawn dashed. The dashed line is not decoration: `(0, −4)` "
             "satisfies `4x − 2y ≥ 8` and fails `4x − 2y &gt; 8`, and the drawing has "
             "to record that difference."),
            ("Test a point rather than guessing a side",
             "Substitute one point that is not on the line. A true statement means "
             "that point's side is the solution set; a false one means the other "
             "side. `(0, 0)` is the easiest test point whenever the boundary misses "
             "the origin, and when the boundary passes through it, any other point "
             "will do."),
        ],
        "read_title": "Boundary, side, and the sign that flips",
        "read_intro": "How to draw the region, why the test point is more reliable than the symbol, and the one algebraic move that reverses an inequality.",
        "body": [
            ("def", ("Linear inequality in two variables",
                     "A <strong>linear inequality in two variables</strong> is a "
                     "statement of the form `Ax + By &lt; C`, with `≤`, `&gt;` or "
                     "`≥` equally allowed and `A` and `B` not both zero. Its "
                     "<strong>solution set</strong> is the set of ordered pairs "
                     "making it true, which is a <strong>half-plane</strong>, "
                     "including its edge or not.")),
            ("p", "The line `Ax + By = C` splits the plane into two open regions. "
                  "Every point in one region makes `Ax + By` larger than `C`, every "
                  "point in the other makes it smaller, and points on the line make "
                  "it equal. That is why one test point settles the whole region: the "
                  "expression cannot change which side of `C` it falls on without "
                  "crossing the line."),
            ("h3", "Drawing the region"),
            ("ol", [
                "<strong>Replace the inequality sign with an equals sign</strong> and "
                "graph that line, by intercepts or by slope-intercept form, whichever "
                "lesson 2's methods make easier here.",
                "<strong>Make it solid or dashed.</strong> Solid for `≤` and `≥`, "
                "since those points are solutions; dashed for `&lt;` and `&gt;`, "
                "since they are not.",
                "<strong>Test one point off the line,</strong> preferably `(0, 0)`. "
                "Substitute both coordinates into the original inequality.",
                "<strong>Shade the side that won.</strong> If the test point made the "
                "statement true, shade its side; if false, shade the other.",
            ]),
            ("p", "For `2x + 3y ≤ 12` the boundary meets the axes at `(6, 0)` and "
                  "`(0, 4)`, and it is solid. Testing `(0, 0)` gives `0 ≤ 12`, which "
                  "is true, so the shaded half-plane is the one containing the "
                  "origin: the side below and to the left of the line."),
            ("h3", "Why the symbol alone cannot tell you the side"),
            ("p", "It is tempting to read `&gt;` as \"above\" and `&lt;` as \"below\". "
                  "That works only when the inequality has already been solved for "
                  "`y` with a positive coefficient, and it fails as soon as the "
                  "coefficient of `y` is negative."),
            ("math", [
                "4x - 2y > 8",
                "",
                "     -2y > -4x + 8",
                "      y  <  2x - 4          divided by -2, so the sign FLIPPED",
                "",
                "test (0, 0):    4(0) - 2(0) = 0        0 > 8 is FALSE",
                "test (3, 1):    4(3) - 2(1) = 10      10 > 8 is TRUE",
                "test (0, -10):  4(0) - 2(-10) = 20    20 > 8 is TRUE",
                "",
                "the symbol says >, the shaded region is BELOW the line y = 2x - 4",
            ]),
            ("p", "The written symbol is `&gt;` and the region is below. Both facts "
                  "are correct, and they are consistent because solving for `y` "
                  "required dividing by `−2`, which reversed the inequality into "
                  "`y &lt; 2x − 4`. A test point reaches the same conclusion without "
                  "needing the rearrangement at all, which is why it is the more "
                  "reliable method."),
            ("thm", ("Multiplying or dividing by a negative reverses the sign",
                     "If `a &lt; b` and `c` is negative then `ac &gt; bc`. This is "
                     "the single rule from course 2, lesson 9 that survives into two "
                     "variables, and it is where a correct boundary line ends up with "
                     "the wrong side shaded. Adding or subtracting anything, and "
                     "multiplying by a positive, leave the direction alone.")),
            ("h3", "When the boundary passes through the origin"),
            ("p", "`y &lt; 3x` has the origin on its boundary, so `(0, 0)` cannot be "
                  "the test point: it satisfies the equation, not the inequality, and "
                  "it lies on the edge rather than in either region. Any other point "
                  "works. Testing `(1, 0)` gives `0 &lt; 3`, which is true, so the "
                  "shaded region is the one containing `(1, 0)`, below and to the "
                  "right of the line."),
            ("example", ("Four points against one inequality",
                         "For `4x − 2y &gt; 8`: `(0, 0)` gives `0`, false. `(3, 1)` "
                         "gives `10`, true. `(0, −4)` gives `8`, and `8 &gt; 8` is "
                         "false, so this point sits exactly on the dashed boundary "
                         "and is not a solution. `(1, 2)` gives `0`, false. Only "
                         "`(3, 1)` is in the solution set, and `(0, −4)` is the one "
                         "worth pausing on: it would be a solution if the symbol were "
                         "`≥`.")),
            ("h3", "Reading a region back into an inequality"),
            ("p", "The reverse direction appears in modelling and in course 8. Find "
                  "the boundary line's equation from two of its points, choose `≤` or "
                  "`&lt;` from whether the line is solid or dashed, and then fix the "
                  "direction by testing a point taken from inside the shaded region. "
                  "The last step is the same substitution as before, run with the "
                  "answer known and the symbol unknown."),
        ],
        "lab": ("system", {
            "mode": "inequalities",
            "presets": [
                {"label": "solid boundary: 2x + 3y <= 12",
                 "eq": ["2x + 3y <= 12", "", "", ""]},
                {"label": "negative y coefficient: 4x - 2y > 8",
                 "eq": ["4x - 2y > 8", "", "", ""]},
                {"label": "boundary through the origin: y < 3x",
                 "eq": ["y < 3x", "", "", ""]},
                {"label": "vertical boundary: x >= -2",
                 "eq": ["x >= -2", "", "", ""]},
            ],
            "panel_title": "Boundary, then side",
            "panel_intro": "Each preset uses one constraint box and leaves the others "
                           "empty. The lab draws the boundary and shaded half-plane; it "
                           "does not accept a clicked test point, so predict and "
                           "substitute your own point before revealing the graph. Any "
                           "multi-constraint corner summary is a Course 8 preview, not "
                           "completion work here.",
        }),
        "steps_title": "Graphing a linear inequality",
        "steps_intro": "Boundary, style, test, shade. Doing the test before choosing a side keeps the symbol from misleading you.",
        "steps": [
            ("Graph the boundary",
             "Swap the inequality for an equals sign and draw that line. Intercepts "
             "are usually quickest: for `4x − 2y = 8` they are `(2, 0)` and `(0, −4)`."),
            ("Choose solid or dashed",
             "Solid when the symbol includes equality, dashed when it does not. Make "
             "this decision from the original inequality, before any rearranging, so "
             "a flipped sign cannot change it. Rearranging never changes whether the "
             "boundary is included."),
            ("Substitute a test point",
             "Use `(0, 0)` unless the boundary passes through it, in which case pick "
             "any convenient point off the line. Substitute into the original "
             "inequality and evaluate to a true or false statement."),
            ("Shade the winning side, then confirm",
             "True means shade the test point's side; false means shade the other. "
             "Then test one point from inside the shaded region: it must satisfy the "
             "inequality. That second substitution is the check that catches a "
             "reversed sign."),
        ],
        "worked": {
            "title": "Two inequalities, graphed and checked",
            "intro": ["The first is straightforward. The second has a negative "
                      "coefficient on `y`, which is where the shading goes wrong."],
            "lines": [
                "1.  2x + 3y <= 12",
                "",
                "        boundary   2x + 3y = 12        SOLID  (<= includes it)",
                "        intercepts (6, 0)  and  (0, 4)",
                "        test (0, 0):  2(0) + 3(0) = 0      0 <= 12   TRUE",
                "        shade the side containing the origin",
                "",
                "        confirm    (1, 1):   2 + 3 = 5     5 <= 12   TRUE",
                "                   (6, 4):  12 + 12 = 24  24 <= 12  FALSE, other side",
                "",
                "2.  4x - 2y > 8",
                "",
                "        boundary   4x - 2y = 8         DASHED (> excludes it)",
                "        intercepts (2, 0)  and  (0, -4)",
                "        test (0, 0):  4(0) - 2(0) = 0      0 > 8     FALSE",
                "        shade the side NOT containing the origin",
                "",
                "        in slope-intercept form:",
                "            -2y > -4x + 8",
                "             y  <  2x - 4              divide by -2, flip the sign",
                "        so the region is BELOW the line, although the symbol is >",
                "",
                "        confirm    (0, -10):  0 + 20 = 20    20 > 8    TRUE",
                "                   (3, 1):   12 -  2 = 10    10 > 8    TRUE",
                "                   (0, -4):   0 +  8 =  8     8 > 8    FALSE, on the edge",
            ],
            "after": [
                "The second example is the whole lesson in one picture. The symbol is "
                "`&gt;`, the region is below, and there is no contradiction: solving "
                "for `y` divided by `−2` and flipped the sign to `&lt;`. Anyone "
                "shading above has applied a rule that is only valid after the "
                "rearrangement has been done.",
                "The point `(0, −4)` is on the boundary and gives `8 &gt; 8`, which "
                "is false. With `≥` in place of `&gt;` it would be a solution and the "
                "line would be solid. One symbol changes the status of every point on "
                "the line and no other point in the plane.",
                "Both confirmations tested a point from inside the shaded region "
                "rather than re-reading the picture. Shading is easy to draw on the "
                "wrong side of a correctly drawn line, and only a substitution "
                "catches it.",
                "For a faded graph, use `3x − 2y ≤ 6`. The boundary "
                "`3x − 2y = 6` is supplied. Decide its line style, find two points on "
                "it, test the origin in the original inequality, shade the winning "
                "side, and confirm with a second point. Finally solve for `y` and use "
                "the reversed sign as an independent check on the shading.",
            ],
        },
        "quiz_title": "Boundaries and sides",
        "quiz": [
            {"q": "Which point satisfies `3x + y ≤ 5`?",
             "a": ["`(0, 6)`", "`(2, 0)`", "`(1, 2)`", "`(3, −3)`"],
             "c": 2,
             "why": "At `(1, 2)`, `3(1) + 2 = 5`, and `≤` includes equality. The "
                    "other three points each give `6`, so they lie on the non-solution "
                    "side. Rejecting `(1, 2)` because it is on the boundary would read "
                    "`≤` as a strict inequality."},
            {"q": "Solving `2x − 4y &gt; 12` for `y` gives which inequality?",
             "a": ["`y &gt; (1/2)x − 3`", "`y &lt; (1/2)x − 3`",
                   "`y &gt; −(1/2)x + 3`", "`y &lt; −(1/2)x − 3`"],
             "c": 1,
             "why": "`−4y &gt; −2x + 12`, and division by `−4` reverses the sign and "
                    "divides every term, giving `y &lt; (1/2)x − 3`. The first choice "
                    "does not flip; the third loses the sign of the x-term and the "
                    "constant; the fourth gets the constant sign wrong."},
            {"q": "A boundary line passes through the origin. Why can `(0, 0)` not be "
                  "used as the test point?",
             "a": ["Because the origin belongs to no quadrant",
                   "Because a point on the boundary makes the two sides equal, so it "
                   "cannot distinguish the regions",
                   "Because the origin satisfies every linear inequality",
                   "Because the inequality must be solved for `y` first"],
             "c": 1,
             "why": "The test works by asking which side of the line a point falls "
                    "on, and a point on the line falls on neither. Substituting it "
                    "gives a statement about equality that is the same whichever "
                    "region is intended. The first is true of the origin but "
                    "irrelevant. The third is false: `(0, 0)` fails `x + y &gt; 1`. "
                    "The fourth describes an optional rearrangement, not a "
                    "requirement."},
        ],
        "mistakes": [
            ("Forgetting to flip when dividing by a negative",
             "`4x − 2y &gt; 8` becomes `y &lt; 2x − 4`, not `y &gt; 2x − 4`. The "
             "boundary line is identical either way, so the graph looks right and the "
             "shading is on the wrong side. Testing `(0, −10)`, which satisfies the "
             "original, exposes it in one line."),
            ("Reading the side off the symbol",
             "`&gt;` does not mean above. It means above only after the inequality "
             "has been solved for `y` and the coefficient of `y` was positive. For "
             "`4x − 2y &gt; 8` the region is below the boundary. A test point never "
             "depends on the form the inequality happens to be written in."),
            ("Drawing a solid line for a strict inequality",
             "`&lt;` and `&gt;` exclude the boundary, so it is dashed. The "
             "difference is real: `(0, −4)` satisfies `4x − 2y ≥ 8` and fails "
             "`4x − 2y &gt; 8`, and a solid line claims every point of the boundary "
             "as a solution."),
        ],
        "standard": ("Finish when you can graph any linear inequality with the right "
                     "line style and the right side shaded, and can justify the side "
                     "by a substitution rather than by the symbol.",
                     "Given `5x − 2y ≥ 10` you should draw the solid boundary from two "
                     "checked points, choose and substitute a test point, shade the "
                     "correct half-plane, and confirm the result after solving for "
                     "`y`. You should also handle a boundary through the origin by "
                     "choosing a different test point, and read an inequality back off "
                     "a shaded picture."),
        "note": "That closes the line block. The next lesson changes the question from "
                "which pairs solve a statement to whether each input has exactly one "
                "output. Course 8 later stacks several shaded regions on one set of axes; "
                "the overlap of the shaded half-planes is the feasible set that "
                "linear programming optimises over.",
    },
]
