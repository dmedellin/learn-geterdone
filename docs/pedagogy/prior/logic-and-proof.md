# Pedagogical assessment — Course 1, Logic and Proof (discrete-math path)

Assessed August 2026, against the full course: all 14 lessons read in the
content package (`content/discrete_math/c1_logic/`), plus the lab kit the
course renders through (`scripts/mathpath/labs/logic.py`,
`scripts/mathpath/labs/induction.py`). Verdicts on the quantifier lab were
checked by brute force over every 3×3 predicate grid, not by reading.

## What this course teaches well

The propositional half (lessons 1–7) is close to exemplary and was left
almost untouched.

- **Observable objectives throughout.** Every lesson carries a `standard`
  stating what the learner must be able to *do*, and they are genuinely
  behavioural: "produce all three relatives of a conditional and say which is
  equivalent, without a table" (`conditional-statements`), "settle a tautology
  claim by assuming it false" (`tautologies-and-satisfiability`), "name the
  fallacy AND produce its counterexample assignment" (`rules-of-inference`).
- **Worked examples fade correctly.** Each lesson runs
  definition → worked instance → adversarial lab → quiz with per-error
  feedback → a closing claim to prove or classify yourself. The
  worked-example → faded-guidance → independent-practice progression the rest
  of the path assumes is actually present here.
- **Misconceptions are named, not implied.** Inclusive-or
  (`logical-connectives`), vacuous truth (`conditional-statements`),
  `∧`-under-`∀` and `→`-under-`∃` (`predicates-and-quantifiers`), witness
  depending on the wrong variable (`nested-quantifiers`), "not all" vs "none"
  (`negating-quantified-statements`), affirming the consequent
  (`rules-of-inference`), the circular proof of "if n² is even then n is
  even" (`direct-proof`), sign-case gaps and fake WLOG
  (`proof-by-cases-and-counterexample`). Each is stated as the error a real
  learner makes, with the row or instance that exposes it.
- **The course closes its own loop.** Lesson 14's `prime41`/`chords` lab is a
  deliberately adversarial design: two false statements that survive every
  check a careful person would run. It is the correct capstone for a course
  whose thesis is that checking is not proving, and it hands off to course 3
  (induction) exactly where it should.
- **The prerequisite chain inside the course is sound.** Truth tables
  (lesson 3) precede equivalence (5); the conditional's relatives (4) precede
  both the fallacies (11) and contraposition as a method (13); negation of
  quantifiers (10) precedes counterexample hunting (14). Forward references
  ("lesson 13 makes this a method") are accurate. As course 1 of the path it
  may assume nothing, and it doesn't: `assumes_short` is "Nothing" and that
  is honest.

## What it taught badly — defects found and repaired

### 1. The quantifier lab evaluated the wrong statement and then lied about it (critical; `nested-quantifiers`, also rendered on `predicates-and-quantifiers` and `negating-quantified-statements`)

The lesson's theorem — correctly stated and correctly proved in the prose —
is `∃y ∀x P(x, y) ⟹ ∀x ∃y P(x, y)`. The lab's third verdict row, however,
computed `∃x ∀y P(x, y)` (a full **row** of the grid) while the status
messages talked about it as if it were the theorem's `∃y ∀x` (a full
**column**). Three concrete consequences, each verified by brute force over
all 512 3×3 grids:

- The status line "∃x∀y implies ∀x∃y always" is **false as displayed**: 42 of
  512 grids satisfy the row-form and refute the implication (e.g. a single
  full row with an empty row elsewhere). A learner probing the lab
  adversarially — which the course home explicitly tells them to do — could
  build a grid where the lab's own verdicts contradict its own explanation.
- The "stronger statement" message ("∀x∃y already fails, so ∃x∀y cannot hold
  either") was false for the same reason: the row-form can hold while ∀x∃y
  fails.
- Lesson 9's `succ` preset was advertised as "the classic separator — watch
  the two middle rows disagree." On the truncated universe {1..4} the top
  element has no successor, so `∀x ∃y` is **false** and the two middle rows
  agree (both F). The advertised separation never appears; the learner is
  told to watch for something the lab cannot show them.

**Repair.** The lab now evaluates and displays all six distinct forms —
`∀x∀y`, `∀x∃y`, `∃y∀x` (column), `∀y∃x`, `∃x∀y` (row), `∃x∃y` — each with
the witness or counterexample that decides it, so the theorem pair the
lesson proves is actually on screen, and the mirrored pair sits beside it
labelled as the reflection it is. The status logic now keys on the correct
pair. Lesson 9's default preset is `diag` (identity), which genuinely
separates `∀x∃y` (T) from `∃y∀x` (F); the prose turns the successor preset's
boundary failure into a retrieval opportunity — the truncated universe is
*why* `∀x ∃y` fails there, reinforcing lesson 8's note that finiteness is a
luxury. Lesson 10's preset moves to `le`, where the complement button
produces a dramatic, explainable collapse (five of six verdicts T → only
`∃x∃y` survives), and the panel now states the duality the learner should
check: after complementing, each verdict equals the negation of its dual's
old value.

### 2. Nothing checked the logic labs' arithmetic (structural)

`mathcheck.js` proved the *algebra* labs' arithmetic and nothing else; the
logic course's parser/evaluator (which seven lessons ride on) and the
quantifier evaluators (three lessons) were exactly the "confidently wrong
lab passes labcheck" case the repo warns about — and defect 1 proves the
risk was real, not theoretical. The quantifier evaluators are now extracted
to a named module-level block (`QUANT_EVAL_JS`) and `mathcheck.js` gained a
logic section: the six evaluators are checked exhaustively over all 512 3×3
grids for the theorem implication and the negation dualities, plus witness
correctness on the presets, and the propositional parser is checked on the
rows this course's lessons hinge on (vacuous truth, precedence of `¬`,
inclusive-or vs xor at TT, right-associativity of `→`). Every new assertion
was broken on purpose and observed to fail before being restored.

### 3. Lesson 1's lab used five connectives four lessons early (cognitive load; `propositions-and-truth-values`)

The first lesson's truth-table lab presets included `p -> q`, `p <-> q` and
`p ^ q` — three connectives the learner has not met (they arrive in lessons
2 and 4), presented with no gloss on the page where the learner has been
taught only what a proposition *is*. The lesson's own note says the lab
"appears here with a single variable on purpose"; the preset list
contradicted it. The presets are now `p`, `~p`, `p & q`, `p | q` — one
variable first, then two, so the 2ⁿ row-doubling the note points at is
visible — and the panel says plainly that the two-variable formulas are a
preview of lesson 2.

### 4. Small factual and framing repairs

- `nested-quantifiers` opened with "with one two-place predicate and two
  quantifiers there are four statements" — true only if the binding order is
  fixed as x-then-y, which is precisely the fixation the lesson exists to
  break. The prose now derives all six distinct forms and says why ∀∀ and ∃∃
  collapse.
- The `standard` for `nested-quantifiers` asked the learner to separate
  `∀x ∃y` from `∃x ∀y` — the mirrored pair, not the theorem pair. It now
  names `∃y ∀x`, matching the theorem the lesson proves, and asks for the
  boundary explanation of the successor preset as the second retrieval task.

## What it claims to teach and does — checked, no gap found

The course summary promises "the four proof techniques the rest of the path
uses": direct, contrapositive, contradiction, cases. All four are delivered
with a full worked proof each (`direct-proof`: divisibility transitivity;
`contraposition-and-contradiction`: n² even ⟹ n even, √2 irrational,
Euclid; `proof-by-cases-and-counterexample`: triangle inequality). Claims
verified during assessment: the √2 proof's use of "lowest terms" is honest
about where the contradiction lands; the Euclid presentation correctly
notes the proof is constructive as written; the `chords` count (31 regions
at n = 6) and `prime41` failure (1681 = 41²) are correct; the analysis
examples (continuity, uniform continuity) are correctly quantified.

## Where a learner still gets stuck — known limits, accepted

- Lessons 9 and 10 use ε-δ continuity as an example. For a beginner-level
  learner who has not met analysis this is decoration, not instruction; but
  both lessons carry a discrete example doing the real teaching first
  (`x + y = 0` over ℤ; the restricted-universal negation), the analysis
  example is framed as "where this pays off outside discrete mathematics",
  and the convergence exercise in lesson 10's `standard` is negatable purely
  mechanically — which is that lesson's whole point. Left as enrichment.
- Lesson 11 states the four quantifier inference rules compactly and defers
  their subtleties (fresh names, arbitrariness) to prose use in lessons
  12–14. The lesson's own note declares this choice. It is the right call at
  this level; a formal treatment belongs to the logic course the course
  summary explicitly declines to be.
- `direct-proof` and lesson 14 both use the induction lab in
  "verify-then-prove" mode before induction itself is taught (course 3).
  This is deliberate — the lab is used as a *checking* tool, and both
  lessons say checking is not proving — but a learner may wonder what the
  "step" text refers to. Acceptable: the step text is exactly the hook
  course 3 picks up.

## Structural verdict

No lessons added, removed, split, merged, reordered, or retitled. The
14-lesson sequence is pedagogically sound: propositional (1–7) →
quantifiers (8–10) → proof (11–14) is the correct dependency order, each
lesson carries one hard idea, and the course's URL space is unchanged. The
defects were in the instrument (the lab), its framing, and the absence of a
guard on its correctness — all repaired in place.
