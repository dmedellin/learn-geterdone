# Pedagogy assessment — Discrete Probability (discrete mathematics, course 5)

First assessment, formed from the twelve lesson dicts in
`content/discrete_math/c5_probability/` (`part_a.py`, `part_b.py`,
`__init__.py`) and the lab kit they render through,
`scripts/mathpath/labs/probability.py` (the sample-space lab with its four
experiments, and the distribution lab with its four distributions), as they
stand on `main` at 6236a44. No prior assessment exists for this course.

This is a generated course: the source is the content package, and every
finding below cites a lesson slug and the field it lives in. Lessons, in
course order: `sample-spaces-and-events`, `computing-probabilities`,
`probability-axioms`, `conditional-probability`, `independence`,
`bayes-theorem`, `random-variables`, `expected-value`,
`linearity-of-expectation`, `variance`, `binomial-distribution`,
`geometric-distribution`. The course declares courses 1–4 as prerequisites
("counting, sets and functions"), so it is judged against what those teach:
proof by cases and its two obligations (course 1 lesson 14), set operations
and De Morgan (course 2 lessons 3 and 4), functions as rules on a domain
(course 2 lesson 10), the plain pigeonhole principle with its 367-people
example (course 2 lesson 14), the geometric series `Σ arⁱ` (course 3 lesson
3), complementary counting for "at least one" (course 4 lessons 1 and 2),
`C(n, r)` (course 4 lesson 4), Vandermonde (course 4 lesson 5), the binomial
theorem (course 4 lesson 6), inclusion–exclusion (course 4 lesson 9) and the
derangement numbers (course 4 lesson 10). Every one of those pointers was
checked against the lesson it names and every one resolves. Every figure
quoted below was recomputed in exact arithmetic (`fractions.Fraction`), and
every lab figure by executing the shipped JavaScript at the shipped preset.

## What the course teaches well

- **Every lesson closes on an act, and the act is the right one.** Write the
  sample space before computing (`sample-spaces-and-events`); check an
  answer against a complementary count (`computing-probabilities`); derive
  a rule from the axioms rather than recall it (`probability-axioms`);
  state the restricted sample space (`conditional-probability`); check the
  equation rather than the story (`independence`); do the calculation both
  ways (`bayes-theorem`); build a distribution from a sample space unaided
  (`random-variables`); compute an expectation and say what it does not
  claim (`expected-value`); reach for indicators first
  (`linearity-of-expectation`); say why averaging reduces spread by `√n`
  (`variance`); check the three assumptions first
  (`binomial-distribution`). None is "understand X".
- **The course is built around one diagnosis and repeats it until it
  sticks:** almost every wrong answer is a right calculation on the wrong
  sample space, or of the wrong conditional. `sample-spaces-and-events`'
  summary says most mistakes are "about what the outcomes are"; its body
  names Cardano's error; `computing-probabilities` Q1 refutes `1/11` by
  naming the coarse space; `conditional-probability`'s two-child worked
  example gets `1/3` and `1/2` from the same family by restricting to sets
  of different sizes; `bayes-theorem` does the medical test by the formula
  and again by counting 100 000 people and says to do both every time. The
  sample-space lab draws every outcome as a chip, keeps every probability an
  exact fraction, and its status line states conditioning as "not a new
  rule, a smaller sample space" on every page that carries it.
- **Disjoint is not independent is said three times, spaced, and each time
  from a different angle:** as a property of sets not sizes
  (`sample-spaces-and-events`, worked `after` and mistake 3), as a
  consequence of the axioms (`probability-axioms`, mistake 2), and as the
  arithmetic `P(A ∩ B) = 0 ≠ P(A)P(B)` (`independence`, body and Q1). The
  same is done for `P(A|B) ≠ P(B|A)` (`conditional-probability`, then
  `bayes-theorem`) and for "the mean is not the likely value"
  (`expected-value`, `binomial-distribution`'s `8%` at `n = 100`,
  `geometric-distribution`'s mode at 1).
- **The proofs are right and they are the explanatory ones.** The six
  consequences of the axioms, with inclusion–exclusion derived by splitting
  into three disjoint pieces and the union bound falling out of it; the
  conditional probability is itself a probability; the multiplication rule
  chained; complements preserve independence; the two-coin triple that is
  pairwise but not mutually independent, with "any two determine the third"
  as the reason; total probability from a partition; Bayes from two
  expressions for `P(A ∩ B)`; linearity by summing over outcomes, with
  "nothing about the joint behaviour entered" as the whole point; `E[I_A] =
  P(A)`; the computational variance formula; `σ²/n`; the binomial mass by
  "one sequence, then count the sequences", summing to 1 by the binomial
  theorem "doing genuine work, not an analogy"; the geometric mass summing
  to 1 by course 3's series; memorylessness as a two-line ratio.
- **The misconceptions named are the real ones, at the point of error.**
  Sums of dice as outcomes; `|S|` in the denominator of a conditional;
  reading the sensitivity as the answer; omitting the false-positive branch;
  treating `X` as random rather than as a function; `E[g(X)]` as `g(E[X])`;
  checking independence before adding, and applying linearity to a product;
  `(E[X])²` for `E[X²]`; the binomial for sampling without replacement; the
  gambler's fallacy stated as a theorem about the model.
- **The numbers are right.** `671/1296`, the birthday table, `103 776 /
  2 598 960` and its Vandermonde check summing to `2 598 960`, `3/5` for the
  loaded die, `1/221`, `0.0194` and `99/5094`, `0.895`, `91/6`, `−1/37`,
  `£10.00`, `35/12`, `35/6`, `35/3`, `0.2023`, `0.0139`, `2.6σ`, `0.08`,
  `(5/6)^k` at 3, 6, 12 and 20, `σ ≈ 5.48`, `50·H₅₀ ≈ 225` — all recomputed
  and all correct.

## What it teaches badly, or claims and does not deliver

### Facts a reader would trust that are wrong

1. **`random-variables`' `math` block for the sum of two dice is garbled.**
   Its first row, labelled `k`, reads `2 3 4 5 6 7 6 5 4 3 2`, and the
   caption under it says "counts of ordered pairs summing to k+1 … (k = 2 …
   12)". Neither row is the values (`2 … 12`) nor the counts (`1 2 3 4 5 6 5
   4 3 2 1`); the row is the counts plus one, and the caption describes
   nothing on the page. The `example` above it states the triangle
   correctly, so the table contradicts the sentence it is meant to
   illustrate.
2. **`geometric-distribution`'s lab reports the definition and the closed
   form disagreeing.** The distribution lab sums the first 30 terms.
   Executed: at the shipped `p = 6/12` the sum is `2.0000 = 1/p`, but at the
   lesson's own `p = 1/6` it reads "Summed from the definition: E[X] =
   5.8483" beside "1/p = 12/2 = 6", and at `p = 1/12` it reads `8.9126`
   against `12`. The status line explains the truncation for the total
   (`0.9958`) and says nothing about `E[X]`, so on the lesson whose
   `footer_lead` promises the distributions are "summed term by term from
   their definitions and compared with the closed forms", the comparison
   fails on the lesson's own example and the page does not say why.
3. `linearity-of-expectation`'s standard says the run-start indicators
   "overlap heavily". They do not overlap at all — each is one position —
   and only adjacent pairs are dependent (a run cannot start at two
   consecutive positions). The number `(n + 1)/4` is right; the sentence
   sends the reader looking for an overlap that is not there.

### Order: things used before they are taught

4. **`random-variables`' lab shows `E[X] summed`, `E[X] formula` and
   `Var(X)` as its three figures**, and its own `panel_intro` speaks of each
   row's "contributions to the expectation", one lesson before
   `expected-value` defines expectation and three before `variance`.
5. **`expected-value` renders "Binomial(n = 10, p = 6/12)"** with the closed
   form `np` beside the sum — lesson 11's distribution and lesson 9's
   result — while the lesson's own example, the fair die with `E[X] = 3.5`
   "not a value the die can show", is one control away (Uniform on `1 … 6`).
6. **`variance` states `Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y)`** and
   `Cov` is defined nowhere on the path.
7. `geometric-distribution` proves `E[X] = 1/p` by "`E[X] = p·1 + (1−p)(1 +
   E[X])`". The step is right, and it conditions an expectation, which the
   course has never defined or justified; a reader who asks why an
   expectation splits over the first trial the way a probability does is
   not answered. One line makes it a computation from the definition:
   `P(X = k) = (1−p)·P(X = k−1)` for `k ≥ 2`, substituted into `Σ k·P(X = k)`.
8. Pointers a reader would follow that stop short. `linearity-of-
   expectation` says "without computing the binomial distribution at all"
   two lessons before the binomial is defined; `computing-probabilities`
   cites "the pigeonhole statement in course 2" with no lesson (14);
   `sample-spaces-and-events` says the conditions "are the same a proof by
   cases needs" without naming course 1 lesson 14; `random-variables` says
   a random variable is a function without pointing at course 2 lesson 10,
   the one prerequisite its whole framing rests on.

### Labs that do not agree with their own lessons

9. **`sample-spaces-and-events` renders four coins with A = exactly two
   heads and B = the first flip is heads.** Executed: `P(A|B) = 3/8`, and
   the status line reports that A and B are *independent* (`3/16 = 6/16 ·
   8/16`) — conditioning and independence are lessons 4 and 5, and the
   panel says nothing about which events are on the screen. The lesson's
   worked example is two dice with "sum is 7", "a double" and "first die
   4", and all three are events in the lab's dice experiment.
10. **`independence`'s lab cannot reproduce the lesson's example.** The
    preset is A = sum is 7, B = the first die is 4, which is independent
    (`1/36 = (1/6)(1/6)`) and surprising, but the lesson's own "independent,
    surprisingly" pair — first die even, sum 7 — is not available, because
    the dice experiment has no "first die is even" event.
11. **`bayes-theorem` has no lab that does Bayes.** The urn with A = both red,
    B = no blue shows `P(A|B) = 1/2` and `P(B|A) = 1`, which is lesson 4's
    point, not this one's. Nothing on the page has a prior, a sensitivity or
    a false-positive rate; the medical test the course home names as
    outcome 3 and its `how_to` says to do "by frequencies as well as by the
    formula" is computed by no lab. The panel says "the status line
    confirms that both routes to `P(A ∩ B)` agree, which is Bayes"; that is
    the multiplication rule, and the lab prints it on every page.
12. **`variance` renders the uniform on `1 … 10`**, whose variance `8.25`
    appears nowhere in the lesson. The lesson's figures are `35/12` for one
    die and `35/6` for two independent dice — the worked example — and the
    lab has both ("Uniform on `1 … 6`" and "Sum of two fair dice", whose
    `Var = 35/6` summed over the eleven sums is the worked example's number
    by a different route).
13. **`binomial-distribution` renders `n = 10`, `p = 1/2`** under a worked
    example at `n = 20`, `p = 1/4` (`P(X = 5) = 0.2023`, `E = 5`, `Var =
    3.75`, `P(X ≥ 10) = 0.0139`). The table also stops at 14 rows, so at
    `n = 20` the rows `k = 14 … 20` a reader would sum for "at least 10" are
    not on the page.
14. **`geometric-distribution` renders `p = 6/12`** (`E[X] = 2`) under a
    worked example at `p = 1/6` (`E[X] = 6`), with a panel saying the mean
    line "sits well to the right"; at `p = 1/2` it sits on the second bar.
15. The panels on `computing-probabilities`, `probability-axioms`,
    `conditional-probability` and `linearity-of-expectation` describe the
    lab correctly and quote none of its figures, so the reader is not told
    what to look for. Executed at the shipped presets: 66 two-card hands
    from the 12-card deck, "at least one A" in `21 = 66 − C(10,2)` of them —
    the complement rule on the screen — and "a pair" in `6/66 = 1/11`; in
    the urn, "both red" (`3/15`) is contained in "no blue" (`6/15`), which
    is monotonicity on the screen; `P(sum is 7 | first die is 4) = 1/6` is
    the lesson's own dice example, and B = "at least one 6" gives `2/11`
    against `P(B|A) = 1/3`; `5.0000 = 10 · 6/12`.

### Practice that repeats the lesson

16. **`geometric-distribution`'s standard is the body's proof.** "Derive
    `E[X] = 1/p` by conditioning: with probability `p` you finish
    immediately, otherwise you have used one trial and face the same
    problem" — that sentence is the proof block three screens up, and the
    lesson says "that technique solves waiting-time problems where no
    series is available" without ever posing one.

### Distractors that are also true, and feedback that does not answer

17. **`sample-spaces-and-events` Q3: "mutually exclusive, meaning: exactly
    one of them occurs."** That is exclusivity *and* exhaustiveness
    together, and the `why` says so; exclusive alone is "no two together".
    The marked-correct option is the conjunction the question did not ask
    about.
18. **`probability-axioms` Q1 offers "`P(A) + P(B) ≤ 1`" as a wrong answer
    to "`P(A ∪ B) = P(A) + P(B)` requires:"**. If the equation holds then
    `P(A) + P(B) = P(A ∪ B) ≤ 1`, so the condition is genuinely required
    (necessary, not sufficient); a reader can argue for it and is marked
    wrong.
19. **`binomial-distribution` Q3 offers "binomial with `p = 4/52`" and
    "binomial with `p = 1/13`"**, the same number; the reader who holds the
    misconception has to choose between two identical models.
20. Of the 36 `why` fields, almost all restate the rule and name no
    distractor. The reader who chose `20` for the geometric mean at `p =
    0.2` is not told that `20` is the variance `0.8/0.04`; who chose `95%`
    for the medical test is not told it is `1 − FPR`, a property of the
    test; who chose `7/36` or `1/12` for the sum of 7; `4/16` for at least
    one head; `9Var(X) + 25` for `Var(3X + 5)`; `1/16` for `P(A∩B)` in the
    coin example; `n/2` or `1/n` for the fixed points; `2.1` for `E[X]`
    with `n = 10`, `p = 0.3` (that is `np(1−p)`); `4/51` for the second ace;
    `1/2` for Monty Hall — none is answered.

### Misconceptions not named

21. **`computing-probabilities` never names the classic wrong answer to its
    own example.** "At least one six in four rolls" invites `4 × 1/6 = 2/3`
    — adding four overlapping events — and with six dice the same reasoning
    gives `1`. The lesson's method (`1 − (5/6)⁴`) is right and the trap it
    replaces is unmentioned; it is lesson 3's union bound read as an
    equality, and saying so would connect the two lessons.
22. **`variance`'s worked example has the number for "add the standard
    deviations" and does not say it.** `σ(X) + σ(Y) = 1.708 + 1.708 =
    3.416`, which is exactly `σ(2X)` — the totally dependent case — while
    the independent sum has `σ = 2.415`. Adding standard deviations is the
    commonest spread error in applied work and it lands on the wrong line
    of the lesson's own table.
23. `independence` does not say what the union of independent events is.
    "Independent so the probabilities add" is the add/multiply confusion,
    and `P(A ∪ B) = P(A) + P(B) − P(A)P(B)` is one line from the lesson's
    definition and lesson 3's inclusion–exclusion.

### Cognitive load and structure

24. `variance` carries six theorems: the definition, the computational
    formula, scaling, the sum rule, the variance of an average, and
    Chebyshev. I have chosen not to split it: the idea is one (spread), the
    key block and the standard confine themselves to the definition and the
    `√n`, and the last two theorems are the "mentioned where they explain
    something" the course home's `not_covered` promises for the law of
    large numbers. What was wrong was `Cov` appearing undefined (item 6),
    which one sentence repairs.
25. The course home lists four outcomes and omits the acts lessons 7, 9,
    11 and 12 close on — build a distribution from a sample space, decompose
    a count into indicators, check the three binomial assumptions, tell a
    fixed-trials question from a fixed-target one — though `syllabus_intro`
    gives those lessons half the course.
26. The course home's `how_to` says to do the Bayes calculation "by
    frequencies as well as by the formula" and names nothing on the site
    that does it (item 11).

## Where a learner gets stuck

- At `random-variables`' table, trying to read `2 3 4 5 6 7 6 5 4 3 2` as
  either values or counts (item 1).
- At `expected-value`'s lab, meeting "Binomial(n = 10, p = 6/12)" and `np`
  with no definition of either (item 5); and at `random-variables`' lab,
  being told to read "contributions to the expectation" (item 4).
- At `variance`'s sum rule, meeting `Cov` (item 6).
- At `geometric-distribution`'s lab, setting `p = 2/12` to match the worked
  example and reading `5.8483` against `6` (item 2); and at its standard,
  being asked to reproduce the proof on the page (item 16).
- At `bayes-theorem`'s lab, looking for the prior (item 11).
- At `independence`'s lab, looking for "the first die is even" (item 10).
- At `probability-axioms` Q1, having answered with a condition that is
  genuinely necessary (item 18).

## Repairs made in this pass

All within the existing URL space; no lesson added, removed, renamed or
reordered, so the five URL declarations are untouched. Every content edit is
in `content/discrete_math/c5_probability/` and the twelve pages under the
slug are rebuilt from it. Three changes are in lab core,
`scripts/mathpath/labs/probability.py`, and one page uses a lab that did not
exist: a `bayes` lab, registered in `scripts/mathpath/labs/__init__.py`. The
arithmetic behind all three probability labs (`FRACTION_JS`, the new
`DIST_JS` with the four mass functions and the moment sums, and the new
`BAYES_JS`) is now exercised by a probability section in
`scripts/mathcheck.js`, which was shown to fail when the geometric tail
was cut at 30 terms and passes with the sum run out. Every figure a panel
now states was obtained by executing the shipped lab JavaScript at the
shipped preset.

Lab core:

- The sample-space lab takes `a` and `b` (event indices) in its config, and
  the dice experiment gains "the first die is even" as its last event so
  no other page's preset moves.
- The distribution lab takes `n` and `p` (twelfths) in its config; sums the
  geometric until the remaining tail is below `10⁻¹⁵` (executed: `E[X] =
  6.0000` and `Var = 30.0000` at `p = 1/6`, `12.0000` and `132.0000` at `p =
  1/12`) while drawing the first 30 bars, and says in the status line what
  the bars omit; shows up to 21 table rows so every binomial row at `n ≤
  20` is on the page; and its mass functions and moment sums are factored
  into `DIST_JS` so `mathcheck.js` can execute them.
- A `bayes` lab: prevalence (six settings from 30 in 100 to 1 in 10 000),
  sensitivity and false-positive rate as controls; a population of
  1 000 000 split into the four cells in whole numbers; the positives drawn
  as a bar with the true positives' share visible; `P(D | +)` as an exact
  fraction from the counts and again by the formula with the
  total-probability denominator expanded; the false-to-true positive ratio;
  and `P(no disease | −)` so the reader sees a negative result is
  informative when a positive one is not. Executed at the shipped preset
  (1 in 1000, 99%, 5%): `1000 / 990 / 50 / 999 000 / 49 950`, `P(D|+) =
  990/50940 = 11/566 ≈ 1.94%`, `50.5` false positives per true one,
  `P(D̄|−) = 949 050 / 949 060 ≈ 99.999%`.

Lessons:

- `sample-spaces-and-events`: the lab is the dice experiment with A = sum is
  7 and B = a double (`A ∩ B = ∅`, the worked example's first intersection),
  the panel fences the conditional rows as lessons 4 and 5's and sends the
  reader to B = the first die is 4 to find `(4,3)`; Q3's correct option is
  "no two of them can occur together" with the `why` separating exclusive
  from exhaustive; the body names course 1 lesson 14; every `why` answers
  each distractor.
- `computing-probabilities`: the four-dice example names `4 × 1/6 = 2/3` as
  the wrong answer and why (with six dice it gives 1), and points at lesson
  3's union bound; the pigeonhole pointer says lesson 14; the panel reads
  `21 = 66 − 45` and `6/66 = 1/11` off the lab; every `why` answers each
  distractor.
- `probability-axioms`: Q1's fourth option is `P(A) = P(B)`; the panel reads
  `3/15 ≤ 6/15` as monotonicity and names the disjoint pair for A3; every
  `why` answers each distractor.
- `conditional-probability`: the panel says the preset is the lesson's dice
  example and sends the reader to B = at least one 6 (`2/11` against `1/3`,
  same numerator `2/36`); every `why` answers each distractor, including
  the random-host `1/2`.
- `independence`: the lab is A = the first die is even, B = sum is 7 — the
  lesson's own surprising pair, `3/36 = (1/2)(1/6)` — and the panel sends
  the reader to B = at least one 6 for a dependent pair (`8/36` against
  `11/72`); a paragraph after the disjoint section gives `P(A ∪ B)` for
  independent events; every `why` answers each distractor.
- `bayes-theorem`: the lab is the new Bayes lab at the lesson's numbers; the
  panel says what the four cells are and where the `2%` comes from; the
  standard's self-check gives `190` true positives against `980` false;
  every `why` answers each distractor, including `95%` as `1 − FPR`.
- `random-variables`: the table has three rows — `k`, the count, `P(X = k)`
  — and a sum line; the body points at course 2 lesson 10; the panel
  fences `E[X]` and `Var(X)` as lessons 8 and 10's and reads the triangle
  and the `Σ = 1` row; every `why` answers each distractor.
- `expected-value`: the lab is the uniform on `1 … 6` — the fair die — with
  the panel reading `3.5` as summed, "not in the `k` column", and the dashed
  line between the bars for 3 and 4; the `Var` figure fenced as lesson
  10's; every `why` answers each distractor.
- `linearity-of-expectation`: "the binomial distribution" says "lesson
  11's"; the standard says adjacent indicators are dependent rather than
  overlapping; the panel reads `5.0000 = 10 · 6/12` and asks for `n` to be
  moved; every `why` answers each distractor.
- `variance`: `Cov(X, Y) = E[XY] − E[X]E[Y]` defined in one line where it is
  used, with lesson 9's product rule making it 0 for independent variables;
  the worked example's `after` names `1.708 + 1.708 = 3.416 = σ(2X)` as the
  add-the-deviations error landing on the dependent line; the lab is the
  sum of two dice (`Var = 35/6 = 5.8333`, the worked example's independent
  sum by a second route) and the panel sends the reader to Uniform on `1 …
  6` for `35/12`; every `why` answers each distractor.
- `binomial-distribution`: the lab is `n = 20`, `p = 3/12`, the worked
  example, and the panel reads the `k = 5` row (`0.202331`) and says the
  rows `10 … 20` sum to `0.013864`; Q3's third option is "binomial, because
  each card is either an ace or not"; every `why` answers each distractor,
  with `2.1` identified as `np(1 − p)`.
- `geometric-distribution`: the proof of `E[X] = 1/p` gets the line that
  turns it into a computation from the definition; the lab is `p = 2/12`,
  the worked example, and the panel reads `0.166667` at `k = 1`, `0.066980`
  at `k = 6`, `6.0000` against `1/p` and `30.0000`; the standard is flips
  until two heads in a row, by conditioning on the first one or two flips,
  with `6` to check against; every `why` answers each distractor, with `20`
  identified as `Var(X)`.
- Course home (`__init__.py`): a fifth outcome names the acts of lessons 7,
  9, 11 and 12; `outcomes_intro` includes it; `how_to` names the Bayes lab
  as where the frequency calculation is done and says every distribution
  lab is preset to its lesson's worked example.
