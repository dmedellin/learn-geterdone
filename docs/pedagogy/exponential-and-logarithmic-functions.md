# Pedagogy assessment — Exponential and Logarithmic Functions (algebra, course 7)

**This assessment supersedes `docs/pedagogy/prior/exponential-and-logarithmic-functions.md`
and makes no source change.** Nothing under `content/` or `site/` was edited in this
pass: the prose is settled and a downstream contract snapshot is pinned to it. The
closing section describes each repair precisely enough to execute later, and the
section after it records the delta against the superseded document — what this pass
caught that the first missed, and what the first claimed that this pass disputes.

Formed from all twelve lesson dicts in `content/algebra/c7_exponentials/`
(`part_a.py` lessons 01–06, `part_b.py` lessons 07–12, plus `__init__.py`), read
front to back, together with the two lab kits they render through — `expo_lab` and
`logarithm_lab` in `scripts/mathpath/labs/algebra_expo.py` — and the path-level
`content/algebra/__init__.py`. Every arithmetic figure a reader would trust was
recomputed by hand; the results are reported below.

Lessons in course order: `exponential-functions`, `growth-and-decay`,
`the-number-e`, `what-a-logarithm-is`, `logarithmic-functions-and-their-graphs`,
`the-laws-of-logarithms`, `common-and-natural-logarithms`, `change-of-base`,
`solving-exponential-equations`, `solving-logarithmic-equations`,
`compound-interest-and-continuous-growth`, `logarithmic-scales`.

The course declares `assumes_long` "exponents, inverse functions, and graphing", so
it is judged backwards against what courses 1–6 actually teach: rational and negative
exponents (`rational-exponents`, `integer-exponents`, `roots-and-radicals` in course
1), inverse functions and the horizontal line test (`inverse-functions`,
`transformations-of-graphs` in course 3), asymptotes (`graphs-and-asymptotes` in
course 5), and factoring a quadratic plus the substitution `u = f(x)`
(`solving-by-factoring`, `equations-reducible-to-quadratic-form` in course 6).

## What the course teaches well

- **The inverse is load-bearing rather than decorative, and it is used in both
  directions.** `what-a-logarithm-is` defines `log_b(x)` as the exponent and proves
  uniqueness from the fencing that `exponential-functions` put on the base
  (`.body[1]`: "`b = 1` is barred: `1^y = 1` for every `y`, so `log_1(1)` would have
  every number as an answer"). `logarithmic-functions-and-their-graphs` then derives
  domain, range, asymptote and direction as *consequences of the reflection* rather
  than as four facts to memorise, and its `.body[0]` says plainly why no domain
  restriction is needed — the exponential is strictly monotone, so the inverse exists
  outright. `solving-exponential-equations` and `solving-logarithmic-equations` are
  then explicitly the same manoeuvre run in opposite directions, and each says so in
  its `note`. A reader is never asked to memorise four unrelated uses of a logarithm.
- **Nearly every rule is derived in two lines from the definition, and the
  derivation is presented as the protection.** `the-laws-of-logarithms` proves all
  three laws by the single substitution `M = b^m`, `N = b^n` followed by one exponent
  law. `change-of-base` derives `log_b(x) = log_c(x)/log_c(b)` from `b^y = x` and the
  power law, and its `standard[1]` makes the point that matters: "If you can get
  there from `b^y = x` and the power law, you cannot put `log b` on top by accident,
  because the derivation shows where the denominator came from. Memorising the
  fraction alone leaves a fifty-fifty guess." `compound-interest-and-continuous-growth`
  builds `A = P(1 + r/n)^(nt)` as one repeated multiplication and then obtains
  `P·e^(rt)` by substituting `m = n/r` into `the-number-e`'s limit.
- **The domain restriction is treated as mathematics, not bookkeeping, and it is
  carried the whole way.** `what-a-logarithm-is` explains why the argument is
  positive (`.concepts[2][1]`: the question "has no answer", not that it is
  difficult); `logarithmic-functions-and-their-graphs` moves that restriction with a
  horizontal shift and flags the shift as "the commonest source of a wrong domain in
  the whole course"; `the-laws-of-logarithms` catches `log_b(x²) = 2 log_b(x)`
  failing at negative `x` and gives the repaired identity `2 log_b|x|`;
  `solving-logarithmic-equations` explains *exactly* why condensing manufactures
  solutions (`.concepts[1][1]`: `log M + log N` needs `M > 0` and `N > 0`, `log(MN)`
  needs only `MN > 0`) and then insists the test is on the arguments and not on the
  sign of `x`. That last distinction is made three separate times — in `.concepts[2]`,
  in `.body[9]`, and in quiz question 3 — and it is the right thing to repeat, because
  the rule of thumb it displaces ("logarithms hate negatives") discards correct
  answers.
- **The exact-versus-rounded discipline is genuine and it is stated at the point of
  use.** `the-number-e`'s table gives `(1 + 1/n)^n` as exact fractions where they are
  short (`625/256 = 2.44140625`, with the reason: "the denominator is a power of
  two") and as twelve-place decimals where they are not, labelled as rounded.
  `change-of-base` prints every quotient to six places and says so.
  `solving-exponential-equations` says the answer *is* `ln 30 / ln 7` and the decimal
  "is not the answer". `compound-interest-and-continuous-growth`'s `steps[2]` tells
  the reader to keep `1 + 0.05/12` as `1 + 1/240` rather than truncating it. The
  course `footer_lead` claims this is the one course on the path where labs show
  rounded decimals and that they say where they rounded; that claim holds.
- **Every completion standard names an act, and the act is what the closing drill
  measures.** Classify a table in one line and state `a`, `b` and the asymptote
  (`exponential-functions`); turn "falls 12% an hour from 90 mg" into
  `A(t) = 90·(22/25)^t` (`growth-and-decay`); convert `log_4(x) = 3/2` to `4^(3/2) = x`
  in one line (`what-a-logarithm-is`); state domain, asymptote and two points before
  drawing (`logarithmic-functions-and-their-graphs`); expand and re-condense with the
  restriction attached (`the-laws-of-logarithms`); cancel only the matched pairs and
  keep the scale factor on the crossed ones (`common-and-natural-logarithms`); state
  and prove the change-of-base identity (`change-of-base`); *sort* ten equations
  before solving any (`solving-exponential-equations` — the strongest standard in the
  course, because it names the decision rather than the algebra); write the domain
  line before the first algebraic step (`solving-logarithmic-equations`); build the
  formula instead of recalling it (`compound-interest-and-continuous-growth`); turn a
  difference into a factor (`logarithmic-scales`). None is "understand X".
- **The arithmetic is right.** Everything a reader would trust was recomputed:
  the rule-of-70 table (`70/1 = 70` against `69.6607`, `14` against `14.2067`, `7`
  against `7.2725`, `3.5` against `3.8018`) and the claim that the rule "runs slightly
  high below about 2% a step and slightly low above it" — the crossover is at about
  `1.95%`, so the sentence is exactly right; `(101/100)^69 ≈ 1.9869` and
  `(101/100)^70 ≈ 2.0068`; the whole `(1 + 1/n)^n` table to twelve places including
  `n = 31 536 000 ≈ 2.71828179`; the six consecutive differences
  `0.25, 0.1914, 0.1716, 0.0796, 0.0220, 0.0037`; `2.718^10 ≈ 22003.6` against
  `e^10 ≈ 22026.5`; `6^10 = 60466176`; `7^10 = 282475249`; `ln 10 ≈ 2.302585` and
  `log 500 ≈ 2.6990` against `ln 500 ≈ 6.2146`; `log_5(40) ≈ 2.292030` through all
  three helper bases and `log_40(5) ≈ 0.436295`; `ln 17 / ln 5 ≈ 1.760374`;
  `ln 4 / ln(9/4) ≈ 1.709511`; the entire compounding table
  (`1628.89, 1638.62, 1643.62, 1647.01, 1648.66, 1648.72`), the six-cent gap between
  daily and continuous, the effective rates `5.1162%`, `6.1364%` and `6.1678%`, the
  quarterly worked example `1346.86` with its `$8.63` and `$3.00` comparisons, and
  `1.4 · 10^21` for the percent-sign error; `10 · log 2 ≈ 3.0103`; the `30.1%` and
  `69.9%` gridline positions. Not one figure was wrong. For a generated course whose
  labs are checked by `mathcheck.js` but whose prose is not, that is the finding worth
  reporting first.

## What it teaches badly, or claims and does not deliver

### Order: an idea used one lesson before it is taught

1. **`growth-and-decay`'s own lab prints `ln` five lessons before `ln` exists.**
   The lesson attaches `("expo", {"mode": "growth"})`, and `drawGrowth()` in
   `scripts/mathpath/labs/algebra_expo.py` emits, into the "how long a factor of two
   takes" step list, the row *"the continuous doubling time — `ln 2 / |ln b|` ≈ …"*
   and then *"the 'rule of 70' — … The rule rounds `ln 2 ≈ 0.6931` up to `0.70`"*.
   Grepping the published page confirms both: `ln 2` appears twice on
   `site/exponential-and-logarithmic-functions/growth-and-decay/index.html`. The
   natural logarithm is not defined until lesson 7, `common-and-natural-logarithms`.
   This matters more than a stray symbol: the lesson prose was deliberately rewritten
   to *defer* that derivation — `.body[8]` now says "For now this is a checked
   shortcut, not a derived rule" — and the lab underneath it performs the derivation
   anyway, in notation the reader cannot read. The prose and the widget on one page
   disagree about what the reader is allowed to know.
2. **`logarithmic-functions-and-their-graphs`' lab hint names the natural logarithm
   two lessons early.** `LOG_HINT["graph"]` reads "Type `e` as the base to see the
   natural logarithm". `e` itself is fair game — `the-number-e` is lesson 3 — but the
   phrase *natural logarithm* and the `ln` notation are lesson 7's, and
   `LOG_LEGEND["graph"]` does not use them, so the hint is the only place the term
   leaks. Same family as item 1 and a one-word fix.
3. **`compound-interest-and-continuous-growth` calls the balances "a geometric
   sequence" two courses before the term is defined.** `.body[2]`: "Each period
   multiplies the balance by `1 + r/n`, so the balances form a geometric sequence."
   Grepping the whole Algebra path shows this is the *only* occurrence of "geometric
   sequence" before course 9, where `geometric-sequences-and-series` defines it. The
   sentence is true and it is doing no work — the derivation immediately below does
   not use the term — so it costs the reader a word they cannot look up in exchange
   for nothing.
4. **`solving-exponential-equations` re-teaches course 6 lesson 7 without naming
   it.** `.body[10]`–`.body[12]` introduce `u = e^x` on `e^(2x) − e^x − 6 = 0`, factor
   `u² − u − 6`, and warn in `.mistakes[1]` against "Solving for the substitution and
   stopping". Course 6's `equations-reducible-to-quadratic-form` teaches exactly that
   substitution, with the same headline (`key[3]`: "solve for `u`, then substitute
   BACK and solve for `x`") and the same named mistake. `e^(2x) = (e^x)²` is precisely
   its stated pattern, "the larger power is the square of the smaller". A reader who
   found that lesson hard is given no pointer back, and a reader who found it easy is
   not told they already own the technique. Every other cross-course debt in this
   course is cited by lesson name; this one is not.

### Facts a reader would trust that are wrong

5. **`the-number-e` question 2 marks as correct an answer that its own theorem
   contradicts.** The question (`.quiz[1]`) is: "A table shows that `(1 + 1/n)^n < 3`
   for `n = 1, 2, 4, 12, 365`. What has that table established by itself?" and the
   correct index is `1`, the option **"Only the five displayed terms are below `3`"**.
   Read as a claim about the sequence, that option is false — *every* term is below
   `3`, which the lesson states as a theorem six paragraphs earlier (`.body[6]`: "The
   sequence `(1 + 1/n)^n` is increasing, and no term of it exceeds `3`"). The intended
   reading is "the table establishes facts about only the five displayed terms", and
   the `why` supplies that reading; but the option as written is a sentence about the
   sequence, and the reader who knows the theorem is being asked to mark a false
   statement true. The question is a good question about evidence — it is the one
   place in the course that tests the path's own material clause — and the wording is
   the only thing wrong with it.
6. **The path page says Systems and Matrices comes last, and it does not.**
   `content/algebra/__init__.py` `why_order[3]`: "Systems and matrices come last
   because row reduction is elimination performed on exact fractions." The path has
   nine courses; Systems and Matrices is eighth and Sequences and Series is ninth.
   This is a path-level defect rather than a course-7 one and is recorded here because
   the same sentence is the one that justifies *this* course's seventh position
   ("Exponentials and logarithms come seventh because a logarithm is an inverse
   function"). It is repeated in the sibling assessments for courses 8 and 9.
7. `exponential-functions` `.concepts[0][1]` says "`x²` and `2^x` agree at `x = 2`
   and at very little else." They also agree at `x = 4` (`16 = 16`), which is the
   second value a reader checking the claim will try. "Very little else" is not false,
   but the lesson's whole method is *check the next value*, and the one example where
   it names an agreement omits the other one.
8. `exponential-functions` `.body[11]` defines "horizontal asymptote" from scratch.
   Course 5's `graphs-and-asymptotes` already defines it and proves the degree rules
   for rational functions. Re-defining it is defensible; doing so with no mention that
   the reader has met it is a missed consolidation, and it is the only prerequisite in
   the course that is re-issued rather than cited.

### Distractors that are also true

The failure `content/AGENTS.md` warns about by name. The data model carries one `why`
per question, so a defensible wrong answer is marked wrong and then explained with a
sentence that does not address it.

9. **`solving-exponential-equations` question 3, option (c).** The question is "Why
   does `2^x = −8` have no real solution?" and option (c) is **"Because `x = −3` gives
   `1/8` rather than `−8`"** — a true statement about the equation, marked wrong. The
   author clearly knew the category: the `why` goes out of its way to handle option
   (a) ("The first option is true but is not a reason: `20` is not a power of `2`
   either, and `2^x = 20` does have a solution"), which is model practice. Option (c)
   gets nothing at all, and it is the same species of answer — true, and not the
   reason.
10. `change-of-base` question 3, option (d), "Because a base of `1` would make the
    logarithm negative", is false; option (c), "Because `1^y` is undefined", is false.
    Neither is addressed. The question is sound; the feedback covers one distractor of
    three.

### Labs that do not agree with their own lessons

11. **`growth-and-decay`'s panel describes only half of what its lab does, and the
    half it describes is the half the lesson does not use.** `.lab[1].panel_intro`
    says the lab "finds the first whole `n` with `b^n ≥ 2` by exact search and then
    prints the true doubling time". The lesson's worked example is a *decay* model —
    `500 g` losing 20% a year, `b = 4/5` — for which `drawGrowth()` takes the other
    branch entirely and reports "first `n` with `b^n ≤ 1/2`" and "the continuous half
    time". The panel never mentions half-life, although half-life is what the lesson's
    `.body[5]` defines and what its worked example computes (`n = 4`, which the lab
    reproduces exactly). Worse, the KPI tile is hard-labelled in
    `EXPO_KPIS["growth"]` as **"Steps to double"**, so for the lesson's own worked
    example the lab displays the half-life under the word *double*.
12. **No preset of `expo/growth` reproduces the lesson's worked example, and the
    panel does not say what to type.** The presets are `b = 2`, `3/2`, `1/2`, `9/10`,
    `101/100`, `1`; the worked example is `a = 500`, `b = 4/5`. The reader who wants
    to watch the 20%-a-year decay the lesson spends a page on must know to type both
    boxes, and nothing tells them to.
13. **`exponential-functions`' panel stops one step short of its own worked
    example.** The lab draws "the straight line through `f(0)` and `f(1)`" beside the
    curve — which *is* the worked example, `g(x) = 3 + 3x` against `f(x) = 3·2^x`,
    agreeing at two points and parting immediately. At the shipped default (`a = 1`,
    `b = 2`) the line is `1 + x` and the numbers on screen are not the numbers in the
    lesson. Setting `a = 3` reproduces the worked example exactly, and the panel does
    not say so. The lab is right and the pointer is missing.
14. **`common-and-natural-logarithms`' completion standard cannot be exercised on its
    lab.** The standard is: given `log(10^u)`, `ln(e^u)`, `log(e^u)` and `ln(10^u)`,
    cancel only the matched pairs and keep the scale factor on the crossed ones. The
    `logarithm/common` mode takes a single argument `x` and reports `log_10(x)` and
    `ln(x)` beside a power-of-ten bracket. It has no way to form a crossed pair, so the
    lesson's central act — the one its worked example spends four lines on — has no
    figure anywhere on the page. The panel promises "compare the exponents needed by
    base `10` and base `e`", which is what the lab does; the mismatch is between the
    lab and the standard, not between the lab and the panel.
15. **`solving-exponential-equations`' lab cannot represent three of the lesson's
    four developments.** `solveexp` solves `a·b^(cx + d) = k`. The lesson's worked
    equation (2) — `5 · 2^x + 3 = 43`, the one `.worked.after[0]` calls "the one worth
    studying" — has a constant outside the power and does not fit. Nor does
    `4^(x + 1) = 3^(2x)` (unknown on both sides, two bases), nor
    `e^(2x) − e^x − 6 = 0` (the hidden quadratic). The panel says "Each equation is
    attempted both ways" without fencing which equations the lab accepts, so a reader
    who types the lesson's headline example gets a parse failure rather than a lesson.
16. **`solving-logarithmic-equations`' signature example has no preset, and both
    presets of the shape it needs are labelled "no solution".** The lesson's most
    carefully constructed idea is the negative candidate that *survives*:
    `log_3(x + 6) − log_3(x + 2) = 2` gives `x = −3/2` with arguments `9/2` and `1/2`,
    and it carries `.concepts[2]`, one of the two `example` blocks, `.mistakes[1]` and
    quiz question 3. In `LOG_PRESETS["solvelog"]` the two `diff`-shape presets are
    "log_2(x) − log_2(x + 3) = 1 — no solution" and
    "log_5(x − 1) − log_5(x − 4) = 0 — no solution". A reader who explores the
    difference shape meets nothing but empty solution sets, which is the exact
    misconception the lesson exists to break. (The default preset is the lesson's
    worked example verbatim, `log_2(x) + log_2(x − 2) = 3` — the best lab/lesson
    agreement in the course.)
17. **`logarithmic-scales` promises a logarithmic axis and the page never draws one.**
    `.body[10]`–`.body[12]` teach how to read a log axis (the mark for `2` at `30.1%`,
    for `5` at `69.9%`, the pattern repeating each decade) and that `y = a·b^x` plots
    as a straight line of slope `log b`. The course home's `how_to[3]` builds on it:
    "The distance from 1 to 10 being the same as 10 to 100 is either obvious or
    wrong-feeling, and it is worth being the first." `drawScale()` produces a
    four-row table of readings, difference and factor, and no plot at all. This is the
    only section in the course whose central claim is visual and whose page has no
    picture of it.
18. Smaller mismatches of the same kind, all worth one sentence each in a panel:
    `logarithmic-functions-and-their-graphs`' panel says "Move a point on one curve"
    when the control is a text field labelled "x (the point to trace)";
    `matrix`-style "set the two sizes first" phrasing recurs in `change-of-base`,
    whose panel frames the mode around "three helper bases … which must agree" while
    its default preset is `log_7(343) = 3`, an exact answer for which no helper base
    is needed; and the `det`-style naming in `change-of-base` is fine but the lesson's
    own worked example, `log_5(40)`, is not among the six presets.

### Quiz feedback that does not answer the wrong answer

19. The `why` fields are specific far more often than not, and where they are good
    they are very good: `growth-and-decay` Q1 names `1/20`, `6/5` and `5` and says
    what each would model; Q2 names the linear model, the year stopped early and the
    amount-lost-for-amount-left swap; `the-laws-of-logarithms` Q3 derives all three
    wrong answers (`log 11` from `5 + 2·3`, `log 30` from `5·3·2`, `log 225` from
    `(5·3)²`); `compound-interest-and-continuous-growth` Q1 and Q3 diagnose every
    option. Roughly a quarter of the thirty-six questions fall short, and these are
    they:
    - `exponential-functions` Q3 (`.quiz[2].why`) explains the correct range and why
      `≥ −5` is wrong, and says nothing about "Every real number" (a linear reading)
      or "greater than `0`" (the shift dropped) — two of the three distractors.
    - `what-a-logarithm-is` Q2 (`.quiz[1].why`) names only "choice one"; `1` and `−7`
      go unexplained, and `−7` is the interesting one (it reads the argument as the
      answer).
    - `what-a-logarithm-is` Q3 (`.quiz[2].why`) says "The other three permute those
      roles" and then diagnoses one of the three.
    - `logarithmic-functions-and-their-graphs` Q1 (`.quiz[0].why`) covers `x > 0` and
      `x ≥ 5` but not "Every real number except `5`", which is the answer of a reader
      who has confused a logarithmic asymptote with a rational one from course 5 —
      the most diagnostic wrong answer on the page.
    - `common-and-natural-logarithms` Q1 (`.quiz[0].why`) covers `100` and `10^3`, not
      `1/3`.
    - `change-of-base` Q3, `solving-exponential-equations` Q3 and
      `solving-logarithmic-equations` Q3 each leave one distractor unnamed (items 9
      and 10 above; `solving-logarithmic-equations`' is "Because the base changes
      during the condensing", which is worth refuting because it is a plausible
      mechanism).
    - `logarithmic-scales` Q3 (`.quiz[2].why`) explains `140` and `80` and not `70`,
      which is the answer of a reader who thinks two equal sources change nothing —
      the misconception the lesson's `.body[7]` heading is named after.

### Cognitive load and structure

20. **`solving-exponential-equations` carries five techniques and is the strongest
    split candidate in the course.** Same-base matching, taking a logarithm, the
    unknown on both sides, the hidden quadratic, and the no-solution shapes — with a
    fourteen-block body, three quiz questions and a lab that supports one of the five
    (item 15). The natural cut is after `.body[6]`: "Solving Exponential Equations"
    keeping the two methods and the sorting standard, and a second lesson taking the
    unknown on both sides and the substitution that hides a quadratic, which is where
    the debt to course 6 lesson 7 belongs (item 4). **I am not recommending the
    split.** It would change the URL space, which requires the five-place update and
    `@site-architect`, and the lesson's standard — *sort ten equations without solving
    any* — is the best thing in the course and depends on all five shapes being on one
    page. Recorded as a judgement, not a deferral.
21. `logarithmic-scales` is the second-heaviest page: three scale definitions, the
    difference theorem, the adding-sources argument, the log-axis section and the
    log-linear plot, on a fourteen-block body. Its three quiz questions test one idea
    (difference-to-factor) three times, so the log-axis material — two body blocks and
    a `how_to` line — is never retrieved. That is the imbalance worth fixing, not the
    length.
22. `common-and-natural-logarithms` is now the thinnest lesson in the course: two
    abbreviations, the matched/crossed inverse pairs, one proportionality, and an
    estimation bracket. The prior pass removed the characteristic-and-mantissa
    material and did not replace it, and the lesson would now sit comfortably inside
    `what-a-logarithm-is` or as the first half of `change-of-base`. It earns its place
    because `compound-interest-and-continuous-growth` needs `ln` and because the
    "which base does a bare `log` mean" convention is genuinely worth a page of its
    own (`.concepts[0][1]` on analysis versus complexity theory is the best paragraph
    in the lesson). Recorded as a judgement; not a merge candidate.
23. **Every lesson in the course has exactly three concepts, exactly four method
    steps, exactly three mistakes and exactly three quiz questions.** That is the
    floor of the range `TestLessonDataMatchesTheRenderer` enforces, and no lesson in
    this course takes the room `content/AGENTS.md` says a lesson may earn. The
    consequence is that `the-laws-of-logarithms`, which carries three proved laws and
    two invented ones, gets the same three questions as
    `common-and-natural-logarithms`, which carries two abbreviations. Retrieval
    density is constant while lesson weight varies by a factor of three.
24. The course outcomes now name the modelling acts (`outcomes[3]`: "build a
    compounding model, and turn a log-scale difference into a ratio"), which the
    superseded assessment correctly identified as missing and correctly repaired. The
    `how_to` promise that every worked example ends in a faded rehearsal is kept:
    all twelve `worked.after` blocks close with one, each supplying the first
    strategic move and withholding the rest. That is the single largest improvement
    in the course and it holds up under inspection.

## Where a learner gets stuck

- At `growth-and-decay`'s lab, five lessons before `ln` exists, reading "the
  continuous doubling time — `ln 2 / |ln b|`" on a page whose prose has just
  explicitly promised not to derive it (item 1).
- At the same lab, on the lesson's own decay example, reading the half-life under a
  tile labelled "Steps to double" (item 11).
- At `the-number-e` question 2, having read the theorem that no term exceeds `3` and
  being asked to mark "Only the five displayed terms are below `3`" as correct
  (item 5).
- At `solving-exponential-equations`' lab, typing `5 · 2^x + 3 = 43` — the equation
  the lesson calls the one worth studying — and finding the lab cannot accept it
  (item 15).
- At `solving-logarithmic-equations`' lab, exploring the difference shape to find the
  negative candidate that survives, and meeting two presets both labelled "no
  solution" (item 16).
- At `logarithmic-scales`' log-axis section, told that `2` sits `30.1%` along and `5`
  sits `69.9%` along, with no axis on the page to look at (item 17).
- At `common-and-natural-logarithms`' completion standard, asked to keep the scale
  factor on a crossed pair, with a lab that cannot form one (item 14).
- At `exponential-functions` question 3, having answered "greater than `0`", and told
  only why `≥ −5` is wrong (item 19).
- At `compound-interest-and-continuous-growth`, meeting "geometric sequence" with
  nothing in seven courses to look it up in (item 3).

## Repairs this pass recommends

No lesson is added, removed, renamed or reordered by any of these, so the five URL
declarations in `AGENTS.md` §1 are untouched by all of them. Items marked **(lab
kit)** are edits to `scripts/mathpath/labs/algebra_expo.py` and therefore belong to
`@chrome-renderer`; everything else is `content/algebra/c7_exponentials/`. Figures
below were recomputed by hand from the lab's shipped presets.

- **(lab kit) `drawGrowth()`: remove `ln` from the page of lesson 2.** In the
  `pairs.push` for the continuous time, replace the label and body
  `'ln 2 / |ln ' + Rtext(b) + '| &asymp; …'` with a form that does not name a
  logarithm — for example "the exact time, which is irrational: ≈ 3.1063 steps,
  computed by a method this course reaches in 'Solving Exponential Equations'" —
  keeping the numeric value, which is correct. In the rule-of-70 row, replace "The
  rule rounds `ln 2` ≈ 0.6931 up to 0.70" with "The rule replaces an irrational
  constant near `0.6931` by `0.70`". Both strings are the only `ln` on lesson 2's
  page; the identical figures stay. *Why:* the lesson prose was deliberately rewritten
  to defer this and the lab undoes the deferral (item 1).
- **(lab kit) `EXPO_KPIS["growth"]`: make the second tile's label mode-aware.** It is
  currently the constant `("Steps to double", "exKpi2")`. `drawGrowth()` already knows
  which branch it took (`doubling || halving`), so set the label text from the same
  test — "Steps to double" when `b > 1`, "Steps to halve" when `0 < b < 1`, "Never"
  when `b = 1`. *Why:* lesson 2's own worked example is a decay model and currently
  reads its half-life under the word *double* (item 11).
- **`growth-and-decay`.lab[1].panel_intro:** rewrite to name both branches and to
  point at the worked example's numbers — "Type `a = 500` and `b = 4/5` and the lab
  is the worked example: the first whole year at or under half is `n = 4`, and the
  true half-life is printed beside it as the rounded irrational it is. For a base
  above `1` the same two rows report doubling instead." *Why:* items 11 and 12.
- **`exponential-functions`.lab[1].panel_intro:** add one sentence — "Set `a = 3` and
  the line beside the curve is the worked example's `g(x) = 3 + 3x`, meeting
  `f(x) = 3·2^x` at `(0, 3)` and `(1, 6)` and nowhere after." *Why:* item 13.
- **`the-number-e`.quiz[1].a[1]:** change the correct option from "Only the five
  displayed terms are below `3`" to **"That those five terms are below `3`, and
  nothing about any other term"**, and extend `.quiz[1].why` with one clause saying
  the theorem in the reading is what covers the rest. *Why:* as written the correct
  answer contradicts the lesson's own theorem (item 5).
- **`solving-exponential-equations`.quiz[2].why:** append a sentence for option (c) —
  "`x = −3` really does give `1/8`, which is true and is a fact about one input; the
  reason is the range, which rules out every input at once." *Why:* item 9. The `why`
  already models this move for option (a); the repair is to apply it twice.
- **`exponential-functions`.concepts[0][1]:** change "agree at `x = 2` and at very
  little else" to "agree at `x = 2` and at `x = 4`, and nowhere else at all", and
  leave the rest. *Why:* item 7; the two agreements are what makes the ratio check
  necessary rather than optional.
- **`exponential-functions`.body[11]:** open the `def` with "Rational and Radical
  Expressions found horizontal asymptotes by comparing degrees; here is the same idea
  for a curve with no degree." *Why:* item 8, and it converts a re-definition into a
  consolidation at the cost of one clause.
- **`compound-interest-and-continuous-growth`.body[2]:** delete "so the balances form
  a geometric sequence" or replace it with "so the balances are each the one before
  multiplied by the same factor". *Why:* item 3; the term is undefined for two more
  courses and is carrying no weight.
- **`solving-exponential-equations`.body[10]:** open the "Equations that hide a
  quadratic" section by citing course 6 — "Quadratics and Complex Numbers' 'Equations
  Reducible to Quadratic Form' named this move: if an equation can be written
  `au² + bu + c = 0` for some `u = f(x)`, the quadratic methods apply. Here
  `u = e^x`." *Why:* item 4. Also add the corresponding pointer to `.mistakes[1]`,
  whose warning is that lesson's warning.
- **`solving-exponential-equations`.lab[1].panel_intro:** add a fence — "The lab
  solves `a·b^(cx + d) = k`, which is the shape of equations (1) and (3) above.
  Equation (2) has a constant outside the power and the two-base and substitution
  equations are outside it too; those are worked on the page rather than in the
  widget." *Why:* item 15, and a fence is far cheaper than widening the lab.
- **`solving-logarithmic-equations`:** add a seventh entry to
  `LOG_PRESETS["solvelog"]` **(lab kit)** for the `diff` shape with `b = 3`,
  `p = −6`, `q = −2`, `k = 2`, labelled "log_3(x + 6) − log_3(x + 2) = 2 — a negative
  candidate that survives", and point `.lab[1].panel_intro` at it. *Why:* item 16 —
  the lesson's signature idea currently has no reachable example on its own lab, and
  both existing presets of that shape reinforce the misconception it attacks.
- **`common-and-natural-logarithms`.lab[1].panel_intro:** say what the lab does *not*
  do — "The crossed pairs `log(e^u)` and `ln(10^u)` are worked on the page; the lab
  takes one argument and shows the two exponents that produce it, which is where the
  constant `ln 10 ≈ 2.302585` comes from." *Why:* item 14, without changing the lab.
- **`logarithmic-scales`:** either (a) add a `axis` sub-figure to `drawScale()`
  **(lab kit)** drawing one decade of a logarithmic axis with the `2` and `5` marks
  placed at `log 2` and `log 5`, or (b) if that is out of scope, move
  `.body[10]`–`.body[12]` behind an `example` block that gives the positions as exact
  statements the reader can check against a ruler, and drop the course home's
  `how_to[3]` claim that the lesson lets you feel the spacing. *Why:* item 17; (b) is
  the honest cheap fix.
- **`logarithmic-functions-and-their-graphs`.lab[1].panel_intro:** "Move a point"
  becomes "Type a value in the trace box". **(lab kit)** `LOG_HINT["graph"]`: "to see
  the natural logarithm" becomes "to see base `e`, which gets its own name two
  lessons from now". *Why:* items 2 and 18.
- **Six `why` fields** gain one clause each, naming the distractor they currently skip
  (item 19): `exponential-functions`.quiz[2] (the linear reading and the dropped
  shift); `what-a-logarithm-is`.quiz[1] (`1` and `−7`) and .quiz[2] (all three
  permutations, not one); `logarithmic-functions-and-their-graphs`.quiz[0] ("every
  real except `5`" is a rational function's domain, not a logarithm's);
  `common-and-natural-logarithms`.quiz[0] (`1/3` inverts the exponent);
  `change-of-base`.quiz[2] (`log_c(1) = 0` is defined, and a base of `1` makes the
  logarithm nonexistent rather than negative);
  `solving-logarithmic-equations`.quiz[1] (the base does not change during
  condensing; only the domain does); `logarithmic-scales`.quiz[2] (`70` is the answer
  of a reader who thinks two equal sources change nothing).
- **Path-level, recorded not fixed here:** `content/algebra/__init__.py`
  `why_order[3]` says Systems and Matrices comes last. It is eighth of nine. The same
  list gives no reason for Sequences and Series' position at all. Belongs in one
  commit with the sibling courses' assessments (item 6).

## Delta against the superseded assessment

The prior document is at `docs/pedagogy/prior/exponential-and-logarithmic-functions.md`
(202 lines, Codex lane). Its repairs are live on `main` and nothing here reverts them.

**What this pass caught that the first missed.**
- The first pass audited prose only and said so ("The generated pages under `site/`
  were not treated as source"), which meant it never opened a lab kit. Eight of this
  document's findings (items 1, 2, 11–18) live in `scripts/mathpath/labs/algebra_expo.py`
  or in the disagreement between a `panel_intro` and the widget underneath it. The
  largest of them, item 1, is a direct incompleteness in a repair the first pass
  claimed to have made.
- No distractor audit was performed. Items 9 and 10 are new, and item 5 — a *correct*
  answer that contradicts the lesson's own theorem — is the inverse of that audit and
  was found by running it.
- No per-distractor feedback audit was performed. Item 19 lists nine `why` fields that
  restate the rule instead of diagnosing a named wrong answer.
- The first pass did not check cross-course order backwards. Items 3, 4 and 8 come
  from that check: a term from course 9 used in course 7, a technique from course 6
  re-taught without citation, and a definition from course 5 re-issued.
- The first pass made no arithmetic check. This pass recomputed every figure a reader
  would trust (listed in the fifth bullet of "What the course teaches well") and found
  none wrong — a positive result that is worth recording precisely because it was not
  previously established.

**What the first pass claimed that this pass disputes.**
- *"Prerequisite repair: `growth-and-decay` defers the logarithmic derivation of the
  rule of 70 until logarithms have been introduced."* The prose defers it; the lab on
  the same page performs it, and `ln 2` appears twice on the published page (item 1).
  The repair is half-made, and the half that is missing is the half the reader sees
  as a computed figure rather than as prose.
- *"Cognitive-load repair: `common-and-natural-logarithms` now concentrates on the two
  hidden bases…"* Accurate as far as it goes, but the result is now the thinnest
  lesson in the course and its completion standard cannot be exercised on its own lab
  (items 14, 22). Removing the mantissa material was right; nothing replaced it.
- *"Worked → faded → independent: every worked panel now ends with a novel faded
  rehearsal."* Confirmed — twelve of twelve — and it is the best thing about the
  course. Not disputed; recorded because it is the one claim in the prior document
  this pass can verify outright.
- *Residual boundary.* The prior document's closing section says the course "does not
  … derive the factorial series used internally by the lab as a numerical
  cross-check". That is true of `the-number-e`'s prose, which now fences the series
  carefully in `.body[8]` and in its panel. But the lab still prints the series column
  and `EXPO_KPIS["e"]` still labels a tile "e, from the series", so a reader meets the
  series as a named method on the page whatever the prose says. Not a defect — the
  fencing is explicit and correct — but the boundary is softer than the prior document
  claims.
