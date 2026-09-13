# Pedagogy assessment — Foundations of Algebra (algebra, course 1)

**Second assessment. It supersedes `docs/pedagogy/prior/algebra-foundations.md`
and it changes no source.** Nothing under `content/` or `site/` was edited in
this pass: the prose is settled and a downstream contract snapshot is pinned to
it. Everything below that would have been a repair is written as a recommendation
precise enough to execute later.

Formed from all thirteen lesson dicts in `content/algebra/c1_foundations/`
(`part_a.py`, `part_b.py`, `__init__.py`), the course home, every lab mode they
attach in `scripts/mathpath/labs/algebra_basics.py`, and the page shape in
`scripts/mathpath/render.py` and `scripts/mathpath/labs/common.py`, as they stand
on `review/course-ui-standardization` at `d0a238a`. (The branch tip has since
moved to `19b6b0b`, which carried the supersession move itself along with a
test-suite change; it touched nothing under `content/` or `scripts/`, so every
line cited below is unchanged at the tip.) No lesson was sampled; every
`body` block, `concepts` card, `steps` entry, `worked` panel, `quiz` item,
`mistakes` row, `standard` and `lab` panel was read, and every preset list the
lessons select from was read against them.

The order the course now ships, from `__init__.py`'s `_LESSON_ORDER`, is
`real-numbers-and-the-number-line`, `order-of-operations`,
`algebraic-expressions-and-terms`, `properties-of-the-real-numbers`,
`absolute-value`, `integer-exponents`, `scientific-notation`,
`roots-and-radicals`, `rational-exponents`, `the-distributive-law`,
`combining-like-terms`, `evaluating-expressions`,
`translating-words-into-algebra`. The declared prerequisite is arithmetic —
"fractions, negatives, and long division" — and the path page promises "No prior
algebra. Foundations of Algebra starts from what a variable is." That promise is
the standard used here.

## What the course teaches well

- **The definitions that could have been asserted are forced instead.**
  `integer-exponents` refuses to hand over `x⁰` and `x⁻ⁿ`: its `body` asks what
  the quotient law *would* say at equal exponents, lets arithmetic supply `1`,
  and then says outright in the `def` that "These are definitions, not
  consequences. They are the only values that keep the three laws true."
  `rational-exponents` runs the same argument one level up, proves
  `(x^(1/n))ⁿ = x` from the product law, and then isolates exactly what is left
  over: "a convention has to [choose]. … That part *is* arbitrary, and it is the
  only arbitrary part." `roots-and-radicals` names the principal-root choice as a
  convention rather than a fact, and `properties-of-the-real-numbers` says in its
  first body paragraph that the field properties "are assumed." A reader finishes
  this course able to say which statements were proved, which were chosen, and
  why the choice was not free. That is unusual at this level and it is the
  course's best property.
- **Every invented law is killed by named numbers, and the numbers are chosen to
  be decisive.** `properties-of-the-real-numbers`' `body` `ul` disposes of
  `a(bc) = (ab)(ac)` at `(2, 3, 4)`, `√(a + b) = √a + √b` at `(4, 9)` and
  `1/(a + b) = 1/a + 1/b` at `(1, 1)`; `the-distributive-law`'s four-item `ul`
  adds `(a + b)²` at `(1, 3)` and `12/(x + 6)` at `x = 6`; `integer-exponents`
  kills `(x + y)² = x² + y²` at `(1, 3)`. `combining-like-terms`' `mistakes[1]`
  goes one better and says why a *bad* test is bad: "Testing at `x = 1, y = 1`
  gives `7` on both sides and proves nothing; testing at `x = 2, y = 1` gives
  `10` against `14`." Both figures check.
- **`properties-of-the-real-numbers`' lab is built the right way round.** The
  `LAWS` array in `algebra_basics.py` holds sixteen *claims*, and its own comment
  says so: "a NAME here is a NAME … Which of these are laws is decided below by
  arithmetic, not by this list." Four of the sixteen are false, and one of them
  is `−(b − c) = −b − c` — the error the lesson's `mistakes[2]` calls the one
  that "will outnumber all the others in the next two courses." The lab then
  searches 512 triples and reports honestly: "A search finding nothing is
  evidence and not proof." The reader watches the course's headline misconception
  fail as a red row rather than being told about it.
- **The reordering the first pass made is coherent all the way through the
  back-references.** `algebraic-expressions-and-terms` now sits at 3, so when
  `properties-of-the-real-numbers` at 4 reorders `x + 7`, the letter, the term,
  the sign and the coefficient have all been named. Every backward citation now
  lands: `combining-like-terms` cites "the invisible coefficient from 'Variables,
  Expressions, and Terms'", `the-distributive-law` cites
  `properties-of-the-real-numbers` for `(−1)(−7) = +7`, `combining-like-terms`'
  `proof` cites `the-distributive-law` read right to left,
  `evaluating-expressions` cites `order-of-operations` for `−3²`, and
  `roots-and-radicals` cites `absolute-value` for `√(x²) = |x|`. All five point
  backwards in the shipped order. The first pass's central claim is verified.
- **Exactness is enforced at the point where it is cheapest to lose.**
  `real-numbers-and-the-number-line` settles `1.41` against `√2` by squaring and
  then states the condition on squaring and demonstrates it failing on negatives
  (`25/16 > 36/25` "would suggest the wrong order"). `evaluating-expressions`'
  worked example at `x = −1/2` stays in fractions to the end. `scientific-notation`'s
  lab carries mantissas as exact rationals and prints a fraction rather than
  rounding when a mantissa has no terminating decimal (`plaindec` returns `null`
  and the caller falls back to `Rtext`).
- **Two labs are fenced honestly against the lessons that own their extra rows.**
  `absolute-value`'s panel says "The `√(a²)` check is a preview of 'Roots and
  Radicals'; the two-case definition and the distance are the work to retrieve
  here", and the lab does compute `|a|` twice, once per branch and once as
  `Rsurd(a·a)`. `algebraic-expressions-and-terms`' panel fences the expanded count
  as a preview of `the-distributive-law` and the degree column as a preview of
  Polynomials and Factoring, and says the degree column "is not part of this
  lesson's completion standard." That is the right shape for a shared lab kit.
- **No wrong answer in the course's thirty-nine quiz options can be defended.**
  I tried to argue for each one. The nearest miss is `roots-and-radicals`
  question 1, where `±4` is offered against `√16`; it fails only because the
  lesson has already said in its `body` that "`√9 = ±3` is wrong as written" and
  explained why the `±` belongs to the equation and not the symbol. Given the
  recurring failure the content package's own `AGENTS.md` warns about, a clean
  result across thirteen lessons is worth recording.

## What it teaches badly, or claims and does not deliver

### Order: an idea used one lesson before it is taught

1. **`properties-of-the-real-numbers` (lesson 4) uses the radical sign three
   lessons before `roots-and-radicals` (8) defines it.** Its `body` `ul` disproves
   `√(a + b) = √a + √b` with "the left side is `√13` and the right side is `5`",
   and its `standard` is built around numerical counterexamples of that kind. The
   symbol `√`, the principal-root convention that makes `√13` name one number, and
   the fact that `√13` is irrational are all lesson 8's. The same counterexample is
   then repeated, correctly placed, in `the-distributive-law` (10) and
   `roots-and-radicals` (8) itself. Lesson 4 does not need it: it already has two
   other disproofs on the same list that use only arithmetic the reader has.
2. **The course's own verification method is used from lesson 4 and taught at
   lesson 12.** `properties-of-the-real-numbers` `steps[3]` instructs "Substitute
   small values into the expression you started with and the one you finished
   with", and its `worked.after` checks `5 − 2(x − 3)` at `x = 4`.
   `the-distributive-law` `steps[3]` makes substitution a numbered step and its
   worked panel checks two lines at `x = 1`. `combining-like-terms` checks at
   `a = b = 1`. The lesson that teaches substitution, and specifically teaches
   that the value must be written in brackets or the structure changes, is
   `evaluating-expressions` at 12 — whose `concepts[0]` says the brackets are
   "how you guarantee" that. A reader told at lesson 4 to substitute `−3` has been
   given the instruction without the discipline, and `order-of-operations`
   (lesson 2) has already shown them that `−3²` is `−9`. The gap is eight lessons
   wide and it is the course's own most-used move.
3. `real-numbers-and-the-number-line`'s `mistakes[1]` states a claim wider than
   the lesson's own theorem: the `thm` covers "the square root of a positive
   whole number", while the mistake says "The root is irrational only when the
   radicand is not a perfect square **of a rational**". The wider claim is true
   and is used in the lesson's own `steps[0]` (`√(4/9)` is `2/3`), but nothing on
   the page or in `roots-and-radicals` proves it, and dividing a radical over a
   quotient is lesson 8's `thm`.

### Facts a reader would trust that are wrong

4. **`scientific-notation` states the comparison rule in signed order on a page
   whose definition admits negative numbers.** `concepts[0]` says: "Two numbers in
   this form are compared by their exponents first, and only by their mantissas if
   the exponents tie — which is why `8.9 × 10⁻⁵` is smaller than `1.2 × 10⁻⁴`."
   The `key` and the `def` both give the condition as `1 ≤ |a| < 10`, so negative
   mantissas are in scope, and for them the rule is false: `−8.9 × 10⁻⁵` is
   *larger* than `−1.2 × 10⁻⁴`. This is precisely the class of error the first
   pass repaired everywhere else on the page — `concepts[1]`, the `body` sign
   check and the `steps[3]` sign rule are all stated in magnitude, and the lab's
   `normalise` uses `Rabs(m)` and handles a negative mantissa correctly. One
   concept card was missed, and it is the one that states a comparison the
   lesson's own quiz question 3 then tests.
5. **`order-of-operations` question 3's feedback names an error that produces a
   different number.** For `2 + 18 / 3 · 2` the `why` says "`16` adds first".
   Adding first gives `(2 + 18)/3 · 2 = 40/3`. `16` is what you get from
   `18 / 3 = 6`, then `2 + 6 = 8`, then `8 · 2 = 16` — the addition level taken
   before the remaining multiplication, which is a different and more interesting
   misreading, and the one the lesson's `concepts[1]` is about.
6. **`evaluating-expressions` question 2 misdiagnoses the lesson's own headline
   error.** The item is `−2x²` at `x = −3`; the answer is `−18` and the distractor
   `18` is `−2 · (−3²) = −2 · (−9)` — the substitution made without brackets,
   which is `concepts[0]`, `mistakes[0]`, the `body`'s first math block and the
   `standard`. The `why` instead says "`18` puts the coefficient inside the
   square's sign change", which describes no operation that yields `18`. The one
   distractor that *is* the lesson is given someone else's diagnosis.
7. **`evaluating-expressions` question 1 gives two distractors the same
   derivation and leaves the third with none.** For `3x² + 2x − 1` at `x = −2`,
   the `why` assigns "squares without brackets" to `−17` and "treats the exponent
   as multiplication by two" to `3`. Both of those errors evaluate to `−17`
   (`3·(−4) + 2·(−2) − 1` either way). I enumerated the plausible
   mis-evaluations and none produces `3`; the reachable wrong values are `−17`,
   `−9`, `8`, `15`, `31` and `39`. The distractor is unreachable and its
   explanation belongs to a different option.
8. `the-distributive-law`'s `key` states the false rule half-evaluated:
   `12/(x + 6) ≠ 12/x + 2`. The `2` is `12/6`, and printing it as `2` hides the
   invented distribution that produced it. The `body` gets this right —
   "`12/(x + 6)` is not `12/x + 12/6`" — and then quiz question 3 offers the
   `key`'s form as an option, so the reader is asked to reject a statement whose
   generating rule has been simplified out of view.

### Distractors that are also true

9. None. This is the recurring failure the content package's `AGENTS.md` names,
   and across thirteen lessons and thirty-nine wrong answers I could not
   construct a defence for one of them. Two shapes came close and both are
   closed by text already on the page: `roots-and-radicals` question 1's `±4`
   (closed by the `body`'s "`√9 = ±3` is wrong as written") and
   `rational-exponents` question 3's "It is a definition adopted for convenience;
   no law requires it" (closed by the `thm` and its proof, and the `why` says so
   explicitly). Recorded as a clean result rather than as a finding.

### Labs that do not agree with their own lessons

10. **`absolute-value` sends the reader to a lab preset that does not exist.**
    The `worked.after` faded rehearsal says: "With `a = −6` and `b = 1`, decide
    which line of the definition fires and find the distance before opening the
    matching lab preset". `RL_PRESETS["absolute"]` holds six entries —
    `(−4, 6, 3)`, `(3, 3, 0)`, `(2, −5, −1)`, `(−3/2, 5/2, 7/2)`, `(0, −7, 5)`
    and `(5, −5, 10)` — and none of them is `a = −6`. The values can be typed
    into `nlA` and `nlB`, so the act is possible; the sentence that tells the
    reader how to perform it is false.
11. **`properties-of-the-real-numbers`' panel promises a diagnosis its default
    preset cannot produce.** The panel says "Predict one row before changing the
    values; the last column then diagnoses a rule that only happened to work on
    your first choice." On the shipped default `a = 2, b = 5, c = 3`, every one
    of the four false claims fails immediately, so no rule "happens to work" and
    the promised experience never occurs. The presets that produce it are
    `(4, 4, 4)` — where commutative subtraction and commutative division both
    hold — and `(1, 1, 1)`, where four false claims hold at once. The lab source
    knows this (`EXPR_PRESETS`' comment says "the property presets include
    (4, 4, 4), where subtraction looks commutative"); the panel does not say it.
12. **`real-numbers-and-the-number-line`'s lab never opens on the lesson's
    work.** `RL_PRESETS["place"]` contains neither the worked example's list
    (`−5/4, −1.2, 0.6, 2/3, 1.41, √2`) nor the `standard`'s
    (`−9/8, −1.12, 5/6, 0.84, √3`). The panel points instead at preset 6,
    `sqrt(2), 2/sqrt(2), sqrt(8)/2` — three spellings of one point, which is
    `concepts[1]`, not the ordering act the `standard` measures. The list is a
    free text field, so nothing blocks the reader; the panel simply directs them
    somewhere else.
13. **`roots-and-radicals`' preset drops the sign that its worked line exists to
    teach.** Worked line 2 is "the 3rd root of `−54`", and its commentary is
    "Line 2 keeps the minus sign outside the radical throughout, which is the tidy
    way to handle an odd index over a negative radicand." `SR_PRESETS["simplify"]`
    offers `cbrt(54)`. The faded `√108` and the `standard`'s `√180` and cube root
    of `−250` are absent too, so of the lesson's six named radicals the selector
    reaches two.
14. `scientific-notation`'s presets track the `body`'s four math blocks exactly
    (`(3×10⁸)(2×10⁻³)`, `(9.9×10³)/(2×10²)`, `1.2×10⁵ + 3.4×10⁴`,
    `(5×10⁻⁷)(2×10⁻³)`) and miss both calculations of the `worked` panel and its
    faded item. The worked panel is the only place the lesson shows renormalising
    in both directions, which is what the panel's "the normalisation line
    identifies whether the mantissa or the power-of-ten arithmetic caused a
    mismatch" is for.

### Quiz feedback that does not answer the wrong answer

15. The `why` field is one string per question, and the course's own standard —
    set by its best explanations — is that every distractor is named and given
    the operation that produced it. `combining-like-terms` question 1 meets it
    (`2x² + 2x` "loses that invisible `1`", `8x² + 3x` "adds `5` and `3` instead
    of subtracting", `2x⁴` "adds the exponents"); so do `absolute-value`
    question 2 and `integer-exponents` questions 1–3. Where the standard is not
    met:
    - `order-of-operations` q3 (item 5) and `evaluating-expressions` q1 and q2
      (items 6 and 7) give wrong derivations.
    - `scientific-notation` q3 never mentions `1.05 × 10⁻⁵`, one of its four
      options.
    - `real-numbers-and-the-number-line` q3 never separates "Finitely many" from
      "Infinitely many"; "without end" is the rule restated, not a reason why a
      finite answer fails.
    - `the-distributive-law` q2 gives three descriptions for three distractors
      with no mapping: "The other options change one sign, change the wrong sign,
      or ignore the outside factor entirely." A reader who chose `2x − 9` cannot
      tell which clause is theirs.
    - `rational-exponents` q3 explains the correct answer and never addresses
      "`x^(1/2) = x/2`" or "`x^(1/2)` and `2^x` are two notations for the same
      thing", both of which are named misconceptions elsewhere on the page.
16. **`the-distributive-law` question 2 and several others identify distractors
    by position on a page that never numbers them.** `common.py`'s `QUIZ_SCRIPT`
    renders each option as `<button class="choice">` with `b.innerHTML = text` and
    no index, and `theme.py`'s `.choice-grid` adds no counter or `::before`. The
    options do stack in source order, so "the first option" is countable, but the
    reader has to count, and every other explanation in the course names the value
    instead. Course 1 carries three of these; courses 2 and 3 carry many more, and
    the worst instance in the path is `parallel-and-perpendicular-lines`'
    "Option 2 … option 4".

### Cognitive load and structure

17. **The quiz and the worked example are rendered as the two cells of one
    `grid-2`, so a faded rehearsal is on screen beside the question it was
    supposed to precede.** `render.py`'s `#practice` section emits
    `labs.QUIZ_MARKUP` and the worked panel — `worked.lines` plus every paragraph
    of `worked.after` — inside a single `<div class="grid-2">`. The first pass
    added a faded rehearsal to every lesson's `worked.after` and separately
    replaced repeated quiz items. In four lessons the two collided:
    - `order-of-operations`: the faded item is `18 / 3 / 2 + (−2)²` with "The
      queue gives `18 / 3 = 6`, then `6 / 2 = 3`" spelled out, and question 1 is
      "Evaluate `18 / 3 / 2`".
    - `the-distributive-law`: the faded item is `−3(2x − 5)` with "The expansion
      is `−6x + 15`", and question 1 is "Expand `−3(2x − 5)`", answer `−6x + 15`.
      The faded commentary even pre-diagnoses the same two distractors.
    - `translating-words-into-algebra`: the faded item is "three times the
      difference of `n` and 4" → `3(n − 4)`, with `3n − 4` named as the rival;
      question 2 is that phrase and those two options.
    - `algebraic-expressions-and-terms`: all three questions are answered in the
      worked table beside them — "`4xy − y² + 2` has three terms" (`example` and
      `worked`), "term 1 `−x` coefficient `−1`" and "as written ONE term … expanded
      `5x + 10`, TWO terms", the last of which is option (c) almost word for word.
    Two further questions are verbatim `body` lines: `roots-and-radicals` q1
    (`√16 = 4`, in the `example`) and q3 ("the 4th root of −16 = no real value",
    in the math block), and `evaluating-expressions` q3 (`1/(x − 2)` at `x = 2`,
    in the math block). This is the first pass's own finding 10 reappearing in a
    new place: the repair moved recognition from "the quiz repeats the worked
    example" to "the quiz repeats the faded rehearsal", and the page layout puts
    the two side by side.
18. **`scientific-notation` carries six acts on one page.** The normalised form;
    converting into it; converting out; multiplication; division; renormalising in
    both directions; addition with a shared power. The `standard` measures four.
    It is the strongest split candidate in the course, and the cheapest cut is the
    addition section: it is three lines of `body`, its own math block and its own
    `mistakes[2]`, and nothing later on the Algebra path adds in scientific
    notation — `integer-exponents` does not, and Exponential and Logarithmic
    Functions uses the exponent, not the mantissa. Recorded as a judgement; a
    split changes the URL space and needs `@site-architect`.
19. **The course outcomes name four acts and absolute value is not one of them.**
    `__init__.py`'s `outcomes` are: evaluate without ambiguity; name the property;
    simplify powers and radicals under their conditions; turn a sentence into an
    expression. `absolute-value` is a full lesson, it is the page Linear Equations
    and Inequalities lessons 11 and 12 are built on (`absolute-value-equations`'
    `concepts[0]` cites it by name), and `roots-and-radicals` needs it for
    `√(x²) = |x|`. A reader reading the course home to decide whether to take the
    course is not told the course teaches it.
20. `real-numbers-and-the-number-line`'s replacement of the `√2` contradiction
    proof by the whole-number-root theorem holds up: the theorem is stated, the
    proof is explicitly deferred ("neither is a prerequisite for this course"),
    and the completion act is the classification. The first pass's finding 3 is
    discharged. So is finding 8: `rational-exponents` `concepts[2]` now
    distinguishes `x ≥ 0` from `x > 0` and the `def` says "At `x = 0` that
    reciprocal has no value."

## Where a learner gets stuck

- At `properties-of-the-real-numbers`, told to disprove a rule by substituting
  small numbers, with no instruction that the value goes in brackets and with
  `order-of-operations` two pages back having just shown that `−3²` is `−9`
  (item 2). The same reader meets `√13` on the same page (item 1).
- At `scientific-notation`'s concept card, holding a rule that compares by
  exponent first, on a page whose definition admits `−8.3 × 10⁻⁵` (item 4).
- At `evaluating-expressions` question 2, having made exactly the error the
  lesson exists to prevent and being told they made a different one (item 6); and
  at question 1, having chosen `3` and being given the explanation for `−17`
  (item 7).
- At `absolute-value`'s faded rehearsal, looking through six presets for the one
  with `a = −6` (item 10).
- At `properties-of-the-real-numbers`' lab, having predicted a row and watched
  every false claim fail on the default numbers, with nothing in the panel
  saying that `(4, 4, 4)` and `(1, 1, 1)` are where the promised thing happens
  (item 11).
- At `algebraic-expressions-and-terms`' quiz, able to score three out of three by
  reading the column beside it (item 17).

## What the first pass caught, what it missed, and what I dispute

The prior assessment's structural verdict was right and its repairs are live and
verified here: the reorder is coherent in both directions (item under *What the
course teaches well*), the `scientific-notation` magnitude rewrite landed
everywhere but one concept card, the `rational-exponents` domain split landed,
the `roots-and-radicals` prime-factorisation procedure is now on the page
("divide by the smallest prime that works until the quotient is `1`"), and the
`√(1/2)` text-versus-lab disagreement is resolved in the text's favour with the
general method deferred to Rational and Radical Expressions.

**What it missed.** Three things, all of which needed the audits it did not run.
It did not try to argue for each wrong answer, so it did not find that three
`why` fields name errors that produce a different number (items 5, 6, 7) — and
item 6 is the lesson's own headline misconception. It did not read the lab preset
lists against the lesson text, so it did not find the preset that does not exist
(item 10), the panel whose promise the default preset cannot keep (item 11), or
the three labs that open on data the lesson never uses (items 12, 13, 14). And it
did not read `render.py`, so it did not notice that the faded rehearsals it added
render in the column beside the quiz, which is what turned its own finding 10
into item 17.

**What I dispute.** The first pass's repair list says of
`order-of-operations` that "all three quiz questions and the completion task use
new expressions rather than the page's trap strings", and of
`translating-words-into-algebra` that "The faded and quiz phrases are new". Both
are true relative to the *body*, and both are false relative to the faded
rehearsal the same commit introduced (item 17). The claim was checked against the
wrong half of the page.

I also dispute its finding 6 in part. It said `absolute-value`'s lab "solved
`|x − a| = c` by cases before course 2's equation method" and that "the panel
failed to say which figures were the present lesson's retrieval and which were
previews". The panel now fences `√(a²)` correctly. But the case-split solve is
not a preview and never was: `absolute-value`'s own `body` derives the two
solutions from the definition, its `standard` requires them, and its closing note
says Linear Equations and Inequalities "supplies the general equation method; it
assumes the meaning of the bars is automatic". The lab is teaching this lesson's
content, not course 2's, and the first pass's framing of it as a preview was
wrong. What the panel does omit is the two rows it never mentions —
`|a + b|` against `|a| + |b|` and `|ab|` against `|a||b|` — which *are* this
lesson's `body`, and are the only figures on the lab the panel leaves unclaimed.

## Repairs this pass recommends

None of these changes the URL space, so the five declarations in root `AGENTS.md`
§1 are untouched. Every edit named is in `content/algebra/c1_foundations/` unless
a lab source is named; after any of them, `python3 scripts/build_paths.py` and the
gate set in `AGENTS.md` §7 must run, with `/usr/bin/python3`.

1. `scientific-notation`, `concepts[0]` (item 4). Restate the comparison rule in
   magnitude and say what it costs when the sign is negative. Suggested body:
   compare magnitudes by exponent first and mantissa on a tie, then note that for
   two negative numbers the order on the line is the reverse of the order of
   their magnitudes, with `−8.9 × 10⁻⁵ > −1.2 × 10⁻⁴` as the instance. Keep
   question 3 as it is; its four options are all positive and it tests the
   magnitude rule correctly.
2. `evaluating-expressions`, `quiz[1].why` (item 6). Replace the clause about
   `18` with the real derivation: `18` is `−2 · (−3²)`, the substitution made
   without brackets, which reads `(−3)²` as `−9`. That is `mistakes[0]`, and
   naming it here is the whole point of offering the distractor.
3. `evaluating-expressions`, `quiz[0]` (item 7). `3` is unreachable. Replace the
   option with `−9`, which is `3(−3²) + 2(−2) − 1` — the unbracketed square with
   the linear sign kept — and rewrite the `why` so `−17` keeps "squares without
   brackets", `−9` gets "squares without brackets and then keeps the sign of the
   linear term", and `15` keeps "drops the sign from the linear term". Do not
   leave two options sharing one diagnosis.
4. `order-of-operations`, `quiz[2].why` (item 5). Change "`16` adds first" to the
   operation that produces it: `18 / 3 = 6`, then `2 + 6 = 8`, then `8 · 2 = 16` —
   the addition level taken before the multiplication that was still queued at
   level 3. Adding first, `(2 + 18)/3 · 2`, gives `40/3` and is not on the list.
5. `properties-of-the-real-numbers`, `body` `ul` (item 1). Replace the
   `√(a + b) = √a + √b` bullet with a disproof that uses only arithmetic the
   reader has at lesson 4 — `(a + b)² = a² + b²` at `a = 1, b = 3` (`16` against
   `10`) is the natural one, and it is the shape `the-distributive-law` and
   `integer-exponents` both reuse. The radical version belongs in
   `roots-and-radicals`, where it already appears.
6. `properties-of-the-real-numbers`, `steps[3]`, and `the-distributive-law`,
   `steps[3]` (item 2). Add one sentence to each: write the substituted value in
   brackets, because `order-of-operations` showed that `−3²` and `(−3)²` are
   different strings. A cross-reference to `evaluating-expressions` as the lesson
   that makes this a method is enough; no new content is needed.
7. `absolute-value`, `worked.after[2]` (item 10). Either change the faded values
   to `a = −4, b = 6`, which is the shipped default preset — `|−4| = 4` and
   `|−4 − 6| = 10` — or change "the matching lab preset" to "the lab, with `a`
   and `b` typed in". The second is the smaller edit and keeps the numbers the
   sentence already computes.
8. `absolute-value`, `lab.panel_intro` (dispute section). Add a clause claiming
   the two fact rows the lab prints and the lesson teaches: `|a + b|` against
   `|a| + |b|`, where the lab reports "equal" or "less" and never "greater", and
   `|ab|` against `|a||b|`, which is always equal. Both are in `body`; neither is
   in the panel.
9. `properties-of-the-real-numbers`, `lab.panel_intro` (item 11). Name the two
   presets where a false claim survives: `a = b = c = 4`, where subtraction and
   division both look commutative, and `a = b = c = 1`, where four of the claims
   hold. The current sentence promises the experience without saying where it is.
10. `real-numbers-and-the-number-line`, `lab.panel_intro` (item 12). Point the
    reader at the ordering act first — type the worked example's six values, read
    the "Distinct places" column, then compare with the `standard`'s list — and
    keep the three-spellings preset as the second sentence rather than the first.
11. `roots-and-radicals`, lab presets (item 13). Add `cbrt(-54)` and `sqrt(108)`
    to `SR_PRESETS["simplify"]` in `scripts/mathpath/labs/algebra_basics.py`, or
    override the presets from the lesson dict the way `domain-and-range` does in
    course 3 — `lab: ("radicals", {"mode": "simplify", "presets": [...]})` is
    already supported by `radicals_lab`'s `cfg.get("presets")`. The negative
    radicand under an odd index is the one shape the current list cannot show.
12. `scientific-notation`, lab presets (item 14). Add `(6.4 × 10⁵)(5 × 10⁻⁸)` and
    `(1.5 × 10³)/(6 × 10⁷)` — the worked example's two calculations, one
    renormalising up and one down — by overriding `presets` from the lesson dict.
13. The four faded-versus-quiz collisions (item 17). In each case change the
    *quiz* item, not the faded one, since the faded rehearsal is the scarcer
    thing: `order-of-operations` q1 to a new left-to-right division string such as
    `36 / 6 / 3`; `the-distributive-law` q1 to a new expansion such as
    `−5(3x − 2)`; `translating-words-into-algebra` q2 to a new packaged phrase
    such as "five times the difference of `n` and 3"; and all three
    `algebraic-expressions-and-terms` questions to expressions not in its worked
    table — the `mistakes[2]` expression `−x + (2/3)x² − 5` is also in the worked
    table, so a genuinely new one is needed, for example `7 − 2ab + b²`. Also
    replace `roots-and-radicals` q1 and q3 and `evaluating-expressions` q3, each
    of which is a `body` line verbatim.
14. All ordinal references in `why` fields (item 16). Replace "the first option",
    "the other options" and similar with the option's own value or phrase:
    `the-distributive-law` q2 should say which of `−2x + 9`, `2x − 9` and
    `2x + 9` did what; `algebraic-expressions-and-terms` q3 should name the
    option rather than call it "the fourth". The page never numbers the buttons.
15. `__init__.py`, `outcomes` (item 19). Add a fifth outcome naming the absolute
    value act — read `|x|` from the two-case definition, measure a distance as
    `|a − b|`, and reject `|X| = c` for negative `c` on sight — and say in it
    that Linear Equations and Inequalities assumes all three.
16. `scientific-notation` (item 18). Not recommended for this pass. A split
    changes the URL space and all five declarations; if it is ever taken, the cut
    is between "Multiplying and dividing" and "Adding", and the addition section
    plus `mistakes[2]` is the material that moves. Consult `@site-architect`
    before any of it.
