# Pedagogy assessment — Logic and Proof (discrete mathematics, course 1)

Re-assessment, formed from the fourteen lesson dicts in
`content/discrete_math/c1_logic/` (`part_a.py`, `part_b.py`, `__init__.py`)
and the lab kit they render through (`scripts/mathpath/labs/logic.py`,
`scripts/mathpath/labs/induction.py`), as they stand on `main` at 0f21367,
before the prior assessment was opened. The delta against that document is
the last section.

This is a generated course: the source is the content package, and every
finding below cites a lesson slug and the field it lives in. Lessons, in
course order: `propositions-and-truth-values`, `logical-connectives`,
`truth-tables`, `conditional-statements`, `logical-equivalence`,
`tautologies-and-satisfiability`, `normal-forms-and-boolean-algebra`,
`predicates-and-quantifiers`, `nested-quantifiers`,
`negating-quantified-statements`, `rules-of-inference`, `direct-proof`,
`contraposition-and-contradiction`, `proof-by-cases-and-counterexample`.
This is course 1 of the path, so it is judged as the entry point: the path
promises "school algebra, and nothing beyond it" and "no calculus".

## What the course teaches well

- **Every lesson closes on an act, and the act is the right one.** The
  `standard` field of each lesson names something the reader does: sort ten
  sentences and give the reason each fails (`propositions-and-truth-values`);
  build an eight-row table without hesitating over the row pattern
  (`truth-tables`); reduce `¬(p ∨ (¬p ∧ q))` to `¬p ∧ ¬q` naming each law
  (`logical-equivalence`); settle a tautology claim by assuming it false
  (`tautologies-and-satisfiability`); build a grid where `∀x ∃y` holds and
  `∃y ∀x` fails (`nested-quantifiers`); negate a three-quantifier definition
  without thinking about its meaning (`negating-quantified-statements`); name
  the fallacy AND produce the row that breaks it (`rules-of-inference`);
  write a proof another person can check line by line (`direct-proof`); pick
  the technique from the shape of the claim
  (`contraposition-and-contradiction`); state, for any claim, what would
  refute it (`proof-by-cases-and-counterexample`). None of these is
  "understand X".
- **The labs are honest and adversarial by design.** The truth-table lab
  evaluates whatever the reader types, and in compare mode shows the
  separating row rather than a verdict — which is the definition of
  equivalence made visible (`logical-equivalence`). The quantifier lab
  evaluates all six two-variable forms from a grid the reader edits, and
  reports the witness or the counterexample rather than a bare T/F; its
  status text distinguishes a full column from a full row, which is exactly
  the confusion `nested-quantifiers` exists to correct. The lesson-9 and
  lesson-10 panel texts make specific, checkable predictions ("five of the
  six verdicts are true; press Complement and only `∃x ∃y` survives") and
  every one of them is right when recomputed by hand from the `le` and
  `diag` presets.
- **The worked example → practice arc is real in most lessons, and the
  worked examples are chosen to expose the error.** `predicates-and-quantifiers`
  writes the wrong translation beside the right one and explains why
  `∃x (P(x) → E(x))` is satisfied by `x = 9`; `nested-quantifiers` shows the
  witness `y = −x` and says that a witness mentioning `x` is the signature of
  a `∀∃` proof; `rules-of-inference` works the "test failed, therefore bug"
  argument to its counterexample row; `contraposition-and-contradiction`
  explains why the direct attempt on "`n²` even ⇒ `n` even" stalls, which
  is the actual reason to choose the contrapositive.
- **Misconceptions are named at the point of error, in the author's voice,
  and they are the real ones.** Reading `∨` as exclusive
  (`logical-connectives`); "unknown" as a third truth value
  (`propositions-and-truth-values`); rejecting vacuous truth and proving one
  direction of an iff (`conditional-statements`); negating both sides
  without flipping the connective (`logical-equivalence`); `∧` under `∀` and
  `→` under `∃` (`predicates-and-quantifiers`); the `x`-dependent witness
  for an `∃∀` claim (`nested-quantifiers`); "not all" read as "none"
  (`negating-quantified-statements`); validity confused with truth
  (`rules-of-inference`); assuming the conclusion and proving one case
  (`direct-proof`); the inverse offered as the contrapositive, and every
  indirect proof called "contradiction" (`contraposition-and-contradiction`);
  cases with a gap and WLOG without a symmetry
  (`proof-by-cases-and-counterexample`).
- **Prerequisite order inside the course is sound at the level of ideas**,
  with one exception noted below. Propositions → connectives → tables →
  conditional → equivalence → classification → normal forms → predicates →
  nesting → negation → inference → direct → indirect → cases. The course
  home's `how_to` states the two load-bearing dependencies (lesson 5 on
  tables, lesson 13 on the contrapositive) correctly, and later courses'
  back-references ("course 1 lesson 12's result", "course 1 lesson 5",
  "course 1 lesson 7") all point at lessons that teach what is cited.
- **The proofs are right.** Every in-body proof (contraposition theorem,
  `∃∀ ⟹ ∀∃`, quantifier negation, odd + odd, `a | b ∧ b | c ⟹ a | c`,
  `n²` even ⇒ `n` even, `√2` irrational, Euclid stated constructively,
  `n² + n` even by cases, the triangle inequality by cases) checks. So do
  the equivalence chains (`logical-equivalence`, `normal-forms-and-boolean-algebra`)
  and the assume-false derivation of modus tollens
  (`tautologies-and-satisfiability`). The remark that Euclid's argument as
  written is direct and constructive, not a contradiction, is correct and
  worth having.

## What it teaches badly, or claims and does not deliver

### Order: an idea used one lesson before it is taught

1. **`truth-tables` uses the conditional before `conditional-statements`
   defines it.** The lesson's only worked example is `p → (q ∨ r)`, and its
   `after` text points at the surprising row ("`p` is false, so the
   conditional is true regardless — lesson 4 explains why that convention
   is the right one"). The `standard` asks for the table of
   `(p → q) ∧ (q → r)`. Three of the eight lab presets contain `->`. The
   conditional's truth table is the one hard idea of lesson 4 — the lesson
   itself says it "looks wrong until you see why it must be that way" — and
   lesson 3 presents it as a fait accompli one page early. A reader who
   builds the worked table from the connectives they have been given cannot
   fill the last column. The fix is not to define `→` here (that is a second
   hard idea in a lesson whose hard idea is the systematic table); it is to
   work a three-variable example in `¬ ∧ ∨ ⊕` and let lesson 4 own its row.

### The entry point assumes calculus the path says it does not

2. **`conditional-statements`'s completion standard cannot be met by the
   stated audience.** "Given 'if a function is differentiable then it is
   continuous', produce the converse, inverse and contrapositive, and
   identify which are true." Producing the three forms is the lesson's act;
   identifying which are true requires knowing that differentiable ⇒
   continuous and that `|x|` refutes the converse, which is a calculus fact
   in a course whose home says "school algebra is enough" and whose path
   says "no calculus". The same lesson's body already has a perfectly good
   number-theory instance (`4 | n ⇒ 2 | n`).
3. `nested-quantifiers` (an `example` block and the `note`) and
   `negating-quantified-statements` (the worked example, quiz question 3,
   the standard) use continuity, uniform continuity, differentiability and
   sequence convergence. These are defensible: lesson 10's whole claim is
   that the mechanism works *without* consulting the meaning, and the
   continuity definition is the canonical demonstration of that. They are
   asides and a reader can do the act without the calculus. Recorded, not
   repaired; the course home should say that they are asides.

### Facts a reader would trust that are wrong

4. **`tautologies-and-satisfiability`: "For a formula with 100 variables …
   that is more rows than there are atoms in the observable universe."**
   `2¹⁰⁰ ≈ 1.3 × 10³⁰`; the usual estimate for atoms in the observable
   universe is `~10⁸⁰`. The claim is off by fifty orders of magnitude. It
   becomes true at around 270 variables.
5. **`normal-forms-and-boolean-algebra`, mistake 2: "The canonical DNF of a
   formula true in seven of eight rows has seven terms; an equivalent
   one-term formula may exist."** A single term (a conjunction of literals
   in three variables) is true in 1, 2, 4 or 8 rows, never 7, so no
   one-term DNF exists for that formula. The true and sharper point is that
   the same formula is `¬p ∨ ¬q ∨ ¬r` — three literals — so canonical and
   small are different goals.
6. **`predicates-and-quantifiers`, the domain definition: "`∀x (x² ≥ 0)` is
   true over the reals and false over the complex numbers."** `≥` is not a
   relation on `ℂ`; the statement is not false there, it is ill-formed. The
   lesson is teaching that the domain is part of the statement and picks an
   example where the predicate itself stops making sense. A clean instance
   that needs nothing beyond arithmetic: `∀x (x² ≥ x)` is true over `ℤ` and
   false over `ℝ` (`x = ½`).

### Distractors that are also true

The recurring failure the content package's own `AGENTS.md` warns about.
The quiz shows one explanation for every wrong answer, so a distractor that
is defensible is marked wrong with an explanation that does not address it.

7. **`logical-equivalence`, question 2: "You want to disprove `A ≡ B`. What
   is enough?"** Option (d), "Show `A` is a tautology and `B` is not", *is*
   enough: if `B` has a false row, that row separates them. The `why` says
   "Nothing more is needed or helps", which is wrong about (d).
8. **`predicates-and-quantifiers`, question 2: "How do you refute
   `∀x P(x)`?"** Option (a), "Show `P(x)` fails for every `x`", refutes it
   over any non-empty domain, and the `why` concedes as much ("proves
   something stronger than needed"). A reader who chose (a) has not made an
   error the lesson wants to correct.

### Objectives and practice that do not match

9. **`direct-proof`'s lab promises a proof the lesson never gives.** The
   panel says "Before proving `n³ − n` is divisible by 6, look at it … the
   proof is what covers the rest, and this lesson is about writing that
   proof." The lesson proves odd + odd is even and transitivity of
   divisibility, and asks the reader to prove odd ⇒ odd square. `6 | n³ − n`
   is never proved, here or anywhere in the course — and it cannot be
   proved by the lesson's technique without a case split, which is lesson
   14. The lab is the right lab (look before you prove; a table is
   evidence, not a proof) attached to a false promise.
10. **The course home's `how_to` says "The last four lessons each end with a
    claim to prove yourself."** Two do (`direct-proof`,
    `contraposition-and-contradiction`). `rules-of-inference` ends with an
    argument to check, and `proof-by-cases-and-counterexample` ends with a
    habit ("state what would refute it") and no claim.
11. **`tautologies-and-satisfiability`'s quiz does not test the lesson's
    act.** The standard is "settle a tautology claim by assuming it false";
    the worked example demonstrates exactly that; no quiz question asks the
    reader to do it. Question 3 tests the NP-completeness aside instead.
12. **`normal-forms-and-boolean-algebra`'s named mistake is never
    drilled.** "Getting the polarity backwards in CNF" is mistake 1 and the
    method's step 3 says it "is the standard slip"; the quiz asks about the
    DNF term count, functional completeness and SAT-solver input, and never
    once asks the reader to write a clause from a false row.
13. **`logical-equivalence`'s lab panel promises a refutation it does not
    hand the reader.** "No highlighted row means equivalent; one is a
    complete disproof" — but every preset pair in the list is equivalent.
    The non-equivalent pair the course has been warning about since lesson
    2 (`~(p & q)` against `~p & ~q`) is available in the dropdowns and the
    panel does not point at it.

### Cognitive load

14. **`predicates-and-quantifiers`'s lab is lesson 9's lab.** The lesson
    teaches one-variable `∀` and `∃`; the lab it ships evaluates the six
    two-variable forms, and the panel opens with "cell `(x, y)` says whether
    `P(x, y)` holds". A reader meets `∀x ∃y` and `∃y ∀x` — the subject of
    the next lesson, and the course home's own headline hazard — before
    the lesson that separates them. The lab is fine; the panel needs to
    tell the reader which two of the six lines are this lesson's.
15. **`contraposition-and-contradiction` carries two techniques.** By the
    one-hard-idea rule it is the strongest split candidate in the course. I
    have chosen not to split it: the lesson's third concept, its second
    mistake and its third quiz question are all about the *contrast* between
    the two ("a proof that assumes `p ∧ ¬q` and derives `¬p` is
    contraposition with extra steps"), the retrieval practice covers both,
    and each has a full in-body proof. The contrast is the content, and it
    would be lost across a page boundary. Recorded as a judgement, not an
    oversight.
16. `rules-of-inference` is the heaviest page: validity and soundness,
    eight propositional rules, two fallacies, four quantifier rules with
    side conditions, and a resolution aside. The quantifier rules are what
    lesson 12's "arbitrary" rests on and cannot move later; the resolution
    paragraph could go. Left as is: the quiz and standard stay on the
    fallacies, which is the right target.
17. `normal-forms-and-boolean-algebra` looks like three ideas (DNF/CNF,
    functional completeness, gates) and is one: the theorem "every truth
    table has a DNF" *is* the proof that `{∧, ∨, ¬}` is complete, and the
    hardware paragraph is the same algebra relabelled. Not split.

### The shared lab speaks two courses ahead

18. **`direct-proof` and `proof-by-cases-and-counterexample` use the
    `induction` lab, whose status and note text are written for course
    3.** Every statement prints an "Inductive step:" line, and the status
    banner says "This is why induction proves the STEP rather than checking
    cases" and "it turns `P(k)` into `P(k+1)` for EVERY `k`". A course-1
    reader has not met induction, `P(k)` or a step. The lesson-14 `note`
    already says course 3 is where that vocabulary lives, which makes it
    tolerable there; lesson 12 says nothing. The kit belongs to
    `lab-arithmetic` and is shared with course 3, so the repair here is in
    the panel text of both lessons. A kit-level option to suppress the
    step note for course-1 use is the right fix and is out of this course's
    scope.

### Smaller

19. `propositions-and-truth-values`'s body says "Three kinds of sentence
    fail this definition" and lists three; the method, the mistakes and the
    standard all count four ("not declarative, open, self-referential, or
    vague"). The fourth exclusion never appears in the material it is
    supposedly drawn from.
20. `conditional-statements`, mistake 1 is titled "Affirming the converse".
    The lesson defers the name to lesson 11, which calls it affirming the
    consequent; the invented phrase in between helps nobody.

## Where a learner gets stuck

- At `truth-tables`' worked example, on the last column, if they try to
  build it from the connectives they have (item 1).
- At `conditional-statements`' standard, at "identify which are true"
  (item 2).
- At `predicates-and-quantifiers`' lab, on the four mixed lines of the
  verdict table (item 14).
- At `direct-proof`'s lab, waiting for the proof of `6 | n³ − n` that the
  panel promised and the page does not contain (item 9), and at its
  "Inductive step" line (item 18).
- At `logical-equivalence` question 2, having chosen (d) for a correct
  reason and been told nothing else helps (item 7).

## Repairs made in this pass

All within the existing URL space; no lesson added, removed, renamed or
reordered. Every edit is in `content/discrete_math/c1_logic/` and the pages
are rebuilt from it.

- `truth-tables`: worked example rebuilt around `¬p ∨ (q ∧ r)` — three
  variables, two subexpression columns, only connectives from lessons 1–2 —
  with the `after` text pointing forward to lesson 4, where the reader will
  meet a connective whose column is exactly this one; the standard changed
  to `(p ∨ q) ∧ ¬(q ∧ r)`; the three `->` lab presets replaced by formulas
  in `¬ ∧ ∨ ⊕` including the worked one. The lab still accepts `->` in the
  typed field, and lesson 4's lab is where it is used.
- `conditional-statements`: standard now uses "if `n` is a multiple of 10
  then `n` is a multiple of 5", whose three relatives the reader can settle
  with `n = 15`; mistake 1 retitled.
- `tautologies-and-satisfiability`: the atoms claim now uses 300 variables;
  a fourth quiz question asks for the assignment that shows
  `(p ∨ q) → (p ∧ q)` is not a tautology, with the three distractors each
  being a row where the conditional is true.
- `normal-forms-and-boolean-algebra`: mistake 2 corrected (`¬p ∨ ¬q ∨ ¬r`,
  three literals); a fourth quiz question asks for the clause that rules
  out the row `p = T, q = F`, with distractors that are the wrong-polarity
  clause, the DNF term for that row, and the term for the wrong row.
- `logical-equivalence`: question 2's option (d) replaced by "Show that `A`
  and `B` are both contingent", which does not refute anything; the `why`
  now says why; the lab panel points at `~(p & q)` against `~p & ~q`.
- `predicates-and-quantifiers`: the domain example replaced by
  `∀x (x² ≥ x)` over `ℤ` and `ℝ`; question 2's option (a) replaced by
  "Show that nobody has proved it", the lesson-1 misconception; the lab
  panel now tells the reader to read only `∀x ∀y` and `∃x ∃y` — the two
  quantifiers of this lesson applied to pairs — and that the four mixed
  lines are lesson 9's.
- `direct-proof`: the lab panel no longer promises a proof; it says the
  direct attempt on `6 | n³ − n` stalls at "one of three consecutive
  integers is a multiple of 3", that this is a case split and lesson 14's
  business, and that the lab's "inductive step" line is course 3's
  vocabulary and can be ignored for now.
- `proof-by-cases-and-counterexample`: the standard now ends with a claim
  to prove — `3 | n³ − n` for every integer, by cases `n = 3k, 3k + 1,
  3k + 2` on the factorisation `(n − 1) n (n + 1)` — closing the claim
  lesson 12's lab opened; the lab panel names the "inductive step" line as
  course 3's.
- `propositions-and-truth-values`: the body now lists four exclusions,
  with vagueness as the fourth, so the material matches the method.
- Course home (`__init__.py`): `how_to` item 3 rewritten to say what is
  true — lesson 11 ends with an argument to check and lessons 12 to 14 each
  end with a claim to prove; `assumes_long` and a new sentence in
  `how_to` say that the continuity and convergence examples in lessons 9
  and 10 are asides the reader can negate without knowing what they mean.

## Delta against the prior assessment

Written after the above, on reading `docs/pedagogy/prior/logic-and-proof.md`
and the diff of 425fbec.

**Its repairs are live and I do not dispute any of them.** The six-form
quantifier lab with witness/counterexample per line, the `diag` default on
`nested-quantifiers` with the successor preset turned into a retrieval task
about truncated domains, the `le` default on
`negating-quantified-statements` with the Complement prediction, the
six-forms derivation in lesson 9's prose, the corrected theorem pair in
lesson 9's standard, the lesson-1 preset trim, and the `mathcheck.js` logic
section are all present. I recomputed every verdict the two panel texts
predict from the `le` and `diag` grids by hand and they are right. The
headline finding — a lab evaluating a full row while its status reasoned
about a full column — was real, and it was the most consequential defect
in the course.

**What it claimed that I dispute.**

- "Each lesson carries one hard idea." `contraposition-and-contradiction`
  carries two by its own account (item 15), and `rules-of-inference` carries
  the propositional rules and the quantifier rules with side conditions
  (item 16). I reach the same structural verdict — no split — but for a
  stated reason, not because the load is single.
- "As course 1 of the path it may assume nothing, and it doesn't."
  `conditional-statements`' completion standard requires knowing that
  differentiability implies continuity and not conversely (item 2). The
  prior noticed the analysis examples in lessons 9 and 10 and accepted
  them as enrichment, which I agree with; it did not notice that lesson 4
  makes the calculus load-bearing.
- "Quiz with per-error feedback." The quiz machinery
  (`labs/common.py`, `QUIZ_SCRIPT`) shows one `why` per question for every
  wrong answer. The explanations in this course are good — most name the
  distractors — but it is per-question feedback, and where a distractor is
  defensible (items 7, 8) the reader is told nothing about their reasoning.
- "The prerequisite chain inside the course is sound … Truth tables
  (lesson 3) precede equivalence (5)." True, and lesson 3 also precedes the
  conditional (4) while using it in its worked example, standard and lab
  presets (item 1). The prior caught this exact class of defect in
  lesson 1's lab presets and repaired it; the same defect one page later,
  in the worked example rather than a dropdown, was not seen.
- On the induction lab in lessons 12 and 14: "a learner may wonder what the
  'step' text refers to. Acceptable: the step text is exactly the hook
  course 3 picks up." Acceptable in lesson 14, whose `note` says so; not in
  lesson 12, which says nothing and whose panel promises a proof of the
  lab's statement that the lesson does not contain (items 9, 18).

**What it missed entirely.** The `2¹⁰⁰`-versus-atoms claim (item 4); the
impossible one-term DNF (item 5); `≥` over `ℂ` (item 6); the two distractors
that are also true (items 7, 8), which are the failure the content
package's own `AGENTS.md` names as recurring; the unfulfilled lab promise in
`direct-proof` (item 9); the course home's inaccurate "last four lessons
each end with a claim" (item 10); the quizzes in lessons 6 and 7 that never
test the lesson's act or its named mistake (items 11, 12); the
equivalence lab whose every preset pair is equivalent (item 13); the
nested-quantifier lab landing on lesson 8 unexplained (item 14) — which the
prior's own repair made more visible, since the lab now shows six forms
instead of four; and the three-versus-four exclusions in lesson 1 (item 19).

**Its verification claim stands.** "Verdicts on the quantifier lab were
checked by brute force over every 3×3 predicate grid" — `mathcheck.js`
does this, and it is the right guard for a lab whose failure mode is a
confidently wrong verdict.
